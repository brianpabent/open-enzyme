---
title: "Butyrate Measurement Audit — Computational Literature Synthesis (COMP-038)"
date: 2026-05-20
tags: [computational, assay-validation, quantification-ladder, butyrate, scfa, microbiome]
related:
  - computational-experiments.md
  - validation-experiments.md
  - quantification-ladder.md
  - open-questions.md
sources:
  - "PMID 23542733 — HPLC-UV for SCFAs and lactate in bacterial culture supernatants"
  - "PMID 42041444; PMCID PMC13114974 — electrochemical/ANN fecal SCFA profiling"
  - "COMP-038 primary-source-verification-2026-07-24.json"
---

# Butyrate Measurement Audit

**Status:** **YELLOW.** No ready-to-adopt Tier 1 or Tier 2 butyrate
method has been established for Open Enzyme. Published evidence supports one
Tier 3 culture-supernatant method-transfer candidate and one separate Tier 2
stool candidate. Neither is qualified for an Open Enzyme matrix or workflow.

## The measurement weakness

Butyrate creates three different observability problems:

1. **Production:** did an organism and culture process produce butyrate?
2. **Exposure:** what concentration reached stool, serum, or the intended
   intestinal compartment?
3. **Mechanism:** did that exposure change ABCG2, urate flux, inflammation, or
   another prespecified target?

A culture-supernatant assay answers only the first question. A stool assay
measures one sampled exposure matrix. Neither establishes target-compartment
exposure, Q141K rescue, gout efficacy, or safety.

## Current methods

| Method | Matrix | Evidence and boundary |
|---|---|---|
| HPLC-UV for four SCFAs plus lactate | Bacterial culture supernatant | **Tier 3 transfer candidate.** De Baere et al. report 210 nm detection after diethyl-ether back-extraction and acidification below pH 2, with matrix-matched calibration from 0.5–50 mM. The accessible primary abstract reports analyte-spanning LOD/LOQ ranges of 0.13–0.33/0.5–1.0 mM; it does not assign those endpoints specifically to butyrate or explicitly state “underivatized.” **In Vitro analytical-method study** ([PMID 23542733](https://pubmed.ncbi.nlm.nih.gov/23542733/), [DOI](https://doi.org/10.1016/j.jpba.2013.02.032)) |
| Electrochemical fingerprints plus ANN | Human stool | **Tier 2 candidate; not adopted.** Gu et al. used a VBS-100 workstation, disposable G3 gold electrodes, target-specific pretreatment, voltammetric features, and an ANN. In the within-study independent 30-sample fecal test cohort versus GC-MS, butyrate MAE/RMSE/R² were 0.029 mM/0.034 mM/0.998. Butyrate bias was −0.015 mM with limits of agreement −0.065 to 0.035 mM and was statistically different from zero. Independent external replication and implementation transfer remain open. **In Vitro analytical-method study** ([PMID 42041444](https://pmc.ncbi.nlm.nih.gov/articles/PMC13114974/), [DOI](https://doi.org/10.3390/bios16040223)) |
| Butyrate or SCFA ELISA | Vendor-claimed matrices | **RED-provisional.** No qualifying primary method comparison surfaced in the bounded COMP-038 search. This is not an exhaustive absence claim. |
| Breath hydrogen or methane | Breath | **Not butyrate-specific.** A broad fermentation or transit proxy, not quantitative butyrate measurement. |
| Generic free-fatty-acid colorimetry | Vendor-dependent | **Wrong assay class for the reviewed use.** The representative protocol excluded short-chain fatty acids including butyrate. |

HPLC-UV is Tier 3 under the [quantification
ladder](./quantification-ladder.md). GC-MS is Tier 3 when run in-house and Tier
4 when a qualified external laboratory supplies the result and audit trail.
Relative affordability does not change the tier. If lower-tier access is not
qualified for the exact analyte and matrix, use a Tier 3 method directly.

## Falsification gates

### Culture-supernatant production QC

[Validation §1.31](./validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms)
tests one exact strain, medium, and harvest workflow with matrix-matched
standards, spike/recovery, interference controls, and paired HPLC-UV/GC-MS
measurements. A pass qualifies only that Tier 3 implementation and matrix.

### Stool monitoring

[Validation §1.45](./validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate)
tests the complete Gu hardware–chemistry–model stack. It separates analytical
reproduction from a later independent external transfer of a locked
implementation. A pass would not transfer to culture supernatant, serum,
another metabolite, or a clinical diagnostic.

## Cross-references

- [COMP-038 experiment artifact](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/)
- [Computational Experiments](./computational-experiments.md)
- [Quantification Ladder](./quantification-ladder.md)
- [Matrix-specific open question](./open-questions.md#matrix-specific-assay-gap-for-microbiome-derived-metabolites)
