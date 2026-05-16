---
type: riskiest-assumption
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 1
global_index: 16
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# The chaperone-orthogonal stacking framework's per-architecture α coefficients (CCP/SCR α = 0.

The chaperone-orthogonal stacking framework's per-architecture α coefficients (CCP/SCR α = 0.3–0.6, transferrin-lobe α = 1.5–2.5) are the single load-bearing belief in the current platform thesis that is least supported by the corpus. These coefficients are derived from non-koji in vitro folding kinetics — Notari 2023 (PMC10465537) for lactoferrin's transferrin-lobe oxidative folding from a fully denatured state, Schmidt 2010 (PMC2806952) for CCP/SCR domain structural rigidity — not from direct PDI residence time measurements in *A. oryzae*. Yet they drive the decision to route DAF SCR1-4 to a separate strain (triple-cassette synergy 0.35–0.65, `chaperone-orthogonal-stacking.md` §5.5), the prediction that single-cassette DAF SCR1-4 will achieve ≥100 mg/L (§3.5.4), the design rule that cytosolic third cassettes bypass chaperone competition (`koji-endgame-strain.md` §3), and the re-scoping of `validation-experiments.md` §1.25 to include a mandatory NSlD-ΔP10 calibration arm. The framework itself honestly documents this uncertainty (`chaperone-orthogonal-stacking.md` §8 item 6: "the architecture-adjusted coefficients remain extrapolations... the transferrin-lobe α could be closer to 1.0 than 2.5 in the functional secretory context"). If the α coefficients are wrong by a factor of 2–3× — if in vivo ER-assisted co-translational folding is substantially faster than in vitro oxidative refolding kinetics imply — the entire architecture strategy shifts: DAF SCR1-4 might be viable as a third cassette in the endgame strain, the separate-strain routing decision would be premature, and the cytosolic-third-cassette design rule would be solving a problem that doesn't exist at the predicted magnitude. The §1.9 + §1.25 calibration set (paired lactoferrin + DAF SCR1-4 expression under harmonized NSlD-ΔP10 / solid-state / matching-promoter conditions) is designed to resolve this, but until it returns, every architecture decision depending on α coefficients rests on uncalibrated extrapolation from non-koji data. The framework's honesty about this uncertainty is a strength; the platform's reliance on its predictions before calibration is the risk.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The riskiest-assumption framing is accurate and already grounded in `chaperone-orthogonal-stacking.md`: DAF SCR1–4 α = 0.3–0.6, lactoferrin transferrin-lobe α = 1.5–2.5, and the triple-cassette prediction is 0.35–0.65 until calibrated. `validation-experiments.md` now makes the §1.9 + §1.25 NSlD-ΔP10/solid-state/matching-promoter pair mandatory for calibration, so this should remain a top architecture-risk call until those data exist.
