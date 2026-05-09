# Synthesis — action queue and history

This directory holds the action queue and history of the wiki sweep daemon (`scripts/sweep-1-propagate.py`, `scripts/synthesize.py`, `scripts/sweep-3-review.py`, plus `scripts/synthesis-emit-files.py` which writes per-item files here). It is **project-management content, not science.** Research findings live in [`wiki/`](../wiki/).

## Subdirectory map

| Directory | Purpose | Writer |
|---|---|---|
| [`queue/`](./queue/) | Pending items the daemon emitted; awaiting walkthrough | Daemon (Pass 3) + `chembl-refresh-prompt.md` |
| [`done/`](./done/) | Items walked through to closure | Walkthrough discipline (`git mv` from queue/) |
| [`history/`](./history/) | Per-sweep narrative summaries (one file per sweep run) | Daemon (Pass 3) |
| [`strategic-reflections/`](./strategic-reflections/) | Content-triggered platform reflections (human-curated) | Humans only |

## File-naming convention

Per [spec §5.1](../operations/specs/2026-05-08-synthesis-filesystem-migration.md):

```
queue/<sweep-date>-<type>-<index>-<slug>.md
done/<sweep-date>-<type>-<index>-<slug>.md
history/<sweep-date>-<short-sha>.md
```

`<type>` ∈ `connection`, `contradiction`, `experiment`, `open-question`, `priority-action`, `riskiest-assumption`, `most-curious-thread`, `chembl-discrepancy`.

## Daemon-write vs human-write boundary

- **Daemon writes** to `queue/` (per-item findings) and `history/` (per-sweep summaries) via `scripts/synthesis-emit-files.py` after Pass 3 review.
- **`chembl-refresh-prompt.md`** writes to `queue/` directly with `chembl-discrepancy` type files (separate quarterly workflow; not via the daemon emit script).
- **Humans write** to `strategic-reflections/` only. Walkthrough discipline moves files from `queue/` to `done/`.

## Closure flow

The walk-synthesis skill (`.claude/skills/walk-synthesis/SKILL.md`) walks each item in `queue/`, appends a `## ✓ Actioned <date>` block to the file, and `git mv`s it to `done/`. Empty `queue/` directory = inbox zero.

## Strategic Reflections semantics

Content-triggered platform reflections live in `strategic-reflections/`. They fire on substance maturity, not on walkthrough cadence. Walk-synthesis lists them but does not action them. See [`strategic-reflections/README.md`](./strategic-reflections/README.md).

## Historical pointer

Pre-2026-05-08 sweep history (the era when synthesis was a single growing `wiki/synthesis.md` file) is archived at [`history/_pre-2026-05-08-archive.md`](./history/_pre-2026-05-08-archive.md).

## Spec link

Full migration architecture, design decisions, and review history at [`operations/specs/2026-05-08-synthesis-filesystem-migration.md`](../operations/specs/2026-05-08-synthesis-filesystem-migration.md).
