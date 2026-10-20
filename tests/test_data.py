import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_data', ROOT/'scripts/build_data.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
source = json.loads((ROOT/'data/upstream.json').read_text())
overlay = json.loads((ROOT/'data/curation.json').read_text())
data = module.build(source, overlay)
books = data['books']

class DataChecks(unittest.TestCase):
    def test_generated_file_matches_sources(self):
        self.assertEqual(data, json.loads((ROOT/'site/data.json').read_text()))

    def test_upstream_books_and_connections_survive(self):
        originals = {}
        def walk(n):
            if 'title' in n: originals[n['id']] = n
            for child in n.get('children', []): walk(child)
        for node in source['books']: walk(node)
        self.assertEqual(len(originals), 82)
        self.assertTrue(set(originals) <= set(books))
        total = 0
        for key,b in originals.items():
            for c in b.get('connections:', b.get('connections', [])):
                total += 1
                matches = [x for x in books[key]['connections'] if x['target']==c['target'] and x['type']==c['type']]
                self.assertEqual(len(matches),1)
                self.assertEqual(matches[0]['description'], module.fix_href(c.get('description','')))
        self.assertEqual(total, 93)

    def test_references_and_world_membership(self):
        membership = [key for world in data['worlds'] for group in world['groups'] for key in group['books']]
        self.assertCountEqual(membership, books)
        categories = {c['id'] for layer in data['layers'] for c in layer['categories']}
        for key,b in books.items():
            self.assertEqual(b['id'],key)
            self.assertTrue(set(b['categories']) <= categories)
            for prior in b.get('requiredBefore',[]): self.assertIn(prior,books)
            for ref in b.get('sources',[]): self.assertIn(ref,data['sources'])
            for c in b['connections']:
                self.assertIn(c['target'],books)
                self.assertNotEqual(key,c['target'])
                self.assertTrue(c['sources'])
                for ref in c['sources']: self.assertIn(ref,data['sources'])
        for ref in data['sources'].values(): self.assertTrue(ref['url'].startswith('https://'))

    def test_curated_claims_have_evidence(self):
        ids=[]
        for c in overlay['connections']:
            ids.append(c['id'])
            self.assertTrue(c['locator'])
            self.assertTrue(c['sources'])
            self.assertTrue(c['visual']['left'])
            self.assertTrue(c['visual']['right'])
            if c.get('excerpt'): self.assertIn(c['excerpt']['source'],data['sources'])
            self.assertIn(c['evidence'],['documented','preview'])
            if c['from'] in ['dsp','twokp','jasnah']:
                self.assertEqual(c['relation'],'development')
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(len(ids),21)

    def test_dates_and_canon_boundaries(self):
        self.assertTrue(books['iote']['publication'].startswith('July 1, 2025'))
        self.assertNotIn('publication',books['sa5.5']['sorting'])
        self.assertNotIn('published',books['fod']['categories'])
        self.assertNotIn('chronology',books['fod']['sorting'])
        for key in ['dsp','twokp','wsp','aon']:
            self.assertIn('apocryphal',books[key]['categories'])
            self.assertNotIn('published',books[key]['categories'])
        self.assertEqual(books['elsecaller']['authors'],['Brandon Sanderson','Dan Wells'])
        self.assertEqual(books['lopen']['authors'],['Brandon Sanderson','Isaac Stewart'])
        self.assertNotIn('sa2.5',books['sa3']['requiredBefore'])
        self.assertNotIn('sa3.5',books['sa4']['requiredBefore'])

    def test_prerequisite_graph_has_no_cycles(self):
        def visit(key,trail):
            self.assertNotIn(key,trail)
            for prior in books[key].get('requiredBefore',[]): visit(prior,trail+[key])
        for key in books: visit(key,[])

    def test_future_upstream_collision_requires_reconciliation(self):
        changed=copy.deepcopy(overlay)
        changed['connections'].append(dict(changed['connections'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate connection'):
            module.build(source,changed)

if __name__=='__main__': unittest.main()
