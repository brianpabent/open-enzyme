---
title: "NLRP3 Inhibitor Discovery Screen: Food-Derived Compounds for Engineered Microbe Production"
date: 2026-04-21
tags: ["NLRP3", "inflammasome", "inhibitors", "polyphenols", "terpenoids", "fermentation", "gout"]
related:
  - gout-deep-dive.md
  - nlrp3-exploit-map.md
  - engineered-yeast-uricase-proposal.md
  - engineered-koji-protocol.md
  - blood-barrier-exploits.md
  - koji-construct-design.md
  - cross-validation.md
  - nlrp3-inflammasome.md
sources:
  - "Inflammopharmacology 2025: NLRP3 natural products review"
  - "PubMed Central: Polyphenols and NLRP3"
  - "Cell Reports Medicine, October 2025: PULSE probiotic"
  - "ACS Synthetic Biology: S. cerevisiae engineered production"
  - "Applied Microbiology and Biotechnology 2025: Ergothioneine in A. oryzae"
  - "Scientific Reports 2025: Georgia State CRISPR S. cerevisiae"
---

# NLRP3 Inhibitor Discovery Screen: Food-Derived Compounds for Engineered Microbe Production

## Executive Summary

This screen evaluates food-derived NLRP3 inflammasome inhibitors producible by engineered *S. cerevisiae* or *A. oryzae*, ranked by:

> **TCM lineage note (2026-05-05):** Several compounds in this screen have explicit TCM materia medica lineage — oridonin (*Rabdosia rubescens* / Dong Ling Cao 冬凌草), EGCG (green tea / Lu Cha 绿茶), resveratrol (*Polygonum cuspidatum* / Hu Zhang 虎杖), curcumin (turmeric / Jiang Huang 姜黄), berberine (*Coptis chinensis* / Huang Lian 黄连). The methodology for applying modern scientific rigor to these compounds — including chokepoint mapping, ChEMBL cross-check, and bioavailability-honest framing — is formalized in [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md). (source: tcm-modern-rigor-intersection.md)
1. **NLRP3 inhibition evidence strength** (clinical > animal > in vitro > mechanistic)
2. **Microbial production feasibility** (established biosynthetic pathways, expression titers, known host organisms)
3. **Food-safety status** (GRAS or traditional use in fermented foods)

**Benchmark compounds:**
- **MCC950** — IC50 ~7.5 nM (crystalline NLRP3 inhibitor, not food-derived)
- **Oridonin** — Covalent Cys279 binder (plant diterpenoid, not easily synthesized)
- **Tranilast** — Non-selective mast cell stabilizer
- **OLT1177 (dapansutrile)** — Phase 2a gout trial success, direct NLRP3 ATPase inhibitor

> **Species-gap caveat (methodological standard, 2026-04-23)**: Rodent cellular IC50 values for NLRP3 inhibitors routinely diverge from human cellular IC50 by up to 3 orders of magnitude. Example: dapansutrile IC50 = 1 nM in mouse J774A.1 cells vs. 1,000 nM (1 μM) in human MDM cells under LPS+nigericin stimulation (ChEMBL v34). Every rodent-derived IC50 in this document should be read with that translation uncertainty in mind. When evaluating new compounds, prefer human-cell (THP-1, PBMC, human MDM) data over rodent cellular assays. (source: chembl-cross-check.md)

---

## Candidate Compounds Evaluated

### Tier 1: Strong NLRP3 Evidence + Established Microbial Production

#### 1. **Quercetin (3,3',4',5,7-pentahydroxyflavone)**

**NLRP3 Mechanism:** (In vitro & animal model)
- Suppresses NLRP3 inflammasome activation and ASC oligomerization
- Inhibits NF-κB and NLRP3 expression via SIRT1 pathway
- Mechanism: mitochondrial protection, upstream IL-1β suppression

**Evidence Level:**
- **In vitro:** Quercetin (IC50 ~11.0 μM) blocks NLRP3 in macrophage lysates
- **Animal (MSU-induced gout):** 200–400 mg/kg quercetin in rats reduced joint edema, IL-1β, TNF-α, COX-2, and PGE2 within 24 h (Clinical trial evidence: NOT published; mechanistic hypothesis only)
- **Human gout:** Quercetin prevents hyperuricemia-associated gouty arthritis via NLRP3/NF-κB inactivation (recent 2025 evidence in literature, but not RCT data)

**Production Feasibility:**
- **S. cerevisiae:** Engineered strains produce kaempferol (26.57 ± 2.66 mg/L) and quercetin (20.38 ± 2.57 mg/L) from glucose via heterologous expression of plant PAL, CHS, CHI, and F3H genes
- **Pathway requirement:** Phenylpropanoid pathway (6–8 heterologous plant genes from *Arabidopsis*, *Petroselinum*)
- **Feasibility:** HIGH — established pathway reconstruction in GRAS yeast; titers sufficient for oral dosing (assuming 10 mg per dose)

**Food Safety:**
- GRAS status: Quercetin-rich foods (onions, apples, berries) widely consumed
- Solubility: Low (poor bioavailability as aglycone)
- Dosing in fermented products: 50–100 mg/mL achievable via engineered yeast

**Advantages:**
- Multiple synergistic mechanisms (antioxidant + direct NLRP3 block)
- Co-production feasible with uricase construct in same yeast

**Limitations:**
- IC50 (11 μM) >> benchmark MCC950 (7.5 nM); ~1500× weaker
- No human gout RCT
- Bioavailability severely limited by poor water solubility

**Ranking Rationale:** Tier 1 due to gout-specific animal evidence and mature biosynthetic production platform. Weakness is IC50 potency vs. benchmark.

---

#### 2. **Ursolic Acid (3β-hydroxy-urs-12-en-28-oic acid)**

**NLRP3 Mechanism:** (In vitro & animal)
- Pentacyclic triterpene; suppresses NF-κB, AP-1, NF-AT transcription factors
- Blocks NLRP3 inflammasome assembly and caspase-1 activation
- Inhibits pro-IL-1β expression upstream

**Evidence Level:**
- **In vitro:** Ursolic acid suppresses NLRP3 inflammasome in multiple cell types (macrophages, endothelial cells)
- **Animal (Kawasaki disease, vascular injury model):** Ursolic acid inhibited NLRP3 inflammasome activation and reduced vascular smooth muscle injury
- **Gout-specific:** NOT directly tested; evidence inferred from osteoarthritis models showing NLRP3 suppression

**Production Feasibility:**
- **S. cerevisiae:** Recently engineered to produce ursolic acid and oleanolic acid via combinatorial metabolic engineering
  - **Recent 2024 achievement:** 1083.62 mg/L in shake flask; **8.59 g/L in fed-batch 5L bioreactor** (highest microbial titer reported)
  - **Pathway:** Mevalonate (MVA) pathway optimization + heterologous OSC (oxidosqualene cyclase), CYP (cytochrome P450), CPR (cytochrome P450 reductase) from plants (*Catharanthus roseus*, *Glycyrrhiza*)
  - **Host:** GRAS *S. cerevisiae* (food-grade)

**Food Safety:**
- GRAS status: Ursolic acid present in apples, rosemary, oregano, thyme
- Traditional use: Chinese medicine (*Radix Salviae Divinorum*)
- Solubility: Poor in water; typically requires lipid formulation
- Dosing: 100–200 mg/day in human trials

**Advantages:**
- **HIGHEST microbial production titer** (8.59 g/L bioreactor) — exceeds any polyphenol production
- Structurally stable triterpene; resistant to gastrointestinal degradation
- Can be formulated with lipid excipients in fermented beverage or solid dosage
- Multiple mechanistic targets beyond NLRP3 (anti-inflammatory, anti-oxidant)

**Limitations:**
- IC50 not quantified vs. MCC950 or oridonin (appears to be in μM range from structure activity)
- No gout-specific animal evidence (extrapolation from OA models)
- Requires two additional metabolic engineering modules (MVA optimization + triterpene synthase pathway)

**Ranking Rationale:** Tier 1 due to exceptional production titer (8.59 g/L), GRAS status, and structural stability. NLRP3 mechanism confirmed but not gout-tested.

---

#### 3. **Taurine (2-aminoethanesulfonic acid)**

**NLRP3 Mechanism:** (Animal & mechanistic)
- Amino acid; upstream inhibitor of NLRP3 inflammasome assembly
- Mechanism: prevents K+ efflux → blocks inflammasome speck formation
- Restores intracellular taurine that is depleted during NLRP3 activation
- Also reduces pyroptosis (GSDMD-mediated cell death)

**Evidence Level:**
- **In vitro:** Taurine restoration in cultured macrophages reverses K+ efflux-induced NLRP3 speck assembly
- **Animal (sepsis, cardiac injury, hemorrhage):** Taurine infusion protected mice against sepsis mortality, reduced myocardial IL-1β at levels comparable to CP-456,773 (NLRP3 inhibitor) and pyrrolidine dithiocarbamate (NF-κB inhibitor); reduces NLRP3, caspase-1, GSDMD
- **Gout-specific:** NOT tested; mechanistic inference only

**Production Feasibility:**
- **S. cerevisiae or *A. oryzae*:** Taurine synthesis pathway is natural to mammals; bacteria also produce it
- **Heterologous pathway:** Cysteine → cysteic acid → taurine (requires cysteinyl-CoA synthetase, cysteate sulfinyltransferase)
- **Engineering status:** Feasible; taurine biosynthesis genes from *E. coli* or *Corynebacterium* have been cloned
- **Titers:** Not extensively published for engineered yeast, but expected to be high (taurine is small, non-toxic amino acid)

**Food Safety:**
- GRAS status: Essential amino acid; widely consumed (meat, seafood, energy drinks, dietary supplements)
- Safe up to 3 g/day in humans
- Naturally produced by *A. oryzae* during koji fermentation (small amounts)

**Advantages:**
- **Oral bioavailability:** Excellent (amino acid; actively transported)
- **Safety profile:** Decades of clinical use; no toxic interaction profiles at physiological levels
- **Mechanistic clarity:** Well-characterized K+ efflux block upstream of ASC oligomerization
- **Synergy potential:** May enhance uricase efficacy by suppressing IL-1β-driven renal urate reabsorption

**Limitations:**
- **Weak potency vs. benchmark:** Direct inhibitor IC50 not applicable (upstream NLRP3 activator block, not direct enzyme inhibition)
- **No gout clinical evidence:** Only mechanistic extrapolation from sepsis and cardiac models
- **Biosynthetic pathway complexity:** Requires 2–3 heterologous enzymes; lower titers than quercetin or ursolic acid expected

**Ranking Rationale:** Tier 1 candidate for **synergy** with other NLRP3 inhibitors, not as standalone agent. Excellent bioavailability and safety make it ideal for co-production with polyphenols. Evidence strong in sepsis and cardiac contexts but not gout-specific.

---

#### 3a. **Lactoferrin (bovine rbLf / porcine rpLF) — NEW Tier 1 CP5 Entry**

**NLRP3 Mechanism:** (In vitro & animal; CP5 — IL-1β / IL-18 output suppression)
- Glycoprotein (~80 kDa) that suppresses the NLRP3 / caspase-1 / GSDMD axis → reduces IL-1β and IL-18 output
- Multi-tissue anti-inflammatory evidence (renal, intestinal, macrophage)
- Talactoferrin (recombinant human lactoferrin, ChEMBL2108651) reached Phase 3 oncology — establishes oral bioavailability + safety at multi-g/day doses

**Evidence Level:**
- **Animal (murine nephrotoxicity, PMID 37926296):** 300 mg/kg/day lactoferrin suppressed renal NLRP3 / caspase-1 / GSDMD and reduced IL-1β/IL-18. Back-translates to ~3 g/day human — achievable at demonstrated fermentation scale. (Animal Model.)
- **Animal (radiation enteritis):** protective against GI-barrier inflammation; GSDMD-axis mechanism.
- **In vitro:** macrophages + IEC-6 intestinal epithelial cells — NLRP3/caspase-1/GSDMD axis suppression confirmed.
- **Clinical (Phase 3):** Talactoferrin (ChEMBL2108651) — oral bioavailability + safety established at multi-g/day doses.
- **Gout-specific:** Not yet directly tested in MSU model; CP5 mechanism (IL-1β/IL-18 output block) is the gout-relevant target class.

**Production Feasibility:**
- ***Pichia pastoris* (KM71-H, AOX1 promoter):** **3.5 g/L bovine rbLf** (Iglesias-Figueroa 2016, *Int J Mol Sci*, PMID 27294912) — highest demonstrated titer
- **Porcine rpLF:** 2.8 g/L (Yen 2024, PMID 38339093)
- ***A. oryzae* (koji):** Not yet attempted — potential future module for the Open Enzyme koji platform, would fit the GRAS food-organism vision
- **Native source:** Bovine colostrum (commercial lactoferrin capsules available at ~100–300 mg/day)

**Food Safety:**
- GRAS: Bovine lactoferrin (colostrum, milk); decades of dietary use as infant formula additive
- Dose precedent: 100–300 mg/day oral in commercial capsules; up to gram-scale in Phase 3 talactoferrin trials

**Strategic Position:**
- **The only CP5 candidate that is fermentable at scale, food-grade, and has direct NLRP3/IL-1β evidence.**
- Fills the Open Enzyme CP5 gap that canakinumab currently occupies at ~$300K/year.
- Orthogonal mechanism to polyphenol NLRP3 pathway modulators (CP1) and direct NLRP3 binders (CP2).
- *P. pastoris* 3.5 g/L titer exceeds all polyphenol candidates; engineering path is well-characterized.

**Ranking Rationale:** **Tier 1 CP5 entry** based on demonstrated 3.5 g/L fermentation, Phase 3 clinical precedent (talactoferrin), direct NLRP3/caspase-1/GSDMD-axis evidence at CP5, and GRAS food-grade status. Gap: direct MSU-gout validation not yet in the literature — recommend as a priority experimental screen.

---

### Tier 2: Moderate NLRP3 Evidence + Feasible Microbial Production

#### 4. **Resveratrol (3,5,4'-trihydroxystilbene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Stilbenoid polyphenol; non-covalent NLRP3 binding
- Primary mechanisms: mitochondrial integrity preservation, SIRT1-dependent autophagy, reduction of ROS-driven NLRP3 priming
- Does NOT directly bind Cys279 (unlike oridonin); mechanism is functional modulation

**Evidence Level:**
- **In vitro:** Resveratrol (0.1–25 μM) suppresses NLRP3 inflammasome in microglia and macrophages via SIRT1/AMPK pathway
- **Animal (ischemia-reperfusion, arthritis, Toxoplasma infection):** Resveratrol reduced NLRP3 activation and IL-1β in CIA (collagen-induced arthritis) mice, Toxoplasma-infected lungs, cardiac IR injury
- **Gout-specific:** Weak indirect evidence via rheumatoid arthritis models

**Production Feasibility:**
- **S. cerevisiae:** Engineered strains produce resveratrol from glucose
  - **2020 benchmark:** 800 mg/L resveratrol in fed-batch fermentation (highest yeast titer reported for polyphenols)
  - **Pathway:** PAL (phenylalanine ammonia-lyase) + STS (stilbene synthase) from *Vitis vinifera* or *Arachis hypogaea*
  - **Feasibility:** HIGH — mature platform; titers exceed quercetin

**Food Safety:**
- GRAS: Resveratrol in grapes, wine, berries
- Solubility: Poor (requires formulation with lipids or cyclodextrin)
- Safety: Well-tolerated up to 2.5 g/day in humans

**Advantages:**
- **Highest documented polyphenol production titer** (800 mg/L)
- Extensive human safety database (wine polyphenol; dietary supplement for decades)
- Multiple mechanisms (autophagy, SIRT1, mitochondrial homeostasis) suggest broad NLRP3 suppression

**Limitations:**
- IC50 vs. NLRP3 not quantified; estimates in μM range (>>benchmark MCC950)
- No direct covalent binding to NLRP3 Cys279; purely functional modulation
- No gout-specific animal evidence
- Bioavailability severely limited by poor water solubility (~3 mg/L)

**Ranking Rationale:** Tier 2 due to high production titers and safety profile, but weaker NLRP3 specificity vs. quercetin or ursolic acid. Not primary candidate but excellent synergy agent.

---

#### 5. **Carnosine (β-alanyl-histidine)**

**NLRP3 Mechanism:** (In vitro & animal)
- Dipeptide; suppresses NLRP3 inflammasome-driven pyroptosis
- Mechanism: Reduces ROS, suppresses p65 (NF-κB), inhibits JNK phosphorylation; downstream NLRP3, caspase-1, URAT1, GLUT9 suppression
- Anti-inflammatory via SIRT1 and HDAC inhibition

**Evidence Level:**
- **In vitro:** Carnosine (100–500 μM) attenuated LPS-induced NLRP3 activation and pyroptosis in aged rat neurons and HK-2 (kidney) cells
- **Animal (diabetes, aging, LPS-induced inflammation):** Carnosine in STZ-induced diabetic mice reduced renal NLRP3, ASC, pro-IL-1β, mature IL-1β, IL-18; protected against kidney injury
- **Gout-specific:** **YES — direct evidence:** Carnosine reduces serum uric acid in hyperuricemia rats via restoring hepatorenal function and enhancing uric acid excretion while inhibiting inflammation

**Production Feasibility:**
- **S. cerevisiae:** Carnosine synthesis pathway is bacterial (from *Lactobacillus*, *Carnobacterium*)
- **Enzymatic route:** β-alanine + L-histidine → carnosine (via carnosine synthase)
- **Engineering challenge:** β-alanine is not naturally abundant in yeast; requires upstream synthesis from aspartate or serine
- **Status:** NOT extensively published for engineered yeast; feasible but more complex than single-enzyme transglycosidases
- **Estimated titers:** Moderate (~100–500 mg/L) based on analogous dipeptide engineering

**Food Safety:**
- GRAS: Carnosine present in muscle meats, poultry
- Safe: Typical dietary intake ~50–150 mg/day; clinical trials use up to 1–2 g/day
- Non-toxic at high doses

**Advantages:**
- **DIRECT GOUT EVIDENCE:** Only candidate with published hyperuricemia rat data showing reduced serum uric acid AND NLRP3 inhibition
- Excellent oral bioavailability (dipeptide; absorbed intact via peptide transporters)
- Multi-target mechanism (ROS, p-p65, p-JNK, NLRP3, URAT1, GLUT9) suggests combinatorial benefit
- Synergistic with uricase: reduces renal uric acid reabsorption while enzymatic activity degrades luminal urate

**Limitations:**
- **Production complexity:** Requires 2–3 enzymes + upstream β-alanine synthesis; titers likely lower than quercetin or ursolic acid
- Not widely engineered in yeast (publication gap)
- Mechanism: NF-κB-dependent suppression, not direct NLRP3 binding (less potent than oridonin-like compounds)

**Ranking Rationale:** Tier 2; PROMOTED due to direct gout evidence (only candidate with hyperuricemia rat data linking uric acid reduction to NLRP3 inhibition). Production complexity and lower potency prevent Tier 1 ranking.

---

### Tier 3: Polyphenols with Strong NLRP3 Evidence but Variable Production Feasibility

#### 6. **EGCG (Epigallocatechin-3-gallate)**

**NLRP3 Mechanism:** (In vitro & animal; **widest-spectrum natural compound in the stack — 4 of 7 chokepoints**)
- **CP1 (NF-κB priming):** IKK inhibition → blocks NF-κB transcriptional priming of NLRP3 / pro-IL-1β
- **CP1a (TNFSF14 / LIGHT direct suppression):** Hosokawa 2010 (PMID 20461739) — **the only stack compound with direct TNFSF14 data**. Gout-relevant since TNFSF14 is an emerging gout-specific priming amplifier (see [tnfsf14-gout-target.md](./tnfsf14-gout-target.md)).
- **CP4 (caspase-1 suppression):** indirect via 20S proteasome inhibition, **IC50 = 86 nM** (ChEMBL). Sub-100 nM proteasome potency is a **hepatotoxicity dose-ceiling flag** at high-dose intense-use protocols.
- **CP5a (IL-1β receptor-downstream suppression):** reduces IL-1β-induced signaling in target cells (chondrocytes, synoviocytes)
- Green tea catechin; also suppresses ROS-driven NLRP3 activation and K⁺-efflux priming as adjunct mechanisms
- **Summary framing:** EGCG is the widest-spectrum natural compound in the current Open Enzyme stack, hitting four of seven chokepoints (CP1, CP1a, CP4, CP5a). Its 20S proteasome sub-100 nM activity is a hepatotoxicity flag at high dose — safety dose-ceiling for intense use protocols.

**Evidence Level:**
- **In vitro:** EGCG (10–50 μM) attenuated α-hemolysin-induced NLRP3 inflammasome and reduced caspase-1, IL-1β, IL-18; direct binding to Hla (Kd = 1.71 × 10⁻⁴ M)
- **Animal (T2D, bacterial infection models):** EGCG improved glucose tolerance and prevented NLRP3-inflammasome-dependent inflammation in high-fat-diet mice; reduced bacterial lipopolysaccharide-induced NLRP3 activation
- **Gout-specific (re-audit 2026-04-23, PROMOTED):** **Direct MSU mouse gout evidence** — Lee 2019 *Molecules* (PMID 31174271): EGCG blocked MSU-induced caspase-1(p10) and IL-1β in primary mouse macrophages; oral EGCG alleviated MSU-injected mouse foot inflammation via NLRP3 suppression; mechanism = mtDNA synthesis block + ROS reduction. **Hyperuricemic mouse serum-UA lowering** — Yu 2024 *Food Funct* (PMID 38757391). The prior "no gout-specific evidence" framing was keyword-gated and missed these. (Animal Model; source: nlrp3-inhibitor-screen.md 2026-04-23 re-audit)

**Production Feasibility:**
- **S. cerevisiae:** EGCG synthesis requires 8–10 heterologous plant genes (PAL, C4H, 4CL, CHS, CHI, F3H, F3'H, FLS, plus GT for galloylation)
- **Estimated titers:** 10–50 mg/L (lower than kaempferol or quercetin due to galloylation complexity)
- **Feasibility:** MODERATE — pathway complexity is highest among polyphenols; multiple post-translational modifications

**Food Safety:**
- GRAS: Green tea extract (40% EGCG) in dietary supplements
- Safe: Clinical trials use 400–800 mg/day EGCG
- Bioavailability: ~20–30% oral absorption (undergoes gut metabolism)

**Advantages:**
- Multiple ROS reduction mechanisms; strong antioxidant activity
- Established clinical use in dietary supplements
- Synergistic with TLR4/NF-κB suppression (upstream priming block)

**Limitations:**
- Production titers likely 10–50 mg/L (lowest among evaluated polyphenols)
- Pathway complexity (8–10 heterologous genes + galloylation)
- No gout-specific evidence
- Bioavailability limited (~20–30%); undergoes extensive gut metabolism

**Ranking Rationale:** **Promoted to Tier 2** (from Tier 3) following 2026-04-23 literature re-audit: direct MSU mouse gout evidence (Lee 2019 PMID 31174271) and hyperuricemic mouse serum-UA lowering (Yu 2024 PMID 38757391) contradict the prior "no gout-specific evidence" framing. Engineered-production complexity (8–10 gene pathway, 10–50 mg/L titers) remains the limiting factor for a Tier 1 ranking, not evidence. Supplement-tier use (400–800 mg/day green tea extract) is a shorter path than engineered yeast production.

---

#### 7. **Curcumin (1,7-bis(4-hydroxy-3-methoxyphenyl)hpta-1,6-diene-3,5-dione)**

**NLRP3 Mechanism:** (In vitro & animal, gout-specific)
- Curcuminoid phenolic; suppresses K+ efflux and mitochondrial dysfunction
- Blocks ASC oligomerization and speckle formation downstream
- Also inhibits ROS/NEK7-NLRP3 complex assembly
- Suppresses NF-κB signaling (upstream priming)

**Evidence Level:**
- **In vitro:** Curcumin (10–50 μM) blocked MSU-induced NLRP3 inflammasome assembly and IL-1β secretion in macrophages
- **Animal (MSU gout model):** Curcumin (~100 mg/kg) reduced joint swelling, inflammatory cell infiltration, and NLRP3 inflammasome activity in mouse gout arthritis; suppressed NF-κB pathway
- **Gout-specific:** YES — demonstrated efficacy in MSU-induced acute gout arthritis model

**Production Feasibility:**
- **S. cerevisiae:** Curcumin synthesis requires phenylpropanoid pathway + phenolic coupling (PAL, CHS, CPR/CYP for 4-hydroxylation, or acetyl-CoA + phenol oxidative coupling)
- **Feasibility:** MODERATE — pathway known but complex (6–8 heterologous genes); main challenge is oxidative coupling chemistry
- **Estimated titers:** 50–200 mg/L (comparable to EGCG; not extensively published for engineered yeast)

**Food Safety:**
- GRAS: Turmeric (contains 2–8% curcumin)
- Safe: Clinical trials up to 8 g/day; low toxicity
- **Critical limitation:** **Poor bioavailability** (~5% oral absorption; extensive first-pass metabolism)
- Requires lipid formulation (piperine co-supplement, nanoparticles, liposomes) for effective oral dosing

**Advantages:**
- **Direct gout animal evidence:** Demonstrated efficacy in MSU-induced arthritis
- Multiple mechanistic targets (K+ efflux, ASC, ROS, NF-κB, NEK7)
- Well-characterized NLRP3 suppression mechanism
- Therapeutic efficacy in murine gout arthritis model

**Limitations:**
- **Severe bioavailability crisis:** Only ~5% oral absorption; requires sophisticated formulation
- Intensive metabolism by gut microbiota and liver (UDP-glucuronosyltransferase, sulfotransferase)
- Would require co-engineering of bioavailability enhancers (piperine, lipid formulation) if used
- High engineering complexity (~8 genes for phenylpropanoid synthesis + oxidative coupling)

**Ranking Rationale:** Tier 3 due to exceptional gout evidence but crippling bioavailability limitations. Requires co-formulation strategy (e.g., piperine from black pepper fermentation, liposome delivery) to be clinically viable.

---

### Tier 4: Terpenoids with NLRP3 Mechanism but Limited Production Evidence

#### 8. **β-Caryophyllene (4-isopropyl-1-methyl-1-cyclohexene + 2-methyl-6-methylene-2,7-octadiene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Sesquiterpene; CB2 receptor agonist; NLRP3 inhibition via anti-inflammatory and antioxidant pathways
- Decreases NLRP3, caspase-1, and MDA (malondialdehyde) expression
- Reduces neuroinflammation in Parkinson's model

**Evidence Level:**
- **In vitro:** β-caryophyllene suppresses NLRP3 expression and inflammasome assembly in neuroinflammation models
- **Animal (hemiparkinsonism):** β-caryophyllene reduced neuroinflammation and protected dopaminergic neurons via NLRP3 inflammasome inhibition
- **Animal (MSU-induced gouty arthritis in rats):** 100, 200, 400 mg/kg reduced ankle swelling, serum IL-1β/IL-6/TNF-α, and synovial NLRP3/caspase-1/ASC/TLR4/NF-κB expression. Computational docking shows NLRP3 binding (CDOCKER energy 31.92 kcal/mol). Direct gout model evidence — this entry needs re-ranking (see [cannabinoids-terpenes.md](cannabinoids-terpenes.md)). *Front Pharmacol* 2021;12:651305. PMID: 33967792.
- **Gout-specific:** YES (MSU crystal model, animal)

**Production Feasibility:**
- **S. cerevisiae:** β-Caryophyllene is a volatile sesquiterpene; engineered yeast can produce sesquiterpenes via mevalonate + sesquiterpene synthase (STS) heterologous expression
- **Status:** Published for engineered *S. cerevisiae* but titers are low (~10–50 mg/L in flask culture)
- **Challenge:** Volatility; product loss during fermentation; requires advanced bioreactor design (in situ product recovery)

**Food Safety:**
- GRAS: β-Caryophyllene in black pepper, cloves, hops, cannabis
- Safe: Food additive status in multiple jurisdictions
- Volatile; bioavailability as aerosolized/vaporized form > oral

**Advantages:**
- Well-characterized NLRP3 mechanism via CB2
- Natural GRAS food component
- Potential for inhalational delivery (lung inflammation)

**Limitations:**
- **Very low production titers** (~10–50 mg/L) vs. polyphenols (~800 mg/L for resveratrol)
- Volatile; product loss in fermentation
- No gout-specific evidence
- Sesquiterpene synthase expression in yeast is less mature than monoterpene (limonene) or triterpene (ursolic acid) pathways

**Ranking Rationale:** Tier 4 for *microbial production* (low titers, volatility). **Re-ranked to Tier 2–3 for supplement stack** given direct MSU gout animal model data (2021). For supplementation from black pepper/clove extracts, beta-caryophyllene is the only terpene or cannabinoid with published gout-model evidence. See [cannabinoids-terpenes.md](cannabinoids-terpenes.md) for full analysis.

---

#### 9. **Limonene (4-isopropenyl-1-methylcyclohexene, d-limonene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Monoterpene; suppresses NF-κB and NLRP3 inflammasome components via NRF2 induction
- Reduces TLR4 signaling (upstream NLRP3 priming block)
- Antioxidant via NRF2-dependent glutathione synthesis

**Evidence Level:**
- **In vitro:** Linalool (related monoterpene) suppresses TLR4, NF-κB, NLRP3, ASC, caspase-1 expression
- **Animal:** Limonene and linalool reduce inflammation via NRF2 pathway in various models
- **Gout-specific (re-audit 2026-04-23, PROMOTED):** **Direct rat PO+MSU dual model** — Venkatesan 2025 *Nutrients* (PMID 41515190): 50 mg/kg limonene reduced paw thickness, serum UA, IL-1β/TNF/IL-6, improved antioxidant status; authors invoke NLRP3-IL-1β suppression as the mechanistic frame. (Animal Model; source: nlrp3-inhibitor-screen.md 2026-04-23 re-audit)

**Production Feasibility:**
- **S. cerevisiae:** Limonene is a volatile monoterpene; engineered yeast via mevalonate + limonene synthase heterologous expression
- **Status:** Published but titers are very low (~5–20 mg/L); volatility is major issue
- **Bioavailability:** Poor for oral (volatile; absorbed mainly via inhalation/vapor)

**Food Safety:**
- GRAS: Limonene in citrus peels, essential oils
- Safe: Food flavoring; typical intake <10 mg/day from food

**Advantages:**
- NLRP3 mechanism clear (NRF2/TLR4 block)
- Natural GRAS compound

**Limitations:**
- **Extremely low production titers** (<20 mg/L)
- Volatility makes fermentation recovery impractical
- No oral bioavailability (requires vaporization)
- No gout evidence
- Not suitable for oral urate-lowering formulation

**Ranking Rationale:** **Supplement use promoted to Tier 3** (direct rat PO+MSU gout model per Venkatesan 2025 PMID 41515190). **Engineered-production path stays Tier 4** due to volatility (<20 mg/L fermentation titers, poor oral bioavailability without inhalation/vaporization). Two separate tiers for two separate strategies: buy the d-limonene capsule; do not engineer the yeast.

---

#### 10. **Sulforaphane (1-isothiocyanato-4-(methylsulfinyl)butane)** — PROMOTED 2026-04-23

**NLRP3 Mechanism:** (In vitro & animal, hyperuricemia)
- Isothiocyanate; potent Nrf2 activator via Keap1-Cys151 covalent modification
- Sub-μM Nrf2 activation: **EC50 = 580 nM** (*J Med Chem* 2019) — crosses into the potency range of synthetic NLRP3 modulators
- Nrf2 cross-talk with NF-κB: Nrf2 competes with NF-κB for CBP/p300 transcriptional co-activator, suppressing NLRP3 and pro-IL-1β transcription
- PYCARD (ASC) promoter methylation effects inferred from broader Nrf2 epigenetic program

**Evidence Level:**
- **In vitro:** Sub-μM Nrf2 activation (EC50 580 nM, *J Med Chem* 2019)
- **Animal (hyperuricemia, re-audit 2026-04-23, PROMOTED):** Wang 2022 *J Adv Res* (PMID 36371056): hyperuricemic rat model — sulforaphane decreased urate synthesis + increased renal urate excretion + Nrf2-mediated epigenetic modification of urate-handling genes. Dual mechanism (synthesis block + excretion enhancement) bridges the uric-acid and inflammation axes. (Animal Model; source: nlrp3-inhibitor-screen.md 2026-04-23 re-audit)
- **Gout-specific (direct MSU, 2026-05-05 audit, ADDED):** **Yang 2018** *Rheumatology* (Oxford) (PMID 29340626): oral sulforaphane attenuated MSU-crystal-induced foot-pad swelling and neutrophil recruitment in mice; air-pouch gout model confirmed in vivo NLRP3 suppression; in primary mouse macrophages SFN suppressed NLRP3 inflammasome activation by MSU, ATP, and nigericin (but not poly(dA:dT)) independent of ROS, suggesting direct action on the NLRP3 complex. (Animal Model; oral administration; source: 2026-05-05 audit)
- **Mechanistic (Nrf2-independent inflammasome inhibition, 2026-05-05 audit, ADDED):** **Greaney 2015** *J Leukoc Biol* (PMID 26269198): sulforaphane inhibits NLRP1, NLRP3, NAIP5/NLRC4, and AIM2 inflammasomes in macrophages **independent of Nrf2 / antioxidant response element pathway** — distinct from the classical Nrf2 → NF-κB cross-talk mechanism. Confirmed in vivo via acute gout peritonitis model (cell recruitment + IL-1β secretion ↓). Adds a direct caspase-1 / inflammasome-assembly mechanism on top of the Nrf2 → ABCG2 / NF-κB axis. (In Vitro + Animal Model; source: 2026-05-05 audit)

**Production Feasibility:**
- **S. cerevisiae / A. oryzae:** No published engineered microbial production. Requires glucosinolate (glucoraphanin) pathway (6+ heterologous plant genes from *Brassica*) + myrosinase activation
- **Food-industry path:** Freeze-dried broccoli sprouts with active myrosinase (10–20 mg sulforaphane/serving) — shorter than engineered production
- **Engineering complexity:** HIGH (pathway never reconstructed in yeast); Tier 4 for engineered production

**Food Safety:**
- GRAS: Broccoli sprouts, mustard, watercress
- Clinical trials: up to 150 μmol/day oral sulforaphane well-tolerated

**Advantages:**
- **Sub-μM Nrf2 potency** (580 nM EC50) — rare among food-derived compounds
- **Hyperuricemic rat validation** (Wang 2022) bridges urate + inflammation
- Food-industry supply chain already exists (broccoli sprout capsules)
- Mechanistically additive with quercetin (different target class)

**Limitations:**
- No engineered microbial production path
- Gout-specific MSU model not yet tested (hyperuricemia extrapolation only)
- Isothiocyanate reactivity: off-target thiol covalent modification at high doses

**Ranking Rationale:** **Promoted to Tier 2 for supplement use** (Yang 2018 direct MSU foot-pad acute gout + Wang 2022 hyperuricemic rat + Greaney 2015 Nrf2-independent inflammasome mechanism + sub-μM Nrf2 EC50). The 2026-05-05 audit upgraded sulforaphane from Tier 2–3 to Tier 2 — three independent in vivo gout-relevant readouts now exist. **Engineered-production path stays Tier 4** — glucosinolate pathway has never been reconstructed in yeast and the food-industry broccoli-sprout route is shorter.

---

#### 11. **Theaflavins (TF1, TF2A, TF2B, TF3)** — ADDED 2026-05-05

**NLRP3 Mechanism:** (In vitro & animal, MSU peritonitis)
- Theaflavins are the dominant red-orange polyphenols of black tea / oolong / pu'er, formed by polyphenol-oxidase oxidation of EGCG and ECG during fermentation
- Mechanism is **distinct from EGCG**: theaflavins disrupt **NLRP3-NEK7 interaction** downstream of mitochondrial ROS suppression, blocking inflammasome **assembly** (CP2/CP3) rather than EGCG's proteasome-mediated CP1a route
- Suppress ASC speck formation and oligomerization → blocked caspase-1 p10 cleavage, GSDMD-NT pyroptosis, mature IL-1β release
- TF3 (theaflavin-3,3'-digallate) is the most potent fraction across in vitro assays
- **Secondary CP1a coverage:** Hosokawa 2010 (PMID 20461739) — TF3 + EGCG + ECG suppress TNFSF14-induced IL-6 and downregulate HVEM receptor on target cells

**Renal urate handling (unique to theaflavins, not shared with EGCG):**
- ↓ URAT1, ↓ GLUT9 (apical and basolateral reabsorption block)
- ↑ OAT1, ↑ OCTN1, ↑ OAT2, ↑ Oct1/2 (proximal-tubule secretion)
- This is the **only multi-transporter renal urate handling profile** in the wider OE supplement stack besides carnosine (which faces serum carnosinase clearance ceiling)

**Evidence Level:**
- **In vitro (MSU NLRP3 assembly, 2026-05-05 audit, ADDED):** Chen 2023 *Acta Pharmacol Sin* (PMID 37221235): 50–200 μM theaflavin dose-dependently inhibited NLRP3 inflammasome activation in LPS-primed macrophages stimulated with ATP, nigericin, or **MSU crystals**. (In Vitro)
- **Animal (oral, MSU peritonitis):** Same Chen 2023 paper — oral theaflavin significantly attenuated MSU-induced mouse peritonitis (acute-gout-flare proxy model); also rescued bacterial sepsis survival via the same NLRP3-NEK7 mechanism. (Animal Model)
- **Mechanism review:** Chen 2023 *Phytomedicine* (PMID 36990009): comprehensive anti-gout mechanism review covering URAT1/GLUT9 downregulation + OAT1/OCTN1/OAT2 upregulation + network-pharmacology prediction (ABCB1, MAPK14, TERT, STAT1, MMP2/14, BCL2 as anti-gout targets).

**Production Feasibility:**
- **S. cerevisiae / A. oryzae:** No engineered route. Theaflavin biosynthesis requires plant polyphenol oxidase + EGCG and ECG substrates — full pathway has never been reconstructed in yeast or bacteria, and substrate cost would dominate. **Tier 4 for engineered production.**
- **Food-industry path:** Black tea (1–2% theaflavins by dry weight), oolong, pu'er; concentrated supplement extracts standardized to 30–80% TF content. Mature commercial supply chain.

**Food Safety:**
- GRAS: Black tea, all common tea types
- Cardiovascular and lipid trials: 700–2,500 mg/day theaflavin-enriched extract for 12+ weeks well-tolerated
- TF3 standardized extracts in commercial OTC supplements

**Advantages:**
- **Mechanism-orthogonal to EGCG** at the NLRP3 step (assembly disruption vs. proteasome) — additive when stacked
- **Unique URAT1 downregulation** in the OE stack (without carnosine's carnosinase ceiling)
- Direct MSU peritonitis Animal Model (oral)
- Mature commercial supply (theaflavin-enriched extracts)

**Limitations:**
- Poor oral bioavailability (~0.1–1%); same formulation challenge as EGCG
- In vitro effective concentrations (50–200 μM) are 100× higher than achievable plasma exposures from oral dosing — in vivo MSU peritonitis effect may operate via a different mechanism at lower concentrations
- No human gout RCT; dose extrapolated from cardiovascular trials
- No engineered microbial production route

**Ranking Rationale:** **Tier 2 supplement candidate** (direct MSU peritonitis Animal Model + multi-mechanism URAT1/GLUT9/OAT modulation + secondary TNFSF14/HVEM coverage). The mechanism breadth is comparable to EGCG; the unique URAT1 angle pulls in a chokepoint EGCG doesn't reach. **Engineered-production path: Tier 4** — no microbial route. See [theaflavins.md](./theaflavins.md) for the full dossier.

---

### Meta-Finding: Keyword-Gating Failure in Prior Tier-4 Classification

> **Methodological correction (2026-04-23 re-audit):** The original Tier-4 classifications for EGCG, limonene, and sulforaphane were keyword-gated on the literal strings "MSU" / "gout" in PubMed abstracts, which missed direct MSU-gout animal models (EGCG, limonene) and hyperuricemia rat models (sulforaphane) that frame the inflammation via "uric acid" or "hyperuricemia" without using the word "gout."
>
> **New methodological standard (per `scripts/sweep-prompt.md` update):** Pass 2 sweeps should explicitly check:
> 1. MSU-crystal animal models (any species, foot/paw/peritonitis/joint)
> 2. Hyperuricemia animal models (uric-acid lowering in rats/mice)
> 3. Human-cell NLRP3 assays (THP-1, PBMC, MDM) separate from mouse-cell data
> 4. Nrf2 / NF-κB pathway activity at sub-μM potency (not just direct NLRP3)
>
> for every compound, not just those with "gout" in the title. Applied retroactively: EGCG → Tier 2; limonene → Tier 3 supplement / Tier 4 production; sulforaphane → Tier 2–3 supplement / Tier 4 production.
>
> **2026-05-05 follow-up audit (PubMed full-text + bioRxiv):** Sulforaphane upgraded from Tier 2–3 to **Tier 2** with two additional citations (Yang 2018 PMID 29340626 direct MSU foot-pad acute gout; Greaney 2015 PMID 26269198 Nrf2-independent inflammasome inhibition). **Theaflavins added** as a new Tier 2 entry (Chen 2023 PMID 37221235 direct MSU peritonitis Animal Model + Chen 2023 PMID 36990009 multi-transporter URAT1/GLUT9/OAT review). α-Pinene confirmed: no direct MSU/gout animal-model data exists; Tier 4 ranking stands.

---

### Native A. oryzae Metabolites: Screening for Inherent NLRP3 Activity

**Koji (*Aspergillus oryzae*) produces multiple bioactive metabolites:**

1. **Kojic acid** (5-hydroxy-2-(hydroxymethyl)-4-pyrone)
   - Antioxidant; melanin synthesis inhibitor
   - **NLRP3 mechanism:** Unknown; not studied
   - **Food safety:** GRAS; used in cosmetics and food preservation
   - **Status:** Natural A. oryzae product; no engineering needed

2. **Ergothioneine** (2-(2-amino-3-sulfanylpropyl)-4-methyl-1,4-thiazolium)
   - Rare amino acid; potent antioxidant and ROS scavenger
   - **NLRP3 mechanism:** Likely indirect via ROS reduction (not directly tested)
   - **Production:** A. oryzae engineered for 20 mg/g dry weight (~100–500 mg/L fermentation) via EGT1/EGT2 heterologous expression and methionine supplementation
   - **Food safety:** GRAS; present in mushrooms, truffles
   - **Potential:** May synergize with polyphenols for ROS suppression; weak NLRP3 specificity

3. **Ferulic acid** (3-(4-hydroxy-3-methoxyphenyl)prop-2-enoic acid)
   - Phenylpropanoid; antioxidant; precursor for vanillin
   - **NLRP3 mechanism:** Suppresses NLRP3 inflammasome via autophagy induction and blocking caspase-1 activation
   - **Native presence:** Koji produces ferulic acid during mold fermentation; can be further enhanced via ferruloyl esterase overexpression
   - **Food safety:** GRAS
   - **Status:** Likely already present in engineered koji fermentation; synergistic with other polyphenols

4. **Isocoumarin derivatives, gliotoxin, aspergillic acid**
   - Multiple secondary metabolites with antimicrobial and anticancer activities
   - **NLRP3 mechanism:** NOT studied; likely not NLRP3-selective

**Conclusion on native A. oryzae:** Koji naturally produces ergothioneine and ferulic acid; enhancing these via genetic engineering (overexpression of biosynthetic genes) could boost NLRP3 suppression without introducing non-native compounds. However, none of the native A. oryzae metabolites have been directly tested for NLRP3 inhibition.

---

## Ranking: Top 5 Candidates by Evidence × Feasibility × Safety

### **Rank 1: Ursolic Acid (Triterpene)**

| Criterion | Score | Justification |
|-----------|-------|---|
| **NLRP3 evidence** | 8/10 | Animal models (Kawasaki disease, vasculitis); mechanism clear (NF-κB, NLRP3, caspase-1); NOT gout-tested but extrapolates from OA models |
| **Production feasibility** | 10/10 | **8.59 g/L bioreactor titer (2024 record)**; established MVA + triterpene synthase pathway; S. cerevisiae GRAS host |
| **Food safety** | 10/10 | GRAS status; present in apples, rosemary, oregano; safe up to 100–200 mg/day |
| **Bioavailability** | 6/10 | Poor water solubility; requires lipid formulation; stable triterpene resists GI degradation |
| **Gout-specificity** | 5/10 | NO direct gout evidence; inferred from OA models |
| **Overall Score** | **39/50** | **Highest production titer + strong mechanism; extrapolation to gout reasonable** |

**Recommendation:** PRIMARY PRODUCTION CANDIDATE. Co-engineer into S. cerevisiae uricase strain alongside quercetin. Ursolic acid tier can sustain 100–200 mg/dose fermented beverage.

---

### **Rank 2: Quercetin (Flavonoid)**

| Criterion | Score | Justification |
|-----------|-------|---|
| **NLRP3 evidence** | 8/10 | Gout-specific animal model (MSU-induced arthritis); 200–400 mg/kg reduces joint swelling, IL-1β, TNF-α; IC50 ~11 μM; NOT human RCT |
| **Production feasibility** | 9/10 | 20.38 ± 2.57 mg/L in engineered S. cerevisiae; established PAL/CHS/CHI/F3H pathway; proven scalability |
| **Food safety** | 10/10 | GRAS; ubiquitous in plant foods; safe up to 1 g/day |
| **Bioavailability** | 5/10 | Poor (aglycone form); glycosidic formulations improve absorption; low bioavailability limits clinical effect |
| **Gout-specificity** | 9/10 | **Direct gout animal evidence; suppresses IL-1β in MSU models** |
| **Overall Score** | **41/50** | **Best gout evidence + established production; adequate titers** |

**Recommendation:** PRIMARY NLRP3 INHIBITOR CANDIDATE for gout. Synergize with uricase in same S. cerevisiae construct. Quercetin production (20 mg/L) achieves therapeutic dosing in fermented beverage (500 mL @ 20 mg/L = 10 mg quercetin per dose; target ~50 mg/dose via fermenter optimization or co-fermentation).

---

### **Rank 3: Carnosine (Dipeptide)**

| Criterion | Score | Justification |
|-----------|-------|---|
| **NLRP3 evidence** | 9/10 | **Direct hyperuricemia rat evidence:** Carnosine reduces serum uric acid AND inhibits inflammation; suppresses NLRP3, caspase-1, p-p65, p-JNK, URAT1, GLUT9 |
| **Production feasibility** | 6/10 | Requires β-alanine + histidine + carnosine synthase; NOT extensively published for yeast; estimated 100–300 mg/L based on dipeptide analogs |
| **Food safety** | 10/10 | GRAS; meat-derived amino acid; safe up to 2 g/day |
| **Bioavailability** | 10/10 | **Excellent; dipeptide transporters ensure intact absorption** |
| **Gout-specificity** | 10/10 | **Only candidate with direct hyperuricemia + NLRP3 linkage in rats** |
| **Overall Score** | **45/50** | **Highest gout relevance + excellent bioavailability; moderate production complexity** |

**Recommendation:** SECONDARY SYNERGY CANDIDATE. Carnosine's direct hyperuricemia evidence and dual mechanism (NLRP3 + urate excretion via URAT1/GLUT9) make it a strong co-engineer with uricase. Production feasibility moderate; recommend pilot fermentation before scale-up.

---

### **Rank 4: Taurine (Amino Acid)**

| Criterion | Score | Justification |
|-----------|-------|---|
| **NLRP3 evidence** | 8/10 | Strong in sepsis and cardiac models; K+ efflux block upstream of ASC; well-characterized mechanism; NOT gout-tested |
| **Production feasibility** | 7/10 | Requires cysteinyl-CoA synthetase + cysteate sulfinyltransferase; feasible but titers not published; simple small molecule (expected high titers) |
| **Food safety** | 10/10 | GRAS; essential amino acid; safe up to 3 g/day |
| **Bioavailability** | 10/10 | **Excellent; actively transported amino acid** |
| **Gout-specificity** | 4/10 | NO gout evidence; mechanism inference only; may synergize with uricase (reduces renal urate reabsorption via SIRT1?) |
| **Overall Score** | **39/50** | **Excellent safety + bioavailability; weak gout evidence** |

**Recommendation:** TERTIARY SYNERGY AGENT. Include in formulation for broad anti-inflammatory benefit + potential NLRP3 upstream block. Low production cost; pairs well with uricase + quercetin + carnosine.

---

### **Rank 5: Resveratrol (Stilbenoid)**

| Criterion | Score | Justification |
|-----------|-------|---|
| **NLRP3 evidence** | 7/10 | Multiple animal models (arthritis, infection, IR injury); ROS/SIRT1 mechanisms clear; NOT gout-specific |
| **Production feasibility** | 10/10 | **800 mg/L bioreactor titer (2020 record); proven PAL/STS pathway** |
| **Food safety** | 10/10 | GRAS; wine polyphenol; decades of dietary supplement use |
| **Bioavailability** | 4/10 | Poor (~3 mg/L solubility); requires lipid formulation; <5% oral absorption |
| **Gout-specificity** | 3/10 | NO direct gout evidence; inferred from rheumatoid arthritis |
| **Overall Score** | **34/50** | **Highest polyphenol titer; weak gout specificity + bioavailability challenge** |

**Recommendation:** SECONDARY OPTION if ursolic acid production proves limiting. Excellent production titer (800 mg/L); weak gout evidence limits prioritization vs. quercetin or carnosine. Better suited as antioxidant synergy partner in formulation.

---

## Candidates NOT Recommended (Below Threshold)

### Excluded Tier 3–4 Compounds

| Compound | Reason for Exclusion |
|----------|---|
| **EGCG** (engineered-production only) | Production titers 10–50 mg/L, complex 8–10 gene pathway. **Note (2026-04-23):** EGCG itself is **promoted to Tier 2 for supplement use** — direct MSU mouse gout evidence (Lee 2019 PMID 31174271) contradicts the prior "no gout evidence" rationale. Engineered path remains excluded on titer + pathway complexity grounds. |
| **Curcumin** | Severe bioavailability crisis (~5% oral absorption); requires nanoparticle/liposome formulation; high engineering cost for modest benefit |
| **β-Caryophyllene** (engineered-production only) | Very low titers (~10–50 mg/L); volatility issues; oral bioavailability poor. Supplement tier 2–3 given MSU gout rat model (Front Pharmacol 2021, PMID 33967792) — see entry. |
| **Limonene** (engineered-production only) | Extremely low titers (<20 mg/L); volatile; no oral bioavailability without inhalation. **Supplement path promoted to Tier 3** (Venkatesan 2025 PMID 41515190). |
| **Sulforaphane** (engineered-production only) | Isothiocyanate; glucosinolate pathway never reconstructed in yeast. **Supplement path promoted to Tier 2–3** (Wang 2022 hyperuricemic rat PMID 36371056; Nrf2 EC50 580 nM). |
| **Omega-3 metabolites (resolvins, lipoxins, DHA)** | Fatty acid derivatives; no published engineered microbial production; would require lipase + additional enzymatic coupling; complex fermentation; weak NLRP3-specific evidence |

---

## Integrated Production Strategy: "Koji-Yeast Hybrid"

Based on this screen, a **synergistic engineered system** combining S. cerevisiae and A. oryzae is recommended:

### **S. cerevisiae Uricase Strain Augmentation:**
1. **Primary load:** Uricase (Tf-uricase or variant) for uric acid degradation
2. **Secondary load:** Ursolic acid biosynthesis (MVA pathway optimization + CYP/OSC/CPR triterpene synthase genes)
3. **Tertiary load:** Quercetin biosynthesis (PAL/CHS/CHI/F3H genes)

**Expected output:** 50–100 mg/L ursolic acid + 20 mg/L quercetin in fermented beverage; uricase activity intact

### **A. oryzae Koji Enhancement:**
1. **Natural baseline:** Koji already produces ergothioneine (20 mg/g dry weight with optimization) and ferulic acid
2. **Augmentation:** Carnosine synthase heterologous expression from *Lactobacillus*
3. **Benefit:** Enhanced ergothioneine (ROS suppression) + natural ferulic acid (NLRP3 block) + engineered carnosine (hyperuricemia reversal)

**Expected output:** Multi-component koji with synergistic NLRP3 + urate regulation

---

## IC50 Potency Gap: Scaling for Clinical Efficacy

**Critical caveat:** Benchmark NLRP3 inhibitors are 100–10,000× more potent than food-derived candidates:
- **MCC950:** IC50 ~7.5 nM
- **Oridonin:** Covalent Cys279 binder (irreversible inhibition)
- **Quercetin:** IC50 ~11 μM (**1,466× weaker**)
- **Ursolic acid:** IC50 not quantified; structural estimates suggest 5–50 μM range

**Clinical strategy to overcome potency gap:**
1. **Dose escalation:** Fermented beverage @ 50–100 mg/L ursolic acid + 20 mg/L quercetin = ~1–2 g/day intake (deliverable in 500 mL)
2. **Synergy:** Combine polyphenol + triterpene + carnosine + taurine for multi-target NLRP3 suppression
3. **Barrier optimization:** Co-administer with [[blood-barrier-exploits]] strategies (zonula occludens-1 enhancers, tight junction peptides) to maximize intestinal bioavailability
4. **Temporal dosing:** Administer 1–2 hours before uricase dosing to prime NLRP3 suppression; sustain IL-1β reduction for uric acid clearance

---

## Summary Table: Candidates Ranked by Multi-Factor Score

**Two-column IC50 discipline (updated 2026-04-23):** The prior single-column "NLRP3 evidence" conflated two fundamentally different measurements. Cleanly separated below:

- **Direct NLRP3 IC50 (ChEMBL, human-cell)** — curated binding/inhibition against human NLRP3 (CHEMBL1741208) in THP-1 / MDM / PBMC. The rigorous "does this compound inhibit NLRP3" column.
- **Functional IL-1β IC50 (MSU-stimulated)** — IL-1β reduction in macrophage assays, pathway-modulator readouts. The "does this compound suppress the gout-relevant output" column.

The two measure different things and should not be cross-compared. Cell-free / mouse-cell figures are footnoted, not mixed into the human-cell column.

| Rank | Compound | Direct NLRP3 IC50 (human-cell, ChEMBL) | Functional IL-1β IC50 (MSU) | Production (mg/L) | Gout-Specific | Bioavailability | Status |
|------|----------|---|---|---|---|---|---|
| 1 | **Ursolic Acid** | — (no curated entry) | ~μM range (estimated) | 8590 | NO (OA infer) | 6/10 | PRIMARY |
| 2 | **Quercetin** | — (no curated entry; most potent activity is **5-LOX 300 nM**) | ~11 μM (MSU macrophages) | 20 | YES (MSU rat) | 5/10 | PRIMARY |
| 3 | **Carnosine** | — (no curated entry) | μM range (LPS/HUA models) | 150* | YES (HUA rat) | 10/10 | SECONDARY |
| 3a | **Lactoferrin** | — (no direct NLRP3 IC50; CP5 downstream) | ~μg/mL range (NLRP3/caspase-1/GSDMD axis) | 3500 (P. pastoris) | NO (CP5 class) | 8/10 | TIER 1 CP5 |
| 4 | **Taurine** | — (upstream K⁺ efflux, not direct) | μM–mM range | HIGH* | NO | 10/10 | TERTIARY |
| 5 | **Resveratrol** | — (no curated entry) | 0.1–25 μM | 800 | NO | 4/10 | BACKUP |
| — | **EGCG** | — (no curated entry) | 10–50 μM | 30 | YES (MSU mouse, Lee 2019) | 5/10 | SUPPLEMENT T2 |
| — | **Curcumin** | **24.2 μM** (human THP-1, ChEMBL) | 10–50 μM | 100 | YES (MSU) | 1/10 | NOT RECOMMENDED (bioavail) |
| — | **β-Caryophyllene** | — (docking only, no IC50) | μM range | 20 | YES (MSU rat) | 2/10 | SUPPLEMENT T2-3 |
| — | **Sulforaphane** | — (no direct; Nrf2 EC50 **580 nM**) | μM range | — (no yeast path) | YES (HUA rat, Wang 2022) | 6/10 | SUPPLEMENT T2-3 |
| — | **Limonene** | — (no curated entry) | μM range | 20 | YES (MSU rat, Venkatesan 2025) | 2/10 | SUPPLEMENT T3 |
| Benchmark | **Dapansutrile** | **1,000 nM** (human MDM) ¹ | — | synthetic | Phase 2a (PMID 33005902) | oral | PHARMA |
| Benchmark | **Oridonin** | **5,180 nM** (human THP-1) ² | — | extract | YES (MSU mouse, cell-free) | low | SUPPLEMENT |

*Estimated; not published
¹ ChEMBL CHEMBL3989943, *Eur J Med Chem* 2023. Mouse J774A.1 IC50 = 1 nM — **1,000× species gap**, footnoted only.
² ChEMBL CHEMBL1164920, *Eur J Med Chem* 2023. Cell-free covalent-binding kinetics of 0.5–2 μM (Nature Commun 2018) is a different measurement class and should not be cross-compared.

---

## Recommendations for Next Steps

### **Phase 1: Validation (3–4 weeks)**
1. **Keratinocyte co-culture assay:** Test quercetin + ursolic acid synergy on MSU-stimulated IL-1β secretion
2. **Hyperuricemia rat model:** Repeat carnosine + uricase co-dosing (compare to uricase alone)
3. **Bioavailability study:** Oral dosing of quercetin + ursolic acid in mice; measure serum levels at 1, 4, 24 h

### **Phase 2: Engineered Strain Construction (6–8 weeks)**
1. **S. cerevisiae:** Engineer ursolic acid + quercetin biosynthesis in uricase-expressing strain
2. **A. oryzae:** Overexpress carnosine synthase in koji strain; verify ergothioneine + ferulic acid levels
3. **Co-fermentation:** Optimize fed-batch conditions for multi-compound production

### **Phase 3: Gout Efficacy (Pending regulatory guidance)**
1. **MSU-induced acute gout model:** Test engineered yeast fermentation supernatant (quercetin + ursolic acid) vs. vehicle control
2. **Dose-response:** Establish minimal effective dose; compare to quercetin or ursolic acid alone
3. **Mechanism validation:** Measure ex vivo NLRP3 inflammasome activation in patient PBMCs after fermentation dosing

---

## Conclusion

**Ursolic acid** and **quercetin** emerge as the primary candidates for engineered microbial production, offering the best balance of:
- Established biosynthetic feasibility (ursolic acid: **8.59 g/L record titer**)
- NLRP3 inflammasome inhibition mechanism (both animal-model proven)
- Food-safety profile (GRAS status)

**Carnosine** is recommended as a synergy partner due to its **unique direct hyperuricemia evidence** and **excellent bioavailability**, despite production complexity.

**Taurine** and **resveratrol** are suitable secondary agents for multi-target anti-inflammatory benefit, though neither has gout-specific evidence.

Integration into engineered **S. cerevisiae + A. oryzae** dual-organism systems would deliver a food-grade, synergistic NLRP3 inhibitor platform for Phase 2 gout efficacy testing, potentially positioned as a **fermented functional food** rather than pharmaceutical.

---

## Appendix: ChEMBL IC50 Cross-Check (2026-04-23)

This section cross-references the IC50 values cited throughout this screen against the EMBL-EBI ChEMBL v34 curated bioactivity database (queried via the Anthropic life-sciences MCP). Purpose: separate "direct NLRP3 inhibition" claims (measurable in a binding/inhibition assay) from "NLRP3 pathway modulation" claims (inferred from downstream IL-1β readouts, NF-κB suppression, ROS scavenging, or mechanistic review).

**NLRP3 target ID:** CHEMBL1741208 (*NACHT, LRR and PYD domains-containing protein 3*, Homo sapiens, UniProt Q96P20).

### What ChEMBL confirms with direct human NLRP3 bioactivity

| Compound | ChEMBL ID | Human NLRP3 IC50 (direct) | Source (journal/year) |
|---|---|---|---|
| **Dapansutrile (OLT1177)** | CHEMBL3989943 | **1,000 nM (1.0 μM)** — human MDM cells, LPS+nigericin, pChEMBL=6.00 | *Eur J Med Chem* 2023 |
| **Oridonin** | CHEMBL1164920 | **5,180 nM (5.18 μM)** — human THP-1, LPS/ATP, pChEMBL=5.29 | *Eur J Med Chem* 2023 |

That's it. Those are the only two compounds in the inhibitor screen with a curated, cited IC50 against human NLRP3 in ChEMBL.

**Dapansutrile species gap (big surprise):** ChEMBL shows dapansutrile at **1 nM (pChEMBL=9.00)** in *mouse* J774A.1 cells (*Eur J Med Chem* 2020 and *Bioorg Med Chem Lett* 2021) — a 1,000× potency gap versus human cells. The wiki's reference to dapansutrile potency should note this interspecies difference: mouse preclinical assays make it look MCC950-class; human cell data puts it at the μM range. This reframes the 2020 Phase 2a clinical efficacy (52–84% pain reduction at 100–2000 mg/day) as consistent with human-cell μM potency at high oral doses, not sub-nM potency.

**Oridonin: our wiki's "0.5–2 μM" claim is not supported by ChEMBL's curated human NLRP3 assay.** The only ChEMBL entry is 5.18 μM in human THP-1 (2023). The 0.5–2 μM figure likely comes from cell-free or mouse-derived assays in the original Nature Communications 2018 paper (covalent Cys279 binding kinetics); it may not translate to cellular human IC50. Update the wiki framing accordingly.

### What ChEMBL does NOT support with direct human NLRP3 data

Zero bioactivities found against CHEMBL1741208 (human NLRP3) for:

- **Quercetin** (CHEMBL50) — 2,930 total bioactivities across other targets, zero against human NLRP3. The "IC50 ~11 μM" cited here is from functional IL-1β readouts in review literature, not a curated direct NLRP3 inhibition assay. Quercetin's most potent ChEMBL activity is against **5-lipoxygenase (5-LOX): IC50 = 300 nM** (*J Med Chem* 1991) — a leukotriene-pathway target not currently represented in the NLRP3 Exploit Map. Worth adding to the wiki.
- **Ursolic acid** (CHEMBL169) — zero direct human NLRP3 entries
- **Tranilast** (CHEMBL415324) — zero direct human NLRP3 entries (despite the 2017 EMBO Mol Med paper claiming direct NACHT domain binding)
- **Beta-caryophyllene** (CHEMBL445740) — zero direct human NLRP3 entries (the 2021 Front Pharmacol MSU gout paper used docking + downstream markers, not a direct NLRP3 inhibition IC50)

**This is not a contradiction of the inhibitor screen's rankings.** Functional IL-1β suppression in MSU-stimulated macrophages IS clinically relevant — it's what Open Enzyme actually cares about. But it IS a rigor upgrade to how we frame mechanisms: most "NLRP3 inhibitors" in the screen are more accurately **NLRP3 pathway modulators** that act upstream (NF-κB priming block, ROS reduction, K+ efflux prevention) or at unknown direct binding sites that haven't been characterized in the medicinal chemistry literature.

### Implications

1. **Two-tier labeling going forward:** Distinguish "direct NLRP3 inhibitor (binding/inhibition IC50 measured)" from "NLRP3 pathway modulator (functional IL-1β reduction, mechanism inferred)." Only **dapansutrile, oridonin, MCC950, and tranilast** (per separate literature) have standing as direct NLRP3 inhibitors.

2. **Quercetin 5-LOX angle is a missed opportunity.** 5-LOX produces leukotrienes (LTB4) that drive neutrophil chemotaxis in gout flares. Quercetin's IC50 = 300 nM on 5-LOX is stronger than anything else in its pharmacology profile, and LTB4 is a known amplifier of MSU-driven inflammation. Worth adding as a quercetin-specific mechanism in the exploit map — complements the NF-κB story.

3. **Dapansutrile's mouse-vs-human species gap (1000×) matters for translational claims.** Several NLRP3 compounds show strong mouse activity that doesn't translate to human cells. This supports Open Enzyme's emphasis on human-cell (THP-1) validation assays over rodent models for NLRP3 screening.

4. **MCC950 not retrievable by common synonyms (MCC950, CRID3, CP-456773) in ChEMBL's name search.** The IC50 value cited in this screen (7.5 nM) comes from Coll et al. 2015 *J Biol Chem* and is widely cited but not directly verified by the MCP cross-check here. Known target: NACHT domain Walker B motif; benchmark status unchanged, just note the ChEMBL lookup remains open.

### How to refresh

```text
target_search(gene_symbol="NLRP3", organism="Homo sapiens")   # get CHEMBL1741208
compound_search(name="<compound>")                             # get molecule_chembl_id
get_bioactivity(molecule_chembl_id=<ID>, target_chembl_id="CHEMBL1741208", activity_type="IC50")
```

Refresh cadence: annually, or whenever a new direct NLRP3 inhibitor clinical program publishes pivotal data.

---

## Sources

### Polyphenol NLRP3 Inhibition
- [Inflammopharmacology 2025: Natural products targeting NLRP3](https://link.springer.com/article/10.1007/s10787-025-02007-2)
- [PubMed Central: Effectiveness of polyphenols on NLRP3](https://pubmed.ncbi.nlm.nih.gov/41105346/)
- [Journal of Immunology 2020: Oridonin NLRP3 mechanism](https://pubmed.ncbi.nlm.nih.gov/32507349/)
- [Inflammopharmacology 2025: Flavonoids in diabetic neuropathy](https://link.springer.com/article/10.1007/s10787-025-01729-7)
- [2025 Quercetin gout study](https://onlinelibrary.wiley.com/doi/10.1111/cbdd.70103)

### Terpenoid NLRP3 Mechanisms
- [Inflammopharmacology 2022: Phenols and terpenoids in NLRP3](https://link.springer.com/article/10.1007/s10787-021-00918-4)
- [Ursolic acid vasculitis model (2024)](https://www.signavitae.com/articles/10.22514/sv.2024.041)
- [β-Caryophyllene Parkinson's NLRP3 (2024)](https://pubmed.ncbi.nlm.nih.gov/37924806/)

### SCFA Context-Dependent NLRP3
- [Cell Reports 2024: Butyrate/propionate as NLRP3 activators](https://pubmed.ncbi.nlm.nih.gov/39277863/)
- [ScienceDirect 2018: Differential endothelial NLRP3 effects](https://www.sciencedirect.com/science/article/pii/S2213231718300247)

### Amino Acid NLRP3 Inhibitors
- [Nature Medicine 2024: Taurine inflammaging](https://pubmed.ncbi.nlm.nih.gov/40501605/)
- [Cell Death & Disease 2018: Taurine pyroptosis](https://www.nature.com/articles/s41419-018-1004-0)
- [Amino Acids 2024: Carnosine hyperuricemia](https://www.sciencedirect.com/science/article/pii/S1567576623004632)

### Engineered Microbial Production
- [S. cerevisiae polyphenol production review (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7582661/)
- [Ursolic acid S. cerevisiae fed-batch 8.59 g/L (2024)](https://pubmed.ncbi.nlm.nih.gov/39883850/)
- [Resveratrol 800 mg/L S. cerevisiae (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7281501/)
- [A. oryzae engineering (2025)](https://link.springer.com/article/10.1007/s00253-025-13505-2)
- [Ergothioneine A. oryzae production (2024)](https://pubmed.ncbi.nlm.nih.gov/30286703/)

### Dapansutrile Gout Clinical Trial
- [Phase 2a dapansutrile gout trial (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7523621/)

### Koji Postbiotics & Metabolites
- [A. oryzae postbiotic review (Frontiers 2024)](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2024.1452725/full)
- [A. oryzae biotechnological applications (2021)](https://link.springer.com/article/10.1186/s40643-021-00408-z)

### Gout-Specific NLRP3 & Uricase
- [Open Enzyme internal docs: gout-deep-dive.md, nlrp3-exploit-map.md]
- [ALLN-346 oral uricase Phase 2a (Project Milestone)]
- [Rasburicase FDA approval 2001 (S. cerevisiae uricase background)]
- [Georgia State CRISPR S. cerevisiae uricase (2025)](https://doi.org/10.1038/s41598-025-xxxxx)

---

**Document prepared:** 2026-04-21  
**Review status:** Ready for validation phase planning  
**Next owner:** Rheinallt Jones (enzymatic mechanism validation)
