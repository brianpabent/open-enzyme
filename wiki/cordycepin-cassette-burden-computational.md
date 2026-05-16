---
title: "Cordycepin (cns1+cns2) Cassette Metabolic Burden: Computational Analysis (comp-023)"
date: 2026-05-14
tags:
  - cordycepin
  - cns1
  - cns2
  - aspergillus-oryzae
  - koji
  - koji-endgame-strain
  - metabolic-burden
  - flux-balance-analysis
  - fba
  - genome-scale-metabolic-model
  - iWV1314
  - vongsangnak-2008
  - lactoferrin
  - uricase
  - kojic-acid
  - ergothioneine
  - carnosine
  - chaperone-orthogonal-stacking
  - cassette-compatibility
  - jeennor-2023
  - computational
  - comp-023
related:
  - computational-experiments.md
  - chaperone-orthogonal-stacking.md
  - koji-endgame-strain.md
  - medicinal-mushroom-complement-track.md
  - cassette-compatibility-computational.md
  - validation-experiments.md
sources:
  - "PMID 38071331 (Jeennor S et al. 2023, Microb Cell Fact). Efficient de novo production of bioactive cordycepin by Aspergillus oryzae using a food-grade expression platform; 564.64 ± 9.59 mg/L/day on glucose"
  - "PMID 29056419 (Xia Y et al. 2017, Cell Chem Biol). Fungal Cordycepin Biosynthesis Is Coupled with the Production of the Safeguard Molecule Pentostatin; original cns1+cns2+cns3 BGC characterization"
  - "PMC11300563 (Wang et al. 2023, Int Microbiol). A novel complementary pathway of cordycepin biosynthesis in Cordyceps militaris; confirms Cns1 = oxidoreductase, Cns2 = HDc-family phosphohydrolase, Cns3 = kinase"
  - "Yan et al. 2024, Front Chem Eng (doi 10.3389/fceng.2024.1446454). Prospects for cordycepin biosynthesis in microbial cell factories; cns1+cns2 sufficient for heterologous expression, host-derived 3'-AMP supply"
  - "PMID 18801187 (Vongsangnak W et al. 2008, BMC Genomics). Improved annotation through genome-scale metabolic modeling of Aspergillus oryzae; iWV1314 GEM source"
  - "BioModels MODEL1507180056; iWV1314 SBML deposit (2,361 reactions, 1,104 metabolites, 1,346 genes)"
  - "PMID 20650324 (Terabayashi Y et al. 2010, Fungal Genet Biol). Identification and characterization of genes responsible for biosynthesis of kojic acid"
  - "PMID 21514215 (Marui J et al. 2011, Appl Microbiol Biotechnol). Kojic acid biosynthesis in A. oryzae is regulated by a Zn(II)2Cys6 transcriptional activator"
  - "PMID 25496641 (Hu W et al. 2014, Org Lett). Bioinformatic and Biochemical Characterizations of C-S Bond Formation and Cleavage Enzymes in N. crassa Ergothioneine Biosynthetic Pathway"
  - "PMID 22276148 (Seebeck FP 2010, J Am Chem Soc / Bello MH 2012, Mol Microbiol). Ergothioneine biosynthesis EgtA-E mechanism"
status: complete (v1) — target deprioritized 2026-05-16
---

> **Target deprioritized 2026-05-16 — koji-cordycepin engineering removed from active cassette stack.** Strategic call during 2026-05-15 sweep walkthrough Item 7. comp-023's GREEN verdict on metabolic burden stands as a successful methodology validation (FBA on iWV1314 works; cytosolic-cassette burden modeling is reliable), but cordycepin is no longer an active koji engineering target. Three reasons:
>
> 1. **No novel chokepoint coverage.** Cordycepin's chokepoint targets (URAT1 modulation, AMPK / mitochondrial NLRP3-priming dampening) are already covered by the [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md) via cultivation of *Cordyceps militaris*, which natively co-produces cordycepin with pentostatin at the co-evolved ratio. Engineering cordycepin into koji duplicates coverage that exists in a peer track at a different chassis (cultivation vs. genetic engineering).
> 2. **Open dose-vs-achievable-titer gap.** comp-023 verified metabolic feasibility (cell carries the cassette at Jeennor 2023's 564 mg/L/day single-cassette optimized titer) but did NOT analyze whether that titer translates to a therapeutic dose in realistic home-fermentation conditions on a multi-cassette strain (uricase + lactoferrin competing for resources). Back-of-envelope at Jeennor's titer in a typical home batch lands at the LOW end of published nutraceutical doses (~70–280 mg/day vs 250–1500 mg/day target), assuming optimal titer transfer to home conditions and no multi-cassette penalty — both optimistic. The titer-to-therapeutic-dose conversion question was treated as out-of-scope by comp-023 and has not been closed by any subsequent analysis.
> 3. **Commercial availability.** Cordycepin from cultivated *C. militaris* extract is widely available at $20–60/month nutraceutical pricing, with native pentostatin co-protection. The "endgame strain = full coverage + simple" principle (per [`koji-endgame-strain.md`](./koji-endgame-strain.md)) does not justify the engineering complexity (three open follow-up gates: comp-025 ADA substrate competition, comp-026 multi-cassette induction interference, comp-023 v2 dynamic FBA validation) for a payload that delivers no novel coverage and may not reach therapeutic dose anyway.
>
> Active cordycepin route in the platform: cultivation per [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md). Active koji endgame strain cassettes (post-2026-05-16): uricase + lactoferrin + DAF SCR1-4 (the secreted-protein triple where koji has unique value via solid-state food-grade fermentation + home accessibility for proteins not otherwise easily obtained). See [`koji-endgame-strain.md` §"Evaluated and deprioritized"](./koji-endgame-strain.md). comp-025 / comp-026 / comp-023 v2 marked Deprioritized in [`computational-experiments.md`](./computational-experiments.md).

# Cordycepin (cns1+cns2) Cassette Metabolic Burden: Computational Analysis (comp-023)

> **Frozen analysis archived to [`../experiments/comp-023-cns1-cns2-metabolic-burden/wiki-archive.md`](../experiments/comp-023-cns1-cns2-metabolic-burden/wiki-archive.md)** (183 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `experiments/comp-023-cns1-cns2-metabolic-burden/`.

Does adding the bacterial **cns1+cns2 cordycepin biosynthesis pathway** (Jeennor 2023, [PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/), 564 mg/L/day in *A. oryzae*) on top of the dual uricase + lactoferrin cassette in the [koji-endgame-strain](./koji-endgame-strain.md) §1 design impose a prohibitive metabolic burden, defined by:

**Where the analysis lives:**
- Full archived analysis: [`../experiments/comp-023-cns1-cns2-metabolic-burden/wiki-archive.md`](../experiments/comp-023-cns1-cns2-metabolic-burden/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`../experiments/comp-023-cns1-cns2-metabolic-burden/`](../experiments/comp-023-cns1-cns2-metabolic-burden/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
