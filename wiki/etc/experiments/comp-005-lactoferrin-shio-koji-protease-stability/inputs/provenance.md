# Provenance — comp-005 inputs

## P02788.fasta — Human lactoferrin sequence
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P02788.fasta
- **Fetch date:** 2026-05-05
- **Entry:** sp|P02788|TRFL_HUMAN Lactotransferrin, Homo sapiens, PE=1 SV=6
- **Length:** 710 aa (canonical isoform, including signal peptide aa 1–19)
- **Signal peptide:** residues 1–19 (MKLVFLVLLFLGALGLCLA); cleaved during mammalian secretion
  - Note: if expressed in A. oryzae, signal peptide processing depends on the host secretory pathway;
    include signal peptide in analysis to be conservative (unprocessed form has disordered N-terminus)

## alphafold_P02788_plddt.json — Per-residue pLDDT confidence scores
- **Source:** AlphaFold Protein Structure Database (EMBL-EBI)
  - Metadata: https://alphafold.ebi.ac.uk/api/prediction/P02788
  - Confidence scores: https://alphafold.ebi.ac.uk/files/AF-P02788-F1-confidence_v6.json
- **Model:** AF-P02788-F1, version 6 (canonical isoform, 710 residues)
- **Fetch date:** 2026-05-05
- **Field used:** `confidenceScore` array, mapped to 1-indexed residue positions

## protease_specificities.json — Koji protease rules + shio-koji conditions
- **Shared input:** copied from comp-001 inputs (same three A. oryzae proteases, same conditions)
- **Source:** MEROPS database release 12.4; Tominaga & Tsujisaka 1976 (NPr); Ikeda et al. 1975 (ALP);
  Koaze et al. 1964 (acid protease)
- See comp-001 inputs/provenance.md for full citations
