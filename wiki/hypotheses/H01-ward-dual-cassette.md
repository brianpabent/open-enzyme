---
id: H01
title: "Ward-derived dual-cassette coexistence in solid-state *A. oryzae*"
committed: 2026-04-24
status: Pending
survival_count: 0
tags:
  - hypothesis
  - aspergillus-oryzae
  - dual-cassette
  - uricase
  - lactoferrin
  - feasibility-gate
related:
  - ../koji-endgame-strain.md
  - ../engineered-koji-protocol.md
  - ../lactoferrin.md
  - ../uricase-variant-selection.md
  - ../validation-experiments.md
  - ./README.md
sources:
  - "Ward PP et al. Biotechnology (N Y) 1995;13(5):498-503. PMID 9634791."
  - "Ward PP et al. Biotechnology (N Y) 1992;10(7):784-789. PMID 1368268."
  - "Huynh HH et al. Fungal Biol Biotechnol 2020;7:7. PMID 32514366."
  - "Wakai S et al. Bioresour Technol 2019;276:146-153. PMID 30623869."
  - "Senoo et al. J Biosci Bioeng 2024;137(3). PMID 38242757."
---

# H01 — Ward-Derived Dual-Cassette Coexistence

## Claim

An *A. oryzae* solid-state configuration can co-express active human lactoferrin and an exact UOX configuration that has already passed its single-payload gates, without a material loss of either payload's measured function or an unacceptable change in host viability, peroxide handling, or specified native-metabolite controls.

This is a narrow cassette-coexistence hypothesis. It does not establish a therapeutic dose, oral efficacy, regulatory status, product architecture, or superiority of one UOX sequence, topology, or host.

## Current evidence state

- Ward 1995 supports recombinant human-lactoferrin expression using a glucoamylase–KEX2 architecture in submerged *A. awamori* culture. **In Vitro; adjacent host and process.**
- Ward 1992 supports recombinant human-lactoferrin expression in *A. oryzae*. **In Vitro; single payload.**
- Huynh 2020, Wakai 2019, and Senoo 2024 support heterologous-protein or multi-enzyme expression capabilities in *A. oryzae*. None tests the exact H01 dual-payload configuration in solid-state rice culture. **In Vitro; adjacent configurations.**
- The literature and patent searches refine construct design but are not biological killshots. No H01 survival event has been recorded.

Parent-organism use history does not transfer to an engineered strain or recombinant payload. Construct, process, containment, exposure, and intended use require configuration-specific review.

## Assumptions

1. A Ward-derived lactoferrin cassette remains active in the selected *A. oryzae* host and solid-state process.
2. The independently advanced UOX configuration retains activity in that process.
3. Co-expression does not create a shared secretion, folding, proteolysis, redox, or metabolic bottleneck that materially degrades either arm.
4. The assays distinguish active payload from expression alone and include matched inactive-payload and host controls.
5. The exact advanced UOX configuration—not a preselected *A. flavus* or *C. utilis* sequence—is used. Those source families remain unranked until a matched configuration screen supplies comparable evidence.

## Required sequence

1. **Build and characterize exact single-payload configurations.** Validation §§1.1, 1.2, and 1.5, or an exact external configuration, must establish identity, localization, active UOX, active lactoferrin where relevant, host viability, and assay variance.
2. **Advance the exact UOX configuration through §1.33.** COMP-044 establishes only that the legacy unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. It does not identify the true physiological regime or select a sequence, host, or topology.
3. **Reproduce UOX in the intended solid-state process.** The UOX-only control must retain configuration-level product formation before the dual construct is tested.
4. **Test dual-cassette coexistence.** Compare parental host, inactive controls, lactoferrin-only, UOX-only, and dual configurations from qualified batches.
5. **Clear §1.36 before animals.** A coexistence result cannot bypass the configuration-specific antioxidant-loss/peroxide safety gate.

## Biological killshot

The first H01 killshot is the matched single-versus-dual configuration experiment in [validation §1.9](../validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate).

Measure:

- UOX product formation under the §1.33 reaction conditions;
- active lactoferrin and its prespecified functional assay;
- sequence and cassette state;
- localization and relevant proteolysis;
- extracellular peroxide, host viability, and growth;
- specified native-metabolite controls only where they remain part of the frozen claim.

Before the result-bearing run, use pilot precision and qualified single-payload batches to freeze equivalence, loss, safety, and ambiguity margins. Do not infer clinical sufficiency from an in-vitro pass.

## Decision rules

- **Alive:** the dual configuration meets the prespecified equivalence and safety margins for both active payloads in independent replication.
- **Killed:** both single-payload configurations pass, but the dual configuration crosses a prespecified loss or safety boundary after the allowed architecture iteration.
- **Pending / ambiguous:** material identity, assay precision, or single-payload qualification is insufficient, or the result lies between the frozen margins.

A killed coexistence claim does not kill either payload, another host, or the Open Enzyme mission. It redirects the track to separate configurations or closes the multi-payload architecture if no justified alternative remains.

## Status

**Pending; survival count 0.** Design and literature work are complete enough to define the experiment, but no completed biological coexistence test has crossed an H01 decision threshold.

## Cross-references

- [validation §1.9](../validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate)
- [validation §1.33](../validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial)
- [validation §1.36](../validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay)
- [koji-endgame-strain.md](../koji-endgame-strain.md)
- [uricase-variant-selection.md](../uricase-variant-selection.md)
- [lactoferrin.md](../lactoferrin.md)
