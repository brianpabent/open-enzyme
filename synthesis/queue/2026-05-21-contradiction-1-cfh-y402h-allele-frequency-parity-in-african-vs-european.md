---
type: contradiction
sweep_date: 2026-05-21
sweep_sha: 3edb643
section_index: 1
global_index: 5
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# CFH Y402H allele frequency parity in African vs. European populations (gout-genetic-variants.md Category 5) directly contradicts the UK Biobank-centric cross-tab strategy of comp-039 — but the contradiction is productively resolvable through All of Us.

1. **CFH Y402H allele frequency parity in African vs. European populations (gout-genetic-variants.md Category 5) directly contradicts the UK Biobank-centric cross-tab strategy of comp-039 — but the contradiction is productively resolvable through All of Us.** `[CHAIN-DEPTH: 1]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `gout-genetic-variants.md` Category 5 CFH row, `cfh-mechanism-dissociation-cp0-candidates-computational.md` §5
   - *Page-pair linkage:* **Both are trigger files in this sweep** — the CFH row was refined with an explicit correction ("~35–37% in Africans, parity with European, not lower") and comp-039's UKB cross-tab specification was written assuming European-ancestry-skewed UKB as the primary dataset. The correction and the cross-tab specification were written in the same sweep but were not reconciled against each other.
   - *Analysis:* comp-039 §5 specifies the UK Biobank as the lead collaboration channel for CFH × rosmarinic-acid × incident-gout cross-tab, with East Asian cohorts deferred for Houttuynia (where the exposure is captured). But the CFH Y402H variant has substantial frequency in African-ancestry populations (~35–37%) — comparable to European (~36–39%). The UK Biobank's African-ancestry representation is thin relative to European. A UKB-only CFH cross-tab would therefore capture the European signal adequately but under-power the African-ancestry signal, missing the population where (a) CFH 402H frequency is high AND (b) the AMD-paradox literature shows population-specific effect-direction differences (Volcik 2008 ARIC: CFH 402H × hypertension interaction significant in whites, null in African Americans). **The UKB-centric strategy is powered for the wrong population on this question.** The correction: the All of Us Researcher Workbench (noted in comp-039's biobank-mining prior as a "parallel direction-check with better African-American representation, ~2–4 weeks free") should be elevated from secondary to **co-primary** with UKB, not treated as a parallel confirmation. Two independent cross-tabs in two populations with comparable CFH 402H frequency but different genetic backgrounds and dietary patterns would produce the most informative answer. This is not a contradiction that kills the strategy; it's a contradiction that sharpens it.
   - *Suggested Action:* Update `cfh-mechanism-dissociation-cp0-candidates-computational.md` §5 to specify All of Us as co-primary with UKB for the rosmarinic-acid cross-tab, with explicit rationale: (a) CFH 402H allele frequency parity (~35–39% European vs. ~35–37% African), (b) UKB under-represents African-ancestry populations, (c) Volcik 2008 population-specific effect-direction differences make single-population cross-tab uninformative for the broader question. The existing UKB-specific specification (rosmarinic acid × Apiaceae) stays; the AoU specification is added as a parallel arm with explicit rationale.

   

---

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: science-gap]` The suggested AoU elevation is directionally right, but the “UKB is powered for the wrong population” phrasing overstates the contradiction: UK Biobank remains well-powered for the European-ancestry CFH 402H signal, while the problem is that African-ancestry parity in CFH frequency plus Volcik 2008 effect-direction heterogeneity make a UKB-only result insufficient for generalization. `gout-genetic-variants.md` and `complement-c5a-gout.md` both document African frequency parity (~35–37%) and Volcik’s white-vs-African-American difference, and the 2026-05-19 biobank report identifies AoU as a lower-friction cohort with better African-American representation. The action should be “AoU co-primary for cross-ancestry direction-check,” not “UKB is the wrong population.”
