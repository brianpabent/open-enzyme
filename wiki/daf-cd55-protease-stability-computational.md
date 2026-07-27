---
title: "DAF/CD55 Shio-Koji Protease Proxy (comp-006)"
date: 2026-05-05
tags: [complement, CD55, DAF, protease, shio-koji, computational, alphafold, structural-biology, CP0]
related:
  - modality-chokepoint-matrix.md
  - complement-c5a-gout.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - computational-experiments.md
  - engineered-koji-protocol.md
sources:
  - "UniProt P08174 (human DAF/CD55, canonical isoform, SV=4)"
  - "AlphaFold AF-P08174-F1-model_v6 (EMBL-EBI)"
  - "MEROPS database release 12.4"
  - "Koaze et al. 1964 (acid protease pH-activity curve)"
  - "Ward et al. 1995 (A. oryzae α-amylase secretion signal)"
status: retired-invalid-model
---

# DAF/CD55 Shio-Koji Protease Proxy (comp-006)

The engineering question is whether a soluble DAF/CD55 ectodomain can retain complement-regulatory activity through production and shio-koji processing. Retired COMP-006 does not answer it.

## What survives from the retired computation

The retired artifact mapped inherited sequence-filter matches across P08174 and added AlphaFold pLDDT context. Those recognition-pattern counts, region tallies, and pLDDT distributions are deterministic inventories under the retired rules, not validated biological interpretations. Its original HIGH label is invalid because the model used pLDDT confidence as solvent accessibility. Its maximum-risk construction also returns the same per-protease maximum across the full, mature, ectodomain, and stalk scopes whenever each contains an “exposed” match, so it cannot support the claimed scope comparison. It did not calculate SASA, model cleavage kinetics, or measure degradation and retained activity.

The Ser/Thr-rich stalk has lower AlphaFold confidence than SCR1–4. That difference is confidence information only; it does not establish that the stalk is exposed, cleaved, or the dominant cause of failure.

> **Research conjecture — stalk removal may change process survival**{ .research-conjecture-label }
>
> **Grounded premises:** [UniProt P08174](https://www.uniprot.org/uniprotkb/P08174/entry) defines the full ectodomain and SCR1–4 boundaries, while [AlphaFold AF-P08174-F1](https://alphafold.ebi.ac.uk/entry/P08174) reports lower confidence for the Ser/Thr-rich stalk than for SCR1–4 (**Mechanistic Extrapolation**). Neither source measures solvent accessibility, cleavage, process survival, folding, or retained complement activity.
>
> **Novel leap:** Removing the stalk may improve recovery of a functional soluble DAF construct under the intended production and processing conditions. No direct evidence establishes a survival or functional advantage for the truncated construct.
>
> **Why it matters:** A real configuration-specific advantage could focus construct development without treating the invalid proxy as predictive.
>
> **Discriminating observation:** Compare matched full-ectodomain and SCR1–4 constructs in the same host, route, and processing conditions; measure product identity, intact recovery, fold, complement-regulatory function, and retained function after process exposure.

## Delivery and falsification gate

For the proposed *A. oryzae* route, the exact secreted construct must fold correctly and retain complement-regulatory function through the intended processing conditions. [§1.25](./validation-experiments.md#125-dafcd55-scr1-4-truncated-single-cassette-expression-in-a-oryzae-cp0-engineering-candidate-wet-lab-gate) tests expression, disulfide/folding, process stability, and function of SCR1–4. Because its current design has no full-ectodomain arm, a favorable result advances the truncated construct but cannot attribute that outcome to stalk removal.

Related: [SCR1–4 proxy](./daf-cd55-scr14-truncated-computational.md) · [H05 falsification card](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [invalidated, non-runnable COMP-006 tombstone](./etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/)
