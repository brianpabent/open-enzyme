# comp-023 Provenance: All Inputs + Verification Log

**Date assembled:** 2026-05-14
**cobra version:** 0.31.1
**Python:** 3.13.7

This file documents every source for `inputs/*` per Open Enzyme reproducibility standard. Subagents verifying this experiment can re-run the data fetch using the URLs/PMIDs below.

## GEM source

| File | Source | URL | Provenance |
|---|---|---|---|
| `inputs/iWV1314.xml` | BioModels MODEL1507180056 | https://www.ebi.ac.uk/biomodels/MODEL1507180056 | Curated SBML L3+FBC deposit of Vongsangnak 2008 iWV1314 *A. oryzae* GEM. Fetched 2026-05-14 via the `model/download/MODEL1507180056.2?filename=MODEL1507180056_url.xml` endpoint. 2,361 reactions / 1,104 metabolites / 1,346 genes / 4 compartments (cytosol, peroxisome, mitochondria, extracellular). Note: original Vongsangnak 2008 paper reports 1,314 reactions / 1,073 metabolites; the BioModels deposit is the curated/extended version. |

## Cordycepin biosynthesis stoichiometry sources

| Claim | Source | Verification |
|---|---|---|
| Cordycepin biosynthesis in *A. oryzae* via cns1+cns2 reaches 564.64 ± 9.59 mg/L/day on glucose | [Jeennor S et al. 2023, *Microb Cell Fact*; PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/) "Efficient de novo production of bioactive cordycepin by Aspergillus oryzae using a food-grade expression platform" | WebFetch 2026-05-14 confirmed: titer = 564.64 ± 9.59 mg/L/d; substrate = glucose; cordycepin is secreted (extracellular). Source organism for cns1+cns2 is not explicitly named in the abstract (per WebFetch); assumed to be *Cordyceps militaris* per the parent BGC characterization in Xia 2017. |
| Cns1 = oxidoreductase; Cns2 = HDc-family metal-dependent phosphohydrolase; Cns3 = nucleotide kinase | [Wang H et al. 2023 *Int Microbiol*; PMC11300563](https://pmc.ncbi.nlm.nih.gov/articles/PMC11300563/) "A novel complementary pathway of cordycepin biosynthesis in Cordyceps militaris" + WebSearch synthesis of canonical Xia 2017 BGC | WebSearch + WebFetch 2026-05-14 confirmed: Cns3 phosphorylates adenosine to 3'-AMP; Cns2 dephosphorylates 3'-AMP to 2'-carbonyl-3'-deoxyadenosine; Cns1 reduces 2'-C-3'-dA to cordycepin. |
| cns1+cns2 alone (without cns3) is sufficient for heterologous cordycepin expression; host kinases supply 3'-AMP | [Yan et al. 2024, Front Chem Eng (doi 10.3389/fceng.2024.1446454)](https://www.frontiersin.org/journals/chemical-engineering/articles/10.3389/fceng.2024.1446454/full) | WebFetch 2026-05-14: "expressing only Cns1 and Cns2 is sufficient for cordycepin heterologous expression"; host-derived 3'-AMP supply via "adenosine via... host kinases" or 2',3'-cAMP from mRNA degradation. |
| Pentostatin protects cordycepin from ADA-mediated deamination; co-produced from the same BGC | [Xia Y et al. 2017, *Cell Chem Biol*; PMID 29056419](https://pubmed.ncbi.nlm.nih.gov/29056419/) "Fungal Cordycepin Biosynthesis Is Coupled with the Production of the Safeguard Molecule Pentostatin" | WebFetch 2026-05-14: "PTN safeguards COR from deamination by inhibiting adenosine deaminase (ADA) activity"; "cordycepin and pentostatin biosynthesis... coupled with PTN production by a single gene cluster." |
| Cns1 cofactor (NADH vs NADPH) not mechanistically pinned | Yan et al. 2024 Front Chem Eng (above) | WebFetch 2026-05-14: "The document does not provide explicit stoichiometric calculations of ATP or NAD(P)H consumption per cordycepin molecule produced." V1 of comp-023 assumes NADPH as the fungal-default biosynthetic reductant. Flagged in Limitations §4. |

**Net stoichiometry used in this v1 (verified against the above):**
```
adenosine + ATP + NADPH  →  cordycepin + ADP + Pi + NADP⁺ + H⁺
```
Captures: (a) host kinase phosphorylating adenosine to 3'-AMP (ATP → ADP + Pi), (b) Cns2 dephosphorylating to 2'-C-3'-dA (Pi released, balanced into the net), (c) Cns1 reducing to cordycepin (NADPH → NADP⁺).

## Kojic acid biosynthesis sources

| Claim | Source | Verification |
|---|---|---|
| kojA / kojR / kojT gene cluster; three-gene biosynthesis | [Terabayashi Y et al. 2010, *Fungal Genet Biol*; PMID 20650324](https://pubmed.ncbi.nlm.nih.gov/20650324/) "Identification and characterization of genes responsible for biosynthesis of kojic acid, an industrially important compound from Aspergillus oryzae" | WebSearch 2026-05-14 confirmed: three genes (kojA, kojR, kojT). KojA = FAD-dependent oxidoreductase. |
| Glucose → kojic acid via one oxidation + two dehydrations (net) | [Marui J et al. 2011, *Appl Microbiol Biotechnol*; PMID 21514215](https://pubmed.ncbi.nlm.nih.gov/21514215/) "Kojic acid biosynthesis in A. oryzae is regulated by a Zn(II)2Cys6 transcriptional activator and induced by kojic acid at the transcriptional level" | WebSearch 2026-05-14 confirmed: "at least one oxidation step (CHOH → CO) and two dehydration steps are required for the conversion of glucose to kojic acid." Net mass balance is glucose (C6H12O6) → kojic acid (C6H6O4) + 2 H₂O + 2[H] (oxidation equivalents). |
| Native *A. oryzae* kojic acid titer 3-5 g/L | [koji-endgame-strain.md §2.3](../../../../koji-endgame-strain.md), [aspergillus-oryzae.md](../../../../aspergillus-oryzae.md) | Already in wiki corpus; not re-verified in comp-023. |

**Net stoichiometry used in this v1:**
```
D-glucose + O₂ + NADP⁺  →  kojic acid + 2 H₂O + NADPH + H⁺
```
Carries: glucose carbon → kojic acid; 1 O₂ consumed (oxidation); 1 NADPH generated (FAD-dependent KojA proxy). v1 simplification; flagged in Limitations §3.

## Ergothioneine biosynthesis sources

| Claim | Source | Verification |
|---|---|---|
| Fungal pathway = Egt1 (N-methylation + C-S bond formation) + Egt2 (β-lyase, C-S cleavage) | [Hu W et al. 2014, *Org Lett*; PMID 25496641](https://pubmed.ncbi.nlm.nih.gov/25496641/) "Bioinformatic and Biochemical Characterizations of C-S Bond Formation and Cleavage Enzymes in N. crassa Ergothioneine Biosynthetic Pathway" | WebSearch 2026-05-14 confirmed: "In N. crassa, EGT is synthesized with two enzymes: Egt1 methylates histidine and forms the C-S bond with cysteine to form hercynylcysteine sulfoxide; and Egt2 cleaves the C-S bond to form ergothioneine." |
| 3 SAM consumed per ergothioneine (for N-trimethylation of histidine to hercynine) | [Bello MH et al. 2012, *Mol Microbiol*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3438316/) + Wikipedia ergothioneine + bacterial EgtD precedent in N-methylation step | WebSearch 2026-05-14 confirmed: "EgtD catalyzes N-alpha-trimethylation of L-histidine with three molecules of S-adenosylmethionine." Fungal Egt1 has the equivalent N-methyltransferase domain. |
| Native *A. oryzae* ergothioneine titer ~20 mg/g dry mycelial mass | [koji-endgame-strain.md §2.4](../../../../koji-endgame-strain.md), [engineered-koji-protocol.md §01b](../../../../engineered-koji-protocol.md) | Already in wiki corpus; not re-verified in comp-023. |

**Net stoichiometry used in this v1:**
```
L-histidine + 3 SAM + L-cysteine + O₂  →  ergothioneine + 3 SAH + pyruvate + NH₃ + H₂O
```
Carries: 3 SAM cost for N-trimethylation; 1 cysteine for sulfur donation; pyruvate + NH₃ released from cysteine via β-lyase action of Egt2. v1 simplification; flagged in Limitations §3.

## Lactoferrin + uricase cassette parameters

| Claim | Source | Verification |
|---|---|---|
| Lactoferrin §1.9 success threshold ≥500 mg/L | [validation-experiments.md §1.9](../../../../validation-experiments.md) | Direct grep against the canonical §1.9 protocol. |
| Lactoferrin = 691 aa, 16 disulfides, PDI-heavy | [chaperone-orthogonal-stacking.md §4](../../../../chaperone-orthogonal-stacking.md) row "Lactoferrin (hLf, P02788)" | Direct grep; 16 disulfides per Notari 2023 PMC10465537. |
| Uricase = *A. flavus* uaZ Q00511, 302 aa, 0 disulfides | [chaperone-orthogonal-stacking.md §4](../../../../chaperone-orthogonal-stacking.md) row "Uricase (uaZ, A. flavus, Q00511)" + [comp-010 cassette-compatibility-computational.md](../../../../cassette-compatibility-computational.md) | Direct grep. |
| Uricase 40 mg/L/d anchor (Phase 0 conservative; matches Huynh 2020 adalimumab order of magnitude) | [comp-010](../../../../cassette-compatibility-computational.md) | Direct grep of Huynh 2020 39.7 mg/L reference. |
| ATP-per-aa translation cost ≈ 4 (basal translation: 2 for aminoacyl-tRNA + 2 for EF-Tu/EF-G GTP hydrolysis) | Standard biochemistry; e.g. [Lodish et al. *Molecular Cell Biology* 8e](https://www.amazon.com/Molecular-Cell-Biology-Harvey-Lodish/dp/1464183392) ch 5 | Standard textbook biochemistry; not separately PMID-cited. The "+0.5 for ER folding (uricase, PDI-light)" and "+2 for ER folding (Lf, PDI-heavy)" elevations are v1 approximations flagged in Limitations §2. |

## Biomass density assumption

| Claim | Source | Verification |
|---|---|---|
| Steady-state biomass density 5 gDW/L for mid-log fungal submerged culture | [Vongsangnak 2008 PMID 18801187](https://pubmed.ncbi.nlm.nih.gov/18801187/) Table 1 supplementary; standard *A. oryzae* submerged-batch reference | Conservative anchor. The Jeennor 2023 fed-batch fermentation likely achieves 10-20 gDW/L at peak biomass; using 5 gDW/L means the comp-023 cordycepin mmol/gDW/h demand is 2-4× higher than the actual Jeennor fed-batch demand. This OVER-estimates burden; i.e. the GREEN verdict is conservative on the burden axis (real burden per gDW is lower than modeled). |

## §1.9 design parameters cross-referenced

| Claim | Source | Verification |
|---|---|---|
| §1.9 success threshold: Lf ≥500 mg/L, uricase activity ≥50 μmol/h/OD, native metabolite within 30% | [validation-experiments.md §1.9 "Success criteria"](../../../../validation-experiments.md) | Direct grep. |
| NSAR1 5-marker platform provides 5 simultaneous integration slots; H01 uses 2 (uricase + Lf), 3 remaining | [koji-endgame-strain.md §3.4 + post-H01 host recommendation](../../../../koji-endgame-strain.md) | Direct grep. cns1+cns2 can use one of the 3 remaining slots. |

## Verification-agent self-review pass

Per the brief Task 10 and the comp-NNN infrastructure proposal in [computational-experiments.md §Infrastructure proposals](../../../../computational-experiments.md):

| Load-bearing claim in `wiki/cordycepin-cassette-burden-computational.md` | Source | Pass? |
|---|---|---|
| iWV1314 has 2,361 reactions / 1,104 metabolites / 1,346 genes | BioModels MODEL1507180056 + cobra load | ✓ (direct read at runtime) |
| Cordycepin titer 564.64 ± 9.59 mg/L/d | PMID 38071331 abstract | ✓ (WebFetch 2026-05-14) |
| cns1+cns2 sufficient without cns3 | Yan 2024 Front Chem Eng | ✓ (WebFetch 2026-05-14) |
| Cns1 cofactor not pinned (NADH vs NADPH) | Yan 2024 Front Chem Eng | ✓ (WebFetch 2026-05-14); flagged in Limitations §4 |
| Cordycepin secreted (extracellular) | PMID 38071331 abstract | ✓ (WebFetch 2026-05-14) |
| Pentostatin protects cordycepin from ADA | PMID 29056419 abstract | ✓ (WebFetch 2026-05-14) |
| Native kojic acid 3-5 g/L | koji-endgame-strain.md §2.3 (canonical reference) | ✓ (grep) |
| Native ergothioneine ~20 mg/g DW | koji-endgame-strain.md §2.4 (canonical reference) | ✓ (grep) |
| §1.9 Lf success threshold ≥500 mg/L | validation-experiments.md §1.9 | ✓ (grep) |
| Lactoferrin = 16 disulfides, 691 aa | chaperone-orthogonal-stacking.md §4 row | ✓ (grep) |
| Decision thresholds <10% growth + ≥80% native yield | computational-experiments.md comp-023 row | ✓ (grep against brief) |
| Vongsangnak 2008 reported mu_max ≈ 0.31 h⁻¹ for *A. oryzae* on glucose | Vongsangnak 2008 PMID 18801187 Table 1 | Approximate; paper cites 0.3 h⁻¹ generic order-of-magnitude for fungal submerged batch. Used only for "model flux ≠ h⁻¹" calibration note; not load-bearing for verdict. |
| 16 disulfides → PDI-heavy → ATP-per-aa ≈ 6 (v1 approximation) | v1 approximation, NOT primary-source-anchored | ⚠ Flagged in Limitations §2; pcSec class model would compute this from PDI/ERO1 occupancy directly. |

## Environment

- Python: 3.13.7 (CPython, x86_64-apple-darwin25.3)
- cobra: 0.31.1
- numpy: bundled
- scipy: bundled
- swiglpk: 5.0.13 (GLPK solver backend)
- Run platform: macOS 25.3
- Date: 2026-05-14
