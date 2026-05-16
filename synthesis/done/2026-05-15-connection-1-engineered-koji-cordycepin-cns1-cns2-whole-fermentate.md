---
type: connection
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 1
global_index: 1
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Engineered koji cordycepin (cns1+cns2) + whole-fermentate *Cordyceps militaris* extract as a minimal-complexity cross-chassis ADA-protection strategy.

1. **Engineered koji cordycepin (cns1+cns2) + whole-fermentate *Cordyceps militaris* extract as a minimal-complexity cross-chassis ADA-protection strategy.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* [`cordycepin-cassette-burden-computational.md`](./cordycepin-cassette-burden-computational.md), [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md), [`validation-experiments.md`](./validation-experiments.md)
   - *Page-pair linkage:* `cordycepin-cassette-burden-computational.md` and `medicinal-mushroom-complement-track.md` already cross-reference each other, but the specific cross-chassis combination (engineered-koji cordycepin + cultivated *C. militaris* pentostatin) is not named as a dedicated low-complexity co-formulation strategy anywhere in the corpus. The connection composes three independent findings: (1) comp-023's GREEN verdict on cns1+cns2 metabolic burden in koji, (2) Xia 2017's characterization of native pentostatin co-production in *C. militaris* as the natural ADA-inhibitor pairing, and (3) the chaperone framework's §5.6 finding that cytosolic third cassettes bypass the PDI/ERO1 bottleneck that gates secreted-only triple-cassette designs. Together they define a "grow koji for bulk cordycepin, spike in a small dose of cultivated *Cordyceps* extract for ADA protection" route that avoids pentostatin co-engineering entirely.
   - *Why It Matters:* The current koji-endgame-strain cordycepin arm is gated on three open follow-ups (comp-025 ADA competition, comp-023 v2 dynamic FBA, comp-026 induction interference) before any wet-lab commitment. This cross-chassis strategy sidesteps all three gates: the koji strain produces cordycepin (comp-023 GREEN), and the ADA inhibitor comes from a separate organism that already makes it natively. The koji strain's engineering complexity drops from "add pentostatin cassette or ADA knockout" to "add cns1+cns2 only," which is already demonstrated. The cultivated *Cordyceps* extract provides pentostatin at its native co-evolved ratio without requiring additional cassette engineering, ADA-knockout host construction, or kinetic modeling of substrate competition. The stability of the co-formulation (does pentostatin survive in dried koji matrix?) is an open question, but a low-cost Tier 2 ADA-challenge assay (~$1,500–3,000, 3–4 weeks) can resolve it before any genetic engineering commits. This is the lowest-friction path to a functional cordycepin product from the koji chassis, and it composes the medicinal-mushroom complement track with the engineered-koji track in a way the corpus hasn't yet named.
   - *Suggested Action:* Queue a `validation-experiments.md` §2.7 entry: co-formulation stability test of engineered-koji cordycepin fermentate + dried *C. militaris* extract under ADA challenge, with cordycepin half-life as the primary readout. If the cross-chassis pairing protects cordycepin from ADA deamination (≥50% of native whole-fermentate protection), promote this route above the full-BGC-engineering or ADA-knockout alternatives. Also queue a sixth arm on the existing §1.26 5-arm ADA half-life assay (per the proposed extension in `validation-experiments.md` §1.26) to test engineered-koji cordycepin + GLPP as an alternative ADA-protection route independent of *C. militaris* cultivation.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: science-gap]` The cross-chassis cordycepin + *C. militaris* pentostatin strategy is worth testing, but the claim that it “sidesteps all three gates” is wrong. External pentostatin can protect cordycepin from ADA after production, but it does not automatically resolve comp-025’s native *A. oryzae* ADA competition for the cns1 substrate pool or comp-026’s multi-cassette induction-interference question; those are explicitly queued follow-up gates in `computational-experiments.md` and `cordycepin-cassette-burden-computational.md`. Keep the co-formulation assay, but do not promote it as bypassing the production-side gates.

---

## ✓ Closed via strategic deprioritization 2026-05-16

**Walkthrough Item 7 — koji-cordycepin engineering deprioritized.** Operator strategic call: cordycepin is commercially available at $20–60/month with native pentostatin co-protection via cultivated *Cordyceps militaris* extract; koji-engineered cordycepin delivers no novel chokepoint coverage, has an open dose-vs-achievable-titer gap (comp-023 verified metabolic feasibility but never analyzed therapeutic-dose achievability in realistic home-fermentation conditions on a multi-cassette strain), and the "endgame strain = full coverage + simple" principle does not justify the engineering complexity for a payload available at the supplement shelf.

This Connection's cross-chassis "engineered-koji cordycepin + whole-fermentate *C. militaris* pentostatin" strategy was a *patch* for the ADA-degradation problem that only exists if you've committed to engineering bulk cordycepin in koji. With koji-cordycepin engineering off the active stack, the patch is moot — the cultivation route already delivers cordycepin + pentostatin together at the natural co-evolved ratio.

The proposed `validation-experiments.md` §2.7 (co-formulation stability test) and §1.26 sixth-arm extension (engineered-koji cordycepin + GLPP) are NOT being added to the wet-lab queue. (Pass 3 separately noted on Priority Action 1 that these may have been added in an earlier pass; if so, they should be removed or marked Deprioritized in the same edit pass — verifying as part of the §2.7 removal.)

Canonical artifacts of this strategic call:
- [`wiki/cordycepin-cassette-burden-computational.md`](../../wiki/cordycepin-cassette-burden-computational.md) — deprioritization note added; comp-023 GREEN verdict stands as methodology validation
- [`wiki/koji-endgame-strain.md` §3.5](../../wiki/koji-endgame-strain.md) — "Cordycepin third-cassette slot — evaluated and deprioritized" subsection
- [`wiki/medicinal-mushroom-complement-track.md`](../../wiki/medicinal-mushroom-complement-track.md) — affirmed canonical cordycepin route; ~~struck-through~~ the engineered-koji cordycepin synergy bullets
- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — comp-023 v2, comp-025, comp-026, comp-028 all marked Deprioritized

Cluster-closure: Items 7 (this), 13 (Experiment 1), 16 (Most Curious Thread), 17 (Open Question 2), 18 (Priority Action 1) all close together via the same strategic call. Pointer maintained in each.
