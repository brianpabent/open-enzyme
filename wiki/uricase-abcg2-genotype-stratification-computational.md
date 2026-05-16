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
status: archived-to-experiments
---

# Gut-Lumen Uricase × ABCG2 Genotype Stratification + Flux Model (comp-019)

> **Frozen analysis archived to [`./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md`](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md)** (272 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/`.

There was a worry that the engineered-koji platform's whole therapeutic mechanism might only work in patients who carry a specific genetic variant — Q141K in the ABCG2 transporter — which is the #1 genetic risk factor for gout. About 25% of European-ancestry gout patients carry this variant; up to 50% of East-Asian-ancestry patients do. **If** the platform mechanism only worked in this subset, the addressable demographic would shrink dramatically and the trial design would have to change.

**Where the analysis lives:**
- Full archived analysis: [`./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md`](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/`](./etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
