---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 3
global_index: 9
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Combined CP0 coverage assay: rosmarinic acid + DAF SCR1-4 in zymosan-activation C5a-generation model.

3. **Combined CP0 coverage assay: rosmarinic acid + DAF SCR1-4 in zymosan-activation C5a-generation model.** *Cost: $1,500–2,500. Time: 3–4 weeks. Decides:* Whether the combined two-layer CP0 strategy (Connection 3) produces additive C5a suppression relative to either intervention alone. Protocol: zymosan-activated human serum ± rosmarinic acid (10–100 μM) ± purified DAF SCR1-4 (1–10 μg/mL), measure C5a by ELISA. Additivity would justify the combined strategy and trigger comp-029 systems modeling. Specified in `complement-c5a-gout.md` §9.7 and `validation-experiments.md` §1.25 extension.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The assay is scientifically reasonable, but the Pass 2 sequencing is wrong: `complement-c5a-gout.md` §9.7 says the rosmarinic-acid + DAF co-treatment experiment is **gated on comp-029 GREEN**, whereas the proposed experiment text says additivity would “trigger comp-029 systems modeling.” It also overstates that the arm is already specified in `validation-experiments.md` §1.25; the explicit co-treatment language lives in `complement-c5a-gout.md` §9.7, not in the §1.25 protocol text I could verify. Keep the experiment, but put comp-029 first.

---

## ✓ Closed by comp-029 YELLOW verdict 2026-05-16

Item 9 spawned comp-029 (combined CP0 systems model). comp-029 returned **YELLOW** at all three DAF MSU-surface accessibility priors (α ∈ {0.05, 0.20, 0.80}). Combined median 1.08–1.10× the better singleton (below the 1.5× GREEN threshold); combined 95% CI overlaps both singleton 95% CIs. Both arms saturate individually, so multiplicative-composition gain is structurally capped near 1.1×.

Per comp-029 decision rule: **YELLOW = park the wet-lab co-administration arm.** The combined-strategy thesis is not refuted; it's just not provably-large-enough under current input uncertainty to justify a co-administration arm on top of the §1.25 DAF SCR1-4 expression screen.

**Re-open condition:** comp-029 identified DAF MSU-surface accessibility α as the load-bearing wet-lab unknown. The existing §1.25 functional readout will resolve α organically — if §1.25 returns α ≥ 0.5, comp-029 re-runs to GREEN and the recommended addition is **a single fourth co-treatment condition** (DAF SCR1-4 + 100 µM rosmarinic acid, same ELISA readout, one additional plate condition). At that point a new sweep item or operator-triggered walkthrough re-opens this experiment.

No wiki edits in this closure. §1.25 protocol unchanged (no co-administration arm added). complement-c5a-gout.md §9.7's gating language ("gated on comp-029 GREEN") remains accurate; Item 25 (comp-029 review) when walked will commit the comp-029 experiment files and update §9.7 + computational-experiments.md table with the YELLOW verdict.

Pass 3's sequencing correction was substantively right — comp-029 ran first, returned YELLOW, and the wet-lab arm correctly stays parked. The mechanical decision rule produced the right closure without operator intervention.
