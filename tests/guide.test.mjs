import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { incomingConnections, seriesPrerequisites, recommendedBackground } from '../site/guide.mjs';
const data = JSON.parse(readFileSync(new URL('../site/data.json', import.meta.url)));
const books = data.books;
const incoming = incomingConnections(books);
test('Series prerequisites exist even without crossover edges', () => {
  assert.deepEqual(seriesPrerequisites(books, 'mb2'), ['mb1']);
  assert.deepEqual(seriesPrerequisites(books, 'sa5'), ['sa1','sa2','sa3','sa4']);
  assert.deepEqual(seriesPrerequisites(books, 'mb7'), ['mb1','mb2','mb3','mb4','mb5','mb6']);
});
test('Side stories need context but never block the next main novel', () => {
  assert.ok(seriesPrerequisites(books, 'lopen').includes('sa2'));
  assert.ok(!seriesPrerequisites(books, 'sa3').includes('lopen'));
  assert.ok(!seriesPrerequisites(books, 'sa4').includes('sa3.5'));
});
test('Prime drafts, retellings and shared narration do not become prerequisites', () => {
  assert.deepEqual(seriesPrerequisites(books, 'sa1'), []);
  assert.deepEqual(seriesPrerequisites(books, 'iote'), []);
  assert.ok(!recommendedBackground(incoming,'sa1').some(c=>['dsp','twokp'].includes(c.from)));
  assert.ok(!recommendedBackground(incoming,'iote').some(c=>c.from==='sotd'));
});
test('Reverse connections keep sources, evidence and visuals', () => {
  const c=incoming.sa1.find(c=>c.from==='dsp');
  assert.ok(c.sources.includes('bridge-origin'));
  assert.equal(c.relation,'development');
  assert.ok(c.visual.label);
});

test('Theories never become recommended background, and nested evidence survives reversal', () => {
  const sample = {fod:[{from:'sa1',type:'significant',evidence:'theory'}, {from:'wb',type:'significant',evidence:'documented',relation:'shared-character'}]};
  assert.deepEqual(recommendedBackground(sample,'fod').map(c=>c.from), ['wb']);
  const vasher = incoming.fod.find(c=>c.from==='wb');
  assert.equal(vasher.claims[0].evidence,'author-confirmed');
  assert.ok(vasher.claims.some(c=>c.evidence==='theory'));
});
