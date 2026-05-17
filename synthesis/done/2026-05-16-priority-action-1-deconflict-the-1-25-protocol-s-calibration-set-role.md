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

---

**WALKED 2026-05-16 — Closed (re-scoped §1.25 to mandatory two-arm).**

Yesterday's walk closed the calibration-harmonization rule as "structurally already in the protocol" because §1.25 said "if you run the optional NSlD-ΔP10 arm, match §1.9 conditions." Today's daemon correctly flagged the gap: "if optional" wasn't enough — RIB40-only execution would forfeit the calibration data, and the riskiest-assumption verdict (Confirmed, prioritize) made calibration platform-architecture-gating.

Actioned:
- ✓ `wiki/validation-experiments.md` §1.25 Co-primary role section: NSlD-ΔP10 arm re-scoped from "optional" to "mandatory" with rationale (the framework's α coefficients are the platform-architecture risk per today's riskiest-assumption verdict; RIB40-only forfeits the calibration role).
- ✓ §1.25 Host strain section: replaced "RIB40 first-pass, NSlD-ΔP10 optional" with explicit two-parallel-arms structure (both mandatory).
- ✓ §1.25 cost line: $2,500–4,000 → $3,500–5,500 (two-arm).
- ✓ §1.25 added to queue table (was missing) as co-#1 priority gate with §1.9.
- ✓ Queue-table-header "#1 priority gate" rewritten: gating experiment is now the chaperone-framework α-coefficient calibration set (§1.9 + §1.25 paired), not §1.9 alone.

Brian's call: prioritize the framework calibration over RIB40-only cost savings. Reason: every framework-driven architecture decision (separate-strain DAF routing, triple-cassette feasibility, single-strain endgame) rests on un-validated α coefficients until this calibration set returns data. $1K marginal cost is trivial against the architecture decisions it gates.
