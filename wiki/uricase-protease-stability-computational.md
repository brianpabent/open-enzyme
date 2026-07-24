---
title: "Uricase Protease-Site Proxy for Shio-Koji (comp-001)"
date: 2026-05-05
tags: [uricase, shio-koji, protease, alphafold, computational]
related:
  - computational-experiments.md
  - validation-experiments.md
  - uricase-shio-koji-thermal-stability-computational.md
  - engineered-koji-protocol.md
sources:
  - "UniProt Q00511 — uricase, Aspergillus flavus"
  - "AlphaFold Protein Structure Database — AF-Q00511-F1-model_v6"
  - "comp-001 inputs/provenance.md — exact hashes, transformation, and legacy-filter limitations"
status: phase-0
---

# Uricase Protease-Site Proxy for Shio-Koji (comp-001)

The exploitable weakness is straightforward: a secreted UOX payload is useless if shio-koji proteases destroy its activity before delivery. COMP-001 does not answer whether that happens. It preserves the narrower computational prior that can be established from the available inputs.

**Verdict: proxy only; empirical protease risk is unresolved.**

## What the computation establishes

**Deterministic computational audit:** The fixed Q00511 sequence contains 215 adjacent pairs matching the legacy ALP P1 filter, 97 matching the legacy NPr P1′ filter, and 44 matching the legacy acid-protease P1/P1′ filter. The AlphaFold model reports high confidence across Q00511: mean pLDDT 97.14, minimum 80.50.

Those residue arrays lack claim-level provenance establishing them as exhaustive protease-specificity rules. They are therefore fixed legacy filters, not verified cleavage rules. The complete pair inventory and exact local pLDDT windows are in the [COMP-001 artifact](./etc/experiments/comp-001-uricase-shio-koji-protease-stability/).

## What remains unknown

pLDDT measures prediction confidence. It does not measure solvent exposure, burial, protease access, cleavage probability, time-integrated degradation, retained UOX activity, or performance in a ferment. High pLDDT around a filter match cannot support a LOW-risk or survival conclusion.

The result applies only to the proposed Q00511-in-shio-koji route. It neither validates nor weakens uricase as an intervention, another delivery route, or another research track.

## Delivery decision

The candidate route is UOX produced by engineered *A. oryzae* and delivered in a shio-koji product. COMP-001 supplies no production, secretion, dose, shelf-life, gastric-transit, or target-compartment exposure claim. Chassis work should proceed only alongside direct measurement of the actual expressed product.

## Discriminating experiment

The [§1.10 shio-koji retained-activity assay](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) remains the feasibility gate. Measure UOX abundance and retained urate-oxidation activity at day 0, 7, and 14 in the actual ferment, with matched no-protease and heat-inactivated controls. A favorable result advances this route; activity loss redirects formulation, host, secretion, or delivery design without rejecting the wider uricase hypothesis.

Related: [computational experiment registry](./computational-experiments.md#comp-001--uricase-shio-koji-protease-site-proxy-2026-05-05) · [thermal-stability proxy](./uricase-shio-koji-thermal-stability-computational.md) · [engineered koji protocol](./engineered-koji-protocol.md)
