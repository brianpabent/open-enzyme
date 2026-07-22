> **⚠️ INVALIDATED / SUPERSEDED (comp-044 2026-07-13; comp-review 2026-07-14).** comp-019 ΔSUA, capacity ratios, genotype ranking, flat-dose, and yield recommendations are RETIRED — the model omitted luminal urate occupancy and finite residence/exposure time. Do NOT use any comp-019 output for dose, yield-deprioritization, genotype-ranking, or trial-arm design. Superseded by comp-044 (gut-lumen-uricase-physiologic-regime-computational.md); sink question reopened under H08 + validation §1.33/§1.36. Frozen invalidated provenance.

# comp-019 — Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model

**Date:** 2026-05-08
**Status:** **Invalidated / superseded by comp-044**
**Current verdict:** Phase A found no Q141K-stratified uricase clinical outcome in the sources searched for comp-019 as of 2026-05-08. The Phase B ΔSUA estimates, genotype ordering, capacity ratios, flat-dose conclusion, yield recommendation, and trial-design implications are invalid and must not be used.

## Question

Two-phase in-silico experiment answering the platform's most important open question for its primary demographic:

**"Can the gut-lumen uricase sink produce meaningful serum urate reduction in non-Q141K males, or does the mechanism rely on Q141K-positive disease-state ABCG2 vulnerability to show benefit?"**

- **Phase A — Literature stratification mining.** Post-hoc stratification of existing oral-uricase + systemic-uricase + ABCG2-axis ULT response data by ABCG2 Q141K (rs2231142) genotype.
- **Phase B — First-principles flux model.** Quantitative model of intestinal urate flux predicting ΔSUA in WT-male / Q141K-het male / Q141K-hom male / female under three uricase-dose scenarios.

## Method

**Phase A:** PubMed MCP `search_articles` + `get_article_metadata` + `get_full_text_article` against ABCG2-Q141K-ULT response literature, ALLN-346 trial corpus, PRX-115 Phase 1 data, and intestinal urate handling primary measurements. WebSearch + WebFetch against ClinicalTrials.gov, EULAR abstracts, Allena/Protalix press releases, and the Miyazaki 2025 J Transl Med paper (PMC11877951) — the load-bearing direct human in-vivo measurement of jejunal urate secretion stratified by ABCG2 functional class.

**Phase B:** Python flux model (`scripts/flux_model.py`, stdlib only — `json`, `math`, `random`, `pathlib`). Inputs from `inputs/flux_model_parameters.json` (literature-anchored). Monte Carlo sensitivity (n=5000) over uncertainty bounds (production rate, gut excretion fraction, renal compensation). Genotype scaling per Matsuo 2014 / Miyazaki 2025 functional-classification framework (100% / 75% / 50% / 25%).

**Aggregation:** Outputs land in `outputs/flux_model_results.json` and `outputs/flux_model_summary.md`.

## Files

```
comp-019-gut-lumen-uricase-abcg2-genotype-stratification/
├── README.md                            # this file
├── inputs/
│   ├── query_strategy.md                # Phase A query strategy + verification gate
│   ├── phase_a_literature.json          # Phase A stratification mining records
│   └── flux_model_parameters.json       # Phase B literature-anchored parameters
├── outputs/
│   ├── flux_model_results.json          # full machine-readable results (central + MC)
│   ├── flux_model_summary.md            # human-readable tables + interpretation
│   └── phase_a_table.md                 # Phase A stratification findings table
└── scripts/
    ├── flux_model.py                    # retired Python flux model + Monte Carlo
    └── verify_retirement.py             # invalidation and archival-fidelity checks
```

## Reproduction

```bash
cd wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/
python3 scripts/flux_model.py --reproduce-invalidated-history
# results land in outputs/
```

The explicit flag is required because this command reproduces an invalidated historical model. Regenerated outputs retain the warning banner and machine-readable invalidation metadata. No external dependencies are required (Python 3 stdlib only).

The reference retirement-contract check was recorded with **CPython 3.14.5**. Run `python3 scripts/verify_retirement.py` to verify refusal without the explicit flag, unchanged historical numerical payload, required warnings and JSON metadata, and byte-identical repeated flagged runs. The command reruns Phase B only; Phase A is a frozen literature-search record dated 2026-05-08.

Reproduction creates no new evidence and authorizes no propagation. Only the scoped Phase A observation may remain active: no Q141K-stratified uricase clinical outcome was identified in the sources searched for comp-019 as of 2026-05-08. [comp-044](../../../gut-lumen-uricase-physiologic-regime-computational.md) owns the current quantitative interpretation.

## Historical invalid output — do not use for decisions

**Predicted ΔSUA at steady state (Monte Carlo medians, mid-dose 25 mg/day uricase):**

| Genotype × sex | ΔSUA | 90% CI | Verdict |
|---|---|---|---|
| WT/WT male | **−0.83 mg/dL** | (−1.13, −0.57) | Largest absolute response |
| Q141K het male | −0.67 mg/dL | (−0.91, −0.45) | Substantial response |
| Q141K hom male | −0.50 mg/dL | (−0.68, −0.34) | Moderate response |
| WT/WT female | −0.74 mg/dL | (−1.00, −0.50) | Substantial response |
| Q141K het female | −0.59 mg/dL | (−0.80, −0.40) | Substantial response |
| Q141K hom female | −0.42 mg/dL | (−0.57, −0.29) | Moderate response |
| Severe dysfunction (Q126*+Q141K compound) | −0.28 mg/dL | (−0.37, −0.19) | Smallest response — structural ceiling |

**The mechanism works ACROSS genotypes; the magnitude scales with the residual ABCG2 capacity. Q141K is associated with LESS response, not more.**

## Wiki link

Interpretive page: [`wiki/uricase-abcg2-genotype-stratification-computational.md`](../../../uricase-abcg2-genotype-stratification-computational.md)

## Tracking

- [`wiki/computational-experiments.md`](../../../computational-experiments.md) — comp-019 entry
- [`wiki/cross-validation.md`](../../../cross-validation.md) Claim 1 — gut-lumen sink mechanism rating updated post-comp-019
- [`wiki/gut-lumen-sink.md`](../../../gut-lumen-sink.md) — genotype-stratification cross-reference
- [`wiki/abcg2-modulators.md`](../../../abcg2-modulators.md) — Q141K rescue context cross-reference
- [`wiki/synthesis.md`](../../../synthesis.md) — Sweep 2026-05-08 Open Question 1 actioned
- [`wiki/open-questions.md`](../../../open-questions.md) — genotype-stratification entry update

## Predecessor experiments

- [comp-016](../comp-016-t-abcg2-suppression-evidence-mining/) — established WEAK / UNCONFIRMED verdict on direct androgen-driven intestinal ABCG2 suppression
- [comp-017](../comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) — established NULL-or-NEAR-NULL healthy-baseline sex dimorphism on intestinal ABCG2; shifted responder logic toward Q141K disease-state framing

## Limitations

1. **No prospective Q141K-stratified oral-uricase outcome was identified in the sources searched for comp-019 as of 2026-05-08.** This is a bounded search result, not proof of universal absence. No Phase B trial-design recommendation survives.
2. **Miyazaki 2025 substrate population is Crohn's-disease-dominated** (30 of 34 subjects). Inflammatory bowel disease may itself affect intestinal ABCG2 expression / function. The genotype-stratified secretion ratios this paper provides are the best available data, but their generalization to typical gout patients (no IBD) is an open question.
3. **The flux model uses a first-order steady-state approximation and omits the physiological operating regime.** No ΔSUA magnitude or genotype-ordering conclusion survives.
4. **Renal compensation fraction (central estimate 0.30, sensitivity 0.0–0.5) is a mechanistic-extrapolation parameter.** It was not directly measured in the searched oral-uricase trials and cannot rescue the invalid model.
5. **Pre-commit verification gate (CLAUDE.md Rule 4):** Miyazaki 2025 numbers are full-text grep-verified from PMC11877951. Wallace 2018, Vora 2021, Stamp 2019, Matsuo 2014, Takada 2014, Nakayama 2011 numbers are abstract-tier-verified (not line-anchored to full-text). ALLN-346 Phase 2a Study 201/202 numbers are EULAR-abstract / press-release tier (not peer-reviewed full-text). PRX-115 Phase 1 is conference-abstract tier.
6. **Multilingual search scope was incomplete.** The comp-019 search included ChiCTR, J-STAGE, and KISS checks but did not establish universal absence across regional databases.
