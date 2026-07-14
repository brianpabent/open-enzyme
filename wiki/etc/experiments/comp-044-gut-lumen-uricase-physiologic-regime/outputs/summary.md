# comp-044 summary — gut-lumen uricase physiological regime

**Verdict: LEGACY FLAT-DOSE REGIME NOT ROBUST.** Applying substrate concentration, Km and a finite active window **invalidates the unconditional flat-dose / saturated-capacity classification** for the central jejunal diagnostic before oxygen, access, or survival penalties are added. (The 50 mg central no-extra-penalty ratio is ~0.93 — close to the ratio-one boundary; this shows the unconditional classification is not robust, not that the physiological regime is definitively reversed.) This experiment does **not** predict ΔSUA or establish the true regime.

## Named-scenario capacity ratios

| Scenario | 5 mg | 25 mg | 50 mg |
|---|---:|---:|---:|
| legacy_vmax_24h | 32.3377 | 161.6886 | 323.3773 |
| jejunal_baseline_no_extra_penalties | 0.0932 | 0.4660 | 0.9320 |
| jejunal_baseline_microoxic_access_limited | 0.0035 | 0.0175 | 0.0349 |
| postprandial_sensitivity_microoxic | 0.1011 | 0.5053 | 1.0106 |
| distal_high_substrate_anoxic_sensitivity | 0.0192 | 0.0962 | 0.1925 |

Ratio <1 means enzyme capacity is below the legacy daily-flux denominator under that scenario; ratio ≥1 does not prove full luminal capture because spatial replenishment and reabsorption remain out of model.

## Discrete full-factorial sensitivity grid

The fractions below one describe occupancy of the selected equally weighted design grid; they are not biological probabilities.

| Dose | Scenarios | Fraction <1 | Min ratio | Max ratio |
|---:|---:|---:|---:|---:|
| 5 mg | 1620 | 0.906 | 0.000001 | 32.0 |
| 25 mg | 1620 | 0.777 | 0.000005 | 160.1 |
| 50 mg | 1620 | 0.709 | 0.000010 | 320.2 |

## Decision

Retire comp-019's quantitative ΔSUA and flat-dose claims. Retain the biological gut-sink hypothesis as open. The next decision gate is a physiological topology × oxygen × peroxide experiment, informed by comp-045.

## Limitations

- pH, effective oxygen-dependent activity, access, and survival factors are nonmechanistic scenario variables, not measured patient parameters.
- The legacy 233 mg/day flux denominator is a population prior, not a local compartment concentration.
- Fixed-concentration capacity is an upper-bound screen; substrate depletion and replenishment require a dynamic gut model.
- The grid is a discrete full-factorial over selected levels. Fractions of grid cells are design-space occupancy, not probabilities or uncertainty distributions.
- Only the ratio=1 boundary has a direct mass-balance meaning; the 0.25 and 4 bins are descriptive heuristics.
- No renal compensation, reabsorption, microbiome metabolism, topology, or serum-urate mapping is modeled. A dynamic compartmental mass balance is required before dose decisions.
