---
title: "ChEMBL Cross-Check — Use Boundary and Source-Verification Workflow"
date: 2026-10-01
tags:
  - chembl
  - rigor
  - bioactivity
  - provenance
related:
  - ../nlrp3-inhibitor-screen.md
  - ../nlrp3-exploit-map.md
  - manual-literature-mining.md
sources:
  - "EMBL-EBI ChEMBL"
status: methodology
---

# ChEMBL Cross-Check — Use Boundary and Source-Verification Workflow

## Compound refresh table

Last refreshed: 2026-10-01. All compounds re-queried via the ChEMBL REST API (`https://www.ebi.ac.uk/chembl/api/data/`); ChEMBL version was not returned by the API in this run (see `logs/chembl-refresh-state.json`). Entries marked ★ are new to this quarter's sweep.

Evidence level for all ChEMBL bioactivity records defaults to **(In Vitro)** unless the underlying reference is explicitly clinical. "pChEMBL" is −log₁₀(molar IC50/Ki/EC50); higher = more potent. Top-target column shows the highest-pChEMBL named protein target, not the most biologically relevant one — see the per-record verification rules below before using any value in a wiki claim.

### Indexed compounds

| Compound | ChEMBL ID | Top annotated target | Best pChEMBL | Notes | Last refreshed |
|---|---|---|---|---|---|
| Dapansutrile | CHEMBL3989943 | NLRP3 (IC50) | 9.00 | MoA confirmed (direct inhibitor); max_phase 4 | 2026-10-01 |
| Colchicine | CHEMBL107 | Tubulin / beta-tubulin binding (MoA) | — | Anti-mitotic; cell-line phenotypic hits dominate top records | 2026-10-01 |
| Zileuton | CHEMBL93 | ALOX5 / 5-LOX (IC50) | 6.85 | MoA confirmed; max_phase 4 | 2026-10-01 |
| Oridonin | CHEMBL1164920 | NLRP3 (IC50) | 6.11 | 408 records; covalent NEK7/NLRP3 mechanism | 2026-10-01 |
| Ursolic acid | CHEMBL169 | ROR-gamma (IC50) | 9.12 | Prior queue item (2026-Q3) resolved; NF-kB p65 also annotated (7.51) | 2026-10-01 |
| Cholecalciferol | CHEMBL1042 | VDR (EC50) | 9.68 | Active metabolite calcitriol (CHEMBL846) has richer dataset | 2026-10-01 |
| Genistein | CHEMBL44 | ERβ (Ki) | 9.23 | 2064 records; also tyrosine kinase and CFTR | 2026-10-01 |
| Curcumin | CHEMBL140 | Amyloid-beta APP (Ki 9.68); DYRK2 (IC50 8.60) | 9.68 | PAINS compound; prior DYRK2 queue item (2026-Q3) resolved | 2026-10-01 |
| Quercetin | CHEMBL50 | MAO-A (IC50) | 8.00 | 2978 records; very broad activity profile | 2026-10-01 |
| EGCG | CHEMBL297453 | Bacterial FabI (Ki) | 8.10 | Top hits are antimicrobial; pref_name typo in ChEMBL ("EPIGALOCATECHIN") | 2026-10-01 |
| Disulfiram | CHEMBL964 | LOXL4 (IC50); ALOX15 (screen) | 7.23 | GSDMD-pore mechanism (cited MoA) not in top-5 pChEMBL records | 2026-10-01 |
| Tranilast | CHEMBL415324 | NPC1 / Rab-9A (NCATS screen) | 7.05 | No formal MoA in ChEMBL mechanism table | 2026-10-01 |
| NAC | CHEMBL600 | ALOX15 (NCATS screen) | 7.60 | Indexed as "Acetylcysteine"; most records use non-pChEMBL readouts | 2026-10-01 |
| Cordycepin | CHEMBL305686 | Antiparasitic / antiviral (functional) | 9.30 | Top-pChEMBL records are anti-trypanosomal; adenosine kinase in broader set | 2026-10-01 |
| Spermidine | CHEMBL19612 | Carbonic anhydrase (Ki) | 6.95 | Autophagy / mTOR mechanism not captured in ChEMBL records | 2026-10-01 |
| Carnosine | CHEMBL242948 | PEPT2 / SLC15A2 (EC50, substrate) | 5.65 | Dipeptide transporter substrate; ROR-gamma screen potency 5.65 (one document) | 2026-10-01 |
| Sulforaphane | CHEMBL48802 | iNOS (IC50); Nrf2 / Keap1 (EC50) | 6.40 | No direct NLRP3 binding in top records | 2026-10-01 |
| Beta-caryophyllene | CHEMBL445740 | CB2 (Ki) | 6.82 | 8 pChEMBL records total; sparse | 2026-10-01 |
| Salidroside ★ | CHEMBL465208 | MAO-B (IC50) | 6.09 | NEW; MSU animal lead (PMID 30265377) vs MAO-B ChEMBL top target — see discrepancy block | 2026-10-01 |
| BHB | CHEMBL1162496 | MCT1 / MCT2 (transport assays) | — | Indexed as "(+/−)-3-hydroxybutyric acid"; 0 pChEMBL records | 2026-10-01 |
| Theaflavin (TF1) | CHEMBL346119 | Bcl-2 (Ki) | 6.16 | 5 pChEMBL records; separate entry for digallate | 2026-10-01 |
| Theaflavin-3,3'-digallate (TF3) | CHEMBL434864 | OATP1B1 (Ki); OATP1B3 (Ki) | 5.82 | Hepatic uptake transporters, not renal; see discrepancy block | 2026-10-01 |
| Eurycomanone | CHEMBL1171981 | Unchecked (IC50, sparse) | 5.62 | Active constituent of *Eurycoma longifolia*; 3 pChEMBL records | 2026-10-01 |
| D-Limonene | CHEMBL449062 | *Plasmodium* (screen) | 4.18 | 1 pChEMBL record; ChEMBL is not useful for limonene target affinity | 2026-10-01 |

### Not indexed or peptide/biologic

| Compound | ChEMBL status | Notes |
|---|---|---|
| BPC-157 | CHEMBL4297358 registered; 0 bioactivity records | Synthetic pentadecapeptide; no curated assay data |
| Apelin-13 ★ | Not indexed — peptide | New wiki page (2026-07-23); stub CHEMBL4650373 exists with 0 activities |
| Thymulin | Not indexed — peptide | Zinc-bound nonapeptide; NONATHYMULIN analogue (CHEMBL2106455) has 0 activities |
| KPV | Not indexed — peptide | Free Lys-Pro-Val tripeptide absent from ChEMBL |
| Resolvin D1 | Not in ChEMBL | SPM not curated as small molecule |
| Maresin 1 | Not in ChEMBL | SPM not curated as small molecule |
| Lactoferrin | Protein/biologic | No ChEMBL small-molecule entry |
| *Houttuynia cordata* polysaccharides | Complex botanical | No ChEMBL entry |

★ = new to this quarter's sweep.

## Discrepancy blocks

### Salidroside — MAO-B as top ChEMBL target

Salidroside (CHEMBL465208, tyrosol-glucose glycoside) was added to the Open Enzyme candidate screen after the 2026-Q3 refresh. The ChEMBL bioactivity set (211 records; 8 with pChEMBL values) shows monoamine oxidase B (MAO-B) as the top annotated protein target: IC50 pChEMBL 6.09 (Ki 6.04), both from CHEMBL4706619. The wiki entry for salidroside ([`nlrp3-inhibitor-screen.md`](../nlrp3-inhibitor-screen.md)) cites one MSU animal-model retrieval lead (PMID 30265377) and notes that the primary study is not rehydrated. MAO-B inhibition at ~800 nM is not mentioned in the current wiki. This is not a contradiction of the MSU animal claim, but it surfaces an additional target profile to verify before attributing any salidroside effect solely to NLRP3 or urate-pathway activity. Queue file: `synthesis/queue/2026-10-01-chembl-discrepancy-1-salidroside-mao-b.md`. *(source: ChEMBL refresh 2026-10-01)* **(In Vitro)**

### Theaflavin-3,3'-digallate — OATP1B1/OATP1B3 hepatic transporter inhibition

The ChEMBL bioactivity set for theaflavin-3,3'-digallate (TF3, CHEMBL434864) contains four pChEMBL-bearing records, all against hepatic uptake transporters from a single study (CHEMBL3039007): OATP1B1 Ki pChEMBL 5.82 (~1.5 μM), OATP1B1 IC50 pChEMBL 5.56, OATP1B3 Ki pChEMBL 5.47 (~3.4 μM), OATP1B3 IC50 pChEMBL 5.35. The wiki page for theaflavins ([`theaflavins.md`](../theaflavins.md)) covers renal URAT1/GLUT9/OAT1 expression effects and intestinal ABCG2 substrate/induction data, but does not mention hepatic OATP1B1 or OATP1B3. OATP1B1/1B3 are hepatic sinusoidal importers relevant to drug-drug interactions (statins, methotrexate, urate-lowering agents). Inhibition at these concentrations could affect co-administered drug pharmacokinetics and may be a relevant safety variable in any experimental design using concentrated TF3. Queue file: `synthesis/queue/2026-10-01-chembl-discrepancy-2-theaflavin-digallate-oatp1b.md`. *(source: ChEMBL refresh 2026-10-01)* **(In Vitro)**

## What ChEMBL can do here

ChEMBL is a discovery and cross-check surface for curated activity records. It is useful for locating a candidate compound–target assay and for noticing that a familiar compound may have a relevant off-target or adjacent mechanism.

It is not, by itself:

- a complete biological-interactor catalogue;
- a transporter-substrate authority;
- a natural-product or multilingual literature census;
- evidence that a non-retrieved relationship does not exist;
- or a basis for ranking values from different assays.

The current Open Enzyme receipt retains version/date context and a refresh recipe, but not immutable raw responses and every exact request parameter from the legacy runs. It therefore cannot support record counts, coverage rates, zero-entry claims, “top target” rankings, or exhaustive absence conclusions.

## Match the source to the question

| Question | Appropriate evidence source |
|---|---|
| Does compound X bind or inhibit target Y in a named assay? | ChEMBL as a locator, then the primary assay paper |
| Is X a transporter substrate or inhibitor? | Primary transport study, product label, or a curated transporter source with relationship type and cited evidence |
| What physiological reaction or pathway contains X or Y? | Primary biology plus Reactome/KEGG as pathway infrastructure |
| Does a biologic or peptide alter the pathway? | Material-specific biochemical, cell, animal, and clinical literature |
| Does a natural product have relevant evidence? | ChEMBL plus primary multilingual searches using mechanism, material/species, traditional formula, and pathology framing |

## Per-record verification

Before a ChEMBL-derived claim enters a reader-facing page:

1. Save the exact query, database version, access date, filters, and returned record identifier.
2. Open the named primary paper.
3. Verify compound identity, target, species, assay format, cell system, stimulus, time point, units, qualifiers, and whether the value is measured or inferred.
4. State the evidence level next to the claim.
5. Keep biochemical, cellular, functional, and phenotypic results separate.
6. Do not call a functional pathway readout direct binding.
7. Treat a missing record as an unresolved query result.

## NLRP3 naming rule

- **Direct NLRP3 inhibitor:** a source-verified direct NLRP3 binding or inhibition measurement in a named assay.
- **NLRP3 pathway modulator:** a functional inflammasome output or an upstream/downstream mechanism.

This distinction is about what was measured, not whether the lead is interesting. A functional MSU result may be more decision-relevant than a biochemical binding value, but it should keep its actual label.

## Cross-assay rule

Do not compare or divide potency values when species, cell type, stimulus, endpoint, time, or assay format differ. In particular, separate mouse and human dapansutrile records motivate a matched species-bridging experiment; their legacy numerical ratio is not an isolated species effect and does not explain clinical dosing or efficacy.

## Refresh receipt

A future refresh should write a compact machine-readable receipt under `logs/` containing:

- ChEMBL release and access date;
- exact request URLs or parameters;
- compound and target identifiers;
- filters and pagination;
- returned record identifiers;
- failures and retry state;
- and hashes or retained raw responses sufficient to reproduce any count or non-retrieval statement.

Scientific interpretations belong on the mechanism-owning wiki page after primary-source verification. The receipt records method, not a second findings narrative.

## Useful leads that survive

Quarterly sweeps have surfaced: quercetin–5-LOX (PMID 2066989, rehydration required), beta-caryophyllene–CB2 (Ki 6.82, CHEMBL4411259), and direct NLRP3 binding records for dapansutrile (IC50 9.00) and oridonin (IC50 6.11). The 2026-Q4 sweep adds two new leads: salidroside–MAO-B (IC50 6.09, CHEMBL4706619) and theaflavin-3,3'-digallate–OATP1B1/OATP1B3 hepatic transporter inhibition (Ki 5.82/5.47, CHEMBL3039007). All are leads to rehydrate from their primary papers. This page does not preserve an assay-wide rank, complete compound table, or claim that these are the only relevant records.

## Decision rule

A ChEMBL record advances a scientific claim only when its primary assay is verified and the measurement answers the question being asked. A database surprise can create a Research Conjecture; it cannot establish gout relevance, exposure, additivity, safety, or production priority by itself.

*Methodology page. Git retains the retired legacy table and its query-era annotations.*
