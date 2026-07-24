---
title: "DAF/CD55 SCR1-4 Truncated Construct Protease Proxy (comp-012)"
date: 2026-05-05
tags: [complement, CD55, DAF, protease, shio-koji, computational, alphafold, structural-biology, CP0, SCR]
related:
  - daf-cd55-protease-stability-computational.md
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

# DAF/CD55 SCR1-4 Truncated Construct Protease Proxy (comp-012)

The construct hypothesis is that removing the Ser/Thr-rich stalk from soluble DAF/CD55 may preserve the four complement-regulatory SCR domains while avoiding a processing liability. COMP-012 does not establish that outcome.

## What the computation establishes

The retired artifact applied the inherited sequence filters to SCR1–4 and reported high AlphaFold confidence across the construct. Its original LOW verdict is invalid because the model used pLDDT confidence as accessibility. It did not establish burial, cleavage, degradation, retained activity, or survival in shio-koji; COMP-001 is not a validated comparator.

The source-backed construct boundary is P08174 aa 35–285. The sequence-filter inventory is a historical record of the retired computation, not a predictive result.

> **Research conjecture — SCR1–4 truncation may change process survival**{ .research-conjecture-label }
>
> **Grounded premises:** [UniProt P08174](https://www.uniprot.org/uniprotkb/P08174/entry) defines aa 35–285 as the four SCR domains, and [AlphaFold AF-P08174-F1](https://alphafold.ebi.ac.uk/entry/P08174) reports higher confidence across this region than across the downstream Ser/Thr-rich stalk (**Mechanistic Extrapolation**). These records do not measure solvent accessibility, cleavage, process survival, folding, or retained activity.
>
> **Novel leap:** The aa 35–285 construct may recover more intact, functional DAF than a matched full ectodomain under the intended production and processing conditions. No direct evidence establishes that advantage.
>
> **Why it matters:** A real configuration-specific advantage could focus DAF engineering without promoting the retired proxy.
>
> **Discriminating observation:** Compare matched full-ectodomain and aa 35–285 constructs in the same host, route, and processing conditions; measure product identity, intact recovery, fold, complement-regulatory function, and retained function after process exposure.

## Delivery and falsification gate

Under [§1.25](./validation-experiments.md#125-dafcd55-scr1-4-truncated-single-cassette-expression-in-a-oryzae-cp0-engineering-candidate-wet-lab-gate), express the exact SCR1–4 construct in *A. oryzae* and measure useful expression, formation of the eight annotated intrachain disulfides, retained complement-regulatory activity, and function through the intended processing conditions. A favorable result advances this exact construct but does not prove that truncation caused the outcome; failed expression, misfolding, loss of activity, or process instability redirects the construct while leaving other CP0 interventions open.

Related: [full-ectodomain proxy](./daf-cd55-protease-stability-computational.md) · [H05 falsification card](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [invalidated, non-runnable COMP-012 tombstone](./etc/experiments/comp-012-daf-cd55-scr14-truncated/)
