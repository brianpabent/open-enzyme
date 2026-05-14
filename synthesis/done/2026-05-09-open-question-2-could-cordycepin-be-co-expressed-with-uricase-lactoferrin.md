---
type: open-question
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 2
global_index: 11
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Could cordycepin be co-expressed with uricase + lactoferrin in a single *A. oryzae* strain without triggering metabolic or chaperone collapse?

2. **Could cordycepin be co-expressed with uricase + lactoferrin in a single *A. oryzae* strain without triggering metabolic or chaperone collapse?** The chaperone framework predicts strong orthogonality (cns1+cns2 are cytosolic, zero ER load), but no empirical multi-cassette data exist for this specific combination. The metabolic burden of cordycepin biosynthesis (ATP cost, precursor supply) is uncharacterised in the koji chassis. (Connection #5)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` This is the right residual uncertainty after the chaperone correction: the ER-load question is settled in the corpus for cns1+cns2, but no page has modeled the ATP, precursor, SAM, growth, or native-metabolite burden of cordycepin biosynthesis on a dual uricase + lactoferrin strain. `chaperone-orthogonal-stacking.md` also explicitly says its framework does not track generic proteome/metabolic burden for cytosolic biosynthetic clusters, so this is a legitimate next question.

---

## ✓ Actioned 2026-05-14

Queued as **comp-023** in [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) §Planned Analyses: metabolic / proteome burden of cns1+cns2 cordycepin biosynthesis on top of the dual uricase + lactoferrin cassette. Flux-balance or pcSecKoji-style model evaluating ATP / SAM / precursor / translation-pool burden, comparators against wild-type + dual-cassette + existing optional cytosolic third cassettes (carnS, panD).

Closes the proteome-burden gap that `chaperone-orthogonal-stacking.md` line 238 explicitly flags as out-of-scope for the chaperone framework. Decision thresholds wired into the brief: <10% growth penalty AND >80% native yield = green-light cordycepin arm in §1.9 extended design; >10% growth penalty OR >20% native yield reduction = red-flag, route to LBP chassis or separate strain.

Brief queued; run deferred per same discipline as comp-022 and comp-024. Closes alongside the other items in this cluster ([2026-05-09-experiment-2](./2026-05-09-experiment-2-in-silico-cns1-cns2-compatibility-assessment-with-uricase.md), [2026-05-09-open-question-2](./2026-05-09-open-question-2-could-cordycepin-be-co-expressed-with-uricase-lactoferrin.md), [2026-05-09-most-curious-thread-1](./2026-05-09-most-curious-thread-1-of-everything-surfaced-in-this-sweep-the-thread-id-spend.md), and the already-closed [2026-05-09-connection-5](./2026-05-09-connection-5-cordycepin-koji-engineering-cns1-cns2-is-implicitly.md)).
