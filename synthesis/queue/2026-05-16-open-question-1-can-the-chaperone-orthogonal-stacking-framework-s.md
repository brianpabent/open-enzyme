---
type: open-question
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 1
global_index: 11
pass3_verdict: Partial
overlap_tag: RESTATEMENT
---

# Can the chaperone-orthogonal stacking framework's α coefficients be calibrated from the two-fold-class calibration set (§1.9 lactoferrin transferrin-lobe + §1.25 DAF SCR1-4 CCP/SCR), or does the §1.25 protocol-design gap (RIB40 default vs NSlD-ΔP10 optional) need to be resolved first?

1. **Can the chaperone-orthogonal stacking framework's α coefficients be calibrated from the two-fold-class calibration set (§1.9 lactoferrin transferrin-lobe + §1.25 DAF SCR1-4 CCP/SCR), or does the §1.25 protocol-design gap (RIB40 default vs NSlD-ΔP10 optional) need to be resolved first?** The framework's predictive power for novel secreted disulfide-rich payloads depends on this calibration. The harmonization gap (Contradiction 1 above) is a protocol-design problem, not a scientific unknown — but until resolved, it blocks the calibration. Route: promote NSlD-ΔP10 from optional to mandatory in §1.25 for the calibration-set role, or accept that RIB40-only execution forfeits the calibration data while still answering §1.25's primary objective (CP0 engineering candidate validation).

   

---

> **Pass 3 review — Partial.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The open question is valid because `chaperone-orthogonal-stacking.md` §3.5.4 already says §1.9 + §1.25 only calibrate α if host/format/promoter/titer units are harmonized, and it names NSlD-ΔP10 as the preferred single-host condition. The problem is again file-state plumbing: `validation-experiments.md` contains no grep-visible §1.25 / DAF / SCR1 protocol, so “RIB40 default vs NSlD optional” is sourced to the chaperone framework’s table, not to an actual validation protocol in that file. The open question should include a first step to create or locate the formal §1.25 protocol before deciding how to deconflict it.
