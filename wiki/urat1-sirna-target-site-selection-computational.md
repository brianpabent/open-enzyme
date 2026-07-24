---
title: "URAT1 mRNA Target-Site Selection — COMP-009 Invalidated"
date: 2026-05-16
tags:
  - sirna
  - urat1
  - slc22a12
  - target-site-selection
  - computational-experiment
  - comp-009
related:
  - sirna-urat1-modality.md
  - hypotheses/H03-sirna-urat1-thesis.md
  - computational-experiments.md
sources:
  - "Reynolds et al. Nature Biotechnology 2004; DOI 10.1038/nbt936"
  - "Ui-Tei et al. Nucleic Acids Research 2004; DOI 10.1093/nar/gkh247"
  - "Tafer et al. Nature Biotechnology 2008; DOI 10.1038/nbt1404"
status: invalidated-comp-output
---

# URAT1 mRNA Target-Site Selection — COMP-009 Invalidated

COMP-009 does not establish a usable URAT1 siRNA guide, target-site tractability, accessibility, specificity, cross-species reuse, or support for [H03](./hypotheses/H03-sirna-urat1-thesis.md). No candidate sequence, funnel count, rank, score, shortlist, GREEN verdict, or P2-2 closure survives. The [artifact](./etc/experiments/comp-009-urat1-sirna-target-site-selection/) is a non-runnable, hash-bound tombstone.

## Why the result is invalid

The rerun used RefSeq NM_144585.4, correcting the original artificial back-translated CDS. Its decision model remained invalid:

- The Reynolds implementation applied cited sense-strand positional preferences to the antisense strand, omitted terminal-stability and inverted-repeat criteria, and substituted a four-base homopolymer check. [Reynolds et al.](https://doi.org/10.1038/nbt936)
- The Ui-Tei gate did not require the cited terminal-composition, A/U-richness, and long-GC-stretch conditions simultaneously. [Ui-Tei et al.](https://doi.org/10.1093/nar/gkh247)
- RNAplfold accessibility had no acceptance threshold. Five shortlisted windows produced a GREEN verdict regardless of their accessibility values.
- The composite score used uncalibrated weights and allowed protein conservation to dominate the accessibility term. It was not the calibrated and independently tested RNAxs method. [Tafer et al.](https://doi.org/10.1038/nbt1404)
- No transcriptome or 3′-UTR off-target clearance was performed; only one transcript was scanned; protein conservation cannot establish cross-species guide reuse; and one boundary-spanning window was mislabeled by a midpoint rule.
- No candidate was tested for intracellular activity, URAT1 knockdown, target-cell uptake, urate transport, or renal safety.

## What survives

The historical rerun examined NM_144585.4, but that fact has no predictive or decision use. The [URAT1-siRNA hypothesis](./sirna-urat1-modality.md) survives independently of COMP-009.

Selective proximal-tubule delivery is the upstream gate. [COMP-048](./etc/experiments/comp-048-human-proximal-tubule-delivery-handle-screen/) is designed to ask whether an internalizing surface receptor co-localizes with SLC22A12-positive human proximal-tubule cells selectively enough to justify receptor-targeted delivery work.

A new guide-design COMP is deferred until a delivery route survives. It must use a validated current design method, cover relevant SLC22A12 transcripts and human variation, perform transcriptome-wide off-target analysis, keep accessibility separate from other evidence dimensions, and require empirical URAT1 knockdown before a guide advances.
