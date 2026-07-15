---
title: "Lit scan — Houttuynia cordata polysaccharide fraction structure→directionality (pro- vs anti-inflammatory) for the MSU-NLRP3 gout screen §1.30"
date: 2026-07-14
tags: [lit-scan, houttuynia, polysaccharide, homogalacturonan, rg-i, tlr4, complement, nlrp3, msu, gout, structure-activity, safety-caution, multilingual]
scope: Does the published literature resolve the HCP fraction-directionality problem well enough to pick Arm A for wet-lab §1.30 and set a pro-inflammatory-directionality safety caution, before spending $2K?
status: complete — reported to Brian; NOT propagated to wiki or validation-experiments.md (report-only scan; propagation done in main session after review)
sources_home: operations/houttuynia-polysaccharide-structure-activity-2026-07-14/
---

# Does the literature resolve the Houttuynia polysaccharide fraction-directionality problem before we spend $2K on §1.30?

**Question.** §1.30 is the wet-lab macrophage screen: "does Houttuynia suppress MSU-induced IL-1β, and does sourcing matter?" Before committing $2K we need (a) the right **Arm A** material to test, and (b) whether to attach a **pro-inflammatory-directionality safety caution**. The unresolved node (walk item 7): the *purified* HCP-2 fraction is **pro-inflammatory** on naïve cells while crude/other fractions are **anti-inflammatory** in disease models. Which structural feature predicts direction, and what does a commercial capsule actually contain?

**Method.** bio-research PubMed MCP (English primary sources, full-text where PMC-available, every load-bearing number grep-verified against primary source). East-Asian corpus via `local_curl_fetch()` (CQVIP carried it; WanFang/Baidu/CNKI bot-walled — see dogfood note). Two-model translation cross-check (Claude=Model A, DeepSeek=Model B) on the 2 load-bearing zh sources — both full agreement. No wiki edits, no commit.

---

## Fraction catalog

Direction key: **PRO** = stimulates inflammatory cytokines; **ANTI** = suppresses. Context: **naïve** = no second stimulus; **disease** = LPS/viral/complement challenge.

| Fraction | Group / source | MW | Monosaccharide comp. | Backbone type | Direction | Assay context | Receptor / target |
|---|---|---|---|---|---|---|---|
| **HCP-2** | CUHK Hong Kong — Cheng, *Carbohydr Polym* 2014, PMID 24528726 | **60 kDa** | ~pure galacturonic acid | **Homogalacturonan** — linear 1,4-α-D-GalA, partial 6-O-methyl-ester + 2-O-acetyl | **PRO** (↑IL-1β 0.1–50 µg/mL; ↑TNF-α, MIP-1α/β, RANTES) | **naïve human PBMCs** | **TLR-4** (LPS-RS blocks dose-dependently) |
| **CHCP** (crude) | Fudan/Chen Daofeng — Lu, *Acta Pharm Sin B* 2018, PMID 29719782 | 1000–5000 kDa (polydisperse) | Glc:Gal:Ara:Rha 3.40:2.14:1.17:1 (+tr Man,Xyl); uronic acid 36.7% | Hetero (mixed HG + RG-I) | **ANTI** / anti-complement | two-hit ALI + LPS fever (rat, **disease**) | **complement C3 + C4** (partial C5); CH50 0.092, AP50 0.209 mg/mL |
| **HCPM** | Fudan/Chen Daofeng — Zhou, *Int J Biol Macromol* 2022, PMID 36252625 | **19.1 kDa** | acidic heteropolysaccharide | **RG-I-type** — backbone 1,3,6-β-Manp / 1,4-α-GalpA / 1,2- & 1,2,4-α-Rhap; glucan+arabinan+galactan branches | **ANTI** / anti-complement | H1N1 ALI (mouse, **disease**) | complement, **CH50 254.1 µg/mL** |
| **HCPM** (same fraction, gout-adjacent readout) | Fudan/Chen Daofeng — Li, *Acta Pharm Sin B* 2025, PMC12254813 / PMID 40654358 | 19.1 kDa | (as above) | RG-I | **ANTI** — suppresses intestinal **NLRP3 / cleaved-caspase-1 / IL-1β / IL-18** | H1N1+MRSA coinfection (mouse, **disease**); oral, gut-acting | intestinal complement **C3a/C5a → NLRP3**; Treg/Th17 |
| **HC-PS1** | Fudan/Chen Daofeng — Lu, *Planta Med* 2019, PMID 31250410 | **274.5 kDa** | 8 sugars (Rha,Ara,Man,Glc,GlcA,Gal,GalA,Xyl) | highly-branched RG-I | **ANTI** (anti-complement, IC50 0.272–0.318 mg/mL) | in vitro complement | **C2, C4, C5** |
| **HC-PS3** | same | **216.4 kDa** | same 8 sugars | highly-branched RG-I | **ANTI** | in vitro | **C2, C4, C5** |
| **HBHP-3** | Hefei UT — Zou, *Int J Biol Macromol* 2022, PMID 35533845 | **397.4 kDa** | Rha:Ara:Glc:Gal:GalA 16.0:12.6:4.6:18.1:15.6 | **RG-I pectin** — backbone →2)-α-Rhap-(1→ / →4)-α-GalpA-(1→ / →4)-β-Galp-(1→; Ara/Glc/Gal branches at O-4 of Rha | **ANTI** (↓NO, ↓pro-inflam cytokine mRNA; ↓NF-κB p65/IκBα) | macrophages (LPS-stim) | NF-κB |
| **HCP** (crude, unspecified) | Wuhan — Yu, *Biomedicines* 2026, PMC12937656 / PMID 41751332 | not characterized | — | crude | **ANTI** (M1→M2; ↓IL-1β, TNF-α, IL-6) | hepatic IRI (mouse, **disease**) | **TLR4/MD-2** (docking + **TAK-242 reversal**) |
| **HCP** (crude) | Fudan/Chen Daofeng — Xu, *J Ethnopharmacol* 2015, PMID 26190353 | not characterized | — | crude | **BIDIRECTIONAL** — pro-inflam alone (naïve); anti-inflam vs LPS | naïve + LPS-ALI (mouse) | ↓TLR4, ↓complement; blocks C5a-macrophage migration |
| **HBHP / CHHP / DAHP / CAHP** | zh (CQVIP 2021); HBHP→HBHP-3 (397.4 kDa)+HBHP-4 (616.7 kDa) | 4 fractions | HBHP/CHHP: Rha-Ara-Glc-Gal; DAHP/CAHP: Ara-Xyl-Glc-Gal; uronic acid 29.6→11.6% | acidic pectic (RG-I-ish) | **ANTI** (in vitro) | in vitro | (NF-κB implied) |
| **Leaf vs stem vs rhizome PS** | zh (CQVIP 2024) | 4.11×10⁴–1.20×10⁶ Da | acidic; Glc/Gal/Ara/Rha/GalA +minor Fuc/Man/Xyl/GlcA | acidic pectic; **leaf = more methyl-ester/acetyl, no triple helix**; stem/rhizome triple-helix | (antioxidant / α-glucosidase, not inflammation) | in vitro | — |

Two-model-verified zh additions (DeepSeek Model-B agreed with Model A on all numbers): the HBHP/CHHP/DAHP/CAHP fraction series, and HBHP-3 = 397.4 kDa (independently matching the English Zou 2022 paper).

---

## Structure→directionality rule

The literature supports a **two-axis** model. Both axes point the same way for our screen, **but they are confounded** — no single paper crosses them cleanly.

**Axis 1 — STRUCTURE.**
- **Homogalacturonan** ("smooth" linear methyl-esterified 1,4-α-GalA, ~60 kDa; HCP-2) → **TLR4/MD-2 agonist → PRO-inflammatory** (↑IL-1β on naïve monocytes; LPS-RS-blockable).
- **RG-I / branched "hairy" heteropolysaccharide** (Rha-rich backbone + Ara/Gal branches; HCPM, HC-PS1/3, HBHP-3, CHCP) → **anti-complement** (blocks C3/C4/C2/C5) **→ ANTI-inflammatory**. The lowest-MW acidic RG-I (**HCPM 19.1 kDa**) is the most potent anti-complement *and* the only fraction with a direct NLRP3/caspase-1/IL-1β/IL-18-suppression readout (Li 2025).

**Axis 2 — CONTEXT** (stronger, single-material evidence).
- **Naïve** (no second stimulus): HCP/HG is **PRO** — Cheng 2014 (HCP-2 on naïve PBMCs) and Xu 2015 ("HCP alone augmented secretion of some pro-inflammatory cytokines").
- **Disease/challenge**: HCP/HCPM is **ANTI** — every disease-model paper (LPS-ALI, viral, fever, colitis, HIRI, coinfection).

**The confound (the honest core of the problem).** HCP-2 (homogalacturonan) was tested **only** naïve; the RG-I fractions were tested **only** in disease models. So "HG is intrinsically pro-inflammatory" cannot be cleanly separated from "naïve context reads pro-inflammatory." Worse, the **same receptor gives opposite outcomes**: pure-HG HCP-2 activates TLR4/MD-2 → pro-inflammatory on naïve PBMCs (Cheng 2014), yet crude HCP also engages TLR4/MD-2 (docking + TAK-242 reversal) but drives **M2 reprogramming → anti-inflammatory** in hepatic IRI (Yu 2026). TLR4 engagement is therefore **necessary but not sufficient** to predict direction — structure (pure HG vs crude/RG-I) and disease context both move the outcome. The 2025 Phytomedicine SAR review (PMID 39899978) concedes the field's own position: structure–activity correlation for HCP "remain[s] relatively underexplored."

---

## Commercial-product read

- **No published COA / composition data exists for any commercial Houttuynia capsule** (checked English PubMed + Chinese CQVIP/WanFang). The closest are patent extracts: crude "total polysaccharide," ~3.65% yield, >70% polysaccharide content — i.e. **crude whole-herb extract**, not a defined HCPM.
- A commercial capsule therefore diverges from HCPM toward **crude**: a **mixture** of homogalacturonan (the TLR4-agonist PRO fraction) + RG-I (anti-complement ANTI fractions) + non-polysaccharide actives (flavonoids/quercitrin, alkaloids, sodium houttuyfonate). The HG:RG-I ratio — hence the TLR4-agonist load — is **not standardized** and varies by plant part (leaf carries more methyl-esterified HG per the 2024 zh part-comparison), extraction solvent, and processing.
- Net: a capsule will **not** behave like purified HCPM. It carries an uncharacterized, source-variable homogalacturonan/TLR4-agonist fraction.

---

## Verdict

| Sub-question | Verdict |
|---|---|
| **Does the literature resolve Arm A selection?** | **Partially.** It identifies the mechanistically-cleanest anti-inflammatory / NLRP3-suppressive candidate (**purified HCPM, 19.1 kDa acidic RG-I** — Li 2025 is the only direct NLRP3/IL-1β/IL-18 evidence). It does **not** resolve the consumer-relevant arm, because commercial capsules are uncharacterized crude extract, and **no fraction has ever been tested in an MSU/urate/gout model** (see gap). |
| **Is a pro-inflammatory-directionality safety caution warranted?** | **Yes — mechanism-grounded, not hypothetical.** Purified homogalacturonan (HCP-2) is a **direct TLR4/MD-2 agonist that raises IL-1β in naïve monocytes/PBMCs** (Cheng 2014). In an MSU screen, MSU supplies signal-2 (NLRP3 assembly); if the Houttuynia material supplies signal-1 (TLR4→NF-κB→pro-IL-1β priming), an HG-rich or crude extract could **amplify IL-1β rather than suppress it** — the opposite of the intended readout. The risk is sharpest if the MSU protocol has **no separate LPS priming step**, because the extract's own TLR4 priming would then be unopposed and mis-attributable. Xu 2015's same-material bidirectionality is the empirical proof the sign can flip. |

**Read for Arm-A design (decision is the main session's / Brian's):**
- If Arm A tests the *mechanism* ("can a defined HC polysaccharide suppress MSU-IL-1β"): use **purified HCPM (19.1 kDa RG-I)** — best mechanistic case, directly NLRP3-linked. But it is not a consumer product.
- If Arm A tests the *consumer question* ("does taking Houttuynia capsules help"): test the **commercial capsule extract**, but on the same plate run **crude-HCP and purified-HCPM comparators** and include a **pro-IL-1β / TLR4-priming readout** (extract-alone, no MSU) — not just a suppression readout — to catch the amplification risk. **Sourcing matters** precisely because the HG:RG-I (TLR4-agonist) ratio is unstandardized; two products can land on opposite sides of the directionality line.
- A defensible design runs **both** as a directionality gate: purified-HCPM (expected ANTI) vs crude/capsule (uncertain), each ± a priming-only control.

---

## Biggest evidence gap

**No Houttuynia cordata polysaccharide fraction has ever been tested in an MSU / urate / gout / hyperuricemia model** — confirmed in **both** English PubMed and Chinese CQVIP (the zh "痛风/尿酸 + 鱼腥草" hits are whole-herb topical 外敷 nursing and a 15-herb hyperuricemia *ferment* in which Houttuynia is one minor ingredient — **zero** polysaccharide-fraction gout papers; two-model-verified). Every directionality inference for the gout context is extrapolated from LPS/viral/complement disease models. Secondary gaps: (1) the HG-vs-RG-I structural axis and the naïve-vs-disease context axis are **confounded** — no head-to-head same-structure naïve-vs-challenge experiment exists; (2) **no compositional/COA data** links any commercial capsule to a defined fraction. §1.30 would be the **first** MSU-context test of any HC polysaccharide — which is exactly why the directionality safety caution and a priming-only control arm are load-bearing.

---

## Queries run
Full log: `operations/.../outputs/query-log.md`. Plan: `inputs/query-strategy.json` (frame audit `adequate`; EN + zh/ja/ko, 272 queries). PubMed: HC polysaccharide × {structure/anti-inflammatory, complement, TLR4/macrophage} + targeted PMID→PMC full-text. East-Asian `local_curl_fetch`: **CQVIP OK** (real SSR, 3 queries incl. gout/MSU); WanFang reached but JS-shell; **Baidu = CAPTCHA wall** (not bypassed); **CNKI + ChinaXiv failed at curl layer**; J-STAGE probed (no zh-equivalent dokudami polysaccharide-fraction hits — field is Chinese-group dominated). Two-model translation (DeepSeek Model-B) on 2 load-bearing zh sources → full agreement.

## Primary sources (PMID / DOI)
- Cheng 2014 — HCP-2 60 kDa homogalacturonan, PRO-inflammatory (naïve PBMC), TLR-4 — PMID 24528726, [DOI](https://doi.org/10.1016/j.carbpol.2013.12.048)
- Xu 2015 — crude HCP, bidirectional (pro alone / anti vs LPS), TLR4+complement — PMID 26190353, PMC7127486, [DOI](https://doi.org/10.1016/j.jep.2015.07.015)
- Lu 2018 — CHCP crude, anti-complement C3+C4, two-hit ALI + fever — PMID 29719782, PMC5925397, [DOI](https://doi.org/10.1016/j.apsb.2017.11.003)
- Lu 2019 — HC-PS1 274.5 kDa / HC-PS3 216.4 kDa RG-I, anti-complement C2/C4/C5 — PMID 31250410, [DOI](https://doi.org/10.1055/a-0955-7841)
- Zhou 2022 — **HCPM 19.1 kDa** acidic RG-I, anti-complement CH50 254.1 µg/mL, H1N1 ALI — PMID 36252625, [DOI](https://doi.org/10.1016/j.ijbiomac.2022.10.027)
- Zou 2022 — HBHP-3 397.4 kDa RG-I pectin, anti-inflammatory (NF-κB) — PMID 35533845, [DOI](https://doi.org/10.1016/j.ijbiomac.2022.05.016)
- Cen 2022 — crude HCPs, DSS colitis, anti-inflammatory (TLR4/NF-κB, Th17/Treg) — PMID 36549805, [DOI](https://doi.org/10.1016/S1875-5364(22)60220-6)
- Li 2025 — **HCPM 19.1 kDa**, suppresses intestinal NLRP3/caspase-1/IL-1β/IL-18, H1N1+MRSA — PMID 40654358, PMC12254813, [DOI](https://doi.org/10.1016/j.apsb.2025.04.008)
- Yu 2026 — crude HCP, TLR4/MD-2 docking + TAK-242 reversal, M1→M2, hepatic IRI — PMID 41751332, PMC12937656, [DOI](https://doi.org/10.3390/biomedicines14020433)
- Gao 2025 — SAR review ("SAR remains underexplored") — PMID 39899978, [DOI](https://doi.org/10.1016/j.phymed.2025.156436)
- Liu 2024 — HCPs review — PMID 39218180, [DOI](https://doi.org/10.1016/j.ijbiomac.2024.135230)

Non-English (read directly; two-model-verified):
- CQVIP 2021 — 《鱼腥草多糖结构表征及抗炎活性研究》(Structural characterization and anti-inflammatory activity of Houttuynia cordata polysaccharides) — sequential-extraction fractions HBHP/CHHP/DAHP/CAHP; HBHP→HBHP-3 397.4 kDa/HBHP-4 616.7 kDa. (zh; CQVIP full-text via local_curl)
- CQVIP 2024 — 《鱼腥草不同部位多糖结构与生物活性差异》(Structure–activity differences of polysaccharides from different Houttuynia cordata parts) — leaf vs stem vs rhizome; triple-helix + methyl-ester/acetyl differences. (zh)
- CQVIP patent — 《适用于高尿酸及痛风人群的药食同源酵素》(A medicine-food-homology ferment for hyperuricemia/gout populations) — 15-herb microbial ferment; Houttuynia = 1 ingredient; **not** a polysaccharide fraction. (zh; the only "HC + gout" signal, confirms the gap)

## Attribution
Based on articles retrieved from PubMed (bio-research MCP) and, for the Chinese-language sources, CQVIP full text fetched via local curl. Load-bearing numbers grep-verified against each primary source before entry.
