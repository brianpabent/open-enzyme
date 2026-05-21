---
type: connection
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 6
global_index: 6
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The Houttuynia cordata polysaccharide (HCP/HCPM) represents the first dual‑CP0+CP1 dietary candidate in the corpus — a widely‑consumed Southeast Asian herb with complement‑inhibitory and NLRP3‑suppressive activity — yet its gout‑specific efficacy has not been tested in any MSU model, and the single‑preparation‑dependent activity (structure‑dependent directionality) creates a consumer‑product caveat that parallels the mushroom β‑glucan structure‑dependence already documented for Ganoderma lucidum.

6. **The Houttuynia cordata polysaccharide (HCP/HCPM) represents the first dual‑CP0+CP1 dietary candidate in the corpus — a widely‑consumed Southeast Asian herb with complement‑inhibitory and NLRP3‑suppressive activity — yet its gout‑specific efficacy has not been tested in any MSU model, and the single‑preparation‑dependent activity (structure‑dependent directionality) creates a consumer‑product caveat that parallels the mushroom β‑glucan structure‑dependence already documented for Ganoderma lucidum.**  
   *Speculative for gout; supported for mechanism.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `upstream-complement-modulator-sweep-computational.md` (comp‑018 Phase 2 Tier 1d), `complement-c5a-gout.md` §9.7 (fourth Tier 1 candidate), `nlrp3-exploit-map.md` §CP1 (new Houttuynia entry), `supplements-stack.md` (new Houttuynia catalog entry).  
   - *Page‑pair linkage:* All references to Houttuynia were added within the **same sweep cluster** (2026‑05‑19 traditional‑name re‑scan). The compound is new to the wiki and has not yet been connected to any downstream validation experiment, biomarker‑tracking protocol, or consumer‑product recommendation.  
   - *Why It Matters:* Houttuynia is the cleanest example of the **query‑framing discipline** that the platform now mandates: it would have been invisible to a “C3 convertase inhibitor” search but is caught by a “Houttuynia cordata anti‑complementary” query. Its dual‑chokepoint coverage (CP0 + CP1) via TLR4‑MD2 partial agonism + complement cascade blockade makes it a uniquely efficient single‑dietary‑agent candidate. However, the **structure‑dependent directionality** (purified 60 kDa HCP‑2 is pro‑inflammatory on naïve PBMCs; the anti‑inflammatory phenotype appears only in disease‑context inflammation) is the same consumer‑product pitfall that the mushroom‑track caveat already warns about — a generic “Houttuynia extract” capsule cannot be assumed equivalent to the Chen‑group HCPM preparation.  
   - *Suggested Action:* The cheapest discriminating experiment is an in‑vitro MSU‑stimulated THP‑1 macrophage assay: HCPM (19.1 kDa Fudan fraction) vs. crude HCP vs. commercial Houttuynia capsule extract, measuring IL‑1β and IL‑6 at dose‑response. Cost: ~$2,000–3,000 for a CRO macrophage assay. Add to `validation-experiments.md` as §1.30. Until this gate is cleared, treat Houttuynia as a “mechanism‑supported, gout‑untested” dietary candidate with an explicit structure‑dependent caveat, parallel to the mushroom β‑glucan structure‑dependence warning already in the corpus.

   

---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The Houttuynia finding is well supported by the inlined `upstream-complement-modulator-sweep-computational.md`: HCP/HCPM is listed as Tier 1d with CH50 79–318 µg/mL CP0 activity plus intestinal NLRP3 / tight-junction / TLR4-MD2 CP1 evidence, and the same entry flags the Cheng 2014 structure-dependent caveat. The proposed MSU-stimulated THP-1 fraction comparison is the right cheap discriminator because it tests both gout relevance and consumer-product equivalence. This hits CP0 and CP1 regardless of chassis; route to validation, not chassis filtering.

---

## ✓ Actioned 2026-05-21 (comp-039 confirms mechanism; THP-1 assay landed as validation-experiments.md §1.30)

[comp-039](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md) (2026-05-21) §3.3 classified HCP/HCPM/CHCP as **CFH-independent (High confidence)** based on Lu 2018 (PMC5925397) depletion-rescue mapping:
- C3-depleted serum rescue 9.29 ± 1.69% (HCP blocks at C3 cleavage)
- C4-depleted serum rescue 12.34 ± 1.39% (HCP blocks at C4 cleavage — and **CFH is AP-specific, does not regulate C4**, so C4 binding is mechanistically incompatible with CFH-dependence)
- C5-depleted serum rescue 44.54 ± 3.92% (partial C5 effect)

Plus TLR4-MD2 binding mode (Yu 2026 PMC12937656) entirely upstream of complement. Three orthogonal lines converge on CFH-independence. Two-model agreement; Model A explicitly highlights HCP's dual CP0 + CP1 chokepoint coverage as a reason for *amplified* benefit in Y402H carriers; Model B predicts null.

**MSU-stimulated THP-1 macrophage assay landed as [`validation-experiments.md` §1.30](../../wiki/validation-experiments.md)** in this walk — three-arm fraction comparison (HCPM 19.1 kDa Fudan / crude HCP / commercial capsule extract) at dose-response, primary endpoint IL-1β supernatant ELISA, secondary endpoints IL-6 + C3a/sC5b-9 + cell viability. Decision rules cover the four outcomes (HCPM works + commercial fails / all three equivalent / none work / crude HCP performs ≥ HCPM). Cost ~$2,000–3,000 CRO assay, 4–6 weeks.

**Consumer-product caveat preserved.** The Cheng 2014 (PMC7112369) structure-dependent directionality (purified 60 kDa HCP-2 pro-inflammatory on naïve PBMCs; anti-inflammatory phenotype only in disease-context inflammation) means a generic "Houttuynia extract" capsule cannot be assumed equivalent to the Chen Daofeng / Fudan group HCPM preparation. The §1.30 assay's three-arm design directly tests this consumer-product equivalence.

**Cross-tab actionability:** HCP cross-tab is **NOT UKB-actionable** (Houttuynia rare in UK dietary corpus). comp-041 queued for East Asian cohort feasibility (KoGES / CKB / Singapore Chinese Health Study) — the Houttuynia-tractable populations where exposure is captured.

Pairs with [Item 9 closure](./2026-05-20-experiment-2-msustimulated-thp1-macrophage-assay-of-houttuynia-cordata.md) (the assay itself) and [Item 15 closure](./2026-05-20-most-curious-thread-1-the-houttuynia-cordata-polysaccharide-is-the-most.md) (the "most curious thread" framing).
