---
title: "KPV Entry Through GSDMD Pores vs. a PepT1 Baseline — Computational Analysis (comp-042)"
tags:
  - computational
  - comp-042
  - kpv
  - gsdmd
  - pyroptosis
  - pept1
  - slc15a1
  - drug-delivery
related:
  - gsdmd-pore-delivery-paradox.md
  - kpv-peptide.md
  - computational-experiments.md
  - validation-experiments.md
sources:
  - "Dalmasso G et al. Gastroenterology 2008;134(1):166-178 (PMID 18061177; DOI 10.1053/j.gastro.2007.10.026)"
  - "Xia S et al. Nature 2021;593:607-611 (PMID 33883744; DOI 10.1038/s41586-021-03478-3)"
  - "Sborgi L et al. EMBO J 2016;35(16):1766-1778 (PMID 27418190; DOI 10.15252/embj.201694696)"
---

# KPV Entry Through GSDMD Pores vs. a PepT1 Baseline

## Decision

**YELLOW — A2 unresolved.**

COMP-042 supports rapid passive KPV entry within its declared pore model, but it does not establish intracellular pharmacology or physiological selectivity.

- **A1, exposure-proxy diagnostic:** intra-articular GREEN, subcutaneous YELLOW, oral RED under the declared route-concentration design spaces. The comparator is the lowest extracellular KPV concentration reported effective in a PepT1-positive cell assay, not an intracellular IC50, target-engagement threshold, or efficacy bar.
- **A2, pore-versus-healthy heuristic:** unresolved. Favorable ≥3× corners occur in the full sensitivity grid, including some intra-articular moderate- and high-PepT1 cases. The healthy-cell equation and PepT1 scenarios are unvalidated, and concurrent PepT1 transport in the pyroptotic cell is not modeled.
- **Platform scope:** this KPV result does not resolve the broader hypothesis that a transporter-orphan, membrane-impermeant payload could exploit GSDMD pores.

## Model

The passive pore contribution uses a short cylindrical pore with two-sided access resistance:

```text
p_pore = H · D · π · r² / (L + π·r/2)
τ_eq   = V_cell / (N_pores · p_pore)
C_pore = C_ext · (1 − exp(−t/τ_eq))
```

`C_pore` is capped at the extracellular boundary concentration. It is the modeled passive pore contribution, not total KPV in a pyroptotic cell.

The A2 response surface compares that contribution with a heuristic healthy-cell PepT1 baseline:

```text
C_healthy = AR_lin · Km · C_ext/(Km + C_ext)
S_model   = C_pore/C_healthy
```

`AR_lin` has four unweighted scenarios: absent, low, moderate, and high. The equation omits measured synovial-macrophage Vmax, efflux, turnover, degradation, membrane potential, and proton coupling. `S_model` is therefore an equation-response diagnostic, not physiological selectivity or a probability.

## A1 result: passive pore contribution vs. extracellular assay proxy

| Route | Central extracellular design input | Central ratio to 10 nM proxy | Unweighted design-space fraction ≥ proxy | A1 state |
|---|---:|---:|---:|---|
| Intra-articular | 292 µM | 29,200× | 1.000 | GREEN |
| Subcutaneous | 0.030 µM | 3.0× | 0.679 | YELLOW |
| Oral | 0.001 µM | 0.1× | 0.036 | RED |

These route concentrations are not established synovial exposures. The intra-articular range is arithmetic from unsourced dose and compartment-volume assumptions; the subcutaneous and oral ranges are named pharmacokinetic design spaces.

At the central pore parameters, `τ_eq` is 2.17 seconds and the modeled passive contribution reaches essentially the extracellular boundary during the 300-second lifetime. Across the unweighted A1 sampling space, the equilibration fraction has a median of 1.000 and a fifth percentile of 0.975.

The deterministic lifetime × pore-count grid includes a one-pore stress case outside the main 10–10,000-pore design range. At 10 pores and 60 seconds, the modeled equilibration fraction is 0.749, so “complete equilibration at every modeled ≥10-pore condition” is not supported. Pore lifetime is low-sensitivity in much of the declared space, not universally irrelevant.

All results in this section are **Mechanistic Extrapolation (computational)**. Dalmasso et al. provide the **In Vitro** extracellular assay observation used as the engineering proxy; they do not provide the modeled intracellular threshold.

## A2 result: full route concentration × Km sensitivity

Each route crosses three extracellular-concentration bounds, three Km bounds, and four PepT1 scenarios: 36 cases per route, 108 total.

| Route | PepT1 absent | PepT1 low | PepT1 moderate | PepT1 high |
|---|---:|---:|---:|---:|
| Intra-articular | 9/9 ≥3× | 9/9 ≥3× | 2/9 ≥3× | 1/9 ≥3× |
| Subcutaneous | 9/9 ≥3× | 9/9 ≥3× | 0/9 ≥3× | 0/9 ≥3× |
| Oral | 9/9 ≥3× | 9/9 ≥3× | 0/9 ≥3× | 0/9 ≥3× |

The full grid contradicts the old central-only claim that favorable selectivity occurs only when PepT1 is absent or low. It does not establish the opposite claim. The crossings show what the heuristic equation permits; no scenario is known to represent synovial macrophages, and no route qualifies without a matched empirical baseline.

When the modeled healthy-cell PepT1 baseline is zero, strict JSON stores `selectivity_ratio: null` with `selectivity_ratio_state: positive_infinity_zero_healthy_baseline`. That value means mathematical positive infinity, not missing data. A future 0/0 case has the distinct state `undefined_zero_over_zero`.

## Interpretation boundaries

1. **PepT1 remains the empirical gate.** Dalmasso et al. demonstrated PepT1-mediated KPV uptake in epithelial and Jurkat models (**In Vitro**). Functional PepT1 and KPV accumulation in synovial macrophages remain unmeasured.
2. **The A2 numerator is pore-only.** Concurrent PepT1 transport in the pyroptotic cell is excluded, so the model does not estimate total-cell pyroptotic-versus-intact selectivity.
3. **Pharmacodynamic timing is unresolved.** KPV is framed as acting upstream of GSDMD pore formation. That ordering makes therapeutic-timing sufficiency uncertain, but the transport model does not establish that all relevant activity is over or that KPV arriving through a pore cannot matter.
4. **Intracellular stability is unresolved.** Extracellular or serum stability cannot be transferred to intracellular retention without evidence.
5. **A KPV-specific result is not a platform verdict.** A transporter-orphan, membrane-impermeant, downstream-acting payload remains a cleaner probe of pore-specific delivery.

## Discriminating experiment

[Validation §1.32](./validation-experiments.md) tests an empirically confirmed transporter-orphan, membrane-impermeant tracer in matched pore-on/off conditions. KPV is a comparator in a pore-on/off × PepT1-on/off design, not an efficacy endpoint. Any conclusion is bounded to the exact tracer, concentration, cell model, and time window tested.

## Evidence and reproduction

- **In Vitro:** Dalmasso et al. reported PepT1-mediated KPV uptake and nanomolar extracellular activity in PepT1-positive cell assays.
- **In Vitro / structural:** Sborgi et al. and Xia et al. provide the GSDMD pore-geometry anchors.
- **Mechanistic Extrapolation (computational):** permeability, equilibration, route proxy ratios, and the A2 response surface.
- **Named gaps:** synovial-macrophage PepT1 function, route-specific synovial KPV exposure, per-cell pore count, intracellular KPV degradation, and matched total-cell accumulation.

The exact code, inputs, generated outputs, and independent lifecycle receipts are in [`etc/experiments/comp-042-kpv-gsdmd-pore-influx/`](./etc/experiments/comp-042-kpv-gsdmd-pore-influx/).
