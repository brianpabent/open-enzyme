---
title: Uricase (Urate Oxidase)
aliases: 
  - urate oxidase
  - uox gene
  - rasburicase
related:
  - nlrp3-inflammasome
  - gut-lumen-sink
  - abcg2-modulators
  - androgen-urate-axis
  - saccharomyces-cerevisiae
  - aspergillus-oryzae
  - blood-barrier
sources:
  - gout-deep-dive.md
  - enzyme-deficit-deep-dive.md
  - engineered-yeast-uricase-proposal.md
  - engineered-koji-protocol.md
  - blood-barrier-exploits.md
  - etc/open-enzyme-vision.md
---

# Uricase (Urate Oxidase)

## Overview

Uricase (EC 1.7.3.3), also called urate oxidase, is the enzyme that catalyzes the conversion of uric acid into allantoin—a highly soluble, easily excreted compound. It is present in nearly all mammals except humans, great apes, and some other primates. For humans, the functional uricase gene (UOX) is a non-functional pseudogene, inactivated by two nonsense mutations at codons 33 and 187, plus an aberrant splice site. (Source: gout-deep-dive.md)

## Evolutionary Loss

The functional uricase gene (UOX) was inactivated ~15–20 million years ago and is now a pseudogene (nonsense mutations at codons 33 and 187 plus an aberrant splice site) — a loss that appears to have been positively selected. Three non-exclusive selective rationales (fructose-fat storage, antioxidant/neuroprotection, blood-pressure maintenance) are reviewed in depth, with the Gaucher-lab 2025 CRISPR confirmation of the fructose-lipogenesis link, in [gout-deep-dive.md §"Evolutionary Loss"](./gout-deep-dive.md) and [gout-pathophysiology.md](./gout-pathophysiology.md). The therapeutic upshot: because urate retains beneficial antioxidant roles, the optimal target is "below crystallization threshold," not "as low as possible."

## The Missing Enzyme Problem

The absence of a functional uricase is the root cause of gout: humans maintain serum uric acid at 3.5–7.2 mg/dL (vs. <2 mg/dL in uricase-positive mammals), and above the ~6.8 mg/dL saturation point monosodium urate (MSU) crystals deposit in joints and tissues. Full pathophysiology — purine catabolism, transporter network, the under-excretor phenotype, NLRP3 → IL-1β flare cascade — is in [gout-pathophysiology.md](./gout-pathophysiology.md) and [gout-deep-dive.md](./gout-deep-dive.md). (Source: engineered-yeast-uricase-proposal.md, gout-deep-dive.md)

## Molecular Characteristics

The *Aspergillus flavus* uricase gene (uaZ), the most well-characterized and therapeutically relevant source, encodes a protein with these properties:

- **Protein size:** 301 amino acids per monomer; ~34 kDa per subunit
- **Native quaternary structure:** Homotetramer, ~135 kDa total
- **Cofactors:** None required (no metal, no heme)
- **Reaction:** Uric acid + O₂ + H₂O → 5-hydroxyisourate → allantoin + CO₂ + H₂O₂
- **Peroxisomal targeting:** Native protein has C-terminal PTS1 signal (SKL)
- **Crystal structure:** Solved at high resolution (PDB: 1R56, 3BJP, others); active site well-characterized

(Source: engineered-koji-protocol.md)

## FDA-Approved Uricase: Rasburicase

**Rasburicase** (brand names: Elitek/Fasturtec) is the only FDA-approved recombinant uricase, approved by the EMA in 2001 and the FDA in 2002. It is produced by expressing the *A. flavus* uricase gene in genetically modified *Saccharomyces cerevisiae*. The enzyme is used intravenously for tumor lysis syndrome in cancer patients. (Source: gout-deep-dive.md, engineered-yeast-uricase-proposal.md)

### Rasburicase Limitations

Approximately 60% of patients receiving repeated rasburicase doses develop anti-drug antibodies (ADAs) that neutralize the enzyme, limiting its use to short-course therapy and creating infusion reactions on reexposure. (Source: gout-deep-dive.md)

## Oral Uricase: ALLN-346

**ALLN-346** was an engineered oral uricase developed by Allena Pharmaceuticals. It is an engineered variant of *Candida utilis* uricase, modified using protein engineering to have 20-fold increased stability against pancreatic proteases (half-life of 85.3 min vs. 4.3 min for wild-type *C. utilis* enzyme in 80 ng/μL pancreatin) while maintaining specific activity. (Source: engineered-yeast-uricase-proposal.md)

### Program Status (2026-04-23)

**The ALLN-346 program is no longer active.** The Phase 2a CKD trial NCT04987294 — the pivotal study planned across 17 US sites — was **terminated September 2022 with only 19 patients enrolled** against a planned cohort of >200. The three earlier Phase 1/2 studies (NCT04236219 SAD, NCT05168683 enteric coating scintigraphy, NCT04987242 inpatient hyperuricemia) had completed by March 2022. Allena Pharmaceuticals has registered no further gout trials on ClinicalTrials.gov after September 2022. (Animal Model + Clinical Trial; source: gout-clinical-pipeline.md)

The mechanism (gut-lumen uricase exploiting ABCG2 secretion) remains scientifically sound; the *commercial* proof-of-concept for oral uricase in gout has not been delivered. Open Enzyme can no longer be framed as "a citizen-science version of a validated clinical program" — it is the citizen-science version of a promising mechanism that pharma did not carry to a pivotal readout. See [gout-clinical-pipeline.md](gout-clinical-pipeline.md) for the full competitive snapshot.

### Clinical Evidence (Historical)

**In vivo:** In urate oxidase-deficient knockout mice, oral ALLN-346 treatment over 7- and 19-day studies normalized urine uric acid excretion and significantly reduced hyperuricemia. (Source: engineered-yeast-uricase-proposal.md)

**Human Phase 2a (Study 201):** Statistically significant reductions in serum uric acid (sUA) were observed from days 5–7 in patients with gout and chronic kidney disease (CKD). (Source: engineered-yeast-uricase-proposal.md)

**Human Phase 2a (Study 202):** The broader cohort showed mean sUA reductions of only 0–5% from baseline on days 7 and 14—not statistically significant vs. placebo. The Phase 2a CKD trial (Study 201's successor at scale, NCT04987294) was then terminated September 2022. (Source: engineered-yeast-uricase-proposal.md, gout-clinical-pipeline.md)

## Active Clinical Uricase Competitors (2026 Snapshot)

Two systemic IV uricase programs are currently in clinical development, both pursuing the systemic-uricase + immunomodulator strategy that Krystexxa+MTX (Amgen) established:

- **PRX-115 (Protalix) — Phase 2 RELEASE trial NCT07280156** (Clinical Trial). Pegylated recombinant uricase ± methotrexate, IV, 24 weeks; N=150, started 2025-12-22, primary completion Dec 2027. Targets treatment-naive gout (not just refractory); excludes eGFR ≤ 40. (source: gout-clinical-pipeline.md)
- **SSS11 (Shenyang Sunshine) — Phase 1 NCT06629376** (Clinical Trial). Pegylated *Candida utilis* uricase, IV, N=60, single-center (Huashan Hospital, Shanghai). First clinical use of *C. utilis*-derived uricase. (source: gout-clinical-pipeline.md)

**All current clinical uricase programs are systemic IV.** No active program (clinical or pharmacological) targets the gut-lumen-uricase angle that Open Enzyme pursues. This positioning is uncompeted in any registered trial as of April 2026. (source: gout-clinical-pipeline.md)

## The Gut-Lumen Insight

Uricase does not require systemic absorption to be effective: ~1/3 of daily urate elimination is intestinal (via apical ABCG2), so lumen-resident uricase creates a "concentration sink" that pulls serum urate across the epithelium without barrier crossing. This is the platform's core delivery thesis — the full mechanism, the three independent validating systems (ALLN-346, PULSE probiotic, engineered *S. boulardii* at 365 μmol/h/OD), and the comp-019 genotype-stratification reframing (gut-lumen uricase is genotype-robust; WT/WT patients show the *largest* predicted ΔSUA; engineering constraint is GI-survival, not enzyme yield) are owned by [gut-lumen-sink.md](./gut-lumen-sink.md). See also [abcg2-modulators.md](./abcg2-modulators.md) for the regulatory landscape and [androgen-urate-axis.md](./androgen-urate-axis.md) for the sex-hormone mechanism. (Source: engineered-yeast-uricase-proposal.md, gut-lumen-sink.md)

## Expression Systems

Uricase has been successfully expressed heterologously in multiple GRAS organisms:

### Saccharomyces cerevisiae

The *A. flavus* uaZ gene has been successfully expressed in *S. cerevisiae*, accumulating intracellular uricase to levels exceeding 13% of total cellular protein using a hybrid GAL7/ADH2 promoter. The rasburicase pharmaceutical product is manufactured using this exact gene-host combination. (Source: engineered-yeast-uricase-proposal.md)

For oral delivery applications, constitutive promoters (pTEF1, pGPK1) are preferred over inducible ones, as you want the enzyme present during normal growth and fermentation without requiring external inducers. (Source: engineered-yeast-uricase-proposal.md)

### Aspergillus oryzae (Koji)

*A. oryzae* and *A. flavus* are extremely closely related (>99.5% genome similarity in coding regions). The *A. flavus* uricase gene should express well in *A. oryzae* without codon optimization due to nearly identical codon usage. Engineering koji to produce uricase alongside its native digestive enzymes creates a dual-purpose therapeutic organism. (Source: engineered-koji-protocol.md)

Using the **PamyB promoter** (α-amylase promoter, starch-inducible) maximizes expression when koji is grown on rice—the enzyme auto-activates on the exact substrate being used. (Source: engineered-koji-protocol.md)

### Saccharomyces boulardii

The 2025 ACS Synthetic Biology paper demonstrated systematic engineering of *S. boulardii* (a probiotic yeast variant of *S. cerevisiae*) for efficient uric acid degradation. This organism offers advantages over *S. cerevisiae*: GRAS status, established oral probiotic use, resistance to antibiotics, and eukaryotic protein folding machinery. (Source: engineered-yeast-uricase-proposal.md)

## Delivery Formats

### Beer and Fermented Beverages

Traditional beer using engineered yeast is problematic. Alcohol raises uric acid through three mechanisms: (1) ethanol metabolism accelerates ATP degradation and purine turnover, increasing uric acid production; (2) lactate produced during ethanol metabolism competes with uric acid for renal tubular secretion, reducing excretion; (3) beer contains high purine content (8–14 mg per 100 mL). You are fighting the delivery vehicle. (Source: engineered-yeast-uricase-proposal.md)

Non-alcoholic fermented beverages (kvass, tepache, kombucha-style with *S. cerevisiae*) remove the alcohol confound and are more therapeutically credible.

### Nutritional Yeast / Dried Yeast Powder

Enzyme stability after drying is critical. Conventional heat-based drying (50–60°C for pasteurization, then drum or spray drying) destroys uricase activity—the *A. flavus* enzyme loses significant activity above 40°C and nearly all activity at 40–45°C. 

Lyophilization (freeze-drying) preserves enzyme activity far better, and encapsulation in trehalose or other lyoprotectants is standard for enzyme stabilization. A lyophilized yeast powder, packaged in capsules, could retain uricase activity. (Source: engineered-yeast-uricase-proposal.md)

**Purine caveat — the dried-yeast biomass is itself very high purine.** Eating the yeast cells means eating their nucleic acids, and dried yeast is one of the highest-purine foods that exists (~1,800–3,000 mg/100 g; Kaneko 2014, USDA Purine Database 2025). At a therapeutic uricase dose (~10 g dried yeast/day), this adds ~180–300 mg dietary purine/day — 45–75% of Japan's 400 mg/day gout limit, from the medicine alone. The koji chassis is mostly low-purine rice (~15–35 mg/100 g) and carries ~15–120× less purine per therapeutic dose. The carried uricase may degrade much of the co-ingested purine in situ, so the *net* effect is unknown and worth a direct assay — but this is a structural argument for the koji chassis on the sustained oral-dosing path. Full quantified comparison: [[purine-load-koji-vs-yeast]].

### Live Probiotic

*S. boulardii* achieves steady-state concentrations in the human colon within 3 days of regular dosing and clears 2–5 days after discontinuation—it transits rather than colonizes. Daily dosing is therefore required to maintain gut levels. (Source: engineered-yeast-uricase-proposal.md)

The **PULSE system** demonstrated this approach: engineered *E. coli* Nissle 1917 with a uric-acid-responsive biosensor (HucR repressor) that dynamically regulates urate oxidase expression. When serum uric acid rises, bacteria automatically produce more uricase; when it normalizes, production decreases. (Source: engineered-yeast-uricase-proposal.md, etc/open-enzyme-vision.md)

### Koji on Rice / Fermented Food Format

Wild-type *A. oryzae* koji, grown on steamed rice for 36–48 hours at 30–32°C with >80% humidity, naturally produces amylases, proteases, and lipases at therapeutically relevant levels. Engineering to add uricase would create a dual-purpose food format consumed as shio koji (koji + salt + water, fermented 7–14 days, shelf-stable for months) or fresh koji rice (used immediately or processed into amazake). (Source: engineered-koji-protocol.md, etc/open-enzyme-vision.md)

## Dosing Considerations

### Therapeutic Need

A typical adult produces ~600–900 mg of uric acid per day. Approximately 200–300 mg is eliminated via the intestine. To reduce serum urate from ~9 mg/dL (common without therapy) to below 6 mg/dL (therapeutic target) requires eliminating roughly 200–400 mg of additional uric acid per day—the amount that would otherwise accumulate. (Source: engineered-yeast-uricase-proposal.md)

### Reference: Rasburicase (IV)

The approved dose is 0.15–0.2 mg/kg/day. For a 90 kg adult, this is ~13.5–18 mg of pure enzyme per day, administered intravenously. This dramatically effective—typically reduces serum urate to near-zero within 4 hours. But IV delivery puts enzyme directly into bloodstream with access to all circulating urate; oral delivery works through the gut lumen, a fundamentally different and less efficient route. (Source: engineered-yeast-uricase-proposal.md)

### Oral Dosing Estimates

ALLN-346 Phase 2a studies used oral doses that were orders of magnitude higher than IV rasburicase, reflecting the inefficiency of the gut-lumen route. Mouse studies used approximately 3–30 mg of engineered enzyme per day, scaled to body weight. (Source: engineered-yeast-uricase-proposal.md)

For engineered yeast expressing uricase: if accumulation reaches 13% of total cellular protein, and a yeast cell contains ~6 pg of total protein, then ~0.78 pg of uricase per cell. At 10⁸ cells/mL in dense culture, this yields ~78 μg uricase/mL, or 78 mg/L. To deliver 20–50 mg of active uricase per dose requires 250–640 mL of saturated culture—roughly a pint to a quart. Concentrated, dried, or capsule formats would reduce this significantly. (Source: engineered-yeast-uricase-proposal.md)

## Safety and Immune Response

### Immunogenicity

Rasburicase (IV uricase) induces anti-drug antibodies in ~60% of patients, limiting re-dosing. However, IV delivery presents the antigen to the systemic immune system. Oral delivery primarily encounters the mucosal immune system, which is inherently **tolerogenic**—designed for tolerance to dietary proteins. The oral tolerance literature from allergen immunotherapy supports the hypothesis that repeated oral exposure to uricase would induce tolerance rather than sensitization. (Source: engineered-yeast-uricase-proposal.md)

ALLN-346 Phase 1 trials showed no serious adverse events, no systemic absorption of enzyme, and no immune reactions at any dose level tested. (Source: engineered-koji-protocol.md)

### Hydrogen Peroxide Byproduct

Uricase produces H₂O₂ as a byproduct. In cells, catalase immediately degrades this. In the gut lumen, catalase from *A. oryzae* (which would be co-delivered with engineered koji) would neutralize H₂O₂. Additionally, the gut lumen has significant peroxidase activity from microbiome and epithelial cells. At expected therapeutic uricase activity levels, H₂O₂ production would be minimal and rapidly scavenged—not a safety concern. (Source: engineered-koji-protocol.md)

The peroxisomal co-localization of uricase + endogenous catalase in the whole-cell oral chassis is more than a safety reassurance — it's free formulation work that every alternative delivery route (IV, SC, intra-articular, rectal) has to re-solve through formulation engineering. See [`engineered-koji-protocol.md` §"The Hydrogen Peroxide Question — and why the chassis solves it for free"](./engineered-koji-protocol.md) and [`delivery-route-matrix.md` §"Chassis-as-formulation"](./delivery-route-matrix.md) for the route-by-route treatment. The **catalase capacity principle** (route-agnostic H₂O₂ safety design rule, [`delivery-route-matrix.md` §"Catalase capacity principle"](./delivery-route-matrix.md)) generalizes this: for any uricase delivery format, H₂O₂ safety is determined by total catalase capacity at the site of H₂O₂ generation, not by residue-level proximity. (source: delivery-route-matrix.md)

## Therapeutic Applications

### Gout Management

Uricase (oral, engineered, or probiotic) addresses the root cause of gout by degrading urate before crystallization, exploiting the ABCG2 intestinal secretion pathway — see [gut-lumen-sink.md](./gut-lumen-sink.md). (Source: gout-deep-dive.md, etc/open-enzyme-vision.md)

### Other Enzyme Deficiencies

The success of uricase as an oral therapeutic enzyme opens pathways for other missing or insufficient enzymes in humans, as part of the broader [[open-enzyme-vision|Open Enzyme platform]]. (Source: etc/open-enzyme-vision.md)

## Industry-Revealed Preference: *C. utilis* for Oral/Gut-Lumen Track

An important finding from the 2026-05-05 audit of the clinical pipeline: of the four recent non-rasburicase/non-Krystexxa uricase programs with publicly disclosed parent enzyme, **three of four chose *C. utilis*** (SSS11, ALLN-346, SEL-212) and the fourth (ACS Synth Bio *S. boulardii* 2025) picked *V. vulnificus*. **None chose *A. flavus* for any recent oral, IV-with-tolerance, or probiotic program.** (source: uricase-variant-selection.md)

This does not displace *A. flavus* for the *S. cerevisiae* intracellular track (where rasburicase precedent is decisive), but it elevates *C. utilis* to **co-primary alongside *A. flavus*** for the oral/gut-lumen track. Key drivers: (a) freedom-to-operate around the rasburicase IP estate, (b) publicly disclosed ALLN-346 protease-resistance mutations (US10815461B2: I180V, V190G, Y165F, E51K, Q244K, I132R, A87G), (c) GRAS food-yeast precedent. (In Vitro + Clinical Trial; source: uricase-variant-selection.md)

**Tang 2025 head-to-head directed evolution (PMID 39892538):** Parallel error-prone-PCR + high-throughput screening of *A. flavus* and *C. utilis* uricases yielded af-UA at **46.21 U/mg** (Thr231Ala) vs. cu-UA at **31.43 U/mg** (Val234Met). Wild-type *C. utilis* (~38 IU/mg) actually exceeds wild-type *A. flavus*, but **post-evolution *A. flavus* retains a ~50% activity advantage**. Industry preference for *C. utilis* is therefore not about specific activity — it is about IP, oral-tolerance profile, and the disclosed ProteinGPS mutations. (In Vitro; source: uricase-variant-selection.md)

**SEL-212 species attribution confirmed:** SEL-212 (pegadricase + ImmTOR) uses ***C. utilis* uricase** (pegylated), per Sands 2022 *Nat Commun* PMID 35022448. This is the Phase 3-validated systemic IV program that solved pegloticase's immunogenicity problem. (Clinical Trial; source: uricase-variant-selection.md)

## AI Analysis Findings (April 2026)

**Variant Comparison Completed:**
- *Aspergillus flavus* confirmed as primary candidate for *S. cerevisiae* intracellular track (FDA approval via rasburicase; proven S. cerevisiae expression; extensive stability engineering precedent; post-evolution activity advantage per Tang 2025)
- *Candida utilis* elevated to co-primary for oral/gut-lumen track (industry-revealed preference in 3-of-3 recent oral programs; publicly disclosed ALLN-346 mutations; GRAS food-yeast precedent)
- *Arthrobacter globiformis* ranked secondary (superior thermostability, neutral pH activity; requires novel expression system optimization)
- Four additional variants evaluated; see [uricase-variant-selection.md](./uricase-variant-selection.md) for detailed ranking

**GI Survival Profile:**
- Baseline survival: 15–25% of ingested enzyme reaches small intestine in active form
- Acid protection required (enteric coating or disulfide bond engineering) improves survival to 40–50%
- Active window: duodenum/jejunum (pH 5.5–7.5), 45–120 min transit
- See [[ai-analysis/02-gi-survival-prediction|02 — GI Survival Prediction]] for complete transit modeling

**Engineering Mutations Designed:**
- Three mutation tiers identified: SB-1 (stability baseline), BAL-1 (balanced engineering), OPT-1 (comprehensive optimization)
- Disulfide bond engineering validated for acid/thermal stability without activity loss
- See [[ai-analysis/03-protein-engineering-strategy|03 — Protein Engineering Strategy]] for mutation details and expression yields

## References

- Oda, M. et al. (2002). "Loss of Urate Oxidase Activity in Hominoids and its Evolutionary Implications." *Molecular Biology and Evolution*, 19(5), 640–653.
- Kratzer, J.T. et al. (2014). "Evolutionary history and metabolic insights of ancient mammalian uricases." *Proceedings of the National Academy of Sciences*, 111(10), 3763–3768.
- Gaucher et al. (2025). "CRISPR-based restoration of ancestral uricase in human liver cells." *Scientific Reports*.
