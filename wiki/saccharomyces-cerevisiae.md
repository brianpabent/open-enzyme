---
title: Saccharomyces cerevisiae — UOX Chassis Evidence and Gates
aliases:
  - S. cerevisiae
  - baker's yeast
  - brewer's yeast
  - budding yeast
tags: [saccharomyces, yeast, uricase, chassis, phase-0]
related:
  - engineered-yeast-uricase-proposal.md
  - codon-optimization-expression-cassette.md
  - uricase-variant-selection.md
  - validation-experiments.md
sources:
  - https://doi.org/10.1016/0378-1119(92)90041-M
  - https://doi.org/10.1021/acssynbio.4c00831
---

# *Saccharomyces cerevisiae* — UOX Chassis Evidence and Gates

## Role in Scope

*S. cerevisiae* is a candidate host for building and measuring UOX configurations. The chassis remains conditional on active expression, localization, substrate access, reaction-site activity, peroxide control, viability, genetic stability, containment, and host-response measurements.

This page does not rank yeast against another chassis or treat yeast expression as evidence for an oral route.

## Direct Evidence

| Evidence | Level | Supported claim | Boundary |
|---|---|---|---|
| Leplatois et al. expressed active, soluble *Aspergillus flavus* UOX intracellularly in *S. cerevisiae*. | **In Vitro** | This host can produce active intracellular *A. flavus* UOX under the reported construct and culture conditions. | Does not establish release, secretion, physiological substrate access, oral delivery, dose, efficacy, or safety. |
| Wang et al. engineered uric-acid catabolism in *S. cerevisiae* and transferred the pathway to *S. boulardii*. | **In Vitro** | UOX identity, urate access, promoter context, and integration context can be varied and whole-cell uric-acid degradation measured in engineered yeast. | Does not select this project's host, payload, cassette, topology, or dose and does not establish activity at the human-baseline substrate prior. |

Systemic UOX evidence does not establish a yeast-derived oral configuration and is not used as a chassis decision here.

## Build Options

The chassis supports matched comparisons across these axes:

- Defined *S. cerevisiae* and *S. boulardii* strain backgrounds.
- Constitutive and inducible promoter candidates.
- Plasmid and defined chromosomal-integration strategies.
- Intracellular, secreted, and surface-displayed UOX cassettes.
- Whole-cell configurations with and without a defined urate-access component.
- Fresh-cell, extracellular, lysate, and processed fractions for activity recovery.

Select an option only from matched results. Within a comparison, hold payload sequence, promoter, terminator, copy strategy, host background, process, and assay constant except for the tested axis. The exact cassette matrix is maintained in [Yeast UOX Expression Cassette](./codon-optimization-expression-cassette.md).

## Required Chassis Measurements

### Identity and Stability

- Complete strain and construct identity.
- Locus or vector, orientation, and measured copy number.
- Viability, growth, passage history, genetic stability, and batch variance.

### Expression and Localization

- Transcript abundance when needed to localize failure.
- Total, soluble, intracellular, surface-associated, and extracellular UOX measured separately.
- Oligomeric state, degradation products, and active IU in each fraction.

### Reaction and Host Response

- Urate access, dissolved oxygen, UOX persistence, reaction product, and hydrogen peroxide over time.
- Viability during the reaction assay.
- Barrier and immune readouts for the exact engineered configuration against its parental-host and inactive-UOX controls.
- Containment and clearance measurements for any live configuration before downstream use.

Expression percentage, culture density, CFU, or recovered protein mass does not establish delivered activity or dose.

## Safety and Regulatory Boundary

Parent-organism food-use or regulatory status does not establish the safety or classification of an engineered strain, a live configuration, a killed preparation, or a recovered protein fraction. Evaluate the exact construct, host background, process state, exposure, containment, barrier effects, immune effects, urate removal, and peroxide burden.

No safety conclusion follows from an additive transgene description, absence of an intended virulence element, or prior use of the parental organism.

## Falsification Gates

1. Advance only a sequence-verified construct with reproducible active UOX, interpretable localization, viability, stability, and batch variance.
2. Represent the yeast configuration explicitly in [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) or a preregistered matched extension using the same substrate, oxygen, peroxide, controls, and decision rule.
3. A configuration that works only at a high-substrate benchmark remains physiologically unproven.
4. A §1.33 survivor must clear [validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay).
5. Failure of peroxide, viability, barrier, or antioxidant-loss criteria stops animal escalation for that configuration.

Only a configuration that clears §§1.33 and 1.36 can inform a dynamic compartmental model and animal-study design.

## Related Decision Pages

- [Engineered Yeast UOX — Current Research Plan](./engineered-yeast-uricase-proposal.md)
- [Yeast UOX Expression Cassette](./codon-optimization-expression-cassette.md)
- [UOX Variant Selection](./uricase-variant-selection.md)
- [COMP-044 physiological-regime audit](./gut-lumen-uricase-physiologic-regime-computational.md)
- [Validation experiments](./validation-experiments.md)

## Primary Sources

- Leplatois P, et al. High-level production of a peroxisomal enzyme: *Aspergillus flavus* uricase accumulates intracellularly and is active in *Saccharomyces cerevisiae*. *Gene*. 1992;122(1):139–145. [doi:10.1016/0378-1119(92)90041-M](https://doi.org/10.1016/0378-1119(92)90041-M). **In Vitro.**
- Wang et al. Systematic Engineering for Efficient Uric Acid-Degrading Activity in Probiotic Yeast *Saccharomyces boulardii*. *ACS Synthetic Biology*. 2025;14(6):2030–2043. [doi:10.1021/acssynbio.4c00831](https://doi.org/10.1021/acssynbio.4c00831). **In Vitro.**
