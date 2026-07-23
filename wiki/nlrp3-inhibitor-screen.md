---
title: "NLRP3 Inhibitor Discovery Screen: Food-Derived Gout-Pathway Modulators"
date: 2026-04-21
tags: ["NLRP3", "inflammasome", "inhibitors", "polyphenols", "terpenoids", "gout", "evidence-screen"]
related:
  - gout-deep-dive.md
  - nlrp3-exploit-map.md
  - blood-barrier-exploits.md
  - cross-validation.md
  - nlrp3-inflammasome.md
sources:
  - "Inflammopharmacology 2025: NLRP3 natural products review"
  - "Phytomedicine 2021: celastrol in MSU-induced gouty arthritis (PMID 33130474)"
  - "PubMed Central: Polyphenols and NLRP3"
  - "Cell Reports Medicine, October 2025: PULSE probiotic"
  - "ACS Synthetic Biology: S. cerevisiae engineered production"
  - "Applied Microbiology and Biotechnology 2025: Ergothioneine in A. oryzae"
  - "Scientific Reports 2025: Georgia State CRISPR S. cerevisiae"
---

# NLRP3 Inhibitor Discovery Screen: Food-Derived Gout-Pathway Modulators

## Executive Summary

This screen evaluates food-derived compounds against gout-relevant NLRP3-pathway weaknesses. Candidate priority is determined first by evidence, gout relevance, exposure, safety, and a falsifiable next gate. For a candidate that survives, evaluate existing dietary, extract, purified-compound, and regulated commercial routes before considering engineered production.

> **TCM lineage note (2026-05-05):** Several compounds in this screen have explicit TCM materia medica lineage — oridonin (*Rabdosia rubescens* / Dong Ling Cao 冬凌草), EGCG (green tea / Lu Cha 绿茶), resveratrol (*Polygonum cuspidatum* / Hu Zhang 虎杖), curcumin (turmeric / Jiang Huang 姜黄), berberine (*Coptis chinensis* / Huang Lian 黄连). The methodology for applying modern scientific rigor to these compounds — including chokepoint mapping, ChEMBL cross-check, and bioavailability-honest framing — is formalized in [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md). (source: tcm-modern-rigor-intersection.md)
1. **Evidence strength and assay identity** (clinical > animal > in vitro > mechanistic; direct NLRP3 activity kept separate from downstream IL-1β suppression)
2. **Gout relevance and tissue context** (MSU/hyperuricemia evidence, human-cell species match, and the enterocyte ABCG2 paradox)
3. **Exposure and safety** (bioavailability, dose ceiling, off-target activity, and interaction risk)
4. **Falsifiability** (the cheapest experiment that can distinguish a useful gout-pathway effect from a generic anti-inflammatory signal)
5. **Sourcing and delivery feasibility** (commercial extract, purified compound, engineered production, or another route), evaluated only after the biological case is credible

**Benchmark compounds:**
- **MCC950** — IC50 ~7.5 nM (crystalline NLRP3 inhibitor, not food-derived)
- **Oridonin** — Covalent Cys279 binder (plant diterpenoid, not easily synthesized)
- **Celastrol** — Gout-relevant NLRP3-pathway comparator: suppresses inflammasome-complex assembly through a proposed BRCC3/K63-deubiquitination mechanism in human THP-1 cells, mouse macrophages, and an MSU-induced gouty-arthritis mouse model (In Vitro + Animal Model; PMID 33130474). This is not evidence of clean direct binding to human NLRP3. Celastrol is a broadly cysteine-reactive quinone-methide triterpenoid with multi-target pharmacology plus preclinical cardiac-ion-channel and hematopoietic liabilities (PMIDs 16407206, 22545133); it is **not a food-grade production candidate or intervention recommendation**.
- **Tranilast** — Non-selective mast cell stabilizer
- **OLT1177 (dapansutrile)** — Phase 2a gout trial success, direct NLRP3 ATPase inhibitor

> **Species-gap caveat:** Prefer human-cell potency when available and apply the cross-species standard in [`chembl-cross-check.md`](./etc/chembl-cross-check.md) before translating rodent results.

---

## Candidate Compounds Evaluated

### Candidate dossiers

#### 1. **Quercetin (3,3',4',5,7-pentahydroxyflavone)**

**NLRP3 Mechanism:** (In vitro & animal model)
- Suppresses NLRP3 inflammasome activation and ASC oligomerization
- Inhibits NF-κB and NLRP3 expression via SIRT1 pathway
- Mechanism: mitochondrial protection, upstream IL-1β suppression

**Evidence Level:**
- **In vitro:** Quercetin (IC50 ~11.0 μM) blocks NLRP3 in macrophage lysates
- **Animal (MSU-induced gout):** 200–400 mg/kg quercetin in rats reduced joint edema, IL-1β, TNF-α, COX-2, and PGE2 within 24 h (Clinical trial evidence: NOT published; mechanistic hypothesis only)
- **Human gout:** Quercetin prevents hyperuricemia-associated gouty arthritis via NLRP3/NF-κB inactivation (recent 2025 evidence in literature, but not RCT data)

**Conditional sourcing observations:**
- **Existing sources:** quercetin-rich foods, standardized extracts, and formulated commercial products provide test material without a new production program.
- **Delivery constraint:** the aglycone has poor water solubility and potential intestinal ABCG2 interaction.
- **Engineering fallback:** yeast pathway reconstruction is documented, but it is considered only if existing sources cannot provide the validated exposure.

**Food Safety:**
- GRAS status: Quercetin-rich foods (onions, apples, berries) widely consumed
- Solubility: Low (poor bioavailability as aglycone)
- Dosing in fermented products: 50–100 mg/mL achievable via engineered yeast

**Research strengths:**
- Direct MSU-animal evidence and multiple separable mechanism hypotheses
- Available comparator material without requiring a new production system

**Limitations:**
- IC50 (11 μM) >> benchmark MCC950 (7.5 nM); ~1500× weaker
- No human gout RCT
- Bioavailability severely limited by poor water solubility

**Current gate:** Direct gout-animal evidence makes quercetin a useful comparator, but human-cell target engagement, exposure, and ABCG2 interaction must be resolved before selecting a sourcing route.

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

**Conditional sourcing observations:**
- **Existing sources:** ursolic acid occurs in apples and culinary herbs and is available as purified research material and commercial extracts.
- **Delivery constraint:** poor water solubility requires an exposure-validating formulation.
- **Engineering fallback:** high-titer yeast production has been reported, but a new host is unnecessary unless the biological case passes and existing sources cannot supply the required validated material.

**Food Safety:**
- GRAS status: Ursolic acid present in apples, rosemary, oregano, thyme
- Traditional use: Chinese medicine (*Radix Salviae Divinorum*)
- Solubility: Poor in water; typically requires lipid formulation
- Dosing: 100–200 mg/day in human trials

**Research strengths:**
- Direct NF-κB biochemistry and multiple separable inflammatory targets
- Existing purified material supports an MSU-relevant screen without production development

**ChEMBL v37 mechanism upgrade (2026-07-01):** Ursolic acid (CHEMBL169) now has **16 curated entries at pChEMBL ≥6** (zero in v34). Top curated biochemical targets (**verified directly against ChEMBL 2026-07-13**): **NF-κB p65 IC50 = 31 nM** (*Bioorg Med Chem* 2018, direct p65–DNA-binding ELISA) and **SENP1 IC50 = 6.4 nM** (*Eur J Med Chem* 2022) — both solid; the NF-κB p65 hit legitimately elevates the NF-κB claim from functional/animal to **In Vitro direct biochemistry** (the load-bearing gout-relevant upgrade). **ROR-γ — corrected to a range, not the headline:** ursolic acid's ROR-γ inverse-agonist IC50 spans **~0.75–680 nM across 5+ curated assays** (human 130–680 nM; mouse 500–1,000 nM; the 0.75 nM in *J Med Chem* 2023 is the single most-potent record, *not* representative — reporting it alone overstates potency up to ~900×). The ROR-γ/Th17 angle was a candidate chronic-tophus (adaptive-immune) mechanism, but a 2026-07-13 scoping scan found **Th17/IL-17 is a bystander, not a driver** of tophus biology — so this is a **curiosity, not a priority** (see [`open-questions.md` §"Chronic tophaceous gout — the adaptive-immune axis"](./open-questions.md)). See [chembl-cross-check.md](./etc/chembl-cross-check.md) for full details. (In Vitro; source: chembl-cross-check.md)

**Limitations:**
- IC50 not quantified vs. MCC950 or oridonin (appears to be in μM range from structure activity)
- No gout-specific animal evidence (extrapolation from OA models)
- Requires two additional metabolic engineering modules (MVA optimization + triterpene synthase pathway)

**Current gate:** No direct gout study is available. Production titer and food occurrence do not substitute for an MSU-relevant, exposure-matched assay.

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

**Conditional sourcing observations:**
- **S. cerevisiae or *A. oryzae*:** Taurine synthesis pathway is natural to mammals; bacteria also produce it
- **Heterologous pathway:** Cysteine → cysteic acid → taurine (requires cysteinyl-CoA synthetase, cysteate sulfinyltransferase)
- **Engineering status:** Feasible; taurine biosynthesis genes from *E. coli* or *Corynebacterium* have been cloned
- **Titers:** Not extensively published for engineered yeast, but expected to be high (taurine is small, non-toxic amino acid)

**Food Safety:**
- GRAS status: Essential amino acid; widely consumed (meat, seafood, energy drinks, dietary supplements)
- Safe up to 3 g/day in humans
- Naturally produced by *A. oryzae* during koji fermentation (small amounts)

**Research strengths:**
- **Oral bioavailability:** Excellent (amino acid; actively transported)
- **Safety profile:** Decades of clinical use; no toxic interaction profiles at physiological levels
- **Mechanistic clarity:** Well-characterized K+ efflux block upstream of ASC oligomerization
- **Synergy potential:** May enhance uricase efficacy by suppressing IL-1β-driven renal urate reabsorption

**Limitations:**
- **Weak potency vs. benchmark:** Direct inhibitor IC50 not applicable (upstream NLRP3 activator block, not direct enzyme inhibition)
- **No gout clinical evidence:** Only mechanistic extrapolation from sepsis and cardiac models
- **Biosynthetic pathway complexity:** Requires 2–3 heterologous enzymes; lower titers than quercetin or ursolic acid expected

**Current gate:** Evidence comes from sepsis and cardiac contexts rather than gout. Test potassium-efflux and inflammasome readouts under MSU challenge before evaluating combinations or sourcing.

---

#### 3a. **Lactoferrin (bovine rbLf / porcine rpLF)**

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

**Conditional sourcing observations:**
- ***Pichia pastoris* (KM71-H, AOX1 promoter):** **3.5 g/L bovine rbLf** (Iglesias-Figueroa 2016, *Int J Mol Sci*, PMID 27294912) — highest demonstrated titer
- **Porcine rpLF:** 2.8 g/L (Yen 2024, PMID 38339093)
- ***A. oryzae* (koji):** Not yet attempted—potential future module within the koji track, conditional on its own feasibility and exposure gates
- **Native source:** Bovine colostrum (commercial lactoferrin capsules available at ~100–300 mg/day)

**Food Safety:**
- GRAS: Bovine lactoferrin (colostrum, milk); decades of dietary use as infant formula additive
- Dose precedent: 100–300 mg/day oral in commercial capsules; up to gram-scale in Phase 3 talactoferrin trials

**Strategic Position:**
- **The only CP5 candidate that is fermentable at scale, food-grade, and has direct NLRP3/IL-1β evidence.**
- Fills the Open Enzyme CP5 gap that canakinumab currently occupies at ~$300K/year.
- Orthogonal mechanism to polyphenol NLRP3 pathway modulators (CP1) and direct NLRP3 binders (CP2).
- *P. pastoris* 3.5 g/L titer exceeds all polyphenol candidates; engineering path is well-characterized.

**Current gate:** The CP5/pyroptosis evidence is from an adjacent model, not MSU gout. Test GI stability, relevant exposure, and CP5 target engagement in an MSU assay before choosing a production route.

---

### Additional candidate dossiers

#### 4. **Resveratrol (3,5,4'-trihydroxystilbene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Stilbenoid polyphenol; non-covalent NLRP3 binding
- Primary mechanisms: mitochondrial integrity preservation, SIRT1-dependent autophagy, reduction of ROS-driven NLRP3 priming
- Does NOT directly bind Cys279 (unlike oridonin); mechanism is functional modulation

**Evidence Level:**
- **In vitro:** Resveratrol (0.1–25 μM) suppresses NLRP3 inflammasome in microglia and macrophages via SIRT1/AMPK pathway
- **Animal (ischemia-reperfusion, arthritis, Toxoplasma infection):** Resveratrol reduced NLRP3 activation and IL-1β in CIA (collagen-induced arthritis) mice, Toxoplasma-infected lungs, cardiac IR injury
- **Gout-specific:** Weak indirect evidence via rheumatoid arthritis models

**Conditional sourcing observations:**
- **S. cerevisiae:** Engineered strains produce resveratrol from glucose
  - **2020 benchmark:** 800 mg/L resveratrol in fed-batch fermentation (highest yeast titer reported for polyphenols)
  - **Pathway:** PAL (phenylalanine ammonia-lyase) + STS (stilbene synthase) from *Vitis vinifera* or *Arachis hypogaea*
  - **Feasibility:** HIGH — mature platform; titers exceed quercetin

**Food Safety:**
- GRAS: Resveratrol in grapes, wine, berries
- Solubility: Poor (requires formulation with lipids or cyclodextrin)
- Safety: Well-tolerated up to 2.5 g/day in humans

**Research strengths:**
- **Highest documented polyphenol production titer** (800 mg/L)
- Extensive human safety database (wine polyphenol; dietary supplement for decades)
- Multiple mechanisms (autophagy, SIRT1, mitochondrial homeostasis) suggest broad NLRP3 suppression

**ChEMBL v37 (2026-07-01):** Resveratrol's strongest curated molecular-target activity remains **DPP-4 IC50 = 0.6 nM** (pChEMBL 9.22, *Eur J Med Chem* 2018). Cell-line antiproliferative IC50s from *J Med Chem* 2011 rank above it by pChEMBL (HeLa 0.023 nM, etc.) but target cell lines, not molecular proteins. The sub-nM DPP-4 finding places resveratrol mechanistically adjacent to the gliptin class at physiologically achievable concentrations — relevant to the gout-T2D comorbidity cluster. See [chembl-cross-check.md](./etc/chembl-cross-check.md) for full profile. (In Vitro; source: chembl-cross-check.md)

**Limitations:**
- IC50 vs. NLRP3 not quantified; estimates in μM range (>>benchmark MCC950)
- No direct covalent binding to NLRP3 Cys279; purely functional modulation
- No gout-specific animal evidence
- Bioavailability severely limited by poor water solubility (~3 mg/L)

**Current gate:** Weak gout specificity and limited exposure outweigh sourcing convenience. Retain as a mechanistic comparator until an MSU-relevant assay establishes a signal.

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

**Conditional sourcing observations:**
- **S. cerevisiae:** Carnosine synthesis pathway is bacterial (from *Lactobacillus*, *Carnobacterium*)
- **Enzymatic route:** β-alanine + L-histidine → carnosine (via carnosine synthase)
- **Engineering challenge:** β-alanine is not naturally abundant in yeast; requires upstream synthesis from aspartate or serine
- **Status:** NOT extensively published for engineered yeast; feasible but more complex than single-enzyme transglycosidases
- **Estimated titers:** Moderate (~100–500 mg/L) based on analogous dipeptide engineering

**Food Safety:**
- GRAS: Carnosine present in muscle meats, poultry
- Safe: Typical dietary intake ~50–150 mg/day; clinical trials use up to 1–2 g/day
- Non-toxic at high doses

**Research strengths:**
- **DIRECT GOUT EVIDENCE:** Only candidate with published hyperuricemia rat data showing reduced serum uric acid AND NLRP3 inhibition
- Excellent oral bioavailability (dipeptide; absorbed intact via peptide transporters)
- Multi-target mechanism (ROS, p-p65, p-JNK, NLRP3, URAT1, GLUT9) suggests combinatorial benefit
- Synergistic with uricase: reduces renal uric acid reabsorption while enzymatic activity degrades luminal urate

**Limitations:**
- **Production complexity:** Requires 2–3 enzymes + upstream β-alanine synthesis; titers likely lower than quercetin or ursolic acid
- Not widely engineered in yeast (publication gap)
- Mechanism: NF-κB-dependent suppression, not direct NLRP3 binding (less potent than oridonin-like compounds)

**Current gate:** The dual urate/NLRP3 signal is animal-model evidence. Establish human-relevant exposure and separate transporter from inflammasome effects before evaluating sourcing.

---

### Polyphenol dossiers

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
- **Gout-specific:** Lee 2019 *Molecules* (PMID 31174271) reported that EGCG blocked MSU-induced caspase-1(p10) and IL-1β in primary mouse macrophages and reduced MSU-injected mouse foot inflammation; Yu 2024 *Food Funct* (PMID 38757391) reported serum-urate lowering in hyperuricemic mice. (Animal Model.)

**Conditional sourcing observations:**
- **S. cerevisiae:** EGCG synthesis requires 8–10 heterologous plant genes (PAL, C4H, 4CL, CHS, CHI, F3H, F3'H, FLS, plus GT for galloylation)
- **Estimated titers:** 10–50 mg/L (lower than kaempferol or quercetin due to galloylation complexity)
- **Feasibility:** MODERATE — pathway complexity is highest among polyphenols; multiple post-translational modifications

**Food Safety:**
- GRAS: Green tea extract (40% EGCG) in dietary supplements
- Safe: Clinical trials use 400–800 mg/day EGCG
- Bioavailability: ~20–30% oral absorption (undergoes gut metabolism)

**Research strengths:**
- Multiple ROS reduction mechanisms; strong antioxidant activity
- Established clinical use in dietary supplements
- Synergistic with TLR4/NF-κB suppression (upstream priming block)

**Limitations:**
- Production titers likely 10–50 mg/L (lowest among evaluated polyphenols)
- Pathway complexity (8–10 heterologous genes + galloylation)
- No human gout evidence; gout-specific evidence is limited to the mouse and primary-macrophage studies above
- Bioavailability limited (~20–30%); undergoes extensive gut metabolism

**Current gate:** Direct mouse evidence supports MSU-relevant inflammatory and hyperuricemia signals. A separate MCF-7Tam study found reduced mitoxantrone-assayed BCRP activity after EGCG exposure without changed BCRP mRNA or protein; it does not establish an acute-versus-chronic switch or intestinal urate direction. Resolve stability, free exposure, ABCG2 attribution, and urate flux before selecting a source.

---

#### 7. **Curcumin (1,7-bis(4-hydroxy-3-methoxyphenyl)hpta-1,6-diene-3,5-dione)**

**NLRP3 Mechanism:** (In vitro & animal, gout-specific)
- Curcuminoid phenolic; suppresses K+ efflux and mitochondrial dysfunction
- Blocks ASC oligomerization and speckle formation downstream
- Also inhibits ROS/NEK7-NLRP3 complex assembly
- Suppresses NF-κB signaling (upstream priming)

**Evidence Level:**
- **In vitro:** Curcumin (10–50 μM) blocked MSU-induced NLRP3 inflammasome assembly and IL-1β secretion in macrophages
- **Direct human NLRP3:** Curated human NLRP3 IC50 = **24.2 μM** (THP-1, *J Nat Prod* 2020, pChEMBL 4.62, ChEMBL v34/v37) — third compound in the stack with ChEMBL-curated direct human NLRP3 data, after dapansutrile (1.0 μM) and oridonin (5.18 μM). 24× weaker than dapansutrile, 5× weaker than oridonin in the same human cellular format. (In Vitro; source: chembl-cross-check.md)
- **Animal (MSU gout model):** Curcumin (~100 mg/kg) reduced joint swelling, inflammatory cell infiltration, and NLRP3 inflammasome activity in mouse gout arthritis; suppressed NF-κB pathway
- **Gout-specific:** YES — demonstrated efficacy in MSU-induced acute gout arthritis model

**Conditional sourcing observations:**
- **S. cerevisiae:** Curcumin synthesis requires phenylpropanoid pathway + phenolic coupling (PAL, CHS, CPR/CYP for 4-hydroxylation, or acetyl-CoA + phenol oxidative coupling)
- **Feasibility:** MODERATE — pathway known but complex (6–8 heterologous genes); main challenge is oxidative coupling chemistry
- **Estimated titers:** 50–200 mg/L (comparable to EGCG; not extensively published for engineered yeast)

**Food Safety:**
- GRAS: Turmeric (contains 2–8% curcumin)
- Safe: Clinical trials up to 8 g/day; low toxicity
- **Critical limitation:** **Poor bioavailability** (~5% oral absorption; extensive first-pass metabolism)
- Requires lipid formulation (piperine co-supplement, nanoparticles, liposomes) for effective oral dosing

**ChEMBL v37 update (2026-07-01; replication verified 2026-07-13):** Curcumin (CHEMBL140) now has a curated **DYRK2 IC50 = 2.5 nM** (pChEMBL 8.60, *J Med Chem* 2023) — rank-2 molecular target after amyloid-β (rank 1). **This is a reproducible hit, not single-paper:** DYRK2 inhibition is curated across three independent assays at IC50 = 2.5, 5, and 10 nM (*J Med Chem* 2023 ×2 + *ACS Med Chem Lett* 2024), verified directly against the ChEMBL bioactivity records on 2026-07-13. DYRK2 regulates proteasome activity via PA28γ phosphorylation, providing a biochemical link between curcumin and the proteasome-regulation mechanism (adjacent to EGCG's 20S proteasome inhibition, IC50 86 nM). Two stack compounds (curcumin + EGCG) now touch proteasome biology through complementary mechanisms. Gout-specific relevance is indirect; DYRK2 was not present in ChEMBL v34. See [chembl-cross-check.md](./etc/chembl-cross-check.md) for full details. (In Vitro; source: chembl-cross-check.md)

**Research strengths:**
- **Direct gout animal evidence:** Demonstrated efficacy in MSU-induced arthritis
- Multiple mechanistic targets (K+ efflux, ASC, ROS, NF-κB, NEK7)
- Well-characterized NLRP3 suppression mechanism
- Therapeutic efficacy in murine gout arthritis model

**Limitations:**
- **Severe bioavailability crisis:** Only ~5% oral absorption; requires sophisticated formulation
- Intensive metabolism by gut microbiota and liver (UDP-glucuronosyltransferase, sulfotransferase)
- Would require co-engineering of bioavailability enhancers (piperine, lipid formulation) if used
- High engineering complexity (~8 genes for phenylpropanoid synthesis + oxidative coupling)

**Current gate:** Gout-relevant evidence is offset by severe bioavailability and intestinal ABCG2-interaction concerns. Establish free concentration and transporter effects before any formulation work.

---

### Terpenoid and other accessible-compound dossiers

#### 8. **β-Caryophyllene (4-isopropyl-1-methyl-1-cyclohexene + 2-methyl-6-methylene-2,7-octadiene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Sesquiterpene; CB2 receptor agonist; NLRP3 inhibition via anti-inflammatory and antioxidant pathways
- Decreases NLRP3, caspase-1, and MDA (malondialdehyde) expression
- Reduces neuroinflammation in Parkinson's model

**Evidence Level:**
- **In vitro:** β-caryophyllene suppresses NLRP3 expression and inflammasome assembly in neuroinflammation models
- **Animal (hemiparkinsonism):** β-caryophyllene reduced neuroinflammation and protected dopaminergic neurons via NLRP3 inflammasome inhibition
- **Animal (MSU-induced gouty arthritis in rats):** 100, 200, 400 mg/kg reduced ankle swelling, serum IL-1β/IL-6/TNF-α, and synovial NLRP3/caspase-1/ASC/TLR4/NF-κB expression. Computational docking shows NLRP3 binding (CDOCKER energy 31.92 kcal/mol). Direct gout model evidence — this entry needs re-ranking (see [cannabinoids-terpenes.md](cannabinoids-terpenes.md)). *Front Pharmacol* 2021;12:651305. PMID: 33967792.
- **ChEMBL v37 update (2026-07-01):** CB2 agonism is now **ChEMBL-curated**: CB2 Ki = **150 nM** (pChEMBL 6.82, *Eur J Med Chem* 2018). At v34 baseline this was external-literature-only; v37 confirms the CB2 mechanism with a curated binding assay. No human NLRP3 entries (CHEMBL1741208) exist — the "direct NLRP3 binding" claim from the 2021 docking paper remains uncurated. (In Vitro; source: chembl-cross-check.md)
- **Gout-specific:** YES (MSU crystal model, animal)

**Conditional sourcing observations:**
- **S. cerevisiae:** β-Caryophyllene is a volatile sesquiterpene; engineered yeast can produce sesquiterpenes via mevalonate + sesquiterpene synthase (STS) heterologous expression
- **Status:** Published for engineered *S. cerevisiae* but titers are low (~10–50 mg/L in flask culture)
- **Challenge:** Volatility; product loss during fermentation; requires advanced bioreactor design (in situ product recovery)

**Food Safety:**
- GRAS: β-Caryophyllene in black pepper, cloves, hops, cannabis
- Safe: Food additive status in multiple jurisdictions
- Volatile; bioavailability as aerosolized/vaporized form > oral

**Research strengths:**
- Well-characterized NLRP3 mechanism via CB2
- Natural GRAS food component
- Potential for inhalational delivery (lung inflammation)

**Limitations:**
- **Very low production titers** (~10–50 mg/L) vs. polyphenols (~800 mg/L for resveratrol)
- Volatile; product loss in fermentation
- No gout-specific evidence
- Sesquiterpene synthase expression in yeast is less mature than monoterpene (limonene) or triterpene (ursolic acid) pathways

**Current gate:** Direct MSU-animal evidence warrants a CB2-dependent, exposure-matched human-cell assay. Volatility and bioavailability are delivery constraints, not biological rank. See [cannabinoids-terpenes.md](cannabinoids-terpenes.md).

---

#### 9. **Limonene (4-isopropenyl-1-methylcyclohexene, d-limonene)**

**NLRP3 Mechanism:** (In vitro & animal)
- Monoterpene; suppresses NF-κB and NLRP3 inflammasome components via NRF2 induction
- Reduces TLR4 signaling (upstream NLRP3 priming block)
- Antioxidant via NRF2-dependent glutathione synthesis

**Evidence Level:**
- **In vitro:** Linalool (related monoterpene) suppresses TLR4, NF-κB, NLRP3, ASC, caspase-1 expression
- **Animal:** Limonene and linalool reduce inflammation via NRF2 pathway in various models
- **Gout-specific:** Venkatesan 2025 *Nutrients* (PMID 41515190) reported reduced paw thickness, serum UA, IL-1β/TNF/IL-6, and improved antioxidant status in a rat PO+MSU model; the authors invoke NLRP3–IL-1β suppression. (Animal Model.)

**Conditional sourcing observations:**
- **S. cerevisiae:** Limonene is a volatile monoterpene; engineered yeast via mevalonate + limonene synthase heterologous expression
- **Status:** Published but titers are very low (~5–20 mg/L); volatility is major issue
- **Bioavailability:** Poor for oral (volatile; absorbed mainly via inhalation/vapor)

**Food Safety:**
- GRAS: Limonene in citrus peels, essential oils
- Safe: Food flavoring; typical intake <10 mg/day from food

**Research strengths:**
- NLRP3 mechanism clear (NRF2/TLR4 block)
- Natural GRAS compound

**Limitations:**
- **Extremely low production titers** (<20 mg/L)
- Volatility makes fermentation recovery impractical
- No oral bioavailability (requires vaporization)
- No gout evidence
- Not suitable for oral urate-lowering formulation

**Current gate:** The rat PO+MSU result supports follow-up, but volatility and poor oral exposure require a concentration-matched human-cell assay before any delivery decision.

---

#### 10. **Sulforaphane (1-isothiocyanato-4-(methylsulfinyl)butane)**

**NLRP3 Mechanism:** (In vitro & animal, hyperuricemia)
- Isothiocyanate; potent Nrf2 activator via Keap1-Cys151 covalent modification
- Sub-μM Nrf2 activation: **EC50 = 580 nM** (*J Med Chem* 2019) — crosses into the potency range of synthetic NLRP3 modulators
- Nrf2 cross-talk with NF-κB: Nrf2 competes with NF-κB for CBP/p300 transcriptional co-activator, suppressing NLRP3 and pro-IL-1β transcription
- PYCARD (ASC) promoter methylation effects inferred from broader Nrf2 epigenetic program

**Evidence Level:**
- **In vitro:** Sub-μM Nrf2 activation (EC50 580 nM, *J Med Chem* 2019)
- **Animal (hyperuricemia):** Wang 2022 *J Adv Res* (PMID 36371056) reported decreased urate synthesis, increased renal urate excretion, and Nrf2-mediated modification of urate-handling genes in a hyperuricemic rat model. (Animal Model.)
- **Gout-specific (direct MSU, 2026-05-05 audit, ADDED):** **Yang 2018** *Rheumatology* (Oxford) (PMID 29340626): oral sulforaphane attenuated MSU-crystal-induced foot-pad swelling and neutrophil recruitment in mice; air-pouch gout model confirmed in vivo NLRP3 suppression; in primary mouse macrophages SFN suppressed NLRP3 inflammasome activation by MSU, ATP, and nigericin (but not poly(dA:dT)) independent of ROS, suggesting direct action on the NLRP3 complex. (Animal Model; oral administration; source: 2026-05-05 audit)
- **Mechanistic (Nrf2-independent inflammasome inhibition, 2026-05-05 audit, ADDED):** **Greaney 2015** *J Leukoc Biol* (PMID 26269198): sulforaphane inhibits NLRP1, NLRP3, NAIP5/NLRC4, and AIM2 inflammasomes in macrophages **independent of Nrf2 / antioxidant response element pathway** — distinct from the classical Nrf2 → NF-κB cross-talk mechanism. Confirmed in vivo via acute gout peritonitis model (cell recruitment + IL-1β secretion ↓). Adds a direct caspase-1 / inflammasome-assembly mechanism on top of the Nrf2 → ABCG2 / NF-κB axis. (In Vitro + Animal Model; source: 2026-05-05 audit)

**Conditional sourcing observations:**
- **S. cerevisiae / A. oryzae:** No published engineered microbial production. Requires glucosinolate (glucoraphanin) pathway (6+ heterologous plant genes from *Brassica*) + myrosinase activation
- **Food-industry path:** Freeze-dried broccoli sprouts with active myrosinase (10–20 mg sulforaphane/serving) — shorter than engineered production
- **Engineering complexity:** HIGH; the pathway has not been reconstructed in yeast. This is a downstream sourcing constraint.

**Food Safety:**
- GRAS: Broccoli sprouts, mustard, watercress
- Clinical trials: up to 150 μmol/day oral sulforaphane well-tolerated

**Research strengths:**
- **Sub-μM Nrf2 potency** (580 nM EC50) — rare among food-derived compounds
- **Hyperuricemic rat validation** (Wang 2022) bridges urate + inflammation
- Food-industry supply chain already exists (broccoli sprout capsules)
- Mechanistically additive with quercetin (different target class)

**Limitations:**
- No engineered microbial production path
- Gout-specific MSU model not yet tested (hyperuricemia extrapolation only)
- Isothiocyanate reactivity: off-target thiol covalent modification at high doses

**Current gate:** Multiple in-vivo gout-relevant readouts support direct validation, but conversion, tissue exposure, Nrf2 dependence, and ABCG2 function must be measured before choosing a dietary or engineered source.

---

#### 11. **Theaflavins (TF1, TF2A, TF2B, TF3)**

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
- **S. cerevisiae / A. oryzae:** No engineered route. Theaflavin biosynthesis requires plant polyphenol oxidase plus EGCG and ECG substrates; the full pathway has not been reconstructed in yeast or bacteria. This matters only if the biological and exposure gates pass.
- **Food-industry path:** Black tea (1–2% theaflavins by dry weight), oolong, pu'er; concentrated supplement extracts standardized to 30–80% TF content. Mature commercial supply chain.

**Food Safety:**
- GRAS: Black tea, all common tea types
- Cardiovascular and lipid trials: 700–2,500 mg/day theaflavin-enriched extract for 12+ weeks well-tolerated
- TF3 standardized extracts in commercial OTC supplements

**Research strengths:**
- **Mechanism-orthogonal to EGCG** at the NLRP3 step (assembly disruption vs. proteasome) — additive when stacked
- **Unique URAT1 downregulation** in the OE stack (without carnosine's carnosinase ceiling)
- Direct MSU peritonitis Animal Model (oral)
- Mature commercial supply (theaflavin-enriched extracts)

**Limitations:**
- Poor oral bioavailability (~0.1–1%); same formulation challenge as EGCG
- In vitro effective concentrations (50–200 μM) are 100× higher than achievable plasma exposures from oral dosing — in vivo MSU peritonitis effect may operate via a different mechanism at lower concentrations
- No human gout RCT; dose extrapolated from cardiovascular trials
- No engineered microbial production route

**Current gate:** Direct MSU-animal evidence and transporter observations justify target-specific follow-up. Separate TNFSF14, inflammasome, and urate-transporter effects before selecting a source. See [theaflavins.md](./theaflavins.md).

---

### Search-scope correction: mechanism-only queries miss gout evidence

Searches limited to the literal strings "MSU" or "gout" miss direct MSU-gout animal models and hyperuricemia models framed under "uric acid" or "hyperuricemia." Candidate searches therefore need to include:

> 1. MSU-crystal animal models (any species, foot/paw/peritonitis/joint)
> 2. Human-cell NLRP3 assays (THP-1, PBMC, MDM) separate from mouse-cell data
> 3. Nrf2 / NF-κB pathway activity at sub-μM potency (not just direct NLRP3)

This search scope supports higher evidence priority for EGCG, limonene, sulforaphane, and theaflavins without implying that any production route or human dose is established. α-Pinene still lacks direct MSU/gout animal-model evidence.

---

## IC50 potency gap: exposure and assay gates

**Critical caveat:** Benchmark NLRP3 inhibitors are 100–10,000× more potent than food-derived candidates:
- **MCC950:** IC50 ~7.5 nM
- **Oridonin:** Covalent Cys279 binder (irreversible inhibition)
- **Quercetin:** IC50 ~11 μM (**1,466× weaker**)
- **Ursolic acid:** IC50 not quantified; structural estimates suggest 5–50 μM range

The potency gap is not a prompt for dose escalation or multi-compound stacking. It is an experimental gate: measure free concentration at the relevant tissue, test each candidate alone before combinations, and reject candidates whose required exposure collides with bioavailability or safety limits.

---

## Summary table: current evidence and next gate

Rows are grouped as research candidates and clinical/research comparators. There is no production-weighted rank.

**Two-column IC50 discipline:** Direct NLRP3 activity and functional MSU-stimulated IL-1β suppression are distinct measurements:

- **Direct NLRP3 IC50 (ChEMBL, human-cell)** — curated binding/inhibition against human NLRP3 (CHEMBL1741208) in THP-1 / MDM / PBMC. The rigorous "does this compound inhibit NLRP3" column.
- **Functional IL-1β IC50 (MSU-stimulated)** — IL-1β reduction in macrophage assays, pathway-modulator readouts. The "does this compound suppress the gout-relevant output" column.

The two measure different things and should not be cross-compared. Cell-free / mouse-cell figures are footnoted, not mixed into the human-cell column.

| Compound | Direct NLRP3 IC50 (human-cell, ChEMBL) | Functional IL-1β IC50 (MSU) | Gout-specific evidence | Exposure limitation | Current next gate |
|----------|---|---|---|---|---|
| **Ursolic Acid** | — (no curated NLRP3 entry; ChEMBL v37: 16 entries pChEMBL≥6 — **ROR-γ 0.75 nM**, **NF-κB p65 31 nM**, **SENP1 6.4 nM**) | ~μM range (estimated) | No direct gout study | Bioavailability uncertain | Concentration-matched MSU assay |
| **Quercetin** | — (no curated entry; most potent activity is **5-LOX 300 nM**) | ~11 μM (MSU macrophages) | MSU rat | Bioavailability and ABCG2 interaction | Confirm human-cell target engagement and exposure |
| **Carnosine** | — (no curated entry) | μM range (LPS/HUA models) | HUA rat | Serum carnosinase | Exposure-matched urate and NLRP3 assay |
| **Lactoferrin** | — (no direct NLRP3 IC50; CP5 downstream) | ~μg/mL range (NLRP3/caspase-1/GSDMD axis) | No direct gout study | GI stability and tissue access | MSU-gout CP5/pyroptosis assay |
| **Taurine** | — (upstream K⁺ efflux, not direct) | μM–mM range | No direct gout study | Required concentration | MSU assay with K⁺-efflux readout |
| **Resveratrol** | — (no curated entry) | 0.1–25 μM | No direct gout study | Low bioavailability | Mechanistic comparator only |
| **EGCG** | — (no curated entry) | 10–50 μM | MSU mouse (Lee 2019) | Stability and intestinal ABCG2 urate direction | Measure free exposure, ABCG2 attribution, and urate flux |
| **Curcumin** | **24.2 μM** (human THP-1, ChEMBL v34/v37); DYRK2 IC50 = 2.5 nM (*J Med Chem* 2023) | 10–50 μM | MSU model | Very low bioavailability; intestinal ABCG2 inhibition | Exposure and transporter-interaction gate |
| **β-Caryophyllene** | — (docking only, no NLRP3 IC50); **CB2 Ki = 150 nM** | μM range | MSU rat | Low oral bioavailability | Human-cell MSU/CB2 dependence assay |
| **Sulforaphane** | — (no direct; Nrf2 EC50 **580 nM**) | μM range | HUA rat (Wang 2022) | Conversion and tissue exposure | Direct MSU and ABCG2-function assay |
| **Limonene** | — (no curated entry) | μM range | MSU rat (Venkatesan 2025) | Volatility and oral exposure | Human-cell concentration-matched assay |
| **Dapansutrile** (clinical comparator) | **1,000 nM** (human MDM) ¹ | — | Phase 2a (PMID 33005902) | Oral clinical comparator | Benchmark candidate assays |
| **Oridonin** (research comparator) | **5,180 nM** (human THP-1) ² | — | MSU mouse, cell-free | Low exposure | Benchmark covalent NLRP3 assay |

*Estimated; not published
¹ ChEMBL CHEMBL3989943, *Eur J Med Chem* 2023. Mouse J774A.1 IC50 = 1 nM — **1,000× species gap**, footnoted only.
² ChEMBL CHEMBL1164920, *Eur J Med Chem* 2023. Cell-free covalent-binding kinetics of 0.5–2 μM (Nature Commun 2018) is a different measurement class and should not be cross-compared.

---

## Falsification sequence

### **Gate 1: Gout-relevant biological validation (3–4 weeks)**
1. **Keratinocyte co-culture assay:** Test quercetin + ursolic acid synergy on MSU-stimulated IL-1β secretion
2. **Hyperuricemia rat model:** Repeat carnosine + uricase co-dosing (compare to uricase alone)
3. **Bioavailability study:** Oral dosing of quercetin + ursolic acid in mice; measure serum levels at 1, 4, 24 h

### **Gate 2: Source and delivery comparison, only after Gate 1 passes**
1. Compare existing dietary, standardized-extract, purified-compound, and engineered sources for identity, purity, stability, achievable exposure, and safety.
2. Select the least complex source that can deliver the validated material at the required exposure.
3. Consider engineered production only if existing sources cannot meet the experimental specification.

### **Gate 3: In-vivo translation after exposure and safety closure**
1. Test the selected exposure-valid material against vehicle and appropriate mechanistic comparators in an MSU-induced model.
2. Establish the exposure–response relationship and compare each candidate alone before any combination.
3. Confirm target engagement with direct NLRP3-pathway readouts; do not infer activity from the production route.

---

## Conclusion

The screen does not select a production chassis or a multi-compound intervention. Quercetin and carnosine have the closest gout-relevant animal evidence among the compared candidates; ursolic acid and resveratrol have strong production records but weaker gout specificity; taurine remains mechanistic extrapolation. The next decision is biological falsification under exposure-matched conditions, followed by sourcing only for candidates that survive.

---

## Appendix: ChEMBL IC50 Cross-Check (2026-04-23 baseline; 2026-07-01 refresh)

This section cross-references the IC50 values cited throughout this screen against the EMBL-EBI ChEMBL curated bioactivity database. Purpose: separate "direct NLRP3 inhibition" claims (measurable in a binding/inhibition assay) from "NLRP3 pathway modulation" claims (inferred from downstream IL-1β readouts, NF-κB suppression, ROS scavenging, or mechanistic review).

**ChEMBL version note:** Baseline v34 (2026-04-24). v37 refresh (2026-07-01, 24.5M activities, 2.9M compounds, 18.6K targets) — significant new entries surfaced for ursolic acid (16 entries at pChEMBL≥6, zero at v34), curcumin (DYRK2 2.5 nM), β-caryophyllene (CB2 now curated), disulfiram (LOXL4 59 nM), and oridonin (3 new 2024 entries). See the canonical [chembl-cross-check.md](./etc/chembl-cross-check.md) for the full 27-compound table + expanded findings.

**NLRP3 target ID:** CHEMBL1741208 (*NACHT, LRR and PYD domains-containing protein 3*, Homo sapiens, UniProt Q96P20).

### What ChEMBL confirms with direct human NLRP3 bioactivity

| Compound | ChEMBL ID | Human NLRP3 IC50 (direct) | Source (journal/year) |
|---|---|---|---|
| **Dapansutrile (OLT1177)** | CHEMBL3989943 | **1,000 nM (1.0 μM)** — human MDM cells, LPS+nigericin, pChEMBL=6.00 | *Eur J Med Chem* 2023 |
| **Oridonin** | CHEMBL1164920 | **5,180 nM (5.18 μM)** — human THP-1, LPS/ATP, pChEMBL=5.29 | *Eur J Med Chem* 2023 |

That's it. Those are the only two compounds in the inhibitor screen with a curated, cited IC50 against human NLRP3 in ChEMBL.

**Dapansutrile species gap:** ChEMBL shows dapansutrile at **1 nM (pChEMBL=9.00)** in *mouse* J774A.1 cells (*Eur J Med Chem* 2020 and *Bioorg Med Chem Lett* 2021) — a 1,000× potency gap versus human cells. Mouse preclinical assays make it look MCC950-class; human cell data puts it at the μM range. The 2020 Phase 2a clinical efficacy (52–84% pain reduction at 100–2000 mg/day) is therefore consistent with human-cell μM potency at high oral doses, not sub-nM potency.

**Oridonin:** ChEMBL's only curated human NLRP3 entry is 5.18 μM in human THP-1 (2023). The 0.5–2 μM figure from cell-free or mouse-derived assays in the original *Nature Communications* 2018 paper (covalent Cys279 binding kinetics) may not translate to a cellular human IC50.

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
**Next owner:** Role 1 collaborator (enzymatic mechanism / in-vivo validation)
