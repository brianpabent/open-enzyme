# Input provenance — COMP-048

All data identities were frozen and checksum-verified on 2026-07-24. The exact
URLs, byte counts, SHA-256 values, release identifiers, archive members, and
roles are in `source-manifest.json`.

## Human kidney expression

The donor-level input is the processed CELLxGENE distribution of the integrated
single-nucleus and single-cell adult human kidney atlas associated with Lake et
al., *Nature* 2023 (DOI
[10.1038/s41586-023-05769-3](https://doi.org/10.1038/s41586-023-05769-3)).
The frozen H5AD identifies collection
`bcb61471-2a44-4d00-a0af-ff085512674c`, dataset
`0b75c598-0893-4216-afe8-5414cab7739d`, and dataset version
`4cd166f1-ef51-4137-869d-0a3688bc2bc8`. It supplies donor, condition,
cell-type, and expression fields. The computation uses nonzero expression as a
detection call and preserves donor-level denominators; it does not reinterpret
processed values as absolute transcript or protein abundance.

This input combines single-cell and single-nucleus assays and multiple tissue
sources. Assay and specimen sensitivity is therefore reported, not averaged
away. Raw human sequencing data are not required and no controlled clinical
fields are used.

## Surface candidate universe and topology prior

The candidate universe is sheet `11.7_Surfaceome` from Bausch-Fluck et al.,
*PNAS* 2018 (DOI
[10.1073/pnas.1808790115](https://doi.org/10.1073/pnas.1808790115)).
The paper combines curated positives, Cell Surface Protein Atlas evidence,
topology annotation, and machine-learning predictions. These are retained as
separate fields. Membership in this list is not treated as proof of renal
surface localization or receptor-mediated uptake. A noncytoplasmic segment is
a topology/accessibility prior only.

## Cross-tissue and protein localization

Human Protein Atlas release 25.1 supplies:

- cell-type RNA in nCPM;
- consensus tissue RNA in nTPM; and
- normal-tissue IHC level and reliability.

RNA and IHC remain separate axes. A missing antibody result is `unknown`, not
negative. HPA cell-type and tissue aggregates are not donor-level estimates and
do not establish vascular or luminal polarity.

The frozen HPA entries in `source-manifest.json` name the official release page,
the cell-type or tissue data-dictionary page, the exact expected TSV header,
the declared primary key used for duplicate detection, the archive member to
read, and the downloaded ZIP archive's byte count and SHA-256. The analysis
refuses an archive, member, schema, key, or required-category mismatch. Release
labels alone are not treated as sufficient provenance.

## Controls and direct evidence boundaries

ASGR1 and ASGR2 provide a method control for the liver/hepatocyte expression
pattern used by hepatocyte-targeted GalNAc-siRNA. The delivery precedent is
Nair et al., *JACS* 2014 (PMID
[25110913](https://pubmed.ncbi.nlm.nih.gov/25110913/)); the control does not
transfer hepatic delivery performance to kidney or prove that either subunit
alone is a delivery handle.

LRP2 and CUBN are proximal-tubule uptake-context controls (Christensen and
Birn, *Nat Rev Mol Cell Biol* 2002, PMID
[11994745](https://pubmed.ncbi.nlm.nih.gov/11994745/)). This is review-tier
context: neither control receives a direct-internalization flag and neither can
support a candidate-specific internalization inference. Candidate-specific
primary evidence is required after nomination. Neither control is evidence for
siRNA delivery.

SLC22A12 is the target-compartment marker, based on the URAT1 identification
paper (Enomoto et al., *Nature* 2002, PMID
[12024214](https://pubmed.ncbi.nlm.nih.gov/12024214/)). Its expression does not
make it an internalizing receptor.

## Deliberate exclusions

No source in this COMP can establish ligand binding, receptor-mediated
internalization, basolateral or apical accessibility, blood or urinary access,
endosomal escape, siRNA loading or release, SLC22A12 knockdown, urate transport
change, dose, safety, or efficacy. Candidate-specific internalization and
polarity evidence must be rehydrated from primary sources after the
expression/surface screen nominates a follow-up candidate; absent evidence is
reported as `unknown` and cannot be silently inferred from an endosome
annotation, cytoplasmic tail, receptor label, or analogy.
