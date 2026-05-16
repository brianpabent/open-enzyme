# Provenance — comp-012 inputs

## P08174.fasta — Human DAF/CD55 sequence
- **Source:** Copied verbatim from `experiments/comp-006-daf-cd55-shio-koji-protease-stability/inputs/P08174.fasta`
- **Original source:** UniProt REST API: https://rest.uniprot.org/uniprotkb/P08174.fasta (fetched 2026-05-05)
- **Entry:** sp|P08174|DAF_HUMAN Complement decay-accelerating factor, Homo sapiens, PE=1 SV=4
- **Length:** 381 aa (canonical isoform; signal peptide aa 1–34, mature ectodomain aa 35–353, GPI propeptide aa 354–381)
- **Construct analyzed in comp-012:** SCR1–4 only (aa 35–285, inclusive = 251 residues). The sequence is
  subset in analyze.py using 0-indexed Python slicing: `seq[34:285]` (positions 35–285, 1-indexed).
  The stalk (aa 286–353) and GPI propeptide (aa 354–381) are excluded from all analysis.

## alphafold_P08174_plddt.json — Per-residue pLDDT confidence scores
- **Source:** Copied verbatim from `experiments/comp-006-daf-cd55-shio-koji-protease-stability/inputs/alphafold_P08174_plddt.json`
- **Original source:** AlphaFold Protein Structure Database (EMBL-EBI),
  https://alphafold.ebi.ac.uk/files/AF-P08174-F1-confidence_v6.json (fetched 2026-05-05)
- **Model:** AF-P08174-F1, version 6 (381 residues)
- **Subset in comp-012:** analyze.py filters the full-sequence pLDDT dict to keys 35–285 inclusive
  before passing to library functions. Full-sequence stats are NOT computed; only the SCR1–4 window
  (251 residues) is analyzed.

## protease_specificities.json — Koji protease rules + shio-koji conditions
- **Source:** Copied verbatim from `experiments/comp-006-daf-cd55-shio-koji-protease-stability/inputs/protease_specificities.json`
- **Shared input:** Same three A. oryzae proteases (ALP, NPr, acid_protease), same shio-koji conditions
  (17.5% NaCl midpoint, pH 4.5–5.0, 22°C, 14–30 days) used in comp-001, comp-005, and comp-006.
- **Sources:** MEROPS database release 12.4; Tominaga & Tsujisaka 1976 (NPr); Ikeda et al. 1975 (ALP);
  Koaze et al. 1964 (acid protease)
- See `comp-001/inputs/provenance.md` for full citations

## Relationship to comp-006
- comp-012 is a direct follow-on to comp-006 (DAF/CD55 full ectodomain, aa 35–353, verdict: HIGH).
- The comp-006 analysis identified the Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52) as the sole
  driver of the HIGH verdict; SCR1–4 domains (aa 35–285) contributed zero exposed sites.
- comp-012 tests the stalk-truncated construct to confirm whether removing the stalk lowers the verdict.
- All structural interpretation in comp-012 cross-references comp-006 as the baseline.
