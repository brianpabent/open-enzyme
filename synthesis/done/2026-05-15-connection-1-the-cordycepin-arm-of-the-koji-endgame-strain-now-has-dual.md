---
type: connection
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 1
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# The cordycepin arm of the koji endgame strain now has dual-axis feasibility validation — metabolic-burden (comp-023 FBA GREEN) and chaperone-load (PDI = 0) — enabling a cross-track ADA dual-inhibition synergy with the medicinal-mushroom-complement track.

1. **The cordycepin arm of the koji endgame strain now has dual-axis feasibility validation — metabolic-burden (comp-023 FBA GREEN) and chaperone-load (PDI = 0) — enabling a cross-track ADA dual-inhibition synergy with the medicinal-mushroom-complement track.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `cordycepin-cassette-burden-computational.md`, `chaperone-orthogonal-stacking.md`, `koji-endgame-strain.md`, `medicinal-mushroom-complement-track.md`, `medicinal-mushroom-extract-sops.md`, `validation-experiments.md`
   - *Page-pair linkage:* `cordycepin-cassette-burden-computational.md` is new (2026-05-14) and not yet cross-referenced from `medicinal-mushroom-complement-track.md` or `koji-endgame-strain.md`. The `chaperone-orthogonal-stacking.md` framework explicitly notes that the cns1+cns2 pathway is cytosolic (PDI load = 0) but does not yet cite comp-023’s FBA results.
   - *Why It Matters:* comp-023’s FBA on the iWV1314 model shows cns1+cns2 cordycepin biosynthesis consumes <1% of cellular carbon flux and leaves kojic acid + ergothioneine yields at 100% of dual-cassette baseline. This closes the proteome-burden gap that the chaperone-orthogonal-stacking framework had flagged as out-of-scope. With both metabolic-burden and chaperone-load axes confirmed green, the engineered-koji cordycepin route is now a credible alternative to *Cordyceps militaris* cultivation. This opens a **cross-track ADA dual-inhibition synergy**: koji produces cordycepin (the substrate), while the medicinal-mushroom-complement track provides GLPP polysaccharide-peptide (a mechanistically orthogonal ADA inhibitor). Together they can hit adenosine deaminase from two independent biochemical angles — competitive inhibition from pentostatin (natively co-produced in *C. militaris* but absent in koji) and polysaccharide-binding from GLPP. This synergy has not been named in any wiki page; the closest existing entry is the “Combined / synergy candidates” bullet in `medicinal-mushroom-complement-track.md`, which discusses whole-fermentate Cordyceps + GLPP but not engineered-koji cordycepin + GLPP.
   - *Suggested Action:* Add a note to `koji-endgame-strain.md` §1.9 that the cordycepin arm has cleared in silico pre-feasibility on both burden axes. In `medicinal-mushroom-complement-track.md`, add a “koji-engineered cordycepin + GLPP” synergy bullet as a third combined candidate. The existing §1.26 five-arm ADA half-life assay can be extended with a sixth arm (engineered-koji cordycepin extract + GLPP) once the koji cordycepin strain exists.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` The central novelty claim is wrong: `medicinal-mushroom-complement-track.md` already has a first-class “Engineered koji cordycepin (cns1+cns2) + GLPP supplement” synergy bullet, explicitly notes that koji lacks native pentostatin unless the whole BGC is engineered, and cites comp-023’s GREEN metabolic-burden result at 564 mg/L/d with ~1,000× breakpoint. The mechanism is also misstated: engineered koji cns1+cns2 + GLPP does **not** hit ADA via pentostatin unless pentostatin is separately co-engineered or supplied; pentostatin is native to whole-fermentate *C. militaris*, not to the minimal koji cns1+cns2 route. The dual-axis feasibility point is real because `chaperone-orthogonal-stacking.md` scores cns1+cns2 PDI load = 0 and `cordycepin-cassette-burden-computational.md` gives the FBA GREEN verdict, but the suggested cross-reference action has largely already landed.

---

## ✓ Actioned 2026-05-15

Pass 3's push-back was correct on both factual errors:
1. The synergy WAS already named (`medicinal-mushroom-complement-track.md` has had the "Engineered koji cordycepin + GLPP supplement" bullet; Item 19 in this walk added the further engineered-koji + whole-fermentate *Cordyceps* entry alongside it)
2. The mechanism — engineered koji cns1+cns2 alone doesn't deliver pentostatin — was Pass 2's overclaim; the actual ADA-protection routes for the engineered-koji cordycepin path are (a) co-formulation with whole-fermentate *Cordyceps* (Item 19's cross-chassis pairing) or (b) GLPP supplementation (pre-existing bullet) or (c) pentostatin co-engineering (high cassette-complexity).

**The dual-axis feasibility composition** is real and was the genuine new content:

**Files shipped:**

- **`wiki/koji-endgame-strain.md`** — new "Dual-axis feasibility of the §1.9-extended cordycepin arm (composition added 2026-05-15)" paragraph appended directly after the existing comp-023 cordycepin-arm callout. Explicitly names the two-axis composition: comp-023 FBA GREEN on metabolic axis + `chaperone-orthogonal-stacking.md` §5.6 PDI=0 on chaperone axis. Both axes pre-cleared in silico before any wet-lab commitment. Cross-links comp-028 as the formal three-axis gate (chaperone + FBA + comp-026 regulatory architecture, still pending). Concrete cost framing preserved: §1.9 design can incorporate cordycepin arm at ~$1,500–2,500 marginal cost once comp-028 returns GREEN.

**Carry-forward (still on this walk):**
- **§1.26 sixth-arm extension** — Pass 2 suggested extending the §1.26 five-arm ADA half-life assay with a sixth arm (engineered-koji cordycepin extract + GLPP). That suggestion is **Item 26 in this walk** (`2026-05-15-experiment-1-extend-the-1-26-ada-half-life-assay-with-a-sixth-arm.md`). Carry-forward annotated; will be addressed at Item 26's briefing.

**No new comp-NNN.** Pass 3 correctly noted the suggested cross-reference action had largely already landed; the dual-axis-feasibility callout is the one real new content piece.

Pass 3 verdict honored. Closing.
