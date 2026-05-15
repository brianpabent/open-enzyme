---
type: connection
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 3
global_index: 3
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Dietary rosmarinic acid (C3 convertase inhibitor) + engineered DAF SCR1-4 (surface decay-accelerator) provide dual-mechanism CP0 coverage at different geometric scales — a cross-track synergy between the upstream-complement dietary thread and the koji engineering thread.

3. **Dietary rosmarinic acid (C3 convertase inhibitor) + engineered DAF SCR1-4 (surface decay-accelerator) provide dual-mechanism CP0 coverage at different geometric scales — a cross-track synergy between the upstream-complement dietary thread and the koji engineering thread.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `complement-c5a-gout.md`, `upstream-complement-modulator-sweep-computational.md` (comp-018), `upstream-complement-verification-rerun-computational.md` (comp-020), `daf-cd55-scr14-truncated-computational.md` (comp-012), `chaperone-orthogonal-stacking.md`, `medicinal-mushroom-extract-sops.md`
   - *Page-pair linkage:* `complement-c5a-gout.md` links to `daf-cd55-scr14-truncated-computational.md` (CP0 engineering thread) and to `upstream-complement-modulator-sweep-computational.md` (dietary thread). However, the dietary thread’s lead compound (rosmarinic acid) and the engineering thread’s lead construct (DAF SCR1-4) are not discussed as a combined strategy in any page. The two threads are presented as parallel, not synergistic.
   - *Why It Matters:* comp-018/020 identified rosmarinic acid as a dietary C3 convertase inhibitor with 30+ years of primary literature (covalent C3b modification, IC50 34 µM). comp-012 and the chaperone framework confirmed DAF SCR1-4 is engineerable in koji (LOW protease risk, effective PDI load 2.4–4.8). These two interventions operate at different geometric scales: dietary rosmarinic acid saturates fluid-phase and gut-luminal C3 convertase; engineered DAF SCR1-4 saturates the MSU crystal surface where convertase assembly occurs. They are **mechanistically additive** — rosmarinic acid reduces the C3b deposition substrate that DAF then accelerates the decay of. A combined strategy could provide robust, two-layer CP0 coverage without relying solely on avacopan. This is a cross-track synergy between the medicinal-mushroom/TCM dietary track and the koji engineering track, not yet named in the corpus.
   - *Suggested Action:* Add a “Combined CP0 strategy” subsection to `complement-c5a-gout.md` that explicitly names the rosmarinic acid (dietary) + DAF SCR1-4 (engineered) combination, with a note that the two mechanisms are predicted additive. Queue a computational systems model of the combined C3 convertase inhibition under MSU-surface conditions (comp-NNN candidate).

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The cross-track pairing is worth surfacing, but the mechanism prose overclaims the evidence. `upstream-complement-verification-rerun-computational.md` reports rosmarinic acid as mechanistically distinctive at C3b deposition with IC50 34 µM, but also documents a 44× assay-format spread and flags dietary bioavailability/occupancy as unresolved; it does not support "saturates fluid-phase and gut-luminal C3 convertase." Likewise `complement-c5a-gout.md` lists luminal-side DAF engagement and MSU-surface geometry as wet-lab unknowns, so "mechanistically additive" should be phrased as a testable hypothesis, not an asserted synergy.

---

## ✓ Actioned 2026-05-15

The cross-track pairing is real and worth naming as a testable hypothesis; Pass 3's softening on the synergy/saturation claims is preserved throughout.

**Files shipped:**

- **`wiki/complement-c5a-gout.md` §9.7 (new)** — "Combined CP0 strategy (testable hypothesis) — dietary rosmarinic acid + engineered DAF SCR1-4." Frames as testable hypothesis, not asserted synergy. Three explicit "what this section does NOT claim" caveats baked in: (a) no "saturation" claim — comp-020's 44× IC50 spread + unresolved bioavailability surfaced inline; (b) no "mechanistically additive" assertion — luminal DAF engagement + MSU-surface geometry are explicitly named as wet-lab unknowns; (c) no clinical effect-size prediction — gated by the same H08-class translation question. Worked-out cross-track logic + wet-lab follow-up gated on comp-029 GREEN.
- **`wiki/computational-experiments.md` Planned Analyses** — queued **comp-029** (Combined CP0 systems model). Brief enforces BioDesignBench evaluation-depth discipline: two orthogonal models (rosmarinic-acid C3 convertase kinetics with explicit 44× IC50 range; DAF SCR1-4 decay-accelerator kinetics with explicit prior bounds for MSU-surface geometry); cross-multiply at post-meal conditions; output predicted combined-effect range with explicit bounds (not a point estimate). GREEN/YELLOW/RED decision rule includes an RED-on-interaction-blocker case (e.g., DAF inactivated under rosmarinic-acid-bioavailable conditions). If GREEN: marginal-cost rosmarinic-acid co-treatment arm on `validation-experiments.md` §1.25.

**Six-surface tracking:**
1. `wiki/complement-c5a-gout.md` §9.7 (canonical combined-CP0 hypothesis framing)
2. `wiki/computational-experiments.md` Planned Analyses — comp-029 row
3. `wiki/validation-experiments.md` §1.25 — already references the DAF expression screen; comp-029 GREEN would gate a co-treatment arm (no edit needed; cross-linked from §9.7)
4. (no H-card update — the H05 DAF thesis stub already exists; the combined-strategy hypothesis is a §9.7 extension, not a new H-card)
5. (not surfaced on `index.md` — this is a sub-strategy hypothesis, not a platform-level riskiest assumption; the H05 DAF thesis is the index-level anchor)
6. This closure annotation + the queue→done move

Pass 3's softening discipline applied throughout. Closing.
