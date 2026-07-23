---
title: "Uricase Protein-Engineering Candidate Screen"
date: 2026-04-21
tags: [uricase, protein-engineering, stability, protease-resistance, computational-design]
related: [uricase-variant-selection.md, gi-survival-prediction.md, validation-experiments.md]
---

# Uricase Protein-Engineering Candidate Screen

This page defines a falsifiable screen for UOX sequence changes. It does not predict gastrointestinal survival, delivered dose, serum-urate effect, safety, or a winning variant.

## Question

Can a sequence change reproducibly improve retained active UOX through the intended production, processing, and reaction-site challenges without unacceptable losses in expression, folding, oligomerization, baseline catalysis, or peroxide control?

Disulfide, salt-bridge, loop-rigidity, surface-charge, and cleavage-site changes are hypotheses. A structure score does not establish that a new bond forms, that the biological oligomer remains active, or that the construct survives the relevant process.

## Candidate set

Use wild type as the anchor and retain single-change controls for every combination. The initial *A. flavus* UOX set may include:

| ID | Design hypothesis | Required control |
|---|---|---|
| SB-1 | A6C plus a geometry-verified partner near position 290 | Each single-Cys construct and wild type |
| BAL-1 | A bounded set of charge/loop changes chosen before the run | Every component mutation and wild type |
| OPT-1 | BAL-1 plus a second geometry-verified disulfide pair | BAL-1, each Cys single, the pair alone, and wild type |

The second-disulfide partner is not fixed by this page. `S119C/C220C` may remain a candidate only after residue numbering, biological-assembly geometry, and primary-source provenance are verified. Do not use `OPT-1` as shorthand for a validated S119C/C220C product.

## Pre-synthesis checks

1. Confirm the exact parent sequence, accession, construct boundaries, residue numbering, and biological oligomer.
2. Inspect every proposed change in the biological assembly, not only a monomer.
3. For disulfide proposals, test sulfur geometry and alternative pairing; reject unpaired or ambiguous cysteine sets.
4. Exclude changes that contact the active site, substrate path, oligomer interface, or known processing site unless that interaction is the explicit test.
5. Record the evidence tier for each proposal. Computational geometry or energy is **Mechanistic Extrapolation** until expressed and measured.

## Computational triage

FoldX, Rosetta, molecular dynamics, and structure prediction may reject obviously poor candidates or identify competing mechanisms. They do not supply an empirical stability correction factor.

For FoldX-style mutation calculations, define the sign convention in the run artifact. Under the common `ΔΔG = ΔG_mutant − ΔG_wild-type` convention, positive values are destabilizing and negative values are stabilizing; never import a threshold without confirming the tool and command's definition. Do not multiply predicted disulfide effects by a generic correction factor.

Record:

- input structure and biological assembly;
- prepared coordinates and protonation choices;
- exact mutation and chain mapping;
- replicate scores and dispersion;
- alternative cysteine pairings or interface states;
- conflicts among methods.

A favorable calculation admits a candidate to the wet-lab screen; it does not assign a survival percentage or expected improvement.

## Matched experimental matrix

### Baseline characterization

For every construct, measure identity, soluble expression, oligomeric state, aggregation, baseline activity, substrate response, oxygen dependence, and peroxide generation under the same assay conditions.

### Sequential challenge

Use the exact intended production and delivery format. Predeclare challenge composition, pH, temperature, exposure time, protease concentration, sampling points, and workup. Measure retained active UOX after each step rather than multiplying independent survival assumptions.

At minimum compare:

- production and harvest;
- drying or formulation, if proposed;
- gastric challenge;
- intestinal challenge;
- reaction-site substrate, oxygen, access, and persistence conditions from [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial), after the exact configuration has been built and characterized in the relevant construct-supply work (§§1.1, 1.2, and 1.5) or supplied as an exact external configuration.

### Advancement rule

A combination advances only when it reproducibly exceeds wild type and the simpler candidates in retained active UOX, and the gain is not offset by lower baseline activity, lower expression, altered oligomerization, aggregation, or worse peroxide behavior. Set numerical thresholds only after an assay-precision pilot and independent review.

## Safety boundary

Host food-use history, a distal mutation, or unchanged annotated catalytic residues do not establish safety of an engineered protein or organism. The screen must not label a construct GRAS-compatible, non-immunogenic, off-target-free, or safe by design.

Any advancing candidate still requires:

- identity and impurity characterization;
- substrate-selectivity and coproduct measurement;
- epithelial or tissue-safety testing appropriate to the route;
- immunogenicity assessment appropriate to exposure;
- engineered-organism containment and product-release criteria;
- regulatory analysis for the actual construct, process, and intended use.

## Decision outcomes

| Result | Interpretation |
|---|---|
| Combination beats wild type and every simpler control | The combination earns topology-specific validation; causality remains decomposable through the controls. |
| A single change matches or beats the combination | Prefer the simpler candidate and retire unsupported components. |
| Structure scores improve but measured active retention does not | Retire the score-based hypothesis for this context. |
| All candidates fail the reaction-site or safety gate | Stop optimizing this sequence family or delivery configuration and test another exploit. |

## Output contract

Report measured results with uncertainty and failure modes. Do not translate a sequence score, retained-activity percentage, expression yield, or favorable challenge result directly into oral dose, biomass, CFU, serum response, product format, or chassis ranking.

[COMP-044](./gut-lumen-uricase-physiologic-regime-computational.md) found that the legacy unconditional flat-dose classification was not robust to its tested substrate-occupancy and finite-window diagnostics; it did not identify the true physiological regime or reverse the old conclusion. [Validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) compares exact, already characterized configurations. Topology nomination is valid only within a controlled host comparison; cross-host results remain configuration-specific. [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) must pass before animal escalation.
