---
type: experiment
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 2
global_index: 6
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Model DAF SCR1-4 and Lactoferrin expression burden in *E. coli* Nissle.

2. **Model DAF SCR1-4 and Lactoferrin expression burden in *E. coli* Nissle.** `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`
   - *Cost:* $0 (computational). *Time:* 1-2 weeks. *Decides:* Whether the LBP chassis is a computationally viable alternative to koji for folding disulfide-rich proteins, as proposed in "New Connections #2".
   - *Protocol:* Perform an in-silico analysis. Use existing genome-scale metabolic models (GEMs) for *E. coli* combined with literature data on the DsbA/DsbC periplasmic folding pathway's capacity. Estimate the metabolic and folding burden of expressing DAF SCR1-4 (8 disulfides) and Lactoferrin (16 disulfides).
   - *Comparison:* Compare the predicted burden and maximum theoretical yield in EcN to the known limits of the *A. oryzae* ER/PDI system documented in `chaperone-orthogonal-stacking.md`.
   - *Success:* The model predicts that EcN can handle the PDI-equivalent load of both proteins with less competition/burden than the koji model predicts. This would justify prioritizing the LBP chassis for these specific high-value payloads.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The experiment is directionally sensible and the $0 cost / 1–2 week timeline is attractive. The flaw is that it proposes GEM-based modeling of DsbA/DsbC periplasmic folding capacity for DAF SCR1-4 (8 disulfides) and lactoferrin (16 disulfides), but the `chaperone-orthogonal-stacking.md` framework (§8 item 6) explicitly flags that no published *E. coli*-specific PDI-equivalent capacity metric exists for the Dsb system at this disulfide scale. A standard *E. coli* GEM (e.g., iJO1366) does not model periplasmic disulfide bond formation — it models metabolic flux, not folding-machinery competition. The right computational move is NOT a GEM but a `comp-006`-style protease-stability + folding-feasibility analysis for DAF SCR1-4 and lactoferrin in the EcN periplasmic environment (analogous to comp-037 for C1-INH). That analysis is zero-cost and directly tests whether the DsbA/DsbC system can handle these payloads. Rephrase the experiment accordingly; the question ("is EcN a viable chassis for these payloads?") is right, but the tool (GEM) is wrong for the folding question.

---

## ✓ Actioned 2026-07-13

**Fulfilled by comp-043.** The card proposed modeling DAF SCR1-4 + lactoferrin expression burden in EcN via a genome-scale metabolic model (GEM); Pass 3 correctly flagged GEM as the wrong tool (models metabolic flux, not folding-machinery competition). Swapped for the right instrument — a comp-006/comp-037-style structural + sequence folding-feasibility analysis — executed as [comp-043](../../wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md). Verdict: folding crossover at DAF SCR1-4 (8 disulfides); lactoferrin (16) not viable in EcN. comp-043 creates no new wet-lab gate — it reallocates chassis assignment (lactoferrin → koji only; DAF → primarily koji, EcN provisional secondary) and names the highest-leverage missing measurement (DsbA/DsbC capacity assay at 8–16 disulfide scale). $0, executed today.
