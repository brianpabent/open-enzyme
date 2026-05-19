---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 4
global_index: 4
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The serpin-fold architecture is absent from the chaperone-orthogonal-stacking framework's α-coefficient calibration set — creating a prediction gap for the C1-INH-on-EcN engineering thread that comp-037 just substantiated.

4. **The serpin-fold architecture is absent from the chaperone-orthogonal-stacking framework's α-coefficient calibration set — creating a prediction gap for the C1-INH-on-EcN engineering thread that comp-037 just substantiated.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `c1-inh-protease-stability-ecn-computational.md`, `chaperone-orthogonal-stacking.md`, `engineered-lbp-chassis.md`, `complement-c5a-gout.md`
   - *Page-pair linkage:* chaperone-orthogonal-stacking.md §3.5.2 defines α coefficients for CCP/SCR (0.3–0.6), Ig-like (1.0 reference), and transferrin-lobe (1.5–2.5). The serpin fold — which C1-INH belongs to — has no coefficient. comp-037 does not reference the chaperone framework at all (it's an EcN-LBP protease-stability analysis, not a koji secretion-burden analysis). But the serpin α coefficient matters for the LBP chassis: if C1-INH is ever expressed in a secreted format (rather than the luminal format comp-037 models), the α coefficient determines whether it competes with other disulfide-rich payloads. Moreover, the generalization caveat at chaperone-orthogonal-stacking.md §8 item 6 explicitly names "C1-INH serpin" as a fold class the framework does NOT cover. This is a documented gap with a specific payload candidate now substantiated by comp-037.
   - *Why It Matters:* comp-037's MODERATE verdict for C1-INH on EcN pushes the two-chassis CP0 architecture (C1-INH on LBP + DAF SCR1-4 on koji, complement-c5a-gout.md §9.8) from scoped to substantiated. The next question is chassis selection for C1-INH: EcN luminal (as comp-037 models) or secreted in a different chassis. If secreted, the serpin α coefficient is needed to predict PDI/ERO1 competition. Serpins have a distinctive fold: a central β-sheet A with a reactive-center loop (RCL) that undergoes a dramatic β-sheet insertion conformational change upon protease binding. C1-INH has only 2 disulfides (grep-verified in comp-037), making it PDI-light relative to lactoferrin — but the metastable serpin fold may have different chaperone engagement kinetics than any calibrated fold class. The framework gap is explicit and documented; the new data is that the C1-INH payload is now computational-gate-substantiated, making the gap load-bearing.
   - *Suggested Action:* Extend the chaperone framework's α-coefficient table (§3.5.2) to include a provisional serpin row with a bounded estimate (plausible range 0.5–1.5 based on the 2-disulfide / ~48 kDa / metastable-fold profile, explicitly flagged as uncalibrated). Queue as a standing note that the serpin α coefficient needs experimental calibration before any C1-INH-on-secreted-chassis design decision. Cross-reference from c1-inh-protease-stability-ecn-computational.md to chaperone-orthogonal-stacking.md §3.5.2.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The gap is real: `chaperone-orthogonal-stacking.md` defines α coefficients for CCP/SCR, Ig-like, and transferrin-lobe folds, and §8’s generalization caveat explicitly names “C1-INH serpin” as a fold class not covered by the calibration set. comp-037 makes that omission load-bearing by elevating C1-INH-on-EcN to MODERATE with LOW strictly-degradative serpin-body risk and GREEN glycosylation feasibility, leaving RCL kinetic competition as the wet-lab gate. A provisional serpin α row is justified if it is labeled uncalibrated and linked to the C1-INH RCL / metastable-serpin-fold uncertainty.

---

**WALKED 2026-05-19 — Closed (provisional serpin row added to chaperone-orthogonal-stacking.md §3.5.2 + §3.5.3; lit scan subagent firing for refinement).**

Actioned:
- ✓ Added provisional serpin row to `chaperone-orthogonal-stacking.md` §3.5.2: archetype = C1-INH (SERPING1), α1-antitrypsin (SERPINA1), antithrombin III (SERPINC1); α = 0.5–1.5 (PROVISIONAL — uncalibrated); basis = low disulfide counts (C1-INH 2; α1-antitrypsin 0; antithrombin III 3) keep raw PDI load light, but the metastable native fold with RCL undergoing dramatic β-sheet insertion may engage BiP/calnexin/PDI differently than any calibrated class — particularly because misfolded serpins polymerize and trigger UPR.
- ✓ Added C1-INH (SERPING1, P05155) row to §3.5.3 effective PDI load table: 2 disulfides × 0.5–1.5 α = **1.0–3.0 effective PDI load (PROVISIONAL)**.
- ✓ Both rows flagged with [NUMBER UNVERIFIED — provisional bound from structural/disulfide-count profile only] and reference to the running lit-scan log (`logs/serpin-fold-alpha-coefficient-lit-scan-2026-05-19.md`).
- 🔄 Lit-scan subagent firing in background: target proteins α1-antitrypsin / antithrombin III / C1-INH / PAI-1 / ovalbumin folding kinetics (ER retention time, BiP/PDI engagement, cooperative vs hierarchical folding, metastable-fold chaperone interaction). Output → `logs/serpin-fold-alpha-coefficient-lit-scan-2026-05-19.md`. Same pattern as Cluster A2: subagent reports findings → Brian propagates refined bound into framework if literature supports tighter range.

Cross-reference deferred to subagent return: `c1-inh-protease-stability-ecn-computational.md` will get an explicit pointer to chaperone-orthogonal-stacking.md §3.5.2 in the same propagation pass that absorbs the subagent's findings — so both edits land coherently in one batch.

Also closes:
- 2026-05-17 open-question-1 (same lit-scan question framed as open question).
