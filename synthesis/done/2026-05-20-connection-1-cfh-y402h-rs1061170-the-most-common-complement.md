---
type: connection
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 1
global_index: 1
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# CFH Y402H (rs1061170), the most common complement-dysregulation variant, may interact with dietary upstream‑CP0 candidates (rosmarinic acid, luteolin, Houttuynia cordata polysaccharides) to produce a genotype‑×‑diet interaction on gout flare severity — analogous to the Q141K‑×‑butyrate model already developed for ABCG2.

1. **CFH Y402H (rs1061170), the most common complement-dysregulation variant, may interact with dietary upstream‑CP0 candidates (rosmarinic acid, luteolin, Houttuynia cordata polysaccharides) to produce a genotype‑×‑diet interaction on gout flare severity — analogous to the Q141K‑×‑butyrate model already developed for ABCG2.**  
   *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `gout-genetic-variants.md` (new CFH Y402H table row + counter‑evidence flag), `complement-c5a-gout.md` (upstream‑CP0 dietary candidates, combined‑coverage hypothesis), `upstream-complement-modulator-sweep-computational.md` (comp‑018 Phase 2 Houttuynia cordata), `upstream-complement-verification-rerun-computational.md` (comp‑020 rosmarinic acid / luteolin / Helicteres ranking).  
   - *Page‑pair linkage:* These pages are **weakly paired**. `complement-c5a-gout.md` names CFH Y402H briefly (§6.3) but never connects it to the dietary‑CP0 thread; `gout-genetic-variants.md` mentions the dietary‑CP0 candidates only in the CFH entry itself and does not cross‑link the complement‑mechanism pages. No existing page models the Y402H‑×‑diet interaction.  
   - *Why It Matters:* If CFH Y402H carriers have exaggerated complement‑priming on MSU crystals, then the dietary C3‑convertase inhibitors already identified by comp‑018/020 could provide a **genotype‑targeted, food‑grade CP0 layer** for ~30–40% of Europeans and Africans — a precision‑prevention lever that would parallel the butyrate‑Q141K thesis and require only dietary adherence, not a new drug. The AMD precedent points in the opposite direction (zinc/antioxidant supplementation *worsens* outcomes in CFH high‑risk carriers), which makes the predicted direction uncertain but also surfaces a testable mechanistic‑dissociation hypothesis: the OE dietary candidates act *upstream* of CFH, so the AMD paradox may not transfer.  
   - *Suggested Action:* The cheapest de‑risker is the **UK Biobank cross‑tabulation** already scoped in `gout-genetic-variants.md` (§Category 5 CFH row): `rs1061170` × dietary polyphenol intake × incident gout, feasible via collaboration with existing UKB gout‑GWAS groups (Merriman/Otago, Major‑Wrigley/Auckland, Choi/MGH). This is a $0, ~3‑month collaboration proposal, not a solo OE application. In parallel, flag the falsifiable prediction in `self-experiment-protocol.md` §4: if SFH DHA‑loaded subjects show faster serum C5a decline during flare resolution than DHA‑deficient subjects, that pattern should be steeper in CFH 402 HH carriers (testable as a within‑subject add‑on to the existing flare‑tracking protocol).

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The CFH Y402H × dietary-CP0 interaction is speculative but chokepoint-correct: `gout-genetic-variants.md` already flags CFH Y402H, the AMD supplementation paradox, and the UKB/AoU mining path, while `upstream-complement-modulator-sweep-computational.md` documents rosmarinic acid, luteolin, and Houttuynia as upstream complement candidates. The synthesis adds a useful genotype-stratified CP0 intervention frame and correctly keeps the AMD result as counter-evidence rather than dismissing it. The self-experiment C5a-decline add-on also fits the existing `self-experiment-protocol.md` C5a slope / omega-3-index readout, though it should remain explicitly hypothesis-generating.

---

## ✓ Actioned 2026-05-21 (via comp-039 + canonical propagation)

The Connection 1 thesis — CFH Y402H × dietary upstream-CP0 candidates producing a genotype × diet interaction — has been **converted from hand-wavy plausibility to per-candidate mechanism-grounded classification** via [comp-039](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md) (2026-05-21). All four upstream-CP0 candidates (rosmarinic acid, luteolin, HCP/HCPM/CHCP, Helicteres) classified **CFH-independent** with primary-source binding-site justification. Two-model agreement on classification; preserved disagreement on prediction direction (Model A negative / Model B null) → UKB cross-tab pre-specifies both.

Canonical propagation completed in this walk:
- [`gout-genetic-variants.md`](../../wiki/gout-genetic-variants.md) Category 5 CFH Y402H row extended with comp-039 per-candidate classifications, lead UKB cross-tab spec (rosmarinic acid × rs1061170), HCP deferral to East Asian cohorts (comp-041 queued), wet-lab definitive test (comp-040 queued).
- [`complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §6.3 two new paragraphs: comp-039 per-candidate classification with primary-source evidence (Sahu 1999 C3b thioester / Zhang 2008 matched CP+AP / Lu 2018 C3+C4 / Yin 2016 CP>AP), candidate-stratified UKB ask with operational deferrals and confound considerations.

The self-experiment C5a-decline-slope add-on Pass 2 suggested for `self-experiment-protocol.md` §4 is **already covered** by [`spm-resolution-pathway.md` §7.3](../../wiki/spm-resolution-pathway.md) and the new [`self-experiment-protocol.md` §13](../../wiki/self-experiment-protocol.md) Protocol C n=1 sub-experiment (landed earlier this walk in commit `fb9780b` for Cluster 3). Pass 2's CFH-402-HH stratification add-on stays as a hypothesis-generating layer on the existing biomarker-tracking framework — no separate edit needed.

Pairs with [Item 7 closure](./2026-05-20-contradiction-1-cfh-y402h-dietary-supplementation-the-predicted-beneficial.md) (AMD-paradox contradiction → both models reject), [Item 8 closure](./2026-05-20-experiment-1-cfh-y402h-dietary-polyphenol-intake-incident-gout-uk.md) (UKB cross-tab → comp-039 per-candidate spec), [Item 13 closure](./2026-05-20-priority-action-2-add-the-cfhdietarycp0-biobankmining-proposal-to-gout-action.md) (surface routing → kept off `gout-action-guide.md` per Pass 3).
