# Accuracy and research handoff — 2026-10-19

The user requested accuracy fixes, research on recent works, optional Prime-novel connections, richer evidence callouts, and safeguards against accidental overwrites.

## Ownership and regeneration

- Pinned upstream input: `data/upstream.json` from 17thshard/reading-order at c1fdba7c45b598d622493c9b9396226611367926.
- Editable research: `data/curation.json`. Book patches, an explicit series-reading graph, new connections, metadata-only patches to inherited connections, source registry and review date.
- Generated output: `site/data.json`. Regenerate offline with `python3 scripts/build_data.py`. Do not edit output directly.
- UI integration: `site/guide.mjs` plus evidence/reading-sequence sections in `site/index.html`. Preserve these when redesigning the UI.
- Verification: `python3 -m unittest discover -s tests`; `node --test tests/guide.test.mjs`. Optional browser check: `python3 tests/browser_check.py` (requires Playwright and `/usr/bin/chromium`; uses a loopback-only server). Data tests preserve all 82 upstream works and 93 original connections. The CI workflow runs these and rejects stale generated output. Checks exist; making them required in GitHub branch rules is an owner setting.

## Invariants

1. Saved progress uses stable IDs and existing `cro.*` localStorage keys. Do not rename IDs or clear progress during a migration.
2. Crossovers are optional context. Series sequence is a separate transitive graph. Side stories are recommended after their parent novel for spoiler safety, but do not block later main novels.
3. Prime drafts are noncanonical and opt-in. Same names and reused concepts do not establish canonical identity or history.
4. The Fires of December is published (backer release September 15, 2026; public digital October 6). It must appear with planned books hidden and support marking read. Connection research remains limited to public preview / official series-grouping claims until a full-book audit. Do not confuse evidence coverage with publication status.
5. Inline visuals are original explanatory diagrams, not official art or evidence. Publisher art is linked with credits, not copied into the project.
6. All evidence content is spoiler-gated. Do not put a connection's secret identity in an unrevealed title, image alt text, tooltip or preload.
7. New claims remain a selected collection, not a complete concordance. Preserve coverage labels. Imported notes retain their original wording and ratings; no independent claim-by-claim endorsement is implied.

## Merging alongside ongoing work

Merge this PR into the branch Claude is using (or merge/rebase its branch onto main after this PR lands). Read these notes first. If upstream adds a connection already curated here, the builder intentionally fails on the duplicate; reconcile sources and notes in the overlay rather than deleting the local research silently. Git history and CI make changes visible but cannot prevent another agent from ignoring instructions.
