---
type: contradiction
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 1
global_index: 8
pass3_verdict: Partial
overlap_tag: RESTATEMENT
---

# The chaperone-orthogonal-stacking framework's α-coefficient calibration set (§3.5.4) requires harmonized experimental conditions between §1.9 and §1.25 that the current protocol designs do not guarantee.

1. **The chaperone-orthogonal-stacking framework's α-coefficient calibration set (§3.5.4) requires harmonized experimental conditions between §1.9 and §1.25 that the current protocol designs do not guarantee.** Location: `chaperone-orthogonal-stacking.md` §3.5.4, `validation-experiments.md` §1.9 + §1.25. Analysis: §3.5.4 pre-registers that the §1.9 + §1.25 pairing functions as a calibration set ONLY if the experiments are run under harmonized conditions — same host (NSlD-ΔP10), same format (solid-state shio-koji), same promoter, same titer units (mg/L ELISA). §1.9 mandates NSlD-ΔP10 and solid-state. §1.25 currently uses RIB40 as default with NSlD-ΔP10 listed as "optional arm." Without the NSlD-ΔP10 arm, the two experiments produce confounded data that cannot recalibrate α. The 2026-05-15 sweep priority-action-1 flagged this as a harmonization need, but the operational gap persists in the current validation-experiments protocol designs (both committed 2026-05-16). If §1.25 runs RIB40-only while §1.9 runs NSlD-ΔP10, the framework's calibration-set data is lost — the two most expensive wet-lab experiments in the OE queue ($3–5K + $2.5–4K) produce data that cannot answer the framework's central predictive question. This is a protocol-design gap with a clear fix (promote the optional NSlD-ΔP10 arm to mandatory in §1.25's calibration-set role), not a scientific contradiction.

   

---

> **Pass 3 review — Partial.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The calibration-set concern is real and already explicit in `chaperone-orthogonal-stacking.md` §3.5.4, including the requirement for harmonized host, format, promoter, and ELISA titer units between §1.9 and §1.25. But the synthesis overclaims the state of `validation-experiments.md`: direct grep of that file for `1.25`, `DAF`, `SCR1`, `RIB40`, and `NSlD` returned no matches, so the file does not currently contain the asserted §1.25 protocol with RIB40 default and NSlD-ΔP10 optional arm. The right finding is “the chaperone framework defines a harmonization requirement, but the validation protocol is missing or not in the claimed file,” not “the current validation protocol design already has a RIB40-vs-NSlD gap.”
