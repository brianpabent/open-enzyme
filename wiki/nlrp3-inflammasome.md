---
title: NLRP3 Inflammasome
aliases:
  - NLRP3
  - NOD-like receptor protein 3
  - inflammasome
  - IL-1β pathway
  - ASC speck
related:
  - uricase
  - gout
  - bpc-157
  - blood-barrier
  - complement-c5a-gout
  - spm-resolution-pathway
  - tnfsf14-gout-target
sources:
  - nlrp3-exploit-map.md
  - gout-deep-dive.md
  - peptide-gout-addendum.md
  - complement-c5a-gout.md
  - spm-resolution-pathway.md
  - tnfsf14-gout-target.md
  - chembl-cross-check.md
---

# NLRP3 Inflammasome

## Overview

The NLRP3 inflammasome is a multi-protein intracellular complex that acts as a master trigger for the acute inflammatory response in gout. It is composed of three core proteins: NLRP3 (the sensor), ASC (the adaptor), and pro-caspase-1 (the executioner). When activated, it cleaves pro-IL-1β into active interleukin-1β (IL-1β), a potent pro-inflammatory cytokine that drives the explosive pain and swelling of a gout flare. (Source: gout-deep-dive.md, nlrp3-exploit-map.md)

The inflammasome is not unique to gout—it evolved to respond to pathogenic danger signals. However, monosodium urate (MSU) crystals, which deposit in joints during hyperuricemia, directly trigger NLRP3 assembly through lysosomal rupture, potassium efflux, and reactive oxygen species (ROS) generation. In gout, the innate immune system mistakes metabolic crystals for microbial threats, producing an outsized inflammatory cascade. (Source: gout-deep-dive.md)

## The NLRP3 Activation Cascade: Seven Chokepoints (with Sub-Branches)

The NLRP3 inflammasome pathway operates as a sequential cascade with seven primary vulnerability points (chokepoints), several of which have mechanistically distinct sub-branches. Each represents a potential therapeutic target. Understanding the cascade structure reveals that gout can be attacked at multiple nodes simultaneously, rather than through a single intervention.

The v1.2 restructure (April 2026) adds CP0 (complement priming — C5a-dominant, upstream of NF-κB), sub-branches CP1a (TNFSF14/LIGHT priming amplifier) and CP1b (C5a→ROS), and promotes 5-LOX/LTB4 neutrophil chemotaxis to a first-class CP6a chokepoint (formerly an annotation under CP6). Active resolution via ALX/FPR2 SPMs becomes CP5b alongside the existing CP5a receptor blockade. (source: nlrp3-exploit-map.md)

### Chokepoint 0: Complement Priming (C5a-Dominant)

**The Step:** Before NLRP3 assembles, monosodium urate crystals can directly activate the complement system via classical and alternative pathways. Complement activation cleaves C5, generating the anaphylatoxin **C5a**, which binds **C5aR1** on macrophages. C5a→C5aR1 signaling generates reactive oxygen species (ROS) that serve as the dominant priming signal for NLRP3 in gout — upstream of and partially independent of the LPS/TLR4→NF-κB axis (Cumpelik et al. 2016; Khameneh et al. 2017, *J Allergy Clin Immunol*). (Animal Model; source: complement-c5a-gout.md)

**Why It Matters:** Complement priming is upstream of all other chokepoints. Even maximal NF-κB suppression leaves CP0 open if C5a continues priming NLRP3 via ROS. The Open Enzyme stack currently has zero fermentable C5a/C5aR1 modulator — an acknowledged platform gap. (source: complement-c5a-gout.md)

**Exploits:**

- **Avacopan (Tavneos)**: FDA-approved oral C5aR1 antagonist indicated for ANCA-associated vasculitis (2021). Direct repurposing candidate for gout. Suppresses complement-driven NLRP3 priming at the receptor level. Clinical safety established; no gout-specific trial published as of April 2026. (Clinical Trial, ANCA vasculitis; Mechanistic Extrapolation for gout; source: complement-c5a-gout.md)

- **Platform gap:** No fermentable C5aR1 modulator currently in the Open Enzyme stack. Whether dietary flavonoids have meaningful C5aR1 affinity is an open question. Microbial C5aR1 antagonist peptides are a speculative long-term engineering target. (source: complement-c5a-gout.md)

See [Complement C5a in Gout](./complement-c5a-gout.md) for the full analysis.

### Chokepoint 1 (CP1a / CP1b): NF-κB Priming

**The Step:** Toll-like receptor (TLR) signaling (typically from damage-associated molecular patterns or LPS from gram-negative bacteria in the gut) triggers NF-κB activation. NF-κB translocates to the nucleus and drives transcription of pro-inflammatory genes: NLRP3 itself, pro-IL-1β, pro-IL-18, and ASC. This is the "priming" step—building the components of the inflammasome.

**Why It Matters:** Without sufficient NLRP3 and pro-IL-1β protein, downstream activation cannot occur at meaningful levels. Preventing priming reduces the inflammasome's capacity to respond. CP1a refers to TNFSF14/LIGHT amplification of NF-κB priming (see below); CP1b refers to C5a→ROS priming (overlapping with CP0). (Source: nlrp3-exploit-map.md)

**Exploits:**

- **KPV peptide** (Lys-Pro-Val): The C-terminal tripeptide of alpha-melanocyte-stimulating hormone (α-MSH). Stabilizes IκB-α, preventing NF-κB nuclear translocation. Research shows α-MSH and its derivative (CKPV)₂ specifically reverse the inflammatory effect of urate crystal formation. (Source: nlrp3-exploit-map.md)

- **Sulforaphane**: Activates the Keap1-Nrf2 pathway, the master regulator of antioxidant defense. Nrf2 competes with NF-κB for the transcriptional co-activator CBP/p300, suppressing NF-κB-driven transcription of NLRP3 and pro-IL-1β. Maximum bioavailability achieved by chewing raw broccoli sprouts (which co-localize glucoraphanin and the enzyme myrosinase) or using freeze-dried sprout capsules. (Source: nlrp3-exploit-map.md)

- **Curcumin**: A validated NF-κB inhibitor. Native curcumin has ~1% bioavailability, but formulations like Theracurmin (27x improvement) or NovaSOL micellar curcumin (~185x improvement) achieve therapeutic plasma levels. Alternative: combine standard curcumin with piperine (black pepper), which inhibits hepatic glucuronidation and increases absorption ~2,000%. **ChEMBL v34 cross-check (2026-04-24):** Curcumin has a curated direct human NLRP3 IC50 of **24.2 μM** (ChEMBL; source: chembl-cross-check.md) — placing it in the same order of magnitude as oridonin (5.18 μM) but substantially higher than pharmaceutical benchmarks. Its NF-κB block is probably the primary gout-relevant mechanism at achievable tissue concentrations. (In Vitro; source: nlrp3-exploit-map.md, chembl-cross-check.md)

- **Berberine**: Suppresses NF-κB and TLR4 signaling, reduces NLRP3 mRNA expression, and remodels the gut microbiota to reduce LPS (lipopolysaccharide) that primes NLRP3 in the first place. Also effective against SIBO (small intestinal bacterial overgrowth), addressing the shared microbial-inflammatory nexus. Dose: 500 mg twice daily with meals. **ChEMBL v34 cross-check (2026-04-24):** Berberine's most potent curated ChEMBL bioactivity is against **tryptophan 2,3-dioxygenase (TDO): IC50 = 30 nM** — not NLRP3 directly. Its NLRP3-related activity is via NF-κB/TLR4 pathway modulation, consistent with its classification as an "NLRP3 pathway modulator" rather than a direct NLRP3 binder. (In Vitro; source: nlrp3-exploit-map.md, chembl-cross-check.md)

- **BPC-157**: Beyond its tissue-healing effects, BPC-157 modulates the nitric oxide (NO) system, which influences macrophage activation states and reduces the priming capacity of immune cells. (Source: nlrp3-exploit-map.md, peptide-gout-addendum.md)

- **TB-500 (Thymosin β4)**: Suppresses NF-κB p65 nuclear translocation and dampens JNK/p38 MAPK signaling in macrophages. Hits both Chokepoint 1 (priming) and Chokepoint 2 (activation). (Source: nlrp3-exploit-map.md)

- **Omega-3 fatty acids (EPA/DHA)**: Precursors to specialized pro-resolving mediators (SPMs) — resolvins (RvE1, RvD1/D2), protectins (PD1), and maresins (MaR1). SPMs suppress neutrophil recruitment and promote macrophage phenotype switching from M1 (inflammatory) to M2 (resolving). Dose: 3–4g EPA+DHA daily. (Source: nlrp3-exploit-map.md)

- **Resveratrol**: Activates SIRT1, which deacetylates p65 (NF-κB subunit), reducing its transcriptional activity. Use micronized trans-resveratrol, liposomal forms, or pair with pterostilbene (4x better bioavailability and same SIRT1 activation). **ChEMBL v34 cross-check (2026-04-24):** Resveratrol's strongest curated ChEMBL bioactivity is **DPP-4 inhibition at 0.6 nM** — not SIRT1 or NF-κB. Its classification here as a CP1 modulator rests on the SIRT1→p65 mechanism, which is mechanistically plausible but does not have a curated direct ChEMBL bioactivity against NLRP3 or NF-κB components. NLRP3 pathway modulator, not direct NLRP3 binder. (In Vitro; source: nlrp3-exploit-map.md, chembl-cross-check.md)

- **Andrographolide** (from Andrographis paniculata): Covalently modifies the p50 subunit of NF-κB via Michael addition, preventing DNA binding. One of the most potent natural NF-κB inhibitors. (Source: nlrp3-exploit-map.md)

- **Parthenolide** (from feverfew): Inhibits IKKβ (the kinase that degrades IκB) and directly modifies NF-κB p65. Dual mechanism. DMAPT (dimethylamino-parthenolide) is a more soluble derivative used in research. (Source: nlrp3-exploit-map.md)

- **Quercetin**: Inhibits NF-κB and also blocks xanthine oxidase (uric acid production). Phytosome form (Quercefit) provides 20x better bioavailability. Dose: 500–1000 mg daily. **Novel mechanism surfaced by the 2026-04-23 ChEMBL cross-check:** Quercetin's most potent curated ChEMBL bioactivity is against **5-lipoxygenase (5-LOX): IC50 = 300 nM** (*J Med Chem* 1991) — the enzyme that produces LTB4, a neutrophil chemoattractant that drives the neutrophil infiltration phase of MSU-triggered gout flares. Quercetin also has zero direct curated human NLRP3 bioactivities in ChEMBL; its NLRP3-inhibitor label is more accurately "NLRP3 pathway modulator" via NF-κB priming block. (In Vitro; source: nlrp3-inhibitor-screen.md; Source: nlrp3-exploit-map.md)

- **EGCG** (green tea catechin): Inhibits IKK activity, suppresses NF-κB. Dose: 400–800 mg daily or 3–5 cups green tea daily. Matcha provides the highest concentration. **TNFSF14 suppression (CP1a cross-link, 2026-04-24):** EGCG/green tea polyphenols suppress TNFSF14-induced IL-6 and downregulate HVEM receptor expression on target cells (source: tnfsf14-gout-target.md) — making EGCG one of the few natural compounds with documented activity at the TNFSF14/LIGHT priming amplifier (CP1a). **ChEMBL v34 cross-check:** EGCG inhibits human 20S proteasome at 86 nM (curated) — mechanistically upstream of NF-κB; the IKK/NF-κB effect is functional but not directly curated in ChEMBL as its top target. (In Vitro; source: nlrp3-exploit-map.md, tnfsf14-gout-target.md, chembl-cross-check.md)

- **Boswellia (AKBA)**: Acetyl-11-keto-β-boswellic acid directly inhibits IKKβ and 5-LOX. Dose: 300–500 mg standardized extract daily. (Source: nlrp3-exploit-map.md)

- **Vitamin D**: Vitamin D receptor (VDR) activation suppresses NF-κB. Target 50–70 ng/mL serum levels; 5,000–10,000 IU daily with K2. (Source: nlrp3-exploit-map.md)

- **Beta-caryophyllene** (CB2 agonist, food additive in black pepper/clove): In MSU-induced gouty arthritis in rats (100–400 mg/kg oral, animal model), dose-dependently reduced synovial TLR4, MyD88, p65 (NF-κB) expression — hitting CP1 alongside its CP2 NLRP3 suppression. This is the only cannabinoid or terpene with direct MSU gout-model evidence. (*Front Pharmacol* 2021;12:651305, PMID: 33967792). See [Cannabinoids & Terpenes](./cannabinoids-terpenes.md). (source: cannabinoids-terpenes.md)

- **TNFSF14/LIGHT blockade (CP1a sub-branch):** TNFSF14 (also called LIGHT, a TNF-superfamily cytokine) is the **second-highest fold-change gout-flare biomarker after IL-6** (Ea et al. 2024, *Ann Rheum Dis*, DOI: 10.1136/ard-2023-225305). LIGHT signals via HVEM and LTβR receptors on fibroblast-like synoviocytes, monocytes, and myeloid cells, driving NF-κB and AP-1 activation — amplifying CP1 priming parallel to LPS/TLR4. Ex vivo TNFSF14 blockade reduced LPS+MSU cytokine production. Safety caveat: LIGHT has dual pro-inflammatory and resolution roles — LIGHT-null mice have worse colitis, suggesting episodic rather than chronic blockade is safer. Natural compounds with TNFSF14 activity: EGCG/green tea polyphenols suppress TNFSF14-induced IL-6 (In Vitro); DHA shows inverse genetic association with circulating LIGHT. CERC-002 (anti-LIGHT mAb) showed positive Phase 2 data in COVID ARDS — potential repurposing candidate for gout. (Clinical Trial + In Vitro; source: tnfsf14-gout-target.md) See [TNFSF14 Gout Target](./tnfsf14-gout-target.md) for the full analysis.

- **CBG (Cannabigerol)**: NF-κB/MAPK pathway inhibition in RAW 264.7 macrophages (In Vitro, *J Microbiol Biotechnol* 2025). In colitis animal models (DNBS and DSS), reduced colonic IL-1β, MPO, iNOS — part of the effect is CB2-independent. Not gout-tested; strongest case is for gut inflammation, not systemic flare suppression. (source: cannabinoids-terpenes.md)

- **Limonene (d-limonene, Tier 3 supplement, PROMOTED 2026-04-26):** Nrf2 activator + TLR4 suppression (upstream NLRP3 priming block). Direct rat PO+MSU dual gout model — Venkatesan 2025 *Nutrients* (PMID 41515190): 50 mg/kg limonene reduced paw thickness, serum UA, IL-1β/TNF/IL-6, and improved antioxidant status; authors invoke NLRP3-IL-1β suppression as the mechanistic frame. GRAS food additive. Practical form: d-limonene softgel capsules 500–1,000 mg/day. (Animal Model; source: supplements-stack.md, cannabinoids-terpenes.md)

### Chokepoint 2: NLRP3 Activation and ASC Assembly

**The Step:** MSU crystal phagocytosis triggers potassium efflux from cells and mitochondrial reactive oxygen species (ROS) generation. These are the primary "Signal 2" inputs that cause NLRP3 to oligomerize and recruit ASC. The exact mechanism of signal transduction is still being elucidated, but K⁺ efflux and mtROS are the most validated triggers. Once activated, NLRP3 serves as a nucleation platform for ASC to polymerize into fibrillar aggregates (specks).

**Why It Matters:** This is where the inflammasome actually assembles. Blocking assembly prevents caspase-1 activation, regardless of how much pro-IL-1β was primed in Chokepoint 1. (Source: nlrp3-exploit-map.md)

**Exploits:**

- **Beta-hydroxybutyrate (BHB)**: The ketone body produced during fasting or ketogenic diet. BHB prevents potassium efflux, reduces ASC speck formation, and directly inhibits NLRP3 assembly. Notably, BHB is NOT dependent on AMPK, autophagy, or ROS reduction—it is a direct inhibitory effect on NLRP3 oligomerization. In rodent models, a ketogenic diet significantly reduced gout flare severity. Critical insight: traditional concern that ketosis raises uric acid is true short-term (ketones compete with urate for renal excretion), but with uricase handling uric acid clearance, ketosis becomes pure inflammasome suppression. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)

- **Oridonin**: An ent-kaurane diterpenoid from the Chinese herb Rabdosia rubescens. Covalently modifies cysteine 279 in the NACHT domain of NLRP3 via Michael addition—the same binding site as the pharmaceutical MCC950. Cell-free / mouse covalent-binding kinetics at 0.5–2 µM; curated **human THP-1 cellular IC50 = 5.18 μM** (ChEMBL v34, *Eur J Med Chem* 2023). Published in Nature Communications (2018): oridonin exhibits dose-dependent inhibition of caspase-1 cleavage and IL-1β secretion and is NLRP3-specific (does not affect NLRC4 or AIM2). Additionally activates Nrf2 and suppresses NF-κB independently—hitting Chokepoints 1 and 2. (Source: nlrp3-exploit-map.md; In Vitro ChEMBL cross-check 2026-04-23, source: nlrp3-inhibitor-screen.md)

- **NAC (N-Acetyl Cysteine)**: Replenishes glutathione, the master intracellular antioxidant. Reduces mtROS, thus reducing the Signal 2 trigger for NLRP3 assembly. Dose: 600–1200 mg daily. Widely available, inexpensive, well-tolerated. The limitation: does not specifically target mitochondria. (Source: nlrp3-exploit-map.md)

- **MitoQ (Mitoquinone)**: A coenzyme Q10 derivative conjugated to a triphenylphosphonium cation that targets specifically to mitochondrial membranes, accumulating 100–1000x higher than untargeted antioxidants. Directly scavenges mtROS. Dose: 10–20 mg daily. Available as MitoQ brand supplement. (Source: nlrp3-exploit-map.md)

- **Spermidine**: Essential for rapamycin-induced autophagy and directly suppresses NLRP3 activation. Found in aged cheese, mushrooms, soy, wheat germ. Supplement dose: 1–6 mg daily. A 2024 study showed spermidine mediates rapamycin's autophagy effects. Also reduces mtROS. (Source: nlrp3-exploit-map.md)

- **Trehalose**: A disaccharide that activates autophagy via TFEB (independent of mTOR), suppresses NLRP3 accumulation. Dose: 5–10g daily in water or as a sugar substitute. Found in mushrooms, honey, shrimp. (Source: nlrp3-exploit-map.md)

- **Tranilast**: An anti-allergic drug approved in Japan and South Korea since 1982. Directly binds the NACHT domain of NLRP3 and blocks oligomerization through the same binding site as MCC950, but via a different binding mode. Published in EMBO Molecular Medicine: tranilast showed "remarkable preventive or therapeutic effects" in mouse models of gouty arthritis, CAPS (cryopyrin-associated periodic syndromes), and type 2 diabetes. Safety profile: up to 600 mg daily clinically used for months with good tolerability. Not FDA-approved in the US but accessible internationally. (Source: nlrp3-exploit-map.md)

- **Autophagy inducers:**
  - **Intermittent fasting (16:8 minimum)**: Activates AMPK, inhibits mTOR, induces autophagy, and generates BHB. Two-for-one mechanism. (Source: nlrp3-exploit-map.md)
  - **Rapamycin**: Gold standard mTOR inhibitor, induces autophagy via spermidine pathway. Dose: 2–5 mg weekly. Requires prescription but accessible through longevity-focused physicians. (Source: nlrp3-exploit-map.md)

- **CBD, CBC, THCV** (P2X7 receptor block, upstream of K⁺ efflux): CBD (10 μM) reduces nigericin-induced K⁺ efflux ~13% in THP-1 monocytes and binds P2X7 at GLU172/VAL173 (In Vitro, Liu et al., *J Nat Prod* 2020, PMID: 32374168). CBC and THCV act via the same PANX1/P2X7 axis (*Molecules* 2023;28(18):6487). Mechanism partially overlaps with BHB's K⁺-efflux block — layering both at CP2 may have diminishing returns. None are gout-tested; extrapolation only. (source: cannabinoids-terpenes.md)

- **Beta-caryophyllene** (CB2 agonist): In the same MSU rat gout model as CP1, suppressed synovial NLRP3, caspase-1, and ASC expression (Animal Model, *Front Pharmacol* 2021). CDOCKER interaction energy 31.92 kcal/mol against NLRP3 (computational; no cell-free IC50 reported). CB2 Ki = 155 nM; functional EC50 ~38 nM. THCV has higher CB2 affinity (Ki = 7.5 nM) but no gout-model data. (source: cannabinoids-terpenes.md)

### Chokepoint 3: ASC Speck Assembly and Caspase-1 Recruitment

**The Step:** ASC (apoptosis-associated speck-like protein containing a CARD) oligomerizes into large fibrillar aggregates (specks) at the site of activated NLRP3. These specks serve as the physical platform for recruiting and activating pro-caspase-1. The speck formation is dependent on PYD domain interactions between ASC monomers and requires microtubule-mediated intracellular transport (ASC is normally localized to mitochondria, but must be transported to NLRP3 at the ER).

**Why It Matters:** Preventing speck assembly prevents recruitment and oligomerization of pro-caspase-1, blocking the conversion to active caspase-1 that executes IL-1β cleavage. (Source: nlrp3-exploit-map.md)

**Exploits:**

- **Colchicine**: Depolymerizes microtubules, preventing microtubule-mediated transport of ASC from mitochondria to ER-localized NLRP3. Without transport, specks cannot form. Additionally, colchicine impairs neutrophil chemotaxis, phagocytosis of MSU crystals, and secretion of inflammatory mediators—multi-hit disruption of the inflammasome platform. The oldest and most validated NLRP3 pathway disruptor for gout. **Dual-hit mechanism:** also directly inhibits the P2X7 ATP-gated ion channel pore (CP2), blocking K⁺ efflux upstream of NLRP3 activation (Leung et al. 2015 *Semin Arthritis Rheum* PMID 26228647). Low-dose acute regimen (1.2 mg + 0.6 mg one hour later) validated by the AGREE trial (Terkeltaub 2010 PMID 20131255). Cardiovascular repositioning: COLCOT (23% CV event reduction, Clinical Trial) and LoDoCo2 (31% reduction, Clinical Trial) led to FDA approval of Lodoco 0.5 mg for atherosclerotic CVD in June 2023. Narrow therapeutic index (~3–5× separation between therapeutic and toxic dose); CYP3A4/P-gp interaction surface is the primary clinical management challenge. See [colchicine.md](./colchicine.md) for the full dossier. (Source: colchicine.md; nlrp3-exploit-map.md, gout-deep-dive.md)

- **Spermidine** (again): Enhances autophagy, which clears damaged mitochondria before they can export ASC and recruit it to specks. (Source: nlrp3-exploit-map.md)

- **BHB** (again): Beyond preventing K⁺ efflux and NLRP3 oligomerization, BHB reduces ASC oligomerization and speck formation directly. Multi-chokepoint weapon. (Source: nlrp3-exploit-map.md)

### Chokepoint 4: Caspase-1 Activation and Substrate Cleavage

**The Step:** The assembled ASC speck recruits and activates pro-caspase-1 through proximity and conformational changes. Active caspase-1 then cleaves pro-IL-1β into the mature, secreted form of IL-1β, and also cleaves gasdermin D (which we address in Chokepoint 6). This is the executioner step.

**Why It Matters:** Active caspase-1 is the irreversible commitment to IL-1β secretion and pyroptotic cell death. Blocking this step directly prevents mature IL-1β production. (Source: nlrp3-exploit-map.md)

**Exploits:**

- **VX-765 (Belnacasan)**: A prodrug that converts to VRT-043198, a potent, selective, reversible caspase-1 inhibitor. Blocks cleavage of pro-IL-1β, pro-IL-18, and gasdermin D simultaneously. Well-tolerated in human Phase 2a trials (though developed for epilepsy, not gout). Available from research chemical suppliers. (Source: nlrp3-exploit-map.md)

- **Procyanidin B2** (from grape seed extract): Reduces MSU crystal-induced caspase-1 cleavage and IL-1β secretion in macrophages by blocking cathepsin B (released from ruptured lysosomes, which is required for caspase-1 activation). Dose: 200–400 mg grape seed extract daily. (Source: nlrp3-exploit-map.md)

- **EGCG** (again, hitting multiple chokepoints): Suppresses caspase-1 activity in macrophages. Also blocks NF-κB (CP1) and IL-1β signaling (CP5). Dose: 400–800 mg daily or 3–5 cups matcha/green tea. (Source: nlrp3-exploit-map.md)

- **Berberine** (again, multi-chokepoint): Dose-dependently reduces caspase-1 mRNA expression and protein levels. (Source: nlrp3-exploit-map.md)

### Chokepoint 5: IL-1β and IL-18 Secretion and Signaling

**The Step:** Cleaved IL-1β is secreted from macrophages and binds to IL-1 receptor type 1 (IL-1R1) on neutrophils, endothelial cells, and other target cells. IL-1β drives vasodilation, neutrophil recruitment, pain signaling, and systemic inflammation. IL-18 (also cleaved by caspase-1) contributes to IFN-γ production and further immune amplification. This is where the inflammasome's output becomes systemically manifested as the acute gout flare.

**Why It Matters:** Even if inflammasome activation is incomplete, blocking IL-1β signaling at the receptor level stops the cascade from progressing to the clinical symptoms of a gout attack. (Source: nlrp3-exploit-map.md)

**Exploits:**

- **Anakinra (Kineret)**: Recombinant IL-1 receptor antagonist (IL-1Ra). Competitive antagonist at IL-1R1 that blocks both IL-1β and IL-1α from binding. Single injection can abort a flare within hours. FDA-approved for RA and CAPS, used off-label for gout. Limitation: 100 mg daily subcutaneous injection, short half-life (~4–6 hours), expensive without insurance. Demonstrates that blocking IL-1 signaling is sufficient to stop a gout flare. (Source: nlrp3-exploit-map.md)

- **Omega-3 SPMs** (again): EPA → Resolvin E1 (RvE1), DHA → Resolvin D1/D2 (RvD1/D2), Protectin D1 (PD1), Maresin 1 (MaR1). These specialized pro-resolving mediators actively command neutrophils to stop infiltrating and promote macrophage phenotype switching from M1→M2. Not just suppression but active resolution signaling. Dose: 3–4g EPA+DHA daily, or pre-formed SPM supplement (SPM Active by Metagenics: 2 softgels daily standardized to 17-HDHA and 18-HEPE). (Source: nlrp3-exploit-map.md)

- **Exercise**: Acute exercise transiently increases IL-1Ra (the body's endogenous IL-1 antagonist). Regular moderate exercise maintains elevated baseline IL-1Ra. Important caveat: avoid exercise during an active flare; benefit occurs between flares through chronic training. (Source: nlrp3-exploit-map.md)

- **EGCG** (again): Suppresses IL-1β secretion from macrophages and reduces IL-1β-induced downstream signaling in target cells (chondrocytes, synoviocytes). (Source: nlrp3-exploit-map.md)

### Chokepoint 5b: Active Resolution via ALX/FPR2 (Specialized Pro-Resolving Mediators)

**The Step:** Parallel to blocking IL-1β signaling (CP5a), the resolution phase of gout inflammation depends on specialized pro-resolving mediators (SPMs) — resolvins, protectins, maresins, and lipoxins — signaling through the ALX/FPR2 receptor on neutrophils and macrophages. Direct MSU gout evidence: **RvD1** reduced mechanical hyperalgesia, joint IL-1β, leukocyte recruitment, and ASC speck formation in a murine gout model (Zaninelli et al. 2022; Animal Model); **MaR1** suppressed gout inflammation via Prdx5 → AMPK/Nrf2 (Jiang et al. 2023; Animal Model). A 2023 expert review (Zaninelli) names ALX/FPR2 agonism as a priority gout therapeutic target. Complement-resolution link: aggregated neutrophil extracellular traps (aggNETs) drive gout resolution; tophi are essentially chronic unresolved aggNETs. (source: spm-resolution-pathway.md)

**Why It Matters:** CP5b is mechanistically distinct from CP5a (IL-1 receptor blockade). SPMs actively command neutrophil withdrawal and promote macrophage efferocytosis — shortening flare duration rather than only dampening peak intensity. Resolution is an active process, not mere cytokine suppression. (source: spm-resolution-pathway.md)

**Exploits:**

- **Omega-3 EPA/DHA precursors** (CP5b access via SPM biosynthesis): DHA → RvD1/D2, Protectin D1, MaR1; EPA → RvE1. The most accessible CP5b strategy is high-dose precursor loading. Dose: 3–4g EPA+DHA daily (high-EPA ratio preferred). The SPM-specific gout evidence above is at the animal model level; precursor supplementation provides both CP1 (priming suppression) and CP5b (active resolution) benefit. (Animal Model; source: spm-resolution-pathway.md, nlrp3-exploit-map.md)

- **Pre-formed SPM supplement** (SPM Active, Metagenics): Standardized to 17-HDHA and 18-HEPE; 2 softgels daily. Bypasses rate-limiting EPA→DHA→SPM conversion steps. (Mechanistic Extrapolation; source: spm-resolution-pathway.md)

- **Aspirin-triggered resolvins** (low-dose aspirin): Low-dose aspirin acetylates COX-2, shifting it to produce 15-epi-lipoxin A4 (aspirin-triggered LXA4) and 17R-resolvin D series — the aspirin-triggered resolvin pathway distinct from aspirin's anti-inflammatory COX-1 effect at higher dose. Note: aspirin at anti-inflammatory doses may impair some prostanoid-derived SPM precursors; the dose-activity relationship is complex. (Mechanistic Extrapolation; source: spm-resolution-pathway.md)

- **Lactoferrin** (indirect ALX/FPR2 modulator; long-term platform target): Fermentable at 3.5 g/L in *P. pastoris*; a candidate for future koji expression. Indirect SPM agonism mechanism. Year 5+ engineering target. (In Vitro; source: spm-resolution-pathway.md)

See [SPM Resolution Pathway](./spm-resolution-pathway.md) for the full analysis.

### Chokepoint 6a: Neutrophil Amplification via 5-LOX/LTB4

**The Step:** Once the initial inflammatory signal fires, MSU-primed mast cells and macrophages produce leukotriene B4 (LTB4) via the **5-lipoxygenase (5-LOX)** pathway. LTB4 is a potent neutrophil chemoattractant — it amplifies neutrophil recruitment to the inflamed joint, establishing the self-sustaining inflammatory loop that characterizes a full gout flare. Blocking LTB4 production or its receptor (BLT1) interrupts this amplification before it peaks. (Animal Model; source: nlrp3-exploit-map.md)

**Why It Matters:** Neutrophil infiltration is the proximate cause of gout flare pain and swelling. The NLRP3 inflammasome assembly in macrophages is only the trigger; it is the recruited neutrophil wave that sustains the flare. Blocking 5-LOX/LTB4 (CP6a) addresses the amplification loop directly, complementary to but distinct from GSDMD pore blockade (CP6b). (source: nlrp3-exploit-map.md)

**Exploits:**

- **Quercetin** (most potent curated 5-LOX inhibitor in the stack): IC50 = 300 nM against 5-lipoxygenase (*J Med Chem* 1991; ChEMBL v34, 2026-04-23) — 36× more potent than its functional NLRP3-pathway activity. Dose: 500–1,000 mg/day phytosome form. Blocks LTB4 production, suppressing the neutrophil chemotaxis amplification loop at CP6a. (In Vitro; source: nlrp3-inhibitor-screen.md, chembl-cross-check.md)

- **Boswellia (AKBA, acetyl-11-keto-β-boswellic acid)**: Directly inhibits both 5-LOX and IKKβ (CP1). Dual CP1/CP6a mechanism. Dose: 300–500 mg standardized extract daily. (In Vitro; source: nlrp3-exploit-map.md)

- **Zileuton** (pharmaceutical 5-LOX inhibitor, off-label): FDA-approved for asthma. Directly inhibits 5-LOX, blocking LTB4 synthesis. No gout-specific trials, but mechanistic case is strong given the LTB4/neutrophil axis in gout. (Clinical Trial for asthma; Mechanistic Extrapolation for gout; source: nlrp3-exploit-map.md)

### Chokepoint 6b: Gasdermin D Pore Formation and Pyroptotic Amplification

**The Step:** Caspase-1 also cleaves gasdermin D (GSDMD), generating an N-terminal fragment that oligomerizes into large membrane pores. These pores mediate pyroptotic cell death (lytic, inflammatory cell death) of the macrophage, releasing all its intracellular contents—including IL-1β, damage signals, and alarm molecules—into the tissue. This amplifies inflammation explosively.

**Why It Matters:** GSDMD pores are the final exit route for IL-1β and the trigger for the cellular-level inflammatory amplification that converts a localized inflammasome activation into a full-blown tissue flare. Blocking this step prevents pyroptotic amplification and may be the most direct way to limit flare severity. (Source: nlrp3-exploit-map.md)

**Exploits:**

- **Disulfiram (Antabuse)**: FDA-approved since the 1950s for alcohol use disorder. Discovered in 2020 (Nature Immunology) to specifically block gasdermin D pore formation at nanomolar concentrations. Covalently modifies Cys191 on GSDMD, preventing the N-terminal fragment from oligomerizing into membrane pores. Elegant mechanism: disulfiram allows pro-IL-1β cleavage (doesn't block caspase-1) but prevents pore formation. Consequence: IL-1β stays sequestered inside the cell rather than being released. No pores = no pyroptosis = no inflammatory amplification from cell death. Safety profile: FDA-approved with 70+ years of clinical data. Cost: ~$30/month. (Source: nlrp3-exploit-map.md)

- **Dimethyl Fumarate (DMF, Tecfidera)**: FDA-approved for multiple sclerosis. Discovered to succinate gasdermin D at Cys191, forming S-(2-succinyl)-cysteine. Blocks caspase-1-GSDMD interaction entirely, preventing cleavage, oligomerization, pore formation, and pyroptosis. Clinical evidence: MS patients taking DMF show reduced blood levels of both IL-1β and GSDMD-N (the cleaved pore-forming fragment). Also activates Nrf2 (hitting Chokepoint 1 simultaneously). Access: prescription for MS; off-label use requires creative conversation with prescriber. More expensive than disulfiram. (Source: nlrp3-exploit-map.md)

## Multi-Chokepoint Compounds

The most efficient exploits hit three or more chokepoints:

- **BHB (Beta-hydroxybutyrate)**: Blocks priming (CP1), prevents K⁺ efflux (CP2), reduces ASC oligomerization (CP3). Single metabolite produced by the body during fasting. Arguably the single most efficient exploit in the entire cascade. (Source: nlrp3-exploit-map.md)

- **Berberine**: Suppresses NF-κB/TLR4 (CP1), reduces NLRP3/ASC/caspase-1 mRNA (CP1+CP4), remodels gut microbiota to reduce LPS priming (CP1). Dual benefit for Lynn's SIBO. Swiss Army knife compound. (Source: nlrp3-exploit-map.md)

- **Oridonin**: Covalent NLRP3 inhibitor (CP2), NF-κB suppressor (CP1), Nrf2 activator (CP1+CP2). Natural compound mimicking pharmaceutical-grade NLRP3 inhibitor. (Source: nlrp3-exploit-map.md)

- **DMF (Dimethyl Fumarate)**: Nrf2 activator (CP1+CP2) AND gasdermin D succinator (CP6). Bridges first and last chokepoints. (Source: nlrp3-exploit-map.md)

- **EGCG**: NF-κB inhibitor (CP1), caspase-1 suppressor (CP4), IL-1β blocker (CP5). Three downstream chokepoints from drinking tea. (Source: nlrp3-exploit-map.md)

## Pharmaceutical NLRP3 Inhibitors

### Approved or In Clinical Development

- **Canakinumab (Ilaris)**: IL-1β monoclonal antibody. **FDA approved for gout in August 2023** — the first biologic ever formally indicated for gout in the US, 12 years after its initial 2011 rejection. Originally approved for CAPS/JIA. Very effective but expensive (~$300,000/year). Systemic immunosuppression risk. (Clinical Trial; *J Inflamm Res* 2026;19, PMID: 41867470. source: gout-clinical-pipeline.md)

- **Genakumab (Firsekibart)**: Chinese canakinumab competitor (GeneScience). Phase 3 NCT05983445 (313 patients) completed April 2024. Same anti-IL-1β mechanism. (Clinical Trial; source: gout-clinical-pipeline.md)

- **Anakinra (Kineret)**: IL-1 receptor antagonist. FDA-approved for RA and CAPS. Off-label for refractory gout. Less expensive than canakinumab but requires daily injection.

- **Rilonacept (Arcalyst)**: IL-1 trap. **Rejected by FDA for gout in 2012** despite a 1,315-patient Phase 3 (NCT00856206) demonstrating efficacy. Not currently in active gout development. (Clinical Trial; source: gout-clinical-pipeline.md)

- **Dapansutrile (OLT1177)**: Oral NLRP3 inhibitor. Phase 2a in gout (N=34, *Lancet Rheumatol* 2020, PMID: 33005902) showed 52–68% target joint pain reduction at day 3 across four dose levels. **However, no Phase 2b or Phase 3 trial in gout is registered on ClinicalTrials.gov as of April 2026.** Olatec's subsequent active programs moved to heart failure (Phase 1b NCT03534297, completed 2019) and COVID-19 (Phase 2 NCT04540120, terminated 2022). Dapansutrile in gout appears stalled, not advancing. (Clinical Trial; source: gout-clinical-pipeline.md) **Species-gap caveat (ChEMBL v34, 2026-04-23):** Dapansutrile's curated cellular IC50 is **1.0 nM in mouse J774A.1 cells but 1.0 μM in human MDM cells — a 1,000× species gap** (*Eur J Med Chem* 2020/2023, *Bioorg Med Chem Lett* 2021). The Phase 2a efficacy at 100–2,000 mg/day is consistent with human-cell μM potency at high oral doses, not with the sub-nanomolar mouse-cell potency. This reframes translational expectations for the entire oral-NLRP3-inhibitor class. (In Vitro; source: nlrp3-inhibitor-screen.md)

- **MCC950 (CRID3)**: The first specific NLRP3 inhibitor. Binds the Walker B motif in the NACHT domain, blocking ATP hydrolysis required for oligomerization. Clinical development terminated due to hepatotoxicity in Phase 1 RA trial, but it defined the druggable target and validated the mechanism. **ChEMBL cross-check (2026-04-23):** MCC950 / CRID3 / CP-456773 are not retrievable by common synonyms in ChEMBL v34's name search; the cited 7.5 nM IC50 (Coll et al. 2015 *J Biol Chem*, cell-free Walker B) has not been independently re-indexed by the MCP cross-check. Benchmark status unchanged, but the IC50 is not verified via ChEMBL. (source: nlrp3-inhibitor-screen.md)

### Two-Tier Labeling: Direct Inhibitors vs. Pathway Modulators (2026-04-23)

The 2026-04-23 ChEMBL v34 cross-check (see [nlrp3-inhibitor-screen.md](nlrp3-inhibitor-screen.md) appendix) surfaced a labeling rigor issue. Only two compounds in the wiki's broader NLRP3 discussion have a curated direct human NLRP3 IC50 in ChEMBL:

- **Dapansutrile:** 1.0 μM (human MDM, *Eur J Med Chem* 2023) — but 1 nM in mouse J774A.1 (1,000× species gap)
- **Oridonin:** 5.18 μM (human THP-1, *Eur J Med Chem* 2023)

MCC950 and tranilast have published direct NLRP3 assays in the primary literature but are not retrievable via ChEMBL's curated target-bound bioactivity table for human NLRP3 (CHEMBL1741208) by common synonyms.

**Compounds with zero curated direct human NLRP3 entries in ChEMBL:** quercetin, ursolic acid, tranilast, beta-caryophyllene. Their "NLRP3 inhibitor" status rests on functional IL-1β readouts in macrophage assays or upstream pathway effects (NF-κB priming, ROS, K⁺ efflux) — not direct NLRP3 binding/inhibition measurements.

**Going-forward convention:** Distinguish "direct NLRP3 inhibitor" (binding/inhibition IC50 measured against NLRP3 protein) from "NLRP3 pathway modulator" (functional IL-1β reduction, mechanism inferred). Both are clinically relevant — Open Enzyme ultimately cares about IL-1β output, not NLRP3 biochemistry per se — but the distinction sharpens how claims are written. (In Vitro; source: nlrp3-inhibitor-screen.md)

### NLRP3 Pipeline Has Drifted Out of Gout

The broader NLRP3 inhibitor pipeline has moved to other indications where the biology has wider therapeutic appeal: DFV890 (Novartis, knee osteoarthritis Phase 2 completed Dec 2024), NT-0796 (NodThera, obesity + semaglutide Phase 2a active), VTX3232 (Zomagen, Parkinson's Phase 2a completed April 2025), VENT-02 (Ventus, Parkinson's Phase 1b **terminated Oct 2025**), Inzomelid (Inflazome/Roche, CAPS Phase 1 completed), ZYIL1 (Zydus, Phase 1 completed). **No NLRP3-specific compound is in active gout-indicated trials as of April 2026.** This is a strategic data point for Open Enzyme's "food-derived NLRP3 adjunct" positioning — the prescription pipeline isn't delivering for gout. (source: gout-clinical-pipeline.md)

### Emerging Target: TNFSF14 (LIGHT) — CP1a Priming Amplifier

A 2024 *Annals of the Rheumatic Diseases* study (Ea et al., DOI: 10.1136/ard-2023-225305, PMID: 38373842) used the Olink 92-protein inflammation panel on gout flare vs. intercritical vs. treat-to-target patients. **TNFSF14 (TNF superfamily 14, also called LIGHT) was the second-highest fold-change gout-flare biomarker after IL-6.** LIGHT signals via HVEM and LTβR receptors on fibroblast-like synoviocytes, B cells, monocytes, and myeloid cells, activating NF-κB and AP-1 — a priming amplifier parallel to LPS/TLR4 (classified as CP1a in the exploit map v1.2). Ex vivo TNFSF14 blockade reduced LPS+MSU cytokine production; SNPs in TNFSF14 modulate myeloid cytokine output. CERC-002 (anti-LIGHT mAb) showed positive Phase 2 data in COVID ARDS — potential repurposing candidate. Safety caveat: LIGHT has dual roles (LIGHT-null mice have worse colitis) — episodic or LTβR-selective blockade is safer than total suppression. Natural compounds: EGCG suppresses TNFSF14-induced IL-6 and downregulates HVEM receptor expression (In Vitro); DHA shows inverse genetic association with circulating LIGHT. (Clinical Trial + In Vitro; source: gout-clinical-pipeline.md, tnfsf14-gout-target.md) See [TNFSF14 Gout Target](./tnfsf14-gout-target.md) for the dedicated analysis.

## Engineered Koji Opportunity

A. oryzae can theoretically be engineered to produce caspase-1 inhibitors or anti-inflammatory compounds during fermentation. While caspase-1 inhibitors are typically peptidomimetics (not easily biosynthesized), koji could be engineered to overproduce compounds like procyanidin precursors or EGCG-like polyphenols that indirectly suppress caspase-1 and NLRP3. The GRAS status of koji makes this feasible as a food-based therapeutic intervention. (Source: nlrp3-exploit-map.md)

## The SIBO–Gout–Lynn Connection

NLRP3 inflammasome activation is central to both gout and SIBO-driven intestinal inflammation. The same compounds that suppress gout suppress gut inflammation:

- **Berberine**: SIBO eradication (comparable to rifaximin) + NLRP3 suppression + NF-κB inhibition + gut microbiota remodeling. Same drug, both conditions through the same mechanism.

- **KPV peptide**: Originally studied for IBD/colitis. PepT1-mediated intestinal uptake delivers KPV directly to the gut. Reduces intestinal inflammation via NF-κB suppression in gut epithelium AND systemic inflammation driving gout.

- **Omega-3 SPMs**: Resolve intestinal inflammation AND joint inflammation through the same mediators.

- **BHB/fasting**: Suppresses NLRP3 in gut macrophages AND joint macrophages.

- **Spermidine + Trehalose**: Enhance autophagy, protecting gut barrier integrity and preventing macrophage NLRP3 activation in joints.

This overlap suggests a unified therapeutic strategy addressing both conditions simultaneously through shared NLRP3 modulation. (Source: nlrp3-exploit-map.md)

## AI Analysis: Production Candidates for Engineered Koji (April 2026)

**High-Priority NLRP3 Inhibitors Producible via Engineered Microbes:**

- **Ursolic Acid** (triterpene): **8.59 g/L in S. cerevisiae fed-batch** (highest microbial titer reported). Animal evidence for NLRP3 inflammasome suppression. GRAS status (apples, rosemary, oregano). Structural stability ideal for GI delivery. See [[ai-analysis/07-nlrp3-inhibitor-screen|07 — NLRP3 Inhibitor Screen]] for full production details.

- **Quercetin** (polyphenol): **930 mg/L in engineered S. cerevisiae**. Gout-specific animal data (MSU-induced edema reduction, IL-1β suppression). Dual mechanism: NLRP3 + xanthine oxidase inhibition. Bioavailability limitation (aglycone form) addressable via engineered glycosylation. IC50 ~11 μM vs. MCC950 (7.5 nM); potency gap noted.

- **Carnosine** (dipeptide): **Unique hyperuricemia evidence** — direct serum uric acid reduction + NLRP3 suppression in rat models. Multi-target (URAT1, GLUT9, ROS, p-p65). Production complexity moderate (~100–500 mg/L estimated); β-alanine synthesis limiting. Only candidate with published gout flare prevention data.

- **Native Koji Production — Kojic Acid**: *A. oryzae* naturally produces 3–5 g/L in solid-state fermentation. NLRP3 mechanism unknown; flagged for screening against inflammasome activation. Food-safe (cosmetics use), no engineering required. Candidate for discovery high-throughput screen.

See [[ai-analysis/07-nlrp3-inhibitor-screen|07 — NLRP3 Inhibitor Screen]] for potency rankings, bioavailability analysis, and production feasibility.

---

## Key Insights

**The Crystal Dissolution Danger Window:** When urate-lowering therapy (including [[uricase|koji-uricase]]) begins dissolving existing MSU crystal deposits, crystals temporarily become smaller with more surface area. Crystal shedding from tophi can trigger acute flares. The NLRP3 stack is essential during this phase—it prevents dissolution-triggered flares while the uricase handles the underlying uric acid problem. Both strategies must run simultaneously. (Source: nlrp3-exploit-map.md, gout-deep-dive.md)

**Disulfiram is Underrated:** An FDA-approved drug with 70 years of safety data, costing ~$30/month, that blocks the final step of IL-1β release and prevents pyroptotic amplification. Few rheumatologists discuss it because it was discovered by immunologists studying sepsis—a market inefficiency in medical knowledge. (Source: nlrp3-exploit-map.md)

**Ketosis Paradox Resolved:** The conventional wisdom that ketosis is bad for gout (ketones compete with urate for renal excretion) misses that BHB simultaneously and potently suppresses NLRP3 inflammasome activation. With [[uricase|koji-uricase]] handling uric acid clearance, ketosis becomes purely beneficial—all inflammasome suppression, no uric acid penalty. (Source: nlrp3-exploit-map.md)

## References

- Source: nlrp3-exploit-map.md — Systematic black hat pen-testing of NLRP3 inflammasome pathway; v1.2 restructure (April 2026) adds CP0, CP1a/1b, CP5a/5b, CP6a/6b — seven primary chokepoints
- Source: gout-deep-dive.md — Comprehensive gout pathophysiology including NLRP3 inflammasome overview and crystal-driven activation
- Source: peptide-gout-addendum.md — Deep dive into peptide mechanisms including BPC-157 and TB-500 NLRP3 interactions
- Source: complement-c5a-gout.md — Complement C5a as dominant NLRP3 priming signal (CP0); avacopan repurposing candidate
- Source: spm-resolution-pathway.md — Active resolution via ALX/FPR2 SPMs (CP5b); RvD1 and MaR1 gout animal model evidence
- Source: tnfsf14-gout-target.md — TNFSF14/LIGHT as second-highest gout-flare biomarker (CP1a); EGCG and DHA natural activity; CERC-002 clinical precedent
- Source: chembl-cross-check.md — ChEMBL v34 curated cross-check of stack compounds; curcumin 24.2 μM NLRP3 IC50, berberine TDO top target, resveratrol DPP-4 top target, EGCG proteasome 86 nM
