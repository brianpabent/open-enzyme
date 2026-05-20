# comp-038 — Provenance and Planned Sources

This document tracks the literature sources and search corpora that comp-038's `analyze.py` will query when it runs. It is filled in *now* with the planned sources and *frozen on run* with the actual dated snapshots / API endpoints / version IDs that were used.

**Status:** Planning (not yet frozen). To be re-stamped to "Frozen YYYY-MM-DD" when `analyze.py` first executes.

## Search corpora (planned)

### Primary (Stage 1 — Crow-tier triage scan)

| Source | Endpoint / Access | Search type | Notes |
|---|---|---|---|
| PubMed | NCBI E-utilities API | Full-text indexed search | Primary corpus for analytical chemistry literature |
| PMC | NCBI PMC Open Access subset | Full-text retrieval | Used for verbatim quotes and methodology details |
| Google Scholar | Web search (paginated) | Citation-graph + grey literature | Catches preprints and conference proceedings PubMed misses |
| Google Patents | patents.google.com | Patent landscape for commercial kits | Vendor IP filings often disclose validation data not in journals |

### Secondary (Stage 2 — Falcon-tier deep on candidates that survive consensus)

| Source | Endpoint / Access | Search type | Notes |
|---|---|---|---|
| Vendor catalogs | Sigma-Aldrich / Megazyme / Cayman Chemical / Cell Biolabs / BioVision / Abcam websites | Direct product page retrieval | Confirms commercial availability + cost + protocol PDFs |
| Espacenet | EPO patent search | International patent landscape | Cross-check vs Google Patents for non-US assignees |
| Open Targets | (not directly relevant for butyrate-assay scope; skip) | — | Skipped for this experiment |

### Deferred (not in scope for comp-038)

| Source | Reason deferred |
|---|---|
| CNKI (中国知网) | Butyrate-assay literature is predominantly Western analytical chemistry; non-English corpora unlikely to surface novel Tier 2 candidates. Revisit only if Stage 1 returns are sparse. |
| J-STAGE | Same reason as CNKI. |
| KISS (Korean) | Same reason as CNKI. |
| ChiCTR / J-RCT trial registries | Out of scope; this experiment is about analytical assays, not clinical trials. |

## Model stack (planned — frozen on run)

| Seat | Model | Provider | Temperature | Notes |
|---|---|---|---|---|
| Synthesis / candidate-extraction | claude-opus-4-7 OR Claude Opus 4.7 (whichever id is current on run date) | Anthropic | 0.3 | OE default for literature synthesis; provides the per-trajectory verdict and candidate list. |
| Pairwise judge | claude-sonnet-4-6 | Anthropic | 0.0 | Pairwise comparison judge; lower temp for ranking stability. |
| Consensus aggregator | claude-haiku-4-5 | Anthropic | 0.0 | Combines N=5 trajectory outputs; lowest-cost model for the determinism-heavy aggregation step. |
| Optional bench (separate eval) | gemini-3-deep-think | Google | 0.3 | Bench eval only — not in production comp-038 run. See operations doc Open Eval #1. |

To be **frozen on run** by appending: model_id (full string), inference_date (UTC), and SHA of the prompt files in `analyze.py` at runtime.

## Date-snapshot discipline

All PubMed E-utilities queries embed `&mindate=` and `&maxdate=` to anchor the search to a literature snapshot date (defaulting to the run date). The resulting PMID list is committed to `outputs/pmids-by-trajectory.json` so a re-run on the same snapshot reproduces.

Google Scholar and Google Patents lack the same date-anchor support; for those sources, the comp-038 output records the access date and the first 100 results returned at that date. A re-run a year later may diverge as the index changes; that divergence is documented honestly in the limitations section of the output.

## Reproducibility standard

This experiment is in the proposed **agentic-literature-synthesis** comp-NNN sub-type (see [`operations/agentic-science-adoption.md`](../../../../../operations/agentic-science-adoption.md)). The reproducibility standard for this sub-type is NOT stdlib-only-determinism (which doesn't apply to LLM-driven analyses). Instead:

- **Inputs are fully documented:** query-strategy.json (frozen on run), provenance.md (this file, frozen on run with actual sources used), model versions (frozen on run).
- **Consensus statistics are reported:** N=5 trajectory outputs are committed to `outputs/`; consensus selection logic is documented; "surfaced by K of N trajectories" appears in the final report.
- **Budget is hard-capped:** $25 maximum in `analyze.py`. Runs that hit the cap report partial results honestly rather than continuing.
- **Date is recorded:** every external retrieval has a fetch-date.

A re-run on the same date with the same inputs SHOULD produce equivalent results (modulo LLM stochasticity bounded by the N=5 consensus). A re-run on a later date with refreshed PubMed/Scholar/Patents corpora MAY produce different results, and that's a feature: the comp-038 readout has a freshness expiration encoded in the dated snapshots.

## Limitations (acknowledged up front)

- **No CNKI / J-STAGE / KISS coverage** — see deferred-sources rationale above. If butyrate-assay literature *does* exist in non-English corpora, comp-038 will miss it. This is a deliberate scope decision, not a methodology gap.
- **No primary-data validation** — comp-038 finds and ranks published assays. It does not validate any candidate against a real butyrate sample. That validation is the proposed downstream step (small wet-lab Tier 2 / Tier 3 cross-validation study, possibly comp-039 or as a validation-experiments.md entry).
- **Single butyrate focus** — the connection-5 framing argues the Tier 2 gap applies to *all* microbiome-metabolite classes (SCFAs broadly, bile acids, indoles). comp-038 is scoped to butyrate only as the canonical case; bile acids and indoles get their own future experiments if the methodology validates.
- **LLM stochasticity** — the N=5 consensus mitigates but doesn't eliminate variance. Limitations section of the final report MUST quantify ("verdict consistent across N=5" vs "surfaced in 3 of 5 only").

## Cross-references

- Methodology framework: [`operations/agentic-science-adoption.md`](../../../../../operations/agentic-science-adoption.md)
- Strategic context: [`synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../../../../../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md)
- Triggering queue items: [open-question-2](../../../../../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md), [connection-5](../../../../../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md)
- Wet-lab validation anchor: [`wiki/validation-experiments.md`](../../../../validation-experiments.md) §1.14 butyrate dose-response arm (would provide Tier 3 GC-MS reference for any Tier 2 candidate comp-038 surfaces)
