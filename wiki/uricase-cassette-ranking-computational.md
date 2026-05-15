---
title: "Uricase Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-022)"
date: 2026-05-14
tags:
  - computational
  - comp-022
  - clockbase-pattern
  - cassette-design
  - uricase
  - codon-optimization
  - signal-peptide
  - secretion-scaffold
  - chaperone-load
  - aspergillus-oryzae
  - ranking
related:
  - computational-experiments.md
  - autonomous-screening-methodology.md
  - cassette-compatibility-computational.md
  - chaperone-orthogonal-stacking.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - engineered-koji-protocol.md
  - digestive-enzyme-optimization.md
  - uricase-protease-stability-computational.md
sources:
  - "Sharp PM, Li WH. Nucleic Acids Res. 1987;15(3):1281-95 (PMID 3547335); CAI methodology"
  - "Kudla G, Murray AW, Tollervey D, Plotkin JB. Science 2009;324(5924):255-8 (PMID 19359587); 5' mRNA structure dominates initiation"
  - "Ward PP et al. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791); glucoamylase-KEX2 architecture"
  - "Huynh HH et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131); A. oryzae NSlD-ΔP10 antibody titer benchmark"
  - "Machida M et al. Nature 2005;438(7071):1157-61 (PMID 16372010); A. oryzae RIB40 genome / codon usage"
  - "Nakao Y et al. Nucleic Acids Res 1992;20 Suppl:2117 (PMID 1482437); A. oryzae codon usage reference"
  - "Tada S et al. PMID 1937733; PamyB Taka-amylase A promoter characterization"
  - "Punt PJ et al. PMID 2113023; PgpdA A. nidulans GAPDH promoter"
  - "Angov E. Biotechnol J 2009;4(11):1583-94 (PMID 18851725); codon harmonization"
  - "Ying K, Tyshkovskiy A, Gladyshev VN et al. bioRxiv 2023.02.28.530532v3 (PMC12667862, PMID 41332661); ClockBase autonomous screening"
status: complete (v1; fold-quality model deferred to wet-lab)
---

# Uricase Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-022)

> **Frozen analysis archived to [`../experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md)** (301 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `experiments/comp-022-clockbase-uricase-cassette-ranking/`.

Across the *A. oryzae* uricase expression cassette design space, parameterized as **6 promoters × 12 signal peptides × 10 codon variants × 60 secretion scaffolds = 43,200 combinations**, which cassettes survive a multi-model concordance gate and warrant promotion to the [§1.9 dual-cassette wet-lab feasibility test](./validation-experiments.md)?

**Where the analysis lives:**
- Full archived analysis: [`../experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`../experiments/comp-022-clockbase-uricase-cassette-ranking/`](../experiments/comp-022-clockbase-uricase-cassette-ranking/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
