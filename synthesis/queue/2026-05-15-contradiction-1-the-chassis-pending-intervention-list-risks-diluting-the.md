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
