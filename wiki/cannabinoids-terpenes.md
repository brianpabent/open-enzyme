---
title: "Cannabinoids & Terpenes: NLRP3 Modulation, Gout Relevance, and EPI Applications"
date: 2026-04-23
tags: ["cannabinoids", "terpenes", "NLRP3", "CBD", "CBG", "CBC", "THCV", "beta-caryophyllene", "myrcene", "inflammation", "gout", "EPI", "P2X7", "CB2"]
related:
  - nlrp3-inflammasome.md
  - nlrp3-inhibitor-screen.md
  - nlrp3-exploit-map.md
  - supplements-stack.md
  - digestive-enzymes.md
  - gout-deep-dive.md
  - oridonin.md
  - bhb-ketones.md
  - gout-action-guide.md
  - self-experiment-protocol.md
  - colchicine.md
  - spm-resolution-pathway.md
sources:
  - "Liu et al., J Nat Prod. 2020;83(6):2025-2029. PMID: 32374168"
  - "Inflammation Research 2024;73(3):521-535 (CBD NLRP3 review)"
  - "Scientific Reports 2025;15:2124 (CBD bioavailability, high-fat meal)"
  - "CNS Drugs 2020;34:765-791 (CBD oral bioavailability review)"
  - "Front Pharmacol 2025;16:1705962 (CBG collagen-induced arthritis)"
  - "J Microbiol Biotechnol 2025;35 (CBG NF-kB/MAPK)"
  - "Biochem Pharmacol 2013;85(9):1306-1316 (CBG colitis, Borrelli)"
  - "J Pharmacol Exp Ther 2024;390 (CBG hemp extract colitis)"
  - "Molecules 2024;29(24):5471 (CBG comprehensive review, PPARg data)"
  - "Front Pharmacol 2021;12:651305 (beta-caryophyllene MSU gout model)"
  - "Inflammopharmacology 2016;24(6):307-318 (beta-caryophyllene CB2 neutrophil)"
  - "Molecules 2023;28(18):6487 (CBC, THCV, CBN in human macrophages)"
  - "Front Mol Neurosci 2019;12:487 (cannabinoid TRP channels)"
  - "J Cannabis Res 2021;3(1):43 (CBC TRP respiratory)"
  - "Br J Pharmacol 2007;157(7):1048-1062 (THCV CB1/CB2)"
  - "Br J Pharmacol 2008;153(2):199-215 (THCV pharmacology)"
  - "Int J Mol Sci 2022;23(14):7891 (myrcene adjuvant arthritis)"
  - "Biomolecules 2020;8(8):296 (quercetin CYP3A4 inhibition)"
  - "Pharmaceutics 2024;17(3):319 (cannabinoid drug interactions)"
---

# Cannabinoids & Terpenes: NLRP3 Modulation, Gout Relevance, and EPI Applications

Cannabinoids (CBD, THC, CBG, CBC, THCV) and terpenes (beta-caryophyllene, limonene, myrcene, alpha-pinene, linalool) probe several gout weaknesses: P2X7-driven potassium efflux, CB2-mediated immune-cell activation, NLRP3 assembly, and neutrophil recruitment. The leading evidence remains preclinical, and route-specific exposure is a recurring constraint.

**Bottom line:** Beta-caryophyllene and limonene have direct MSU-model evidence. CBD has functional NLRP3 data but no gout-specific model, and its mechanism is upstream P2X7 modulation rather than direct NLRP3 binding. CBG and THCV remain indirect candidates; myrcene has analgesic arthritis data but no NLRP3 assay.

> **Species-gap caveat:** Rodent NLRP3 potency does not establish human-cell potency; apply the cross-species standard in [`chembl-cross-check.md`](./etc/chembl-cross-check.md) before making dose claims.

---

## 1. Cannabinoids and NLRP3 Inflammasome Modulation

### CBD (Cannabidiol)

CBD is the most studied cannabinoid for anti-inflammatory effects outside the psychoactive pathway.

**Mechanism — what's actually known:**

CBD does NOT directly bind NLRP3 or ASC. The mechanism is upstream, primarily via P2X7 receptor modulation and NF-kB inhibition.

- **P2X7 modulation (in vitro):** CBD (10 μM) reduced nigericin-induced K+ efflux by 13.7-13.0% in human THP-1 monocytes. Computational docking identifies CBD binding interactions with GLU172 and VAL173 residues on P2X7. K+ efflux is the canonical signal 2 trigger for NLRP3 assembly. Blocking it upstream prevents inflammasome formation without direct NLRP3 engagement (Liu et al., *J Nat Prod* 2020, PMID: 32374168).
- **NF-κB inhibition:** Multiple in vitro studies report CBD blocks nuclear translocation of NF-κB in macrophages, reducing NLRP3 gene expression at the transcriptional level (CP1 — priming block).
- **Functional NLRP3 suppression:** CBD at 0.1, 1, and 10 μM reduced IL-1β secretion in LPS-nigericin-stimulated THP-1 monocytes by 63.9%, 64.1%, and 83.1%, respectively. The 83.1% reduction at 10 μM is noted as "comparable to MCC950 and oridonin" in the same assay system (in vitro). Interpret cautiously — this comparison is assay-specific and the IC50 context differs from benchmark measurements.

**No formal IC50 for NLRP3 inhibition has been reported for CBD.** The functional data suggests activity in the 0.1–10 μM range, putting it in roughly the same neighborhood as quercetin (~11 μM) rather than MCC950 (7.5 nM) or oridonin (nM–low μM covalent).

**Gout-specific data:** None found. CBD has not been tested in MSU crystal-induced inflammation models in published literature. The mechanistic basis exists (P2X7 → K+ efflux → NLRP3), but the gout application is mechanistic extrapolation.

**Oral bioavailability and GI pharmacokinetics:**

- Absolute oral bioavailability: ~6% fasting; 4–17× higher with a high-fat meal (geometric mean Cmax ratio = 17.4 fed vs. fasting; AUC ratio = 9.7) (*Scientific Reports* 2025).
- 70–75% of absorbed dose undergoes hepatic first-pass metabolism before systemic circulation (*CNS Drugs* 2020).
- Micellarization in intestinal fluid (fed state): 14.15% (10 mg CBD) and 22.67% (100 mg CBD). Fasted state: 0.65% and 0.14% respectively.
- **GI concentration constraint:** Low systemic bioavailability does not imply high active luminal concentration. Lipid/fecal-matrix sequestration, gastric-acid lability, and extensive host metabolism limit free CBD; direct colonic-microbial degradation is only weakly evidenced. Gastric-acid conversion to THC is stomach-specific (~85% at 60 min, with no conversion in neutral buffer; [Merrick 2016, PMID 28861485](https://doi.org/10.1089/can.2016.0020)). The "poor bioavailability = gut-lumen concentration" hypothesis is not supported. CBD is not an ABCG2/BCRP inhibitor; see [`abcg2-modulators.md` §"Gut-luminal metabolic stability"](./abcg2-modulators.md).

**Open questions remaining:**
- Does CBD's P2X7 inhibition in the gut specifically suppress MSU-relevant inflammasome signaling in gut-associated macrophages?
- Any interaction between CBD and the enteric nervous system's inflammasome regulation?

### THC (Delta-9-Tetrahydrocannabinol)

THC activates CB1/CB2 receptors. CB2 activation is anti-inflammatory in multiple immune cell types.

**Relevance:**
- CB2 agonism suppresses NF-κB and downstream IL-1β in some models (CP1)
- CB2 is expressed on macrophages, neutrophils, and gut-associated lymphoid tissue
- Psychoactivity and regulatory status constrain THC delivery, while its CB2 mechanism provides a comparison point for beta-caryophyllene and THCV.

**Translation boundary:** Direct human gout evidence is absent. Psychoactivity, variable local regulation, and route-dependent exposure complicate testing relative to non-psychoactive CB2 agonists.

### CBG (Cannabigerol)

CBG is the biosynthetic precursor to both CBD and THC. Non-psychoactive. Has newer animal model data that is relevant.

**NLRP3 evidence — yes, direct:**

- **Animal model (collagen-induced arthritis in rats, 2025):** CBG reduced NLRP3 expression in blood and synovial tissue. Also significantly reduced NLRP1A, caspase-1, and gasdermin D (pyroptosis marker). Model: collagen-induced arthritis (CIA), not MSU/gout (*Front Pharmacol* 2025;16:1705962, PMID: 41230096).
- **In vitro (RAW 264.7 macrophages):** CBG anti-inflammatory effects via MAPK and NF-κB pathway inhibition; no cytotoxicity up to 15 μM (*J Microbiol Biotechnol* 2025, PMID: 41423277).

**PPARγ agonism — quantified (and weak):**

CBG is a partial PPARγ agonist with higher affinity than CBD or THC at that receptor, but the absolute affinity is modest:
- EC50 for PPARγ activation: 1,270–15,700 nM
- Ki for PPARγ: ~11.7 μM

At physiologically achievable oral concentrations, PPARγ activation by CBG is likely minimal. The PPARγ → NLRP3 suppression connection exists (ligand-dependent transrepression of NF-κB and inflammasome), but CBG-specific PPARγ → NLRP3 data has not been published. This remains mechanistic extrapolation.

**IBD/gut inflammation evidence:**

- **Borrelli et al. 2013 (murine DNBS-induced colitis, animal model):** CBG reduced colon MPO activity, iNOS expression; increased SOD activity; normalized IL-1β, IL-10, IFN-γ. CB2 receptor antagonism enhanced the anti-inflammatory effect, suggesting the CBG mechanism is partially CB2-independent (*Biochem Pharmacol* 2013, PMID: 23415610).
- **2024 (DSS-induced colitis, animal model):** High-CBG hemp extract reduced colitis severity scores, improved colon length, reduced colonic damage, and modulated microbiome (*J Pharmacol Exp Ther* 2024, PMID: 38974519).

**Translation boundary:** CBG has relevant animal gut data, but the CIA arthritis NLRP3 result is not gout-specific. PPARγ agonism is too weak at achievable concentrations to be the primary mechanism; NF-κB/MAPK inhibition is the better-supported anti-inflammatory explanation.

### CBC (Cannabichromene)

CBC is a non-psychoactive cannabinoid with newer in vitro NLRP3 data and potent TRP channel activity.

**NLRP3 inhibition evidence:**

- **In vitro (THP-1 macrophages, LPS+ATP stimulation):** CBC dose-dependently suppressed pro-IL-1β and mature IL-1β. Lower doses particularly effective at suppressing the second phase (activation) of the inflammasome. Mechanism: mitigates the PANX1/P2X7 axis and downregulates IL-6/TYK2/STAT3 pathway (*Molecules* 2023;28(18):6487, PMID: 37764262). No formal IC50 reported.

**TRP channel activity — strongest among cannabinoids:**

- **TRPA1:** EC50 = 90 nM for activation; desensitization IC50 = 370 nM. Very potent.
- **TRPV4:** EC50 = 600 nM; desensitization IC50 = 9.9 μM
- **TRPV3:** EC50 = 1.9 μM
- In vivo relevance: Inhaled CBC reduced cytokine production in acute respiratory distress models via TRPA1/TRPV1 mechanisms (*J Cannabis Res* 2021, PMID: 34598736).

**NLRP3 priming link via TRP channels:** TRPA1 and TRPV1 activation can increase intracellular calcium and ROS, which are NLRP3 priming signals. However, this would be a priming ACTIVATOR, not an inhibitor — the TRP activation data cuts the opposite direction from anti-inflammatory intent. CBC's NLRP3 suppression (via PANX1/P2X7 in macrophages) appears to operate separately from its TRP channel pharmacology. The two effects are not in conflict but are mechanistically distinct.

**GI data:** No pure CBC GI inflammation studies found.

**Translation boundary:** The PANX1/P2X7 mechanism overlaps with CBD, while gout data and pure-compound GI data are absent. Regulatory and sourcing complexity add another constraint.

### THCV (Tetrahydrocannabivarin)

THCV has stronger CB2 affinity than beta-caryophyllene and new NLRP3 data.

**NLRP3 inhibition evidence:**

- **In vitro (THP-1 macrophages, LPS+ATP):** THCV at 5 and 15 μM suppressed both pro-IL-1β and mature IL-1β. Suppressed the IL-1β/Pro-IL-1β ratio (marker of activation phase). Mechanism: PANX1/P2X7 axis blockade and NF-κB suppression (*Molecules* 2023;28(18):6487, PMID: 37764262).

**CB1/CB2 receptor profile — notable:**

- **CB1:** High-affinity antagonist at low/moderate doses (Ki = 75.4 nM); shifts toward partial agonism at high in vivo doses
- **CB2:** High-affinity partial agonist (Ki = 7.5 nM; 95% CI: 5.7–10.0 nM) — notably higher CB2 affinity than beta-caryophyllene (CB2 Ki ~155 nM)
- IC50 for CB1 antagonism: 52.4 nM (Δ9-THCV) and 119.6 nM (Δ8-THCV) vs. CP55,940

(*Br J Pharmacol* 2007;157(7):1048-1062 and 2008;153(2):199-215)

**No gout or uric acid data found.** THCV has not been tested in MSU crystal models or for effects on uric acid metabolism.

**Regulatory status:** THCV is psychoactive at high doses (CB1 agonism threshold) and is derived from cannabis. Sourcing and regulatory status are more complex than beta-caryophyllene. The high CB2 affinity is theoretically attractive, but beta-caryophyllene has direct gout animal model evidence that THCV lacks.

**Open question:** Would THCV's higher CB2 affinity (Ki 7.5 nM vs. beta-caryophyllene 155 nM) translate to better anti-inflammatory efficacy in gout models? This is testable but unpublished.

---

## 2. Terpenes with Anti-Inflammatory Properties

### Beta-Caryophyllene — Direct Gout Animal Model Data

**Key findings in MSU-induced gouty arthritis (animal model):**

- **Model:** MSU crystal injection into rat ankle joints (standard gout flare model)
- **Doses:** 100, 200, 400 mg/kg (single daily oral dose)
- **Results:** Significant, dose-dependent reduction in:
  - Ankle joint swelling and locomotor dysfunction
  - Serum IL-1β, IL-6, TNF-α
  - Synovial tissue NLRP3, caspase-1, ASC expression
  - TLR4, MyD88, p65 (NF-κB) expression in synovial tissue
- **Computational docking:** CDOCKER interaction energy = 31.92 kcal/mol (suggests NLRP3 direct binding; no formal IC50)
- **Evidence level:** Animal model (in vivo, MSU-induced gouty arthritis in rats)
- **Citation:** *Front Pharmacol* 2021;12:651305. PMID: 33967792

This is the only terpene or cannabinoid with direct, published data in the gout-specific MSU crystal model.

**CB2 agonism — receptor affinity data:**

- CB2 Ki: 155 ± 4 nM (selective CB2 agonist, full agonist functionally)
- Functional CB2 EC50: ~38 nM (cAMP assay in CHO-K1 cells) to 1.9 μM (depending on assay)
- CB1 affinity: negligible (selectivity for CB2 over CB1 estimated at >100-fold)
- **ChEMBL v37:** CB2 Ki = **150 nM** (pChEMBL 6.82, *Eur J Med Chem* 2018). See [chembl-cross-check.md](./etc/chembl-cross-check.md). (In Vitro)

**Neutrophil effects — CB2 and NETosis correction:**

Available data do not support reduced NET formation as the mechanism:

- CB2 agonism (JWH133) shows **no effect on NETosis** in published studies
- CB1 agonists actually **promote** NET formation
- Beta-caryophyllene's neutrophil suppression acts through inhibiting migration/recruitment (via CB2-mediated chemokine reduction: CXCL1/KC, LTB4) rather than NETosis suppression (*Inflammopharmacology* 2016;24(6):307-318, PMID: 27379721)
- In the BCG infection model: 50 mg/kg beta-caryophyllene impaired neutrophil recruitment and reduced NO production

**Source and delivery:** Beta-caryophyllene is present in black pepper, cloves, and hops and is available in standardized oral extracts. Volatility and the animal-to-human exposure gap are the practical formulation constraints.

> **Dose-translation caveat (source: supplements-stack.md):** The 2021 MSU rat gout efficacy was demonstrated at 100–400 mg/kg oral. BSA-scaled to a 70 kg human, that is ~1.1–4.5 g/day — **20–50× above the typical supplement dose of 50–200 mg/day**. Whether common supplement exposure reproduces the synovial NLRP3/TLR4/NF-κB suppression seen in rats is unverified. Treat this as "plausible mechanism, dose adequacy unconfirmed" until a PK/PD translation study resolves the gap.

### Limonene

**Mechanism:** Nrf2 activator + TLR4 suppression (upstream NLRP3 priming block); suppresses NF-κB, NLRP3, ASC, caspase-1 expression via NRF2-dependent pathway. Hits CP1 (NF-κB/TLR4) and CP2 (NLRP3 assembly).

**Gout-specific evidence:** Direct rat PO+MSU dual gout model — Venkatesan 2025 *Nutrients* (PMID 41515190): 50 mg/kg limonene reduced paw thickness, serum UA, IL-1β/TNF/IL-6, and improved antioxidant status; authors invoke NLRP3-IL-1β suppression as the mechanistic frame. (Animal Model; source: supplements-stack.md)

**Source and delivery:** d-limonene occurs in citrus peel and is commercially available in standardized softgel capsules. Volatility, formulation, and translation from the rat exposure remain the main delivery questions.

**Contraindications:** None absolute. Citrus allergy (rare; d-limonene is the dominant terpene in citrus peel). GERD patients: d-limonene is marketed for GERD support but can transiently worsen reflux in a subset (paradoxical LES relaxation). Pregnancy: insufficient supplement-dose data; food-level intake fine.

**Drug interactions:**
- **CYP3A4 substrates (statins, calcium channel blockers, immunosuppressants):** d-limonene weakly induces CYP3A4 at chronic doses; clinical significance is small at the gout-relevant range.
- **Acid-suppression drugs (PPIs, H2 blockers):** mechanistic overlap with GERD use; not a pharmacological conflict.

**Dose-dependent risk profile:**
- 500–1,000 mg/day: well-tolerated. GRAS food-additive compound at much higher cumulative dietary exposure (orange peel, citrus oils in foods).
- >2 g/day chronic: case reports of mild hepatic enzyme elevation (rare; idiosyncratic).
- Inhalation/vaporized forms have very different PK and are not appropriate for NLRP3/gout endpoint use.

**Combination constraints:**
- **Synergy with sulforaphane, oridonin (Nrf2 axis):** cumulative Nrf2 induction with diminishing returns.
- **No ABCG2 interaction documented.**


### Myrcene

Myrcene has meaningful analgesic and anti-inflammatory data in arthritis models, but no direct NLRP3 assays.

**Arthritis model data (animal model, in vivo):**

- **Model:** Adjuvant monoarthritis in rats (knee joint)
- **Doses:** 1 and 5 mg/kg (local sc injection)
- **Acute pain (120 min):** 1 mg/kg improved nociception by 211.0 ± 17.93%; 5 mg/kg by 269.3 ± 63.27%
- **Chronic dosing (days 1–21):** Sustained reduction in joint pain and inflammatory scores
- **Receptor mechanism:** Analgesic effect blocked by both CB1 antagonist (AM281) and CB2 antagonist (AM630); anti-inflammatory effect (leukocyte rolling) blocked by CB2 antagonist only — suggesting dual CB1+CB2 involvement for pain, CB2 primarily for inflammation
- **Anti-inflammatory markers:** Reduced leukocyte rolling (early phase); reduced adhesion and vasodilation (chronic)
- **Citation:** *Int J Mol Sci* 2022;23(14):7891. PMID: 35887239

**Analgesic mechanism:**

Partially opioid-dependent (naloxone-reversible component), but primarily via:
- CB1/CB2 receptor engagement (dominant mechanism in arthritis model)
- TRPV1 activation (Ca2+ influx-mediated analgesia)
- COX/PGE2 inhibition (comparable to indomethacin for PGE2 reduction)
- Mechanism: endogenous opioid release via alpha-2-adrenergic stimulation — myrcene does not bind opioid receptors directly

**NLRP3 data:** None found. The COX/PG inhibition and CB2-mediated leukocyte suppression indirectly reduce NLRP3 priming signals, but myrcene has not been tested in NLRP3-specific macrophage assays. This is mechanistic extrapolation.

**Gout-specific relevance:** The arthritis model is adjuvant-induced, not MSU crystal-induced. The CB2-mediated leukocyte recruitment suppression is mechanistically relevant to gout (neutrophil influx is a key amplifier of MSU flares), but no MSU data exists.

**Pain management use case:** Myrcene's strongest case is analgesic during acute flares — particularly the CB2-mediated neutrophil suppression and the non-opioid pain relief in inflammatory arthritis. This is different from NLRP3 suppression. For chronic prevention, it's weaker than beta-caryophyllene.

### Alpha-Pinene

- Monoterpene; in vitro anti-inflammatory (IL-6, TNF-α suppression in LPS-stimulated macrophages)
- No NLRP3-specific data; no gout data
- Volatile monoterpene with route-specific formulation and exposure constraints.
- **Verdict:** Low priority pending direct NLRP3 or gout evidence.

---

## 3. Uric Acid Metabolism Connections

Cannabis compounds are not known to directly affect uric acid synthesis (xanthine oxidase) or renal excretion (URAT1/ABCG2). No new evidence found to challenge this.

The speculative renal inflammation angle (CBD/CBG → reduced renal inflammation → improved urate clearance) remains mechanistic extrapolation with no direct evidence. No data on cannabinoid effects on serum urate levels found.

The current evidence supports inflammation and barrier hypotheses more than a direct urate-production or transporter hypothesis. Limonene's rat result is an exception that needs mechanistic replication.

---

## 4. Combination hypotheses and drug interactions

### Mechanistic overlap

Current CP coverage from [NLRP3 Exploit Map](nlrp3-exploit-map.md):
- CP1 (NF-κB priming): BHB, oridonin, quercetin, KPV
- CP2 (NLRP3 assembly): Oridonin (covalent Cys279), BHB
- CP3 (ASC speck): BHB, oridonin
- CP4 (Gasdermin D): Disulfiram

**Cannabinoids/terpenes offer:**
- **CB2 agonism (beta-caryophyllene, THCV):** Reduces immune cell activation upstream of NLRP3 priming via TLR4/MyD88 suppression. Beta-caryophyllene in the MSU model hit both TLR4/NF-κB (CP1) and NLRP3/caspase-1 (CP2). CB2-mediated mechanism is mechanistically distinct from oridonin (Cys279) or BHB (K+ efflux) — additive potential.
- **P2X7 block (CBD, CBC, THCV):** P2X7 → K+ efflux is a key NLRP3 activation trigger at CP2. This partially overlaps with BHB's mechanism (BHB also reduces K+ efflux). Adding a P2X7 blocker on top of BHB may have diminishing returns at the same chokepoint.
- **PPARγ agonism (CBG):** CBG's affinity is modest (EC50 1,270–15,700 nM), and the PPARγ → NLRP3 link is mechanistic extrapolation rather than direct evidence.

### Pharmacokinetic Interaction: Quercetin + CBD

**Clinically relevant finding:** Quercetin inhibits CYP3A4 with IC50 = 1.97 μM and also inhibits intestinal UDP-glucuronosyltransferase at achievable concentrations (*Biomolecules* 2020, PMID: 32751996). CBD is metabolized primarily by CYP2C19 and CYP3A4. Co-administration of quercetin and CBD would be expected to increase CBD plasma exposure — essentially a grapefruit-juice-like effect.

- **Translation consequence:** Co-exposure could increase CBD plasma concentration and creates dose uncertainty; the interaction has not been tested in a gout setting.
- **Evidence level:** In vitro enzyme inhibition; pharmacokinetic inference.

### Cannabinoids + BHB

No published data found on CBD, CBG, or beta-caryophyllene combined with BHB. The mechanisms are distinct enough (P2X7 vs. K+ efflux / histone deacetylase inhibition vs. mitochondrial protection) that additive effects are plausible, but no empirical evidence exists.

### Cannabinoids + Oridonin

No direct combination studies. CBD (P2X7 upstream) and oridonin (covalent NACHT domain Cys279) operate at different points in the inflammasome assembly sequence. No known antagonistic interactions. Additive or synergistic effects are plausible but untested.

---

## 4a. Topical-delivery hypothesis

Topical CBD:THC has no direct human gout-flare RCT evidence. The proposed mechanism combines local CB2 signaling and TRP-mediated analgesia, but skin penetration, synovial exposure, cannabinoid contribution, and interaction with cooling have not been isolated. A controlled topical-vehicle comparison with local pharmacokinetics and flare readouts is required before treating this as an acute-flare intervention. (Mechanistic Extrapolation; source: [gout-action-guide.md](./gout-action-guide.md))

---

## 5. Digestive Health and EPI Relevance

**CBG is the strongest gut candidate:**

- Direct in vivo colitis data (Borrelli 2013; Frontiers 2024)
- Reduces IL-1β, MPO activity, iNOS in gut tissue; modulates microbiome
- CB2 receptor expressed throughout the enteric nervous system
- Mechanism appears partly CB2-independent (SR144528 enhancement in Borrelli study suggests additional pathways)

**CBD GI pharmacokinetics — revisited:**

The poor systemic bioavailability (~6% fasting) does NOT support a "stays in gut lumen" model. The unabsorbed CBD fraction is likely degraded, not retained as active compound. For gut-lumen anti-inflammatory intent, CBD is not mechanistically well-suited compared to a molecule like KPV (which is absorbed intact via PepT1 directly in gut epithelium) or BPC-157.

**CB1 motility caution:** CB1 agonism (THC, high-dose myrcene) slows gut motility. This is a risk for EPI patients who may already have dysmotility. CB2-selective agonists (beta-caryophyllene, THCV) avoid this concern.

**EPI-specific data:** None found for any cannabinoid or terpene. The connection remains indirect: if cannabinoids reduce gut inflammation and improve barrier integrity, they could reduce secondary inflammation worsening enzyme deficit symptoms. This is mechanistic extrapolation.

**Open questions:**
- Any interaction between cannabinoids and exogenous pancreatic enzyme supplements (Creon/Zenpep)? No data found.
- CBG PPARγ agonism and acinar cell health? No data found.

---

## 6. Evidence summary and translation priorities

### Potency Hierarchy in Context

| Compound | NLRP3 Mechanism | Evidence Level | Gout-Specific? | Estimated Potency vs. Quercetin (IC50 ~11 μM) |
|----------|----------------|----------------|----------------|----------------------------------------------|
| MCC950 | Direct NLRP3 ATP pocket | Clinical (Phase 2a) | Indirect | Cell-free 7.5 nM (Coll 2015); not retrievable in ChEMBL by synonyms (2026-04-23) |
| Oridonin | Covalent Cys279 | Preclinical; **curated human THP-1 IC50 = 5.18 μM** in ChEMBL v34 (*Eur J Med Chem* 2023) | No (no gout model) | Cellular IC50 5.18 μM in human cells; 0.5–2 μM in cell-free/mouse kinetic assays |
| Quercetin | ASC / upstream; **zero curated direct human NLRP3 in ChEMBL**; quercetin's most potent ChEMBL activity is **5-LOX (IC50 = 300 nM, *J Med Chem* 1991)** → LTB4 → neutrophil chemotaxis | Animal model (MSU) | Yes | Benchmark functional (~11 μM); 36× more potent on 5-LOX |
| **Beta-caryophyllene** | CB2/TLR4/NLRP3/NF-κB | **Animal model (MSU gout)**; **zero curated direct human NLRP3 bioactivities in ChEMBL** (functional/downstream markers only) | **Yes (functional)** | Unknown — no direct NLRP3 IC50; CB2 Ki 155 nM |
| CBD | P2X7/NF-κB (upstream, indirect) | In vitro (human monocytes) | No | Active 0.1–10 μM; no formal IC50 |
| CBG | NF-κB/MAPK (indirect) | Animal model (CIA arthritis) | No | Unknown |
| THCV | P2X7/NF-κB | In vitro | No | Unknown |
| CBC | PANX1/P2X7 | In vitro | No | Unknown |
| Myrcene | COX/PG, CB2 (no NLRP3 assay) | Animal model (adjuvant arthritis) | No | Not applicable |

### Translation priorities

**Beta-caryophyllene:** Direct MSU-model evidence makes it a leading test candidate, but the rat exposure is far above common supplement exposure. Human-cell potency and pharmacokinetics should precede combination claims.

**CBG:** Colitis and CIA data support gut and inflammation hypotheses, but not gout. Regulatory, sourcing, and exposure constraints remain.

**CBD:** Functional NLRP3 data exists, but the upstream P2X7 mechanism overlaps with BHB and poor luminal pharmacokinetics weaken the GI hypothesis. The quercetin interaction is a pharmacokinetic uncertainty. An MSU-model and exposure comparison is needed.

**THCV:** High CB2 affinity is interesting, but regulatory complexity, psychoactivity at high dose, and zero gout data dominate translation.

**Myrcene:** Arthritis-model analgesia supports a pain hypothesis, not an NLRP3 or gout claim. Route-specific MSU testing is required.

**CBC and alpha-pinene:** No gout data; mechanisms overlap with better-characterized candidates. **Limonene** has direct rat MSU-model data but still needs human-cell potency and exposure translation.

---

## 7. Falsification experiments

1. **Beta-caryophyllene dose-response in an MSU macrophage assay:** A human-cell dose-response with NLRP3, caspase-1, and IL-1β readouts would test whether the rat finding survives at achievable exposure. (source: nlrp3-inhibitor-screen.md)

2. **THCV vs. beta-caryophyllene head-to-head:** Test whether higher CB2 affinity translates into better NLRP3 suppression in MSU-stimulated macrophages.

3. **CBG in an MSU crystal model:** Determine whether the CIA and colitis signals translate to gout-relevant inflammation.

4. **Quercetin + CBD pharmacokinetics:** Measure whether quercetin changes CBD exposure before making an efficacy or dose-sparing claim.

5. **Beta-caryophyllene + oridonin in an MSU model:** Test additivity and safety directly rather than inferring them from non-overlapping mechanisms.

---

## Related Pages

- [NLRP3 Inflammasome](nlrp3-inflammasome.md)
- [NLRP3 Inhibitor Screen](nlrp3-inhibitor-screen.md) — comparative evidence screen
- [NLRP3 Exploit Map](nlrp3-exploit-map.md) — chokepoint framework
- [Supplements Stack](supplements-stack.md) — cross-compound safety and interaction context
- [Digestive Enzymes & EPI](digestive-enzymes.md)
- [Oridonin](oridonin.md) — benchmark covalent NLRP3 inhibitor
- [BHB / Ketones](bhb-ketones.md) — K+ efflux overlap with P2X7 pathway
- [KPV Tripeptide](kpv-peptide.md) — NF-κB/CP1 comparison point
