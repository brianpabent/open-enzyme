# comp-013: TCM Gout Compound Triage — Summary

**Date:** 2026-05-06
**Framework:** comp-004 (gut-conc + Hill equation occupancy) + comp-007 (potency × selectivity × gut-enrichment composite)
**Compounds evaluated:** 9
**Interpretive wiki page:** [`wiki/tcm-gout-compound-triage-computational.md`](../../wiki/tcm-gout-compound-triage-computational.md)

## Verdict counts

- **MECHANISM UNCLEAR**: 4
- **GUT-LUMINAL VIABLE**: 4
- **MODERATE / VIABLE-WITH-DOSE-CAVEAT**: 1

## Per-compound triage table

| Rank | Compound | TCM source | Verdict | Composite | Confidence | Best on-target IC50 (nM) | Mechanism site |
|---|---|---|---|---|---|---|---|
| 1 | **Luteolin** | Lonicera japonica (金银花 / Jin Yin Hua); also Achyranthes bidentata (component of Si Miao San) | **GUT-LUMINAL VIABLE** | 0.0071 | HIGH | 550 | gut-luminal AND systemic (limited) |
| 2 | **Astilbin** | Smilax glabra (土茯苓 / Tu Fu Ling) | **GUT-LUMINAL VIABLE** | 0.0000 | MODERATE | N/A | gut-luminal AND systemic |
| 3 | **Rhein** | Rheum officinale (大黄 / Da Huang) | **MODERATE / VIABLE-WITH-DOSE-CAVEAT** | 0.0000 | MODERATE | N/A | systemic |
| 4 | **Emodin** | Rheum officinale (大黄 / Da Huang); also Polygonum cuspidatum (虎杖) | **GUT-LUMINAL VIABLE** | 0.0000 | HIGH | N/A | gut-luminal AND systemic |
| 5 | **Aucubin** | Plantago asiatica (车前子 / Che Qian Zi) | **MECHANISM UNCLEAR** | 0.0000 | LOW | N/A | gut-luminal |
| 6 | **Berberine** | Coptis chinensis (黄连 / Huang Lian); also Phellodendron amurense (黄柏 / Huang Bai) | **GUT-LUMINAL VIABLE** | 0.0000 | HIGH | N/A | gut-luminal AND systemic (low) |
| 7 | **Cylindrin** | Imperata cylindrica (白茅根 / Bai Mao Gen) | **MECHANISM UNCLEAR** | 0.0000 | LOW | N/A | gut-luminal |
| 8 | **Chlorogenic acid** | Lonicera japonica (金银花 / Jin Yin Hua); also coffee, many plants | **MECHANISM UNCLEAR** | 0.0000 | MODERATE | N/A | systemic |
| 9 | **Atractylenolide_I** | Atractylodes macrocephala / lancea (苍术 / Cang Zhu — Si Miao San component) | **MECHANISM UNCLEAR** | 0.0000 | LOW | N/A | systemic (anti-inflammatory) |

## Per-compound rationale

### Rank 1: Luteolin — GUT-LUMINAL VIABLE

- **TCM source:** Lonicera japonica (金银花 / Jin Yin Hua); also Achyranthes bidentata (component of Si Miao San)
- **ChEMBL ID:** CHEMBL151
- **Mechanism site:** gut-luminal AND systemic (limited)
- **Mechanism note:** ChEMBL XO IC50=550 nM (best, J Nat Prod 1998), 7,800 nM (Bioorg Med Chem Lett 2015), Ki=2,900 nM (Eur J Med Chem 2014). ABCG2 IC50=8,900 nM (J Nat Prod 2011). CYP1B1 IC50=79 nM. URAT1 expression downregulation in mouse PO model 3-10 mg/kg per PMC9635963 ref 45 (Lin 2018 PMID 29519319).
- **Dose:** 100 mg; **BA:** 5.0%; **MW:** 286.24 g/mol
- **Gut lumen conc:** 174.68 µM (solubility-capped: True)
- **Plasma Cmax:** 0.25 µM
- **Best on-target IC50:** 550 nM
- **Selectivity (on/off):** 0.14 (on/off ratio = 0.14)
- **Gut-enrichment score:** 0.500 (mixed gut + systemic: balanced)
- **Composite score:** 0.0071
- **Confidence:** HIGH
- **Triage rationale:** Gut-targeted mechanism + low BA (5.0%) concentrates compound at gut lumen; animal-model evidence supports in vivo activity. Dose translation to human achievable.

Per-target occupancy:

| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |
|---|---|---|---|---|---|---|---|
| Xanthine dehydrogenase/oxidase | plasma | 550 | 250 | 0.45 | 31% | LOW | In Vitro biochemical (multi-lab confirmation) |
| ABCG2 | gut | 8,900 | 174,679 | 19.63 | 95% | VERY_HIGH | In Vitro cell-based |
| Cytochrome P450 1B1 (CYP1B1) | plasma | 79 | 250 | 3.16 | 76% | HIGH | In Vitro biochemical |

### Rank 2: Astilbin — GUT-LUMINAL VIABLE

- **TCM source:** Smilax glabra (土茯苓 / Tu Fu Ling)
- **ChEMBL ID:** NOT IN ChEMBL — primary literature only
- **Mechanism site:** gut-luminal AND systemic
- **Mechanism note:** Astilbin reduces hyperuricemia in mouse model via URAT1 expression downregulation (renal) per PMC9635963 §flavanonol; XO inhibition demonstrated in vitro per PMID 34885887. Systemic via aglycone (taxifolin) post-microbiome conversion; gut-luminal effect plausible.
- **Dose:** 250 mg; **BA:** 5.0%; **MW:** 450.39 g/mol
- **Gut lumen conc:** 444.06 µM (solubility-capped: True)
- **Plasma Cmax:** 0.396 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.500 (mixed gut + systemic: balanced)
- **Composite score:** 0.0000
- **Confidence:** MODERATE
- **Triage rationale:** Gut-targeted mechanism + low BA (5.0%) concentrates compound at gut lumen; animal-model evidence supports in vivo activity. Dose translation to human achievable.

Per-target occupancy:

_No target IC50 data — see ChEMBL gap notes in inputs/bioactivity_data.json_

### Rank 3: Rhein — MODERATE / VIABLE-WITH-DOSE-CAVEAT

- **TCM source:** Rheum officinale (大黄 / Da Huang)
- **ChEMBL ID:** CHEMBL418068
- **Mechanism site:** systemic
- **Mechanism note:** Rhein claimed URAT1 inhibitor in TCM literature (mechanism extrapolation from in vivo rat data). NO ChEMBL bioactivity vs URAT1, ABCG2, XO, or NLRP3 (verified empty). Most-potent ChEMBL bioactivity: AChE IC50=637 nM (Electrophorus electricus), HSP90 IC50=3,339 nM, FTO IC50=2,180 nM. Off-target enriched.
- **Dose:** 50 mg; **BA:** 50.0%; **MW:** 284.22 g/mol
- **Gut lumen conc:** 351.84 µM (solubility-capped: False)
- **Plasma Cmax:** 1.257 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.500 (systemic-only: high BA favorable)
- **Composite score:** 0.0000
- **Confidence:** MODERATE
- **Triage rationale:** Systemic mechanism with achievable plasma Cmax in MODERATE range; dose escalation or formulation enhancement required for HIGH occupancy.

Per-target occupancy:

| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |
|---|---|---|---|---|---|---|---|
| Acetylcholinesterase (off-target) | plasma | 637 | 1,257 | 1.97 | 66% | MODERATE | In Vitro biochemical |
| FTO (alpha-ketoglutarate dioxygenase) | plasma | 2,180 | 1,257 | 0.58 | 37% | MODERATE | In Vitro biochemical |

### Rank 4: Emodin — GUT-LUMINAL VIABLE

- **TCM source:** Rheum officinale (大黄 / Da Huang); also Polygonum cuspidatum (虎杖)
- **ChEMBL ID:** CHEMBL289277
- **Mechanism site:** gut-luminal AND systemic
- **Mechanism note:** PMC10304951 (Hou 2023): Emodin 30/50 mg/kg in PO rat model significantly lowered SUA via increased FEUA. Mechanism is NOT XO inhibition (XO activity unchanged in study). Likely renal urate transporter modulation. NO ChEMBL bioactivity vs URAT1/ABCG2/XO/NLRP3. Most-potent ChEMBL: CK2α IC50=890 nM, ER-α IC50=2,700 nM.
- **Dose:** 50 mg; **BA:** 3.0%; **MW:** 270.24 g/mol
- **Gut lumen conc:** 18.5 µM (solubility-capped: True)
- **Plasma Cmax:** 0.079 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.500 (mixed gut + systemic: balanced)
- **Composite score:** 0.0000
- **Confidence:** HIGH
- **Triage rationale:** Gut-targeted mechanism + low BA (3.0%) concentrates compound at gut lumen; animal-model evidence supports in vivo activity. Dose translation to human achievable.

Per-target occupancy:

| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |
|---|---|---|---|---|---|---|---|
| Casein kinase II alpha (off-target) | plasma | 890 | 79 | 0.09 | 8% | LOW | In Vitro biochemical |
| Estrogen receptor alpha (off-target) | plasma | 2,700 | 79 | 0.03 | 3% | LOW | In Vitro biochemical |

### Rank 5: Aucubin — MECHANISM UNCLEAR

- **TCM source:** Plantago asiatica (车前子 / Che Qian Zi)
- **ChEMBL ID:** NOT IN ChEMBL — primary literature only
- **Mechanism site:** gut-luminal
- **Mechanism note:** Aucubin/Plantago asiatica claimed uricosuric in classical TCM. NO ChEMBL bioactivity for aucubin against any target. Mechanism extrapolation only — diuretic effect plausible via aquaporin or RAS modulation but not gout-specific.
- **Dose:** 100 mg; **BA:** 5.0%; **MW:** 346.33 g/mol
- **Gut lumen conc:** 1097.22 µM (solubility-capped: False)
- **Plasma Cmax:** 0.206 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.950 (gut-luminal-only: low BA favorable)
- **Composite score:** 0.0000
- **Confidence:** LOW
- **Triage rationale:** No ChEMBL bioactivity for any target; no published in vivo dose-response data found in the literature reviewed.

Per-target occupancy:

_No target IC50 data — see ChEMBL gap notes in inputs/bioactivity_data.json_

### Rank 6: Berberine — GUT-LUMINAL VIABLE

- **TCM source:** Coptis chinensis (黄连 / Huang Lian); also Phellodendron amurense (黄柏 / Huang Bai)
- **ChEMBL ID:** CHEMBL295124
- **Mechanism site:** gut-luminal AND systemic (low)
- **Mechanism note:** Berberine 6.25-25 mg/kg in mouse PO model inhibits URAT1 expression, promotes urate excretion (PMC9635963 ref 70-71). Most-potent ChEMBL bioactivity: TDO IC50=30 nM (verified), CYP1B1 IC50=94 nM, AChE IC50=100 nM, IDO1 IC50=260 nM. NO direct URAT1/ABCG2/XO IC50 in ChEMBL. NLRP3 effect via NF-κB modulation (indirect).
- **Dose:** 500 mg; **BA:** 0.5%; **MW:** 336.37 g/mol
- **Gut lumen conc:** 1486.46 µM (solubility-capped: True)
- **Plasma Cmax:** 0.106 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.500 (mixed gut + systemic: balanced)
- **Composite score:** 0.0000
- **Confidence:** HIGH
- **Triage rationale:** Gut-targeted mechanism + low BA (0.5%) concentrates compound at gut lumen; animal-model evidence supports in vivo activity. Dose translation to human achievable.

Per-target occupancy:

| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |
|---|---|---|---|---|---|---|---|
| Tryptophan 2,3-dioxygenase (TDO) | plasma | 30 | 106 | 3.54 | 78% | HIGH | In Vitro biochemical |
| Cytochrome P450 1B1 (CYP1B1) | plasma | 94 | 106 | 1.13 | 53% | MODERATE | In Vitro biochemical |

### Rank 7: Cylindrin — MECHANISM UNCLEAR

- **TCM source:** Imperata cylindrica (白茅根 / Bai Mao Gen)
- **ChEMBL ID:** NOT IN ChEMBL — primary literature only
- **Mechanism site:** gut-luminal
- **Mechanism note:** Imperata cylindrica claimed diuretic/uricosuric in classical TCM. NO ChEMBL bioactivity. Mechanism unknown — likely diuretic via aquaporin or sodium handling, not gout-specific.
- **Dose:** 50 mg; **BA:** 2.0%; **MW:** 426.72 g/mol
- **Gut lumen conc:** 2.34 µM (solubility-capped: True)
- **Plasma Cmax:** 0.033 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.980 (gut-luminal-only: low BA favorable)
- **Composite score:** 0.0000
- **Confidence:** LOW
- **Triage rationale:** No ChEMBL bioactivity for any target; no published in vivo dose-response data found in the literature reviewed.

Per-target occupancy:

_No target IC50 data — see ChEMBL gap notes in inputs/bioactivity_data.json_

### Rank 8: Chlorogenic acid — MECHANISM UNCLEAR

- **TCM source:** Lonicera japonica (金银花 / Jin Yin Hua); also coffee, many plants
- **ChEMBL ID:** CHEMBL284616
- **Mechanism site:** systemic
- **Mechanism note:** ChEMBL most-potent: PTP1B IC50=100 nM, AKR1B1 IC50=300 nM, ONOO scavenging IC50=520 nM. NO direct URAT1/ABCG2/XO IC50. Mechanism for gout via anti-inflammatory and antioxidant pathways — Mechanistic Extrapolation.
- **Dose:** 200 mg; **BA:** 33.0%; **MW:** 354.31 g/mol
- **Gut lumen conc:** 1512.8 µM (solubility-capped: False)
- **Plasma Cmax:** 2.661 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.330 (systemic-only: high BA favorable)
- **Composite score:** 0.0000
- **Confidence:** MODERATE
- **Triage rationale:** ChEMBL data present but no clear connection to gout-relevant target at achievable concentration; insufficient to triage with confidence.

Per-target occupancy:

| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |
|---|---|---|---|---|---|---|---|
| PTP1B (PTPN1) | plasma | 100 | 2,661 | 26.61 | 96% | VERY_HIGH | In Vitro biochemical |
| Aldo-keto reductase 1B1 (AKR1B1) | plasma | 300 | 2,661 | 8.87 | 90% | VERY_HIGH | In Vitro biochemical |

### Rank 9: Atractylenolide_I — MECHANISM UNCLEAR

- **TCM source:** Atractylodes macrocephala / lancea (苍术 / Cang Zhu — Si Miao San component)
- **ChEMBL ID:** NOT IN ChEMBL — primary literature only
- **Mechanism site:** systemic (anti-inflammatory)
- **Mechanism note:** Component of Si Miao San (Cang Zhu) — anti-inflammatory in TCM gout formulas. NO ChEMBL bioactivity. HDAC inhibition claim from Brian's brief is speculative; not in ChEMBL or comp-007 corpus. Si Miao San efficacy demonstrated as formula (PMC5360963 meta-analysis: −90.62 µmol/L SUA reduction) but cannot attribute to single component.
- **Dose:** 30 mg; **BA:** 10.0%; **MW:** 230.3 g/mol
- **Gut lumen conc:** 43.42 µM (solubility-capped: True)
- **Plasma Cmax:** 0.186 µM
- **Best on-target IC50:** N/A (ChEMBL gap)
- **Selectivity (on/off):** None (no on-target IC50)
- **Gut-enrichment score:** 0.100 (systemic-only: high BA favorable)
- **Composite score:** 0.0000
- **Confidence:** LOW
- **Triage rationale:** No ChEMBL bioactivity for any target; no published in vivo dose-response data found in the literature reviewed.

Per-target occupancy:

_No target IC50 data — see ChEMBL gap notes in inputs/bioactivity_data.json_

## Formula-level evidence (Si Miao San / Modified Simiao Decoction)

### Si Miao San / Modified Simiao Decoction (MSD)
- **Components:** Phellodendron (Huang Bai), Atractylodes (Cang Zhu), Achyranthes bidentata (Niu Xi), Coix lacryma-jobi (Yi Yi Ren)
- **Clinical evidence:** 24 RCTs systematic review + meta-analysis (Liu et al 2017, PMC5360963, doi:10.1155/2017/6037037).
- **Quantitative finding:** MSD monotherapy vs anti-inflammation medications: SUA reduction = -90.62 µmol/L (95% CI [-128.38, -52.86]), p<0.00001. MSD vs urate-lowering therapies: SUA -91.43 µmol/L (95% CI [-122.38, -60.49]), p<0.00001. MSD added to combined therapy: additive -40.30 µmol/L (95% CI [-74.24, -6.36]), p=0.02. AEs significantly fewer (OR=0.08).
- **Verification:** Paperclip grep /papers/PMC5360963/content.lines line 7 — abstract verbatim: 'MSD monotherapy significantly lowered serum uric acid (p<0.00001, mean difference = −90.62, and 95% CI [−128.38, −52.86]; p<0.00001, mean difference = −91.43, and 95% CI [−122.38, −60.49]; p=0.02, mean difference = −40.30, and 95% CI [−74.24, −6.36], resp.)'
- **Evidence level:** Clinical Trial (meta-analytic)
- **Limitation:** Authors note 'low methodological quality of the included trials' — heterogeneous formulations, blinding inconsistent, attribution to specific component impossible.

## Methodology adaptation notes (vs comp-004 and comp-007)

**comp-004 IC50 occupancy framework — direct application**
Same Hill equation n=1, same gut-conc model (dose × (1−BA) ÷ 250 mL, capped at intestinal solubility), same risk thresholds.

**comp-007 composite scoring — adapted**
Three changes from comp-007 (HDACi screen):
1. **Gut-enrichment is BIDIRECTIONAL.** comp-007's HDACi candidates all targeted Q141K-ABCG2 trafficking — a gut-mucosal target where low BA is uniformly favorable. TCM compounds split: some target gut-luminal (favorable for low BA), others target systemic urate transporters URAT1/XO/NLRP3 (UNFAVORABLE for low BA). The gut-enrichment score is now site-aware.
2. **Selectivity uses on/off-target ratio.** comp-007 used HDAC6/class-I ratio (avoiding cardiotoxicity). Here, selectivity = best gout-relevant on-target IC50 / best non-gout off-target IC50. Compounds with off-target hits more potent than the on-target hit get penalized.
3. **Animal-model evidence is admissible.** comp-007 ranked on biochemical IC50 only. For TCM compounds, ChEMBL coverage is so sparse that animal-model in vivo dose-response data has to count toward the verdict — explicitly tagged in evidence_level field.

**Honesty caveats**
- ChEMBL coverage of TCM compounds is poor: 5 of 9 candidates have NO ChEMBL entry at all.
- For compounds without ChEMBL bioactivity but with animal-model in vivo data, the composite score will be 0 (no on-target IC50). Verdict still uses animal data via the `assign_verdict` override.
- Plasma Cmax is a crude single-dose estimate using Vd ≈ 1 L/kg for polyphenols. Real Cmax depends on formulation, absorption rate, and clearance.
- Human dose translation from murine in vivo studies uses no formal allometric scaling; values are bounded estimates.