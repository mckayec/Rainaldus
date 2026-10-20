# Claude Code handoff

Read and follow `AGENTS.md`, `docs/CLAUDE_HANDOFF.md`, and `docs/COSMERE_RESEARCH.md` before edits. The user explicitly requested this shared research to survive future Claude work.

Book content lives in `data/curation.json`, layered over pinned `data/upstream.json`. Run `python3 scripts/build_data.py` to regenerate `site/data.json`. An upstream-only regeneration loses reviewed additions and must not replace the combined output. Run the Python and Node regression checks listed in `AGENTS.md` before committing.

Keep stable IDs (`iote`, `sa5`, `elsecaller`, `lopen`, `dsp`, `twokp`, new `fod`) so saved reading progress remains valid. Preserve the separation of series prerequisites, optional crossovers, preview-only connections and noncanonical development history.
