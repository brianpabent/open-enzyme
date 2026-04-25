---
date: 2026-04-25
scenario: 01-chembl-ic50-cross-check
model: anthropic/claude-haiku-4-5
before_sha: c55ec09331283079fde836a65a02c8c0b9993c35
iterations: 35
completed: False
hit_iter_cap: True
input_tokens: 2466622
output_tokens: 14421
cost_usd: 2.0310
recall: 1.0
precision: 0.7777777777777778
files_changed: 9
diff_lines: 331
---

# Propagation eval — anthropic/claude-haiku-4-5 on 01-chembl-ic50-cross-check

## Done summary

(model did not call done() — see last_text)

## Last assistant text

```
Let me check if there are any other references to the compounds that need updating:
```

## Metrics

- Recall: 1.0
- Precision: 0.7777777777777778
- Files touched (9): ['index.md', 'wiki/GRAPH.md', 'wiki/cannabinoids-terpenes.md', 'wiki/gout-clinical-pipeline.md', 'wiki/nlrp3-exploit-map.md', 'wiki/nlrp3-inflammasome.md', 'wiki/nlrp3-inhibitor-screen.md', 'wiki/oridonin.md', 'wiki/supplements-stack.md']
- Expected but not touched: []
- Touched but not expected: ['index.md', 'wiki/nlrp3-inhibitor-screen.md']

## Diff

```diff
diff --git a/index.md b/index.md
index 6d41db4..273c7d3 100644
--- a/index.md
+++ b/index.md
@@ -58,9 +58,9 @@ See [wiki/validation-experiments.md](wiki/validation-experiments.md) for the ful
 
 ## Strategy & Practice
 
-- **[Gout Clinical Pipeline](wiki/gout-clinical-pipeline.md)** — Current ClinicalTrials.gov + PubMed snapshot (2026-04-23): ALLN-346 program terminated 2022, dapansutrile gout development stalled, canakinumab FDA-approved for gout Aug 2023, PRX-115 is the new systemic-uricase competitor. Refreshable quarterly via MCP.
+- **[Gout Clinical Pipeline](wiki/gout-clinical-pipeline.md)** — Current ClinicalTrials.gov + PubMed snapshot (2026-04-23): ALLN-346 program terminated 2022, dapansutrile gout development stalled (Phase 2a published 2020, no Phase 2b/3 registered), canakinumab FDA-approved for gout Aug 2023, PRX-115 is the new systemic-uricase competitor. **Dapansutrile species gap:** 1,000× potency difference between mouse (1 nM) and human cellular (1,000 nM) IC50. Refreshable quarterly via MCP.
 - **[Supplements Stack](wiki/supplements-stack.md)** — Practical NOW/SOON/FUTURE recommendations with dosing and evidence levels
-- **[Cannabinoids & Terpenes](wiki/cannabinoids-terpenes.md)** — CBD, CBG, CBC, THCV, beta-caryophyllene, myrcene: NLRP3 mechanisms, gout evidence, EPI applications; beta-caryophyllene has direct MSU gout animal model data
+- **[Cannabinoids & Terpenes](wiki/cannabinoids-terpenes.md)** — CBD, CBG, CBC, THCV, beta-caryophyllene, myrcene: NLRP3 mechanisms, gout evidence, EPI applications. **Beta-caryophyllene upgraded:** direct MSU gout animal model data (Front Pharmacol 2021; 100–400 mg/kg dose-dependently reduced ankle swelling, IL-1β, NLRP3/caspase-1 in rats). Only terpene/cannabinoid with gout-specific validation.
 - **[Validation Experiments](wiki/validation-experiments.md)** — All proposed experiments consolidated: in vitro, animal, and human self-experimentation phases
 - **[Bio-AI Tools](wiki/bio-ai-tools.md)** — Open source protein AI (ESM-2, ColabFold, Boltz-2, RFdiffusion2, ProteinMPNN, SPURS, DiffDock, CodonTransformer) + commercial tools (GPT-Rosalind, Amazon Bio Discovery, Coefficient Bio) + **Anthropic life-sciences marketplace** (17 à la carte plugins — PubMed, bioRxiv, ChEMBL, Open Targets, ClinicalTrials.gov MCP servers as Phase 0 core); project-specific prompts and workflow
 
@@ -104,7 +104,7 @@ Detailed technical analyses for the uricase and koji engineering tracks.
 **Koji / *A. oryzae* track:**
 - **[Koji Construct Design](wiki/koji-construct-design.md)** — *A. oryzae* uricase via amyB promoter (starch-inducible, 6–10× baseline). Expected 40–80 mg/g koji.
 - **[Digestive Enzyme Optimization](wiki/digestive-enzyme-optimization.md)** — RIB40 strain; lipase 1,813–2,280 U/g koji; rice bran optimal substrate; CRISPR tglA target. 10–15 g koji ≈ Creon equivalence.
-- **[NLRP3 Inhibitor Screen](wiki/nlrp3-inhibitor-screen.md)** — Top candidates: ursolic acid (8.59 g/L yeast), quercetin (930 mg/L), carnosine. Kojic acid native production (3–5 g/L) flagged as free bonus.
+- **[NLRP3 Inhibitor Screen](wiki/nlrp3-inhibitor-screen.md)** — **Two-tier potency framing:** Only oridonin (5.18 µM human IC50) and dapansutrile (1,000 nM human IC50) have curated human NLRP3 IC50 in ChEMBL. Everything else is a "pathway modulator" (NF-κB priming block, ROS reduction, K+ efflux prevention) rather than direct inhibitor. Top candidates: ursolic acid (8.59 g/L yeast), quercetin (930 mg/L, triple mechanism: NF-κB + 5-LOX + xanthine oxidase), carnosine (unique hyperuricemia data). Kojic acid native production (3–5 g/L) flagged as free bonus. Beta-caryophyllene validated in MSU gout animal model (Front Pharmacol 2021).
 
 **Cross-platform:**
 - **[Cross-Validation (Thesis Stress Test)](wiki/cross-validation.md)** — Risk matrix across all tracks; NLRP3 suppression confirmed; variant redundancy tested; ALLN-346 clinical bridge.
diff --git a/wiki/GRAPH.md b/wiki/GRAPH.md
index c9bd1bf..6374632 100644
--- a/wiki/GRAPH.md
+++ b/wiki/GRAPH.md
@@ -71,11 +71,11 @@ graph TB
         I4["IL-10 Promotion"]
     end
 
-    subgraph Inhibitors["NLRP3 INHIBITORS"]
-        J1["Oridonin"]
-        J2["Disulfiram"]
-        J3["ASC Block"]
-        J4["Gasdermin D Block"]
+    subgraph Inhibitors["NLRP3 INHIBITORS & MODULATORS"]
+        J1["Oridonin (Direct Inhibitor)"]
+        J2["Disulfiram (Gasdermin D)"]
+        J3["Dapansutrile (Direct, 1µM human IC50)"]
+        J4["Pathway Modulators (Quercetin, Ursolic Acid, Carnosine, etc.)"]
     end
 
     subgraph Cannabinoids["CANNABINOIDS / TERPENES"]
@@ -169,13 +169,17 @@ graph TB
     B5 --> A3
     
     %% Cannabinoid/terpene relationships
-    M1 -->|"P2X7/NF-kB"| C2
-    M2 -->|"CB2/TLR4/NLRP3 — MSU gout model"| C2
-    M2 -->|"CB2 agonism — neutrophil block"| C1
+    M1 -->|"P2X7/NF-kB (upstream)"| C2
+    M2 -->|"CB2/TLR4/NLRP3 — VALIDATED MSU gout model"| C2
+    M2 -->|"CB2 agonism — neutrophil recruitment block"| C1
     M3 -->|"NF-kB/MAPK — CIA arthritis"| C2
     M3 -->|"CBG colitis data"| B3
     M4 -->|"CB2 agonism (Ki 7.5 nM)"| C2
     M1 -->|"barrier support"| H1
+    
+    %% Quercetin triple mechanism
+    J4 -->|"NF-kB + 5-LOX (neutrophil block) + XO"| C2
+    J4 -->|"Xanthine oxidase inhibition"| B1
 
     %% Styling
     style Core fill:#ffe6e6
diff --git a/wiki/cannabinoids-terpenes.md b/wiki/cannabinoids-terpenes.md
index b43d33a..57eff46 100644
--- a/wiki/cannabinoids-terpenes.md
+++ b/wiki/cannabinoids-terpenes.md
@@ -152,9 +152,9 @@ THCV has stronger CB2 affinity than beta-caryophyllene and new NLRP3 data.
 
 ## 2. Terpenes with Anti-Inflammatory Properties
 
-### Beta-Caryophyllene — UPGRADED: Direct Gout Animal Model Data
+### Beta-Caryophyllene — UPGRADED: Direct Gout Animal Model Data (Animal Model)
 
-The inhibitor screen classified beta-caryophyllene as Tier 4 with "no gout evidence." That was incorrect — a 2021 paper demonstrates direct efficacy in an MSU gout animal model.
+The inhibitor screen classified beta-caryophyllene as Tier 4 with "no gout evidence." That was incorrect — a 2021 paper demonstrates direct efficacy in an MSU gout animal model. This finding recontextualizes beta-caryophyllene from a speculative CB2 agonist to a gout-validated NLRP3 pathway modulator. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check appendix)
 
 **Key findings in MSU-induced gouty arthritis (animal model):**
 
diff --git a/wiki/gout-clinical-pipeline.md b/wiki/gout-clinical-pipeline.md
index 390beaa..f3855be 100644
--- a/wiki/gout-clinical-pipeline.md
+++ b/wiki/gout-clinical-pipeline.md
@@ -101,6 +101,8 @@ According to PubMed, Dapansutrile (OLT1177) Phase 2a proof-of-concept in gout wa
 - 25/34 patients had treatment-emergent AEs (mostly metabolism and GI); 2 SAEs (one flare worsening, one coronary stenosis unrelated)
 - **Conclusion:** "Dapansutrile is a specific NLRP3 inflammasome inhibitor with a satisfactory safety profile and efficacy in the reduction of target joint pain."
 
+**Critical species gap (ChEMBL cross-check, April 2026):** Dapansutrile shows **1 nM IC50 in mouse J774A.1 cells** (preclinical) vs. **1,000 nM IC50 in human MDM cells** (LPS+nigericin, Eur J Med Chem 2023). This 1,000× potency gap recontextualizes the Phase 2a trial: the high oral doses (100–2,000 mg/day) were required to achieve human-cell-equivalent NLRP3 suppression, not because the compound is weak, but because mouse preclinical assays dramatically overestimated human efficacy. The clinical efficacy (52–84% pain reduction) is consistent with the human cellular IC50 (~1 µM) at high oral doses. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check appendix)
+
 **What happened next:**
 - No Phase 2b or Phase 3 in gout on ClinicalTrials.gov (as of 2026-04-23)
 - Olatec pivoted to heart failure (Phase 1b NCT03534297, completed 2019) and COVID-19 (Phase 2 NCT04540120, terminated 2022)
diff --git a/wiki/nlrp3-exploit-map.md b/wiki/nlrp3-exploit-map.md
index f6c1af4..9c1c2d6 100644
--- a/wiki/nlrp3-exploit-map.md
+++ b/wiki/nlrp3-exploit-map.md
@@ -113,11 +113,13 @@ A. oryzae already produces kojic acid (a tyrosinase inhibitor). With the synthet
 
 #### Oridonin
 
-> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. Active at 0.5–2 µM. Same binding site as MCC950.
+> **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition) → blocks NLRP3-NEK7 interaction → prevents inflammasome assembly. **Two-tier potency:** Cell-free kinetic IC50 0.5–2 µM (Nat Commun 2018); human cellular IC50 5.18 µM (Eur J Med Chem 2023, ChEMBL-curated). Same binding site as MCC950.
 
 This is the gem of the natural compound world for NLRP3 inhibition. Oridonin, an ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens, covalently and specifically modifies NLRP3 at cysteine 279. This is the same domain that MCC950 targets — the NACHT domain. By forming an irreversible covalent bond, oridonin blocks the NLRP3-NEK7 interaction that's essential for inflammasome assembly.
 
-Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
+Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage, IL-1β secretion, and pyroptotic cell death at concentrations of 0.5–2 µM in cell-free systems. In human THP-1 monocytes (LPS/ATP-stimulated), the cellular IC50 is 5.18 µM. It's NLRP3-specific — doesn't affect NLRC4 or AIM2 inflammasomes. And recent 2025 research on oridonin analogs shows you can engineer even more potent derivatives.
+
+**Two-tier interpretation:** The cell-free kinetic number (0.5–2 µM) reflects intrinsic covalent binding rate to purified NLRP3. The cellular IC50 (5.18 µM) reflects the concentration needed to suppress inflammasome activation in intact human cells, accounting for membrane permeability, cellular metabolism, and competing off-target effects. The cellular IC50 is the more clinically relevant metric for oral supplementation. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check appendix)
 
 The dual hit: Beyond NLRP3, oridonin also activates Nrf2 and suppresses NF-κB independently. So it hits CP1 AND CP2 through different mechanisms.
 
diff --git a/wiki/nlrp3-inflammasome.md b/wiki/nlrp3-inflammasome.md
index 2bd5ea7..bab425d 100644
--- a/wiki/nlrp3-inflammasome.md
+++ b/wiki/nlrp3-inflammasome.md
@@ -75,7 +75,7 @@ The NLRP3 inflammasome pathway operates as a sequential cascade with six distinc
 
 - **Beta-hydroxybutyrate (BHB)**: The ketone body produced during fasting or ketogenic diet. BHB prevents potassium efflux, reduces ASC speck formation, and directly inhibits NLRP3 assembly. Notably, BHB is NOT dependent on AMPK, autophagy, or ROS reduction—it is a direct inhibitory effect on NLRP3 oligomerization. In rodent models, a ketogenic diet significantly reduced gout flare severity. Critical insight: traditional concern that ketosis raises uric acid is true short-term (ketones compete with urate for renal excretion), but with uricase handling uric acid clearance, ketosis becomes pure inflammasome suppression. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)
 
-- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. Active at 0.5–2 µM. Published in Nature Communications: oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md)
+- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. **Two-tier potency:** Cell-free kinetic IC50 0.5–2 µM (Nat Commun 2018); human cellular IC50 5.18 µM in THP-1 macrophages (Eur J Med Chem 2023, ChEMBL-curated). Published in Nature Communications: oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md, nlrp3-inhibitor-screen.md)
 
 - **NAC (N-Acetyl Cysteine)**: Replenishes glutathione, the master intracellular antioxidant. Reduces mtROS, thus reducing the Signal 2 trigger for NLRP3 assembly. Dose: 600–1200 mg daily. Widely available, inexpensive, well-tolerated. The limitation: does not specifically target mitochondria. (Source: nlrp3-exploit-map.md)
 
diff --git a/wiki/nlrp3-inhibitor-screen.md b/wiki/nlrp3-inhibitor-screen.md
index 7876498..728be1b 100644
--- a/wiki/nlrp3-inhibitor-screen.md
+++ b/wiki/nlrp3-inhibitor-screen.md
@@ -37,6 +37,21 @@ This screen evaluates food-derived NLRP3 inflammasome inhibitors producible by e
 
 ---
 
+## Critical Framing: Two-Tier Potency and "Inhibitor" vs. "Modulator" Terminology
+
+**ChEMBL IC50 Cross-Check Finding (April 2026):** Only two compounds in this screen have curated human NLRP3 IC50 values in the EMBL-EBI ChEMBL v34 database:
+
+1. **Dapansutrile (OLT1177):** 1,000 nM (1.0 µM) in human MDM cells, LPS+nigericin (Eur J Med Chem 2023)
+2. **Oridonin:** 5,180 nM (5.18 µM) in human THP-1 macrophages, LPS/ATP (Eur J Med Chem 2023)
+
+**Everything else in this screen is a "pathway modulator," not a direct "NLRP3 inhibitor."** Quercetin, ursolic acid, carnosine, taurine, resveratrol, EGCG, curcumin, and beta-caryophyllene all suppress NLRP3 inflammasome activation through upstream mechanisms (NF-κB priming block, ROS reduction, K+ efflux prevention, autophagy induction) rather than direct NLRP3 binding or inhibition. This is not a weakness — it's mechanistic clarity. Multi-target pathway modulation may be more robust than single-agent direct inhibition.
+
+**Dapansutrile species gap caveat:** The published 1 nM mouse IC50 (J774A.1 cells) vs. 1,000 nM human cellular IC50 represents a 1,000× potency gap. This recontextualizes the 2020 Phase 2a trial (52–84% pain reduction at 100–2,000 mg/day) as requiring high oral doses to achieve human-cell-equivalent NLRP3 suppression. The clinical efficacy is consistent with the human cellular IC50, not the mouse preclinical IC50.
+
+**Oridonin two-tier potency:** The cell-free covalent kinetics number (0.5–2 µM, Nat Commun 2018) and the cellular human IC50 (5.18 µM, Eur J Med Chem 2023) both are correct in their respective contexts. Cell-free kinetics measure intrinsic binding rate to purified NLRP3. Cellular IC50 measures the concentration needed to suppress inflammasome activation in intact human cells, accounting for membrane permeability, cellular metabolism, and competing off-target effects. The cellular IC50 is the more clinically relevant metric for oral supplementation.
+
+---
+
 ## Candidate Compounds Evaluated
 
 ### Tier 1: Strong NLRP3 Evidence + Established Microbial Production
@@ -422,11 +437,11 @@ This screen evaluates food-derived NLRP3 inflammasome inhibitors producible by e
 
 ## Ranking: Top 5 Candidates by Evidence × Feasibility × Safety
 
-### **Rank 1: Ursolic Acid (Triterpene)**
+### **Rank 1: Ursolic Acid (Triterpene) — Pathway Modulator**
 
 | Criterion | Score | Justification |
 |-----------|-------|---|
-| **NLRP3 evidence** | 8/10 | Animal models (Kawasaki disease, vasculitis); mechanism clear (NF-κB, NLRP3, caspase-1); NOT gout-tested but extrapolates from OA models |
+| **NLRP3 evidence** | 8/10 | Animal models (Kawasaki disease, vasculitis); mechanism clear (NF-κB, NLRP3, caspase-1); NOT gout-tested but extrapolates from OA models. **Classification: Pathway modulator** (no direct NLRP3 IC50 in ChEMBL) |
 | **Production feasibility** | 10/10 | **8.59 g/L bioreactor titer (2024 record)**; established MVA + triterpene synthase pathway; S. cerevisiae GRAS host |
 | **Food safety** | 10/10 | GRAS status; present in apples, rosemary, oregano; safe up to 100–200 mg/day |
 | **Bioavailability** | 6/10 | Poor water solubility; requires lipid formulation; stable triterpene resists GI degradation |
@@ -437,26 +452,26 @@ This screen evaluates food-derived NLRP3 inflammasome inhibitors producible by e
 
 ---
 
-### **Rank 2: Quercetin (Flavonoid)**
+### **Rank 2: Quercetin (Flavonoid) — Pathway Modulator with Triple Mechanism**
 
 | Criterion | Score | Justification |
 |-----------|-------|---|
-| **NLRP3 evidence** | 8/10 | Gout-specific animal model (MSU-induced arthritis); 200–400 mg/kg reduces joint swelling, IL-1β, TNF-α; IC50 ~11 μM; NOT human RCT |
+| **NLRP3 evidence** | 8/10 | Gout-specific animal model (MSU-induced arthritis); 200–400 mg/kg reduces joint swelling, IL-1β, TNF-α. **Classification: Pathway modulator** (no direct NLRP3 IC50 in ChEMBL; acts via NF-κB suppression). **Bonus mechanism:** 5-LOX inhibition (IC50 300 nM) suppresses leukotriene-driven neutrophil recruitment in gout flares. |
 | **Production feasibility** | 9/10 | 20.38 ± 2.57 mg/L in engineered S. cerevisiae; established PAL/CHS/CHI/F3H pathway; proven scalability |
 | **Food safety** | 10/10 | GRAS; ubiquitous in plant foods; safe up to 1 g/day |
 | **Bioavailability** | 5/10 | Poor (aglycone form); glycosidic formulations improve absorption; low bioavailability limits clinical effect |
 | **Gout-specificity** | 9/10 | **Direct gout animal evidence; suppresses IL-1β in MSU models** |
-| **Overall Score** | **41/50** | **Best gout evidence + established production; adequate titers** |
+| **Overall Score** | **41/50** | **Best gout evidence + established production; triple mechanism (NF-κB + xanthine oxidase + 5-LOX)** |
 
 **Recommendation:** PRIMARY NLRP3 INHIBITOR CANDIDATE for gout. Synergize with uricase in same S. cerevisiae construct. Quercetin production (20 mg/L) achieves therapeutic dosing in fermented beverage (500 mL @ 20 mg/L = 10 mg quercetin per dose; target ~50 mg/dose via fermenter optimization or co-fermentation).
 
 ---
 
-### **Rank 3: Carnosine (Dipeptide)**
+### **Rank 3: Carnosine (Dipeptide) — Pathway Modulator with Unique Hyperuricemia Data**
 
 | Criterion | Score | Justification |
 |-----------|-------|---|
-| **NLRP3 evidence** | 9/10 | **Direct hyperuricemia rat evidence:** Carnosine reduces serum uric acid AND inhibits inflammation; suppresses NLRP3, caspase-1, p-p65, p-JNK, URAT1, GLUT9 |
+| **NLRP3 evidence** | 9/10 | **Direct hyperuricemia rat evidence:** Carnosine reduces serum uric acid AND inhibits inflammation; suppresses NLRP3, caspase-1, p-p65, p-JNK, URAT1, GLUT9. **Classification: Pathway modulator** (no direct NLRP3 IC50 in ChEMBL; acts via ROS/NF-κB/URAT1 suppression). |
 | **Production feasibility** | 6/10 | Requires β-alanine + histidine + carnosine synthase; NOT extensively published for yeast; estimated 100–300 mg/L based on dipeptide analogs |
 | **Food safety** | 10/10 | GRAS; meat-derived amino acid; safe up to 2 g/day |
 | **Bioavailability** | 10/10 | **Excellent; dipeptide transporters ensure intact absorption** |
diff --git a/wiki/oridonin.md b/wiki/oridonin.md
index a98649a..6e0853f 100644
--- a/wiki/oridonin.md
+++ b/wiki/oridonin.md
@@ -35,14 +35,21 @@ Oridonin's mechanism is a **Michael addition** — a nucleophilic attack by the
 
 ## Potency & Specificity
 
-### Active Concentration
+### Active Concentration: Two-Tier Potency
 
-Oridonin exhibits dose-dependent inhibition of NLRP3 at **0.5–2 µM** concentrations:
+Oridonin exhibits dose-dependent inhibition of NLRP3 at different concentrations depending on the assay context:
+
+**Cell-free / kinetic assays (covalent binding):** 0.5–2 µM (Nat Commun 2018)
 - Caspase-1 cleavage: reduced dose-dependently
 - IL-1β secretion: suppressed
 - Pyroptotic cell death: prevented
+- **Mechanism:** Covalent Cys279 binding kinetics measured in cell-free systems
+
+**Human cellular assay (THP-1 macrophages):** 5.18 µM (Eur J Med Chem 2023, ChEMBL curated)
+- IL-1β secretion endpoint in LPS/ATP-stimulated human monocytes
+- **Mechanism:** Functional NLRP3 inflammasome inhibition in living cells
 
-These concentrations are physiologically achievable with oral supplementation.
+**Interpretation:** Both measurements are correct in their respective contexts. The cell-free kinetic number (0.5–2 µM) reflects the intrinsic covalent binding rate to purified NLRP3 protein. The cellular IC50 (5.18 µM) reflects the concentration needed to suppress inflammasome activation in intact human cells, accounting for membrane permeability, cellular metabolism, and competing off-target effects. The cellular IC50 is the more clinically relevant metric for oral supplementation. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check appendix)
 
 ### NLRP3-Specific
 
@@ -98,12 +105,14 @@ Natural plant extracts vary significantly in bioavailability. Oridonin-specific
 
 ## Comparison: Oridonin vs. Pharmaceutical NLRP3 Inhibitors
 
-| Compound | Target | Mechanism | Status | Cost | Duration | Safety |
-|----------|--------|-----------|--------|------|----------|--------|
-| **Oridonin** | NLRP3 Cys279 | Covalent (natural) | Available now | ~$20–40/month | ✓ Irreversible | Good (traditional use) |
-| **MCC950** | NLRP3 Walker B | Non-covalent (pharma) | Preclinical | NA | ~30 min | Hepatotoxic (Phase 1) |
-| **Dapansutrile** | NLRP3 (general) | Direct inhibitor | Phase 3 (gout) | Unknown | Hours | Good (Phase 2 data) |
-| **Tranilast** | NLRP3 NACHT | Non-covalent (pharma) | Approved (Japan/Korea) | ~$30–50/month | Hours | Good (decades of use) |
+| Compound | Target | Mechanism | Human IC50 | Status | Cost | Safety |
+|----------|--------|-----------|--------|--------|------|--------|
+| **Oridonin** | NLRP3 Cys279 | Covalent (natural) | 5.18 µM (THP-1) | Available now | ~$20–40/month | Good (traditional use) |
+| **MCC950** | NLRP3 Walker B | Non-covalent (pharma) | ~7.5 nM | Preclinical | NA | Hepatotoxic (Phase 1) |
+| **Dapansutrile** | NLRP3 ATPase | Direct inhibitor | 1,000 nM (human cells) | Phase 2/3 (gout) | Unknown | Good (Phase 2 data) |
+| **Tranilast** | NLRP3 NACHT | Non-covalent (pharma) | Not curated in ChEMBL | Approved (Japan/Korea) | ~$30–50/month | Good (decades of use) |
+
+**Key insight:** Oridonin's cellular IC50 (5.18 µM) is ~700× weaker than MCC950 (7.5 nM) but ~5× stronger than dapansutrile's human cellular IC50 (1,000 nM). Dapansutrile's mouse preclinical IC50 (1 nM) is 1,000× more potent than its human cellular IC50 — a critical species gap that recontextualizes the 2020 Phase 2a trial as requiring high oral doses (100–2,000 mg/day) to achieve human-cell-equivalent NLRP3 suppression. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check appendix)
 
 **Key observation:** Oridonin is a covalent NLRP3 inhibitor like MCC950, but unlike MCC950 it has not shown hepatotoxicity. It's available immediately, costs far less than clinical-stage drugs, and has the advantage of traditional use history (though this is not the same as modern clinical trial validation).
 
diff --git a/wiki/supplements-stack.md b/wiki/supplements-stack.md
index dcce8fd..a16a716 100644
--- a/wiki/supplements-stack.md
+++ b/wiki/supplements-stack.md
@@ -125,11 +125,13 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 ### Oridonin (Rabdosia rubescens Extract)
 
-**Category:** Natural Compound / NLRP3 Inhibitor
+**Category:** Natural Compound / Direct NLRP3 Inhibitor
 
 **Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition); blocks NLRP3-NEK7 interaction (CP2). Also activates Nrf2 and suppresses NF-κB (CP1/CP2).
 
-**Evidence level:** Established (Nature Communications 2018; dose-dependent IL-1β reduction at 0.5–2 µM)
+**Evidence level:** Established (Nature Communications 2018; cell-free kinetic IC50 0.5–2 µM; human cellular IC50 5.18 µM in THP-1 macrophages per Eur J Med Chem 2023, ChEMBL-curated)
+
+**Potency note:** Oridonin is one of only two compounds in the supplement/natural product space with a curated human NLRP3 IC50 in ChEMBL (the other being dapansutrile at 1,000 nM). Most other "NLRP3 inhibitors" in the stack are more accurately "NLRP3 pathway modulators" acting upstream (NF-κB priming block, ROS reduction, K+ efflux prevention) rather than direct NLRP3 binding. (Source: nlrp3-inhibitor-screen.md, ChEMBL IC50 cross-check)
 
 **Dosing:** 50–100 mg/day
 
@@ -169,6 +171,35 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 ---
 
+### Beta-Caryophyllene (Black Pepper / Clove Extract)
+
+**Category:** Terpene / CB2 Agonist
+
+**Mechanism:** 
+- CB2 receptor agonism (Ki 155 nM; selective CB2 agonist)
+- TLR4/MyD88 suppression (CP1 — NF-κB priming block)
+- Direct NLRP3 assembly suppression (CP2)
+- Neutrophil recruitment suppression (CB2-mediated chemokine reduction: CXCL1/KC, LTB4)
+
+**Evidence level:** Animal Model (MSU-induced gouty arthritis in rats, 2021)
+
+**Gout-specific data:** 
+- Model: MSU crystal injection into rat ankle joints (standard gout flare model)
+- Doses: 100, 200, 400 mg/kg (single daily oral dose)
+- Results: Significant, dose-dependent reduction in ankle swelling, serum IL-1β/IL-6/TNF-α, synovial NLRP3/caspase-1/ASC
+- Computational docking: CDOCKER interaction energy = 31.92 kcal/mol (suggests NLRP3 direct binding)
+- Citation: *Front Pharmacol* 2021;12:651305. PMID: 33967792
+
+**Dosing:** 50–100 mg/day (from standardized black pepper extract or clove oil)
+
+**Form:** Black pepper extract (piperine standardized), clove essential oil, or food sources (black pepper, cloves, hops)
+
+**Practical note:** Beta-caryophyllene is GRAS (food additive), readily available, and has direct MSU gout animal model evidence — the only terpene or cannabinoid with this distinction. Acts at CP1 (NF-κB/TLR4) and CP2 (NLRP3/caspase-1). Additive to oridonin and BHB. (Source: cannabinoids-terpenes.md, nlrp3-inhibitor-screen.md)
+
+**Cost:** $10–20/month
+
+---
+
 ### Cherry Extract (Tart Cherry Concentrate)
 
 **Category:** Botanical
@@ -208,11 +239,12 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 ### Quercetin (Phytosome Form Preferred)
 
-**Category:** Flavonoid
+**Category:** Flavonoid / Multi-Target
 
 **Mechanism:** 
 - NF-κB inhibition (CP1)
-- Xanthine oxidase inhibition (direct uric acid production reduction)
+- Xanthine oxidase inhibition (direct uric acid production reduction) — IC50 ~300 nM (ChEMBL-curated)
+- **5-Lipoxygenase (5-LOX) inhibition** — IC50 = 300 nM (J Med Chem 1991). 5-LOX produces leukotrienes (LTB4) that drive neutrophil chemotaxis in gout flares. This is a missed opportunity in the gout context: quercetin's 5-LOX inhibition is stronger than its xanthine oxidase activity and directly suppresses neutrophil recruitment.
 - Mast cell stabilization
 
 **Evidence level:** Established
@@ -221,7 +253,7 @@ Compounds currently accessible, with strong evidence, that can be started immedi
 
 **Form:** Phytosome (Quercefit) has ~20× better absorption than standard quercetin
 
-**Practical note:** Dual mechanism: hits both CP1 and uric acid production. Synergizes with sulforaphane (both Nrf2 activators). (Source: nlrp3-exploit-map.md)
+**Practical note:** Triple mechanism: hits CP1 (NF-κB), uric acid production (xanthine oxidase), AND neutrophil recruitment (5-LOX). Synergizes with sulforaphane (both Nrf2 activators). (Source: nlrp3-exploit-map.md, nlrp3-inhibitor-screen.md)
 
 **Cost:** $15–25/month
 

```
