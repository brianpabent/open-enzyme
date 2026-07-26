# comp-044 summary — gut-lumen uricase physiological regime

**Verdict: LEGACY FLAT-DOSE REGIME NOT ROBUST.** COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement dose, ΔSUA, genotype ordering, physiological regime, efficacy model, topology or chassis selection, production-sufficiency, or safety conclusion.

## Named-scenario capacity ratios

| Scenario | 5 mg | 25 mg | 50 mg |
|---|---:|---:|---:|
| legacy_vmax_24h | 32.3377 | 161.6886 | 323.3773 |
| terminal_ileal_clinical_cohort_no_extra_penalties | 0.0932 | 0.4660 | 0.9320 |
| terminal_ileal_clinical_cohort_microoxic_access_limited | 0.0035 | 0.0175 | 0.0349 |
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

Keep the biological gut-sink hypothesis and its quantitative regime open. Build and characterize exact configurations before the configuration-level physiological screen; complete the separate peroxide-safety gate before animal escalation.

## Limitations

- pH, effective oxygen-dependent activity, access, and survival factors are nonmechanistic scenario variables, not measured patient parameters.
- Oxygen is represented only by a dimensionless scenario multiplier; oxygen stoichiometry, delivery, depletion, and kinetic coupling are not modeled.
- Hydrogen-peroxide production, scavenging, tissue exposure, and safety are not evaluated.
- The legacy 233 mg/day flux denominator is a population prior, not a local compartment concentration.
- Fixed-concentration capacity is an upper-bound screen; substrate depletion and replenishment require a dynamic gut model.
- The grid is a discrete full-factorial over selected levels. Fractions of grid cells are design-space occupancy, not probabilities or uncertainty distributions.
- Only the ratio=1 boundary has a direct mass-balance meaning; the 0.25 and 4 bins are descriptive heuristics.
- The 8.3 U/mg specific activity, Km range, 2-4 hour window, and 233 mg/day denominator are inherited priors, not newly primary-source verified quantitative-planning inputs.
- No renal compensation, reabsorption, microbiome metabolism, topology, or serum-urate mapping is modeled. A dynamic compartmental mass balance is required before dose decisions.
