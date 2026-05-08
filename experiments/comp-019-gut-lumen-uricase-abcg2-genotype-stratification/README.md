# comp-019 — Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model

**Date:** 2026-05-08
**Status:** Complete
**Verdict:** **The gut-lumen uricase mechanism does NOT depend on Q141K-positive disease-state vulnerability. Non-Q141K (WT/WT) males show the LARGEST predicted ΔSUA, not the smallest. The platform's primary demographic positioning should NOT be narrowed to Q141K-positive patients.**

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
    └── flux_model.py                    # Python flux model + Monte Carlo
```

## Reproduction

```bash
cd experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/
python3 scripts/flux_model.py
# results land in outputs/
```

No external dependencies required (Python 3 stdlib only).

## Headline finding

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

Interpretive page: [`wiki/uricase-abcg2-genotype-stratification-computational.md`](../../wiki/uricase-abcg2-genotype-stratification-computational.md)

## Tracking

- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — comp-019 entry
- [`wiki/cross-validation.md`](../../wiki/cross-validation.md) Claim 1 — gut-lumen sink mechanism rating updated post-comp-019
- [`wiki/gut-lumen-sink.md`](../../wiki/gut-lumen-sink.md) — genotype-stratification cross-reference
- [`wiki/abcg2-modulators.md`](../../wiki/abcg2-modulators.md) — Q141K rescue context cross-reference
- [`wiki/synthesis.md`](../../wiki/synthesis.md) — Sweep 2026-05-08 Open Question 1 actioned
- [`wiki/open-questions.md`](../../wiki/open-questions.md) — genotype-stratification entry update

## Predecessor experiments

- [comp-016](../comp-016-t-abcg2-suppression-evidence-mining/) — established WEAK / UNCONFIRMED verdict on direct androgen-driven intestinal ABCG2 suppression
- [comp-017](../comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/) — established NULL-or-NEAR-NULL healthy-baseline sex dimorphism on intestinal ABCG2; shifted responder logic toward Q141K disease-state framing

## Limitations

1. **No prospective Q141K-stratified oral uricase RCT exists.** ALLN-346 Phase 2a Studies 201 and 202 did not report ABCG2 stratification; PRX-115 Phase 1 (n=64) did not pre-specify genotype. The flux model's predictions are PROSPECTIVE — they have not been clinically validated. The Phase 2b RCT design recommendation is the bridge from this in-silico finding to clinical evidence.
2. **Miyazaki 2025 substrate population is Crohn's-disease-dominated** (32 of 34 subjects). Inflammatory bowel disease may itself affect intestinal ABCG2 expression / function. The genotype-stratified secretion ratios this paper provides are the best available data, but their generalization to typical gout patients (no IBD) is an open question.
3. **The flux model uses 1st-order steady-state approximation.** A more rigorous PBPK model with explicit clearance + reabsorption + circadian dosing would refine the magnitude estimates but is unlikely to flip the genotype-ordering conclusion.
4. **Renal compensation fraction (central estimate 0.30, sensitivity 0.0–0.5) is a mechanistic-extrapolation parameter.** Not directly measured in oral uricase trials. Flux model is robust to this parameter direction (compensation reduces magnitude but doesn't flip genotype ordering).
5. **Pre-commit verification gate (CLAUDE.md Rule 4):** Miyazaki 2025 numbers are full-text grep-verified from PMC11877951. Wallace 2018, Vora 2021, Stamp 2019, Matsuo 2014, Takada 2014, Nakayama 2011 numbers are abstract-tier-verified (not line-anchored to full-text). ALLN-346 Phase 2a Study 201/202 numbers are EULAR-abstract / press-release tier (not peer-reviewed full-text). PRX-115 Phase 1 is conference-abstract tier.
6. **Multilingual scan deferred.** Per CLAUDE.md §"Global-multilingual research by default": ChiCTR / J-STAGE / KISS searches did not surface a published genotype-stratified oral-uricase RCT. The likelihood of finding one in a non-English source not already indexed by gnomAD-citing researchers is low, but a future Paperclip-MCP run on Chinese-language gout pharmacogenomics could refine the genotype-stratification picture for East-Asian-ancestry cohorts (Q141K MAF ~30% vs ~10% in European-ancestry).
