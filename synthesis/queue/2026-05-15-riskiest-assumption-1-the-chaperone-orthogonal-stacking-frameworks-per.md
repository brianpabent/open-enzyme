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
