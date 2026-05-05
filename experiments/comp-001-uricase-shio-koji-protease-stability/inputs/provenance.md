# Input Provenance — comp-001

| File | Source | Version / Date fetched | URL |
|---|---|---|---|
| `Q00511.fasta` | UniProt REST API | UniProt release 2025_03; fetched 2026-05-05 | https://rest.uniprot.org/uniprotkb/Q00511.fasta |
| `alphafold_Q00511_plddt.json` | AlphaFold Protein Structure Database (EMBL-EBI); B-factor column of PDB file = per-residue pLDDT confidence score | AlphaFold v6 model; fetched 2026-05-05 | https://alphafold.ebi.ac.uk/files/AF-Q00511-F1-model_v6.pdb |
| `protease_specificities.json` | Hand-encoded from MEROPS database entries + primary literature (see file `_source` field) | MEROPS release 12.4; encoded 2026-05-05 | https://www.ebi.ac.uk/merops/ |

## Protein identity
- **UniProt accession:** Q00511
- **Protein name:** Uricase (urate oxidase), *Aspergillus flavus*
- **Gene:** uaZ
- **Length:** 302 amino acids (mature form)
- **Evidence level:** Reviewed (Swiss-Prot, PE=1 experimental evidence)
- **Relevance:** Primary uricase candidate for Open Enzyme koji expression (see `wiki/uricase-variant-selection.md` and `wiki/koji-endgame-strain.md` §2.1)

## AlphaFold model notes
- Model: AF-Q00511-F1-model_v6 (AlphaFold2, latest release as of fetch date)
- pLDDT = per-residue Local Distance Difference Test score (0–100); stored in B-factor column of PDB ATOM records
- Interpretation: >90 = very high confidence (well-folded core); 70–90 = confident; 50–70 = low confidence (may be disordered); <50 = likely disordered/unstructured
- Mean pLDDT observed: 97.1 (highly unusual — essentially all residues confidently folded)

## Protease specificity notes
- Specificities encoded from published biochemical characterization, not computational prediction
- P1 / P1' notation: P1 = residue N-terminal to cleavage site; P1' = residue C-terminal to cleavage site
- Salt inhibition values are approximate (±15%) based on original literature; exact values depend on assay conditions
- The acid protease (aspergillopepsin I) is partially active at shio-koji pH ~4.5–5.0 (upper edge of its range); residual activity at this pH estimated at ~20–40% of pH-optimal activity
