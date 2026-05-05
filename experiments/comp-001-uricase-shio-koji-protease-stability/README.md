# comp-001 — Uricase Shio-Koji Protease Stability

**Question:** Will *A. flavus* uricase (Q00511) survive the protease environment of a shio-koji ferment (15–20% NaCl, pH 4.5–5.0, RT, 7–14 days) with meaningful activity retained?

**Short answer:** Computational analysis predicts **low risk**. All protease recognition sites are in confidently-folded regions (100% of residues pLDDT > 80). Combined with strong salt inhibition of the dominant protease (ALP retains ~19% activity at shio-koji NaCl concentrations), the structural evidence argues against significant proteolytic degradation.

**Verdict:** §1.10 wet-lab stability experiment should still run — this analysis shifts the prior from "unknown" to "probably fine," reframing §1.10 as confirmation rather than feasibility gate.

## How to reproduce

```bash
python3 analyze.py
# Outputs: outputs/cleavage_sites.json, outputs/summary.md
```

Requirements: Python 3.8+, stdlib only (json, pathlib, os). No packages to install.

## Re-running with updated data

- **New AlphaFold model:** Download updated PDB from `https://alphafold.ebi.ac.uk/files/AF-Q00511-F1-model_v<version>.pdb`, re-extract pLDDT values into `inputs/alphafold_Q00511_plddt.json`, update `inputs/provenance.md`, re-run.
- **Updated protease specificities:** Edit `inputs/protease_specificities.json` and update `_source` field with new MEROPS reference.
- **Different protein:** Replace `Q00511.fasta` and `alphafold_Q00511_plddt.json` with inputs for the new target.

## File index

```
inputs/
  Q00511.fasta                    UniProt sequence (fetched 2026-05-05)
  alphafold_Q00511_plddt.json     Per-residue pLDDT from AlphaFold v6 PDB (fetched 2026-05-05)
  protease_specificities.json     P1/P1' rules + salt inhibition data (MEROPS + primary literature)
  provenance.md                   Data sources, fetch dates, version notes
outputs/
  cleavage_sites.json             Full machine-readable results
  summary.md                      Human-readable findings — this is the artifact cited in the wiki
analyze.py                        Analysis script
README.md                         This file
```

## Wiki links

- Interpretive page: [`wiki/uricase-protease-stability-computational.md`](../../wiki/uricase-protease-stability-computational.md)
- Tracking index: [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md)
- Wet-lab experiment this informs: [`wiki/validation-experiments.md` §1.10](../../wiki/validation-experiments.md)
- Platform context: [`wiki/koji-endgame-strain.md`](../../wiki/koji-endgame-strain.md)
