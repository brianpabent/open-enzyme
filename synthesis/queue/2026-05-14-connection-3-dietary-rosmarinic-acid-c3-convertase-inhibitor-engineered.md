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

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The cross-track pairing is worth surfacing, but the mechanism prose overclaims the evidence. `upstream-complement-verification-rerun-computational.md` reports rosmarinic acid as mechanistically distinctive at C3b deposition with IC50 34 µM, but also documents a 44× assay-format spread and flags dietary bioavailability/occupancy as unresolved; it does not support “saturates fluid-phase and gut-luminal C3 convertase.” Likewise `complement-c5a-gout.md` lists luminal-side DAF engagement and MSU-surface geometry as wet-lab unknowns, so “mechanistically additive” should be phrased as a testable hypothesis, not an asserted synergy.
