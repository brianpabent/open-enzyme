---
title: "DAF/CD55 SCR1-4 Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-030)"
date: 2026-05-15
tags:
  - computational
  - comp-030
  - clockbase-pattern
  - cassette-design
  - daf
  - cd55
  - scr14
  - ccp-fold
  - codon-optimization
  - signal-peptide
  - secretion-scaffold
  - chaperone-load
  - aspergillus-oryzae
  - ranking
  - alpha-coefficient
related:
  - daf-cd55-scr14-truncated-computational.md
  - uricase-cassette-ranking-computational.md
  - validation-experiments.md
  - chaperone-orthogonal-stacking.md
  - etc/autonomous-screening-methodology.md
  - cassette-compatibility-computational.md
  - engineered-koji-protocol.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - computational-experiments.md
sources:
  - "Sharp PM, Li WH. Nucleic Acids Res. 1987;15(3):1281-95 (PMID 3547335); CAI methodology"
  - "Kudla G, Murray AW, Tollervey D, Plotkin JB. Science 2009;324(5924):255-8 (PMID 19359587); 5' mRNA structure dominates translation initiation"
  - "Schmidt CQ et al. J Mol Biol 2010;396(1):1-10 (PMC2806952); NMR/SAXS CCP rigid-unit evidence (alpha-coefficient primary source)"
  - "Huynh HH et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131); A. oryzae NSlD-ΔP10 PDI-load capacity calibration"
  - "Machida M et al. Nature 2005;438(7071):1157-61 (PMID 16372010); A. oryzae RIB40 genome / codon usage"
  - "Nakao Y et al. Nucleic Acids Res 1992;20 Suppl:2117 (PMID 1482437); A. oryzae codon usage reference"
  - "Tada S et al. PMID 1937733; PamyB Taka-amylase A promoter"
  - "UniProt P08174 (human DAF/CD55 SV=4); DISULFID feature annotations for SCR1-4; verified 2026-05-06 + 2026-05-15"
  - "Verkuil R et al. bioRxiv 2022; Hsu C et al. 2022; ESM2 pseudo-likelihood fold-quality proxy"
  - "Ward PP et al. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791); glucoamylase-KEX2 architecture"
status: complete (v1, 2026-05-15)
---

# DAF/CD55 SCR1-4 Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-030)

> **Frozen analysis archived to [`../experiments/comp-030-daf-cassette-ranking/wiki-archive.md`](../experiments/comp-030-daf-cassette-ranking/wiki-archive.md)** (398 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `experiments/comp-030-daf-cassette-ranking/`.

Across the *A. oryzae* DAF/CD55 SCR1-4 expression cassette design space, parameterized as **6 promoters × 12 signal peptides × 10 codon variants × 60 secretion scaffolds = 43,200 combinations**, which cassettes survive a multi-model concordance gate and warrant promotion to the [§1.25 wet-lab feasibility test](./validation-experiments.md)?

**Where the analysis lives:**
- Full archived analysis: [`../experiments/comp-030-daf-cassette-ranking/wiki-archive.md`](../experiments/comp-030-daf-cassette-ranking/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`../experiments/comp-030-daf-cassette-ranking/`](../experiments/comp-030-daf-cassette-ranking/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
