---
type: connection
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 3
global_index: 3
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Dietary rosmarinic acid (C3 convertase inhibitor) + engineered DAF SCR1-4 (surface decay-accelerator) as a combined two-layer CP0 intervention — a testable hypothesis that composes the upstream-complement and engineered-DAF threads into a single strategy.

3. **Dietary rosmarinic acid (C3 convertase inhibitor) + engineered DAF SCR1-4 (surface decay-accelerator) as a combined two-layer CP0 intervention — a testable hypothesis that composes the upstream-complement and engineered-DAF threads into a single strategy.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* [`complement-c5a-gout.md`](./complement-c5a-gout.md), [`upstream-complement-verification-rerun-computational.md`](./upstream-complement-verification-rerun-computational.md), [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md), [`hypotheses/H05-daf-scr14-cp0-thesis.md`](./hypotheses/H05-daf-scr14-cp0-thesis.md), [`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md)
   - *Page-pair linkage:* `complement-c5a-gout.md` §9.7 (newly added 2026-05-15) explicitly names the combined strategy for the first time, but the two threads (dietary rosmarinic acid from comp-018/comp-020, engineered DAF SCR1-4 from comp-012/H05) have advanced in parallel without being composed into a single intervention hypothesis until this sweep. The connection composes three independent findings: (1) comp-020 identified rosmarinic acid as a C3 convertase inhibitor via covalent C3b modification (IC50 ~34 μM with a 44× assay-format spread), operating at the fluid-phase and gut-luminal complement scales; (2) comp-012 confirmed DAF SCR1-4 is shio-koji protease-stable and a viable engineered-koji CP0 candidate, predicted to operate at the MSU crystal surface by accelerating decay of deposited C3 convertases; (3) the chaperone framework's §5.5 triple-cassette prediction routes DAF SCR1-4 to a separate strain or peer-track chassis, meaning the two interventions are delivered via different chassis (dietary rosemary/lemon balm vs. engineered koji) and therefore don't compete for the same fermentation capacity.
   - *Why It Matters:* CP0 is the platform's longest-standing "honest gap" — the only chokepoint with zero fermentable coverage, defaulting to avacopan as a permanent pharma adjunct. The combined rosmarinic acid + DAF SCR1-4 strategy would provide two-layer CP0 coverage (fluid-phase C3 convertase inhibition + surface decay-acceleration) from two independent, food-grade interventions. Neither alone is likely to fully close CP0 (rosmarinic acid's IC50 spread and bioavailability are unresolved; DAF SCR1-4's mucosal delivery geometry is a wet-lab unknown), but together they cover complementary steps of the complement cascade. The strategy is testable: a comp-029 systems model (queued in `computational-experiments.md` Planned Analyses) can bound the combined-effect prediction, and a low-cost rosmarinic-acid co-treatment arm on the existing §1.25 DAF SCR1-4 expression screen can empirically test additivity in a zymosan- or MSU-crystal C5a-generation assay.
   - *Suggested Action:* Prioritize comp-029 (combined CP0 systems model) ahead of other medium-priority computational experiments, since it gates whether the combined strategy is worth wet-lab spend. If comp-029 returns GREEN, add a rosmarinic-acid co-treatment arm to `validation-experiments.md` §1.25 at marginal cost (~$500–1,000). The combined strategy also needs a named home in the wiki — either a new "Combined CP0 Intervention Strategy" section in `complement-c5a-gout.md` or a dedicated hypothesis stub (H10).

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is a valid CP0 composition: `complement-c5a-gout.md` §9.7 explicitly frames rosmarinic acid as upstream C3-convertase inhibition with a 44× IC50 assay-format caveat, and DAF SCR1-4 as engineered surface decay acceleration tied to H05 and comp-012. The important part is the sequencing discipline: comp-029 should bound the combined-effect range before the rosmarinic-acid co-treatment arm is added to the DAF wet-lab screen.

---

## ✓ Actioned 2026-05-16

Substantive content already in place across §9.7 / comp-029 brief / §1.25 wet-lab gate; this Connection's actionable lever was the operator decision on whether to spawn comp-029. Operator said spawn.

**comp-029 spawned as background Opus subagent** following the `new-comp-experiment` skill discipline. Brief: two orthogonal models (rosmarinic acid C3-convertase inhibition with 44× IC50 uncertainty distribution + DAF SCR1-4 decay-accelerator kinetics across explicit surface-accessibility priors) cross-multiplied at typical post-meal + active-flare conditions, with confidence bounds throughout. Pass 3 softening discipline baked in (combined-coverage is the *outcome*, not the *input*). Decision rule: GREEN if combined CI clears either singleton CI; YELLOW if overlap; RED if interaction blocker surfaces.

Auto-appended review-task as walkthrough **Item 25 — Review comp-029 output** per skill Section 4 background-subagent rule. The subagent's output will be reviewed at its natural walkthrough turn, not when its notification arrives.

**Remaining gated work (NOT actioned today; all conditional on comp-029 outcome):**
- Item 15 (Experiment 3, wet-lab gate "Combined CP0 coverage assay: rosmarinic acid + DAF SCR1-4 in zymosan-activation C5a-generation model") — walks separately when its turn comes; the wet-lab addition to §1.25 gates on comp-029 GREEN.
- H10 hypothesis stub deferred — H-cards are most valuable once there's a concrete prediction to falsify. Revisit after comp-029 returns.

No wiki content changes in this commit (§9.7 already comprehensive; comp-029 row stays in Planned Analyses until the subagent moves it). The substantive output is the spawned subagent + Item 25.
