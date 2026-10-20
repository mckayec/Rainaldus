// Pure reading-guide rules shared by the UI and regression checks.
export function incomingConnections(books) {
  const incoming = {};
  for (const b of Object.values(books)) for (const c of b.connections || []) {
    (incoming[c.target] ||= []).push({ ...c, from: b.id });
  }
  return incoming;
}
export function seriesPrerequisites(books, id) {
  const result = new Set();
  function visit(key) {
    for (const prior of books[key]?.requiredBefore || []) {
      if (!result.has(prior)) { result.add(prior); visit(prior); }
    }
  }
  visit(id);
  return [...result].filter(key => books[key]).sort((a, b) =>
    (books[a].sorting?.order || 0) - (books[b].sorting?.order || 0));
}
export function recommendedBackground(incoming, id) {
  return (incoming[id] || []).filter(c => ['major', 'significant'].includes(c.type)
    && !['development', 'retelling', 'shared-narrator'].includes(c.relation));
}
