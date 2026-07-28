---
title: Cross-Validation — Adversarial Method and Track Threat Models
date: 2026-07-16
tags: [cross-validation, red teaming, falsification, track portfolio, gout]
related: [open-enzyme-vision, validation-experiments, open-questions, koji-track]
---

# Cross-Validation: Adversarial Method and Track Threat Models

## Purpose

Cross-validation is the red-team layer for Open Enzyme. It asks whether a track attacks a real weakness in gout, whether the proposed engineering reaches the relevant compartment at the required operating conditions, and what evidence would make us stop.

It does **not** assign one feasibility score to the project. Open Enzyme is a portfolio of falsifiable tracks, not a single product chain. A local failure updates that track unless the experiment directly tests a shared mission-level assumption.

Mission and failure semantics are defined in [Mission and Operating Principles](./etc/open-enzyme-vision.md).

## Real-claim rule

Before challenging a project claim:

1. link the current page and section where the claim is actually made;
2. quote or paraphrase it at its current strength;
3. identify whether it is evidence, a computational result, a design choice, or an aspiration;
4. test that claim, not a stronger version invented for the critique.

If no current source supports the premise, do not build a threat model around it.

## Threat-model template

Each active track should answer:

| Field | Question |
|---|---|
| Gout weakness | What causal or operational weakness is being exploited? |
| Track claim | What exact, sourced claim is under test? |
| Attack surface | Which biological, engineering, safety, manufacturing, or regulatory assumptions can fail? |
| Evidence boundary | What is directly observed, and what is extrapolated? |
| Cheapest discriminator | What is the smallest test that changes the decision? |
| Pass / revise / kill | What outcomes promote, redirect, or stop the track? |
| Blast radius | What other claims actually depend on this result? |
| Next track | If killed, what becomes the better use of the same insight? |

The reusable authoring form is [track-template.md](./etc/track-template.md).

## Current threat-model index

| Track | Threat model | Shared dependency or local risk |
|---|---|---|
| Gut-lumen urate sink | [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md), [gut-lumen sink](./gut-lumen-sink.md), [comp-050 measurement map](./luminal-uox-break-even-identifiability-computational.md) | Shared by oral luminal urate-degradation approaches; topology, qualified product attribution, source/boundary-fate closure, and operating regime remain decisive |
| Engineered koji | [Koji track](./koji-track.md) | Payload–chassis fit, secretion/activity, format, safety, and production are track-local |
| Community fermentation | [H09](./hypotheses/H09-community-fermentation-reliability.md) | A production/distribution option for the koji track; not mission-load-bearing |
| Engineered live biotherapeutics | [H02](./hypotheses/H02-engineered-lbp-thesis.md), [LBP chassis](./engineered-lbp-chassis.md) | Host engineering, colonization, containment, and regulatory path are track-local |
| URAT1 siRNA | [H03](./hypotheses/H03-sirna-urat1-thesis.md) | Target accessibility, renal delivery, off-targets, and durability are track-local |
| Complement/DAF | [H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) | Payload validity and delivery to the relevant compartment are track-local; complement biology informs other tracks |
| Medicinal mushrooms | [Exact-material conjecture](./medicinal-mushroom-complement-track.md#research-conjecture--a-reproducible-medicinal-fungal-material-may-expose-a-gout-weakness) | Extract identity, standardization, exposure, and assay validity are track-local |
| TCM × modern rigor | [H04](./hypotheses/H04-tcm-rigor-intersection.md) | Formula identity, trial quality, active constituents, and exposure are track-local |

This index is not a ranking. Current priorities belong in the dashboard and may change as evidence changes.

## Koji-track threat model

The current track claim is defined in [koji-track.md](./koji-track.md). Detailed construct, format, and assay reasoning remains in [engineered-koji-protocol.md](./engineered-koji-protocol.md), [koji-endgame-strain.md](./koji-endgame-strain.md), and [validation-experiments.md](./validation-experiments.md).

The adversarial questions are:

- **Payload–chassis fit:** Does the selected payload express, fold, localize, and remain active in *A. oryzae* under the intended production format?
- **Operating regime:** Does activity persist at physiologically relevant substrate, oxygen, residence-time, pH, and protease conditions?
- **Product burden:** Do multi-cassette designs create expression, folding, secretion, or stability tradeoffs that erase the intended benefit?
- **Format:** Does the proposed food, dried powder, capsule, or other preparation preserve the relevant payload and dose consistency?
- **Safety:** Are coproducts, peroxide, allergenicity, viable-organism containment, contamination, off-target activity, and repeat exposure acceptable for the claimed use?
- **Manufacturing:** Can the selected process reproduce identity, activity, and purity? Community fermentation is one option, not a premise.
- **Translation:** Does the intervention reach a meaningful gout endpoint, and is the regulatory path compatible with the actual claim and product—not merely the organism’s historical food use?

Fermentation reproducibility, contamination, dose consistency, GI survival, and strain stability remain legitimate risks. They attach to the relevant koji production and delivery configuration; they are not evidence against unrelated gout exploits.

## Mission-level threats

A result affects the mission only when it attacks a shared method or biological premise. Current mission-level risks include:

- the gout system map omits a dominant causal or compensatory pathway;
- the corpus repeatedly upgrades mechanistic or computational evidence into clinical confidence;
- synthesis creates attractive connections that do not survive raw-source rehydration;
- intervention discovery outruns compartment, exposure, safety, or translation constraints;
- portfolio language turns a currently favored track into an implicit requirement;
- duplicated prose causes a corrected claim to survive elsewhere as stale “independent” support.

The knowledge-system controls—evidence levels, primary-source verification, exact COMP review, bounded propagation, distributed synthesis, and current-state-only authoring—exist to make these failure modes visible.

## Decision rule

Cross-validation should end with one of four decisions:

- **Pass:** the stated evidence gate is met; proceed to the next discriminator.
- **Revise:** the exploit remains plausible, but the payload, chassis, topology, dose, format, population, or assay changes.
- **Kill track:** a stated kill criterion fires; stop spending on that implementation.
- **Escalate shared assumption:** the result may affect multiple tracks; update every dependent surface before drawing a mission-level conclusion.

The output is a decision and its blast radius, not a rhetorical verdict about whether Open Enzyme “works.”
