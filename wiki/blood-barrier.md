---
title: Gut-Blood Barrier and Enzyme Delivery Routes
date: 2026-04-21
tags:
  - delivery
  - gut barrier
  - uricase
aliases:
  - gut barrier
  - intestinal epithelium
  - bioavailability
  - enzyme absorption
  - oral delivery
related:
  - uricase
  - gut-lumen-sink
  - blood-barrier-exploits
  - validation-experiments
sources:
  - blood-barrier-exploits.md
  - gut-lumen-sink.md
  - uricase.md
---

# Gut-Blood Barrier and Enzyme Delivery Routes

The gut epithelium separates two different uricase hypotheses: degrade urate in the lumen without systemic enzyme exposure, or move an active enzyme or encoded payload across the barrier. Evidence for one route does not validate the other.

## Luminal UOX hypothesis

The luminal hypothesis exploits urate already secreted into the intestine. It does not require intact UOX to enter the bloodstream. Human oral-enzyme studies support the general proposition that an active luminal enzyme can alter systemic urate handling, but they do not validate an engineered yeast or koji construct, a delivery format, or a dose. **Clinical Trial evidence for the modality; Mechanistic Extrapolation for an untested engineered construct.** See [gut-lumen sink](./gut-lumen-sink.md) and [uricase](./uricase.md).

An engineered UOX candidate therefore remains conditional on two preclinical gates:

1. Build and characterize exact candidate configurations in their intended host or material, then use [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) to identify whether any produces product at the human-baseline substrate prior without an unacceptable peroxide or viability signal.
2. A surviving topology must pass [validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay), which tests the coupled loss of urate antioxidant capacity and UOX-derived hydrogen peroxide before animal escalation.

Until those gates pass, no fermented preparation, live organism, lysate, powder, or capsule is an established delivery format.

## Barrier-crossing hypotheses

[Blood-barrier exploits](./blood-barrier-exploits.md) catalogs paracellular, transcellular, vesicular, mucosal, and barrier-bypassing routes. These are separate delivery programs because systemic or tissue exposure introduces route-specific pharmacokinetic, immunogenicity, and safety questions. A route should be advanced only when the target requires exposure outside the lumen and the proposed carrier has a direct measurement and falsification plan.

For UOX, systemic and intra-articular routes should be compared with existing systemic uricase evidence rather than inferred from luminal feasibility. Deliberately increasing epithelial permeability also requires direct barrier-integrity and translocation measurements; theoretical bioavailability is not a safety result.

## Immune boundary

Mucosal immune tolerance is a biological phenomenon, not a guarantee for a recombinant enzyme or engineered organism. The immune result depends on the antigen, formulation, exposure pattern, barrier state, host, and whether material reaches systemic compartments. Tolerability observed for one oral-enzyme formulation cannot be transferred to engineered yeast, engineered koji, or another payload. Each candidate needs direct local and systemic immune readouts in its own delivery configuration.

## Decision rule

- Use a luminal route only if activity at physiological substrate, peroxide control, viability, and the §1.36 safety interaction survive testing.
- Pursue barrier crossing only when a gout-relevant target cannot be reached from the lumen and the route has a measurable exposure advantage.
- Kill or redirect the construct when the required compartment cannot be reached with an acceptable safety margin.

This page concerns delivery logic. Chassis selection and cross-track ranking belong in the [modality–chokepoint matrix](./modality-chokepoint-matrix.md).
