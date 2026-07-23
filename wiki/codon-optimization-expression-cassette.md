---
title: Yeast UOX Expression Cassette — Matched Build and Measurement Plan
date: 2026-04-21
tags: [codon-optimization, expression-cassette, saccharomyces, uricase, phase-0]
related:
  - engineered-yeast-uricase-proposal.md
  - saccharomyces-cerevisiae.md
  - uricase-variant-selection.md
  - gut-lumen-uricase-physiologic-regime-computational.md
  - validation-experiments.md
sources:
  - https://rest.uniprot.org/uniprotkb/Q00511.fasta
  - https://www.ncbi.nlm.nih.gov/nuccore/X61766.1
  - https://doi.org/10.1016/0378-1119(92)90041-M
  - https://doi.org/10.1021/acssynbio.4c00831
---

# Yeast UOX Expression Cassette — Matched Build and Measurement Plan

## Scope

Define sequence-controlled, matched *Saccharomyces* UOX constructs that can distinguish effects of payload identity, synonymous coding sequence, promoter, terminator, copy strategy, substrate access, and topology.

This page does not recommend a sequence variant, promoter, terminator, vector, integration strategy, topology, expression target, formulation, or dose.

## Sequence Provenance

For the *Aspergillus flavus* UOX reference:

- Protein record: [UniProt Q00511](https://rest.uniprot.org/uniprotkb/Q00511.fasta).
- Coding-sequence record: [GenBank X61766.1](https://www.ncbi.nlm.nih.gov/nuccore/X61766.1), 906 bp.
- Q00511 contains a 302-residue precursor; the annotated mature chain after initial-methionine removal is 301 aa. Record explicitly whether construct and assay numbering include the initiator methionine.
- P78609 is the *Candida utilis*/*Cyberlindnera jadinii* UOX record, not the *A. flavus* record. Treat it as a separate payload identity routed through [variant selection](./uricase-variant-selection.md).

Every construct record must include the exact nucleotide sequence, translated sequence, accession and version, leader or anchor junctions, stop codon, and numbering convention. A name such as “uaZ,” “wild type,” or “codon optimized” is not sufficient provenance.

## Design Matrix

Use matched pairs or a preregistered factorial. Do not change promoter, terminator, copy strategy, host background, and topology simultaneously and then attribute the result to one element.

| Axis | Candidate comparison | What remains fixed |
|---|---|---|
| Payload | Exact UOX sequences selected through [variant selection](./uricase-variant-selection.md) | Host, topology, promoter, terminator, copy strategy, process, assay |
| Synonymous coding sequence | Source CDS and preregistered synonymous variants | Amino-acid sequence and all noncoding elements |
| Promoter | Defined constitutive and inducible candidates | UOX sequence, topology, terminator, copy strategy, locus or vector |
| Terminator | Defined terminator candidates | UOX sequence, topology, promoter, copy strategy, locus or vector |
| Copy strategy | Defined plasmid or chromosomal-integration candidates | Cassette sequence, host background, process, assay |
| Topology | No leader; defined secretion leader; defined surface anchor | UOX sequence, promoter, terminator, copy strategy, host, process |
| Substrate access | No added transporter; defined transporter; transport-inactive control | UOX cassette and assay conditions |

Candidate part names may include TDH3, PGK1, TEF1, or GAL1 promoters; CYC1, ADH1, or CPS1 terminators; and plasmid or defined chromosomal-integration strategies. These are build options, not ranked choices.

## Matched Topology Schemas

```text
Intracellular comparator
promoter ─ UOX ─ terminator

Secreted comparator
same promoter ─ defined secretion leader ─ same UOX ─ same terminator

Surface-displayed comparator
same promoter ─ defined leader/anchor ─ same UOX ─ same terminator
```

A recovered cell-free fraction is a process comparator rather than a distinct expression cassette. Measure it from the matched producing construct and record every recovery step.

## Sequence and Build Acceptance

- Sequence-verify the complete cassette and every junction.
- Confirm the translated UOX sequence and numbering convention against the pinned source record.
- Record all synonymous changes and the constraint that motivated each one.
- Record predicted codon, GC, motif, and RNA-structure descriptors as design metadata only.
- Verify the integration locus or plasmid identity, orientation, and copy number.
- Record host background and passage history.
- Use an inactive-UOX counterpart and a chassis-only control in the same cassette context.

Codon scores and expression forecasts are not acceptance criteria. A synonymous variant advances only through measured soluble and active UOX under matched conditions.

## Measurement Panel

| Layer | Required readouts |
|---|---|
| Construct | Complete sequence, junctions, locus or vector, orientation, copy number |
| Transcription | Transcript abundance when needed to localize failure |
| Protein | Total UOX, soluble UOX, oligomeric state, degradation products |
| Localization | Intracellular, surface-associated, and extracellular UOX measured separately |
| Activity | Active IU in each fraction with assay substrate, pH, oxygen, time, and uncertainty reported |
| Host | Growth, viability, genetic stability, and batch variance |
| Process | Active UOX before and after recovery, storage, formulation, and simulated transit steps actually proposed |
| Reaction site | Urate, reaction product, dissolved oxygen, hydrogen peroxide, UOX persistence, and viability over time |

Report total protein and active UOX separately. Do not convert promoter identity, codon score, transcript abundance, or total protein into a delivered dose.

## Decision Sequence

1. **Identity:** Reject any construct whose sequence, junctions, host background, or copy state is unresolved.
2. **Active expression:** Advance only constructs with reproducible active UOX, interpretable localization, acceptable viability, and batch variance reported.
3. **Topology:** Expression measurements nominate configurations for [validation §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial); they do not select a topology. A yeast arm must be explicit in §1.33 or in a preregistered matched extension using the same control and decision framework.
4. **Safety:** A §1.33 survivor must clear [validation §1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay).
5. **Escalation:** No animal design follows until both gates pass.

If a construct fails, change the smallest axis supported by the failure localization, rebuild the matched control, and repeat the relevant measurement. Do not rescue a weak result with an unmeasured yield, dose, survival, or substrate-access assumption.

## Evidence Boundary

- Leplatois et al. establish **In Vitro** intracellular active *A. flavus* UOX expression in *S. cerevisiae*. They do not select the present cassette or oral topology.
- Wang et al. establish **In Vitro** engineered yeast uric-acid catabolism and show that payload, transporter, promoter, and integration context can be tested experimentally. Their result does not select this project's construct.
- **Mechanistic Extrapolation:** COMP-019's unconditional flat-dose classification is not robust to [COMP-044's](./gut-lumen-uricase-physiologic-regime-computational.md) tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no expression or production-sufficiency target, replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, or safety conclusion.

## Primary Sources and Decision Records

- [UniProt Q00511 source record](https://rest.uniprot.org/uniprotkb/Q00511.fasta) and [GenBank X61766.1 coding-sequence record](https://www.ncbi.nlm.nih.gov/nuccore/X61766.1).
- Leplatois P, et al. *Gene*. 1992;122(1):139–145. [doi:10.1016/0378-1119(92)90041-M](https://doi.org/10.1016/0378-1119(92)90041-M). **In Vitro.**
- Wang et al. *ACS Synthetic Biology*. 2025;14(6):2030–2043. [doi:10.1021/acssynbio.4c00831](https://doi.org/10.1021/acssynbio.4c00831). **In Vitro.**
- [Validation §§1.33 and 1.36](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).
