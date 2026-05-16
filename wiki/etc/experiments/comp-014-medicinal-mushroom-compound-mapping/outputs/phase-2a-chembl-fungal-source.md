---
title: comp-014 Phase 2a — ChEMBL fungal-source bioactivity sweep across 19 chokepoints
date: 2026-05-06
phase: 2a
artifact: phase-2a-chembl-fungal-source.json
---

# comp-014 Phase 2a — ChEMBL × fungal-source × chokepoint sweep

**Method.** Two-pass ChEMBL MCP query: (1) bulk bioactivity pulls per chokepoint target (top 200 IC50-ranked records each) to inventory named compounds; (2) targeted compound→all-targets queries for known fungal natural products to surface chokepoint hits not captured in the top-200 cut. Confidence assignments use ChEMBL's `natural_product` flag + literature-confirmed biosynthetic source organism.

**Scope.** 19 Open Enzyme chokepoints (URAT1, GLUT9, ABCG2, XO, NLRP3, ASC, Caspase-1, IL-1β, TNFα, C5aR1, Lp-PLA2, HDAC6, PPARγ, KEAP1, OAT1, OAT3, OAT4, TXNIP, PDI). 18 mapped to ChEMBL targets; TXNIP has no curated ChEMBL target.

## Headline findings

| Compound | Fungal source | Chokepoint | Best potency | Tier |
|---|---|---|---|---|
| **FUMITREMORGIN C** (CHEMBL410316) | *Aspergillus fumigatus* | **ABCG2** | **IC50 = 800 nM (pChEMBL 6.10)** | **TIER 1** — drug-like, canonical reference inhibitor |
| MYCOPHENOLIC ACID (CHEMBL866) | *Penicillium brevicompactum* | PPARγ | functional activity at 1 μM (cell-based, "Active"); Kd ≈ 110 μM (out-of-range) | TIER 3 — real but weak; mechanism probe |
| LOVASTATIN (CHEMBL503) | *Aspergillus terreus* / *Pleurotus ostreatus* | HDAC6 | IC50 = 16.3 μM (pChEMBL 4.79) | TIER 3 — off-target, low potency |
| LOVASTATIN (CHEMBL503) | *A. terreus* / *P. ostreatus* | PPARγ | Potency = 50 μM (qHTS, inconclusive) | TIER 4 — likely artifact |

**Total chokepoints with fungal-source hits: 3 of 19** (ABCG2, HDAC6, PPARγ).
**Total fungal compound × chokepoint pairs: 4** (one TIER 1, two TIER 3, one TIER 4 + one out-of-scope cytotoxicity-only entry).

## Strategic negative finding — C5aR1

C5aR1 returned **zero fungal-source hits**. ChEMBL has only 2 named compounds against C5aR1 (one peptide, one synthetic small molecule), neither fungal-derived. This corroborates `validation-experiments.md §1.21` conclusion that there are no validated natural-product C5aR1 antagonists in the literature. **Implication:** C5aR1 looks like a pharmacochemistry-only target — fungal compounds are unlikely to provide a hit. Do NOT spend wet-lab time screening mushroom extracts against C5aR1.

## Per-target highlights

### Top-tier hit: FUMITREMORGIN C → ABCG2 (sub-μM)

The only sub-μM fungal hit in the entire sweep. FTC is the historical pharmacological tool compound for distinguishing ABCG2 / BCRP from MDR1 in efflux-pump biology; multiple independent labs across 2005–2011 confirm IC50 in the 800 nM – 11 μM range depending on cell line and assay format. ChEMBL `natural_product:true`. Source organism: *Aspergillus fumigatus*. **For a chokepoint where ABCG2 is the gut-secretion pathway accounting for ~1/3 of uric acid excretion, this is the highest-leverage finding from this sweep.**

### XO sweep — fungal hits absent in ChEMBL but Chinese-language literature exists

XO top-200 is dominated by plant flavonoids (luteolin, apigenin, chrysin, kaempferol, quercetin, myricetin, fisetin, galangin, baicalein, broussochalcone A) and synthetic xanthine-oxidase inhibitors (febuxostat, allopurinol, bropirimine). **Zero fungal-source hits.** Some Ganoderma triterpenoids have been reported as XO inhibitors in CNKI/Chinese-language pharmacology literature but are not in ChEMBL. Phase 2c lit scan should pick these up.

### URAT1, GLUT9, NLRP3, IL-1β, TNF, Caspase-1, ASC, OAT1/3/4, KEAP1, Lp-PLA2, PDI

All zero fungal-source hits. URAT1's top hits are all synthetic uricosurics (benzbromarone, verinurad, lesinurad, probenecid). NLRP3 has very thin ChEMBL coverage (8 named compounds total). Transporters (GLUT9, OAT4) and PPI targets (ASC, Caspase-1, KEAP1, TXNIP) have shallow ChEMBL chemistry overall — lack of fungal hits here is partly a coverage artifact, not necessarily a true biological null.

### HDAC6 / PPARγ — secondary tier

Lovastatin's HDAC6 activity (IC50 16 μM, J Med Chem 2013) is a documented off-target. Mevastatin (also fungal, *Penicillium citrinum*) was tested in the same assay and was inactive. Mycophenolic acid's PPARγ activity is real in cell-based assays at 1 μM but the binding Kd is flagged as outside typical range (~110 μM). Both are tier-3 — useful as mechanism probes, not drug-like leads.

## Notable absences from ChEMBL (need Phase 2b LOTUS / Phase 2c lit scan to recover)

These canonical mushroom compounds were searched by name and **NOT found** in ChEMBL — they need to be picked up by the LOTUS pull and multilingual lit scan:

- Ganoderic acids A/B/C/D, ganoderiol, lucidenic acids (Ganoderma lucidum)
- Ergosterol, ergosta-7,22-dien-3β-ol (ubiquitous fungal sterol)
- Hericenones C–H, erinacines A/B/C (Hericium erinaceus / Lion's Mane)
- Inotodiol, lanosterol-class compounds (Inonotus obliquus / Chaga)
- Pachymic acid, eburicoic acid, dehydrotrametenolic acid (Wolfiporia / Poria cocos)
- Polyporus polysaccharopeptides (PSK / krestin), polyporenic acids beyond polyporenic C
- Eritadenine (Lentinula edodes / shiitake hypocholesterolemic adenosine analog)
- Terreusinone (Aspergillus terreus pigment), aspulvinones, orsellinic acid (Aspergillus nidulans secondary metabolite reference)

The fact that none of these surfaced in ChEMBL is itself a finding — the Western-pharma curation bias is severe for medicinal mushroom chemistry, exactly the path-dependent narrowing the project's multilingual default rule warns against.

## Limitations (full list in JSON)

- ChEMBL source-organism field is sparsely populated; many fungal compounds will be missed.
- Western-pharma curation bias means TCM-source compounds are underrepresented.
- Bioactivity coverage is enzyme/GPCR-biased; transporters and PPI targets have shallow records.
- Tested only the canonical fungal NPs ChEMBL has as named molecules; mushroom-specific compound classes need Phase 2b/2c.
- The 800 nM FTC number is from a single primary source; check Rabindran/Allen primary characterization.
- Many flavonoids in the ABCG2 / XO sweeps could have plant + fungal endophyte production routes — not disambiguated here.

## Output artifact

Full structured data: [`phase-2a-chembl-fungal-source.json`](./phase-2a-chembl-fungal-source.json).
