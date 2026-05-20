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
