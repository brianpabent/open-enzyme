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

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the strongest design-rule extraction in the batch. `chaperone-orthogonal-stacking.md` §5.5 pessimism is explicitly about uricase + lactoferrin + secreted DAF SCR1-4, while the same page's scope note says cytosolic burden is outside the ER-folding framework and `cordycepin-cassette-burden-computational.md` closes that axis for cns1+cns2 with a GREEN verdict. The practical implication is real: reserve the third same-strain slot for cytosolic payloads and keep DAF SCR1-4 on a separate strain or peer chassis unless wet-lab data overturn the current PDI-load model.

---

## ✓ Actioned 2026-05-15

The design rule is structurally already covered by Item 16 (Connection 1) which shipped `chaperone-orthogonal-stacking.md` §5.6 "Design escape — cytosolic third cassette" with the "Generalization — cytosolic payloads as a strategic design lever" subsection. comp-028 (Triple-cassette endgame strain feasibility) is queued as the formal gate.

Item 20's incremental contribution is to **elevate the design rule from the chaperone framework page (where the mechanism lives) to the strain-design surface (where the rule applies).**

**Files shipped:**

- **`wiki/koji-endgame-strain.md` §3 (Gating Feasibility Test)** — new "Third-cassette slot design rule (added 2026-05-15)" callout added directly under the H01 hypothesis-card reference. States the rule explicitly: third slot reserved for cytosolic payloads; secreted DAF SCR1-4 routes to separate strain or LBP peer chassis. Cross-links chaperone framework §5.6 (mechanism), comp-028 (formal gate), and the generalization ("the practical stacking limit is the count of *secreted* cassettes, not total cassette count").

**Why a callout, not a full subsection:** the rule's mechanistic anchor + comp-028 gate live elsewhere; the strain-design surface just needs the rule to be discoverable from the place where designers actually compose strain architectures. Adding a full §3.X subsection would duplicate the chaperone-framework §5.6 material.

Pass 3's "Confirmed, prioritize" verdict honored: the design rule is now grep-able from the strain-design surface, not just the chaperone framework page. Closing.
