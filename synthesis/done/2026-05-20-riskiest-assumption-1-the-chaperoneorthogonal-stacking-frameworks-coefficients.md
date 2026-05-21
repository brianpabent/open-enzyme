---
type: riskiest-assumption
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 1
global_index: 14
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# The chaperone‑orthogonal stacking framework’s α‑coefficients — the transferrin‑lobe coefficient (α = 1.

The chaperone‑orthogonal stacking framework’s α‑coefficients — the transferrin‑lobe coefficient (α = 1.5–2.5) for lactoferrin and the CCP/SCR coefficient (α = 0.3–0.6) for DAF SCR1‑4 — are the single load‑bearing belief in the current platform‑architecture design space that is least supported by the corpus. Every multi‑cassette decision (DAF separate‑strain routing, triple‑cassette feasibility, the endgame strain’s single‑organism thesis) rests on these coefficients, but they were **derived from non‑koji in vitro folding kinetics** (Notari 2023 for lactoferrin, Schmidt 2010 crystallography for CCP domains) and have never been measured in *A. oryzae* solid‑state fermentation. The framework’s own §8 item 6 explicitly names this as the calibration‑uncertainty limitation: “the architecture‑adjusted synergy coefficients are more differentiated than the bulk‑count model but carry the same calibration uncertainty.” The §1.9 + §1.25 paired calibration set — now explicitly mandated under harmonised NSlD‑ΔP10 / solid‑state / matching‑promoter conditions — is designed to resolve this, but until that data lands, the platform is committing architecture decisions on coefficients that could be wrong by 2–3×. The worst‑case outcome (transferrin‑lobe α = 2.5, DAF α = 0.3) collapses triple‑cassette synergy to 0.35, forcing a two‑strain fallback; the best‑case (α = 1.0 for both, in‑vivo ER‑assisted folding) would validate the single‑strain endgame thesis. The gap between those two outcomes is the platform’s architecture risk.  

Citable pages: `chaperone-orthogonal-stacking.md` §3.5.2 (coefficient derivation), §3.5.4 (calibration set design), §8 item 6 (framework’s own calibration‑uncertainty caveat); `koji-endgame-strain.md` §3.3 (capacity‑vs‑titer benchmark ambiguity).

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The riskiest-assumption call is correct and should be elevated: `chaperone-orthogonal-stacking.md` §3.5.2 explicitly gives the transferrin-lobe α = 1.5–2.5 and CCP/SCR α = 0.3–0.6 ranges, and the `validation-experiments.md` queue now makes the §1.9 + §1.25 paired calibration set the co-#1 platform gate. Those coefficients drive DAF routing, triple-cassette feasibility, and the single-strain endgame thesis, while the page itself flags their non-koji calibration uncertainty. This is a genuine architecture-risk item, not a bookkeeping concern.

---

## ✓ Actioned 2026-05-21 (known-restatement closure, no new work)

**This is the same α-coefficient riskiest-assumption that has appeared in multiple recent sweeps.** Already self-disclosed at [`chaperone-orthogonal-stacking.md`](../../wiki/chaperone-orthogonal-stacking.md) §8 item 6 ("the architecture-adjusted synergy coefficients are more differentiated than the bulk-count model but carry the same calibration uncertainty"); resolution gate already specified at [`validation-experiments.md`](../../wiki/validation-experiments.md) §1.9 + §1.25 paired calibration set under harmonised NSlD-ΔP10 / solid-state / matching-promoter conditions; the gate is the co-#1 platform-blocker.

The platform is wet-lab-blocked on resolving the coefficients, not awareness-blocked. Re-surfacing this in every sweep is wasted attention. No new evidence in this sweep changes the calibration; closing as a known-restatement per the new [[feedback-no-riskiest-assumption-regurgitation]] discipline.

**Structural follow-up:** the Pass 2 sweep prompt at `scripts/sweep-prompt-2-synthesize.md` will be updated post-walk (before push) to skip restatements of riskiest-assumption items already in `synthesis/done/` history, OR tag them `[KNOWN-RESTATEMENT]` for fast-close. Stops the regurgitation upstream.
