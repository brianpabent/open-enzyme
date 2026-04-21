# reference/ — Canonical read-only material

This directory holds canonical source material that the sweep daemon **reads but never modifies**.

## What goes here

- **Published papers** — PDFs, markdown transcripts, or extracted text of peer-reviewed research.
- **External reports** — FDA filings, trial registries, third-party market data.
- **Vendor data** — manufacturer specifications, strain catalogs, regulatory documents.
- Anything authored outside this project that should be cited as-is.

## reference/generated/

Output from scripts and analysis programs goes here. These are machine-produced artifacts (sequence alignments, protein structures, docking scores, BLAST hits, etc.) that should be treated as reference material — consumed by the docs, not rewritten by them.

If a program's output needs to be updated, re-run the program. Do not edit the output in place.

## Rules (enforced by `scripts/sweep-prompt.md`)

- The daemon never writes to any file under `reference/`.
- If the sweep is triggered by a file under `reference/` (which shouldn't happen — `wiki-watch.sh` doesn't watch this directory), the daemon aborts with a logged note.
- Docs in `docs/` may cite files here with standard provenance: `(source: reference/<path>)`.

## What does NOT go here

- Living research notes → `docs/`
- Derived concept pages → `wiki/`
- Daemon synthesis output → `ai-analysis/`

If you're not sure whether something is "canonical" or "living," the test is: *can I imagine the daemon rewriting this next week when new findings land?* If yes → `docs/`. If no → `reference/`.
