---
date: 2026-05-06
scenario: 01-chembl-ic50-cross-check
model: deepseek/deepseek-v4-pro
before_sha: c55ec09331283079fde836a65a02c8c0b9993c35
iterations: 30
completed: False
hit_iter_cap: True
input_tokens: 1690964
output_tokens: 11732
cost_usd: 0.7458
recall: 1.0
precision: 1.0
files_changed: 7
diff_lines: 202
---

# Propagation eval — deepseek/deepseek-v4-pro on 01-chembl-ic50-cross-check

## Done summary

(model did not call done() — see last_text)

## Last assistant text

```
Now let me add the two-tier labeling concept to `nlrp3-inflammasome.md` and run the Mermaid linter:




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
index c9bd1bf..7ff50c4 100644
--- a/wiki/GRAPH.md
+++ b/wiki/GRAPH.md
@@ -71,11 +71,13 @@ graph TB
         I4["IL-10 Promotion"]
     end
 
-    subgraph Inhibitors["NLRP3 INHIBITORS"]
-        J1["Oridonin"]
-        J2["Disulfiram"]
-        J3["ASC Block"]
-        J4["Gasdermin D Block"]
+    subgraph Inhibitors["NLRP3 INHIBITORS & MODULATORS"]
+        J1["Oridonin — direct inhibitor<br/>cell-free 0.5-2µM / cellular 5.18µM"]
+        J2["Disulfiram — GSDMD blocker"]
+        J3["Dapansutrile — direct inhibitor<br/>⚠️ 1000× mouse-vs-human gap"]
+        J4["ASC Block"]
+        J5["Gasdermin D Block"]
+        J6["Pathway Modulators<br/>(quercetin, ursolic acid,<br/>beta-caryophyllene, etc.)"]
     end
 
     subgraph Cannabinoids["CANNABINOIDS / TERPENES"]
@@ -146,10 +148,12 @@ graph TB
     H3 --> B3
     
     %% NLRP3 inhibition path
-    J1 --> J3
+    J1 --> J4
     J1 --> C2
-    J2 --> J4
+    J2 --> J5
     J2 --> C2
+    J3 --> C2
+    J6 -->|"functional IL-1β ↓"| C2
     
     %% Metabolic modulation
     K1 --> K2
diff --git a/wiki/cannabinoids-terpenes.md b/wiki/cannabinoids-terpenes.md
index b43d33a..7f5e05d 100644
--- a/wiki/cannabinoids-terpenes.md
+++ b/wiki/cannabinoids-terpenes.md
@@ -37,7 +37,7 @@ sources:
 
 Cannabis produces two broad classes of bioactive compounds relevant to Open Enzyme's targets: cannabinoids (CBD, THC, CBG, CBC, THCV) and terpenes (beta-caryophyllene, limonene, myrcene, alpha-pinene, linalool). This page synthesizes what the literature actually supports, where the evidence is thin, and how these compounds fit the existing NLRP3 and gout framework.
 
-**Bottom line up front:** Beta-caryophyllene is the standout compound — it has direct MSU (gout) animal model data that the inhibitor screen missed. CBD has functional NLRP3 data but no gout-specific model testing, and its mechanism is upstream (P2X7) rather than direct NLRP3 binding. CBG and THCV have newer data worth tracking. Myrcene has analgesic data in arthritis but no NLRP3 assays.
+**Bottom line up front:** Beta-caryophyllene is the standout compound — it has direct MSU (gout) animal model data that the inhibitor screen missed. However, ChEMBL cross-check (2026-04-23) confirms zero direct human NLRP3 bioactivities for beta-caryophyllene (CHEMBL445740). The 2021 *Front Pharmacol* MSU gout paper used computational docking + downstream markers (IL-1β, caspase-1, ASC), not a direct NLRP3 inhibition IC50. Beta-caryophyllene is more accurately an **NLRP3 pathway modulator** (CB2/TLR4/NF-κB upstream) rather than a direct NLRP3 inhibitor. CBD has functional NLRP3 data but no gout-specific model testing, and its mechanism is upstream (P2X7) rather than direct NLRP3 binding. CBG and THCV have newer data worth tracking. Myrcene has analgesic data in arthritis but no NLRP3 assays.
 
 ---
 
diff --git a/wiki/gout-clinical-pipeline.md b/wiki/gout-clinical-pipeline.md
index 390beaa..acb02e5 100644
--- a/wiki/gout-clinical-pipeline.md
+++ b/wiki/gout-clinical-pipeline.md
@@ -29,6 +29,8 @@ Data compiled from ClinicalTrials.gov and PubMed via the Anthropic life-sciences
 
 2. **Dapansutrile (OLT1177) in gout: published Phase 2a, but no current late-phase trial.** The 2020 Phase 2a proof-of-concept (N=34) showed 52–68% pain reduction at day 3 across four dose levels. Olatec's subsequent gout development appears stalled; their active programs moved to heart failure (completed) and COVID-19 (terminated). Phase 2b/3 in gout is **not registered on ClinicalTrials.gov as of April 2026.**
 
+> ⚠️ **Species gap (ChEMBL cross-check):** Dapansutrile shows a ~1,000× potency gap between mouse and human cells — 1 nM IC50 in mouse J774A.1 cells vs. 1,000 nM (1.0 µM) in human MDM cells (*Eur J Med Chem* 2020/2023 via ChEMBL). The 2020 Phase 2a efficacy (52–84% pain reduction at 100–2,000 mg/day) is consistent with human-cell µM potency at high oral doses, not sub-nM potency. Mouse preclinical data overstates dapansutrile's potency relative to human cells. (source: nlrp3-inhibitor-screen.md ChEMBL appendix)
+
 3. **Canakinumab finally got FDA approval for gout in August 2023** — the first biologic formally indicated for gout in the US, 12 years after its initial rejection. Our wiki references canakinumab but does not reflect this regulatory update.
 
 4. **The real competitor to Open Enzyme's thesis is PRX-115 (Protalix)**, whose Phase 2 RELEASE trial began recruiting December 2025. It's a systemic pegylated uricase + methotrexate — same immunomodulator strategy as SEL-212/Krystexxa+MTX. PRX-115 being in Phase 2 proves the systemic-uricase-with-tolerance-induction path is alive. Open Enzyme's gut-lumen-uricase angle remains the untested and uncompeted path.
diff --git a/wiki/nlrp3-exploit-map.md b/wiki/nlrp3-exploit-map.md
index f6c1af4..62e6445 100644
--- a/wiki/nlrp3-exploit-map.md
+++ b/wiki/nlrp3-exploit-map.md
@@ -113,11 +113,11 @@ A. oryzae already produces kojic acid (a tyrosinase inhibitor). With the synthet
 
 #### Oridonin
 
-> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. Active at 0.5–2 µM. Same binding site as MCC950.
+> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. Two-tier potency: cell-free covalent kinetics 0.5–2 µM (*Nat Commun* 2018); human cellular IC50 = 5.18 µM in THP-1 (*Eur J Med Chem* 2023 via ChEMBL). Both correct in context. Same binding site as MCC950.
 
 This is the gem of the natural compound world for NLRP3 inhibition. Oridonin, an ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens, covalently and specifically modifies NLRP3 at cysteine 279. This is the same domain that MCC950 targets — the NACHT domain. By forming an irreversible covalent bond, oridonin blocks the NLRP3-NEK7 interaction that's essential for inflammasome assembly.
 
-Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
+Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM (cell-free covalent kinetics). The curated human cellular IC50 in THP-1 macrophages is 5.18 µM (*Eur J Med Chem* 2023 via ChEMBL) — both numbers are correct in context; the cell-free number measures target engagement, the cellular number reflects full-cell pharmacology. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
 
 The dual hit: Beyond NLRP3, oridonin also activates Nrf2 and suppresses NF-κB independently. So it hits CP1 AND CP2 through different mechanisms.
 
@@ -157,6 +157,8 @@ MCC950 (CRID3): The first specific NLRP3 inhibitor. Binds the Walker B motif in
 
 Dapansutrile (OLT1177): Oral NLRP3 inhibitor. Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with reduction in swelling by day 3. Good safety profile (no hepatotoxicity like MCC950). Currently in Phase 2/3 trials. This may eventually be the pharma solution, but oridonin and tranilast give you access to the same target class now.
 
+> ⚠️ **Species gap (ChEMBL cross-check):** Dapansutrile shows a ~1,000× potency gap between mouse and human cells — 1 nM IC50 in mouse J774A.1 cells vs. 1,000 nM (1.0 µM) in human MDM cells (*Eur J Med Chem* 2020/2023 via ChEMBL). The 2020 Phase 2a gout trial efficacy (52–84% pain reduction at 100–2,000 mg/day) is consistent with human-cell µM potency at high oral doses, not sub-nM potency. Mouse preclinical data overstates dapansutrile's potency relative to human cells. This supports Open Enzyme's emphasis on human-cell (THP-1) validation assays over rodent models for NLRP3 screening. (source: nlrp3-inhibitor-screen.md ChEMBL appendix)
+
 #### Colchicine — The Established Exploit
 
 > **Mechanism:** Binds β-tubulin → depolymerizes microtubules → prevents microtubule-mediated transport of mitochondrial ASC to ER-localized NLRP3 → specks can't form
@@ -251,7 +253,7 @@ BHB (ketones): Blocks priming (CP1), prevents K⁺ efflux (CP2), reduces ASC oli
 
 Berberine: Suppresses NF-κB/TLR4 (CP1), reduces NLRP3/ASC/caspase-1 mRNA (CP1+CP4), remodels gut microbiota to reduce LPS priming (CP1). Plus: SIBO treatment for Lynn, blood sugar regulation, antimicrobial. It's the Swiss Army knife.
 
-Oridonin: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). A natural compound that mimics a pharma-grade NLRP3 inhibitor.
+Oridonin: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). A natural compound that mimics a pharma-grade NLRP3 inhibitor. Two-tier potency: cell-free 0.5–2 µM, cellular human IC50 5.18 µM — both correct in context. (source: nlrp3-inhibitor-screen.md ChEMBL appendix)
 
 Dimethyl Fumarate: Nrf2 activator (CP1+CP2) AND gasdermin D succinator (CP6). Bridges the first and last chokepoints.
 
diff --git a/wiki/nlrp3-inflammasome.md b/wiki/nlrp3-inflammasome.md
index 2bd5ea7..e7a8994 100644
--- a/wiki/nlrp3-inflammasome.md
+++ b/wiki/nlrp3-inflammasome.md
@@ -75,7 +75,7 @@ The NLRP3 inflammasome pathway operates as a sequential cascade with six distinc
 
 - **Beta-hydroxybutyrate (BHB)**: The ketone body produced during fasting or ketogenic diet. BHB prevents potassium efflux, reduces ASC speck formation, and directly inhibits NLRP3 assembly. Notably, BHB is NOT dependent on AMPK, autophagy, or ROS reduction—it is a direct inhibitory effect on NLRP3 oligomerization. In rodent models, a ketogenic diet significantly reduced gout flare severity. Critical insight: traditional concern that ketosis raises uric acid is true short-term (ketones compete with urate for renal excretion), but with uricase handling uric acid clearance, ketosis becomes pure inflammasome suppression. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)
 
-- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. Active at 0.5–2 µM. Published in Nature Communications: oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md)
+- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. **Two-tier potency:** cell-free covalent kinetics at 0.5–2 µM (*Nat Commun* 2018); human cellular IC50 = 5.18 µM in THP-1 cells (*Eur J Med Chem* 2023 via ChEMBL). Both are correct in context — the cell-free number measures target engagement, the cellular number reflects full-cell pharmacology. Published in Nature Communications: oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md, nlrp3-inhibitor-screen.md ChEMBL cross-check)
 
 - **NAC (N-Acetyl Cysteine)**: Replenishes glutathione, the master intracellular antioxidant. Reduces mtROS, thus reducing the Signal 2 trigger for NLRP3 assembly. Dose: 600–1200 mg daily. Widely available, inexpensive, well-tolerated. The limitation: does not specifically target mitochondria. (Source: nlrp3-exploit-map.md)
 
@@ -157,7 +157,7 @@ The most efficient exploits hit three or more chokepoints:
 
 - **Berberine**: Suppresses NF-κB/TLR4 (CP1), reduces NLRP3/ASC/caspase-1 mRNA (CP1+CP4), remodels gut microbiota to reduce LPS priming (CP1). Dual benefit for Lynn's SIBO. Swiss Army knife compound. (Source: nlrp3-exploit-map.md)
 
-- **Oridonin**: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). Natural compound mimicking pharmaceutical-grade NLRP3 inhibitor. (Source: nlrp3-exploit-map.md)
+- **Oridonin**: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). Natural compound mimicking pharmaceutical-grade NLRP3 inhibitor. Two-tier potency: cell-free 0.5–2 µM, cellular human IC50 5.18 µM. (Source: nlrp3-exploit-map.md, nlrp3-inhibitor-screen.md ChEMBL cross-check)
 
 - **DMF (Dimethyl Fumarate)**: Nrf2 activator (CP1+CP2) AND gasdermin D succinator (CP6). Bridges first and last chokepoints. (Source: nlrp3-exploit-map.md)
 
@@ -165,6 +165,15 @@ The most efficient exploits hit three or more chokepoints:
 
 ## Pharmaceutical NLRP3 Inhibitors
 
+### Two-Tier Labeling: Direct Inhibitors vs. Pathway Modulators
+
+A ChEMBL cross-check (2026-04-23, source: nlrp3-inhibitor-screen.md) reveals that most compounds described as "NLRP3 inhibitors" in the literature lack curated human NLRP3 IC50 data. Only **dapansutrile** and **oridonin** have direct human NLRP3 bioactivity entries in ChEMBL (target CHEMBL1741208). Going forward, the wiki distinguishes:
+
+- **Direct NLRP3 inhibitor:** Binding/inhibition IC50 measured against human NLRP3 in a curated assay (ChEMBL). Currently: dapansutrile, oridonin, MCC950, tranilast (per separate literature).
+- **NLRP3 pathway modulator:** Functional IL-1β reduction demonstrated, but mechanism is upstream (NF-κB priming block, ROS reduction, K+ efflux prevention) or at unknown binding sites. Includes: quercetin, ursolic acid, beta-caryophyllene, curcumin, resveratrol, EGCG, carnosine, taurine.
+
+This distinction does not diminish the clinical relevance of pathway modulators — functional IL-1β suppression in MSU-stimulated macrophages is what Open Enzyme cares about. It is a rigor upgrade to mechanism framing.
+
 ### Approved or In Clinical Development
 
 - **Canakinumab (Ilaris)**: IL-1β monoclonal antibody. FDA-approved for gout and periodic fever syndromes. Very effective but expensive (~$300,000/year). Systemic immunosuppression risk.
@@ -173,6 +182,8 @@ The most efficient exploits hit three or more chokepoints:
 
 - **Dapansutrile (OLT1177)**: Oral NLRP3 inhibitor. Phase 2a trial for gout showed "marked target joint pain reduction in all dose groups" with swelling reduction by day 3. Good safety profile (no hepatotoxicity like MCC950). Currently in Phase 2/3 trials. This may eventually be the pharmaceutical solution. (Source: nlrp3-exploit-map.md)
 
+> ⚠️ **Species gap (ChEMBL cross-check):** Dapansutrile shows a ~1,000× potency gap between mouse and human cells — 1 nM IC50 in mouse J774A.1 cells vs. 1,000 nM (1.0 µM) in human MDM cells (*Eur J Med Chem* 2020/2023 via ChEMBL). The 2020 Phase 2a gout trial efficacy (52–84% pain reduction at 100–2,000 mg/day) is consistent with human-cell µM potency at high oral doses, not sub-nM potency. Mouse preclinical data overstates dapansutrile's potency relative to human cells. (source: nlrp3-inhibitor-screen.md ChEMBL appendix)
+
 - **MCC950 (CRID3)**: The first specific NLRP3 inhibitor. Binds the Walker B motif in the NACHT domain, blocking ATP hydrolysis required for oligomerization. Clinical development terminated due to hepatotoxicity in Phase 1 RA trial, but it defined the druggable target and validated the mechanism.
 
 ## Engineered Koji Opportunity
diff --git a/wiki/oridonin.md b/wiki/oridonin.md
index a98649a..44a5c0e 100644
--- a/wiki/oridonin.md
+++ b/wiki/oridonin.md
@@ -35,12 +35,24 @@ Oridonin's mechanism is a **Michael addition** — a nucleophilic attack by the
 
 ## Potency & Specificity
 
+### Two-Tier Potency: Cell-Free vs. Cellular IC50
+
+Oridonin's potency depends on which assay you measure. Both numbers are correct in context (source: nlrp3-inhibitor-screen.md ChEMBL cross-check):
+
+| Measurement | Value | System | Source |
+|---|---|---|---|
+| **Cell-free covalent kinetics** | 0.5–2 µM | NACHT domain Cys279 binding (Michael addition) | *Nat Commun* 2018 |
+| **Cellular human IC50** | 5.18 µM (5,180 nM) | Human THP-1 cells, LPS/ATP, pChEMBL=5.29 | *Eur J Med Chem* 2023 via ChEMBL |
+
+The 0.5–2 µM figure from the Nature Communications 2018 paper measures covalent binding kinetics at the NACHT domain — a cell-free/biochemical measurement. The 5.18 µM figure from ChEMBL is the curated human cellular IC50 in THP-1 macrophages. The ~2.5–10× gap between them reflects the difference between direct target engagement and the full cellular context (membrane permeability, intracellular protein binding, efflux).
+
+Both figures are physiologically achievable with oral supplementation at typical doses (50–200 mg/day).
+
 ### Active Concentration
 
-Oridonin exhibits dose-dependent inhibition of NLRP3 at **0.5–2 µM** concentrations:
-- Caspase-1 cleavage: reduced dose-dependently
-- IL-1β secretion: suppressed
-- Pyroptotic cell death: prevented
+Oridonin exhibits dose-dependent inhibition of NLRP3:
+- **Cell-free:** 0.5–2 µM — covalent Cys279 modification, NLRP3-NEK7 interaction blockade (In Vitro, *Nat Commun* 2018)
+- **Cellular:** 5.18 µM IC50 in human THP-1 — caspase-1 cleavage reduced, IL-1β secretion suppressed, pyroptotic cell death prevented (In Vitro, *Eur J Med Chem* 2023 via ChEMBL)
 
 These concentrations are physiologically achievable with oral supplementation.
 
@@ -102,7 +114,7 @@ Natural plant extracts vary significantly in bioavailability. Oridonin-specific
 |----------|--------|-----------|--------|------|----------|--------|
 | **Oridonin** | NLRP3 Cys279 | Covalent (natural) | Available now | ~$20–40/month | ✓ Irreversible | Good (traditional use) |
 | **MCC950** | NLRP3 Walker B | Non-covalent (pharma) | Preclinical | NA | ~30 min | Hepatotoxic (Phase 1) |
-| **Dapansutrile** | NLRP3 (general) | Direct inhibitor | Phase 3 (gout) | Unknown | Hours | Good (Phase 2 data) |
+| **Dapansutrile** | NLRP3 ATPase | Direct inhibitor | Phase 2a (gout, stalled) | Unknown | Hours | Good (Phase 2 data); **1,000× mouse-vs-human potency gap** (1 nM mouse IC50 vs 1,000 nM human cellular IC50 — source: ChEMBL) |
 | **Tranilast** | NLRP3 NACHT | Non-covalent (pharma) | Approved (Japan/Korea) | ~$30–50/month | Hours | Good (decades of use) |
 
 **Key observation:** Oridonin is a covalent NLRP3 inhibitor like MCC950, but unlike MCC950 it has not shown hepatotoxicity. It's available immediately, costs far less than clinical-stage drugs, and has the advantage of traditional use history (though this is not the same as modern clinical trial validation).
diff --git a/wiki/supplements-stack.md b/wiki/supplements-stack.md
index dcce8fd..6bb9bc0 100644
--- a/wiki/supplements-stack.md
+++ b/wiki/supplements-stack.md
@@ -129,7 +129,7 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition); blocks NLRP3-NEK7 interaction (CP2). Also activates Nrf2 and suppresses NF-κB (CP1/CP2).
 
-**Evidence level:** Established (Nature Communications 2018; dose-dependent IL-1β reduction at 0.5–2 µM)
+**Evidence level:** Established (Nature Communications 2018: cell-free covalent kinetics at 0.5–2 µM; human cellular IC50 = 5.18 µM in THP-1 via ChEMBL — both correct in context)
 
 **Dosing:** 50–100 mg/day
 

```
