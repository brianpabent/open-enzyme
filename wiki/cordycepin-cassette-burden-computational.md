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

# Cordycepin (cns1+cns2) Cassette Metabolic Burden: Computational Analysis (comp-023)

## Current status

The *cns1+cns2* cordycepin cassette is deprioritized. Cultivated *Cordyceps militaris* remains the controlled-material route for investigating native cordycepin/pentostatin biology; there is no current reason to add a cordycepin cassette to an engineered *A. oryzae* configuration.

## Evidence boundary

Jeennor et al. reported heterologous cordycepin production in *A. oryzae* at 564.64 ± 9.59 mg/L/day under their optimized conditions ([PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/)). COMP-023 asked whether the modeled *cns1+cns2* pathway imposed a prohibitive stoichiometric burden in iWV1314. Its qualitative result is a heuristic burden prior, not a validated flux result. It does not establish multi-cassette growth, cordycepin productivity, material identity, delivered exposure, safety, or efficacy.

## Reopen gate

Reconsider the cassette only if a non-duplicative biological role requires cordycepin production in the same exact configuration. A new experiment would need a current model and exact construct inputs, prespecified burden and productivity rules, independent pre-run and post-run review, and wet-lab confirmation of growth and product identity.

## Artifact links

- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-023-cns1-cns2-metabolic-burden/`](./etc/experiments/comp-023-cns1-cns2-metabolic-burden/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)
- Related native-compound track: [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md)
