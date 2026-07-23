---
title: Engineered Yeast UOX — Current Research Plan
date: 2026-04-01
tags: [uricase, yeast, engineering, gout, phase-0]
related:
  - codon-optimization-expression-cassette.md
  - saccharomyces-cerevisiae.md
  - uricase-variant-selection.md
  - gut-lumen-uricase-physiologic-regime-computational.md
  - validation-experiments.md
  - hypotheses/H08-gut-lumen-sink-platform-thesis.md
sources:
  - https://doi.org/10.1016/0378-1119(92)90041-M
  - https://doi.org/10.1021/acssynbio.4c00831
---

# Engineered Yeast UOX — Current Research Plan

**Phase:** Phase 0 — Research & Design

## Decision in Scope

Determine whether an engineered *Saccharomyces* configuration can produce reproducible active urate oxidase (UOX), deliver that activity to the intended reaction compartment, and pass the physiological-reaction and safety gates.

This page does not select a UOX variant, yeast strain, promoter, copy strategy, topology, formulation, dose, or animal model.

## Evidence That Supports a Yeast Build

| Evidence | Level | What it supports | What it does not support |
|---|---|---|---|
| Leplatois et al. expressed active, soluble *Aspergillus flavus* UOX intracellularly in *S. cerevisiae*. | **In Vitro** | Active expression of this enzyme-host combination is experimentally possible. | Oral delivery, release, substrate access, physiological-rate activity, peroxide control, dose, efficacy, or safety. |
| Wang et al. engineered uric-acid catabolism in *S. cerevisiae* and transferred the pathway to *S. boulardii*, varying the UOX, urate transporter, promoters, and integration loci. | **In Vitro** | Whole-cell uric-acid degradation is measurable in engineered yeast, and payload access plus cassette context are experimental variables. | Selection of this project's host, payload, cassette, or topology; activity at the human-baseline substrate prior; a sufficient dose; systemic urate reduction; or an acceptable safety profile. |

[COMP-044](./gut-lumen-uricase-physiologic-regime-computational.md) is a **Mechanistic Extrapolation** and consistency audit. COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion.

## Matched Build Matrix

Change one axis at a time or preregister a factorial design. Within a topology comparison, hold the UOX sequence, promoter, terminator, copy strategy, host background, culture conditions, and assay constant.

| Axis | Comparisons to construct | Required control |
|---|---|---|
| UOX identity | Exact accession and sequence candidates routed from [variant selection](./uricase-variant-selection.md) | Sequence-verified inactive-UOX counterpart where feasible |
| Host background | Defined *S. cerevisiae* and *S. boulardii* backgrounds | Parental host under the same process |
| Transcription | Constitutive and inducible promoter candidates | Same topology, locus or vector, and UOX sequence |
| Topology | Intracellular/no leader; secreted/defined leader; surface-displayed/defined anchor; recovered cell-free UOX | Fraction-matched inactive UOX and chassis-only controls |
| Substrate access | Whole-cell configuration with and without a defined urate-access component | Matched transport-inactive or no-transporter control |
| Copy strategy | Plasmid and defined chromosomal integration options | Measured copy number and genetic stability |
| Process state | Fresh cells, recovered extracellular fraction, lysate, or processed preparation | Activity measured before and after each process step |
| Peroxide handling | No mitigation and compartment-matched mitigation candidates | Matched inactive UOX at the same oxygen condition |

No result on one axis is evidence for another. Total protein does not select topology; whole-cell urate disappearance does not establish UOX localization; retained activity after processing does not establish physiological reaction-site activity.

## Required Measurements

### Construct and Expression

- Full construct sequence, host background, locus or vector, orientation, and measured copy number.
- Transcript abundance when needed to distinguish transcription from post-transcriptional failure.
- Total, soluble, intracellular, surface-associated, and extracellular UOX.
- Oligomeric state and active UOX reported separately from total protein.
- Viability, growth, genetic stability, and batch variance.

### Processing and Access

- Active UOX before and after the complete proposed processing and simulated-transit sequence.
- Release or secretion kinetics in the relevant fraction.
- Urate access and dissolved oxygen measured with the activity result.
- Urate, reaction product, hydrogen peroxide, and viability measured over time.

Expression output must be reported as active IU per culture volume and dry biomass, with CFU where live cells are used. These measurements are not a dose calculation.

## Falsification Gates

1. **Expression entry gate:** Advance only a sequence-verified construct with reproducible active UOX and interpretable localization, viability, and batch variance.
2. **Physiological reaction-site gate:** Test the yeast configuration in [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) or a preregistered matched extension using the same substrate, oxygen, peroxide, control, and decision framework. A result only at the high-substrate benchmark does not establish physiological activity.
3. **Safety gate:** A §1.33 survivor must clear [validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay). Lower peroxide alone does not pass if barrier injury persists after urate removal.
4. **Downstream escalation:** Only a configuration that clears §§1.33 and 1.36 can inform a dynamic compartmental model and subsequent animal-study design.

## Stop or Redirect Rules

- No reproducible active UOX: stop that construct and diagnose sequence, transcription, solubility, assembly, localization, or assay recovery before changing another axis.
- Active UOX without reaction-site product formation: do not advance the topology.
- Product formation without acceptable peroxide and viability: stop or alter the compartment and mitigation strategy, then repeat the gate.
- Failure of §1.36: do not proceed to animal efficacy work.
- A failure updates only the tested sequence, host, topology, or process configuration; it does not decide unrelated gout tracks.

## Boundaries

- No human-use or dosing recommendation follows from these experiments.
- Parent-organism food-use or regulatory status is not transferred to an engineered strain or purified payload.
- Intravenous UOX products do not establish an oral yeast route.

## Primary Sources and Decision Records

- Leplatois P, et al. High-level production of a peroxisomal enzyme: *Aspergillus flavus* uricase accumulates intracellularly and is active in *Saccharomyces cerevisiae*. *Gene*. 1992;122(1):139–145. [doi:10.1016/0378-1119(92)90041-M](https://doi.org/10.1016/0378-1119(92)90041-M). **In Vitro.**
- Wang et al. Systematic Engineering for Efficient Uric Acid-Degrading Activity in Probiotic Yeast *Saccharomyces boulardii*. *ACS Synthetic Biology*. 2025;14(6):2030–2043. [doi:10.1021/acssynbio.4c00831](https://doi.org/10.1021/acssynbio.4c00831). **In Vitro.**
- [COMP-044 physiological-regime audit](./gut-lumen-uricase-physiologic-regime-computational.md). **Mechanistic Extrapolation.**
- [Validation experiments §§1.33 and 1.36](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).
