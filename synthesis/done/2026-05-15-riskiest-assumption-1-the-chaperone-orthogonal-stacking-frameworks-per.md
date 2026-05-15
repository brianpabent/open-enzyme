---
type: riskiest-assumption
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 12
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The chaperone-orthogonal-stacking framework’s per-architecture PDI-residence-time coefficients (α = 0.

The chaperone-orthogonal-stacking framework’s per-architecture PDI-residence-time coefficients (α = 0.3–0.6 for CCP/SCR, α = 1.5–2.5 for transferrin-lobe) are derived from in vitro folding kinetics in non-koji systems (Notari 2023 lactoferrin oxidative refolding from denatured state; Schmidt 2010 CCP module NMR dynamics) and applied to predict PDI saturation in *A. oryzae* solid-state fermentation. The framework’s own §8 item 6 acknowledges that in vivo ER-assisted co-translational folding may be substantially faster, potentially collapsing the α range toward 1.0 for all fold classes. If the coefficients are systematically conservative, the triple-cassette prediction (currently 0.35–0.65, central 0.45–0.55) may be a false negative — the actual synergy could be above the 0.6 decision gate, meaning DAF SCR1-4 could co-express with uricase + lactoferrin in a single strain after all. The §1.9 + §1.25 calibration set is designed to test this, but it has not yet run. The framework’s predictions currently drive the separate-strain routing decision for DAF SCR1-4 (a major platform architecture choice) and are cited as load-bearing in `koji-endgame-strain.md` §3.3 and `validation-experiments.md` §1.25. The belief that these coefficients transfer from non-koji in vitro data to in vivo *A. oryzae* is the single least-supported load-bearing claim in the current platform thesis. (Anchored to: `chaperone-orthogonal-stacking.md` §3.5, §5.5, §8 item 6; `lactoferrin.md` §7.3; `daf-cd55-scr14-truncated-computational.md` §1.5.)

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is a strong synthesis of the highest-risk load-bearing assumption in the current chassis logic. `chaperone-orthogonal-stacking.md` §3.5.2–§3.5.4 and §8 explicitly state that CCP/SCR α = 0.3–0.6 and transferrin-lobe α = 1.5–2.5 are extrapolated from non-koji in vitro/structural evidence, and §5.5 uses those coefficients to route DAF SCR1-4 away from the triple-cassette endgame strain with a predicted 0.35–0.65 synergy range. Because that routing decision changes platform architecture, the assumption deserves priority treatment until §1.9 + §1.25 calibration data exist.

---

## ✓ Already actioned 2026-05-15 (closure note — extensively scaffolded across existing surfaces; no H-card)

Pass 3's "Confirmed, prioritize" verdict is honored by existing scaffolding rather than by committing a new H10 falsification card. Reasons documented in the briefing for this item:

1. **The α-coefficient uncertainty is already extensively documented and propagated:**
   - `chaperone-orthogonal-stacking.md` §3.5.2 line 178 (Critical caveat) + §3.5.4 (calibration-set candidate) + line 344 (Lf α uncertainty) + §5.5.4 (architecture-adjusted range with α-uncertainty acknowledgment) + §8 item 6 (full extrapolation caveat including in-vitro-vs-in-vivo + Item 32's two-fold-class generalization caveat appended 2026-05-15)
   - `koji-endgame-strain.md` §3 — Item 27 added the in-vitro-α uncertainty propagation paragraph to the Third-cassette-slot design rule callout (2026-05-15)
   - `wiki/open-questions.md` — Item 32 added the chaperone-framework α-coefficient generalization open question with explicit "Fires when" trigger (2026-05-15)
   - `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` Assumption 1 lines 76 + 80 — already carries the in-vivo-α caveat + §8 item 7 cross-link

2. **The calibration resolver is already designed and queued.** §1.9 (lactoferrin transferrin-lobe arm) + §1.25 (DAF SCR1-4 CCP/SCR arm) under harmonized NSlD-ΔP10 / solid-state / matching-promoter conditions produce the empirical α data that resolves the uncertainty.

3. **comp-030 (completed 2026-05-15, in-silico) provided partial empirical corroboration of α = 0.3–0.6 for CCP/SCR.** ESM2 pseudo-pLDDT across 720 candidates: mean 88.8, std 0.5, 100% > 80 — consistent with the predicted "low PDI load" architecture. Not a kinetic measurement, but a structural-quality cross-check that the framework's prior is at least directionally plausible.

4. **Asymmetric failure modes argue against H-card treatment.** H08 (mechanism) + H09 (production) failure modes both reshape the platform. The α-coefficient question failure modes are asymmetric: if α turns out LOWER than predicted, DAF SCR1-4 can co-express in the single-strain endgame (upside vs. current default routing); if HIGHER than predicted, current default routing (separate strain or LBP peer chassis) already absorbs the outcome. There's no "platform reshapes" downside the way H08/H09 carry. The "load-bearing for a routing decision" framing is real but bounded.

5. **Preserving H08 + H09 as the two distinctive index.md riskiest-assumption anchors** keeps the platform-level "two load-bearing scientific bets" framing clear. A third H-card with asymmetric (and substantially less existential) failure modes would dilute that framing without adding new structural rigor — the calibration set + scaffolding already does the rigor work.

**Conclusion:** Pass 3's "prioritize" verdict is satisfied by the extensive existing scaffolding (Items 24 + 27 + 32 + 19's cross-references + the §1.9 / §1.25 calibration set + comp-030's partial corroboration). No new H-card. The assumption is well-named, well-propagated, and has a designed resolver in the queue. Closing.

This is the **last item of the 2026-05-15 sweep AND the last item of the 35-item walk.**
