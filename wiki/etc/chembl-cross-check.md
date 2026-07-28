---
title: "ChEMBL Cross-Check — Use Boundary and Source-Verification Workflow"
date: 2026-07-27
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

The legacy cross-check surfaced several potentially relevant records, including quercetin–5-LOX, beta-caryophyllene–CB2, and candidate human-cell NLRP3 assays for dapansutrile and oridonin. These remain leads to rehydrate from their primary papers. This page does not preserve an assay-wide rank, complete compound table, or claim that these are the only relevant records.

## Decision rule

A ChEMBL record advances a scientific claim only when its primary assay is verified and the measurement answers the question being asked. A database surprise can create a Research Conjecture; it cannot establish gout relevance, exposure, additivity, safety, or production priority by itself.

*Methodology page. Git retains the retired legacy table and its query-era annotations.*
