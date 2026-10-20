"""Offline, reproducible upstream import plus reviewed local additions.

Never edit site/data.json by hand. Put corrections in data/curation.json.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
def fix_href(value):
    return re.sub(r"href='([^'>]*)>", r"href='\1'>", value) if value else value

def build(source, overlay):
    books, worlds = {}, []
    def walk(node, world, group, ids):
        if 'title' in node:
            b = copy.deepcopy({k: v for k, v in node.items() if k not in ('title2', 'padding')})
            b['connections'] = b.pop('connections:', b.get('connections', []))
            for key in ('world', 'system', 'publication', 'chronology', 'au', 'link'):
                if key in b: b[key] = fix_href(b[key])
            for item in b['connections'] + b.get('appearances', []):
                if 'description' in item: item['description'] = fix_href(item['description'])
            b.update(worldName=world, group=group)
            books[b['id']] = b
            ids.append(b['id'])
        else:
            for child in node.get('children', []): walk(child, world, group, ids)
    def plain(value): return re.sub(r'<[^>]+>', '', (value or '').replace('<br>', ' ')).strip()
    for w in source['books']:
        wd = dict(name=plain(w['label']), color=w['color'], groups=[])
        for group in w['children']:
            ids = []
            label = plain(group.get('label'))
            walk(group, wd['name'], label, ids)
            wd['groups'].append(dict(label=label, books=ids))
        worlds.append(wd)
    for key, patch in overlay['books'].items():
        if key not in books:
            books[key] = dict(id=key, connections=[], appearances=[])
            books[key].update(copy.deepcopy(patch))
            world = next(w for w in worlds if w['name'] == patch['worldName'])
            world['groups'][0]['books'].append(key)
        else:
            books[key].update(copy.deepcopy(patch))
    for key, ids in overlay['requiredBefore'].items(): books[key]['requiredBefore'] = ids
    for patch in overlay.get('connectionPatches', []):
        current = next(c for c in books[patch['from']]['connections'] if c['target'] == patch['target'])
        current.update({k: v for k, v in patch.items() if k not in ('from', 'target')})
    for record in overlay['connections']:
        c = copy.deepcopy(record)
        origin = c.pop('from')
        if any(x['target'] == c['target'] for x in books[origin]['connections']):
            raise ValueError(f'Duplicate connection: {origin} -> {c["target"]}; reconcile upstream and curation')
        books[origin]['connections'].append(c)
    data = {k: copy.deepcopy(source[k]) for k in ('connections', 'layers', 'appearances')}
    data.update(books=books, worlds=worlds, sources=overlay['sources'],
                provenance=overlay['provenance'], researchAsOf=overlay['reviewedAt'])
    for b in books.values():
        for c in b['connections']:
            if c['target'] not in books: raise ValueError(f'Unknown connection target: {c["target"]}')
            if not c.get('sources'):
                urls = list(dict.fromkeys(re.findall(r"href=['\"](https?://[^'\"]+)", c.get('description', ''))))
                c['sources'] = []
                for url in urls:
                    key = 'legacy-' + hashlib.sha256(url.encode()).hexdigest()[:12]
                    data['sources'][key] = dict(url=url, label='Reference from 17th Shard notes', kind='inherited',
                                                locator='See linked article; original notes retain any chapter references.')
                    c['sources'].append(key)
                if not c['sources']:
                    key = 'upstream-data'
                    data['sources'][key] = dict(url='https://github.com/17thshard/reading-order/blob/c1fdba7c45b598d622493c9b9396226611367926/public/data.json', label='Original 17th Shard data', kind='inherited', locator='Imported connection record; no more precise citation supplied upstream.')
                    c['sources'].append(key)
                c['evidence'] = 'inherited'
    return data

def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'data/upstream.json'
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / 'site/data.json'
    data = build(json.loads(src.read_text()), json.loads((ROOT / 'data/curation.json').read_text()))
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(data["books"])} works; {sum(len(b["connections"]) for b in data["books"].values())} connections')

if __name__ == '__main__': main()
