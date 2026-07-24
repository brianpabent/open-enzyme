# COMP-038 — Butyrate Measurement Audit

**Current verdict:** **YELLOW**

No ready-to-adopt Tier 1 or Tier 2 butyrate assay has been established for
Open Enzyme. Two useful methods remain, but they answer different questions
and require different validation.

| Method | Source matrix | Current status | Next gate |
|---|---|---|---|
| HPLC-UV for SCFAs and lactate | Bacterial culture supernatant | **Tier 3 transfer candidate** | Matrix-matched standards and spike/recovery, then paired HPLC-UV/GC-MS in one exact strain–medium workflow ([§1.31](../../../validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms)) |
| Electrochemical fingerprints + ANN | Human stool | **Tier 2 candidate; not adopted** | Reproduce and lock the complete hardware–chemistry–model stack, then test independent external transfer ([§1.45](../../../validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate)) |

## Evidence boundary

De Baere et al. 2013 (PMID 23542733) is verified at
**primary-abstract scope**, not full-text scope. The abstract supports
bacterial-culture-supernatant use, 210 nm detection, ether back-extraction,
acidification below pH 2, matrix-matched calibration from 0.5–50 mM, and
analyte-spanning LOD/LOQ ranges of 0.13–0.33/0.5–1.0 mM. It does not
explicitly support the shorthand “underivatized.”

Gu et al. 2026 (PMID 42041444; PMCID PMC13114974) is
**full-text verified**. Its within-study independent 30-sample fecal test
cohort was compared with GC-MS. Reported butyrate MAE/RMSE/R² were
0.029 mM/0.034 mM/0.998. This is source-study validation, not independent
external replication. The complete implementation and transfer remain open.

The claim that a July 14 full-text pass verified both candidates is retracted.
That addendum was written on July 15 without a supporting source-read
artifact. The newly dated claim map is
[`primary-source-verification-2026-07-24.json`](./primary-source-verification-2026-07-24.json).

SCFA/ELISA kits remain **RED-provisional** only in the bounded sense that no
qualifying primary method comparison surfaced in the documented May search.
Breath hydrogen/methane is a fermentation proxy, not a butyrate assay, and the
reviewed generic free-fatty-acid kit class is not suitable for butyrate.

Neither published method establishes Open Enzyme matrix qualification,
target-compartment exposure, ABCG2 engagement, gout efficacy, or safety.
