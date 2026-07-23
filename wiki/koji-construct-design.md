---
title: "A. oryzae UOX Construct Screen"
date: 2026-04-21
tags: [koji, Aspergillus-oryzae, uricase, construct-design, fermentation]
related: [engineered-koji-protocol.md, protein-engineering-strategy.md, validation-experiments.md, aspergillus-oryzae.md]
---

# *A. oryzae* UOX Construct Screen

This page defines a matched construct screen for asking whether *A. oryzae* can produce active UOX in a topology that survives the intended process and functions at the reaction site. It does not select secretion, predict a yield, establish a serving, or rank koji against another chassis.

## Sequence contract

Each build starts from an accession-bound amino-acid sequence and a synthesis record. UniProt Q00511 contains a 302-residue precursor; its annotated chain is residues 2–302, or 301 residues after initiator-methionine removal. GenBank X61766.1 supplies the 906-nt coding record excluding a stop codon. Record whether a construct and its residue numbering include the initiator methionine and stop codon. Do not reuse the conflicting 273-aa/819-bp description from earlier drafts.

Record:

- parent accession and sequence checksum;
- wild-type versus engineered mutations;
- codon-optimization method and final coding sequence;
- signal peptide, linker, tags, terminator, marker, and integration boundaries;
- expected localization as a hypothesis, not an observed result.

## Matched construct matrix

Use the same parent sequence, promoter class, integration strategy, and assay wherever the topology permits.

| Arm | Construct question | Required measurements |
|---|---|---|
| Intracellular/release | Is active oligomer produced, retained through processing, and released in the relevant compartment? | Total and active UOX by fraction; release kinetics; oligomer state; retained activity after processing and transit. |
| Direct secretion | Does a native *A. oryzae* signal peptide yield active extracellular UOX without damaging folding or increasing proteolysis? | Intracellular and supernatant mass/activity; signal cleavage; glycosylation; oligomer state; extracellular proteolysis. |
| Surface display | Does tethering improve reaction-site access without blocking assembly or activity? | Surface localization; active UOX per biomass; substrate access; shedding; peroxide at the reaction site. |
| Cell-free product | Does recovered UOX retain more usable activity than organism-associated formats? | Recovery, purity, retained activity, formulation stability, oxygen and peroxide behavior. |

`amyB`, `glaA`, and constitutive promoters are candidates to compare. `amyB` and `glaA` signal peptides are secretion candidates, not defaults. Published behavior with other proteins does not justify a UOX secretion percentage.

## Build controls

- parental *A. oryzae* processed identically;
- promoter-only or marker control as appropriate;
- wild-type UOX alongside any engineered variant;
- topology-matched inactive or no-UOX control for peroxide and matrix effects;
- at least two independent verified integrants per build before treating a result as construct-level.

Confirm integration identity and copy number before comparing expression. Measure transcription only as a diagnostic; the decision variable is active UOX in the relevant fraction and final processed material.

## Measurement contract

Report:

- total UOX identity and mass by intracellular, surface, and extracellular fraction;
- active IU per culture volume, dry biomass, and wet/dry final material;
- soluble fraction, oligomer state, aggregation, processing cleavage, and glycosylation where relevant;
- batch variance and strain stability;
- retained activity after the actual fermentation, harvest, drying/formulation, and simulated-transit sequence;
- substrate removal, oxygen dependence, peroxide, access, and persistence under [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

General fungal secreted-protein titers, promoter strength, copy number, or native-enzyme output cannot be converted into a UOX yield, therapeutic dose, or product claim. Native digestive-enzyme performance is a separate measurement and does not prove that UOX expression maintains or enhances the combined product.

## Iteration logic

| Observation | Next experiment |
|---|---|
| Transcript present; little UOX protein | Check translation, degradation, integration context, and construct identity. |
| Protein present; low active fraction | Check folding, oligomerization, glycosylation, processing, and aggregation. |
| Active intracellular UOX; poor release/access | Compare release and alternative topology arms rather than assuming more expression solves delivery. |
| Active extracellular UOX; poor processing retention | Test formulation/process protection and proteolysis before scaling expression. |
| Reaction-site activity passes but peroxide fails | Test matched scavenger topology/capacity; do not promote the UOX construct alone. |
| No arm clears §1.33 | Stop or redirect the *A. oryzae* UOX configuration. |

## Advancement boundary

A topology advances only after it produces reproducible active UOX and clears the physiological substrate, oxygen, peroxide, access, and persistence comparison in §1.33. [Validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) then determines whether animal escalation is justified. Expression yield alone cannot establish dose sufficiency or make a format shippable.

## Sources

- [Promoter tools for *A. oryzae*](https://fungalbiolbiotech.biomedcentral.com/articles/10.1186/s40694-020-00093-1)
- [amyB promoter functional elements](https://pubmed.ncbi.nlm.nih.gov/10052139/)
- [Codon optimization in *A. oryzae*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2576710/)
- [Protein secretion systems in *A. oryzae*](https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-8-73)
- [Filamentous-fungal protein-expression engineering](https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2020.00293/full)
