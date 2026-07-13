---
title: "wiki/etc/ — reference / methodology / tooling pages (synthesis-excluded)"
date: 2026-05-15
updated: 2026-07-13
status: meta
---

# wiki/etc/

Reference, methodology, and tooling pages that **belong in the wiki** for human browsing but **should not be re-synthesized by the daemon** on every sweep.

## What lives here

Pages where the content is:
- A **catalog** (tools, references, team) — humans want to find it via cross-reference, but it's not generative research the daemon should cross-connect.
- A **methodology / how-to** — describes how OE does work; not a finding the daemon should re-evaluate.
- A **diagram / static artifact** — Mermaid graphs, bibliographies; daemon can't usefully synthesize over them.

Examples in this directory:

| File | Type | Why |
|---|---|---|
| `bio-ai-tools.md` | Tool catalog | Available AI/bio tools — reference, not research |
| `ai-bio-tools-playbook.md` | Playbook | How to use the tools — methodology, not findings |
| `references.md` | Bibliography | Citation list — daemon doesn't synthesize bibliographies |
| `GRAPH.md` | Mermaid diagram | Graph diagrams — non-vision models can't usefully read them |
| `team.md` | Staff page | Team roster — no biology synthesis value |
| `paperclip-deep-dive.md` | Tool deep-dive | Single-tool reference |
| `practitioner-toolkit.md` | Utility guide | How-to for practitioners |
| `manual-literature-mining.md` | Methodology | How-to for lit mining |
| `autonomous-screening-methodology.md` | Methodology | How-to for autonomous screens |
| `chembl-cross-check.md` | Quality methodology | How OE validates against ChEMBL |
| `experiments/comp-NNN-*/` | Reproducible computational artifacts | Too large for every global sweep; each changed comp receives its own bounded independent artifact review |

## What does NOT live here

If a page contains **active research findings**, **mechanistic claims**, **chokepoint analysis**, **engineering plans**, **hypothesis cards**, or **synthesis output**, it normally belongs in `wiki/` proper, not in `wiki/etc/`. The global daemon should re-read it on every sweep so cross-document connections surface.

**Exception — computational experiment artifacts.** The narrative stub for each comp remains in `wiki/` proper, while its reproducible code/input/output/archive bundle lives under `wiki/etc/experiments/`. These artifacts are active evidence but are too large and too implementation-specific to inline into every global synthesis. They are covered by the independent `.github/workflows/comp-review.yml` daemon instead: every changed comp gets a bounded artifact-level review with on-demand corpus search. This exception must not be generalized to other active-research pages.

When in doubt: ask "would the daemon's synthesis benefit from re-reading this every sweep?" If yes → `wiki/`. If no → `wiki/etc/`.

## How exclusion works (mechanics)

Two layers exclude `wiki/etc/` from the daemon:

1. **Corpus loader (`scripts/synthesize.py` `build_corpus()`):** globs `wiki/*.md` + `wiki/hypotheses/*.md`. Does NOT glob `wiki/etc/*.md`. So pages in this directory are naturally excluded from the synthesis input. (The `EXCLUDE` set in synthesize.py is empty as of 2026-05-15 — directory-based exclusion replaced per-file exclusion.)

2. **Workflow path trigger (`.github/workflows/wiki-sweep.yml`):** the push trigger watches `wiki/**.md` with `!wiki/etc/**` negation. Editing a page in this directory does not trigger a sweep run.

Together: ordinary pages here are invisible to the **global wiki daemon**, both as input and as triggers. The `wiki/etc/experiments/comp-*/**` subtree is separately watched by `.github/workflows/comp-review.yml`; comp artifacts are excluded from global synthesis, not from review.

## Cross-references

Pages in `wiki/etc/` can be referenced from `wiki/` proper using `./etc/<page>.md` paths. References from `wiki/etc/` back to `wiki/` use `../<page>.md`. The script `/tmp/claude/move-to-etc.py` (run 2026-05-15) handled the cross-reference rewriting when the directory was created.

## Adding a new etc/ page

1. Decide it's reference/methodology, not active research (per the criteria above).
2. Create the file at `wiki/etc/<name>.md` (or `git mv wiki/<name>.md wiki/etc/<name>.md` to relocate).
3. Update any cross-references in `wiki/*.md` to use `./etc/<name>.md`.
4. No EXCLUDE list to update — the directory-based exclusion handles it automatically.
5. Add a row to the table above so future readers know what's here and why.

## When to promote a page OUT of etc/ back to wiki/

If a page that started as reference/methodology evolves into active research (e.g., a methodology page accumulates evidence-tier findings the daemon should synthesize against), promote it back: `git mv wiki/etc/<name>.md wiki/<name>.md` and fix cross-references back to `./<name>.md`. Reverse of the move-in process.

## Origin

This convention was introduced 2026-05-15 after the post-PR-#11 sweep failed when the wiki corpus reached ~975K tokens (97.5% of DeepSeek V4-Pro's 1M-token cap). Brian's framing: reference catalogs and methodology pages "belong in the wiki, but they don't need to be synthesized" — the right solution is a within-wiki exclusion folder, not moving them out of the wiki entirely. See [`synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md`](../../synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md) for the same-session reflection that produced the chassis-pending discipline; the etc/ convention is a sister discipline operating on the corpus-management axis instead of the chassis-fit axis.
