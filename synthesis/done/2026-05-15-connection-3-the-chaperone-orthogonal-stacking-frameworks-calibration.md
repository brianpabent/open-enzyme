---
type: connection
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 3
global_index: 3
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# The chaperone-orthogonal-stacking framework’s calibration set (lactoferrin transferrin-lobe vs DAF SCR1-4 CCP/SCR) requires explicit harmonization of §1.9 and §1.25 experimental conditions — the current designs are mismatched on host strain, format, and promoter, which would confound the calibration.

3. **The chaperone-orthogonal-stacking framework’s calibration set (lactoferrin transferrin-lobe vs DAF SCR1-4 CCP/SCR) requires explicit harmonization of §1.9 and §1.25 experimental conditions — the current designs are mismatched on host strain, format, and promoter, which would confound the calibration.** *Supported*. `[CHAIN-DEPTH: 1]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `chaperone-orthogonal-stacking.md`, `validation-experiments.md`, `koji-endgame-strain.md`, `daf-cd55-scr14-truncated-computational.md`
   - *Page-pair linkage:* `chaperone-orthogonal-stacking.md` §3.5.4 defines the calibration set and lists required harmonization conditions. `validation-experiments.md` §1.25 notes the calibration role but uses RIB40 as default host and does not mandate NSlD-ΔP10 or solid-state shio-koji format. The pages are cross-referenced but the harmonization gap is not surfaced as a contradiction.
   - *Why It Matters:* The framework’s α coefficients (CCP/SCR = 0.3–0.6, transferrin-lobe = 1.5–2.5) are the load-bearing numbers for the triple-cassette prediction that routed DAF SCR1-4 to a separate strain. If the calibration experiment runs under mismatched conditions (RIB40 vs NSlD-ΔP10, submerged vs solid-state, PTEF1 vs PamyB), the measured titer ratio cannot be attributed to fold architecture — it is confounded by host/format/promoter effects. The framework would remain uncalibrated, and the triple-cassette prediction would stay at its current wide uncertainty range (0.35–0.65). This is a fixable design gap, not a scientific unknown.
   - *Suggested Action:* Update `validation-experiments.md` §1.25 to require the optional NSlD-ΔP10 arm, solid-state shio-koji format, and PamyB promoter when the experiment is intended to serve as the calibration-set data point. Add a note that RIB40-only execution is acceptable for the primary CP0 engineering candidate validation but does not produce calibration data. Mirror the requirement in §1.9’s “Secondary role — chaperone-framework calibration set” note.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` The harmonization gap is already explicitly surfaced in both cited pages. `chaperone-orthogonal-stacking.md` §3.5.4 states that §1.9 + §1.25 only function as a calibration set if host, format, promoter, and titer units are harmonized, and its table names the mismatch: §1.9 uses NSlD-ΔP10 and solid-state shio-koji, whereas §1.25 defaults to RIB40 and mixed format. `validation-experiments.md` §1.25 already says that for calibration, the optional NSlD-ΔP10 arm must run under the same solid-state format and matching promoter as §1.9, and that RIB40-only execution is acceptable for the primary CP0 validation but does **not** produce calibration data. The suggested action is therefore not a new fix; it is already in the current protocol text.

---

## ✓ Already actioned 2026-05-15 (closure note — Pass 3 verified)

Pass 3's push-back held under direct grep verification:

- `wiki/validation-experiments.md` §1.25 line 969 contains verbatim: *"For this experiment to function as the calibration-set data point, run the optional NSlD-ΔP10 arm under the same solid-state shio-koji format and matching promoter as §1.9... RIB40-only execution is fine for §1.25's primary objective (CP0 engineering candidate validation) but does NOT produce calibration data."*
- `wiki/validation-experiments.md` §1.9 line 327 mirrors the calibration-set + harmonization framing on the lactoferrin transferrin-lobe side.
- `wiki/chaperone-orthogonal-stacking.md` §3.5.4 defines the calibration set and lists the required harmonization conditions.

All three pages already carry the harmonization requirement that Pass 2 proposed adding. No wiki edits needed; closing.
