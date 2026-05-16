---
type: contradiction
sweep_date: 2026-05-15
sweep_sha: ebbce26
section_index: 1
global_index: 5
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The chassis-pending intervention list risks diluting the centralized home-fermentation thesis without a clear triage framework for which chassis to pursue first.

1. **The chassis-pending intervention list risks diluting the centralized home-fermentation thesis without a clear triage framework for which chassis to pursue first.** *Documents Connected:* `chassis-pending-interventions.md`, `open-enzyme-vision.md`, `open-source-platform.md`
   - *Analysis:* The platform vision explicitly positions the koji chassis as the first and primary output of the discovery engine, with the strain library as the mechanism for democratized access. The newly added chassis-pending inventory, however, aggregates seven distinct interventions (engineered EcN PDB, siRNA URAT1, LBPs, inhaled mRNA, intra-articular uricase, bacteriophage, pharmacological chaperones) that span commercial pharma, synthetic biology, and formulation chemistry — none of which are home-fermentable. While the discipline “chassis is downstream of chokepoint” is correctly articulated, the practical implication is that a growing fraction of the platform’s most promising leads now live outside the original vision of “grow at home.” There is currently no explicit decision rule for when a chassis-pending intervention should be promoted to an active peer track versus parked as a discovery-engine output.
   - *Resolution:* This is not a contradiction to be resolved by removing interventions, but a **strategic design gap** — the project needs a “chassis triage rubric” to guide resource allocation. This could be formalized as a small addition to `open-source-platform.md` or `chassis-pending-interventions.md` itself.
   

---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right strategic critique and it respects the chassis-downstream discipline: `chassis-pending-interventions.md` explicitly says these entries are “not deprioritized, not off-platform,” but its “When an entry leaves this page” section only defines migration once a chassis is selected; it does not give a resource-allocation rubric for promoting a chassis-pending intervention into an active peer track. `open-enzyme-vision.md` and `open-source-platform.md` correctly frame koji as the highest-priority chassis-shaped expression of the mission, not the mission itself, so the missing piece is a chokepoint-first triage rule rather than a return to koji filtering. Prioritize adding a rubric keyed to chokepoint leverage, evidence tier, cheapest first move, and chassis maturity.

---

## ✓ Actioned 2026-05-16 — closed without rubric (operator pushback)

**The contradiction was a framing artifact, not a real structural gap.** Walkthrough operator (Brian) pushed back on the rubric recommendation: the daemon's Pass 2 already re-evaluates every chassis-pending entry against current corpus state on every sweep, and the walkthrough operator's per-item decision IS the promote / park / falsify call. The same walkthrough (Items 1–5) produced concrete evidence of this mechanism working — PDB×disulfiram CP6 stack named, CFTR-corrector Q141K chaperone promoted to comp-032, inhaled mRNA-IL-1RA temporal complement landed in open-enzyme-vision.md §10 + comp-033 — none required a documented rubric to action. A static rubric would have been documentation that re-derives what Pass 2 already does, drifting from the live evaluator faster than the evaluator updates.

Both Pass 2 (synthesizer) and Pass 3 (reviewer) fell into a "name a rule and document it" frame. This is a recurring architectural-bias pattern in synthesizer / reviewer recommendation generation that the walkthrough operator should de-prefer when it surfaces. Recorded as a structural observation:

- [`wiki/chassis-pending-interventions.md`](../../wiki/chassis-pending-interventions.md) — single-paragraph subsection "### How decisions actually get made — there's no static rubric, by design" inside the existing "When an entry leaves this page" section. Names the dynamic mechanism explicitly so the page is self-documenting; no rubric added.
- [`scripts/SWEEP-ARCHITECTURE.md`](../../scripts/SWEEP-ARCHITECTURE.md) — new section "Static-rubric bias in Pass 2 + Pass 3 recommendations" documenting the observation as a recurring pattern. Includes operational guidance for future walkthroughs (default = close with dynamic-mechanism annotation, no rubric; only add documented rules when they encode constraints the daemon cannot currently surface OR span multi-operator / partner-organization contexts). Proposes a future Pass 3 prompt iteration check: "before recommending a documented rubric, verify the recommendation isn't re-describing existing daemon behavior."

No new rubric. No pre-classification table. The contradiction is closed by naming what's already true.

**Meta-pattern recorded for future sweeps:** when Pass 2 surfaces a "we need a documented framework / rubric / triage rule" recommendation, the walkthrough operator should immediately ask "is the daemon already doing this?" The answer is usually yes; the contradiction is then a framing artifact and closure is a short annotation, not new infrastructure.
