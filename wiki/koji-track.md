---
title: Engineered Koji Track
date: 2026-07-16
tags: [koji, Aspergillus oryzae, uricase, gout, research track]
related: [engineered-koji-protocol, koji-endgame-strain, aspergillus-oryzae, gut-lumen-sink]
status: active-phase-0
---

# Engineered Koji Track

## 1. Gout weakness

Gout exposes several potentially engineerable weaknesses: intestinal urate can be targeted before reabsorption, and inflammatory amplification can be attacked at multiple points. The system-level rationale is documented in [gut-lumen sink](./gut-lumen-sink.md), [NLRP3 exploit map](./nlrp3-exploit-map.md), and [gout kill-chain delivery routes](./gout-kill-chain-delivery-routes.md).

## 2. Exploit hypothesis

**Mechanistic extrapolation:** an *A. oryzae* production system may provide active gout-relevant payloads in a useful oral or food-derived format if expression, physiological operating conditions, product stability, dose consistency, and safety gates are met.

This hypothesis does not require one strain, one format, home production, or a particular payload stack.

## 3. Proposed engineering

The track evaluates *A. oryzae* as a production chassis for uricase and selected immunomodulatory payloads. Construct architectures, candidate formats, and multi-cassette options are detailed in [engineered-koji-protocol.md](./engineered-koji-protocol.md) and [koji-endgame-strain.md](./koji-endgame-strain.md). Those designs are candidates within this track, not project requirements.

## 4. Evidence by level

- **Clinical Trial:** Oral urate-degradation evidence informs the broader gut-sink premise; it does not validate engineered koji. See [gut-lumen sink](./gut-lumen-sink.md).
- **Animal Model:** Relevant urate and inflammation findings are catalogued in the linked mechanism pages; no animal result establishes the complete engineered-koji product.
- **In Vitro:** Chassis engineering, enzyme expression, protease stability, and assay evidence are maintained in [engineered-koji-protocol.md](./engineered-koji-protocol.md), [uricase](./uricase.md), and the validation protocols.
- **Computational:** Current computational priors are indexed in [computational-experiments.md](./computational-experiments.md) and require current COMP receipts before they can support synthesis.
- **Mechanistic Extrapolation:** Combining payload, chassis, format, and gout endpoint remains an extrapolation until the linked gates are executed.

## 5. Key assumptions

- A selected payload can be produced with the required activity and localization.
- Activity survives the intended manufacturing, storage, and delivery format.
- The payload operates under physiologically relevant substrate, oxygen, pH, residence-time, and protease conditions.
- The achieved exposure is sufficient to change a gout-relevant endpoint.
- Coproducts, organism state, contamination controls, and repeat exposure are acceptable for the intended use.

## 6. Failure modes and safety constraints

Payload misfolding, proteolysis, secretion failure, cassette interference, genetic instability, batch variation, contamination, GI inactivation, peroxide burden, allergenicity, and regulatory mismatch can each stop or redirect a specific configuration. The current threat model is in [cross-validation.md](./cross-validation.md).

## 7. Cheapest discriminating experiment

Start with the smallest payload–chassis assay that measures identity, active yield, and stability under the intended format. Do not build the full stack before single-payload and physiological operating-regime gates pass. Current protocols and ordering are maintained in [validation-experiments.md](./validation-experiments.md).

## 8. Pass / revise / kill criteria

- **Pass:** a configuration meets its predefined identity, activity, operating-regime, and safety gates; advance that configuration.
- **Revise:** the gout weakness remains exploitable but the payload, topology, strain architecture, format, or manufacturing model must change.
- **Kill:** no tested configuration can reach the required operating regime without unacceptable burden or safety risk, or a shared upstream experiment invalidates the targeted mechanism.

## 9. Status and next move

Active Phase 0 track. Resolve the current single-payload, physiological-regime, and safety gates before treating a multi-payload configuration as a product plan.

## 10. What remains true if this track fails

The gout exploit map, gut-sink evidence, payload data, assay methods, and non-koji tracks remain. A failed koji configuration can still identify a useful payload, operating constraint, delivery requirement, or better chassis.
