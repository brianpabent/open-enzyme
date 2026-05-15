---
type: priority-action
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 9
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Harmonize the §1.25 DAF SCR1-4 protocol with §1.9 for the chaperone-framework calibration.

1. **Harmonize the §1.25 DAF SCR1-4 protocol with §1.9 for the chaperone-framework calibration.** Update `validation-experiments.md` §1.25 to mandate NSlD-ΔP10 host, solid-state shio-koji format, and PamyB promoter when the experiment is intended to serve as the calibration-set data point. Without this harmonization, the paired titer comparison cannot recalibrate the α coefficients, and the framework’s triple-cassette prediction remains at its current wide uncertainty range. (Rationale: Connection 3; cross-ref `chaperone-orthogonal-stacking.md` §3.5.4.)

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` This priority action has already been implemented. `validation-experiments.md` §1.25 explicitly says that for calibration, the optional NSlD-ΔP10 arm must run under the same solid-state format and matching promoter as §1.9, and that RIB40-only execution is acceptable for primary CP0 candidate validation but does not produce calibration data. `chaperone-orthogonal-stacking.md` §3.5.4 already states the same conditional harmonization rule and names host, format, promoter, and titer units as required variables. There is no remaining “update §1.25” action of the form described here.
