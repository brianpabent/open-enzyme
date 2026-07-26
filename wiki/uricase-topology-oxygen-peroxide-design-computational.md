---
title: "Uricase Topology × Oxygen × Peroxide — Computational Design (comp-045)"
date: 2026-07-13
tags: [uricase, gout, EcN, koji, oxygen, hydrogen-peroxide, topology, computational, comp-045]
related:
  - computational-experiments.md
  - validation-experiments.md
  - gut-lumen-uricase-physiologic-regime-computational.md
  - gut-lumen-sink.md
sources:
  - "Gao et al. 2025 — PMID 41038159; PMCID PMC12629798"
  - "Zhao et al. 2022 — PMID 35491895; PMCID PMC9067508"
  - "Li et al. 2023 — PMCID PMC10242094"
  - "Miyazaki et al. 2025 — PMID 40033341; PMCID PMC11877951"
---

# Uricase Topology × Oxygen × Peroxide — Computational Design (comp-045)

## Question

How can exact published and proposed UOX configurations be compared across substrate concentration, dissolved-oxygen context, KatG, VHb, and reaction-site catalase without assigning a published joint effect to either component or encoding a topology winner?

## Current state

**Design disposition: `CANDIDATE_LAYOUT_GENERATED`. Biological verdict: `NOT_EVALUATED`.**

COMP-045 contains no biological measurements. It does not advance, eliminate, or rank intracellular, secreted, displayed, or koji-secreted UOX. It generates a blocked experimental template whose exact constructs, controls, stocks, oxygen targets, sampling plan, and assay qualifications must be fixed before wet-lab execution.

## Evidence boundary

Gao/PULSE provides **In Vitro** activity precedents at 250 µM urate for three exact EcN configurations: intracellular smUOX+YgfU, LamB-smUOX, and InaK-N-smUOX. The paper also compared each topology with the same joint KatG+VHb module under its low-oxygen method. It did not test KatG-only or VHb-only UOX configurations.

Zhao provides a **related In Vitro** intracellular PucL-mutant/PucM+YgfU+KatG+VHb precedent, not the exact PULSE smUOX construct. Li provides a related intracellular PucLM+YgfU precedent without KatG or VHb. Neither related configuration is relabeled as exact PULSE evidence.

For LamB and InaK-N UOX, the joint construct is direct whole-configuration evidence, but intracellular KatG is not located at the extracellular UOX reaction site. The reported comparison therefore does not establish extracellular peroxide closure. InaK-N fusion and whole-cell activity were reported, but a dedicated surface-accessibility localization assay was not.

No cited primary source establishes secreted active UOX in *A. oryzae*. Both koji rows are proposed configurations. Native intracellular catalase is host background, not a separate engineered arm and not evidence that peroxide is controlled where secreted UOX reacts.

## Substrate regimes

- **0 µM:** matched no-urate control.
- **0.59 µM:** rounded direct measurement from terminal-ileal fluid in a 34-patient balloon-enteroscopy cohort; not a jejunal or healthy-population baseline and not tested in the cited UOX configurations.
- **50 µM:** sensitivity scenario only.
- **250 µM:** lowest reported PULSE topology-assay concentration.

PULSE used filled, sealed tubes without a reported dissolved-oxygen target. Zhao used approximately 15% of normal dissolved oxygen. A new `microoxic` label is not an exact match to both sources; each wet-lab oxygen target must be predeclared and measured.

## Candidate design

Schema 2 defines:

- 18 unique physical configurations and 20 block assignments;
- 14 preregistered same-block contrasts;
- active UOX plus an otherwise support-module-matched inactive-UOX control at every concentration;
- three biological runs × two measured oxygen contexts × two blocks;
- 12 full 96-well plates with deterministic SHA-256 allocation;
- urate, pathway product, H₂O₂, dissolved oxygen, viability, and localization readouts.

Two LamB comparator configurations repeat across blocks so the KatG/VHb and proposed reaction-site-catalase contrasts each retain a within-block comparator. The mixed three-topology PULSE-KV composition is a proposed cross-plate anchor, not a published in-vitro positive control.

> **Research conjecture — What drives the joint-module benefit outside the cell?**{ .research-conjecture-label }
>
> **Grounded premises:** PULSE compared exact LamB and InaK-N UOX configurations with and without joint KatG+VHb under its low-oxygen method (**In Vitro**; source: Gao 2025, PMID 41038159). KatG remained intracellular while UOX activity was associated with supernatant or whole cells; extracellular reaction-site peroxide closure was not measured.
>
> **Novel leap:** The observed joint-module difference may reflect VHb-mediated oxygen/cell-fitness support, intracellular ROS handling, or both rather than extracellular peroxide closure. No direct evidence separates those explanations.
>
> **Why it matters:** The answer determines whether to invest in intracellular support, reaction-site catalase, or both.
>
> **Discriminating observation:** Compare no module, KatG only, VHb only, joint KatG+VHb, and reaction-site catalase with matched product, dissolved oxygen, H₂O₂, viability, localization, and epithelial-exposure readouts.

## Wet-lab readiness

`BLOCKED_PENDING_EXACT_CONTROL_AND_SAMPLING_QUALIFICATION`

Before execution, bind and review:

- exact active/inactive UOX identities, retained activity, and matched expression/localization criteria;
- exact KatG, VHb, and reaction-site-catalase constructs, retained function, localization, and co-expression compatibility;
- chassis and mixed-anchor stocks plus cell normalization;
- dissolved-oxygen targets;
- sampling times, volume, aliquoting, and destructive-assay compatibility;
- sensitivity and quantification limits at 0.59 µM.

The template must be regenerated under a new exact lifecycle if the qualified subset, contrasts, concentrations, blocks, or controls change.

## What would advance or redirect the track

A topology can advance only from measured within-host, exact-configuration contrasts with qualified controls. Cross-host observations remain configuration-specific. A negative result applies to the tested construct × concentration × oxygen × control regime; it does not kill gut-lumen UOX, another topology, another chassis, or the project.

## Cross-references

- [Reproducible artifact and plate maps](./etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/)
- [Physiological-regime audit](./gut-lumen-uricase-physiologic-regime-computational.md)
- [Validation experiment §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial)
- [Gut-lumen sink](./gut-lumen-sink.md)
