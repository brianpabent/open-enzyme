# comp-047 — ABCG2 Q141K pharmacological-chaperone re-screen

**Status:** Phase 0 — Research & Design. Computational triage only. **Held for human review before any corpus integration.**
**Supersedes:** comp-032 (frozen as a flawed record; see the 2026-07-13 independent push review).
**Date:** 2026-07-14.

## Single decision this experiment answers

Which FDA-approved molecules are credible **ABCG2 Q141K pharmacological-chaperone**
candidates — predicted to bind a **fold-stabilizing NBD site** (NOT the
transport/ATP pocket) AND **not already known ABCG2 inhibitors/substrates** —
worth a wet-lab Q141K trafficking assay?

Output is an **evidence-grounded ranked shortlist for wet-lab triage**, NOT a
rescue claim. A "candidate" here means "worth a Q141K trafficking + urate-flux
assay," nothing more.

## Why comp-032 was replaced (not relabeled)

Independent audit (2026-07-13) found comp-032's GREEN verdict came from a
hardcoded **drug-class prior** (CFTR correctors = 1.00, decoys = 0.15). Its
"positive-control pass" was tautological (decoy max 0.684 = 0.15^(1/5)). It did
**no docking**, no Q141K side-chain modeling, no chaperone-vs-inhibitor
discrimination, and no sensitivity analysis. ABCG2 *inhibitors* (the opposite of
what we want) scored high. comp-047 rebuilds the screen on two orthogonal,
real-data axes with non-tautological controls and a sensitivity analysis.

## Method — two orthogonal evidence axes, no class prior

### Axis 1 — real docking (AutoDock Vina 1.2.5)
- **Receptor:** comp-032's AlphaFold ABCG2 monomer (Q9UNQ0, v6). Cleaned to
  chain A / standard residues (Biopython), prepared as a rigid PDBQT with Open
  Babel (`-xr -p 7.4`).
- **Q141K model:** static side-chain substitution — backbone + CB/CG/CD kept
  from GLN141, OE1/NE2 dropped, CE/NZ built in extended geometry, re-protonated
  at pH 7.4 (NZ = NH3+). **This is a static-structure proxy, not folding
  thermodynamics** — the acknowledged weakest link (see Limitations).
- **Two grid boxes (22 Å cubic, centers 32.6 Å apart):**
  - `fold_site` — residue-141 side chain + contact shell (137–145). Candidate
    fold-stabilizing site.
  - `transport_site` — Walker A P-loop (80–87). ATP/nucleotide site; strong
    binding here flags an ATP-competitive inhibitor → **disqualifying**.
- **Ligands:** 134 library molecules + 1 appended negative control (novobiocin).
  SMILES resolved from PubChem (the comp-032 library has none). Each ligand:
  Open Babel pH-7.4 protonation → RDKit ETKDGv3 3D embed (seed 42) + MMFF →
  Meeko PDBQT.
- Each ligand docked to **3 site/receptor combinations**: `fold_site@Q141K`,
  `fold_site@WT` (WT/mutant selectivity proxy), `transport_site@WT`.
- **Chaperone-likeness** is expressed with transparent metrics over the real
  Vina numbers — strong fold-site binding AND weak transport-site binding AND
  not a known ABCG2 inhibitor. Exact tier rule in `analyze.py::classify()`. No
  drug-class prior anywhere in the score.

### Axis 2 — empirical ChEMBL grounding
- ABCG2/BCRP target = **CHEMBL5393** (UniProt Q9UNQ0), 1307 human bioactivity
  records. Executed via the bio-research **ChEMBL MCP** (`target_search` +
  `get_bioactivity` + `compound_search`) on the candidate + control set — MCP
  tools are not subprocess-callable, so this axis is run interactively and its
  per-molecule results are transcribed to `outputs/chembl_axis2.json`
  (schema: `{name: {chembl_id, has_activity, best_pchembl, note}}`).
  Known ABCG2 inhibitors/substrates are **disqualified** (they would block urate
  efflux — the confound comp-032 missed).

### Controls (non-tautological — the validation comp-032 lacked)
- **POSITIVE:** CFTR correctors (lumacaftor, tezacaftor, elexacaftor, ivacaftor).
  They must **earn** their rank from docking + ChEMBL, with no prior. Whether
  they do is reported honestly in `outputs/controls.md`.
- **NEGATIVE:** known ABCG2 inhibitors (Ko143, fumitremorgin C, novobiocin,
  tariquidar, elacridar, azoles) + ABCG2 substrates. A valid screen must NOT
  rank these as top chaperone candidates. Where they land is reported.

### Sensitivity analysis (mandatory)
`sensitivity.py` re-docks the top candidates + controls under grid-center
shifts, box-size changes (18/26 Å), alternate Vina seeds, and neutral-vs-pH-7.4
protonation. A candidate that only ranks under one grid choice is not a finding.
Output: `outputs/sensitivity.json`.

## Files

```
inputs/            AlphaFold PDB, FASTA, confidence JSON, drug library, provenance.md
prep_receptor.py   clean WT + build Q141K static substitution + define grid boxes
resolve_smiles.py  PubChem name -> SMILES (+ control role tags, + novobiocin)
analyze.py         Axis 1: ligand prep + Vina docking (3 combos) + tier classification
sensitivity.py     perturbation / rank-stability analysis
build_results.py   merge Axis 1 + Axis 2 -> results.json, controls.md, summary.md
work/              receptor PDBQT, ligand PDBQT, docking poses, boxes.json (regenerable)
outputs/           results.json, sensitivity.json, controls.md, summary.md, chembl_axis2.json
logs/              run.log, full_run.out
```

## Reproduce

```bash
cd wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen
VENV=/private/tmp/.../docking-smoketest/.venv/bin/python   # RDKit+Meeko+obabel venv
# 1. receptor prep + boxes
$VENV prep_receptor.py
$VBIN/obabel work/receptor/abcg2_wt_clean.pdb   -O work/receptor/abcg2_wt.pdbqt   -xr -p 7.4
$VBIN/obabel work/receptor/abcg2_q141k_clean.pdb -O work/receptor/abcg2_q141k.pdbqt -xr -p 7.4
# 2. SMILES (needs network; PubChem)
$VENV resolve_smiles.py
# 3. dock all 135 (Vina 1.2.5, seed 20260714, exhaustiveness 8, cpu 4)
$VENV analyze.py
# 4. sensitivity + merge
$VENV sensitivity.py
$VENV build_results.py
```

Determinism: Vina `--seed 20260714 --cpu 4 --exhaustiveness 8`, RDKit
`randomSeed=42`. Exact affinities depend on (seed, cpu, exhaustiveness); the
tuple is pinned above. Different `--cpu` can shift scores slightly (thread RNG
split) — keep cpu=4 to reproduce exactly.

## Honest limitations (load-bearing — read before citing any number)

1. **Q141K is a static side-chain substitution, not a folding-ΔΔG calculation.**
   A pharmacological chaperone works by stabilizing a folding-competent
   conformation of the mutant. Docking a small molecule into a *static* modeled
   Q141K pocket tests shape/chemical complementarity to that one conformation —
   it does **not** compute whether the molecule lowers the folding free energy or
   rescues trafficking. This is the single weakest link. Treat fold-site
   affinity as a triage signal, not evidence of rescue.
2. **Misfolded-state selectivity is not directly modeled.** A true chaperone
   should preferentially bind the mutant folding intermediate over the native
   protein. The `fold@WT − fold@Q141K` delta is a crude surrogate for this and
   is within Vina's noise for most molecules.
3. **Apo monomer.** ABCG2 is a homodimer; the physiological composite ATP site
   forms across the NBD–NBD interface on dimerization + ATP binding, which this
   monomer does not represent. The `transport_site` box is the Walker A P-loop
   only and tests **ATP-competitive** binding — NOT the transmembrane
   drug/urate cavity where most clinically relevant ABCG2 inhibitors act. Axis 2
   (empirical ChEMBL) is therefore the primary inhibitor filter; the ATP-site
   box is a secondary, mechanism-specific signal.
4. **Vina scores are noisy** (commonly ±1–2 kcal/mol vs experiment). Use ranks,
   not absolute affinities. Small margins between molecules are not meaningful.
5. **Blind-ish local docking.** Grid boxes are anchored on sequence/structure
   landmarks, not on an experimentally validated pocket. The fold-site is a
   region, not a known druggable cavity — a favorable score does not prove a
   real binding pocket exists there in the folded protein.
6. **Physiological exposure not modeled** — no intracellular free concentration,
   ER-lumen access during folding, tissue distribution, dose, or Cmax. Even a
   real binder must reach the NBD at a rescuing concentration in enterocytes/
   renal cells; that is untested here.

## What comp-047 does NOT establish
Binding affinity in the physiological sense, folding rescue, Q141K-vs-WT
selectivity, ATP-independence, urate-flux effect, or wet-lab priority beyond
"worth an assay." Those require the wet-lab Q141K trafficking + urate-flux +
ABCG2-inhibition counterscreen registered as a new validation experiment.

## Verdict

See `outputs/summary.md` (verdict + ranked shortlist) and `outputs/controls.md`
(the control-based validity check). Corpus integration superseding comp-032 is
**deliberately held** until a human reviews this verdict.
