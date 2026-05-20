# comp-038 — Provenance and Planned Sources

This document tracks the literature sources and search corpora that comp-038's `analyze.py` queried when it ran. It preserves both the planned corpus and the actual frozen run artifacts.

**Status:** Frozen 2026-05-20 for the Codex source-packet run. PubMed snapshot: `outputs/pubmed-snapshot.json` (`2026-05-20T15:06:05+00:00`, 27 queries, 74 records). Codex synthesis output: `outputs/results.json` + `outputs/summary.md` (`2026-05-20T15:09:12+00:00`). No OpenRouter model calls were made for the completed run.

## Search corpora (planned)

### Primary (Stage 1 — Crow-tier triage scan)

| Source | Endpoint / Access | Search type | Notes |
|---|---|---|---|
| PubMed | NCBI E-utilities API | Title / abstract / citation search | Primary discovery corpus for analytical chemistry literature; PMID hits require separate full-text retrieval before assay-method verdicts. |
| PMC | NCBI PMC Open Access subset | Full-text retrieval for PMID-linked open-access articles | Used for methods-table details, verbatim quotes, and validation-protocol extraction when full text is available. |
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

## Firewall-sensitive source retrieval

Some Chinese and East Asian academic domains may only be reachable through Brian's local laptop network path because the firewall allowlist applies locally, while model/web-fetch tools may egress from vendor infrastructure. For those sources, use `experiments/lib/agentic_lit_synthesis.py::local_curl_fetch()` rather than model-side fetch. The helper:

- shells out to local `curl` from the laptop;
- only allows explicitly allowlisted academic host suffixes (`cnki.net`, `cnki.com.cn`, `wanfangdata.com.cn`, `wanfang.com.cn`, `cqvip.com`, `sinomed.ac.cn`, `chictr.org.cn`, `medresman.org`, `nstl.gov.cn`, `chinaxiv.org`, `jst.go.jp`, `nii.ac.jp`, `kci.go.kr`, `riss.kr`, etc.);
- writes the fetched body plus a `.provenance.json` sidecar recording URL, timestamp, method = `local_curl`, network_path = `local_machine`, return code, and effective URL;
- never sends the fetched source through a model unless a later analysis step explicitly includes a bounded excerpt / extracted metadata.

This is not currently expected to be needed for comp-038's butyrate-assay scope, but it is part of the shared agentic-literature-synthesis workflow so future non-English corpus passes do not reinvent the firewall workaround.

## Non-English translation protocol

If a non-English source becomes relevant, the run must use the two-model independent translation protocol from `experiments/lib/agentic_lit_synthesis.py::translate_source_two_model()` before any source-derived claim enters `outputs/summary.md` or a wiki page.

Operational requirements:

- Use two independent models from different vendors / training pipelines.
- For Chinese sources, include a native-language-strong model by default (`deepseek/deepseek-chat` in `model-config.json`) plus a second independent model (`openai/gpt-5.5` by default).
- Do not choose a single "winning" translation when the models disagree.
- The annotated translation must preserve science-relevant disagreements inline with `{Model A: "..." | Model B: "..."}`.
- Add `[TRANSLATION-DISAGREEMENT]` when disagreement affects evidence tier, mechanism mapping, dose, route, units, statistics, sample size, study design, or scientific hedging (`inhibits` vs `modulates` vs `may`).
- Commit both raw model translations and the annotated referee output under `outputs/` so future readers can audit the disagreement.

This matches the repo-wide translation rule in `CLAUDE.md` and is part of the shared agentic-literature-synthesis workflow, even though comp-038 currently defers CNKI / J-STAGE / KISS unless Stage 1 is sparse.

## Model stack (frozen on run)

| Seat | Model | Provider | Temperature | Notes |
|---|---|---|---|---|
| Query strategist / blind-spot critic | Codex/GPT-5.5 in-session | Codex subscription | n/a | In-session query-strategy critique; no paid external call. |
| Synthesis / candidate-extraction | Codex/GPT-5.5 in-session | Codex subscription | n/a | N=5 synthesis trajectories from `outputs/codex-synthesis-packet.md`; no OpenRouter model calls. |
| Pairwise judge | Codex/GPT-5.5 in-session | Codex subscription | n/a | Pairwise-style ranking and overclaim detection in the same Codex run. |
| Verifier / limitations reviewer | Codex source-evidence gate | Codex subscription | n/a | No GREEN verdict from abstracts alone. |

Optional external roles remain configured in [`model-config.json`](./model-config.json) under `*_openrouter` keys and are used only with the explicit `python3 analyze.py --run-openrouter` path. `OPENROUTER_API_KEY` is read from the repo-root `.env` (gitignored) or shell environment only for explicit OpenRouter paths and is never written to outputs.

## Date-snapshot discipline

All PubMed E-utilities queries are committed as a dated snapshot in `outputs/pubmed-snapshot.json`; a re-run on a later date may diverge as PubMed changes. For candidate assays, the next pass must attempt full-text retrieval via PMC, DOI / publisher pages, institutional access, or vendor protocol PDFs before assigning any final GREEN verdict; PubMed abstracts alone are insufficient for load-bearing method-validation claims.

Google Scholar and Google Patents lack the same date-anchor support; for those sources, the comp-038 output records the access date and the first 100 results returned at that date. A re-run a year later may diverge as the index changes; that divergence is documented honestly in the limitations section of the output.

## Reproducibility standard

This experiment is in the proposed **agentic-literature-synthesis** comp-NNN sub-type (see [`operations/agentic-science-adoption.md`](../../../../../operations/agentic-science-adoption.md)). The reproducibility standard for this sub-type is NOT stdlib-only-determinism (which doesn't apply to LLM-driven analyses). Instead:

- **Inputs are fully documented:** query-strategy.json (frozen on run), provenance.md (this file, frozen on run with actual sources used), model versions (frozen on run).
- **Consensus statistics are reported:** N=5 trajectory outputs are committed to `outputs/`; consensus selection logic is documented; "surfaced by K of N trajectories" appears in the final report.
- **Budget is explicit:** the default Codex packet path has no OpenRouter model spend. The optional `--run-openrouter` path has a $25 review ceiling in the config and should be used only when external-vendor roles are intentional.
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
