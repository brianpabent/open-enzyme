---
title: "Medicinal Mushroom Extract Characterization SOPs"
date: 2026-05-06
tags:
  - medicinal-mushroom-complement
  - phase-7
  - sop
  - extract-characterization
  - reproducibility
related:
  - medicinal-mushroom-complement-track.md
  - medicinal-mushroom-compound-mapping-computational.md
  - hypotheses/H06-medicinal-mushroom-complement-track.md
  - validation-experiments.md
sources:
  - "comp-014 Phase 7-2 cultivation × yield meta-analysis (`etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md`) — handoff items for SOP work"
  - "comp-014 Phase 7-1a/b/c strain selection lit scans"
  - "Phase 7 scope page `medicinal-mushroom-complement-track.md` §6 follow-up #3"
status: draft
---

# Medicinal Mushroom Extract Characterization SOPs

Draft methods for identity, extraction, chemical characterization, and functional verification. The reproducibility target from [H06](./hypotheses/H06-medicinal-mushroom-complement-track.md) is **±15% inter-operator variation** for load-bearing chemical measurements. Methods that still require primary-source or bench validation are labeled accordingly.

## SOPs

### SOP-1 — *Ganoderma lingzhi* GLPP Polysaccharide-Peptide Fractionation (load-bearing)

**Status:** Stub — gated on Phase 5b CNKI dive (Lin Zhanxi 林占熺 Juncao SOP + Lin Zhibin 林志彬 GLPP fractionation primary literature).

**Source material:** mycelium from ITS-verified *G. lingzhi* (Mycelia.bvba M9724 is the only commercially-verified ITS-authenticated strain per Phase 7-1a; Cao 2012 *Ganoderma*-specific primers G-ITS-F1/G-ITS-R2 at academic core facility, ~$20-40/sample, mandatory upstream gate).

**Planned method (extrapolated from English-language pharmacology papers — needs CNKI-sourced upstream protocol verification):**
1. Hot water extraction of dried mycelium (or freeze-dried fruiting body), 90°C, 2 hr, water:biomass = 10:1
2. Centrifugation + concentration of supernatant under vacuum
3. Ethanol precipitation (4 vol EtOH, 4°C overnight) → polysaccharide-peptide fraction
4. DEAE-Sepharose anion-exchange chromatography → fraction by charge profile
5. Sephacryl S-500 size-exclusion chromatography → MW-based separation
6. SEC-MALS verification of MW (target: determine which Lin-lab fraction the HUA mechanism load-bears on — 520 kDa is the bulk crude prep per sister paper PMC11351902; 31–42 kDa are post-DEAE sub-fractions per PMID 37852403 + 29541200; Lin 2022 HUA paper itself does not specify which fraction. Resolved 2026-05-06 grep-verify gate — see [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) for full citation chain)
7. Amino acid analysis (peptide composition)
8. Glycan linkage NMR fingerprint

**Phase 5b prerequisite:** without the Lin Zhanxi Juncao cultivation SOP from CNKI, the upstream substrate is not Western-reproducible. SOP-1 cannot be drafted at usable detail before that dive lands. Phase 7-1a strain scan documents the specific search terms: `菌草 灵芝 栽培` (CNKI), `林占熺 灵芝` (CNKI author search).

**Reproducibility target (per H06 Dimension 2):** ±15% inter-operator on MW + peptide:polysaccharide ratio + glycan composition.

### SOP-2 — *Cordyceps militaris* Cordycepin + Pentostatin HPLC Quantification

**Source material:** *C. militaris* fruiting body or mycelium from cultivated source (top-yield strain GYS60 per Phase 7-1b, or commercial cultivation kit for home-cultivation track).

**Phase 5b source-read anchor (2026-05-20):** Xiong 2024 *Biotechnology Bulletin* reports a whole *C. militaris* water extract active in potassium-oxonate + yeast-paste hyperuricemia rats; the visible publisher-page composition includes 35.86% polysaccharides, 27.05% protein, 0.21% phenolics, and 0.83% cordycepin. SOP-2 should therefore quantify cordycepin without collapsing the biological result into cordycepin alone; total polysaccharide/protein and, where feasible, pentostatin remain part of the batch-release fingerprint.

**Planned method (Wang 2014 with Xia 2017 cluster diagnostic ratio):**
1. Aqueous extraction of dried biomass, 80°C, 1 hr
2. C18 SPE cleanup
3. RP-HPLC, C18 column, water-methanol gradient
4. UV detection at 260 nm
5. Co-quantify: cordycepin (3'-deoxyadenosine), adenosine (precursor + ADA-deamination context), **pentostatin** (the natural ADA-inhibitor co-product per Xia 2017 PMID 29056419)
6. Pentostatin:cordycepin ratio is a diagnostic for whether the cordycepin BGC is fully expressed — this is the load-bearing readout for whole-fermentate-vs-purified cordycepin clinical positioning (per Phase 7-4 wet-lab gate)
7. Reference standard: cordycepin ≥98% HPLC purity (Sigma C9881 or equivalent); pentostatin reference standard is regulated (FDA-approved drug, restricted access — sourcing requires research-use license)

**Reproducibility target:** ±15% inter-operator on cordycepin mg/g; ±20% on pentostatin:cordycepin ratio (lower-abundance target).

### SOP-3 — *Pleurotus citrinopileatus* Ergothioneine HILIC-HPLC Quantification

**Source material:** dried fruiting body of *P. citrinopileatus* (golden oyster — highest fungal EGT producer at 7.0 mg/g DW per Phase 7-1c). Pasteurized-straw bag cultivation per Phase 7-2, freeze-dry to powder.

**Planned method (Cohen 2014 with HILIC modification for polar zwitterion):**
1. UA-DES (urea-based deep eutectic solvent) or aqueous methanol extraction
2. HILIC chromatography (suitable for polar zwitterionic EGT — reverse-phase fails for this analyte)
3. UV detection at 254 nm (or LC-MS for sensitivity)
4. Stable-isotope-labeled internal standard (²H₉-ergothioneine) for absolute quantification
5. Calibration: 0.1-10 mg/g range covers dietary-relevant content

**Reproducibility target:** ±15% inter-operator; consistent with the 7.0 mg/g DW Singapore RCT formulation reference (PMID 40552321 per Phase 7-1c).

### SOP-4 — Functional Verification Readouts

For each compound, a downstream functional readout that confirms bioactivity beyond chemical identification:

- **GLPP — ADA inhibition assay:** purified GLPP fraction + recombinant human ADA + adenosine substrate → measure 3'-deoxyinosine production decrease via HPLC. Target: dose-dependent inhibition with IC50 measurable.
- **Cordycepin — URAT1 expression assay:** HEK293 cells stably expressing human SLC22A12 (URAT1) + qPCR for URAT1 mRNA after 24h cordycepin treatment. Target: dose-dependent URAT1 mRNA reduction (matches in vivo finding from PMID 29422889).
- **Ergothioneine — Nrf2-ARE reporter assay:** HepG2 cells with stable ARE-luciferase reporter + EGT treatment → luciferase induction. Target: dose-dependent activation matching dietary-mushroom-derived EGT plasma range (~5-25 µM).

**Reproducibility target:** consistent dose-response shape across operators; absolute potency may vary 2× operator-to-operator on cell-based assays (typical for biological readouts).

### SOP-6 — Tiered methodology framework

The SOPs above (SOP-1 GLPP, SOP-2 cordycepin, SOP-3 EGT) are written at **Tier 3 (bench, publication-grade)** rigor. The same four-tier quantification ladder (kitchen → smartphone → bench → outsourced) that operationalizes the koji track also operationalizes the mushroom track, giving any open-source contributor a rigor-graded path from "I made a tea, did anything happen?" up to "this is a quantified extract suitable for synergy-experiment use."

The [quantification ladder](./quantification-ladder.md) defines the shared four tiers. This SOP supplies mushroom-specific assays and calibration anchors; [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md) supplies the koji-enzyme methods. First-batch values do not yet exist. GLPP requires Tier 3 SEC-MALS, and the proposed cordycepin Tier 2 diazo method remains speculative pending primary-literature and bench validation.

| Compound | Tier 1 (kitchen, ~$0) | Tier 2 (smartphone colorimetry, ~$50) | Tier 3 (bench HPLC, ~$2K) | Tier 4 (outsourced regulatory) |
|---|---|---|---|---|
| **Cordycepin** | Visual + dosing-by-known-extract-ratio (calibrated against Tier 3 batch); not analytical, just consistency | **Speculative — needs literature verification.** Diazo-coupling chemistry typically targets phenolic/amine groups; cordycepin is a 3'-deoxyadenosine analog without those motifs. Do not use this method until primary literature or bench validation establishes the needed sensitivity. Alternative: UV-vis at 260 nm (purine absorption) with known extract-ratio backing. **The validation experiment at [`validation-experiments.md` §1.28](./validation-experiments.md) (~$200, 2 weeks) compares diazo coupling with a UV 260 nm fallback and a Tier 3 HPLC-UV anchor, including an explicit adenosine cross-reactivity check.** | **SOP-2** above (HPLC, calibrated cordycepin standard from Sigma C3394) | Outsourced GMP-grade HPLC if regulatory submission ever needed |
| **Ergothioneine** | Visual + dosing-by-known-extract-ratio | **Ellman's reagent (DTNB) thiol detection**, smartphone colorimetry. Well-established chemistry (DTNB → 412 nm yellow on free thiol); EGT's free thiol is the substrate. Pharmacy-accessible reagent. Calibrate against a Tier 3 EGT-quantified batch to convert absorbance → mg/g. | **SOP-3** above (HILIC-HPLC with stable-isotope internal standard) | Outsourced GMP-grade HILIC-HPLC if regulatory ever needed |
| **GLPP** | Visual + extract weight + standardized decoction yield (mass-balance check, not compound-specific) | **Phenol-sulfuric acid total polysaccharide assay** (well-established colorimetric method, ~490 nm). **Caveat: measures total polysaccharide, not GLPP specifically.** Co-extracted *Ganoderma* polysaccharides + any residual decoction polysaccharides will be counted. Useful as a batch-to-batch consistency check ("this batch is in the same polysaccharide ballpark as the calibrated reference"), NOT as a GLPP-specific quantification. SOP-1's SEC-MALS at Tier 3 is non-negotiable for the protein:polysaccharide ratio per H06 Dimension 2 reproducibility discipline. | **SOP-1** above (SEC-MALS for MW + protein:polysaccharide ratio, with phenol-sulfuric and Bradford / Lowry as orthogonal anchors) | Outsourced GMP-grade SEC-MALS if regulatory ever needed |

**Operational pattern (the calibrate-once-track-batches workflow):**

1. **Initial Tier 3 calibration** — quantify a reference batch by SOP-1/2/3 above. Anchor numbers: mg/g extract for each target compound; document extract source, batch ID, lot, harvest details.
2. **Batch tracking at Tier 2** — for each new batch of extract from the same protocol, run the Tier 2 colorimetric assay against the reference batch as the standard curve anchor. If batch reads within ±20% of reference, accept. If outside, escalate to Tier 3 re-quantification.
3. **Field-grade Tier 1** — for end-user / kitchen-grade reproducibility, dosing follows the Tier 3-calibrated extract-ratio (e.g., "1 g of this batch ≈ 8 mg cordycepin per the SOP-2 quantification done on this lot"). Tier 1 is consumption-side, not characterization-side.
4. **Tier 4 outsourced** — only invoked if regulatory submission requires it. Adds GLP/GMP overhead but uses the same analytical chemistry as Tier 3.

**Why this matters operationally:** without the tiered framework, every batch would need full Tier 3 HPLC (cost-prohibitive at scale and impossible for distributed open-source contributors without HPLC access). With it, Tier 3 is invoked once per protocol revision; Tier 2 handles batch consistency cheaply; Tier 1 keeps end-user dosing tied to verified content. Same discipline that lets the koji track work as a home-fermentation project rather than a CRO-only project.

### Substrate-accumulated vs biosynthesized compounds

Not all compounds detected in a mushroom extract are produced by the fungus. **Substrate-accumulated compounds** pass through from the cultivation substrate (e.g., plant flavonoids from oak sawdust) and concentrate in mycelium without being biosynthesized by fungal metabolism. **Biosynthesized compounds** are produced by the fungal genome's secondary-metabolite biosynthetic gene clusters (BGCs). The two have fundamentally different batch-variability profiles:

| Compound | Origin | Dominant batch-variance source |
|---|---|---|
| **Cordycepin** (*C. militaris*) | Biosynthesized (cns1+cns2 BGC) | Strain genetics + fermentation conditions |
| **Ergothioneine** (*Pleurotus* / koji) | Biosynthesized (egtBCD pathway) | Strain genetics + substrate sulfur availability |
| **GLPP** (*G. lucidum*) | Biosynthesized (mycelium-specific polysaccharide-peptide) | Strain genetics + cultivation stage |
| **Kojic acid** (*A. oryzae*) | Biosynthesized | Strain genetics + carbon source |
| **Quercetin, genistein, daidzein, morin** (in mushroom extracts) | **Substrate-accumulated** (plant flavonoids passed through) | **Substrate lot + source** (oak sawdust species, geographic origin) |
| **Various polyphenols** (in mushroom extracts grown on hardwood) | Often substrate-accumulated | Substrate lot + source |

**QC implication:** for substrate-accumulated compounds, **substrate lot variation — not strain genetics — dominates batch-to-batch variability.** The Tier 2 colorimetric assay will detect a shifted quercetin batch but cannot distinguish "strain drift" from "substrate lot change" as the root cause. For H06 falsification-card Dimension 2 (characterization protocol robustness, ±15% inter-operator), substrate-accumulated origin must be a documented variable, not an invisible confound.

**Required documentation fields (cultivation data sheet):**
- **Substrate species / source** (e.g., oak species, sawdust grade, lot number, geographic origin, supplier)
- **Substrate lot identifier** (vendor lot, harvest date, treatment history)
- **Substrate composition characterization** (if available — lignin content, ash content, mineral profile, any vendor analytical certificate)
- **Substrate-accumulated vs biosynthesized origin tag** (per the table above; applies on a per-compound basis)

For compounds tagged "substrate-accumulated," the Tier 2 batch QC reading must be paired with substrate-lot documentation to be interpretable. A Tier 2 reading showing 20% drop in quercetin content is uninformative without knowing whether the substrate lot also changed.

**See also:** [Culture configuration](./etc/open-source-platform.md#culture-configuration) treats substrate and medium composition as part of a reproducible biological artifact. The documentation discipline above is the prerequisite QC anchor for any substrate-engineering experiment.

**Cross-reference to [Sourcing and delivery](./medicinal-mushroom-complement-track.md#sourcing-and-delivery):** product form and biomass do not establish target-compound exposure. Downstream reasoning requires target-specific chemical characterization of the exact batch.

### SOP-7 — Substrate Engineering Protocol Matrix

**Validation state:** Draft and primary-literature-anchored. Tier 3 HPLC validation is required for each candidate species and reagent pair before quantitative use.

This matrix is an idea registry, not a transfer table. Each result belongs to the reported strain, medium, culture format, timing, and assay. A result in one fungus can justify a matched experiment in another; it cannot supply an expected direction or magnitude there. Cultivation studies below are **In Vitro** evidence for the named configuration. Cross-species, cross-strain, or cross-format application remains **Mechanistic Extrapolation** until tested.

#### Target-compound leads

| Target | Exact source configuration | Observed in the source | Missing measurement or transfer limit | Primary source |
|---|---|---|---|---|
| Cordycepin | *C. militaris* CM01; solid PDA; 12 g/L L-alanine; 7 d dark plus 3 d light | 3.03 mg/g dry weight, approximately 3× the no-alanine control | Pentostatin not measured; no liquid- or grain-culture inference | [Yu 2024, PMC11698586](https://pmc.ncbi.nlm.nih.gov/articles/PMC11698586/) |
| Cordycepin | *C. militaris* GDMCC5.270; submerged medium with 10 g/L glucose, 3.5 g/L peptone, and 1.5 g/L corn-steep-liquor hydrolysate; 8 d | 343.03 ± 15.94 mg/L versus 70.97 ± 5.70 mg/L without hydrolysate, 4.83× | Pentostatin not measured; response varied among five strains | [Chang 2024, PMC10931215](https://pmc.ncbi.nlm.nih.gov/articles/PMC10931215/) |
| Cordycepin | Unaccessioned commercial *C. militaris* strain; solid *Allomyrina dichotoma* versus *Bombyx mori* pupae | 89.5 mg/g dry weight on *A. dichotoma*, 34× the *B. mori* condition | Substrates differ in many components; pentostatin not measured | [Turk 2022, PMC9627333](https://pmc.ncbi.nlm.nih.gov/articles/PMC9627333/) |
| Cordycepin | Same Turk strain on *A. dichotoma* with versus without added oleic acid | Cordycepin content increased 51.4%; *cns1* and *cns2* transcripts increased about 3× and 1.8× | Supplement dose is not stated in the article text; pentostatin not measured | [Turk 2022, PMC9627333](https://pmc.ncbi.nlm.nih.gov/articles/PMC9627333/) |
| Total ganoderic-acid assay | *G. lucidum* CGMCC5.0026; submerged culture; 1.5% microcrystalline cellulose added at 72 h | 21.2 versus 11.4 mg/100 mL, reported as an 85.96% increase | Individual ganoderic and lucidenic acids not resolved | [Hu 2017, PMC5395960](https://pmc.ncbi.nlm.nih.gov/articles/PMC5395960/) |
| Total ganoderic-acid assay | Same strain and format; 0.5% D-galactose added at 72 h | 20.36 versus 12.42 mg/100 mL, reported as a 63.9% increase | Individual compounds not resolved | [Hu 2017, PMC5395960](https://pmc.ncbi.nlm.nih.gov/articles/PMC5395960/) |
| Triterpenoid profile | Five commercial *G. lucidum* fruiting bodies per method; wood-log versus substitute cultivation; exact strain unreported | Wood-log samples had about 1.2× total triterpenoid peak area and 2.19× combined lucidenic acids. Substitute samples had 13.5× ganosporelactone B. Ganoderic-acid A/alpha favored substitute cultivation; E/O favored wood-log cultivation. | Not a controlled within-strain substrate swap; identities were putative untargeted-MS assignments | [Luo 2024, PMC10879320](https://pmc.ncbi.nlm.nih.gov/articles/PMC10879320/) |
| Ergothioneine | Nine mushroom species; submerged fungal growth medium; 2 mM methionine; 10 d | Significant EGT increases in six of nine tested species | Species-specific effects differed; the paper does not support a universal fold change | [Lee 2009, PMC3749454](https://pmc.ncbi.nlm.nih.gov/articles/PMC3749454/) |
| Ergothioneine | *Ganoderma neo-japonicum* mycelial culture; 4 mM methionine plus 1 g/L yeast extract | Approximately 1.7 versus 0.7 mg/L, 2.4×; mycelial growth was inhibited | Not evidence for *Pleurotus*, koji, or solid culture | [Lee 2009, PMID 18688580](https://pubmed.ncbi.nlm.nih.gov/18688580/) |
| Ergothioneine | Wild-type *A. oryzae* RIB40; solid DPY; 5 d; methionine titration | 0.1% methionine produced about 2× the unsupplemented EGT level; 0.8% produced 5.12 mg/g dry weight, while growth declined as methionine concentration increased | DPY is not rice koji. The reported 20.03 mg/g and 8× result also required an engineered strain and a different carbon-source/precursor configuration. | [Wang 2025, PMC12152031](https://pmc.ncbi.nlm.nih.gov/articles/PMC12152031/) |
| Betulinic acid | *I. obliquus* CFCC 83414; submerged culture; 1.0 g/L oleic acid added on day 6; measured day 13 | Dry-mycelium BA increased 223.1% and broth BA 202.0% (3.23× and 3.02× control) | Betulin and other triterpenoid ratios not reported for this comparison | [Lou 2021, PMC8066064](https://pmc.ncbi.nlm.nih.gov/articles/PMC8066064/) |
| Betulinic acid | Same strain; 45 mg/L disrupted *A. niger* elicitor | Positive candidate, but the article's abstract and results assign incompatible magnitudes to biomass and intracellular BA | Re-extract figure-level values before using a quantitative expectation | [Lou 2021, PMC8066064](https://pmc.ncbi.nlm.nih.gov/articles/PMC8066064/) |
| Betulinic acid | Same strain; 1.0 g/L oleic acid plus 45 mg/L elicitor added on day 7 | Intracellular BA reached 22.2× control; total BA increased 129.7% (2.30×) | The 22.2× intracellular result is not a 22.2× total-yield result | [Lou 2021, PMC8066064](https://pmc.ncbi.nlm.nih.gov/articles/PMC8066064/) |
| Betulinic acid | Natural *I. obliquus* conks from different isolates/sites on *Alnus incana* versus *Betula pendula* | 474–635 versus 20–132 µg/g dry weight; inotodiol ranges were similar, while birch conks contained more polyphenols, flavonols, and glucans | **Mechanistic Extrapolation:** host, isolate, and site are confounded; this is not a within-strain host intervention | [Drenkhan 2022, PMC9496626](https://pmc.ncbi.nlm.nih.gov/articles/PMC9496626/) |
| Erinacine C and pathway profile | One barcoded private-library *H. erinaceus* culture; submerged dextrose/oatmeal complex medium versus barley-malt minimal medium; 21 d | Erinacine C was about two orders of magnitude higher in complex medium; relative erinacine Q peak area was higher in minimal medium; A and P signals did not differ significantly; tested *eri* transcripts did not differ significantly | Q, A, and P lacked analytical standards, so a quantitative C:Q ratio was not established | [Doar 2025, PMC11969743](https://pmc.ncbi.nlm.nih.gov/articles/PMC11969743/) |

#### Production-only leads

These rows can improve cultivation or supply, but they do not establish more of a gout-relevant compound.

| Response | Exact source configuration | Observed in the source | Limit | Primary source |
|---|---|---|---|---|
| Fruiting-body yield | Unaccessioned *P. ostreatus* strain; sawdust/cottonseed-hull/wheat-bran substrate; 0.04% uridine | 362.6 g total yield, 35.3% above control; biological efficiency 73.77%, 19.77% above control | Target secondary metabolites were not profiled | [Tang 2025, PMC12299871](https://pmc.ncbi.nlm.nih.gov/articles/PMC12299871/) |
| Faster wood-free production | *H. erinaceus* 20190111; 16.3% rice straw, 59.7% corn cob, 20% wheat bran plus minor components | First crop arrived 7–9 d sooner. Biological efficiency was 89.14% versus 92.49% for the wood-chip control; fresh yield was also slightly lower. | A resource-substitution and cycle-time result, not an erinacine-yield result | [Lu 2024, PMC11671258](https://pmc.ncbi.nlm.nih.gov/articles/PMC11671258/) |

**Operational discipline (per SOP-6 four-tier framework):**

1. **Candidate registration** — preserve the exact source configuration and state what was not measured.
2. **Tier 3 analytical replication** — reproduce one matched control/intervention pair and quantify the target, relevant sibling compounds, and growth or biomass.
3. **Tier 2 batch QC development** — only after Tier 3 establishes that a lower-cost readout tracks the target in that exact configuration.
4. **Controlled translation** — define safety, contamination, exposure, and regulatory gates for any application beyond research cultivation.

**Calibration-per-revision discipline:** a replicated Tier 3 comparison estimates the effect for the exact configuration. A validated Tier 2 readout may then track later batches only while strain, formulation, culture conditions, extraction, and assay remain within that calibration's scope.

**Transfer rule:** strain, medium or substrate, supplement, culture format, timing, harvest, and assay form one configuration. Until a transferred configuration is tested, neither the source-study direction nor its magnitude is assumed. See [Culture configuration](./etc/open-source-platform.md#culture-configuration).

### SOP-5 — Strain Banking + ITS Authentication

**Cross-reference:** Phase 7-1a outlined the ITS-PCR authentication protocol (Cao 2012 *Ganoderma*-specific primers); applies to all medicinal mushroom strains used for Open Enzyme protocols.

**Planned method:**
1. ITS region amplification (ITS1-5.8S-ITS2)
2. Sanger sequencing
3. BLAST against NCBI nt database with species-level confidence threshold (≥98% identity for genus, ≥99.5% for species)
4. Deposit verified strain in -80°C glycerol stock with documented provenance
5. Re-verify ITS every 6 months or after 5 serial passages (whichever first)

**Reproducibility target:** binary — pass/fail on species ID; provenance fully documented per strain.

## Cross-references

- [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) — the scope page these SOPs operationalize
- [`hypotheses/H06-medicinal-mushroom-complement-track.md`](./hypotheses/H06-medicinal-mushroom-complement-track.md) — H06 Dimension 2 (characterization protocol robustness) is the falsification mirror for these SOPs
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — comp-014, parent computational analysis
- [`validation-experiments.md`](./validation-experiments.md) §2.6 — GLPP+cordycepin synergy wet-lab gate (uses these SOPs as input materials)
- [`etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md) — Phase 7-2 source for cultivation upstream parameters
- [`etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7a-ganoderma-strain-scan.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7a-ganoderma-strain-scan.md), [`phase-7b-cordyceps-strain-scan.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7b-cordyceps-strain-scan.md), [`phase-7c-pleurotus-strain-scan.md`](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7c-pleurotus-strain-scan.md) — strain selection inputs

## Validation priorities

1. Resolve SOP-1 upstream Juncao cultivation and GLPP fraction identity from primary Chinese sources.
2. Validate SOP-3 EGT as the lowest-complexity analytical method.
3. Source a lawful research-use pentostatin standard before attempting SOP-2 co-quantification.
4. Require two independent operators to achieve the H06 ±15% reproducibility target before treating a method as validated.
