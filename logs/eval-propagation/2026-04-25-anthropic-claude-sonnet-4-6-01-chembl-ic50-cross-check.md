---
date: 2026-04-25
scenario: 01-chembl-ic50-cross-check
model: anthropic/claude-sonnet-4-6
before_sha: c55ec09331283079fde836a65a02c8c0b9993c35
iterations: 25
completed: False
hit_iter_cap: True
input_tokens: 1851023
output_tokens: 13546
cost_usd: 5.7563
recall: 1.0
precision: 1.0
files_changed: 7
diff_lines: 311
---

# Propagation eval — anthropic/claude-sonnet-4-6 on 01-chembl-ic50-cross-check

## Done summary

(model did not call done() — see last_text)

## Last assistant text

```
Now update `wiki/GRAPH.md` to add two-tier labeling nodes and the quercetin 5-LOX edge:
```

## Metrics

- Recall: 1.0
- Precision: 1.0
- Files touched (7): ['wiki/GRAPH.md', 'wiki/cannabinoids-terpenes.md', 'wiki/gout-clinical-pipeline.md', 'wiki/nlrp3-exploit-map.md', 'wiki/nlrp3-inflammasome.md', 'wiki/oridonin.md', 'wiki/supplements-stack.md']
- Expected but not touched: []
- Touched but not expected: []

## Diff

```diff
diff --git a/wiki/GRAPH.md b/wiki/GRAPH.md
index c9bd1bf..abf06bf 100644
--- a/wiki/GRAPH.md
+++ b/wiki/GRAPH.md
@@ -72,10 +72,12 @@ graph TB
     end
 
     subgraph Inhibitors["NLRP3 INHIBITORS"]
-        J1["Oridonin"]
+        J1["Oridonin — Direct Inhibitor — human IC50 5.18 uM"]
         J2["Disulfiram"]
         J3["ASC Block"]
         J4["Gasdermin D Block"]
+        J5["Dapansutrile — Direct Inhibitor — human IC50 1.0 uM"]
+        J6["Quercetin — Pathway Modulator — 5-LOX IC50 300 nM"]
     end
 
     subgraph Cannabinoids["CANNABINOIDS / TERPENES"]
@@ -146,10 +148,13 @@ graph TB
     H3 --> B3
     
     %% NLRP3 inhibition path
+    J1 -->|"covalent Cys279 — direct inhibitor"| C2
     J1 --> J3
-    J1 --> C2
     J2 --> J4
     J2 --> C2
+    J5 -->|"ATPase inhibition — direct inhibitor — 1000x mouse-human gap"| C2
+    J6 -->|"NF-kB pathway modulator"| C2
+    J6 -->|"5-LOX inhibition IC50 300 nM"| C4
     
     %% Metabolic modulation
     K1 --> K2
diff --git a/wiki/cannabinoids-terpenes.md b/wiki/cannabinoids-terpenes.md
index b43d33a..b6548c8 100644
--- a/wiki/cannabinoids-terpenes.md
+++ b/wiki/cannabinoids-terpenes.md
@@ -168,6 +168,7 @@ The inhibitor screen classified beta-caryophyllene as Tier 4 with "no gout evide
 - **Computational docking:** CDOCKER interaction energy = 31.92 kcal/mol (suggests NLRP3 direct binding; no formal IC50)
 - **Evidence level:** Animal model (in vivo, MSU-induced gouty arthritis in rats)
 - **Citation:** *Front Pharmacol* 2021;12:651305. PMID: 33967792
+- **ChEMBL status:** Beta-caryophyllene (CHEMBL445740) has **zero curated bioactivities against human NLRP3** (CHEMBL1741208) in ChEMBL v34. The 2021 gout paper used computational docking + downstream inflammatory markers, not a direct NLRP3 inhibition IC50 assay. Beta-caryophyllene is therefore classified as an **NLRP3 pathway modulator**, not a direct NLRP3 inhibitor. This does not diminish the in vivo gout model evidence — functional IL-1β suppression in MSU models is clinically relevant — but the mechanism of NLRP3 engagement remains uncharacterized at the binding level. (source: nlrp3-inhibitor-screen.md)
 
 This is the only terpene or cannabinoid with direct, published data in the gout-specific MSU crystal model.
 
@@ -321,17 +322,20 @@ The poor systemic bioavailability (~6% fasting) does NOT support a "stays in gut
 
 ### Potency Hierarchy in Context
 
-| Compound | NLRP3 Mechanism | Evidence Level | Gout-Specific? | Estimated Potency vs. Quercetin (IC50 ~11 μM) |
-|----------|----------------|----------------|----------------|----------------------------------------------|
-| MCC950 | Direct NLRP3 ATP pocket | Clinical (Phase 2a) | Indirect | ~1,500× more potent |
-| Oridonin | Covalent Cys279 | Preclinical | No | Irreversible (not IC50 comparable) |
-| Quercetin | ASC / upstream | Animal model (MSU) | Yes | Benchmark |
-| **Beta-caryophyllene** | CB2/TLR4/NLRP3/NF-κB | **Animal model (MSU gout)** | **Yes** | Unknown — no IC50 |
-| CBD | P2X7/NF-κB (upstream, indirect) | In vitro (human monocytes) | No | Active 0.1–10 μM; no formal IC50 |
-| CBG | NF-κB/MAPK (indirect) | Animal model (CIA arthritis) | No | Unknown |
-| THCV | P2X7/NF-κB | In vitro | No | Unknown |
-| CBC | PANX1/P2X7 | In vitro | No | Unknown |
-| Myrcene | COX/PG, CB2 (no NLRP3 assay) | Animal model (adjuvant arthritis) | No | Not applicable |
+| Compound | NLRP3 Mechanism | Classification | Evidence Level | Gout-Specific? | Human NLRP3 IC50 (ChEMBL) |
+|----------|----------------|----------------|----------------|----------------|---------------------------|
+| MCC950 | Direct NLRP3 ATP pocket | **Direct inhibitor** | Clinical (Phase 2a) | Indirect | ~7.5 nM (Coll et al. 2015; not in ChEMBL by common synonyms) |
+| Dapansutrile | NLRP3 ATPase | **Direct inhibitor** | Clinical (Phase 2a gout) | Yes | 1,000 nM human MDM (1 nM mouse — 1,000× gap) |
+| Oridonin | Covalent Cys279 | **Direct inhibitor** | Preclinical | No | 5,180 nM human THP-1 (cell-free kinetics: 0.5–2 µM) |
+| Quercetin | NF-κB/upstream (5-LOX IC50 = 300 nM) | **Pathway modulator** | Animal model (MSU) | Yes | None in ChEMBL |
+| **Beta-caryophyllene** | CB2/TLR4/NLRP3/NF-κB (docking only) | **Pathway modulator** | **Animal model (MSU gout)** | **Yes** | None in ChEMBL |
+| CBD | P2X7/NF-κB (upstream, indirect) | **Pathway modulator** | In vitro (human monocytes) | No | None in ChEMBL |
+| CBG | NF-κB/MAPK (indirect) | **Pathway modulator** | Animal model (CIA arthritis) | No | None in ChEMBL |
+| THCV | P2X7/NF-κB | **Pathway modulator** | In vitro | No | None in ChEMBL |
+| CBC | PANX1/P2X7 | **Pathway modulator** | In vitro | No | None in ChEMBL |
+| Myrcene | COX/PG, CB2 (no NLRP3 assay) | **Pathway modulator** | Animal model (adjuvant arthritis) | No | None in ChEMBL |
+
+**Two-tier labeling note:** "Direct NLRP3 inhibitor" = curated human NLRP3 IC50 in ChEMBL or equivalent peer-reviewed binding assay. "NLRP3 pathway modulator" = functional IL-1β/inflammasome suppression demonstrated, but direct NLRP3 binding IC50 not characterized in human cells. Functional modulation is clinically relevant; the distinction is a mechanistic rigor upgrade. (source: nlrp3-inhibitor-screen.md)
 
 ### Revised Stack Positions
 
diff --git a/wiki/gout-clinical-pipeline.md b/wiki/gout-clinical-pipeline.md
index 390beaa..c17b17c 100644
--- a/wiki/gout-clinical-pipeline.md
+++ b/wiki/gout-clinical-pipeline.md
@@ -101,6 +101,16 @@ According to PubMed, Dapansutrile (OLT1177) Phase 2a proof-of-concept in gout wa
 - 25/34 patients had treatment-emergent AEs (mostly metabolism and GI); 2 SAEs (one flare worsening, one coronary stenosis unrelated)
 - **Conclusion:** "Dapansutrile is a specific NLRP3 inflammasome inhibitor with a satisfactory safety profile and efficacy in the reduction of target joint pain."
 
+**Species gap caveat — recontextualizing the Phase 2a efficacy (source: nlrp3-inhibitor-screen.md):**
+
+A ChEMBL v34 cross-check (CHEMBL3989943, queried 2026-04-23) reveals a 1,000× interspecies potency gap for dapansutrile:
+- **Mouse J774A.1 cells:** IC50 = **1 nM** (pChEMBL = 9.00; *Eur J Med Chem* 2020, *Bioorg Med Chem Lett* 2021)
+- **Human MDM cells:** IC50 = **1,000 nM (1.0 µM)** (pChEMBL = 6.00; *Eur J Med Chem* 2023)
+
+This gap is clinically significant: preclinical mouse studies made dapansutrile appear MCC950-class (sub-nM). The human cellular data places it firmly in the µM range. The Phase 2a efficacy (52–84% pain reduction at 100–2,000 mg/day) is **consistent with human-cell µM potency at high oral doses** — not with sub-nM potency. This reframes the dose-response: the high doses (1,000–2,000 mg/day) were likely necessary to achieve µM tissue concentrations in human joints, not because of poor bioavailability alone.
+
+**Implication:** Compounds showing strong mouse NLRP3 activity may not translate to human cells at equivalent concentrations. This supports Open Enzyme's emphasis on human-cell (THP-1 or MDM) validation assays over rodent models for NLRP3 screening. (source: nlrp3-inhibitor-screen.md)
+
 **What happened next:**
 - No Phase 2b or Phase 3 in gout on ClinicalTrials.gov (as of 2026-04-23)
 - Olatec pivoted to heart failure (Phase 1b NCT03534297, completed 2019) and COVID-19 (Phase 2 NCT04540120, terminated 2022)
diff --git a/wiki/nlrp3-exploit-map.md b/wiki/nlrp3-exploit-map.md
index f6c1af4..9821a6d 100644
--- a/wiki/nlrp3-exploit-map.md
+++ b/wiki/nlrp3-exploit-map.md
@@ -107,17 +107,19 @@ Boswellia (AKBA): Acetyl-11-keto-β-boswellic acid directly inhibits IKKβ. 300
 
 Vitamin D: VDR activation suppresses NF-κB. Most people are deficient. Test and target 50–70 ng/mL. 5,000–10,000 IU/day with K2.
 
-Quercetin: Inhibits NF-κB and stabilizes mast cells. 500–1000 mg/day. Phytosome form (Quercefit) has 20x better absorption. Found in onions, apples. Also blocks xanthine oxidase (uric acid production) — dual anti-gout mechanism.
+Quercetin: Inhibits NF-κB and stabilizes mast cells. 500–1000 mg/day. Phytosome form (Quercefit) has 20x better absorption. Found in onions, apples. Also blocks xanthine oxidase (uric acid production) — dual anti-gout mechanism. **ChEMBL note:** Quercetin is an **NLRP3 pathway modulator** (no curated human NLRP3 IC50 in ChEMBL); its most potent ChEMBL activity is 5-LOX inhibition (IC50 = 300 nM, *J Med Chem* 1991). 5-LOX produces LTB4, a key neutrophil chemoattractant in gout flares — quercetin's 5-LOX inhibition may be a significant underappreciated mechanism complementing its NF-κB effects. (source: nlrp3-inhibitor-screen.md)
 
 A. oryzae already produces kojic acid (a tyrosinase inhibitor). With the synthetic biology toolkit now available for A. oryzae — CRISPR-Cas9, tunable promoters, neutral loci for gene insertion — you could theoretically engineer it to produce curcumin precursors, sulforaphane glucosinolates, or even KPV peptide alongside the uricase. The GRAS status of A. oryzae makes this a unique platform: you're engineering a food organism, not a drug. This is a Lauren conversation — the genetic tools exist, it's a matter of pathway design.
 
 #### Oridonin
 
-> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. Active at 0.5–2 µM. Same binding site as MCC950.
+> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. **Direct NLRP3 inhibitor** (curated human NLRP3 IC50 in ChEMBL). Same binding site as MCC950.
 
 This is the gem of the natural compound world for NLRP3 inhibition. Oridonin, an ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens, covalently and specifically modifies NLRP3 at cysteine 279. This is the same domain that MCC950 targets — the NACHT domain. By forming an irreversible covalent bond, oridonin blocks the NLRP3-NEK7 interaction that's essential for inflammasome assembly.
 
-Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
+Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM (cell-free covalent kinetics, In Vitro). It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
+
+**Two-tier potency (ChEMBL cross-check, 2026-04-23):** The 0.5–2 µM figure reflects cell-free covalent kinetics from the Nat Commun 2018 paper. ChEMBL v34 (CHEMBL1164920) records a curated human THP-1 cellular IC50 of **5.18 µM** (*Eur J Med Chem* 2023). Both values are correct in context — the cell-free number captures covalent reaction rate; the cellular number captures functional inhibition in human cells. For translational claims, use the human cellular IC50 (5.18 µM). (source: nlrp3-inhibitor-screen.md)
 
 The dual hit: Beyond NLRP3, oridonin also activates Nrf2 and suppresses NF-κB independently. So it hits CP1 AND CP2 through different mechanisms.
 
@@ -155,7 +157,7 @@ Desferrioxamine: Iron chelator that stabilizes lysosomes by preventing iron-cata
 
 MCC950 (CRID3): The first specific NLRP3 inhibitor. Binds the Walker B motif in the NACHT domain, blocking ATP hydrolysis required for oligomerization. Clinical development was terminated due to hepatotoxicity in Phase 1 RA trial. But it defined the druggable target — every subsequent inhibitor stands on its shoulders.
 
-Dapansutrile (OLT1177): Oral NLRP3 inhibitor. Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with reduction in swelling by day 3. Good safety profile (no hepatotoxicity like MCC950). Currently in Phase 2/3 trials. This may eventually be the pharma solution, but oridonin and tranilast give you access to the same target class now.
+Dapansutrile (OLT1177): Oral NLRP3 inhibitor. **Direct NLRP3 inhibitor** (curated human NLRP3 IC50 in ChEMBL: 1,000 nM / 1.0 µM in human MDM cells, *Eur J Med Chem* 2023). Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with reduction in swelling by day 3. Good safety profile (no hepatotoxicity like MCC950). **Species gap caveat:** ChEMBL also records dapansutrile at 1 nM in mouse J774A.1 cells — a 1,000× potency gap vs. human cells. The Phase 2a clinical efficacy (52–84% pain reduction at 100–2,000 mg/day) is consistent with human-cell µM potency at high oral doses, not sub-nM potency. Gout development appears stalled as of 2026 (no Phase 2b/3 registered). Oridonin and tranilast give you access to the same target class now. (source: nlrp3-inhibitor-screen.md)
 
 #### Colchicine — The Established Exploit
 
@@ -251,11 +253,11 @@ BHB (ketones): Blocks priming (CP1), prevents K⁺ efflux (CP2), reduces ASC oli
 
 Berberine: Suppresses NF-κB/TLR4 (CP1), reduces NLRP3/ASC/caspase-1 mRNA (CP1+CP4), remodels gut microbiota to reduce LPS priming (CP1). Plus: SIBO treatment for Lynn, blood sugar regulation, antimicrobial. It's the Swiss Army knife.
 
-Oridonin: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). A natural compound that mimics a pharma-grade NLRP3 inhibitor.
+Oridonin: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). A natural compound that mimics a pharma-grade NLRP3 inhibitor. **Direct NLRP3 inhibitor** (human THP-1 IC50 = 5.18 µM, ChEMBL; cell-free covalent kinetics 0.5–2 µM, Nat Commun 2018). (source: nlrp3-inhibitor-screen.md)
 
 Dimethyl Fumarate: Nrf2 activator (CP1+CP2) AND gasdermin D succinator (CP6). Bridges the first and last chokepoints.
 
-EGCG: NF-κB inhibitor (CP1), caspase-1 suppressor (CP4), IL-1β blocker (CP5). Three downstream chokepoints from drinking tea.
+EGCG: NF-κB inhibitor (CP1), caspase-1 suppressor (CP4), IL-1β blocker (CP5). Three downstream chokepoints from drinking tea. **NLRP3 pathway modulator** (no curated human NLRP3 IC50 in ChEMBL). (source: nlrp3-inhibitor-screen.md)
 
 Cross-Reference: Peptide Mechanisms
 
diff --git a/wiki/nlrp3-inflammasome.md b/wiki/nlrp3-inflammasome.md
index 2bd5ea7..e7d23f6 100644
--- a/wiki/nlrp3-inflammasome.md
+++ b/wiki/nlrp3-inflammasome.md
@@ -57,7 +57,7 @@ The NLRP3 inflammasome pathway operates as a sequential cascade with six distinc
 
 - **Parthenolide** (from feverfew): Inhibits IKKβ (the kinase that degrades IκB) and directly modifies NF-κB p65. Dual mechanism. DMAPT (dimethylamino-parthenolide) is a more soluble derivative used in research. (Source: nlrp3-exploit-map.md)
 
-- **Quercetin**: Inhibits NF-κB and also blocks xanthine oxidase (uric acid production). Phytosome form (Quercefit) provides 20x better bioavailability. Dose: 500–1000 mg daily. (Source: nlrp3-exploit-map.md)
+- **Quercetin**: Inhibits NF-κB and also blocks xanthine oxidase (uric acid production). Phytosome form (Quercefit) provides 20x better bioavailability. Dose: 500–1000 mg daily. **ChEMBL note:** Quercetin has zero curated bioactivities against human NLRP3 (CHEMBL1741208) — it is an **NLRP3 pathway modulator**, not a direct NLRP3 inhibitor. Its most potent ChEMBL activity is against **5-lipoxygenase (5-LOX): IC50 = 300 nM** (*J Med Chem* 1991) — a leukotriene-pathway target. LTB4 (produced by 5-LOX) is a known amplifier of MSU-driven neutrophil chemotaxis in gout flares; quercetin's 5-LOX inhibition may be a significant underappreciated mechanism. (Source: nlrp3-exploit-map.md; source: nlrp3-inhibitor-screen.md)
 
 - **EGCG** (green tea catechin): Inhibits IKK activity, suppresses NF-κB. Dose: 400–800 mg daily or 3–5 cups green tea daily. Matcha provides the highest concentration. (Source: nlrp3-exploit-map.md)
 
@@ -75,7 +75,7 @@ The NLRP3 inflammasome pathway operates as a sequential cascade with six distinc
 
 - **Beta-hydroxybutyrate (BHB)**: The ketone body produced during fasting or ketogenic diet. BHB prevents potassium efflux, reduces ASC speck formation, and directly inhibits NLRP3 assembly. Notably, BHB is NOT dependent on AMPK, autophagy, or ROS reduction—it is a direct inhibitory effect on NLRP3 oligomerization. In rodent models, a ketogenic diet significantly reduced gout flare severity. Critical insight: traditional concern that ketosis raises uric acid is true short-term (ketones compete with urate for renal excretion), but with uricase handling uric acid clearance, ketosis becomes pure inflammasome suppression. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)
 
-- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. Active at 0.5–2 µM. Published in Nature Communications: oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md)
+- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. **Two-tier potency:** cell-free covalent kinetics 0.5–2 µM (Nat Commun 2018, In Vitro); human THP-1 cellular IC50 5.18 µM (ChEMBL CHEMBL1164920, *Eur J Med Chem* 2023, In Vitro). Both values are correct in context — the 0.5–2 µM figure reflects covalent reaction kinetics in cell-free or murine systems; the 5.18 µM is the curated human cellular IC50. Oridonin is classified as a **direct NLRP3 inhibitor** (curated human NLRP3 IC50 in ChEMBL). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md; source: nlrp3-inhibitor-screen.md)
 
 - **NAC (N-Acetyl Cysteine)**: Replenishes glutathione, the master intracellular antioxidant. Reduces mtROS, thus reducing the Signal 2 trigger for NLRP3 assembly. Dose: 600–1200 mg daily. Widely available, inexpensive, well-tolerated. The limitation: does not specifically target mitochondria. (Source: nlrp3-exploit-map.md)
 
@@ -163,6 +163,21 @@ The most efficient exploits hit three or more chokepoints:
 
 - **EGCG**: NF-κB inhibitor (CP1), caspase-1 suppressor (CP4), IL-1β blocker (CP5). Three downstream chokepoints from drinking tea. (Source: nlrp3-exploit-map.md)
 
+## Two-Tier Labeling: Direct Inhibitors vs. Pathway Modulators
+
+A ChEMBL v34 cross-check (queried 2026-04-23 against CHEMBL1741208, human NLRP3, UniProt Q96P20) reveals that most compounds described as "NLRP3 inhibitors" in the literature lack a curated direct human NLRP3 IC50. Only two compounds in the Open Enzyme inhibitor screen have such data: (source: nlrp3-inhibitor-screen.md)
+
+| Compound | ChEMBL ID | Human NLRP3 IC50 | Classification |
+|---|---|---|---|
+| **Dapansutrile (OLT1177)** | CHEMBL3989943 | 1,000 nM (1.0 µM) — human MDM cells | **Direct NLRP3 inhibitor** |
+| **Oridonin** | CHEMBL1164920 | 5,180 nM (5.18 µM) — human THP-1 | **Direct NLRP3 inhibitor** |
+| Quercetin | CHEMBL50 | No curated human NLRP3 IC50 | **NLRP3 pathway modulator** |
+| Ursolic acid | CHEMBL169 | No curated human NLRP3 IC50 | **NLRP3 pathway modulator** |
+| Beta-caryophyllene | CHEMBL445740 | No curated human NLRP3 IC50 | **NLRP3 pathway modulator** |
+| Tranilast | CHEMBL415324 | No curated human NLRP3 IC50 | **NLRP3 pathway modulator** (despite NACHT domain binding claim) |
+
+**This is not a contradiction of the inhibitor screen's rankings.** Functional IL-1β suppression in MSU-stimulated macrophages is clinically relevant — it's what Open Enzyme cares about. The distinction is a rigor upgrade: most "NLRP3 inhibitors" act upstream (NF-κB priming block, ROS reduction, K+ efflux prevention) or at unknown direct binding sites not yet characterized in medicinal chemistry assays. Going forward, use "direct NLRP3 inhibitor" only for compounds with a curated human NLRP3 IC50 in ChEMBL or equivalent peer-reviewed binding assay. (source: nlrp3-inhibitor-screen.md)
+
 ## Pharmaceutical NLRP3 Inhibitors
 
 ### Approved or In Clinical Development
@@ -171,7 +186,7 @@ The most efficient exploits hit three or more chokepoints:
 
 - **Anakinra (Kineret)**: IL-1 receptor antagonist. FDA-approved for RA and CAPS. Off-label for refractory gout. Less expensive than canakinumab but requires daily injection.
 
-- **Dapansutrile (OLT1177)**: Oral NLRP3 inhibitor. Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with swelling reduction by day 3. Good safety profile (no hepatotoxicity like MCC950). Currently in Phase 2/3 trials. This may eventually be the pharmaceutical solution. (Source: nlrp3-exploit-map.md)
+- **Dapansutrile (OLT1177)**: Oral NLRP3 inhibitor. Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with swelling reduction by day 3. Good safety profile (no hepatotoxicity like MCC950). **Species gap caveat:** ChEMBL v34 shows dapansutrile at 1 nM (pChEMBL=9.00) in mouse J774A.1 cells vs. **1,000 nM (1.0 µM)** in human MDM cells (pChEMBL=6.00) — a 1,000× interspecies potency gap. The Phase 2a clinical efficacy (52–84% pain reduction at 100–2,000 mg/day) is consistent with human-cell µM potency at high oral doses, not sub-nM potency. Gout development appears stalled as of 2026 (no Phase 2b/3 registered). Dapansutrile is classified as a **direct NLRP3 inhibitor** (curated human NLRP3 IC50 in ChEMBL). (Source: nlrp3-exploit-map.md; source: nlrp3-inhibitor-screen.md)
 
 - **MCC950 (CRID3)**: The first specific NLRP3 inhibitor. Binds the Walker B motif in the NACHT domain, blocking ATP hydrolysis required for oligomerization. Clinical development terminated due to hepatotoxicity in Phase 1 RA trial, but it defined the druggable target and validated the mechanism.
 
diff --git a/wiki/oridonin.md b/wiki/oridonin.md
index a98649a..56f501d 100644
--- a/wiki/oridonin.md
+++ b/wiki/oridonin.md
@@ -35,14 +35,17 @@ Oridonin's mechanism is a **Michael addition** — a nucleophilic attack by the
 
 ## Potency & Specificity
 
-### Active Concentration
+### Two-Tier Potency Framing
 
-Oridonin exhibits dose-dependent inhibition of NLRP3 at **0.5–2 µM** concentrations:
-- Caspase-1 cleavage: reduced dose-dependently
-- IL-1β secretion: suppressed
-- Pyroptotic cell death: prevented
+Oridonin's potency is reported at two distinct levels that measure different things — both are correct in context:
 
-These concentrations are physiologically achievable with oral supplementation.
+**Tier 1 — Cell-free covalent kinetics (0.5–2 µM):** The original *Nature Communications* 2018 paper characterizes covalent Cys279 binding kinetics and dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death in cell-based assays. This figure reflects the covalent reaction rate and is derived from mouse or cell-free biochemical systems. (In Vitro; source: nlrp3-inhibitor-screen.md)
+
+**Tier 2 — Human cellular IC50 (5.18 µM):** ChEMBL v34 (CHEMBL1164920) records a curated human NLRP3 IC50 of **5,180 nM (5.18 µM)** in human THP-1 cells stimulated with LPS/ATP (*Eur J Med Chem* 2023, pChEMBL = 5.29). This is the only curated direct human NLRP3 inhibition assay for oridonin in ChEMBL. (In Vitro, human cells; source: nlrp3-inhibitor-screen.md)
+
+> ⚠️ **Potency context:** The 0.5–2 µM figure (Nat Commun 2018) reflects cell-free covalent kinetics and may not translate directly to the human cellular IC50 (5.18 µM, ChEMBL). The two numbers measure different things. For translational claims, the human THP-1 cellular IC50 (5.18 µM) is the more relevant benchmark. Both values are consistent with oridonin being a low-µM direct NLRP3 inhibitor — substantially weaker than MCC950 (7.5 nM) but with a covalent, irreversible mechanism that may compensate for lower apparent potency.
+
+**Active concentration range:** 0.5–5 µM (spanning both tiers). These concentrations are in the range achievable with oral supplementation, though human PK data for oridonin is limited.
 
 ### NLRP3-Specific
 
@@ -70,14 +73,15 @@ This multi-target property makes oridonin more potent than a single-mechanism in
 
 The peer-reviewed evidence for oridonin's NLRP3 inhibition is strong:
 
-- **Primary mechanism:** 2018 Nature Communications study on covalent NLRP3-Cys279 modification
+- **Primary mechanism:** 2018 Nature Communications study on covalent NLRP3-Cys279 modification (cell-free and murine cell-based assays; IC50 range 0.5–2 µM in these systems) (In Vitro / Animal Model)
+- **Human NLRP3 IC50:** 5.18 µM in human THP-1 cells (LPS/ATP stimulation), curated in ChEMBL v34 (CHEMBL1164920), *Eur J Med Chem* 2023 (In Vitro, human cells; source: nlrp3-inhibitor-screen.md)
 - **Analog development:** 2025 research on more potent oridonin derivatives
 - **Gout-specific studies:** ✗ None published
 - **Human clinical trials:** ✗ None
 
-The mechanism is well-established in cell culture and animal models, but clinical translation to gout has not occurred.
+The mechanism is well-established in cell culture and animal models, but clinical translation to gout has not occurred. Oridonin is classified as a **direct NLRP3 inhibitor** (binding/inhibition IC50 measured against human NLRP3 in ChEMBL), distinguishing it from NLRP3 pathway modulators that act upstream without a curated direct binding assay.
 
-**(Source: nlrp3-exploit-map.md)** — "Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM."
+**(Source: nlrp3-exploit-map.md; nlrp3-inhibitor-screen.md ChEMBL appendix)**
 
 ## Traditional Medicine Provenance
 
@@ -102,9 +106,11 @@ Natural plant extracts vary significantly in bioavailability. Oridonin-specific
 |----------|--------|-----------|--------|------|----------|--------|
 | **Oridonin** | NLRP3 Cys279 | Covalent (natural) | Available now | ~$20–40/month | ✓ Irreversible | Good (traditional use) |
 | **MCC950** | NLRP3 Walker B | Non-covalent (pharma) | Preclinical | NA | ~30 min | Hepatotoxic (Phase 1) |
-| **Dapansutrile** | NLRP3 (general) | Direct inhibitor | Phase 3 (gout) | Unknown | Hours | Good (Phase 2 data) |
+| **Dapansutrile** | NLRP3 ATPase | Direct inhibitor | Phase 2a (gout, stalled) | Unknown | Hours | Good (Phase 2 data) |
 | **Tranilast** | NLRP3 NACHT | Non-covalent (pharma) | Approved (Japan/Korea) | ~$30–50/month | Hours | Good (decades of use) |
 
+**Note on potency comparison:** Oridonin's human cellular IC50 (5.18 µM, ChEMBL) and dapansutrile's human cellular IC50 (1.0 µM, ChEMBL) are both in the µM range — substantially weaker than MCC950 (7.5 nM) in direct assays. Dapansutrile's mouse IC50 (1 nM) is 1,000× more potent than its human cellular IC50, a species gap that recontextualizes preclinical comparisons. (source: nlrp3-inhibitor-screen.md)
+
 **Key observation:** Oridonin is a covalent NLRP3 inhibitor like MCC950, but unlike MCC950 it has not shown hepatotoxicity. It's available immediately, costs far less than clinical-stage drugs, and has the advantage of traditional use history (though this is not the same as modern clinical trial validation).
 
 ## Derivative Development
diff --git a/wiki/supplements-stack.md b/wiki/supplements-stack.md
index dcce8fd..f912645 100644
--- a/wiki/supplements-stack.md
+++ b/wiki/supplements-stack.md
@@ -125,11 +125,11 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 ### Oridonin (Rabdosia rubescens Extract)
 
-**Category:** Natural Compound / NLRP3 Inhibitor
+**Category:** Natural Compound / Direct NLRP3 Inhibitor
 
 **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition); blocks NLRP3-NEK7 interaction (CP2). Also activates Nrf2 and suppresses NF-κB (CP1/CP2).
 
-**Evidence level:** Established (Nature Communications 2018; dose-dependent IL-1β reduction at 0.5–2 µM)
+**Evidence level:** Established (Nature Communications 2018; dose-dependent IL-1β reduction at 0.5–2 µM cell-free covalent kinetics, In Vitro). **Two-tier potency:** cell-free covalent kinetics 0.5–2 µM (Nat Commun 2018); human THP-1 cellular IC50 5.18 µM (ChEMBL CHEMBL1164920, *Eur J Med Chem* 2023, In Vitro). Oridonin is a **direct NLRP3 inhibitor** — one of only two compounds in the inhibitor screen with a curated human NLRP3 IC50 in ChEMBL. (source: nlrp3-inhibitor-screen.md)
 
 **Dosing:** 50–100 mg/day
 
@@ -208,14 +208,15 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 ### Quercetin (Phytosome Form Preferred)
 
-**Category:** Flavonoid
+**Category:** Flavonoid / NLRP3 Pathway Modulator
 
 **Mechanism:** 
 - NF-κB inhibition (CP1)
 - Xanthine oxidase inhibition (direct uric acid production reduction)
 - Mast cell stabilization
+- **5-LOX inhibition (IC50 = 300 nM, *J Med Chem* 1991):** Quercetin's most potent ChEMBL activity is against 5-lipoxygenase, which produces LTB4 — a key neutrophil chemoattractant amplifying MSU-driven gout flares. This may be a significant underappreciated mechanism. (In Vitro; source: nlrp3-inhibitor-screen.md)
 
-**Evidence level:** Established
+**Evidence level:** Established for NF-κB/XO inhibition; Animal Model for gout-specific NLRP3 suppression (MSU-induced arthritis in rats). **ChEMBL note:** Quercetin is an **NLRP3 pathway modulator** — zero curated human NLRP3 IC50 entries in ChEMBL v34. The "IC50 ~11 µM" cited in some reviews is from functional IL-1β readouts, not a direct NLRP3 binding assay. (source: nlrp3-inhibitor-screen.md)
 
 **Dosing:** 500–1,000 mg/day
 
@@ -422,11 +423,11 @@ These become available as Open Enzyme [[engineered-yeast-uricase]] and [[enginee
 | KPV peptide | Supported | CP1 | NF-κB stabilization | $100–200 |
 | BPC-157 | Established | CP1 (tissue repair) | Cytoprotection, NO modulation | Existing |
 | Sulforaphane | Established | CP1, CP2 | Nrf2/NF-κB crosstalk | $5–30 |
-| Oridonin | Established | CP1, CP2 | NLRP3 covalent inhibitor | $30–60 |
+| Oridonin | Established (direct NLRP3 inhibitor; human IC50 5.18 µM ChEMBL) | CP1, CP2 | NLRP3 covalent inhibitor (Cys279) | $30–60 |
 | Omega-3 (high-EPA) | Established | CP1, CP5 | SPM precursors | $30–50 |
 | Cherry extract | Supported | CP1 (XO inhibition) | Anthocyanins | $20–30 |
 | NAC | Established | CP2 | Glutathione replenishment | $10–15 |
-| Quercetin (Phytosome) | Established | CP1 (XO inhibition) | NF-κB + direct inhibition | $15–25 |
+| Quercetin (Phytosome) | Established (pathway modulator; no human NLRP3 IC50 in ChEMBL; 5-LOX IC50 = 300 nM) | CP1 (XO + 5-LOX inhibition) | NF-κB pathway modulator + 5-LOX | $15–25 |
 | Vitamin D3 + K2 | Established | CP1 | VDR activation | $10–15 |
 | Disulfiram | Established | CP6 | GSDMD pore blockade | ~$30 |
 | Tranilast | Established | CP2 | NACHT domain binding | $50–100 |

```
