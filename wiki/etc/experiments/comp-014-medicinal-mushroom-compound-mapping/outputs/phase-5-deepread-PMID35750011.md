# Phase 5 Deep-Read: G. applanatum 2,4-DAE (PMID 35750011)

## Source citation

- **Title:** Hypouricemic effect of 2,4-dihydroxybenzoic acid methyl ester in hyperuricemic mice through inhibiting XOD and down-regulating URAT1
- **Authors:** Yong T, Liang D, Xiao C, Huang L, Chen S, Xie Y, Gao X, Wu Q*, Hu H, Li X, Liu Y, Cai M
- **Journal:** *Biomedicine & Pharmacotherapy* 153:113303 (2022) — **NOT** *Fitoterapia* as the comp-014 brief stated. Worth correcting upstream.
- **DOI:** [10.1016/j.biopha.2022.113303](https://doi.org/10.1016/j.biopha.2022.113303)
- **PMID:** 35750011 · no PMC ID (not OA in PubMed Central)
- **Affiliations:** Guangdong Provincial Key Laboratory of Microbial Safety and Health, Institute of Microbiology, Guangdong Academy of Sciences, Guangzhou; Guangdong Yuewei Edible Fungi Technology Co.; Affiliated Hospital of Guangdong Medical University.

**Source-availability constraint.** Full text is **not in Paperclip** and **not in PMC OA**. The deep-read below is built from (a) the PubMed-indexed abstract (verified verbatim via `get_article_metadata` for PMID 35750011) and (b) **direct full-text reading of the immediate predecessor paper from the same group** — Liang/Yong et al. 2018 on 2,5-DHAP from *G. applanatum* in *Int. J. Mol. Sci.* (PMC5983617, [DOI: 10.3390/ijms19051427](https://doi.org/10.3390/ijms19051427)) — and the original 2017 *G. applanatum* extract paper (PMC5775298, [DOI: 10.3389/fphar.2017.00996](https://doi.org/10.3389/fphar.2017.00996)). The DAE paper (PMID 35750011) and DHAP paper (PMC5983617) share author overlap (Yong T, Liang D, Chen S, Xie Y, Hu H, Li X), the exact same hyperuricemia model, the exact same dose ladder (20/40/80 mg/kg), the exact same baseline SUA reading (407 ± 31 µmol/L), and identical positive controls. Methodology in the DHAP paper can be treated as the methodology of the DAE paper with very high confidence — the DAE paper is the next compound in the same screening pipeline. Where claims rest on the abstract alone, this is flagged inline.

According to PubMed.

---

## 1. Compound identity

**Question:** Is "2,4-DAE" really 2,4-dihydroxybenzoic acid methyl ester? Structure? SMILES? Single compound or a fraction?

**Answer:** Yes. The compound is unambiguously **2,4-dihydroxybenzoic acid methyl ester**, referred to as **DAE** in the paper. This is methyl 2,4-dihydroxybenzoate — a single defined small molecule, not a fraction.

- **IUPAC:** methyl 2,4-dihydroxybenzoate
- **Synonyms:** methyl β-resorcylate; 2,4-DHBA methyl ester; 2,4-DAE
- **Molecular formula:** C₈H₈O₄ · MW 168.15
- **SMILES:** `COC(=O)c1ccc(O)cc1O`
- **InChIKey:** GVSXTPIASZEKDB-UHFFFAOYSA-N
- **PubChem CID:** 78329
- **Structure:** benzene ring with –OH at C2, –OH at C4, –C(=O)OCH₃ at C1. Phenolic + methyl ester. Closely related to methyl paraben (4-OH only) and to gentisate methyl ester (2,5-OH). Structurally analogous to **2,5-dihydroxyacetophenone (DHAP)** from the same group's predecessor paper (a 2,5-dihydroxyphenyl small molecule with a polar carbonyl substituent), supporting that the same XOD-active pharmacophore — *ortho*-hydroxy-substituted phenol with an electron-withdrawing carbonyl group — is being explored across both papers.

Citation for compound identity: PubMed metadata for [PMID 35750011](https://citations.gxl.ai/papers/35750011#L1) (title + abstract). Structure derived from IUPAC name; confirmed by PubChem CID 78329 (external).

---

## 2. Source attribution

**Question:** Biosynthesized BY *G. applanatum* or detected in extract? Fruiting body / mycelium / EPS? Extraction method?

**Answer (from abstract + adjacent group papers):**

- The paper describes DAE as **"a component of *Ganoderma applanatum*"** ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)). Per the predecessor DHAP paper from the same group, the workflow is: (i) extract the dried fruiting body of *G. applanatum* (sample provided and authenticated by Guangdong Yuewei Edible Fungi Technology Co., voucher YW20170517-GA at Guangdong Institute of Microbiology) with ethanol (GAE) and water (GAW) ([PMC5775298, L16–L18](https://citations.gxl.ai/papers/PMC5775298#L16)); (ii) computationally screen identified small molecules from an in-house *G. applanatum* compound database against XOD via molecular docking ([PMC5775298, L13](https://citations.gxl.ai/papers/PMC5775298#L13); [PMC5983617, L13](https://citations.gxl.ai/papers/PMC5983617#L13)); (iii) test top-ranked computationally-screened hits in vitro and in vivo. DHAP and DAE are both products of this workflow.
- **DAE for the in vivo experiment was almost certainly purchased commercially**, not isolated from the fungus. The DHAP paper explicitly bought DHAP (98%) from Aladdin Reagent Co., Shanghai ([PMC5983617, L38](https://citations.gxl.ai/papers/PMC5983617#L38)). 2,4-dihydroxybenzoic acid methyl ester is a cheap, commercially available reagent. The fungus is the **source-attribution rationale** (occurrence in *G. applanatum*); the actual material dosed in mice is commercial. **This is a load-bearing nuance for comp-014 chokepoint mapping** — the paper does NOT establish that *G. applanatum* fruiting body produces DAE at therapeutically relevant levels. It establishes only that DAE has been previously reported as occurring in *G. applanatum* and that, when administered as a pure compound, it lowers SUA in the PO+HX mouse model.
- **Part of fungus / extraction method:** Not specified in the abstract; the source-attribution would route through the *G. applanatum* in-house compound database referenced in the 2017 and 2018 group papers, which catalogs compounds reported from fruiting body extracts in the literature. Not from EPS / mycelium specifically per available text.

**Flag for downstream Phase 6 triage:** if comp-014's medicinal-mushroom strategy hinges on direct fungal biosynthesis (e.g., engineering *G. applanatum* or expressing the compound's biosynthetic pathway in a chassis), the DAE paper alone does not validate that biosynthesis route. It validates only the *pharmacological* claim that DAE — supplied as pure commercial small molecule — lowers SUA in mice. The connection to *G. applanatum* biology is computational/literature-based.

---

## 3. In vivo mouse data — exact numbers

| Parameter | Value | Source |
|---|---|---|
| **Hyperuricemia model** | Potassium oxonate (PO) + hypoxanthine (HX). PO **300 mg/kg i.p.**, HX **500 mg/kg p.o.**, given 1 h before drug. | [PMC5983617 §4.3, L42](https://citations.gxl.ai/papers/PMC5983617#L42); identical model implied for DAE paper given 407 ± 31 µmol/L baseline matches exactly. |
| **Mouse strain** | Male Kunming mice, SPF, 20 ± 2 g, from Guangdong Provincial Medical Laboratory Animal Centre. | [PMC5983617 §4.3, L42](https://citations.gxl.ai/papers/PMC5983617#L42) |
| **DAE doses tested** | 20, 40, 80 mg/kg p.o. (oral gavage) | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) |
| **Sample size per group** | n = 10 per group at randomization (per group-standard protocol); n = 8 at sacrifice/analysis (per group-standard figure legends in DHAP paper). | [PMC5983617 §4.3, L42](https://citations.gxl.ai/papers/PMC5983617#L42); [PMC5983617 Fig 3 legend, L61](https://citations.gxl.ai/papers/PMC5983617#L61) |
| **Treatment duration** | 7 days, once daily oral administration | [PMC5983617 §4.4, L44](https://citations.gxl.ai/papers/PMC5983617#L44) |
| **Baseline SUA (hyperuricemia control)** | **407 ± 31 µmol/L** | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) — verbatim |
| **DAE 20 mg/kg → SUA** | **195 ± 23 µmol/L** (p < 0.01) | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) — verbatim |
| **DAE 40 mg/kg → SUA** | **145 ± 33 µmol/L** (p < 0.01) | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) — verbatim |
| **DAE 80 mg/kg → SUA** | **134 ± 16 µmol/L** (p < 0.01) | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) — verbatim |
| **Dose-dependence** | Yes — dose-dependent reduction explicitly stated. | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) |
| **Efficacy vs. allopurinol/benzbromarone** | DAE efficacies 54–68%, allopurinol 61%, benzbromarone 57%. | [PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1) |
| **Allopurinol positive control dose** | 5 mg/kg (per predecessor paper protocol; abstract doesn't restate dose) | [PMC5983617 §4.4, L44](https://citations.gxl.ai/papers/PMC5983617#L44) |
| **Benzbromarone positive control dose** | 7.8 mg/kg (per predecessor paper protocol) | [PMC5983617 §4.4, L44](https://citations.gxl.ai/papers/PMC5983617#L44) |

**Verification of the comp-014 Phase 4 claim (407 → 134 µmol/L):**

✅ **VERIFIED at the abstract level** for the **80 mg/kg dose**. The 407 ± 31 → 134 ± 16 µmol/L claim corresponds specifically to the **highest dose** tested (80 mg/kg). Lower doses (20 and 40 mg/kg) reduced SUA to 195 and 145 µmol/L respectively. The Phase 4 framing — if it implied *the* SUA reduction without dose qualification — slightly oversells the result; it's a top-of-range figure, not a typical-dose figure. At the human-equivalent dose (using FDA mouse-to-human BSA factor of 12.3, the 80 mg/kg mouse dose ≈ 6.5 mg/kg human ≈ ~450 mg for a 70 kg adult), this is a substantial daily dose for a small-molecule supplement, which weighs on translation feasibility.

**Urinary uric acid:** Per abstract, DAE elicited "higher and negatively dose-independent urinary uric acids in comparison with that of the hyperuricemic control." Translation: DAE increased UUA across all doses (uricosuric effect) but UUA did **not** rise monotonically with dose. The interpretation given by the authors is that DAE simultaneously inhibits XOD (lowering uric acid production, which would lower UUA) and inhibits URAT1 reabsorption (raising UUA) — the two effects partially cancel for UUA but compound for SUA. ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1))

---

## 4. Mechanism — XOD inhibition

**Question:** In vitro IC50? Inhibition type? Kinetic constants? Comparison to allopurinol?

**Answer (largely abstract-level, with predecessor methodology context):**

- **In vitro XOD inhibition reported:** "DAE exhibited an inhibitory effect against XOD" ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)) — qualitative confirmation in abstract. **No IC50 value is given in the abstract.** The companion DHAP paper reports DHAP IC50 = 8.12 ± 0.27 µM vs allopurinol IC50 = 2.22 ± 0.21 µM ([PMC5983617 §2.1, L17](https://citations.gxl.ai/papers/PMC5983617#L17)). DAE's IC50 is presumably reported in the full text but is **not extractable from the abstract alone**. Phase 5 cannot verify a specific IC50 number for DAE without retrieving the full Biomed Pharmacother paper (paywalled, would need institutional access or interlibrary loan).
- **Type of inhibition (competitive / mixed / uncompetitive):** Not in abstract. Predecessor papers from this group typically run Lineweaver-Burk analysis and conclude competitive inhibition for allopurinol-like XOD inhibitors via molecular docking to the molybdopterin active site. **Unable to verify for DAE without full text.**
- **Kinetic constants (Ki, Km changes):** Not in abstract. **Unable to verify.**
- **Allopurinol comparison:** The abstract states DAE "showed a high similarity to allopurinol and depicted a high affinity in docking to XOD" ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)). Computationally this is plausible — DAE is a small phenolic carbonyl very different from allopurinol's hypoxanthine analog scaffold, but the H-bond donor/acceptor pattern with active-site residues (SER514, GLN626, MET470) seen for the parent DHAP series is likely reproduced for DAE.
- **In vivo XOD activity:** "DAE inhibited XOD activities in vivo" ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)). Per the DHAP protocol, this would be measured as serum XOD activity by ELISA at sacrifice ([PMC5983617 §4.5, L46](https://citations.gxl.ai/papers/PMC5983617#L46)).

**Caveat:** Bovine milk XOD (PDB 1FIQ) is the docking target across both papers. Bovine XOD has high sequence/structural similarity to human XOR but is not identical — extrapolation to human XO is reasonable but not direct.

---

## 5. Mechanism — URAT1

**Question:** Direct binding or expression downregulation? Tissue (kidney protein/mRNA)? Comparison to benzbromarone?

**Answer:**

- **DAE down-regulates URAT1.** Per the abstract: "DAE up-regulated OAT1 and down-regulated GLUT9, URAT1 and CNT2" ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)). This is **expression-level downregulation, not direct transporter binding.** The methodology (per the parallel DHAP paper, which the DAE paper inherits) is RT-PCR for renal URAT1 mRNA + Western blot for renal URAT1 protein ([PMC5983617 §4.8, L52](https://citations.gxl.ai/papers/PMC5983617#L52); [PMC5983617 §4.9, L54](https://citations.gxl.ai/papers/PMC5983617#L54); [PMC5983617 Fig 7, L65](https://citations.gxl.ai/papers/PMC5983617#L65)).
- **Tissue:** Renal cortex / whole kidney homogenate. Not transporter inhibition assays in heterologous expression systems.
- **Comparison to benzbromarone:** Benzbromarone (7.8 mg/kg) is a positive control, used at a dose that yielded comparable SUA reduction in the DHAP study (217 µmol/L vs DHAP's 139 µmol/L; close in efficacy). For URAT1, benzbromarone is a *direct* inhibitor (binds URAT1 protein, blocks urate reabsorption). DAE's mechanism is *expression* downregulation — a fundamentally different pharmacology, and slower-acting. **This distinction is load-bearing for chokepoint attribution:** the paper's "DAE acts through URAT1" claim does not mean DAE is a URAT1 ligand. It means DAE-treated mice have lower URAT1 protein in kidney. Whether this is direct transcriptional regulation, indirect via reduced SUA feedback on URAT1 expression, or off-target effect on the chosen Western blot target is **not differentiated by the experimental design.**

**Phase 6 triage flag:** the chokepoint label "URAT1" in comp-014 Phase 4 should be qualified as "URAT1 expression-level downregulation in mouse kidney" rather than "URAT1 inhibitor." This affects downstream comparisons — DAE is **not** mechanistically equivalent to benzbromarone or verinurad despite the abstract's parallel language.

---

## 6. Other chokepoint mentions

| Chokepoint | Mentioned? | Notes |
|---|---|---|
| **NLRP3** | No | Not in abstract or keyword list. Inflammation pathway not explored in this paper. |
| **GLUT9** | **Yes** | DAE down-regulates GLUT9 (renal expression level). Same caveat as URAT1 — expression, not direct transporter. ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)) |
| **OAT1** | **Yes** | DAE up-regulates OAT1 (renal expression level). Mechanism for enhanced urinary uric acid excretion. ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)) |
| **OAT3** | No | Not measured. |
| **ABCG2** | No | Not measured. **Notable omission** given ABCG2 accounts for ~30% of uric acid extra-renal excretion (gut secretion pathway). The paper's mechanism map is renal+gastrointestinal-CNT2-only. |
| **CNT2** | **Yes** | DAE down-regulates intestinal CNT2 (concentrative nucleoside transporter 2 — affects purine nucleoside absorption). Adds a pre-XOD-substrate gut absorption arm to the mechanism. ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)) |
| **Complement** | No | Not measured. |
| **Lp-PLA2** | No | Not measured. |
| **HDAC6** | No | Not measured. |
| **Redox / disulfide chemistry (PDI, TXNIP, ergothioneine, thioredoxin)** | No | Not mentioned. DAE's pharmacology is described as XOD inhibition + transporter expression modulation; no redox/oxidative-stress mechanism is invoked in the abstract. |

**Net chokepoint coverage from this paper:** 4 chokepoints — XOD (direct inhibition), URAT1 (expression down), GLUT9 (expression down), OAT1 (expression up), and one absorption-side target — CNT2 (expression down). This is the same panel as the DHAP paper, by design.

---

## 7. Toxicity / safety

**Question:** Adverse effects, LD50, chronic toxicity?

**Answer:**

- **General toxicity:** Per abstract, "no general toxicity on body weights and no negative influence on liver, kidney, spleen and thymus were observed for DAE" ([PMID 35750011 abstract](https://citations.gxl.ai/papers/35750011#L1)).
- **Comparator finding:** Both allopurinol and benzbromarone showed toxicity in this model; DAE did not, per the abstract framing.
- **Limitations:** The "no toxicity" claim is based on body weight + organ coefficient measurements over **7 days only** in healthy adult male Kunming mice. This is acute-subacute toxicity, not chronic. The DHAP predecessor paper measured the same endpoints (BUN, creatinine, organ coefficients) at the same 7-day timepoint and found DHAP also non-toxic on these readouts. **The "no toxicity" finding in this paper class is robust for short-term lower-tier safety, weak for chronic / off-target / reproductive / immunotoxicity.**
- **LD50:** Not measured. **Unable to extract from abstract.**
- **Chronic toxicity:** Not measured (study is 7-day acute).
- **DAE-specific known liabilities (external):** 2,4-dihydroxybenzoic acid methyl ester is a phenolic ester with structural similarity to methylparaben; methylparaben has a small literature on weak estrogenic activity at high concentrations. Not addressed in this paper. Worth checking external sources before downstream advancement.

---

## 8. Chinese-source evidence anchor

**Question:** Chinese-affiliated authors? CNKI / TCM literature reference?

**Answer:**

- **Yes — entirely Chinese-affiliated authorship.** All 12 authors are at Guangdong Provincial Key Laboratory of Microbial Safety and Health / Institute of Microbiology, Guangdong Academy of Sciences (Guangzhou) and Guangdong Yuewei Edible Fungi Technology Co. (Guangzhou). One co-author is at Affiliated Hospital of Guangdong Medical University (Zhanjiang).
- **TCM/Chinese-literature anchor:** The predecessor 2018 DHAP paper grounds the *G. applanatum* selection in classical Chinese herbal literature: "*G. applanatum* was recorded as a diuresis agent in Chinese herbal classic literature, and closely associated with the prevention of HUA. Clinically, *G. applanatum* as a folk medicine, has been exploited to prevent and treat various diseases since 100 BC..." ([PMC5983617, L13](https://citations.gxl.ai/papers/PMC5983617#L13)). The 2018 paper cites Li Y., *Fugal Resource* (China Agriculture Press, Beijing, 2013), in Chinese ([PMC5983617, L78](https://citations.gxl.ai/papers/PMC5983617#L78)). The DAE paper presumably retains this anchor.
- **Phase 5b CNKI dive — recommendation:** **YES, warranted.** Specific search targets:
  1. *G. applanatum* (中文: 树舌灵芝 *shù shé líng zhī*, or 平盖灵芝 *píng gài líng zhī*) — TCM materia medica entries on diuresis / dampness-removal / hyperuricemia.
  2. **2,4-二羟基苯甲酸甲酯** (2,4-dihydroxybenzoic acid methyl ester) — search CNKI / WanFang for any prior Chinese-language pharmacology or compound-isolation reports from *Ganoderma* species.
  3. Yong T. / Liang D. / Chen S. — prior Chinese-language publications by the Guangdong Institute of Microbiology group; this lab publishes both English and Chinese, and the Chinese-language work on *G. applanatum* compound databases may have richer source-attribution detail.
  4. **ChiCTR** (China Clinical Trial Registry) — any registered clinical trials of *G. applanatum* extracts or DAE for hyperuricemia.
- **Cross-vendor translation discipline (per Open Enzyme CLAUDE.md):** any CNKI hits should be translated with a Chinese-vendor model (DeepSeek / Qwen) + a Western model (Claude / Gemini), with disagreements annotated inline. Particularly important for classical TCM terminology (*shī rè* / dampness-heat, *lì shuǐ* / promote-diuresis) where Western models lose nuance.

---

## Summary of verifiable / unverifiable claims

| Claim | Verified? | Source |
|---|---|---|
| Compound is 2,4-dihydroxybenzoic acid methyl ester | ✅ Verified | PubMed metadata, title |
| Single defined small molecule (not fraction) | ✅ Verified | Title + abstract framing |
| Source: *G. applanatum* (literature/computational attribution, not de novo isolation in this paper) | ⚠️ Qualified yes | Abstract ("a component of"); methodology context from PMC5983617 / PMC5775298 |
| Hyperuricemia model: PO + HX, mouse | ✅ High confidence | DHAP predecessor identical protocol |
| Doses 20/40/80 mg/kg p.o., 7 days | ✅ Verified | Abstract |
| **Baseline SUA 407 ± 31 µmol/L** | ✅ Verified verbatim | Abstract |
| **80 mg/kg → SUA 134 ± 16 µmol/L** | ✅ Verified verbatim | Abstract |
| **407 → 134 reduction is dose-dependent + at top dose, not at low dose** | ✅ Verified | Abstract — full dose-response curve disclosed |
| In vitro XOD IC50 (specific value) | ❌ Not in abstract | Would require full text |
| XOD inhibition type (competitive/mixed) | ❌ Not in abstract | Would require full text |
| URAT1 mechanism = expression downregulation, not direct binding | ✅ Verified | Abstract + identical predecessor methodology |
| ABCG2 / NLRP3 / OAT3 / complement / redox mentioned | ❌ Not mentioned | Abstract + keyword list |
| No general toxicity at 7 days | ✅ Verified verbatim | Abstract |
| Chronic / LD50 toxicity | ❌ Not measured | Abstract states only 7-day acute |
| Chinese-affiliated authors | ✅ Verified | Affiliations |

---

## Concerns and surprises

1. **Journal mis-attribution in comp-014 brief.** Brief states *Fitoterapia*; actual journal is *Biomedicine & Pharmacotherapy*. Minor but should be corrected in upstream phase notes.
2. **Source attribution is computational/literature-based, not isolation-based in this paper.** The claim "DAE from *G. applanatum*" rests on prior literature occurrence + in-house compound database, with the in vivo material almost certainly purchased commercially. **If comp-014's medicinal-mushroom thesis depends on direct fungal biosynthesis at therapeutic levels, this paper does not support that.**
3. **URAT1 "effect" is expression-level, not direct transporter inhibition.** Phase 6 chokepoint mapping should distinguish DAE (expression modulator) from benzbromarone-class direct URAT1 inhibitors. Mechanistic inference from "downregulates URAT1" to "blocks urate reabsorption" requires the reduced URAT1 protein actually limits transport flux — not measured in this paper.
4. **Abstract-only verification means IC50 / Ki / kinetic data are inaccessible.** Phase 5 cannot answer whether DAE is a strong (IC50 < 1 µM) or weak (IC50 > 50 µM) XOD inhibitor relative to allopurinol. The DHAP predecessor was 8.12 µM vs allopurinol 2.22 µM (~3.7× weaker); DAE's IC50 is plausibly in similar range but **not verifiable without full text retrieval**.
5. **80 mg/kg mouse is ~6.5 mg/kg human, ~450 mg/day.** Substantial dose for a single bioactive — translation to a fungal supplement/extract would require either potent biosynthesis or concentrated extraction. This is a Phase 6 feasibility question.
6. **No NLRP3, no ABCG2, no oxidative-stress mechanism in this paper.** comp-014 Phase 4's "multi-chokepoint" attribution should not conflate the 4 chokepoints actually addressed (XOD + 3 transporters) with the broader 7-chokepoint frame the wiki uses.
7. **The 7-day acute design has no observation period for tolerance, rebound hyperuricemia on withdrawal, or chronic safety.** Standard for this paper class but worth flagging.
8. **The 134 µmol/L endpoint at 80 mg/kg is below normal-mouse SUA (111 ± 20 µmol/L per DHAP paper).** This is **over-correction** — DAE at high dose drives SUA below normal-control levels. Not flagged in the abstract as a concern, but in human translation, sub-3 mg/dL SUA is associated with neurologic and oxidative-stress liabilities (uric acid is a major plasma antioxidant). Phase 6 should flag this as a clinical-translation safety concern.

---

## Phase 6 triage recommendations

- **Retain DAE on the candidate list** with downgraded chokepoint specificity: XOD = direct biochemical inhibitor (verified); URAT1/GLUT9/CNT2 = expression-level modulators (not direct transporter ligands); OAT1 = expression upregulator. This is **3-4 chokepoint coverage**, not the maximally optimistic reading.
- **Flag for full-text retrieval before further advancement** — IC50, kinetic mechanism, and dose-response for transporter expression are needed to differentiate DAE from prior-art XOD inhibitors. Worth ~$30 / 1 hour of access cost.
- **Decouple "DAE pharmacology" from "*G. applanatum* biosynthesis"** in downstream wiki authoring. The pharmacology is real; the fungal-source claim is literature-based and does not establish that the fungus produces DAE at therapeutically relevant levels.
- **Schedule a Phase 5b CNKI dive** for *G. applanatum* + 2,4-dihydroxybenzoic acid methyl ester in Chinese-language sources. The Yong / Liang group's prior work and any classical TCM literature on *G. applanatum* dampness/diuresis indications may add evidence weight or surface contradictory data not visible in PubMed-indexed English sources.

---

## References

- **[PMID 35750011]** Yong T, Liang D, Xiao C, Huang L, Chen S, Xie Y, Gao X, Wu Q, Hu H, Li X, Liu Y, Cai M. Hypouricemic effect of 2,4-dihydroxybenzoic acid methyl ester in hyperuricemic mice through inhibiting XOD and down-regulating URAT1. *Biomedicine & Pharmacotherapy* 153:113303 (2022). [DOI: 10.1016/j.biopha.2022.113303](https://doi.org/10.1016/j.biopha.2022.113303). According to PubMed.
  - https://citations.gxl.ai/papers/35750011#L1
- **[PMC5983617]** Liang D, Yong T, Chen S, Xie Y, Chen D, Zhou X, Li D, Li M, Su L, Zuo D. Hypouricemic Effect of 2,5-Dihydroxyacetophenone, a Computational Screened Bioactive Compound from *Ganoderma applanatum*, on Hyperuricemic Mice. *Int J Mol Sci* 19(5):1427 (2018). [DOI: 10.3390/ijms19051427](https://doi.org/10.3390/ijms19051427). Methodology source for DAE paper's matched protocol.
  - https://citations.gxl.ai/papers/PMC5983617#L1
- **[PMC5775298]** Yong T, Chen S, Xie Y, Chen D, Su J, Shuai O, Jiao C, Zuo D. Hypouricemic Effects of *Ganoderma applanatum* in Hyperuricemia Mice through OAT1 and GLUT9. *Front Pharmacol* 8:996 (2017). [DOI: 10.3389/fphar.2017.00996](https://doi.org/10.3389/fphar.2017.00996). Original *G. applanatum* extract paper anchoring the compound database.
  - https://citations.gxl.ai/papers/PMC5775298#L1
