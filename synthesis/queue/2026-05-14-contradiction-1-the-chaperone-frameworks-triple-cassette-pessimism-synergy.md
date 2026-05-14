---
type: contradiction
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 1
global_index: 5
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The chaperone framework’s triple-cassette pessimism (synergy 0.35–0.65 for uricase + Lf + DAF SCR1-4) implicitly assumes the third cassette is secreted — but the cordycepin burden analysis demonstrates that a cytosolic third cassette imposes zero PDI load, making the triple-cassette design tractable via payload-class selection rather than separate-strain routing.

1. **The chaperone framework’s triple-cassette pessimism (synergy 0.35–0.65 for uricase + Lf + DAF SCR1-4) implicitly assumes the third cassette is secreted — but the cordycepin burden analysis demonstrates that a cytosolic third cassette imposes zero PDI load, making the triple-cassette design tractable via payload-class selection rather than separate-strain routing.** Locations: `chaperone-orthogonal-stacking.md` §5.5 (predicts sub-0.6 synergy for secreted triple cassette) vs. `cordycepin-cassette-burden-computational.md` (shows cytosolic cns1+cns2 is GREEN) vs. `uricase-cassette-ranking-computational.md` (provides refined uricase cassette). Analysis: The chaperone framework’s triple-cassette discussion (§5.5) is scoped to secreted payloads — it evaluates DAF SCR1-4 (secreted, 8 disulfides) as the third cassette. The framework’s own scope note (line 238) explicitly states it does not track cytosolic burden. comp-023 fills that gap for cordycepin. The contradiction is not a factual error — it is a **scope boundary** that, when crossed, changes the platform recommendation. The triple-cassette strain is predicted to fail if the third cassette is secreted (DAF SCR1-4); it is predicted to succeed if the third cassette is cytosolic (cordycepin). This reframes the endgame strain design space: the third cassette slot should be reserved for a **cytosolic payload** (cordycepin, carnosine, or a future small-molecule pathway) rather than a secreted one. DAF SCR1-4 remains on a separate strain or the LBP chassis. This is a design rule that none of the individual pages states explicitly.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the strongest design-rule extraction in the batch. `chaperone-orthogonal-stacking.md` §5.5 pessimism is explicitly about uricase + lactoferrin + secreted DAF SCR1-4, while the same page’s scope note says cytosolic burden is outside the ER-folding framework and `cordycepin-cassette-burden-computational.md` closes that axis for cns1+cns2 with a GREEN verdict. The practical implication is real: reserve the third same-strain slot for cytosolic payloads and keep DAF SCR1-4 on a separate strain or peer chassis unless wet-lab data overturn the current PDI-load model.
