---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 7
global_index: 7
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# C1-INH on EcN + dietary rosmarinic acid compose into a dietary + engineered two-node CP0 strategy — the missing composition between the two-chassis architecture (§9.8) and the dietary-thread-only frame (§9.7).

7. **C1-INH on EcN + dietary rosmarinic acid compose into a dietary + engineered two-node CP0 strategy — the missing composition between the two-chassis architecture (§9.8) and the dietary-thread-only frame (§9.7).** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `c1-inh-protease-stability-ecn-computational.md`, `complement-c5a-gout.md`, `upstream-complement-modulator-sweep-computational.md`, `upstream-complement-verification-rerun-computational.md`
   - *Page-pair linkage:* complement-c5a-gout.md §9.7 models dietary rosmarinic acid + engineered DAF SCR1-4 (comp-029, YELLOW). §9.8 models engineered C1-INH on EcN + engineered DAF SCR1-4 on koji (two-chassis, two-node). Neither section models dietary rosmarinic acid + engineered C1-INH. The C1-INH thread (comp-037) and the dietary rosmarinic acid thread (comp-018/020) have never been composed. Partially matched because the individual sub-steps are known; the composition is genuinely new.
   - *Why It Matters:* C1-INH (SERPING1, comp-037, MODERATE kinetic-competition gated) acts at classical/lectin pathway ENTRY — it inactivates C1r/C1s/MASP-2 before C4b2a convertase forms. Rosmarinic acid (comp-018/020, Tier 1 dietary) acts one step DOWNSTREAM — it covalently modifies C3b and inhibits C3 convertase. These are two different cascade nodes (entry vs. amplification) via two completely different delivery substrates (engineered LBP vs. dietary herb). The composition would provide two-layer CP0 coverage without requiring DAF SCR1-4 or avacopan. The mechanism logic is: C1-INH prevents convertase formation at the classical/lectin entry point → whatever C3b deposits anyway (via alternative pathway tick-over or incomplete C1-INH coverage) gets blocked by dietary rosmarinic acid at the C3 convertase step. Two nodes, two independent failure modes, one dietary + one engineered. This composition has been hiding in plain sight because the §9.7 and §9.8 framings used different engineering partners for the dietary arm (DAF in §9.7, C1-INH in §9.8) and never swapped them.
   - *Suggested Action:* Add a brief "C1-INH + dietary rosmarinic acid" composition note to complement-c5a-gout.md as a third combined-CP0 strategy (alongside §9.7 and §9.8), with the explicit caveat that both components have unresolved wet-lab gates (C1-INH: RCL kinetic competition assay; rosmarinic acid: 44× assay-format IC50 spread per comp-020 + gut-luminal PK unresolved per comp-029). Do NOT queue a comp-NNN for this composition until at least one component's gate clears — the combined prediction would inherit both uncertainties multiplicatively. Track as a dormant composition.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The composition is real and not already named: `complement-c5a-gout.md` §9.7 covers rosmarinic acid + DAF SCR1-4, while §9.8 covers C1-INH + DAF SCR1-4, but neither composes C1-INH with dietary rosmarinic acid. The mechanistic layering is coherent — C1-INH blocks classical/lectin entry at C1r/C1s/MASP-2, while rosmarinic acid acts downstream on C3b / convertase biology — but both arms are gated hard: comp-037 leaves C1-INH at RCL kinetic-competition risk, and comp-029 reframes rosmarinic acid as gut-luminal-transient rather than systemic CP0 coverage. Dormant composition note is the right action; do not promote to a new comp until one component’s wet-lab gate clears.

---

**WALKED 2026-05-19 — Closed (§9.9 dormant composition added to complement-c5a-gout.md, gated on either component arm's wet-lab gate clearing).**

Actioned:
- ✓ Added new §9.9 "Dormant composition — C1-INH (LBP-luminal) + dietary rosmarinic acid" section to `complement-c5a-gout.md` (between §9.8 two-chassis architecture and §10 natural-product modulators). Names the third combined-CP0 strategy alongside §9.7 (rosmarinic + DAF) and §9.8 (C1-INH + DAF).
- ✓ Mechanism layering documented: C1-INH blocks classical/lectin entry (C1r/C1s/MASP-2 → no C4b2a convertase); rosmarinic acid blocks one step downstream (covalent C3b modification → no C3 convertase). Two cascade nodes, two delivery substrates (engineered LBP + dietary herb).
- ✓ Pass 3's "dormant" discipline encoded: explicit reactivation conditions documented (IF C1-INH RCL kinetic-competition assay clears OR rosmarinic acid gut-luminal PK clears → arm is de-risked → combined prediction becomes worth a comp-NNN). Multiplicative-uncertainty rationale stated. No asserted synergy; no clinical effect-size prediction.

Closes the composition as a documented architecture option without committing wet-lab budget — the dormant framing is the right epistemic tier given both arms' unresolved gates.
