---
title: "Medicinal Mushroom Extract Characterization SOPs"
date: 2026-05-06
tags:
  - medicinal-mushroom-complement
  - sop
  - extract-characterization
  - reproducibility
related:
  - medicinal-mushroom-complement-track.md
  - medicinal-mushroom-compound-mapping-computational.md
  - validation-experiments.md
sources:
  - "Primary configurations cited inline in SOP-7"
  - "Xiong et al. 2024, DOI 10.13560/j.cnki.biotech.bull.1985.2024-0379 — whole C. militaris water extract in hyperuricemic rats"
  - "Xia et al. 2017, PMID 29056419 — cordycepin/pentostatin co-production"
status: draft
---

# Medicinal Mushroom Extract Characterization SOPs

Draft methods for identity, extraction, chemical characterization, and functional verification. No analytical tolerance or acceptance threshold has been established; each must be set from method qualification before result-bearing use.

## SOPs

### SOP-1 — *Ganoderma lingzhi* GLPP Polysaccharide-Peptide Fractionation (load-bearing)

**Status:** Stub — the exact upstream cultivation, extraction, and fractionation protocol still requires primary-source recovery and method qualification.

**Source material:** an authenticated *G. lingzhi* material with strain/accession, source, substrate, harvest state, and storage history recorded. No unique acceptable commercial strain has been established.

**Planned method (extrapolated from English-language pharmacology papers — needs CNKI-sourced upstream protocol verification):**
1. Hot water extraction of dried mycelium (or freeze-dried fruiting body), 90°C, 2 hr, water:biomass = 10:1
2. Centrifugation + concentration of supernatant under vacuum
3. Ethanol precipitation (4 vol EtOH, 4°C overnight) → polysaccharide-peptide fraction
4. DEAE-Sepharose anion-exchange chromatography → fraction by charge profile
5. Sephacryl S-500 size-exclusion chromatography → MW-based separation
6. SEC-MALS verification of molecular-weight distribution. The HUA-active GLPP fraction remains unresolved: related papers report materially different bulk and post-fractionation sizes, and those preparations are not interchangeable.
7. Amino acid analysis (peptide composition)
8. Glycan linkage NMR fingerprint

**Primary-source prerequisite:** recover and verify the exact cultivation, extraction, and fractionation methods for the material whose biological result is being tested. The historical search notes are query aids, not method authority.

**Acceptance criteria:** unset until the method's precision, recovery, specificity, and between-operator variance are measured.

### SOP-2 — *Cordyceps militaris* Cordycepin + Pentostatin HPLC Quantification

**Source material:** an authenticated *C. militaris* fruiting-body or mycelial material with strain/accession and cultivation configuration recorded. Historical yield ranks do not select the material.

[Xiong et al. 2024](https://doi.org/10.13560/j.cnki.biotech.bull.1985.2024-0379) reports a whole *C. militaris* water extract in potassium-oxonate + yeast-paste hyperuricemia rats. The publisher page reports that material as 35.86% polysaccharides, 27.05% protein, 0.21% phenolics, and 0.83% cordycepin. The biological result therefore cannot be assigned to cordycepin alone: SOP-2 should quantify cordycepin while retaining total polysaccharide/protein and, where feasible, pentostatin in the batch fingerprint (**Animal Model** for the whole-extract result).

**Planned method (Wang 2014 with Xia 2017 cluster diagnostic ratio):**
1. Aqueous extraction of dried biomass, 80°C, 1 hr
2. C18 SPE cleanup
3. RP-HPLC, C18 column, water-methanol gradient
4. UV detection at 260 nm
5. Co-quantify: cordycepin (3'-deoxyadenosine), adenosine (precursor + ADA-deamination context), **pentostatin** (the natural ADA-inhibitor co-product per Xia 2017 PMID 29056419)
6. Record the pentostatin:cordycepin ratio as batch-identity data. Co-production does not make the ratio a diagnostic of full-cluster expression, protection, exposure, efficacy, or clinical positioning without direct validation.
7. Reference standards: cordycepin ≥98% HPLC purity ([Sigma C3394](https://www.sigmaaldrich.com/US/en/product/sigma/c3394) or equivalent) and pentostatin ([Cayman 14878](https://www.caymanchem.com/product/14878/pentostatin) or equivalent). Source and handle both under applicable institutional research-use and chemical-safety requirements.

**Acceptance criteria:** unset until cordycepin and pentostatin recovery, specificity, calibration, detection limits, and inter-operator precision are measured.

### SOP-3 — *Pleurotus citrinopileatus* Ergothioneine HILIC-HPLC Quantification

**Source material:** authenticated dried *P. citrinopileatus* fruiting body. One reported material contained 7.0 mg/g dry weight; that exact configuration is a calibration lead, not a cross-species production rank.

**Planned method (Cohen 2014 with HILIC modification for polar zwitterion):**
1. UA-DES (urea-based deep eutectic solvent) or aqueous methanol extraction
2. HILIC chromatography (suitable for polar zwitterionic EGT — reverse-phase fails for this analyte)
3. UV detection at 254 nm (or LC-MS for sensitivity)
4. Stable-isotope-labeled internal standard (²H₉-ergothioneine) for absolute quantification
5. Calibration: 0.1-10 mg/g range covers dietary-relevant content

**Acceptance criteria:** unset until extraction recovery, matrix effects, calibration, detection limits, and inter-operator precision are measured against the exact material.

### SOP-4 — Functional Verification Readouts

For each compound, a downstream functional readout that confirms bioactivity beyond chemical identification:

- **GLPP — proposed ADA test:** qualify one exact fraction, then measure ADA-driven substrate/product conversion directly with interference controls. The ADA mechanism is a hypothesis, not an established property of generic GLPP.
- **Cordycepin — renal transport test:** use a polarized urate-transport assay with transporter attribution; keep URAT1 expression as a secondary readout rather than the functional gate.
- **Ergothioneine — gout-inflammation test:** choose a primary-source-grounded exposure range, then measure a prespecified MSU-relevant functional endpoint with Nrf2/redox readouts as mechanism probes.

**Acceptance criteria:** preregister after pilot estimates establish assay variance, viability bounds, and the smallest effect that would change the decision.

### SOP-6 — Tiered methodology framework

The SOPs above are unvalidated bench-method candidates. The [quantification ladder](./quantification-ladder.md) can organize method development, but a lower-cost readout becomes a batch-control method only after it is validated against a qualified analytical anchor for the exact material.

The [quantification ladder](./quantification-ladder.md) defines the shared four tiers. This SOP supplies mushroom-specific assays and calibration anchors; [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md) supplies the koji-enzyme methods. First-batch values do not yet exist. GLPP requires Tier 3 SEC-MALS, and the proposed cordycepin Tier 2 diazo method remains speculative pending primary-literature and bench validation.

| Material | Tier 1 observation | Tier 2 candidate screen | Tier 3 analytical anchor | Tier 4 qualified external method |
|---|---|---|---|---|
| **Cordycepin material** | Record mass, moisture, extraction yield, and appearance; no compound inference | Candidate UV/color method must first pass specificity, recovery, and cross-reactivity against the Tier 3 anchor | SOP-2 candidate HPLC/LC-MS method with reference standards | Qualified external chromatography when required |
| **Ergothioneine material** | Record mass, moisture, extraction yield, and appearance; no compound inference | Candidate thiol/color method must first show that matrix interferents do not dominate | SOP-3 candidate HILIC-LC/MS method with internal standard | Qualified external HILIC-LC/MS when required |
| **GLPP material** | Record mass and extraction yield; not GLPP-specific | Total-polysaccharide assays may track a batch only after correlation with the exact fraction is validated | SOP-1 candidate SEC-MALS plus composition methods | Qualified external fraction-characterization method when required |

**Operational pattern (the calibrate-once-track-batches workflow):**

1. **Initial Tier 3 calibration** — quantify a reference batch by SOP-1/2/3 above. Anchor numbers: mg/g extract for each target compound; document extract source, batch ID, lot, harvest details.
2. **Batch tracking at Tier 2** — use a lower-cost readout only after the validation study defines its acceptable agreement and scope.
3. **Tier 1 observation** — record process and mass-balance variables only; do not infer concentration, dose, or biological activity.
4. **Tier 4 outsourced** — only invoked if regulatory submission requires it. Adds GLP/GMP overhead but uses the same analytical chemistry as Tier 3.

**Operational boundary:** method-transfer cost matters, but it cannot be solved by declaring a low-cost proxy valid. Recalibrate whenever strain, substrate, culture, extraction, matrix, or assay leaves the validated scope.

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

**QC implication:** substrate lot and strain genetics are both candidate sources of batch variation. A lower-cost readout cannot attribute a shift to either cause; substrate and strain provenance must remain documented variables.

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

**Status:** Draft identity workflow. Primer choice and taxonomic acceptance criteria require primary-source and reference-database qualification for the selected species.

**Planned method:**
1. ITS region amplification (ITS1-5.8S-ITS2)
2. Sanger sequencing
3. Compare against curated reference sequences using a preregistered locus- and species-specific acceptance rule
4. Deposit verified strain in -80°C glycerol stock with documented provenance
5. Define re-verification frequency from the propagation and contamination-control plan

**Acceptance criteria:** unset until the barcode locus, reference set, ambiguity policy, contamination controls, and confirmatory method are selected.

## Cross-references

- [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) — the scope page these SOPs operationalize
- [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md#research-conjecture--a-reproducible-medicinal-fungal-material-may-expose-a-gout-weakness) — exact-material reproducibility conjecture
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — invalidated COMP-014 boundary; no method authority
- [`validation-experiments.md`](./validation-experiments.md) §2.6 — pilot-driven matched interaction study

## Open method-development gates

- For SOP-1, recover the exact cultivation, extraction, and GLPP fractionation methods for the material whose biological result is being tested. Historical Juncao search terms are retrieval aids, not a reason to select that cultivation route.
- For SOP-3, qualify the method against one exact material without presuming it is the simplest sourcing route.
- Before SOP-2 co-quantification, obtain lawful research-use reference standards and qualify both analytes in the intended matrix.
- Use independent operators to estimate method transferability, then set acceptance criteria before result-bearing batch comparisons.
