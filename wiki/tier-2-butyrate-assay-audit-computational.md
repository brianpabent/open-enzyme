---
title: "Butyrate Measurement Audit — Computational Literature Synthesis (comp-038)"
date: 2026-05-20
tags: [computational, assay-validation, quantification-ladder, butyrate, scfa, microbiome, agentic-literature-synthesis]
related:
  - computational-experiments.md
  - validation-experiments.md
  - quantification-ladder.md
  - genotype-informed-supplement-workflow.md
  - purine-degrading-bacteria.md
sources:
  - "comp-038 outputs/results.json and outputs/summary.md, 2026-05-20"
  - "PMID 23542733 — HPLC-UV SCFA + lactate method for in vitro fermentation supernatants"
  - "PMID 42041444 — electrochemical fecal SCFA profiling"
  - "PMID 41082646 — exhaled breath condensate SCFA correlation caution"
  - "Abcam ab65341 protocol v17a — generic FFA kit excludes acetic, propionic, and butyric acid"
---

# Butyrate Measurement Audit — Computational Literature Synthesis (comp-038)

**Status:** YELLOW. The original COMP-038 first pass was an abstract-level assay landscape. Its later full-text-verification provenance remains under corrective review; current method claims below are anchored directly to the primary papers. Neither candidate has been validated for an Open Enzyme strain, medium, operator workflow, or intervention study.

## Question

Which accessible methods could measure butyrate in culture supernatant, stool, serum, or breath, and what analytical validation would each matrix require?

## Current verdict

No ready-to-adopt Tier 1 or Tier 2 butyrate assay has been established for current OE use. The scan did, however, surface two useful and non-interchangeable directions:

| Candidate | Matrix | Current classification | Evidence boundary |
|---|---|---|---|
| HPLC-UV SCFA + lactate assay | Bacterial culture supernatant | **Tier 3 bench method; transfer candidate** | De Baere et al. validated direct UV at 210 nm after acidification and diethyl-ether extraction, with matrix-matched calibration from 0.5–50 mM. The method still requires qualification in the exact OE strain and medium. **In Vitro** ([PMID 23542733](https://pubmed.ncbi.nlm.nih.gov/23542733/)) |
| Electrochemical fingerprints + ANN | Human stool | **Tier 2 candidate; not adopted** | Gu et al. compared the complete VBS-100/G3-electrode, pretreatment, feature-extraction, and ANN stack with GC-MS in an independent 30-sample fecal test set; butyrate MAE/RMSE were 0.029/0.034 mM. External replication, exact-hardware or cross-hardware transfer, electrode-lot robustness, and a reusable implementation remain open. **In Vitro method study** ([PMID 42041444](https://pmc.ncbi.nlm.nih.gov/articles/PMC13114974/), [DOI](https://doi.org/10.3390/bios16040223)) |
| Butyric-acid / SCFA ELISA kits | Vendor-claimed serum, plasma, or tissue matrices | **RED-provisional** | COMP-038 did not surface primary method-comparison evidence sufficient to advance a kit. |
| Breath H2/CH4 | Breath | **Not butyrate-specific** | Useful as a broad fermentation proxy, not a quantitative butyrate measurement. |
| Generic free-fatty-acid colorimetry | Vendor-dependent | **Wrong assay class for this use** | The representative protocol reviewed by COMP-038 excluded short-chain fatty acids including butyrate. |

HPLC-UV is not Tier 2 under the [quantification ladder](./quantification-ladder.md): HPLC is bench instrumentation and therefore Tier 3. GC-MS is also Tier 3 when run in-house and becomes Tier 4 when an external qualified laboratory supplies the result and audit trail. Relative cost does not change the tier.

## Why this matters

Butyrate creates at least three separate observability problems:

1. **Production:** did the exact organism and culture process produce butyrate?
2. **Exposure:** what concentration appears in stool, serum, or the intended intestinal compartment?
3. **Mechanism:** did the measured exposure change ABCG2, urate flux, inflammation, or another prespecified target?

A culture-supernatant assay answers only the first question. A stool assay addresses one sampled exposure matrix. Neither establishes target-compartment exposure, direct Q141K rescue, gout efficacy, or safety.

The absence of a cheap assay does not block rigorous work: use a matrix-appropriate Tier 3 method directly. It does make routine distributed batch tracking more expensive until a lower-tier method is independently validated.

## What COMP-038 established

The committed first pass used 27 PubMed queries and a 74-record title/abstract snapshot, then generated five in-session synthesis trajectories. It identified:

- HPLC-UV as the leading culture-supernatant method-transfer candidate.
- Electrochemical/ANN profiling as a separate stool-specific direction.
- Breath hydrogen/methane as a fermentation proxy rather than a butyrate assay.
- Generic free-fatty-acid kits as a false-friend assay class for short-chain fatty acids.

These are candidate-selection results, not OE method validation.

## Next gates

### Culture-supernatant production QC

Run [validation §1.31](./validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms): qualify HPLC-UV in one exact strain–medium configuration and compare it with GC-MS. A successful transfer would establish a Tier 3 in-house method for that matrix, not a universal butyrate assay.

### Stool monitoring

Treat the Gu electrochemical/ANN workflow as a separate Tier 2 candidate. [Validation §1.45](./validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate) first seeks the author package and exact hardware path, then separates analytical replication from independent cohort transfer. A successful result applies only to the locked implementation, fecal matrix, working range, and analytical objective tested.

### COMP artifact integrity

COMP-038 still requires its exact full-text-verification artifact, updated results/provenance, and a new exact-snapshot review. Until that closes, distinguish primary-paper method support from validation performed by Open Enzyme.

## Cross-references

- [comp-038 experiment folder](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/)
- [computational experiment registry](./computational-experiments.md)
- [quantification ladder](./quantification-ladder.md)
- [genotype-informed intervention research workflow](./genotype-informed-supplement-workflow.md)
- [purine-degrading bacteria](./purine-degrading-bacteria.md)
