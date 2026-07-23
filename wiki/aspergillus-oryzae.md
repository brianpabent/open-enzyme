---
title: "Aspergillus oryzae (Koji)"
date: 2026-04-21
tags: [Aspergillus-oryzae, koji, fermentation, enzyme-production, uricase]
related: [koji-track.md, engineered-koji-protocol.md, koji-construct-design.md, validation-experiments.md]
---

# *Aspergillus oryzae* (Koji)

*Aspergillus oryzae* is a filamentous fungus used in East Asian food fermentation and supported by mature genetic and fermentation tools. Open Enzyme tests it as one possible production and delivery chassis for specific gout-relevant payloads. Its food-use history and native enzyme secretion justify experiments; they do not establish safety, dose, efficacy, or superiority for an engineered strain.

## Native biology relevant to the track

During solid-state growth on grain, *A. oryzae* produces amylases, proteases, and lipases that break down starch, protein, and fat. It also produces a substrate- and strain-dependent secondary-metabolite background that may include kojic acid, ergothioneine, and ferulic acid.

These outputs create two distinct questions:

1. Can a defined native enzyme or metabolite be measured reproducibly in the intended process?
2. Does an engineered payload preserve, alter, or eliminate that native output?

An in-vitro anti-inflammatory mechanism or a fermentation titer does not establish therapeutic exposure. Compare parental and engineered strains under the same process and report the measured output and uncertainty.

The separate wild-type food-fermentation track is documented in [Koji Home Fermentation](./koji-home-fermentation.md). It is not a production protocol for an engineered strain.

## Engineering toolkit

Candidate tools include protoplast-mediated transformation, *Agrobacterium*-mediated transformation, CRISPR/Cas9, auxotrophic selection, and chromosomal integration. Promoter and signal-peptide behavior is protein-, strain-, substrate-, and process-dependent.

For UOX work:

- `amyB`, `glaA`, and constitutive promoters are candidates to compare;
- intracellular/release, secretion, surface display, and cell-free recovery remain unranked topologies;
- `pyrG`, `niaD`, or another justified marker/integration system must be evaluated in the actual host;
- construct identity, copy number, stability, and off-target integration require direct verification.

See the [matched UOX construct screen](./koji-construct-design.md) for the build contract.

## UOX hypothesis

The track asks whether *A. oryzae* can produce active UOX in a configuration that survives processing and functions at an intestinal reaction site. Manufacturing precedent for recombinant proteins in fungi does not answer that question.

### Required measurements

- UOX identity and mass in intracellular, surface, and extracellular fractions;
- active IU per culture volume, dry biomass, and final processed material;
- soluble fraction, oligomer state, aggregation, processing cleavage, and glycosylation where relevant;
- strain and batch reproducibility;
- retained activity through the intended fermentation, harvest, drying/formulation, and simulated-transit sequence;
- substrate removal, oxygen dependence, peroxide, access, and persistence under [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

General fungal-protein yields, promoter strength, related-species codon usage, or native digestive-enzyme output cannot be converted into a UOX titer, serving, dose, or therapeutic claim.

## Reaction-site peroxide

UOX consumes urate and oxygen and produces hydrogen peroxide. Peroxide control depends on reaction-site topology and measured scavenger capacity.

Intracellular co-localization with host catalase is a hypothesis until localization and activity are measured. Secreted or surface-displayed UOX cannot be assumed to inherit intracellular catalase protection. Measure UOX activity, H₂O₂ time course, catalase activity, viability or tissue effects, and failure modes for every advancing topology. See [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md) and [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

## Processing and format gates

Fresh material, dried material, lysate, purified enzyme, and other formulations expose UOX to different thermal, proteolytic, localization, and containment constraints. No format is selected from generic heat-stability or food-use assumptions.

For each candidate format, measure:

- active UOX before and after processing and storage;
- organism viability and containment status;
- release and access in the target compartment;
- impurities, native metabolites, and batch variance;
- peroxide control and relevant safety endpoints.

The output is an assay-qualified research configuration, not a home-use or dosing protocol.

## Engineered-strain safety boundary

Food-use history applies to established wild-type production organisms and processes; it does not automatically transfer to a modified strain, new payload, new impurities, or new intended use. Advancing constructs require institutional biosafety, containment, identity, contamination, metabolite, allergenicity/immunogenicity, and product-release review appropriate to the work.

ALLN-346 and rasburicase provide evidence about their own enzyme products and routes. They do not establish oral tolerance, efficacy, or safety for an engineered *A. oryzae* product.

## Multi-cassette boundary

UOX plus lactoferrin or another payload is a later configuration, not an assumed end state. Each single-cassette leg must pass its own expression, activity, processing, reaction-site, and safety gates before a combined strain is justified. Published multi-gene integration and single-protein secretion precedents do not predict combined active output.

The [koji endgame strain](./koji-endgame-strain.md) holds that conditional multi-payload hypothesis. Genuine cross-chassis comparison belongs in [modality-chokepoint-matrix.md](./modality-chokepoint-matrix.md) and [chassis-pending-interventions.md](./chassis-pending-interventions.md), not here.

## Decision rule

| Result | Action |
|---|---|
| A configuration produces reproducible active UOX and clears §1.33 | Advance it to [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay). |
| Expression is high but reaction-site activity is low | Diagnose topology, access, processing, oxygen, and persistence; do not infer that more yield solves it. |
| UOX activity passes but peroxide or safety fails | Test a justified scavenger or different topology; do not promote the current construct. |
| No *A. oryzae* configuration clears the gates | Document the failure and redirect the payload or test another gout exploit. |

## Sources

- [Genome sequence of *A. oryzae*](https://www.nature.com/articles/nature04300)
- [*A. oryzae* as a cell factory](https://pmc.ncbi.nlm.nih.gov/articles/PMC11051239/)
- [Promoter tools for *A. oryzae*](https://fungalbiolbiotech.biomedcentral.com/articles/10.1186/s40694-020-00093-1)
- [Codon optimization in *A. oryzae*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2576710/)
- [Filamentous-fungal protein-expression engineering](https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2020.00293/full)
