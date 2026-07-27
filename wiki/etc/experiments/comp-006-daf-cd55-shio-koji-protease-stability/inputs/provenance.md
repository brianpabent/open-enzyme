# Provenance — comp-006 inputs

## P08174.fasta — Human DAF/CD55 sequence
- **Source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P08174.fasta
- **Fetch date:** 2026-05-05
- **Entry:** sp|P08174|DAF_HUMAN Complement decay-accelerating factor, Homo sapiens, PE=1 SV=4
- **Length:** 381 aa (canonical isoform, including signal peptide aa 1–34 and GPI-anchor propeptide aa 354–381)
- **Annotation boundaries (UniProt P08174 SV=4):**
  - Signal peptide: aa 1–34 (cleaved during secretion via the ER signal peptide pathway)
  - Mature chain: aa 35–353 ("Complement decay-accelerating factor"; the native membrane-attached ectodomain)
  - Propeptide / GPI-anchor signal: aa 354–381 (cleaved during GPI-anchor attachment in the ER lumen;
    this region would be replaced by, or simply truncated, in a soluble secreted engineering construct)
  - GPI-anchor amidation site: Ser353 (C-terminal residue of the mature ectodomain after propeptide cleavage)
- **Structural regions:**
  - SCR1 (Sushi domain 1): aa 35–96
  - SCR2 (Sushi domain 2): aa 97–160
  - SCR3 (Sushi domain 3): aa 161–222
  - SCR4 (Sushi domain 4): aa 223–285
  - Ser/Thr-rich stalk (heavily O-glycosylated in native context): aa 286–353
- **Engineering note:** For A. oryzae expression of a secreted soluble ectodomain, the human signal peptide
  (aa 1–34) would be replaced with a koji-native secretion signal (e.g., A. oryzae α-amylase signal, Ward 1995)
  and the construct would terminate at aa 353, omitting the GPI-anchor propeptide (aa 354–381).
  The operationally relevant sequence is the soluble ectodomain (aa 35–353).

## alphafold_P08174_plddt.json — Per-residue pLDDT confidence scores
- **Source:** AlphaFold Protein Structure Database (EMBL-EBI)
  - Confidence scores: https://alphafold.ebi.ac.uk/files/AF-P08174-F1-confidence_v6.json
- **Model:** AF-P08174-F1, version 6 (canonical isoform, 381 residues)
- **Fetch date:** 2026-05-05
- **Field used:** `confidenceScore` array, re-indexed to 1-indexed string keys to match library format
- **Format note:** The AlphaFold confidence JSON uses parallel arrays (`residueNumber`, `confidenceScore`);
  converted here to the dict format `{"1": score, "2": score, ...}` expected by
  `experiments/lib/protease_stability.py::load_plddt()`.

## protease_specificities.json — Koji protease rules + shio-koji conditions
- **Shared input:** copied verbatim from comp-005 inputs (same three A. oryzae proteases, same conditions)
- **Source:** MEROPS database release 12.4; Tominaga & Tsujisaka 1976 (NPr); Ikeda et al. 1975 (ALP);
  Koaze et al. 1964 (acid protease)
- See comp-001 inputs/provenance.md for full citations
