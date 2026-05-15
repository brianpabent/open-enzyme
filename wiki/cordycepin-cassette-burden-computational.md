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
status: complete (v1)
---

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
