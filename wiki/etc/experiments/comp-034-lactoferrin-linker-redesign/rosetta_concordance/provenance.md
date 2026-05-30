# Provenance — comp-034 Rosetta concordance leg

## Tooling
- **PyRosetta** `2026.3+releasequarterly.5e498f1409` (cp313, macOS arm64), installed
  2026-05-29 from `https://west.rosettacommons.org/pyrosetta/quarterly/release` under
  the Rosetta & PyRosetta Software Non-Commercial License Agreement (credential-free;
  UW CoMotion academic-license update, K. Brede 2026-05-29). Commercial use requires a
  separate paid UW license.
- Score functions: `ref2015_cart` (Cartesian ΔΔG, method 1), `ref2015` (sanity), DSSP
  via `core.scoring.dssp.Dssp.get_dssp_secstruct()`, SASA via
  `core.scoring.sasa.SasaCalc`.
- Python 3.13.7, stdlib + PyRosetta only. No torch/ESM dependency (the ESMFold route
  was blocked — see README Caveats).

## Inputs (all mirrored from the comp-034 experiment dir — read-only)
- `../proteinmpnn_rerun/AF-P02788-F1-model_v6.pdb` — AlphaFold monomer, 710 residues,
  linker CA at 353–363 verified to match WT `SEEEVAARRAR`.
- `../inputs/P02788.fasta`, `../inputs/alphafold_P02788_plddt.json` — comp-005 mirrors.
- `../../comp-005-lactoferrin-shio-koji-protease-stability/inputs/protease_specificities.json`
  — canonical koji-protease P1/P1′ table (read-only).
- Helix retention per variant read from `rosetta_ddg_results_torsion3.json` /
  recomputed per-variant in `refold_via_relax.py`.

## Candidate set (6) — verified against comp-034 outputs + proteinmpnn_rerun
- WT `SEEEVAARRAR`; `V357P` → `SEEEPAARRAR`; `S353E+V357P` → `EEEEPAARRAR`;
  MPNN-native `NEEEQQQEEEQ` and `NEEEQEEQDQQ` (from `proteinmpnn_rerun/shortlist_mpnn.json`);
  aggressive multi-proline `EEEEPAAPPAP`. All length-11, flanking residues 352/364 fixed.

## Pre-commit verification (CLAUDE.md Rule 4)
Every load-bearing number in README.md is read directly from a results JSON in this
directory (not transcribed from memory):
- Cartesian ΔΔG (+0.23 / +2.39 / +20.11 / +21.26 / +57.48) ← `rosetta_ddg_results_cartesian10.json` `ddG_min_REU`.
- Helix fractions (0.818 / 0.727 / 0.364) ← same file `linker_helix_frac_at_min` and `refold_via_relax_results.json` `helix_frac_real` (cross-agree).
- Structure-gated cleavage real (0.388 / 0.943 / 1.041 / 1.104 / 1.143) ← `refold_via_relax_results.json`.
- WT SASA exposure (8 exposed / 3 partial / 0 buried) ← `structure_gated_cleavage.py` console table; pLDDT 93–98 ← `../inputs/alphafold_P02788_plddt.json`.

## Bugs found + fixed during the run (recorded so the next user doesn't re-hit them)
1. **Space-in-path PDB load failure.** Rosetta's file reader fails on paths containing
   spaces (the repo lives under `.../Open Enzyme/...`). Fix: `staged_pdb()` copies the
   PDB to a spaceless temp dir before `pose_from_pdb`.
2. **DSSP accessor.** `Dssp.dssp_reduced()` + `pose.secstruct()` silently returned
   all-loop on this build; `Dssp.get_dssp_secstruct()` is correct (linker = `LHHHHHHHHHL`).
3. **`pyrosetta.rosetta.basic.version.version()`** does not exist on this build; use
   `pyrosetta._version_string()`.

## Methodological flag (affects other comp-NNNs)
The pLDDT-as-accessibility proxy in `lib/protease_stability.py` mis-classifies
confidently-predicted exposed regions as buried. This affects every comp-NNN using that
model (comp-001/005/006/012/037). Flagged in the library docstring and in
`autonomous-screening-methodology.md` (a second instance of the comp-022 proxy-quality
lesson: a cheap proxy can be near-uncorrelated with the real biophysical quantity).
