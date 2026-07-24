---
title: "Lactoferrin Shio-Koji Protease Proxy (comp-005)"
date: 2026-05-05
tags: [lactoferrin, protease, shio-koji, computational, alphafold]
related:
  - lactoferrin.md
  - uricase-protease-stability-computational.md
  - computational-experiments.md
  - validation-experiments.md
sources:
  - "UniProt P02788 (human lactoferrin, canonical isoform, SV=6)"
  - "AlphaFold AF-P02788-F1-model_v6 (EMBL-EBI)"
status: retired-invalid-model
---

# Lactoferrin Shio-Koji Protease Proxy (comp-005)

The engineering weakness is loss of intact, functional lactoferrin during the 7–14 day shio-koji ferment. COMP-005 does not determine whether that happens.

## Evidence boundary

The retired artifact mapped inherited sequence-filter matches onto the P02788 sequence and added AlphaFold pLDDT context. Its original HIGH/MODERATE labels are invalid because the model used pLDDT confidence as solvent accessibility. It did not calculate SASA, model the biological assembly or cleavage kinetics, or measure degradation and retained activity.

COMP-005 supplies no cleavage-region priority. In particular, the exact inter-lobe connector is not a lower-confidence AlphaFold segment in the retired input. COMP-001 also cannot serve as a validated uricase comparator. Empirical protease risk remains unresolved.

## Delivery and falsification gate

This question applies specifically to lactoferrin produced for delivery through shio-koji. Expression does not solve exposure: the payload must remain sufficiently intact and retain the relevant activity through the complete process.

The [§1.10 assay](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) is decisive. Measure abundance, fragment pattern, and retained iron-binding activity at day 0, 7, and 14 with matched controls. Map any reproducible fragment without prespecifying the linker as its origin. Only an observed linker-associated failure can activate the separate redesign conjecture. A favorable result advances that exact construct and process; failure redirects the construct, formulation, or delivery format without rejecting lactoferrin as a wider intervention.

Related: [lactoferrin evidence page](./lactoferrin.md) · [COMP registry](./computational-experiments.md#comp-005--lactoferrin-shio-koji-protease-proxy-2026-05-05) · [invalidated, non-runnable COMP-005 tombstone](./etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability/)
