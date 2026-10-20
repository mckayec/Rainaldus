# Rainaldus

An unofficial interactive guide to Brandon Sanderson's Cosmere. Open the star map, follow a suggested reading path, track progress, and reveal source-backed connection cards.

## Reading guidance

Series sequence is separate from optional crossover background. Prime novels and other noncanonical drafts are hidden by default; enable **Noncanonical drafts & Prime novels** and **Easter eggs** to explore development history. Announced books have a separate toggle. *The Fires of December* has public-preview coverage only in this research snapshot.

New connection cards include citations, chapter/section locators, original explanatory diagrams, and selected short excerpts. Official artwork is linked with credits. Evidence stays behind spoiler reveals. Existing source notes are labeled as imported, not independently reverified.

## Run locally

```sh
python3 -m http.server -d site 8000
```

Visit http://localhost:8000. Reading progress uses the existing `cro.*` localStorage keys. Existing optional Claude account sync is preserved.

## Update and verify content

**Read [AGENTS.md](AGENTS.md), [Claude handoff](docs/CLAUDE_HANDOFF.md), and [research notes](docs/COSMERE_RESEARCH.md) first.**

- `data/upstream.json`: pinned 17th Shard input; retain its MIT notice in `data/LICENSE` and deployed `site/DATA-LICENSE.txt`.
- `data/curation.json`: editable local research, corrections, sources, series sequence and additions.
- `site/data.json`: generated combined output; do not edit directly or replace with an upstream-only export.

```sh
python3 scripts/build_data.py
python3 -m unittest discover -s tests
node --test tests/guide.test.mjs
```

The generator also accepts an explicit upstream path and output path: `python3 scripts/build_data.py upstream.json site/data.json`. It always applies the local overlay. When refreshing upstream, reconcile duplicates rather than discarding the local notes. CI checks source preservation and deterministic regeneration.

## Deploy

`.github/workflows/pages.yml` publishes `site/` on pushes to `main`. Set **Settings → Pages → Source: GitHub Actions** once. The research PR does not merge or deploy automatically.

## Credits and limits

Original book data: [17th Shard reading order](https://github.com/17thshard/reading-order), MIT, © 2019 Marvin Rösch. Additional research links to Sanderson, Dragonsteel and Coppermind. Original diagrams illustrate claims; they are not official art or independent evidence. Quoted text and linked artwork remain the property of their respective creators. This is a selected guide, not an exhaustive concordance.
