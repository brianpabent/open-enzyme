---
type: most-curious-thread
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 1
global_index: 16
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Of everything surfaced in this sweep, the thread I’d spend the next experiment slot on is the cordycepin koji-engineering route (cns1+cns2) as a chaperone-orthogonal third cassette for the endgame strain.

Of everything surfaced in this sweep, the thread I’d spend the next experiment slot on is the **cordycepin koji-engineering route (cns1+cns2) as a chaperone-orthogonal third cassette for the endgame strain.** The convergence of evidence is multi-track: (a) the chaperone-orthogonal stacking framework predicts that cytosolic cns1+cns2 enzymes impose zero ER load and would stack additively with uricase + lactoferrin (predicted synergy ≥0.9); (b) `medicinal-mushroom-complement-track.md` Phase 7-1b documents Jeennor 2023’s demonstration of cordycepin production in *A. oryzae* at 564 mg/L/day, making the route precedent-adjacent; (c) comp-015 v2 establishes cordycepin as a gout-favorable URAT1 modulator, giving it a clear therapeutic chokepoint that the current dual-cassette strain does not cover. The refutation would come from a combined metabolic-model + chaperone-load analysis showing that cordycepin biosynthesis (which requires ATP, SAM, and precursor flux) either imposes a growth penalty on the dual-cassette strain or depletes the precursor pools needed for kojic acid/ergothioneine native metabolite production. The cheapest discriminating experiment is **in-silico metabolic-flux analysis of the cns1+cns2 pathway on top of the uricase + lactoferrin background** (comp-021 candidate), combined with a chaperone-orthogonality scoring per the existing framework — combined cost ~$0, 1–2 weeks. If the in silico prediction is favourable, a wet-lab co-expression test could be added as an arm of the §1.9 extended design at marginal cost. I suspect other sweep models (especially those with strong synthetic-biology priors) would converge on this thread — the multi-payload, single-chassis logic is the core value proposition of Open Enzyme, and cordycepin is the only currently surfaced compound that extends the strain’s chokepoint coverage without triggering the PDI-saturation constraints that gate out DAF SCR1-4.



Sources cited:
- wiki/autonomous-screening-methodology.md
- wiki/computational-experiments.md
- wiki/medicinal-mushroom-compound-mapping-computational.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/engineered-lbp-chassis.md
- wiki/personal-genome-protocol.md
- wiki/t-axis-adjuvant-urate-mapping-computational.md
- wiki/androgen-natural-modulation.md
- wiki/enzyme-quantification-protocol.md
- wiki/medicinal-mushroom-extract-sops.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/medicinal-mushroom-complement-track.md
- wiki/koji-endgame-strain.md
- wiki/uricase-abcg2-genotype-stratification-computational.md
- wiki/cross-validation.md
- wiki/gut-lumen-sink.md

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The cordycepin thread is genuinely interesting and the cheapest discriminating experiment is correctly identified, but the synthesis overclaims novelty and uniqueness: `chaperone-orthogonal-stacking.md` already contains the cns1+cns2 row with zero ER/PDI load, and `koji-endgame-strain.md` already has carnosine as a cytosolic optional third cassette that extends URAT1/GLUT9 coverage without PDI saturation. The strongest version of this item is not “cordycepin is the only such compound,” but “cordycepin is an additional cytosolic small-molecule arm with demonstrated *A. oryzae* production precedent and a distinct URAT1-modulating mushroom-track bridge, pending metabolic-burden modeling.”
