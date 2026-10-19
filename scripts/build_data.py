import json, sys, re
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src))
books, worlds = {}, []
def strip(s): return re.sub(r'<[^>]+>', '', s or '').strip()
def fix_href(s):
    # repair links missing their closing quote: href='...>  -> href='...'>
    return re.sub(r"href='([^'>]*)>", r"href='\1'>", s) if s else s
def walk(n, world, group):
    if 'title' in n:
        b = {k: n[k] for k in ('id','title','series','world','system','publication','chronology','categories','appearances','connections','au','link','sorting') if k in n}
        if 'connections:' in n: b['connections'] = n['connections:']
        for k in ('world','system','publication','chronology','au','link'):
            if k in b: b[k] = fix_href(b[k])
        for c in b.get('connections', []): c['description'] = fix_href(c.get('description',''))
        for a in b.get('appearances', []):
            if 'description' in a: a['description'] = fix_href(a['description'])
        b['worldName'] = world
        b['group'] = group
        books[b['id']] = b
        group_books.append(b['id'])
        return
    for c in n.get('children', []):
        walk(c, world, group)
for w in d['books']:
    wd = {'name': strip((w['label'] or '').replace('<br>', ' ')), 'color': w['color'], 'groups': []}
    for g in w['children']:
        group_books = []
        label = strip((g.get('label') or '').replace('<br>', ' '))
        walk(g, wd['name'], label)
        wd['groups'].append({'label': label, 'books': group_books})
    worlds.append(wd)
# --- data corrections (Oct 2026) ---
i = books['iote']
i['title'] = 'Isles of the Emberdark'
i['publication'] = 'September 2025'
i['categories'] = ['no-series', 'novel', 'phase3', 'published']
i['sorting'] = {'order': 3.13, 'publication': 2025.09, 'chronology': 13.02}
books['sa5.5']['title'] = 'Horneater'
books['sa5.5']['publication'] = books['sa5.5'].get('publication') or 'Planned for 2026'
books['sa5.5']['categories'] = ['stormlight', 'novella', 'unpublished', 'forthcoming']
# verify connections
for b in books.values():
    b['connections'] = [c for c in b.get('connections', []) if c['target'] in books]
data = {
  'connections': d['connections'],
  'layers': d['layers'],
  'appearances': d['appearances'],
  'worlds': worlds,
  'books': books,
}
json.dump(data, open(out, 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(books), 'books', sum(len(b['connections']) for b in books.values()), 'connections')
print('published', sum('published' in b['categories'] for b in books.values()))
print({b['id']: b.get('publication') for b in books.values() if b['id'] in ('sa5.5','sa5','iote')})
