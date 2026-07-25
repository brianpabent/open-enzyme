# comp-042: KPV entry through GSDMD pores vs. a PepT1 baseline

## Question

Does a diffusive pore model support rapid KPV entry into a pyroptotic macrophage (A1), and what does a deliberately heuristic PepT1 comparator reveal about the measurements needed to establish pore-specific selectivity (A2)?

A1 compares the modeled passive pore contribution to intracellular KPV with the lowest extracellular concentration reported effective in a PepT1-positive cell assay. That reference is an engineering exposure proxy, not an intracellular IC50, target-engagement threshold, or efficacy claim.

A2 is not a physiological selectivity estimate. It maps how a heuristic healthy-cell accumulation equation responds to declared extracellular-concentration, Km, and PepT1-scenario inputs. Numerical ≥3× points are model diagnostics, not route qualifications.

## Evidence-state boundary

KPV is a poor proof-of-concept payload independent of any numerical A2 corner:

- PepT1 provides a competing import route, while functional PepT1 and KPV accumulation remain unmeasured in synovial macrophages.
- KPV is framed as an upstream NLRP3/NF-κB inhibitor, while GSDMD pore formation is downstream of inflammasome activation. This ordering makes therapeutic-timing sufficiency uncertain; the transport model does not resolve residual targetable activity, cytokine-release timing, or efficacy.

A transporter-orphan, membrane-impermeant, downstream-acting payload is the cleaner test of the pore-delivery platform. The platform remains open regardless of the KPV-specific result.

## How to reproduce

```bash
cd wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx
python3 analyze.py
```

The design was frozen under CPython 3.14.5 with the standard library only, and the script rejects another Python version. The design-space sampler uses seed 42. Repeated runs on the same CPython/platform environment should be byte-identical; compare output hashes. Cross-platform byte identity is not guaranteed because standard-library floating-point functions can depend on the platform math implementation.

## Files

```text
comp-042-kpv-gsdmd-pore-influx/
  analyze.py
  README.md
  inputs/
    query-strategy.json
    provenance.md
    kpv_properties.json
    pore_geometry.json
    macrophage_geometry.json
    pept1_and_effective_concentration.json
    route_concentrations.json
  outputs/
    central_results.json
    monte_carlo.json
    selectivity_grid.json
    robustness_sweep.json
    verdicts.json
    summary.md
```

`selectivity_grid.json` and `central_results.json` use strict JSON. When PepT1 is absent and the modeled healthy-cell denominator is zero, mathematical positive infinity is encoded as `"selectivity_ratio": null` with `"selectivity_ratio_state": "positive_infinity_zero_healthy_baseline"`. This is not missing data. A future 0/0 case has a separate `undefined_zero_over_zero` state.

## Model

Per-pore permeability includes two-sided access resistance:

```text
p_pore = H · D · π · r_p² / (L_pore + π·r_p/2)
```

Cell equilibration uses a well-mixed compartment:

```text
τ_eq    = V_cell / (N_pores · p_pore)
C_in(t) = C_ext · (1 − exp(−t/τ_eq))
```

The PepT1 comparator is:

```text
C_in,healthy = AR_lin · Km · C_ext/(Km + C_ext)
C_pore       = f_pore · C_ext
S_model      = C_pore/C_in,healthy
```

`C_pore` is the modeled passive pore contribution, not total KPV in a pyroptotic cell. Concurrent PepT1 transport in the pyroptotic cell is not modeled. `AR_lin` is an unweighted design scenario, not a measured expression value or probability. The equation borrows a rate-saturation shape as an accumulation heuristic; without synovial-macrophage Vmax, efflux, turnover, degradation, membrane potential, and proton-coupling measurements, it is not a validated steady state or a proved upper/lower bound.

## Preregistered metrics and decision rules

1. **A1 exposure-proxy diagnostic:** modeled passive pore contribution divided by the extracellular cell-assay effective-concentration proxy.
2. **A2 heuristic ratio:** central case plus the full 3 route-concentration bounds × 3 Km bounds × 4 PepT1 scenarios. The 108 evaluations are unweighted.
3. **Pore robustness:** lifetime × pores-per-cell grid for all three routes, with all other inputs central. The one-pore rows are stress cases outside the main 10–10,000-pore design range.

A1 traffic lights are engineering rules:

- GREEN: central ratio ≥10 and at least 0.9 of unweighted log-uniform design-space draws ≥1.
- YELLOW: central ratio ≥1 and sampled fraction ≥0.5.
- RED: otherwise.

The sampled fraction is not a calibrated probability. A2 remains `UNRESOLVED` regardless of heuristic ≥3× crossings until a matched pyroptotic-versus-intact-cell experiment measures the healthy-cell baseline. A route cannot qualify without both an A1 pass and empirical A2 resolution.

Contrary results can win: the generated outputs must report the computed A1 states and every A2 corner without suppressing threshold crossings. The overall machine verdict is derived from the best computed A1 state and capped below GREEN while A2 remains unresolved.

## Limitations

- Pores per cell, subcutaneous/oral synovial concentrations, and the PepT1 scenarios are named design-space assumptions.
- A quantitative hindrance-factor band is a conservative engineering sensitivity, not a measured KPV/GSDMD value.
- The 10 nM reference is an extracellular cell-assay observation.
- Concurrent PepT1 transport in pyroptotic cells is excluded, so A2 is a pore-route-versus-healthy-baseline diagnostic rather than total-cell selectivity.
- The model does not establish pharmacodynamics, therapeutic timing, tissue sparing, efficacy, or safety.
- Intracellular KPV degradation is uncharacterized.

## Authoring contract

The canonical evidence home is [`kpv-gsdmd-pore-influx-computational.md`](../../../kpv-gsdmd-pore-influx-computational.md). Local decision deltas may update:

- [`computational-experiments.md`](../../../computational-experiments.md)
- [`gsdmd-pore-delivery-paradox.md`](../../../gsdmd-pore-delivery-paradox.md)
- [`kpv-peptide.md`](../../../kpv-peptide.md)
- [`open-questions.md`](../../../open-questions.md)
- [`validation-experiments.md`](../../../validation-experiments.md) §1.32
- [`chassis-pending-interventions.md`](../../../chassis-pending-interventions.md)
- [`index.md`](../../../../index.md)

The computation can resolve transport behavior within its declared model. It cannot establish KPV efficacy, physiological PepT1 selectivity, a preferred production chassis, or failure of the transporter-orphan pore-delivery platform.
