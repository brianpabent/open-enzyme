# Input provenance — comp-050

## Evidence boundary

COMP-050 is a mathematical conditional-capacity and structural-identifiability map. It introduces no patient, dose, enzyme, chassis, topology, oxygen, reabsorption, residence-time, or serum-effect estimate.

The need for this map comes from the current Open Enzyme decision boundary:

- COMP-044 showed that COMP-019's unconditional flat-dose classification was not robust to the tested substrate-occupancy and finite-window diagnostics. COMP-044 did not identify a replacement physiological regime.
- Validation §1.33 requires an exact built configuration and measures urate, oxidative product, H₂O₂, dissolved oxygen, viability, localization, and active UOX at the reaction site.
- H08 keeps the measured dynamic compartmental model blocked until local urate replenishment, oxygen, calibrated active-UOX capacity, residence, reabsorption, outflow, and source-fate measurements exist.

These are repository decision boundaries, not independent evidence for a quantitative biological parameter.

## Mathematical inputs

The integrated ledger is an amount balance over one declared window:

`U_T - U_0 = I_systemic + I_other - R_UOX - R_reabsorption - R_outflow - R_unattributed`.

Initial and terminal concentration measurements require measured volume and sampling/dilution correction before conversion to amount. The response surface uses mean total local influx, `(I_systemic + I_other)/T`, as its denominator. It does not call that systemic-source capture.

The conditional capacity identity holds `C/Km` fixed and defines the active-capacity time-area fraction from calibrated reaction-site `Vmax_active(t)`. The grid levels are dimensionless engineering scenarios selected to expose the shape of the boundary. They are not fitted distributions, probabilities, clinical targets, or claims about an exact UOX configuration.

The same-concentration examples are constructed algebraic counterexamples under constant volume. They are not biological measurements.

The structural-identifiability audit uses exact rational linear algebra. Direct observations are ideal, noiseless observation equations. Qualified total and source-resolved product observations are included only as declared ideal assumptions; COMP-050 does not establish that an assay satisfies their identity, stoichiometry, recovery, product-fate, background, or interference prerequisites. A separate sensitivity removes those observations and must make local UOX removal non-identifiable, including when an unattributed residual-loss term remains in the ledger.

## Excluded inference

No output may be mapped to milligrams of enzyme, CFU, production yield, a chassis, a topology, serum urate, efficacy, or safety. Structural identifiability under ideal observation assumptions is not practical identifiability, assay validation, or evidence that the biological variables occupy a useful regime. A measured dynamic model remains downstream of exact-configuration data and source/boundary-fate measurements.
