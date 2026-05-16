---
type: priority-action
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 1
global_index: 12
pass3_verdict: Partial
overlap_tag: RESTATEMENT
---

# Deconflict the §1.25 protocol's calibration-set role.

1. **Deconflict the §1.25 protocol's calibration-set role.** If the chaperone framework's α-coefficient calibration is a platform priority (per the 2026-05-15 riskiest-assumption verdict), the §1.25 protocol must include the NSlD-ΔP10 arm and match the §1.9 harmonization conditions (same host, same format, same promoter, same titer units). If the calibration is deferred and §1.25 runs RIB40-only for its primary CP0 engineering objective, the framework calibration data is lost from this pair of experiments. The decision is Brian's; the operational implication is clear.

> **Pass 3 review — Partial.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The priority action is directionally right if α-calibration is a platform priority, because `chaperone-orthogonal-stacking.md` §3.5.4 states the comparison is confounded unless §1.25 uses the same host/format/promoter/titer units as §1.9. But the synthesis presents this as editing an existing §1.25 protocol in `validation-experiments.md`, and that file currently has no grep hits for §1.25, DAF, SCR1, RIB40, or NSlD. The actionable version is: add/formalize §1.25 with a mandatory NSlD-ΔP10 calibration arm, or explicitly mark calibration forfeited if the DAF experiment is run under non-harmonized conditions.
