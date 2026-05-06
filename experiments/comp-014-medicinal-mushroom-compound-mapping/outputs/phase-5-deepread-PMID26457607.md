# Phase 5 Deep-Read: Cordyceps Cochrane Review (PMID 26457607)

**Citation:** Hong T, Zhang M, Fan J. *Cordyceps sinensis* (a traditional Chinese medicine) for kidney transplant recipients. *Cochrane Database Syst Rev.* 2015 Oct 12;2015(10):CD009698. [DOI:10.1002/14651858.CD009698.pub2](https://doi.org/10.1002/14651858.CD009698.pub2). PMID: 26457607. PMCID: [PMC9446485](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446485/).

**Source attribution:** According to PubMed (full-text via PMC9446485). Cited via Paperclip-equivalent PMC URL above; this paper is not in Paperclip's `/papers/` index (Cochrane reviews mirror to PMC under restricted licence; full-text retrieval via `mcp__plugin_pubmed_PubMed__get_full_text_article` returned empty `full_text`, so extraction was performed against the PMC HTML mirror via WebFetch).

**Phase 5 reader:** Claude (Opus 4.7), 2026-05-06.

---

## Executive verdict (TL;DR)

The PubMed Phase-4 hit promising "Cochrane systematic review with SUA reduction in CKD/hyperuricemia" was **partially correct in structure and substantively misleading in scope**. This is NOT a CKD/hyperuricemia review. It is a **kidney-transplant-recipient adjuvant-immunosuppression** review. SUA appears as a secondary biochemical endpoint in **one of the five RCTs** (Ding 2011, n=109 in the SUA analysis subset), not as a meta-analytic pooled outcome. Hyperuricemia is not the indication. The "highest evidence-tier finding" framing in Phase 4 needs to be **downgraded substantially** — Cochrane methodology does not redeem a single-study endpoint within a transplant-immunosuppression review.

The defensible Phase-6 carry-forward is narrower than the breadth pass implied: Cordyceps may lower SUA in kidney transplant recipients on cyclosporin A as a secondary effect of CNI dose-sparing, with **one Chinese RCT (Ding 2011, MD −84.19 µmol/L; 95% CI −117.86 to −50.52)** as the primary evidence and unclear risk of bias.

---

## Q1. Cochrane scope (indication + outcomes)

**Indication:** Adjuvant immunosuppressive treatment for **kidney transplant recipients** (post-transplant maintenance), NOT chronic kidney disease, hyperuricemia, or gout. The review's framing motivation is calcineurin-inhibitor (CNI) toxicity reduction — cyclosporin A (CsA) and tacrolimus cause long-term renal, hepatic, and metabolic damage; Cordyceps is positioned in Chinese clinical practice as a CNI-sparing adjuvant.

**Comparisons evaluated:**
1. Cordyceps vs azathioprine (AZA) — 4 studies, 265 participants
2. Cordyceps + low-dose CsA vs standard-dose CsA — 1 study (Ding 2011), 182 participants

**Primary outcomes:** Patient survival, graft survival, acute rejection episodes.

**Secondary outcomes (where SUA lives):** Anaemia (haemoglobin), leucopenia (white cell count), liver function (ALT/AST), serum albumin, **serum uric acid**, infection incidence, CNI nephrotoxicity, hepatotoxicity. SUA is one of ~10 biochemical endpoints, reported only in the Cordyceps + low-dose CsA arm (Ding 2011).

**Implication for comp-014:** The hyperuricemia signal is a side-effect of the CNI dose-sparing logic — lower CsA dose → less CsA-induced hyperuricemia. This is **mechanistically distinct** from a direct urate-axis pharmacology (XO inhibition, URAT1 blockade, etc.) and the Phase-6 thesis cannot use this RCT as evidence for a primary urate-lowering mechanism without additional support.

---

## Q2. The 5 included RCTs

All five RCTs are from China and published in Chinese-language venues (per the review's note that 131 of 156 search records came from Chinese-language databases).

| # | Trial | Year | Country | n (T/C) | Cordyceps preparation | Comparator |
|---|---|---|---|---|---|---|
| 1 | Yu | 1991 | China | 34 (17/17) | Cultivated *C. sinensis* "Q80" (powder) | AZA |
| 2 | Sun | 2004 | China | 121 (57/64) | Bailing capsule | AZA |
| 3 | Wang | 2005 | China | 42 (21/21) | Bailing capsule | AZA |
| 4 | Wang | 2005a | China | 68 (36/32) | Bailing capsule (dose not reported) | AZA |
| 5 | Ding | 2011 | China | 182 (83/99) | Bailing capsule | Cordyceps + low-dose CsA vs standard-dose CsA |

**Total: 447 participants across 5 RCTs (6 reports — one trial had two associated publications).**

**CNKI accessibility (Phase 5b feasibility):** All five trials are Chinese-language and were located via Chinese-language databases per the Cochrane search methods section. CNKI (China National Knowledge Infrastructure) is the canonical home for these. WanFang and SinoMed are secondary mirrors. None of the five appear to be PMC-deposited (Cochrane sourced them through database search, not PMC). Phase-5b primary-source verification will require direct CNKI access — the multilingual ingestion discipline (umbrella CLAUDE.md, global-multilingual-research rule) is load-bearing here. Specifically: Ding 2011 is the only RCT that matters for the SUA claim, so prioritise that for primary-source retrieval.

**Author/title leads for CNKI search (best inferences from the Cochrane-disambiguated cites — verify against CNKI catalogue before treating as canonical):**
- Yu 1991 — likely Chinese Journal of Organ Transplantation or similar early-1990s Chinese transplant journal
- Sun 2004 — Bailing capsule + transplant maintenance, n=121
- Wang 2005 / Wang 2005a — likely two reports of related cohorts
- Ding 2011 — Bailing capsule + low-dose CsA, n=182, the SUA-reporting trial

---

## Q3. Cordyceps preparation — disaggregation

**No disaggregation by preparation type.** The review pools across preparations.

Preparation breakdown:
- **Bailing capsule (Hirsutella sinensis fermented mycelium, brand-name product)** — 4 of 5 studies (Sun 2004, Wang 2005, Wang 2005a, Ding 2011). The dominant preparation in the evidence base.
- **Cultivated *C. sinensis* "Q80" (powder)** — 1 study (Yu 1991). Older, lower-dose preparation.
- **Wild *Ophiocordyceps sinensis*** — NOT used in any included RCT.
- **Cultivated *Cordyceps militaris*** — NOT used in any included RCT.
- **Other branded products (Jinshuibao, Corbrin)** — NOT used in any included RCT.

**Implication:** The Cochrane evidence base is, in practice, **a Bailing-capsule (Hirsutella sinensis CS-4 fermented mycelium) evidence base** — not "Cordyceps" generically. This narrows the Phase-6 carry-forward considerably. Conclusions about wild *O. sinensis* (the rare, expensive caterpillar-fungus complex) cannot be inferred from this review. Likewise *C. militaris* (the common cultivated cordycepin-producer) is not represented. Bailing's active fraction is from a *Hirsutella sinensis* anamorph fermentation, which has a different secondary-metabolite profile than wild *O. sinensis* (notably lower cordycepin, higher polysaccharide content; see [Pu et al. 2024 PMC10776043](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10776043/) for FOSM characterisation).

---

## Q4. SUA / urate-axis numerical data

**Pooled meta-analysis: NONE.** SUA is reported in **one trial only** (Ding 2011).

**Ding 2011 SUA result:**
> "MD −84.19 µmol/L; 95% CI −117.86 to −50.52" (n=109 in the SUA analysis subset, after excluding patients who died, lost graft function, or developed nephrotoxicity)

**Conversion to mg/dL (for comp-014 cross-comparison):** −84.19 µmol/L ÷ 59.48 = **−1.42 mg/dL** SUA reduction (95% CI roughly −1.98 to −0.85 mg/dL). For context, allopurinol typically achieves ~−2 to −3 mg/dL in hyperuricemic patients; febuxostat ~−3 to −4 mg/dL. The Cordyceps + low-dose CsA arm shows a clinically meaningful but modest signal — and it is **confounded by the CsA dose reduction itself** (CsA causes hyperuricemia in ~50% of transplant recipients via reduced renal urate excretion; lowering the CsA dose lowers SUA independently of any Cordyceps effect).

**Heterogeneity (I²):** Not applicable — single study, no pooling possible.

**Confounding caveat (the load-bearing one):** The Cochrane authors flag that "recipients who had died or experienced allograft function loss and nephrotoxicity were excluded from the analyses." This is a per-protocol-style analysis on a high-event-rate population, which biases toward the treatment-favouring direction.

---

## Q5. Risk of bias

All 5 studies rated as **unclear risk of bias overall** by Cochrane criteria. Specific domain assessments:

| Domain | Yu 1991 | Sun 2004 | Wang 2005 | Wang 2005a | Ding 2011 |
|---|---|---|---|---|---|
| Random sequence generation | Unclear | Unclear | Unclear | Unclear | **Low** (random number table) |
| Allocation concealment | Unclear | Unclear | Unclear | Unclear | Unclear |
| Blinding (performance) | Unclear / not reported | Not reported | Not reported | Not reported | Not reported |
| Blinding (detection) | Low (objective endpoints) | Low | Low | Low | Low |
| Incomplete outcome data | Low | Low | Low | Low | Low |
| Selective reporting | Unclear | Unclear | Unclear | Unclear | Unclear |

**Cochrane authors' aggregate judgement:** "Limited reporting of study methods and data meant that all included studies were assessed as having unclear risks of bias." Combined with small study sizes, short follow-up (3 months to 1 year), and selective participant exclusion in the analyses, the authors explicitly warn: "All results should be interpreted with caution: we identified limitations relating to the quality, number, size, duration, and nature of included studies."

No study is flagged as low-quality outright; all are flagged as **unclear / insufficiently reported**. This is the structural problem Cochrane reviews of older Chinese-language RCTs frequently encounter — the underlying trials were conducted to clinical-practice norms of their era and venue, not to modern CONSORT reporting standards.

---

## Q6. Cochrane verdict — authors' conclusions

**Verbatim:**
> "Although there were some favourable aspects associated with Cordyceps, longer‐term studies are needed to clarify any benefit‐harm trade‐off. Future studies should investigate the use of Cordyceps in combination with other immunosuppressive agents such as tacrolimus, mycophenolate mofetil or induction therapy. Such studies also need to be appropriately sized and powered."

**Plain-language framing:** "Reporting and study designs were significantly flawed and may have overestimated benefits and underestimated harms."

**Specific verdict on the Cordyceps + low-dose CsA arm (where SUA lives):** "There was limited low quality evidence to suggest benefits in pulmonary infection, serum albumin, serum uric acid levels, CNI nephrotoxicity and hepatotoxicity."

**Verdict in evidence-tier language:** Cochrane = **insufficient evidence to recommend for clinical use**, with a tilt toward "favourable trends, longer trials needed." This is a **negative-by-default Cochrane verdict**, not a positive endorsement.

---

## Q7. Mechanism — addressed?

**Mostly outcome-based; mechanism barely touched.**

Direct quote on mechanism (one paragraph in the discussion):
> "Studies on the mechanisms of action of Cordyceps for kidney transplant recipients have suggested that its therapeutic effects may be related to its bidirectional immunomodulating activity, antioxidant activity, and anti‐inflammatory properties. Cordyceps may protect grafted kidneys by ameliorating renal tubular impairment and reducing renal interstitial fibrosis."

**Specific urate-axis mechanisms mentioned:** NONE. No discussion of:
- Xanthine oxidase (XO) inhibition
- URAT1 / GLUT9 / OAT urate transporter modulation
- ADA (adenosine deaminase) — relevant given Cordyceps' nucleoside content
- NLRP3 inflammasome
- Renal tubular urate handling

The review treats the SUA reduction as a downstream consequence of CsA dose sparing + general renal protection, NOT as evidence of a mechanism-specific urate effect. **This is the mechanistic weakness that Phase 6 must address head-on:** the Cochrane evidence does not establish a mechanism for Cordyceps urate lowering, and the most parsimonious explanation (CsA dose-sparing → less CsA-induced hyperuricemia) does not require Cordyceps to have any urate-axis pharmacology of its own.

---

## Implications for comp-014 Phase 6 triage

1. **Downgrade the Cordyceps urate-axis claim by one tier.** The Phase 4 ranking treated this Cochrane review as Tier-1 evidence (Cochrane methodology = highest evidence tier). It is structurally Tier-1 for the *transplant-immunosuppression* indication, but only **Tier-3 (single small RCT, unclear risk of bias, confounded by co-intervention)** for the urate-axis indication. The "highest evidence-tier finding" framing in Phase 4 was an over-read of the breadth-pass PubMed metadata.

2. **The Bailing-capsule-specific evidence base is the actionable carry-forward, not "Cordyceps" generically.** If comp-014 advances any Cordyceps lead to compound-mapping or wet-lab consideration, it should be Bailing capsule (Hirsutella sinensis CS-4 fermented mycelium) — that's where the human RCT evidence sits. Wild *O. sinensis* and *C. militaris* should be triaged on independent evidence streams.

3. **Mechanism work is required.** The Cochrane review provides clinical-outcome evidence (weak, confounded) but no mechanistic anchor in the urate axis. Before any Phase 6 wet-lab consideration, comp-014 needs to either: (a) find primary mechanism literature (XO inhibition assays, urate transporter assays, NLRP3 work) for Bailing capsule or its characterised fractions, or (b) treat the urate-lowering signal as an indirect / non-mechanism-grounded clinical observation and flag it accordingly.

4. **Phase 5b feasibility (Ding 2011 primary-source):** Worth attempting. CNKI access via the multilingual-ingestion protocol — translate-twice (Claude + DeepSeek per umbrella translation protocol), surface disagreements on the SUA numerics. Specific load-bearing items to verify: (a) the −84.19 µmol/L MD against the original Chinese paper (Cochrane data extraction errors are non-zero), (b) the n=109 subset rationale (which patients excluded, why), (c) whether the Chinese paper reports any mechanism work or only outcomes.

5. **Phase 5b feasibility (other 4 RCTs):** Lower priority. None of them report SUA. They are evidence for the immunosuppression-adjuvant indication, not the urate-axis indication. Skip unless comp-014 expands scope to immunomodulation.

6. **Cross-reference to related reviews:** Two Phase 5/6-relevant adjacent reviews surfaced in the Paperclip search and may strengthen the picture:
   - Wu et al. 2025 (PMC11747039) — Cordyceps for renal dysfunction broader meta-analysis. Includes creatinine, urine output. Worth reading next.
   - Pu et al. 2024 (PMC10776043) — Fermented *O. sinensis* mycelium for contrast-associated AKI prevention. Bailing/Jinshuibao characterised. Relevant to nailing down what the Bailing preparation actually contains.
   - Tan et al. 2022 (PMC9304961) — Cordyceps for renal fibrosis mechanism review. Mechanism literature, not RCT data.

---

## Translation/multilingual notes

This Cochrane review is English-authored (Hong et al. are at Sixth People's Hospital of Chengdu). The underlying RCTs are Chinese-language. The Cochrane data extraction is the only English-language synthesis publicly available; primary-source verification per the umbrella's two-model translation protocol (`Open Enzyme/CLAUDE.md` §"Translation protocol") is needed for any load-bearing Phase-6 numerical claim. Specifically, the −84.19 µmol/L MD has passed through one translation step (Chinese RCT → Cochrane extraction) and should be verified against the original Ding 2011 paper before propagating to wiki content.

---

## Provenance

- Metadata via `mcp__plugin_pubmed_PubMed__get_article_metadata` (PMID 26457607)
- Full-text extraction via `WebFetch` against [PMC9446485](https://pmc.ncbi.nlm.nih.gov/articles/PMC9446485/) (Cochrane PMC mirror — `mcp__plugin_pubmed_PubMed__get_full_text_article` returned empty `full_text` field, common for Cochrane PMC entries due to licence restrictions)
- Adjacent-review discovery via `mcp__paperclip__paperclip search "Cordyceps sinensis chronic kidney disease Cochrane" -n 10`
- DOI: [10.1002/14651858.CD009698.pub2](https://doi.org/10.1002/14651858.CD009698.pub2)
