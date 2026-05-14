---
type: experiment
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 2
global_index: 8
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# In silico cns1+cns2 compatibility assessment with uricase + lactoferrin (comp-021).

2. **In silico cns1+cns2 compatibility assessment with uricase + lactoferrin (comp-021).** Cost: ~$0. Time: 1–2 weeks. Decides: whether the cordycepin koji-engineering route is predicted chaperone-orthogonal and metabolically tractable on top of the existing dual cassette, per Connection #5. If yes, adds a cordycepin arm to the §1.9 extended design.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The metabolic-flux compatibility question is valid, but the “whether the route is predicted chaperone-orthogonal” part is already answered: `chaperone-orthogonal-stacking.md` scores cns1+cns2 as cytosolic, secretion-bypassing, effective PDI load 0, and `medicinal-mushroom-complement-track.md` documents the Jeennor 2023 *A. oryzae* cordycepin route at 564 mg/L/day. Reframe the experiment as a proteome/metabolic-burden and precursor/ATP/SAM-flux analysis layered onto the uricase + lactoferrin background, not as a first-pass chaperone-orthogonality assessment.

---

## ✓ Actioned 2026-05-14

Queued as **comp-023** in [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) §Planned Analyses: metabolic / proteome burden of cns1+cns2 cordycepin biosynthesis on top of the dual uricase + lactoferrin cassette. Flux-balance or pcSecKoji-style model evaluating ATP / SAM / precursor / translation-pool burden, comparators against wild-type + dual-cassette + existing optional cytosolic third cassettes (carnS, panD).

Closes the proteome-burden gap that `chaperone-orthogonal-stacking.md` line 238 explicitly flags as out-of-scope for the chaperone framework. Decision thresholds wired into the brief: <10% growth penalty AND >80% native yield = green-light cordycepin arm in §1.9 extended design; >10% growth penalty OR >20% native yield reduction = red-flag, route to LBP chassis or separate strain.

Brief queued; run deferred per same discipline as comp-022 and comp-024. Closes alongside the other items in this cluster ([2026-05-09-experiment-2](./2026-05-09-experiment-2-in-silico-cns1-cns2-compatibility-assessment-with-uricase.md), [2026-05-09-open-question-2](./2026-05-09-open-question-2-could-cordycepin-be-co-expressed-with-uricase-lactoferrin.md), [2026-05-09-most-curious-thread-1](./2026-05-09-most-curious-thread-1-of-everything-surfaced-in-this-sweep-the-thread-id-spend.md), and the already-closed [2026-05-09-connection-5](./2026-05-09-connection-5-cordycepin-koji-engineering-cns1-cns2-is-implicitly.md)).
