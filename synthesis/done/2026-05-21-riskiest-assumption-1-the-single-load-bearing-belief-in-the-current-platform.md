---
type: riskiest-assumption
sweep_date: 2026-05-21
sweep_sha: 3edb643
section_index: 1
global_index: 14
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The single load-bearing belief in the current platform thesis least supported by the corpus is that dietary doses of rosmarinic acid, luteolin, and Houttuynia cordata polysaccharide reach gut-luminal concentrations sufficient to meaningfully suppress complement activation at the C3 convertase / C4 / C5 nodes — and that this gut-luminal complement suppression propagates to reduced systemic C5a-driven NLRP3 priming at the MSU crystal surface.

**The single load-bearing belief in the current platform thesis least supported by the corpus is that dietary doses of rosmarinic acid, luteolin, and Houttuynia cordata polysaccharide reach gut-luminal concentrations sufficient to meaningfully suppress complement activation at the C3 convertase / C4 / C5 nodes — and that this gut-luminal complement suppression propagates to reduced systemic C5a-driven NLRP3 priming at the MSU crystal surface.**

The corpus has built an entire upstream-CP0 dietary strategy (comp-018, comp-020, comp-039) on the assumption that post-meal gut-luminal concentrations of these dietary candidates clear the IC50 threshold for their respective complement targets. The PK evidence is almost entirely unanchored: rosmarinic acid's gut-luminal concentration after a dietary rosemary/lemon-balm meal is estimated at 252–1,100 µM (Kang 2021, a computational estimate from oral dose + intestinal volume assumptions, not a direct measurement), which overlaps the C3b-deposition IC50 range (34–180 µM after comp-021's assay-format stratification) — but the uncertainty band is 4–5×. Luteolin's dietary PK after a celery/parsley meal is uncharacterized at the gut-luminal level. Houttuynia polysaccharide's absorption and gut-luminal residence time after oral consumption is completely unstudied. None of the three has a direct in vivo measurement of gut-luminal complement suppression after dietary intake.

If the actual gut-luminal concentrations fall below the IC50 threshold for any of these candidates, the dietary CP0 strategy collapses from "mechanism-grounded dietary intervention" to "interesting pharmacology that doesn't translate at the dinner table." The CFH-dependence classification (comp-039) is computationally rigorous; the missing variable is whether the candidates ever reach their target at dietary doses. The platform has built a three-candidate CP0 stack on a PK assumption that has never been directly measured.

This belief is anchored to `complement-c5a-gout.md` §9.7 (the combined CP0 strategy section), `upstream-complement-verification-rerun-computational.md` (which documented the 44× IC50 spread but did not resolve the PK question), `combined-cp0-systems-model-computational.md` (comp-029, which used wide PK priors explicitly because the data doesn't exist), and `cfh-mechanism-dissociation-cp0-candidates-computational.md` §6 (which names bioavailability as a limitation but treats it as a secondary caveat, not the primary load-bearing unknown). The evidence against it is negative space — no direct measurement exists. The closest positive evidence is the gut-luminal concentration estimate for rosmarinic acid (Kang 2021), which is a calculation, not a measurement.



---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right riskiest-assumption call: `combined-cp0-systems-model-computational.md` shows rosmarinic acid’s plausible CP0 effect is gut-luminal rather than systemic, `cfh-mechanism-dissociation-cp0-candidates-computational.md` §6 names bioavailability as a limitation for all four candidates, and `complement-c5a-gout.md` §9.7 explicitly preserves the rosmarinic-acid assay-format and PK caveats. The platform has stronger mechanistic evidence for CFH-independence than for dietary exposure actually reaching the relevant complement compartment. Prioritize PK / gut-luminal complement-readout validation before further expanding the dietary CP0 stack.

---

## ✓ Actioned 2026-05-22

**Riskiest Assumption #3 added** to `open-questions.md` Platform / Strategic section 2026-05-22, sitting alongside RA #1 (gut-lumen sink mechanism, mechanism side) and RA #2 (community fermentation reliability, production side). RA #3 covers the dietary-CP0 PK side — whether dietary doses of rosmarinic acid, luteolin, Houttuynia, and Helicteres reach gut-luminal concentrations sufficient to meaningfully suppress complement at C3 convertase / C4 / C5 nodes.

Entry structure mirrors RA #1 + RA #2:

- **Anchored against existing corpus content** — comp-029 gut-luminal-transient reframe (rosmarinic acid systemic ~0% inhibition at free plasma Cmax 20 nM, ~1,700× below central IC50 — leverage is gut-luminal post-meal window only); comp-039 §6 bioavailability limitation across all four candidates; complement-c5a-gout.md §9.7 IC50 spread + tissue occupancy caveats. Per Pass 3, these were named but not promoted to platform-level riskiest-assumption status.
- **Provisional alive/killed thresholds** — Alive: at least one candidate produces measured gut-luminal concentration ≥ IC50 lower bound in a fed-state human study AND biobank cross-tab supports CFH-independence prediction. Killed: none of the four reach IC50 lower bound within an order of magnitude AND biobank returns null/AMD-paradox direction.
- **Four Phase 2 follow-ups:** P2-1 stable-isotope tracer feasibility scan; P2-2 gut-luminal complement-activity readout as functional proxy; P2-3 gate further dietary CP0 candidate expansion on at least one PK anchor; P2-4 re-anchor §9.9 dormant composition gate.
- **Comparison table** with RA #1 + RA #2 explaining why all three are non-redundant.

Pass 3's "Prioritize PK / gut-luminal complement-readout validation before further expanding the dietary CP0 stack" is implemented as P2-3 (operational gate on candidate expansion). The §9.9 dormant composition's reactivation conditions are now strengthened — RA #3 closure is the cheaper of the two reactivation paths.

Closure complete.
