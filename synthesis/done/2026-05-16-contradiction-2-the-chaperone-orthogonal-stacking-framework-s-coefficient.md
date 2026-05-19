---
type: contradiction
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 2
global_index: 8
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The chaperone-orthogonal stacking framework's α-coefficient calibration uncertainty contradicts the platform's reliance on its predictions for architecture decisions.

2. **The chaperone-orthogonal stacking framework's α-coefficient calibration uncertainty contradicts the platform's reliance on its predictions for architecture decisions.** Locations: `chaperone-orthogonal-stacking.md` §8 item 6 ("the architecture-adjusted coefficients remain extrapolations") and §3.5.4 (calibration set design) vs. `koji-endgame-strain.md` §3 (third-cassette slot design rule depending on α coefficients) and `validation-experiments.md` §1.25 (NSlD-ΔP10 arm re-scoped as mandatory based on the framework's calibration role). Analysis: The framework honestly documents that its α coefficients are "bounded estimates pending direct koji-specific calibration" derived from non-koji in vitro folding kinetics. Yet the platform has already routed DAF SCR1-4 to a separate strain based on the framework's triple-cassette synergy prediction (0.35–0.65), re-scoped §1.25 to include a mandatory NSlD-ΔP10 calibration arm, and codified a "cytosolic third cassette" design rule in `koji-endgame-strain.md` §3. These are reasonable decisions given the available information, but they treat the framework's predictions as load-bearing before the calibration data exists. The §1.9 + §1.25 calibration set will resolve this, but until it returns, every architecture decision resting on α coefficients carries an explicit "uncalibrated" caveat that the decision documents themselves don't always surface. The framework's honesty about its limitations and the platform's reliance on its predictions are in tension — not a contradiction in the science, but a contradiction in the confidence-with-which-decisions-are-made vs. the confidence-warranted-by-evidence.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right risk call. `chaperone-orthogonal-stacking.md` §3.5.4 explicitly frames §1.9 lactoferrin + §1.25 DAF SCR1–4 as the two-fold-class calibration set, and §8 item 6 states the α coefficients remain extrapolations from non-koji folding data. Because `validation-experiments.md` elevates §1.9 + §1.25 to the co-#1 architecture gate, every architecture decision using α values should carry an “uncalibrated until §1.9/§1.25 returns” caveat.

---

**WALKED 2026-05-19 — Closed (duplicate of [[2026-05-17-riskiest-assumption-1-the-single-load-bearing-belief-in-the-current-platform]] — D4 in the 2026-05-19 walkthrough).**

Same root concern: uncalibrated α coefficients drive load-bearing architecture decisions (DAF routing, triple-cassette feasibility, single-strain endgame thesis). D4 closed as "already prioritized in §1.9 + §1.25 paired calibration set; gates on wet-lab budget." Full closure context in the canonical entry.
