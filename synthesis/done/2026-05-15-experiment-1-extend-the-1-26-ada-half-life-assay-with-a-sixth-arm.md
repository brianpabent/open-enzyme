---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 5
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Extend the §1.26 ADA half-life assay with a sixth arm: engineered-koji cordycepin extract (when available) + GLPP, testing whether the koji-produced cordycepin + mushroom-derived GLPP combination achieves ADA dual inhibition comparable to whole-fermentate Cordyceps.

1. **Extend the §1.26 ADA half-life assay with a sixth arm: engineered-koji cordycepin extract (when available) + GLPP, testing whether the koji-produced cordycepin + mushroom-derived GLPP combination achieves ADA dual inhibition comparable to whole-fermentate Cordyceps.** *Cost: $500–1,000 adder to §1.26. Time: same as §1.26. Decides: whether the cross-track ADA synergy is real or whether the koji route’s lack of native pentostatin makes it dependent on GLPP supplementation.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Rationale:* comp-023 green-lit the koji cordycepin route on metabolic-burden grounds, but koji lacks the native pentostatin that *C. militaris* co-produces. GLPP is the most accessible orthogonal ADA inhibitor. If koji cordycepin + GLPP matches whole-fermentate Cordyceps in the ADA half-life assay, the koji track gains a viable cordycepin delivery route independent of mushroom cultivation. If it underperforms, the koji cordycepin route needs pentostatin co-engineering or remains dependent on GLPP co-administration.
   - *Dependencies:* Engineered-koji cordycepin strain (gated on §1.9 extended design + comp-025/026 follow-ups). Can be deferred until the strain exists; the protocol addition costs nothing to document now.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The proposed sixth arm is a valid extension of `validation-experiments.md` §1.26, which currently specifies a five-arm ADA half-life assay centered on cordycepin, pentostatin, GLPP, whole-fermentate *Cordyceps*, and whole-fermentate *Cordyceps* + GLPP. `medicinal-mushroom-complement-track.md` already names engineered koji cns1+cns2 + GLPP as the koji-track equivalent of the synergy pair and notes that the koji route lacks natural pentostatin unless the whole BGC is engineered. Adding an engineered-koji cordycepin extract + GLPP arm is therefore technically coherent, but it should remain gated on the existence of the engineered cordycepin strain and comp-025's ADA-competition result.

---

## ✓ Actioned 2026-05-15

Pass 3 confirmed; carry-forward from Item 24 (2026-05-15 Connection 1) now landed.

**File shipped:**

- **`wiki/validation-experiments.md` §1.26 Sixth-arm extension (new subsection)** — engineered-koji cordycepin + GLPP arm spec. Identical protocol to base §1.26 (ADA challenge + LC-MS) with engineered-koji cordycepin extract co-administered with Tier 3-anchored GLPP. Hard gating on: (a) engineered cordycepin strain availability, (b) comp-025 ADA-competition GREEN, (c) comp-028 three-axis GREEN. GREEN/YELLOW/RED decision rule with concrete numeric thresholds (≥70% / 50-70% / <50% of Arm 4 whole-fermentate baseline). Distinction from §2.7 (Item 19's koji × whole-fermentate stability test) explicitly named: §2.7 tests koji + native-pentostatin pairing for co-formulation stability; §1.26 sixth arm tests koji + GLPP pairing for ADA dual-inhibition. The two together inform which co-product is the preferred deliverable for the engineered koji track.

**No new comp-NNN.** The sixth arm is a downstream wet-lab experiment gated on multiple existing comp-NNNs (comp-025, comp-028) returning GREEN before it can run.

**Cost framing preserved:** $500-1,000 adder (one cordycepin-extract prep + 18 additional LC-MS samples + shared GLPP reagent). Same wall-clock time as §1.26 base — sixth arm runs in parallel with Arms 1-5 once the strain exists.

Pass 3 verdict honored. Closing.
