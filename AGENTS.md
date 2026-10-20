# Collaboration rules for this repository

Read `docs/COSMERE_RESEARCH.md` and `docs/CLAUDE_HANDOFF.md` before changing book data or guide rules. These files document the user's requested accuracy work.

- `data/upstream.json` is a pinned 17th Shard input; `data/curation.json` contains reviewed local additions. `site/data.json` is generated. Never replace it with an upstream-only export or hand-edit it.
- Run `python3 scripts/build_data.py`, `python3 -m unittest discover -s tests`, and `node --test tests/guide.test.mjs` after data/UI changes. Preserve source parity, citations, existing stable IDs and localStorage keys.
- Series prerequisites are separate from optional crossover strength. Noncanonical drafts are opt-in and never become canon prerequisites. Public-preview coverage is not full-book coverage.
- Preserve this curation layer and the evidence UI when redesigning. Reconcile competing research using dated sources rather than discarding either agent's work. Do not force-push over another agent's branch.
- New connection claims need a source URL, a chapter/section locator (or an explicit unresolved-location note), an evidence label and a continuity/relation type. Keep spoilers, diagrams, excerpts and art links behind reveals. Do not present illustrations as textual evidence.
