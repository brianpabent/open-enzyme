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
  - etc/chembl-cross-check.md
  - supplement-abcg2-antagonism-computational.md
  - food-grade-hdaci-screen-computational.md
  - computational-experiments.md
  - etc/manual-literature-mining.md
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

# TCM Gout Compound Triage — Computational Analysis (comp-013)

> **Frozen analysis archived to [`./etc/experiments/comp-013-tcm-gout-compound-triage/wiki-archive.md`](./etc/experiments/comp-013-tcm-gout-compound-triage/wiki-archive.md)** (409 lines).
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-013-tcm-gout-compound-triage/`.

**Question:** Which Traditional Chinese Medicine (TCM) compounds with documented gout indication are mechanistically viable when triaged via the comp-004 IC50 occupancy + comp-007 composite scoring frameworks?

**Where the analysis lives:**
- Full archived analysis: [`./etc/experiments/comp-013-tcm-gout-compound-triage/wiki-archive.md`](./etc/experiments/comp-013-tcm-gout-compound-triage/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-013-tcm-gout-compound-triage/`](./etc/experiments/comp-013-tcm-gout-compound-triage/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)

---

## Addendum — 2026-05-19 traditional-name re-scan corrections + additions

This addendum captures the **marker-correction batch** surfaced by the 2026-05-19 traditional-formula-name re-scans ([URAT1 rescan](../logs/urat1-classical-formula-rescan-2026-05-19.md), [XO rescan](../logs/xo-classical-formula-rescan-2026-05-19.md)). These are formula-anchored + species-anchored findings that the original comp-013 herb-by-herb query framing missed. Per [CLAUDE.md §"Global-multilingual research by default"](../CLAUDE.md), the discipline upgrade is to seed compound lists from **traditional formula composition + traditional pathology term** (e.g., 痛风 / 痹证 / 湿热痹) in addition to mechanism-name queries.

**1. Mangiferin → Zhi Mu / Anemarrhena asphodeloides (new tier-1 entry).** Mangiferin (CHEMBL3611008) is the cardinal anti-hyperuricemia active in *A. asphodeloides*. Niu 2015 + supporting series: dual-pathway URAT1 down-regulation + AQP2 modulation. Anemarrhena is a cardinal herb of Bai Hu Jia Gui Zhi Tang (BHGZ; the canonical gout-active formula in the modern Chinese RCT literature). **Tier-1 promotion based on (a) mechanism, (b) BHGZ RCT context, (c) ChEMBL coverage of mangiferin.** Adds to the comp-013 URAT1 row alongside cordycepin and astilbin. (In Vitro + Animal Model; source: urat1-classical-formula-rescan-2026-05-19.md)

**2. Bai Hu Jia Gui Zhi Tang (BHGZ) — ChiCTR1900024974 RCT scope.** White Tiger Plus Cinnamon Branch decoction (Anemarrhena + gypsum + cinnamon + rice + licorice) is the canonical TCM gout formula in the modern Chinese RCT literature. ChiCTR1900024974 is a registered RCT (protocol PMC9013133, 2022); outcomes paper pending. 91% pilot effectiveness in the protocol's prior-series basis is **uncontrolled** — wait for the RCT outcomes paper before promoting beyond mechanism-tier. (Clinical Trial protocol; outcomes pending. Source: urat1-classical-formula-rescan-2026-05-19.md)

**3. Coix lacryma-jobi (Yi Yi Ren) — major mechanism upgrade.** Original comp-013 entry attributed activity to "atractylenolide I = MECHANISM UNCLEAR". The 2026-05-19 re-scan replaces this with **Coix seed oil four-transporter mechanism** (URAT1 + GLUT9 + OAT1 + ABCG2) at 73-87% SUA reduction in HUA rodent models (PMC12114407). This is a major upgrade — four-transporter coverage from a single GRAS food-grade input. (Animal Model; source: urat1-classical-formula-rescan-2026-05-19.md)

**4. Plantago seed (Che Qian Zi) — attribution correction.** Original comp-013 attributed Plantago activity to aucubin. The 2026-05-19 re-scan replaces aucubin attribution with **acteoside + apigenin + geniposidic acid via PPAR pathway → URAT1 + GLUT9** (Liu 2024 PMC11313179). Apigenin specifically deserves a separate URAT1 mechanism entry per Li 2021 PMID 34044255. (In Vitro + Animal Model; source: urat1-classical-formula-rescan-2026-05-19.md)

**5. Si Miao San (SMS) — phytoecdysteroid + estrone arms missed.** The original comp-013 SMS row captured the main flavonoid + alkaloid contributions. The 2026-05-19 re-scan surfaced two additional axes: (a) **Phytoecdysteroids** from Achyranthes bidentata / Niu Xi (one of the four SMS cardinal herbs) — independent ecdysteroid-pathway anti-inflammatory mechanism. (b) **Estrone-family signaling** — multiple SMS components engage estrogen-receptor-mediated downstream effects relevant to bone + inflammation. Both axes are mechanism-additive to the existing flavonoid arm. (Mechanistic Extrapolation; source: urat1-classical-formula-rescan-2026-05-19.md)

**6. Rhein / Emodin split in Rheum palmatum (Da Huang) — mechanism separation.** Original comp-013 framing treated rhein + emodin as a co-acting anthraquinone class. The 2026-05-19 re-scan separates them: **rhein → direct XO inhibition** (Meng 2015, Animal Model); **emodin → transporter-mediated UA excretion, NO XO inhibition** (Hou 2023 PMC10304951, already cited but mechanism not separated in narrative). Treat as two distinct chokepoint engagements rather than one. (Animal Model; source: xo-classical-formula-rescan-2026-05-19.md)

**7. Acacetin → Agastache rugosa / Huo Xiang (new tier-1 XO chokepoint candidate).** Yuk 2023 PMC9914411: acacetin XO IC50 = 0.58 μM. Most potent flavonoid in panel, beats luteolin. Classical formula context: Huo Xiang Zheng Qi. GRAS culinary status in Korea + Japan. Tier-1 XO chokepoint entry. (In Vitro; source: xo-classical-formula-rescan-2026-05-19.md)

**8. Kaempferol → Chrysanthemum morifolium / Ju Hua (new tier-1 XO chokepoint candidate).** Wee 2023 PMC9864848: kaempferol XO IC50 = 2.18 μM. Lee 2018 PMC6213378 DKB114 formula 38.3% UA ↓ at 200 mg/kg, XO IC50 104.4 μg/mL. Tier-1 XO chokepoint entry. (In Vitro + Animal Model; source: xo-classical-formula-rescan-2026-05-19.md)

**9. Chlorogenic acid as a compound-class entry (not per-herb).** Chlorogenic acid family is XO-active across Wu Mei (Prunus mume), Lonicera japonica, and likely Crataegus pinnatifida (Shan Zha) and others. Reframe as a compound-class entry rather than per-herb redundant entries. (In Vitro; source: xo-classical-formula-rescan-2026-05-19.md)

**10. H04 falsification card partial closure.** Comp-013's H04 hypothesis card flagged "ChEMBL coverage gap" — 5/9 compounds had no ChEMBL data. The 2026-05-19 traditional-name-first scan partially closes this: mangiferin (CHEMBL3611008), apigenin (well-cataloged), acteoside (curated). The methodology gap **isn't ChEMBL coverage** — it's **seed-list construction at the herb level rather than the formula + marker level**. Update H04 with this diagnosis: the falsification was query-framing, not database coverage.

**Cross-references for this addendum:**
- [`urat1-classical-formula-rescan-2026-05-19.md`](../logs/urat1-classical-formula-rescan-2026-05-19.md)
- [`xo-classical-formula-rescan-2026-05-19.md`](../logs/xo-classical-formula-rescan-2026-05-19.md)
- [`lit-scan-query-framing-retrospective-audit-2026-05-19.md`](../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md) — the audit triggering both re-scans
- [`hypotheses/H04-tcm-rigor-intersection.md`](./hypotheses/H04-tcm-rigor-intersection.md) — needs marker-correction update incorporating items 1, 3, 4 above
- [`gout-pathophysiology.md`](./gout-pathophysiology.md) §"multi-track urate transporter coverage" — XO row updated with acacetin + kaempferol + rhein
- [`abcg2-modulators.md`](./abcg2-modulators.md) §"Tier 2 — Solid mechanism, modest evidence" — Poria cocos added (sister rescan finding, [`mushroom-hdac6-q141k-rescan-2026-05-19.md`](../logs/mushroom-hdac6-q141k-rescan-2026-05-19.md))
