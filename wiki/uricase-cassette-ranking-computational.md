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
  - etc/autonomous-screening-methodology.md
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
status: corrective review open; current shortlist non-authoritative
---

# Uricase Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-022)

> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-022-clockbase-uricase-cassette-ranking/`.

Across the *A. oryzae* uricase expression cassette design space, parameterized as **6 promoters × 12 signal peptides × 10 codon variants × 60 secretion scaffolds = 43,200 combinations**, which cassettes survive a multi-model concordance gate?

> **Current evidence boundary:** COMP-022 enumerates hypotheses inside a koji cassette-design space, but its current shortlist and “winner” labels are non-authoritative. One concordance axis uses uncalibrated chaperone-load coefficients inherited from the retired folding-score framework; the remaining axes also predict different intermediate properties rather than a shared measured outcome. The open [COMP-022 review](../synthesis/queue/comp-review-022.md) must recompute or retire the affected ranking before any candidate is promoted. Separately, [§1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) must determine whether an exact koji-compatible configuration functions under physiological substrate, oxygen, peroxide, localization, and viability conditions.

**Where the analysis lives:**
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/`](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
