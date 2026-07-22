---
title: "Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model (comp-019)"
date: 2026-05-08
tags:
  - abcg2
  - q141k
  - rs2231142
  - gut-lumen-sink
  - uricase
  - genotype-stratification
  - flux-model
  - alln-346
  - prx-115
  - rasburicase
  - intestinal-urate-secretion
  - matsuo-2014
  - miyazaki-2025
  - wallace-2018
  - vora-2021
  - nakayama-2011
  - takada-2014
  - phase-2b-trial-design
  - comp-019
  - mechanistic-extrapolation
  - in-silico
related:
  - cross-validation.md
  - gut-lumen-sink.md
  - abcg2-modulators.md
  - intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
  - t-abcg2-suppression-evidence-mining-computational.md
  - androgen-urate-axis.md
  - validation-experiments.md
  - personal-genome-protocol.md
  - gout-clinical-pipeline.md
  - computational-experiments.md
  - ../synthesis/README.md
  - open-questions.md
sources:
  - "Miyazaki R, Ohashi Y, Sakurai T, Iwamoto T, Ichida K, Saruta M (2025) J Transl Med 23:257, PMID 40033341, doi:10.1186/s12967-025-06145-7"
  - "Wallace MC et al. (2018) Rheumatology (Oxford) 57(4):656-660, PMID 29342288, doi:10.1093/rheumatology/kex467"
  - "Vora B et al. (2021) Clin Transl Sci 14(4):1431-1443, PMID 33931953, doi:10.1111/cts.12992"
  - "Stamp LK et al. (2019) Clin Transl Sci 13(1):110-115, PMID 31444839, doi:10.1111/cts.12686"
  - "Matsuo H et al. (2014) Nucleosides Nucleotides Nucleic Acids 33(4-6):266-274, PMID 24940678, doi:10.1080/15257770.2013.866679"
  - "Takada T et al. (2014) Nucleosides Nucleotides Nucleic Acids 33(4-6):275-281, PMID 24940679, doi:10.1080/15257770.2013.854902"
  - "Nakayama A et al. (2011) Nucleosides Nucleotides Nucleic Acids 30(12):1091-1097, PMID 22132962, doi:10.1080/15257770.2011.633953"
  - "Pierzynowska K et al. (2020) Front Med 7:569215, PMID 33330529, doi:10.3389/fmed.2020.569215"
  - "Allena Pharmaceuticals EULAR POS1157 (2022) ALLN-346 Phase 2a Study 201"
  - "Protalix BioTherapeutics (2024) PRX-115 Phase 1 ACR Convergence late-breaking poster"
  - "Nguyen KP et al. (2025) Clin Rheumatol 44(10):4275-4281, PMID 40858881, doi:10.1007/s10067-025-07656-w"
status: superseded-by-comp-044
---

# Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model (comp-019)

> **Superseded 2026-07-13 by [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md).** comp-019's code did not use the luminal-urate concentration or UOX Km stored in its inputs and assumed 24 hours of saturated activity. Its quantitative ΔSUA, genotype-effect magnitudes, capacity ratios, flat-dose conclusion, and yield-priority recommendations are retired. The frozen artifact remains for provenance only; do not use it for dose or efficacy decisions.

## What survives

Phase A found no Q141K-stratified uricase clinical outcome in the sources searched for comp-019 as of 2026-05-08. This is a bounded search result, not proof of universal absence. Q141K therefore remains a prospective stratification variable rather than a computationally established response predictor.

## Current decision

No Phase B interpretation survives. The gut-lumen uricase track remains open, but dose, genotype response, topology, oxygen, peroxide, access, survival, and transit require direct measurement. [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md), [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md), and [validation experiment 1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) define the current gate.

The frozen inputs, code, invalidated outputs, and review receipts are in the [comp-019 experiment directory](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/).
