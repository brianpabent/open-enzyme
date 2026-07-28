---
title: "Luminal UOX Conditional Capacity and Measurement Identifiability"
date: 2026-07-28
tags: [computational, uricase, gut-lumen-sink, mass-balance, identifiability, phase-0]
related:
  - gut-lumen-uricase-physiologic-regime-computational.md
  - hypotheses/H08-gut-lumen-sink-platform-thesis.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "comp-050 — exact rational conditional-capacity and structural-identifiability artifact"
  - "comp-044 — physiological-regime robustness audit"
---

# Luminal UOX Conditional Capacity and Measurement Identifiability

The exploitable weakness is intestinal urate disposal: a luminal UOX system could increase elimination if it consumes urate that would otherwise return to circulation. The current evidence does not establish the relevant human operating regime. COMP-050 instead defines what can be calculated conditionally and what must be measured before a dynamic model can answer that biological question.

**Result: `METHOD_MAP_DERIVED`; biological regime `NOT_EVALUATED`. Evidence level: deterministic computational method, not biological validation.**

## What the capacity boundary means

For a declared window, fixed substrate occupancy, and a calibrated reaction-site active-capacity time course:

```text
Vmax_initial / J_total_mean = q / (occupancy × A_time)
```

`J_total_mean` is mean total local urate influx from systemic and other sources. `q = 1` is the conditional point at which integrated UOX capacity equals total local influx. It is not a closed dynamic mass balance, a dose, a production target, or a serum-urate prediction. Actual removal also depends on changing substrate, initial and terminal inventory, reabsorption, outflow, unattributed loss, oxygen, and retained activity.

The exact response surface spans the declared dimensionless scenarios; its extrema are 101/400 and 1,010 for required initial capacity relative to mean total local influx. Those are grid boundaries, not physiological estimates or planning values.

## Why urate concentration is insufficient

Three constructed constant-volume steady states use the same concentration, `Km`, and total influx. Their UOX-attributed fluxes are 1/10, 1/2, and 9/10 in dimensionless units, while non-UOX loss changes so that `dC/dt = 0` in every case.

The same concentration trajectory can therefore conceal a nine-fold difference in UOX removal within the declared rate law. A terminal urate value—and even an ideal concentration time course without the missing flux observations—cannot identify local UOX activity.

## What each measurement combination can identify

The structural audit uses an exact rational coefficient matrix. A target is identifiable only when its coefficient vector lies in the row space of the governing and observation equations.

| Measurement combination | Local UOX removal | Calibrated active capacity | Declared local ledger | Systemic-origin UOX removal |
|---|---|---|---|---|
| Terminal urate amount only | Not identifiable | Not identifiable | Not identifiable | Not identifiable |
| Initial/terminal urate + qualified product equivalent | Conditionally identifiable | Not identifiable | Not identifiable | Not identifiable |
| Add calibrated reaction-site capacity | Conditionally identifiable | Identifiable | Not identifiable | Not identifiable |
| Add both source influxes, reabsorption, outflow, and source-resolved product fate | Conditionally identifiable | Identifiable | Structurally identifiable | Conditionally identifiable |

“Conditionally identifiable” means only under ideal, noiseless observations. It does not mean that an assay has been validated or that the variables are practically estimable with useful precision.

## Product qualification is load-bearing

Calling a signal “UOX product” is not enough. The product-equivalent observation requires:

- analyte identity and UOX specificity;
- validated stoichiometry and matrix recovery;
- initial product, non-UOX formation, sampling, outflow, degradation, and scavenging fate;
- no-UOX or inactive-UOX, no-urate, and matrix controls;
- prespecified recovery, mass-balance, and interference criteria; and
- source-resolved product fate for systemic-origin attribution.

When COMP-050 removes the qualified total and source-resolved product observations, local UOX removal becomes non-identifiable in every measurement combination. The complete declared ledger also fails because UOX removal cannot be separated from the explicit unattributed-loss term.

## Decision boundary

COMP-050 supplies a measurement contract, not a replacement physiological model. It does not:

- determine whether oral UOX works;
- identify a human substrate, oxygen, residence, or reabsorption regime;
- select a sequence, topology, host, formulation, or dose;
- establish production sufficiency or serum-urate effect;
- validate a product assay or prove practical identifiability; or
- address peroxide, barrier, or clinical safety.

H08 therefore remains open. The next useful evidence is an exact-configuration experiment that measures qualified product formation and calibrated reaction-site capacity under defined substrate and oxygen conditions, followed by source and boundary-fate measurements sufficient to reconstruct every declared ledger term. Practical closure additionally requires the algebraically reconstructed unattributed residual to pass a prespecified mass-balance tolerance. See [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) and the [H08 falsification card](./hypotheses/H08-gut-lumen-sink-platform-thesis.md).

## Reproducible artifact

- [Experiment contract, code, inputs, outputs, and reviews](./etc/experiments/comp-050-luminal-uox-break-even-identifiability/)
- [Structured results](./etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/results.json)
- [Exact response surface](./etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/break-even-surface.csv)
- [Measurement-identifiability matrix](./etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/measurement-identifiability.csv)
