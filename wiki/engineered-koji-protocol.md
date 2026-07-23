---
title: "Engineered Koji UOX — Build, Measurement, and Falsification Plan"
date: 2026-04-21
tags: [koji, aspergillus-oryzae, uricase, engineering, phase-0]
related: [aspergillus-oryzae.md, koji-construct-design.md, uricase-variant-selection.md, validation-experiments.md, koji-endgame-strain.md]
sources:
  - https://www.uniprot.org/uniprotkb/Q00511/entry
  - https://www.ncbi.nlm.nih.gov/nuccore/X61766.1
  - https://pubmed.ncbi.nlm.nih.gov/1339455/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11051239/
---

# Engineered Koji UOX — Build, Measurement, and Falsification Plan

## 01 Track Question

Can a defined *Aspergillus oryzae* configuration produce reproducible active UOX, retain it through the intended process, and deliver activity to a physiological reaction site without unacceptable peroxide, host, barrier, or safety effects?

Koji is one candidate chassis. This plan does not select a UOX sequence, promoter, strain, topology, product format, dose, or animal model. Expression success advances only the tested configuration; failure redirects or kills that configuration rather than holding up Open Enzyme.

## 01b Natural Metabolite and Enzyme Baseline

Parental *A. oryzae* can produce digestive enzymes and strain- and process-dependent metabolites such as kojic acid and ergothioneine. Those are baseline analytes, not free therapeutic payloads.

For every engineered strain, compare the parental host, process-matched control, and engineered material for:

- amylase, protease, and lipase activity;
- kojic acid, ergothioneine, and other relevant metabolites;
- growth, sporulation, viability, and batch variance;
- contaminants and unexpected process products.

An engineered payload must not be credited with preserving or enhancing a native output until the matched assay shows it.

## 02 UOX Identity and Evidence

UOX sequence choice is governed by [variant selection](./uricase-variant-selection.md). *A. flavus* Q00511 is an initial comparator because it has an exact sequence record, biochemical literature, and recombinant-expression precedent. That history does not make it the best oral sequence or transfer systemic-product safety and efficacy to an engineered koji configuration.

For Q00511:

- UniProt contains a 302-residue precursor and annotates residues 2–302 as the 301-residue chain after initiator-methionine removal.
- GenBank X61766.1 supplies the 906-nt coding record excluding a stop codon.
- the construct record must state whether sequence and residue numbering include the initiator methionine and stop codon;
- the native C-terminal `SKL` targeting signal is a localization variable, not an instruction to remove or retain it by default.

Every build must record the accession and version, exact nucleotide and translated sequences, mutations, codon-design method, leader or anchor, linkers, tags, promoter, terminator, marker, integration boundaries, and sequence checksum.

## 03 Matched Construct Matrix

[Koji construct design](./koji-construct-design.md) owns the detailed matrix. Compare only interpretable changes:

| Axis | Candidate comparison | Required readouts |
|---|---|---|
| UOX identity | Accession-bound wild-type and justified engineered candidates | Identity, active oligomer, substrate response, oxygen and peroxide |
| Promoter | `amyB`, `glaA`, or defined constitutive candidates | Transcript, total/soluble/active UOX, burden and stability |
| Topology | Intracellular/release, secretion, surface display, recovered cell-free UOX | Fraction-specific active UOX, access, release, persistence and H₂O₂ |
| Copy strategy | Defined single- and multicopy integration candidates | Copy number, active output, growth and passage stability |
| Process | Submerged and solid-state conditions only where they answer the same question | Active UOX through harvest, processing, storage and transit challenge |

Published promoter strength or generic fungal-protein secretion does not supply a UOX yield. Do not combine several changing axes and then attribute the result to one component.

## 04 Transformation Options

Protoplast-mediated transformation, CRISPR-assisted integration, and *Agrobacterium*-mediated transformation are candidate methods. Select the method from the host background, desired locus, construct size, available controls, and required containment—not from a generic ranking.

For every route:

1. preserve an unmodified parental stock;
2. use an appropriate process-matched or marker control;
3. recover independent transformants rather than treating one colony as the construct;
4. verify the complete intended insertion and exclude material off-target changes before result-bearing comparison;
5. record passage history and test stability over the intended process.

This is institutional biosafety work. The page is not a home-transformation protocol.

## 05 Screening and Analytical Contract

### Construct identity

- junction PCR is a preliminary screen, not final identity;
- sequence the complete construct and integration boundaries;
- measure copy number when it is a design variable;
- verify the host background and strain purity.

### Step 5: Strain QC Infrastructure (Plasmidsaurus pipeline for plasmid → transformant → strain verification)

Use a staged sequencing workflow or an equivalent validated service:

1. verify the assembled plasmid or donor before transformation;
2. sequence the complete inserted construct and junctions in candidate transformants;
3. use whole-genome or targeted long-read analysis when off-target integration, rearrangement, copy state, or strain identity is load-bearing;
4. use RNA measurements only to localize an expression failure—short-read expression counts do not resolve cryptic splicing or full transcript structure;
5. retain machine-readable sequence records and checksums with the experiment.

The service provider is replaceable. The decision requirement is complete, auditable identity at the resolution needed for the claim.

### Product and host measurements

Report:

- total and active UOX by intracellular, surface, and extracellular fraction;
- active IU per culture volume, dry biomass, and final processed material;
- oligomeric state, aggregation, degradation, cleavage, and glycosylation where relevant;
- urate and reaction product over time, with substrate, pH, temperature, dissolved oxygen, and uncertainty;
- H₂O₂ time course and compartment-matched scavenger activity;
- growth, viability, host stress, genetic stability, and batch variance;
- native digestive-enzyme and metabolite outputs against parental controls.

Total protein, transcript, promoter strength, CFU, or biomass is not a delivered-activity or dose measurement.

## 06 Process and Transit Comparison

Test only process formats that remain plausible after construct characterization. For each format, use the same starting batch and measure active UOX before and after each step:

- fermentation and harvest;
- recovery or intended release;
- drying or other formulation workup;
- storage;
- sequential gastric and intestinal challenge;
- reaction-site assay under the §1.33 substrate, oxygen, access, peroxide, and persistence framework.

Fresh material, dried material, lysate, extracellular fraction, and cell-free UOX are separate configurations. No format is preferred from food tradition, presumed protection, or convenience.

Native digestive-enzyme survival is a separate question. It cannot select an engineered-UOX topology because the proteins, localization, processing, and failure modes differ.

## 07 Decision Sequence

1. **Identity gate:** exact construct, host, and copy state.
2. **Active-expression gate:** reproducible active UOX with interpretable localization, host effects, and variance.
3. **Physiological reaction gate:** [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial). A high-substrate benchmark alone does not pass.
4. **Process-retention gate:** only for a format carried forward from §1.33.
5. **Safety gate:** [validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay).
6. **Translation:** only a configuration that clears the preceding gates can inform a dynamic compartmental model and animal-study design.

COMP-019's unconditional flat-dose classification is not robust to [COMP-044's](./gut-lumen-uricase-physiologic-regime-computational.md) tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion. No expression result on this page can be converted directly into a serving, human dose, serum-urate effect, or chassis ranking.

## 08 Peroxide and Safety Boundary

UOX consumes oxygen and generates H₂O₂. Intracellular host catalase does not automatically protect a secreted, displayed, released, or cell-free reaction site. Measure UOX and scavenger localization, activity, stoichiometry, retention, diffusion, H₂O₂ time course, local exposure, and tissue or barrier effects for the same configuration.

Parent-organism food-use history does not transfer automatically to an engineered strain, new payload, new impurity profile, viable-organism format, or intended use. Advancing work requires institutional biosafety, containment, identity, contamination, metabolite, allergenicity/immunogenicity, and release review appropriate to the actual construct and process.

## 09 Falsification and Redirect Rules

| Result | Action |
|---|---|
| No reproducible active UOX | Diagnose sequence, expression, folding, oligomerization and assay recovery; stop the failed construct. |
| Active UOX but no reaction-site product formation | Stop or change topology, access, process or compartment; more expression alone is not a rescue. |
| Product formation with peroxide, viability or barrier failure | Stop escalation and test a justified compartment-matched mitigation or different topology. |
| Process destroys active UOX | Reject that process format; do not infer a chassis-wide failure. |
| No koji configuration clears §§1.33 and 1.36 | Close or redirect the engineered-koji UOX track and move to another gout exploit. |

## 15 Carnosine Co-Expression Module

Carnosine is an optional, separate hypothesis—not part of the active UOX build. Its proposed renal-transporter mechanism, intact exposure, carnosinase liability, biosynthetic precursor supply, expression, process retention, and interaction with other cassettes all require direct evidence.

[Validation §1.24](./validation-experiments.md#124-carnosine-co-expression-validation-in-a-oryzae-koji-endgame-optional-third-cassette) owns the current construct test. The experiment must begin with a sequence-verified single-cassette arm and measure carnosine identity and amount rather than inherit a yeast titer or a required daily intake.

Small peptide payloads exposed to an active-protease ferment require an explicit degradation time course. A generic “dried” or “fermented” label does not select a format. Add no third cassette until its single-cassette mechanism, exposure, burden, and safety evidence justify a new interaction study.

## 16 Lactoferrin Co-Expression Module

Ward 1992 and 1995 provide single-protein *Aspergillus* lactoferrin-expression precedents under different submerged processes. They do not establish solid-state output, dual-cassette compatibility, gout target engagement, or a delivered dose.

The current sequence is:

1. lactoferrin-only expression and product characterization may run independently;
2. the UOX-only leg must clear §1.33 in a koji-compatible topology;
3. a combined strain is built only after both single-cassette legs pass;
4. the combined strain is compared directly with the parental and both single-cassette controls.

[Koji multi-payload strain hypothesis](./koji-endgame-strain.md) and [validation §1.9](./validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate) own the interaction design. A favorable lactoferrin titer cannot rescue a failed UOX leg, and co-expression does not create an intermediate product claim.

## Primary Sources and Decision Records

- Legoux R et al. “Cloning and expression in *E. coli* of the gene encoding *A. flavus* urate oxidase.” *J Biol Chem* 1992;267:8565–8570. [PMID 1339455](https://pubmed.ncbi.nlm.nih.gov/1339455/). **In Vitro.**
- [UniProt Q00511](https://www.uniprot.org/uniprotkb/Q00511/entry) and [GenBank X61766.1](https://www.ncbi.nlm.nih.gov/nuccore/X61766.1). Primary sequence records.
- Huang Y et al. “*Aspergillus oryzae* as a cell factory.” 2024. [PMCID PMC11051239](https://pmc.ncbi.nlm.nih.gov/articles/PMC11051239/). Chassis and engineering review; not UOX evidence.
- Ward PP et al. “Production of biologically active recombinant human lactoferrin in *Aspergillus oryzae*.” *Biotechnology (N Y)* 1992;10:784–789. [PMID 1368268](https://pubmed.ncbi.nlm.nih.gov/1368268/). **In Vitro.**
- Ward PP et al. “A system for production of commercial quantities of human lactoferrin.” *Biotechnology (N Y)* 1995;13:498–503. [PMID 9634791](https://pubmed.ncbi.nlm.nih.gov/9634791/). **In Vitro.**
- [Koji construct screen](./koji-construct-design.md), [COMP-044](./gut-lumen-uricase-physiologic-regime-computational.md), and [validation experiments](./validation-experiments.md) are the current decision records.

## Related

- [*A. oryzae* chassis](./aspergillus-oryzae.md)
- [Uricase](./uricase.md)
- [Gut-lumen UOX sink](./gut-lumen-sink.md)
- [Koji multi-payload hypothesis](./koji-endgame-strain.md)
- [Validation experiments](./validation-experiments.md)
