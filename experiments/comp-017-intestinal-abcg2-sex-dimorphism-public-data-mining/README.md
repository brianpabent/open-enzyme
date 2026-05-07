# comp-017 — Intestinal ABCG2 sex-dimorphism: public-data mining + 4-paper full-text re-read

**Date:** 2026-05-07  
**Status:** Complete  
**Verdict:** **NULL OR NEAR-NULL SEX-DIMORPHISM** at healthy baseline; emerges only under disease-state genetic stress (Q140K LOF) — provisional pending direct GTEx access.

## Question

Two-part Tier-0 killshot for [`H07-clomid-intestinal-er-antagonism`](../../wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md) sub-claims 1 and 3:

- **Part A:** GTEx + Human Protein Atlas mining for sex-stratified intestinal ABCG2 expression in healthy humans. Do male and female intestinal ABCG2 expression distributions differ meaningfully at population scale?
- **Part B:** Full-text re-read of 4 anchor papers from comp-016 (Yu Y et al. 2021; Klyushova LS et al. 2023; MacLean C et al. 2008; Hoque KM, Halperin Kuhns VL et al. 2020 PMID 32488095). What does full text show that comp-016's abstract-only scan missed?

## Method

- **Part A:** WebSearch + WebFetch against GTEx Portal, Human Protein Atlas, secondary GTEx-derived sex-bias publications (Oliva 2020 Science, Schärfe 2023 Nat Comm), and the Halperin Kuhns 2020 IJMS sex-differences review. Sandbox-blocked from direct portal access; fell back to WebSearch result-snippet extraction quoting source-paper text.
- **Part B:** WebSearch + WebFetch against PMC, journal landing pages, ResearchGate, alternative full-text mirrors. Same sandbox limitation. Extracted method, exact quantitative findings, and abstract-vs-full-text differences via WebSearch result-snippets quoting source papers.
- **Aggregation:** `analyze.py` (stdlib only — `json`, `pathlib`, `collections`) reads `inputs/{gtex_data,hpa_data,full_text_extract}.json` and produces `outputs/{results.json,summary.md}`. Per-paper records include `comp016_summary` (what comp-016 had), `full_text_extract` (what full-text re-read found), `abstract_vs_fulltext_difference` (the gain), and `h07_sub_claim_impact` (which H07 sub-claims update).

## Files

```
comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/
├── README.md                    # this file
├── analyze.py                   # stdlib-only aggregator
├── inputs/
│   ├── gtex_data.json           # GTEx mining + secondary literature
│   ├── hpa_data.json            # HPA mining
│   ├── full_text_extract.json   # 4-paper full-text records
│   └── provenance.md            # URLs + access route + dates
└── outputs/
    ├── results.json             # machine-readable verdict + sub-claim updates
    └── summary.md               # human-readable per-paper table + verdict
```

## Reproduction

```bash
cd experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/
python3 analyze.py
# outputs land in outputs/
```

To extend with direct GTEx data: an environment with portal access (or an authenticated GTEx REST API key) is needed. The `inputs/gtex_data.json` schema has a `raw_per_tissue_sex_stratified_TPM` slot pre-defined for those values when accessible.

## Wiki link

Interpretive page: [`wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`](../../wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md)

## Tracking

- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — comp-017 entry
- [`wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md`](../../wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md) — H07 falsification card; this experiment executes the Tier-0 killshot for sub-claims 1 and 3.
- [`wiki/t-abcg2-suppression-evidence-mining-computational.md`](../../wiki/t-abcg2-suppression-evidence-mining-computational.md) — comp-016 (predecessor); this experiment closes its full-text-verification follow-up.
