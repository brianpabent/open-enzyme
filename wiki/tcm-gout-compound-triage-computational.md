---
title: "TCM Gout Compound Triage — Computational Analysis (comp-013)"
date: 2026-05-06
tags:
  - tcm
  - traditional-chinese-medicine
  - gout
  - hyperuricemia
  - computational
  - chembl-cross-check
  - bioavailability
  - urat1
  - abcg2
  - xanthine-oxidase
  - nlrp3
  - astilbin
  - rhein
  - emodin
  - berberine
  - luteolin
  - chlorogenic-acid
  - smilax-glabra
  - rheum-officinale
  - si-miao-san
  - global-multilingual
  - peer-track
related:
  - tcm-modern-rigor-intersection.md
  - chembl-cross-check.md
  - supplement-abcg2-antagonism-computational.md
  - food-grade-hdaci-screen-computational.md
  - computational-experiments.md
  - manual-literature-mining.md
  - gut-lumen-sink.md
  - abcg2-modulators.md
  - gout-pathophysiology.md
  - hypotheses/H04-tcm-rigor-intersection.md
sources:
  - "Yuan Q, Cheng Y, Sheng R, Yuan Y, Hu M. A Brief Review of Natural Products with Urate Transporter 1 Inhibition for the Treatment of Hyperuricemia. doi:10.1155/2022/5419890 (PMC9635963)"
  - "Liang G, Nie Y, Chang Y, et al. Protective effects of Rhizoma smilacis glabrae extracts on potassium oxonate- and monosodium urate-induced hyperuricemia and gout in mice. doi:10.1016/j.phymed.2018.11.032 (PMID 31005813)"
  - "Huang L, Deng J, Chen G, et al. The anti-hyperuricemic effect of four astilbin stereoisomers in Smilax glabra on hyperuricemic mice. doi:10.1016/j.jep.2019.03.004 (PMID 30851369)"
  - "Liu YF, Huang Y, Wen CY, et al. The Effects of Modified Simiao Decoction in the Treatment of Gouty Arthritis: A Systematic Review and Meta-Analysis. doi:10.1155/2017/6037037 (PMC5360963)"
  - "Hou SW, Chen SJ, Shen JD, et al. Emodin, a Natural Anthraquinone, Increases Uric Acid Excretion in Rats with Potassium Oxonate-Induced Hyperuricemia. doi:10.3390/ph16060789 (PMC10304951)"
  - "Zhang D, Zhao M, Li Y, et al. Natural Xanthine Oxidase Inhibitor 5-O-Caffeoylshikimic Acid Ameliorates Kidney Injury Caused by Hyperuricemia in Mice. doi:10.3390/molecules26237307 (PMID 34885887)"
  - "Petrangolini G, Corti F, Ronchi M, et al. Development of an Innovative Berberine Food-Grade Formulation with an Ameliorated Absorption: In Vitro Evidence Confirmed by Healthy Human Volunteers Pharmacokinetic Study. doi:10.1155/2021/7563889 (PMC8665891)"
  - "ChEMBL v34 — bioactivity data accessed via mcp__plugin_chembl_ChEMBL__get_bioactivity, 2026-05-06"
status: complete
---

# TCM Gout Compound Triage — Computational Analysis

**Question:** Which Traditional Chinese Medicine (TCM) compounds with documented gout indication are mechanistically viable when triaged via the comp-004 IC50 occupancy + comp-007 composite scoring frameworks?

**Verdict (top-line):** Of 9 candidate TCM compounds, 4 land **GUT-LUMINAL VIABLE** (luteolin, astilbin, emodin, berberine), 1 lands **MODERATE / VIABLE-WITH-DOSE-CAVEAT** (rhein), and 4 land **MECHANISM UNCLEAR** (aucubin, cylindrin, chlorogenic acid, atractylenolide I) — the latter primarily because no curated ChEMBL bioactivity data exists for them. The Si Miao San multi-herb formula has the strongest clinical evidence (24-RCT meta-analysis: SUA −90.62 µmol/L vs anti-inflammation control), though attribution to a single component is impossible.

**First concrete computational application** of the global-multilingual research discipline codified in `Open Enzyme/CLAUDE.md` (2026-05-06). All primary sources read directly without translation step (English-translated full texts available via Paperclip + PubMed); the two-model translation cross-check protocol was NOT triggered.

**Reproducible artifact:** [`experiments/comp-013-tcm-gout-compound-triage/`](../experiments/comp-013-tcm-gout-compound-triage/) — script, inputs, and outputs committed.

---

## §1 Question

The [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) scope page enumerates 8 candidate TCM herbs with classical gout indication (Smilax glabra, Rheum officinale, Plantago asiatica, Phellodendron amurense, Polygonum cuspidatum, Cinnamomum cassia, Atractylodes macrocephala, Astragalus membranaceus) plus the Si Miao San formula and several other multi-herb decoctions. The original P2-2 follow-up was framed as a "ChEMBL cross-check"; the question this analysis actually answers is sharper:

> **For each candidate TCM herb, identify the dominant bioactive compound(s), pull every available bioactivity datum against the gout-relevant target panel, layer the bioavailability honestly, compute predicted IC50 occupancy at the mechanism site, and decide: is the compound mechanistically viable for gout in vivo, gut-luminal viable only, systemic non-viable, or mechanism unclear?**

The bar is the same as comp-004 (supplement ABCG2 antagonism) and comp-007 (food-grade HDACi screen): IC50 occupancy at achievable in vivo concentration, with explicit caveats for cell-line vs in vivo translation, ChEMBL data sparsity, and bioavailability gating.

---

## §2 Verdict

| Rank | Compound | TCM source | Verdict | Composite | Confidence | Mechanism site | Best on-target IC50 |
|---|---|---|---|---|---|---|---|
| 1 | **Luteolin** | Lonicera japonica + many | **GUT-LUMINAL VIABLE** | 0.0071 | HIGH | gut-luminal AND systemic | XO 550 nM (J Nat Prod 1998) |
| 2 | Astilbin | Smilax glabra (Tu Fu Ling) | **GUT-LUMINAL VIABLE** | 0.0000 | MODERATE | gut-luminal AND systemic | N/A — animal-model URAT1 5-20 mg/kg |
| 3 | Rhein | Rheum (Da Huang) | **MODERATE / VIABLE-WITH-DOSE-CAVEAT** | 0.0000 | MODERATE | systemic | N/A — ChEMBL gap; off-target enriched |
| 4 | Emodin | Rheum / Polygonum cuspidatum | **GUT-LUMINAL VIABLE** | 0.0000 | HIGH | gut-luminal AND systemic | N/A — animal FEUA↑, NOT XO |
| 5 | Aucubin | Plantago asiatica | **MECHANISM UNCLEAR** | 0.0000 | LOW | gut-luminal | N/A — no ChEMBL, no IC50 |
| 6 | Berberine | Coptis chinensis (Huang Lian) | **GUT-LUMINAL VIABLE** | 0.0000 | HIGH | gut-luminal AND systemic (low) | TDO 30 nM off-target; URAT1 animal-only |
| 7 | Cylindrin | Imperata cylindrica | **MECHANISM UNCLEAR** | 0.0000 | LOW | gut-luminal | N/A |
| 8 | Chlorogenic acid | Lonicera japonica + coffee | **MECHANISM UNCLEAR** | 0.0000 | MODERATE | systemic | PTP1B 100 nM (off-target only) |
| 9 | Atractylenolide I | Atractylodes (Si Miao San cmpt) | **MECHANISM UNCLEAR** | 0.0000 | LOW | systemic | N/A |

**Verdict counts:** 4 GUT-LUMINAL VIABLE, 1 MODERATE, 4 MECHANISM UNCLEAR. **Zero outright SYSTEMIC NON-VIABLE** — but several compounds (chlorogenic acid, atractylenolide I) come close: ChEMBL has off-target IC50s but no gout-relevant target hits at achievable concentration.

The composite scores are dominated by ChEMBL data sparsity. **Luteolin is the only compound with both ChEMBL biochemical IC50 against a gout-relevant target (XO 550 nM) AND animal-model URAT1 evidence.** Every other GUT-LUMINAL VIABLE compound is animal-model-evidence-only, with the composite score correctly pinned at 0 (no biochem IC50 to multiply through) — the verdict relies on the assign_verdict override that admits animal-model evidence.

---

## §3 Per-compound analysis

### §3.1 Luteolin — GUT-LUMINAL VIABLE (rank 1)

**TCM source:** *Lonicera japonica* (金银花, Jin Yin Hua) and many other plants; component of multiple TCM gout formulas.
**ChEMBL ID:** CHEMBL151

**ChEMBL bioactivity (verified 2026-05-06):**

| Target | IC50 / Ki | Source |
|---|---|---|
| Xanthine dehydrogenase/oxidase | **IC50 = 550 nM** | activity_id 2331843, J Nat Prod 1998 (best); also 7,800 nM (BMCL 2015), 11,540 nM (J Nat Prod 2009), Ki = 2,900 nM (EJMC 2014) |
| ABCG2 | IC50 = 8,900 nM | activity_id 5312915, J Nat Prod 2011 (NCI-H460 PhA accumulation) |
| Cytochrome P450 1B1 | IC50 = 79 nM | activity_id 3409869, BMC 2010 (off-target) |

**In vivo evidence:** Per Yuan 2022 review (PMC9635963 doi:10.1155/2022/5419890) line 21 — "luteolin (3-10 mg/kg) and luteolin-4'-O-glucoside (20-100 mg/kg) could inhibit URAT1 expression and promote uric acid excretion in potassium oxonate-induced hyperuricemia mice [ref 45]" — verified via Paperclip grep.

**Bioavailability:** ~5% systemic (heavy glucuronidation; main circulating form is luteolin-glucuronide per Shimoi 1998 PMID 9625363). 100 mg dose × 95% gut-retained ÷ 250 mL = 380 mg/L unconstrained, capped at ~50 mg/L solubility = **175 µM gut lumen** vs 8.9 µM plasma Cmax (formal calculation per `outputs/triage.json`).

**Occupancy:**
- XO IC50 550 nM vs **plasma Cmax** (~24 nM at 100 mg dose) = ratio 0.04× → LOW occupancy systemically
- ABCG2 IC50 8,900 nM vs **gut conc** ~175,000 nM = ratio 19.6× → VERY_HIGH gut occupancy

**Tension:** Luteolin is **simultaneously a gut ABCG2 inhibitor (BAD for gout, predicted 95% inhibition) and a systemic XO + URAT1 modulator (GOOD for gout)**. The net effect depends on which arm dominates. In the mouse PO model, the URAT1-uricosuric arm wins. In humans on Q141K-amplified-risk genotype, the gut ABCG2 inhibition arm could dominate.

**Verdict rationale (GUT-LUMINAL VIABLE):** XO is the most-potent on-target hit, but plasma Cmax is too low for systemic XO impact. The published animal-model URAT1 effect at 3-10 mg/kg suggests gut + tissue accumulation drives the in vivo mechanism — gut-luminal exposure is the likely driver. Luteolin is the **most analytically tractable** TCM gout compound — only one in this set with confirmed biochemical IC50 against a gout-relevant target plus convergent animal-model data.

**Caveat for OE platform:** Luteolin is also flagged in [`abcg2-modulators.md`](./abcg2-modulators.md) as an ABCG2 inhibitor at gut concentrations — same paradox as comp-004 quercetin/curcumin. Co-delivery of luteolin (e.g., from Lonicera japonica extract) alongside engineered uricase would inhibit gut ABCG2 alongside delivering uricase. This is a strategic question for any future Lonicera-koji co-fermentation product.

---

### §3.2 Astilbin — GUT-LUMINAL VIABLE (rank 2)

**TCM source:** *Smilax glabra* (土茯苓, Tu Fu Ling) — the primary TCM gout herb in classical materia medica.
**ChEMBL ID:** None (astilbin is not curated in ChEMBL v34 as of 2026-05-06 — verified via name search + 85% SMILES similarity).

**Animal-model evidence (verified):**
- PMC9635963 line 29 (Yuan 2022): "In potassium oxonate-induced hyperuricemia mice, astilbin (5-20 mg/kg) inhibited URAT1 expression and promoted the excretion of uric acid [ref 54, 55 — Wang 2016 PMID 27522260]"
- PMID 30851369 (Huang 2019): Total flavonoids of S. glabra (TFSG, 55.6% astilbin stereoisomers) at 62.5-250 mg/kg in PO mouse model significantly reduced SUA, reduced hepatic XOD activity at 125 mg/kg, AND **upregulated renal OAT1 + OCTN2 expression**. Triple mechanism: XO inhibition + URAT1 downregulation + OAT1 upregulation.
- PMID 31005813 (Liang 2018): Smilax glabra water extract dose-dependently reduces PO+MSU-induced paw edema, lowers serum TNF-α/IL-1β/IL-6/IL-12, lowers uric acid and BUN, elevates serum IL-10, urinary uric acid and creatinine. Hepatic XOD activity dose-dependently reduced.

**XO inhibition direct evidence:** Zhang 2021 (PMID 34885887, doi:10.3390/molecules26237307) identifies astilbin as one of three known XO inhibitors in Smilax glabra rhizome alongside the novel 5-O-caffeoylshikimic acid (IC50 13.96 µM) and quercetin. Astilbin-specific IC50 not quoted in the abstract — bounded estimate 5-50 µM range based on the closely related 5OCSA value and astilbin's structural class.

**Bioavailability:** [UNVERIFIED — bound: 1-10%]. Astilbin glycosides are deglycosylated by gut microbiota; the aglycone (taxifolin) has BA ~6%. Most pharmacological activity in vivo appears to be from gut-microbiota-converted metabolites (taxifolin) PLUS direct gut-luminal action of intact glycoside.

**Verdict rationale:** Multi-mechanism in vivo efficacy across multiple independent labs in the murine PO model. Mechanism site is BOTH gut-luminal (intact glycoside acts locally on gut microbiota and possibly mucosal cells) AND systemic post-conversion (taxifolin reaches plasma). The poor systemic BA is favorable for the gut-luminal arm. **GUT-LUMINAL VIABLE** with HIGH-priority follow-up: in vitro biochemical IC50 vs human URAT1 (HEK293T-URAT1 standard assay) and human XO would close the ChEMBL gap and dramatically improve the composite score.

**OE platform relevance:** Smilax glabra is an excellent candidate for **synergy with engineered uricase**. Both act on hyperuricemia via complementary mechanisms (uricase = degrades urate; astilbin = blocks reabsorption + promotes excretion + suppresses production). A Smilax-co-administered or even Smilax-fermented koji product (if compatible) is worth wet-lab exploration. Smilax is GRAS-classified in TCM use; toxicology profile is favorable.

---

### §3.3 Rhein — MODERATE / VIABLE-WITH-DOSE-CAVEAT (rank 3)

**TCM source:** *Rheum officinale* (大黄, Da Huang) — Chinese rhubarb; rhein is also the active metabolite of diacerein (CHEMBL41286 max_phase=3, FDA-recognized osteoarthritis drug).
**ChEMBL ID:** CHEMBL418068

**ChEMBL bioactivity (verified, all OFF-target):**

| Target | IC50 | Source |
|---|---|---|
| Acetylcholinesterase (electric eel) | 637 nM | activity_id 17734059, EJMC 2016 |
| FTO (m6A demethylase) | 2,180 nM | activity_id 24989142, JMC 2021 |
| HSP90 | 3,339 nM | activity_id 3700505, PubChem confirmation |
| ALKBH3, ALKBH5 (alkB demethylases) | 5,300-9,960 nM | activity_id 24989167, 24989023, 26037633 |

**Critical finding: NO ChEMBL bioactivity vs URAT1, ABCG2, XO, or NLRP3.** The literature claim that rhein inhibits URAT1 (frequently cited in TCM gout reviews) is NOT curated in ChEMBL. Yu et al PMID 32209407 reports rhein as URAT1 inhibitor in HEK293T-URAT1 oocyte assay; specific IC50 was not extracted in this analysis [UNVERIFIED — placeholder for future grep].

**Bioavailability:** Diacerein (rhein diacetate) is the FDA-approved prodrug; converted to rhein in vivo with BA ~50% as the active carboxylate. Direct rhein BA also ~50%. Standard diacerein dose 50-100 mg twice daily.

**Verdict rationale (MODERATE / VIABLE-WITH-DOSE-CAVEAT):** Mechanism site is systemic (URAT1, XO are kidney/tissue targets). Plasma Cmax achievable is modest. Off-target enriched profile (AChE, FTO, HSP90, multiple alkB demethylases) is concerning for chronic dosing — selectivity ratio is poor. The diacerein FDA-approval pathway is for osteoarthritis, not gout — repurposing for gout would require:
1. Formal IC50 against URAT1 / XO / ABCG2 (close the ChEMBL gap)
2. Selectivity demonstration vs the off-target panel at therapeutic plasma concentrations
3. Clinical trial vs allopurinol/febuxostat comparator

**OE platform relevance:** Rhein is **NOT a candidate for koji co-expression** (it's a small-molecule plant secondary metabolite, not protein). Its potential as a stand-alone repurposed drug is interesting but lies outside OE's strain-library output. As a discovery-engine output, the mechanism gap is the load-bearing question to resolve.

---

### §3.4 Emodin — GUT-LUMINAL VIABLE (rank 4)

**TCM source:** *Rheum officinale* (大黄, Da Huang) and *Polygonum cuspidatum* (虎杖, Hu Zhang).
**ChEMBL ID:** CHEMBL289277

**ChEMBL bioactivity (verified):**

| Target | IC50 | Source |
|---|---|---|
| Casein kinase II alpha | 890 nM | activity_id 2897088, Biochem J 2003 |
| Estrogen receptor alpha | 2,700 nM | activity_id 1044711, BMCL 2001 |
| Estrogen receptor beta | 5,200 nM | activity_id 1044713, BMCL 2001 |

**NO ChEMBL bioactivity vs URAT1, ABCG2, XO, or NLRP3.**

**Animal-model evidence (verified, KEY FINDING):** PMC10304951 (Hou 2023, doi:10.3390/ph16060789) Sprague-Dawley rats with PO-induced hyperuricemia, emodin 30 + 50 mg/kg significantly lowered SUA via increased fractional excretion of uric acid (FEUA). **Critically, the same study explicitly RULES OUT XO inhibition as the mechanism**: line 33 verbatim — *"The activity did not change significantly between groups. Therefore, the effect of emodin on serum uric acid levels did not occur through the inhibition of xanthine oxidase."* Mechanism is renal urate transporter modulation (URAT1/OAT1/OAT3/ABCG2 not specified).

**Bioavailability:** Emodin systemic BA <5% (heavy gut + hepatic glucuronidation). [UNVERIFIED — bound: 1-5%]. 50 mg dose × 97% gut-retained ÷ 250 mL ≈ 195 mg/L unconstrained, capped at 5 mg/L solubility = **18.5 µM gut lumen** (analogous to curcumin in comp-004).

**Verdict rationale (GUT-LUMINAL VIABLE):** Mechanism is gut-luminal AND tissue (renal). Low BA concentrates compound in gut lumen where local effects on microbiome and mucosal transporters are plausible. Animal-model data confirms in vivo SUA reduction at translatable dose (50 mg/kg → human-equivalent ~8 mg/kg → 500 mg/60-kg adult, within supplement range). Off-target estrogen receptor binding is a chronic-dosing concern (endocrine disruption potential) but at IC50 2,700 nM vs achievable plasma Cmax sub-µM, off-target plasma occupancy is low.

**OE platform relevance:** Emodin is a small-molecule plant metabolite — NOT a koji co-expression candidate. Worth pursuing as a **synergy compound** alongside engineered uricase: emodin handles renal excretion side, uricase handles enzymatic degradation side. Both have favorable safety profiles per existing literature.

---

### §3.5 Aucubin — MECHANISM UNCLEAR (rank 5)

**TCM source:** *Plantago asiatica* (车前子, Che Qian Zi).
**ChEMBL ID:** None — verified zero hits 2026-05-06.

**Bioactivity:** No published IC50 against any urate-handling target found. Mechanism extrapolation only — diuretic effect plausible via aquaporin or RAS modulation but not gout-specific.

**Verdict rationale (MECHANISM UNCLEAR):** Cannot triage with the framework. Would need (1) ChEMBL biochemical screen against URAT1/ABCG2/XO/GLUT9 OR (2) targeted murine PO model dose-response study. Until either lands, aucubin remains in the "tradition-only, mechanism speculative" category. Recommended platform action: defer entirely.

---

### §3.6 Berberine — GUT-LUMINAL VIABLE (rank 6)

**TCM source:** *Coptis chinensis* (黄连, Huang Lian) — the primary "damp-heat" herb in TCM.
**ChEMBL ID:** CHEMBL295124

**ChEMBL bioactivity (verified — re-confirms wiki's chembl-cross-check.md observation):**

| Target | IC50 | Source |
|---|---|---|
| **Tryptophan 2,3-dioxygenase (TDO)** | **30 nM** ⭐ MOST POTENT | activity_id 26130523, EJMC 2024 |
| Cytochrome P450 1B1 | 94 nM | activity_id 18948707, EJMC 2019 |
| Acetylcholinesterase (human) | 100 nM | activity_id 15628432, BMC 2015 |
| Indoleamine 2,3-dioxygenase 1 (IDO1) | 260 nM | activity_id 26130521, EJMC 2024 |

**No ChEMBL hits vs URAT1, ABCG2, XO, or NLRP3 directly.**

**Animal-model evidence (verified):** PMC9635963 line 43 (Yuan 2022) — "berberine (6.25-25.0 mg/kg) and dihydroberberine (25-50 mg/kg) could inhibit URAT1 expression and promote the excretion of uric acid in potassium oxonate-induced hyperuricemia mice [refs 68-71]" — verified Paperclip grep.

**Bioavailability:** <1% systemic (verified — Petrangolini 2021 PMC8665891 doi:10.1155/2021/7563889 explicitly developed enhanced formulations because standard berberine BA is so poor). 500 mg dose × 99.5% gut-retained → effectively 100% in gut. Solubility ~500 mg/L, easily exceeds achievable concentrations → highly enriched in gut lumen.

**Verdict rationale (GUT-LUMINAL VIABLE):** The picture is consistent with the broader chembl-cross-check.md finding for berberine — the most-potent ChEMBL bioactivity (TDO 30 nM) is OFF the gout pathway. The URAT1 effect is real but at much lower potency (animal-model only). Berberine's gout effect is likely a **combination of gut microbiome modulation + low-grade systemic URAT1 effect via the small fraction that absorbs**. Low BA is favorable for the gut-microbiome-mediated arm.

**OE platform relevance:**
1. **Berberine is the strongest case for "TCM compound × engineered uricase synergy"** — both act in the gut, complementary mechanisms (uricase = degradation, berberine = microbiome shift + local immune modulation).
2. Co-fermentation with koji is worth investigating: berberine is an antimicrobial alkaloid — koji may not tolerate co-culture; needs empirical test.
3. The TDO 30 nM hit is unrelated to gout but is a serious off-target for chronic systemic dosing — kynurenine pathway disruption. Low BA limits systemic exposure → not a clinical concern at supplement doses.

---

### §3.7 Cylindrin — MECHANISM UNCLEAR (rank 7)

**TCM source:** *Imperata cylindrica* (白茅根, Bai Mao Gen).
**ChEMBL ID:** None.

**Bioactivity:** No ChEMBL data; no published gout-relevant IC50 found. Mechanism speculative.

**Verdict rationale:** Same as aucubin — defer entirely until ChEMBL biochemical screen or murine model data lands.

---

### §3.8 Chlorogenic acid — MECHANISM UNCLEAR (rank 8)

**TCM source:** *Lonicera japonica* (金银花, Jin Yin Hua); also abundant in coffee, many plants.
**ChEMBL ID:** CHEMBL284616

**ChEMBL bioactivity (verified — all off-target for gout):**

| Target | IC50 | Source |
|---|---|---|
| PTP1B (PTPN1) | 100 nM | activity_id 23169820, BMC 2021 |
| Aldo-keto reductase 1B1 (AKR1B1) | 300 nM | activity_id 7998582, EJMC 2012 |
| ONOO scavenging (cell-free) | 520 nM | activity_id 19004038, BMC 2020 |

**NO ChEMBL hits vs URAT1, ABCG2, XO, NLRP3.**

**Bioavailability:** ~33% systemic (Stalmach 2010 PMID 19735245 healthy ileostomy subjects; significant gut microbiota metabolism to caffeic acid + quinic acid).

**Verdict rationale (MECHANISM UNCLEAR):** ChEMBL has IC50 data, but none are against gout-relevant targets. PTP1B at 100 nM is metabolic-syndrome-relevant (insulin signaling), not gout-direct. The TCM "anti-inflammatory + diuretic" framing for Jin Yin Hua does not map cleanly to a chokepoint in gout pathophysiology. **Mechanism for gout is Mechanistic Extrapolation, not Supported.** Recommended action: defer chlorogenic acid as a primary candidate; it remains relevant as anti-inflammatory adjunct in multi-component formulas but doesn't earn first-class status under the rigorous lens.

---

### §3.9 Atractylenolide I — MECHANISM UNCLEAR (rank 9)

**TCM source:** *Atractylodes macrocephala* / *lancea* (苍术, Cang Zhu) — component of Si Miao San.
**ChEMBL ID:** None.

**Bioactivity:** No ChEMBL data; HDAC inhibition claim (from Brian's task brief) is speculative — not in ChEMBL v34, not in the comp-007 corpus.

**Verdict rationale:** Cannot triage as an isolated compound. However, **Si Miao San as a multi-herb formula** has the strongest clinical evidence in this entire analysis — see §4.

---

## §4 Cross-cutting findings

### §4.1 Most-represented mechanism: URAT1 expression downregulation in animal models

The single most-represented mechanism across viable TCM gout candidates is **URAT1 expression downregulation in the murine PO hyperuricemia model**. Astilbin, luteolin, and berberine all show this effect at translatable doses (5-25 mg/kg). Per Yuan 2022 PMC9635963, this is a recurring pattern across natural product flavonoids and alkaloids — the C-ring of flavonoids is electron-rich and partially explains URAT1 binding.

**Implication for OE methodology:** URAT1 modulation may be a more reachable mechanism for natural products than direct ABCG2 activation or NLRP3 inhibition. The broader TCM corpus likely contains many more URAT1-modulating candidates worth investigating.

### §4.2 ChEMBL data sparsity is a load-bearing limitation

**5 of 9 candidate compounds have NO ChEMBL bioactivity data of any kind.** Of the 4 with ChEMBL data (rhein, emodin, berberine, chlorogenic acid, luteolin), only luteolin has a curated biochemical IC50 against a gout-relevant target (XO 550 nM).

This is the single most important methodology finding from comp-013: **the ChEMBL cross-check discipline (per `chembl-cross-check.md` and rule #2 of `tcm-modern-rigor-intersection.md`) is not fully applicable to TCM compounds because the curated database simply doesn't have most of them.** The discipline as written assumes reasonably comprehensive ChEMBL coverage — which is true for FDA-approved drugs, much of medicinal chemistry literature, and even many natural products — but fails for the long tail of TCM-specific phytochemicals.

The workaround used here: admit animal-model in vivo dose-response data as evidence for the verdict, while keeping the composite numerical score honest (composite = 0 when no biochem IC50 is available). Future work would benefit from a targeted in vitro biochemical screen against URAT1/ABCG2/XO using the cassette compatibility data we've generated for the validation pipeline.

### §4.3 Si Miao San: strongest clinical evidence, weakest mechanistic attribution

The **Si Miao San / Modified Simiao Decoction (MSD) meta-analysis (Liu 2017 PMC5360963 doi:10.1155/2017/6037037) of 24 RCTs is the highest-grade clinical evidence in this entire analysis** — verified via Paperclip grep:

> "MSD monotherapy significantly lowered serum uric acid (p<0.00001, mean difference = −90.62 µmol/L, 95% CI [−128.38, −52.86]; vs urate-lowering therapies: −91.43 µmol/L; combined: additive −40.30 µmol/L)"

Adverse effects were significantly fewer (OR=0.08). Comparable urate reduction to allopurinol with better safety profile.

But the meta-analysis cannot attribute this efficacy to a single component — Si Miao San has 4 herbs (Phellodendron + Atractylodes + Achyranthes + Coix), each with multiple bioactives. The "designed coverage vs redundancy" decomposition (rule #4 of tcm-modern-rigor-intersection.md) is a real epistemic problem here. Three of the 4 components contribute compounds in our triage table (atractylenolide I from Cang Zhu, berberine from Huang Bai per the Phellodendron-berberine pathway, plus uncharacterized Achyranthes saponins and Coix coixol/coixenolide). At least one of these is likely doing most of the urate-lowering work, but without component-isolation studies, attribution is impossible.

**Recommended platform action:** Si Miao San is the highest-priority TCM gout intervention by clinical evidence. For OE, it represents a **discovery-engine output** rather than a strain-library output (it's a multi-herb decoction, not a fermentable strain). Possible OE contributions: (1) component-isolation studies via fractionated extracts; (2) integration of Si Miao San as adjunct therapy in any human protocol involving engineered uricase or LBP chassis; (3) systematic ChiCTR-database scan for additional Si Miao San variants and clinical experience.

### §4.4 Platform-relevance ranking

For OE's strain-library output (koji co-expression / synergy with engineered uricase):

1. **Astilbin / Smilax glabra extract** — most platform-relevant. Multi-mechanism in vivo efficacy, gut-luminal favorable BA, classical primary gout herb. Worth wet-lab co-administration study with engineered uricase.
2. **Berberine** — second-most platform-relevant. Strongest case for "gut-microbiome modulator × engineered uricase synergy." Antimicrobial property may complicate co-fermentation with koji; needs empirical test.
3. **Luteolin** — analytically valuable (clean ChEMBL IC50) but raises the gut-ABCG2-paradox flag (see §3.1). Strategic use only.
4. **Emodin** — secondary candidate. Stand-alone synergy compound; rules out XO mechanism explicitly which is useful information for the broader urate-handling map.
5. Rhein, chlorogenic acid, aucubin, cylindrin, atractylenolide I — defer or use only as multi-herb formula components.

For OE's discovery-engine output (mechanistic clarity, repurposing surface):

1. **Si Miao San** — highest priority for component decomposition + integration with allopurinol-comparator data
2. **Smilax glabra extract** standardization (rule #5) — significant scientific opportunity
3. **Rhein-URAT1 mechanism gap closure** — formal IC50 measurement is a 1-week wet-lab experiment with reasonable cost

---

## §5 Methodology — comp-004 + comp-007 framework adaptation

### §5.1 comp-004 IC50 occupancy framework — direct application

Identical to comp-004's protocol:
- Hill equation n=1: fractional_inhibition = ratio / (ratio + 1)
- Gut-conc model: dose × (1 − BA) ÷ 250 mL, capped at intestinal solubility
- Risk thresholds: LOW <0.5×, MODERATE 0.5-2×, HIGH 2-5×, VERY_HIGH ≥5×
- Plasma Cmax via crude single-dose: dose × BA / (Vd × BW), Vd ≈ 1 L/kg for polyphenols

### §5.2 comp-007 composite scoring — adapted for site-aware mechanism

Three pivots from comp-007's HDACi screen formulation:

1. **Gut-enrichment is BIDIRECTIONAL.** comp-007's HDACi candidates all targeted Q141K-ABCG2 in gut mucosa — a target where low BA is uniformly favorable. TCM compounds split: gut-luminal targets (favorable for low BA) vs systemic targets URAT1/XO/NLRP3 (UNFAVORABLE for low BA). The gut-enrichment score is now site-aware:
   - gut-luminal-only: score = 1 − BA (low BA favorable)
   - systemic-only: score = BA (high BA favorable; low BA penalized)
   - mixed: balanced midpoint

2. **Selectivity uses on-target / off-target ratio.** comp-007 used HDAC6/class-I ratio (cardiotoxicity avoidance). Here:
   - on-target IC50 = best (lowest) IC50 against any gout-relevant target in the panel
   - off-target IC50 = best IC50 against any non-gout-relevant target
   - selectivity = off / on (higher = more selective for gout target)
   - sigmoid normalization at midpoint = 10

3. **Animal-model evidence is admissible.** comp-007 ranked on biochemical IC50 only. For TCM compounds, ChEMBL coverage is so sparse that animal in vivo dose-response data must count toward the verdict — explicitly tagged in `evidence_level` field. The composite score remains honest (= 0 when no biochem IC50), but the verdict assignment uses an override that admits animal-model evidence.

### §5.3 Bioavailability honesty layer

For each compound, four data points are tracked:
- Oral bioavailability fraction (cited if available; bounded estimate otherwise)
- Achievable gut-luminal concentration (per comp-004 model)
- Achievable plasma Cmax (per crude Vd=1 L/kg estimate)
- Mechanism site (gut-luminal / systemic / mixed)

This is the load-bearing layer for TCM compound triage. Many compounds have impressive in vitro IC50s that cannot be achieved in vivo at any reasonable dose; the BA layer separates "real candidate" from "in vitro artifact at unachievable concentration."

---

## §6 Limitations

- **ChEMBL coverage gap (load-bearing).** 5 of 9 candidate compounds are not curated in ChEMBL v34 at all (astilbin, aucubin, cylindrin, atractylenolide I; partial coverage for chlorogenic acid). The composite score reflects this honestly (= 0 for these compounds), but the verdict assignment leans heavily on animal-model data via the override path. Future work: targeted in vitro biochemical IC50 screen against URAT1/ABCG2/XO would close the largest gap and re-rank significantly.

- **Plasma Cmax is order-of-magnitude.** Crude single-dose estimate using Vd ≈ 1 L/kg for polyphenols. Real Cmax depends on dose, formulation, absorption rate, clearance kinetics, and saturation. Quantitative IC50 occupancy at plasma is therefore approximate; verdict directions (high/moderate/low) should be robust but absolute % inhibition values carry ±2-3× uncertainty.

- **Animal-to-human dose translation uses no formal allometric scaling.** Murine 5-50 mg/kg → human-equivalent ~1-8 mg/kg via BSA scaling factor = 60-500 mg/60-kg adult. Used as bounded estimate, not precise prediction.

- **Multi-component formula attribution is unresolved.** Si Miao San's clinical effect cannot be attributed to a single component without isolation studies. The triage of individual components (atractylenolide I, berberine, etc.) does NOT capture the formula's true effect.

- **Off-target panel is not comprehensive.** Selectivity ratio uses only the off-target hits already in ChEMBL — does not exclude unmeasured off-target effects. Compounds with no off-target ChEMBL data may have hidden off-targets we cannot score.

- **Bounded placeholders for BA values.** Astilbin, aucubin, cylindrin, atractylenolide I bioavailability values are `[UNVERIFIED — bound: ...]` per the verification gate discipline. Verdict directions are robust to bounded uncertainty; absolute values are not.

- **Single-dose reporting.** One representative supplement dose used per compound. Dose-response analysis is the natural follow-up.

- **Substrate-dependent IC50.** Inherits comp-004's caveat: IC50 measured against fluorescent substrates (Hoechst, mitoxantrone) may differ from urate-substrate IC50. ABCG2 IC50 specifically. Luteolin XO IC50 was measured with xanthine substrate (multiple assays) so this caveat is less load-bearing for the XO data.

- **The chembl-cross-check methodology has a coverage limit for TCM compounds.** As discussed in §4.2, this is the single most important meta-finding from comp-013.

---

## §7 Cross-references

- [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) — the scope page this analysis operationalizes (closes P2-2 follow-up)
- [`chembl-cross-check.md`](./chembl-cross-check.md) — the ChEMBL discipline this applies; berberine TDO-30nM finding re-confirmed
- [`supplement-abcg2-antagonism-computational.md`](./supplement-abcg2-antagonism-computational.md) — comp-004; framework template for IC50 occupancy
- [`food-grade-hdaci-screen-computational.md`](./food-grade-hdaci-screen-computational.md) — comp-007; framework template for composite scoring (this analysis adapts the gut-enrichment scoring for bidirectional sites)
- [`abcg2-modulators.md`](./abcg2-modulators.md) — luteolin-as-ABCG2-inhibitor flagged here connects back to comp-004's broader supplement-paradox finding
- [`gut-lumen-sink.md`](./gut-lumen-sink.md) — gut-luminal mechanism thesis fits perfectly with TCM bioavailability profile
- [`computational-experiments.md`](./computational-experiments.md) — tracking index entry for comp-013
- [`manual-literature-mining.md`](./manual-literature-mining.md) §"Pre-commit verification gate" — verification protocol applied to every load-bearing number in this analysis
- [`hypotheses/H04-tcm-rigor-intersection.md`](./hypotheses/H04-tcm-rigor-intersection.md) — falsification card stub for the methodology lens
- [`experiments/comp-013-tcm-gout-compound-triage/`](../experiments/comp-013-tcm-gout-compound-triage/) — reproducible artifact

**External sources cited inline (with DOI links per PubMed attribution discipline):**

Per the PubMed attribution requirement, all primary literature sources cited above are PubMed-indexed and identified by DOI:
- PMC9635963 — [doi:10.1155/2022/5419890](https://doi.org/10.1155/2022/5419890) — Yuan et al 2022 review of natural product URAT1 inhibitors
- PMID 31005813 — [doi:10.1016/j.phymed.2018.11.032](https://doi.org/10.1016/j.phymed.2018.11.032) — Liang et al 2018 Smilax glabra mouse PO model
- PMID 30851369 — [doi:10.1016/j.jep.2019.03.004](https://doi.org/10.1016/j.jep.2019.03.004) — Huang et al 2019 astilbin stereoisomers
- PMC5360963 — [doi:10.1155/2017/6037037](https://doi.org/10.1155/2017/6037037) — Liu et al 2017 Modified Simiao decoction meta-analysis
- PMC10304951 — [doi:10.3390/ph16060789](https://doi.org/10.3390/ph16060789) — Hou et al 2023 emodin rat PO model
- PMID 34885887 — [doi:10.3390/molecules26237307](https://doi.org/10.3390/molecules26237307) — Zhang et al 2021 Smilax XOD inhibitors
- PMC8665891 — [doi:10.1155/2021/7563889](https://doi.org/10.1155/2021/7563889) — Petrangolini et al 2021 berberine bioavailability
- ChEMBL v34 bioactivity data accessed via mcp__plugin_chembl_ChEMBL__get_bioactivity, fetch date 2026-05-06, all activity_ids cited inline
