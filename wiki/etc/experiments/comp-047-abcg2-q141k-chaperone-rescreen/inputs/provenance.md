# Provenance — comp-047 inputs

comp-047 re-screens the same biological question as comp-032 but replaces the
descriptor/class-prior heuristic with **real AutoDock Vina docking + empirical
ChEMBL grounding**. Structural inputs are inherited unchanged from comp-032;
the drug library is reused for *identity/descriptors only* — SMILES were newly
resolved because comp-032's library contains none.

## Inherited from comp-032 (unchanged)

### alphafold_Q9UNQ0_model_v6.pdb — WT ABCG2 AlphaFold model
- Source: AlphaFold Protein Structure Database (EMBL-EBI),
  https://alphafold.ebi.ac.uk/files/AF-Q9UNQ0-F1-model_v6.pdb (fetched 2026-05-16, via comp-032)
- Model: AF-Q9UNQ0-F1 v6, monomer, full 655 aa. Q141 CA pLDDT 97.06.
- **Caveat (load-bearing):** this is an **apo monomer**. ABCG2 functions as a
  homodimer and the physiological composite ATP site forms across the NBD-NBD
  interface upon dimerization. In this monomer the Walker A motif (80-87) and
  the second ATP-binding loop (184-190) are ~35 A apart — the composite
  nucleotide site is NOT formed. The transport-site grid box is therefore
  centered on the Walker A P-loop alone (see below).

### Q9UNQ0.fasta / alphafold_Q9UNQ0_confidence_v6.json
- UniProt sp|Q9UNQ0|ABCG2_HUMAN (655 aa) and AlphaFold per-residue pLDDT.
- Q141K variant rs2231142 (c.421C>A, p.Gln141Lys): "associated with high serum
  urate and increased gout risk; lower urate transport; decreased protein
  abundance" (UniProt VARIANT). Position 141 is in the NBD.

### fda_approved_drug_library.json — 134-molecule identity/descriptor set
- Hand-curated (comp-032, 2026-05-16). **Used here only for molecule identity,
  drug_class, and control role tagging.** comp-047 does NOT use comp-032's
  physicochemical descriptors or `class_prior` field for scoring — those were
  the source of comp-032's invalid class-prior verdict.

## New in comp-047

### work/ligands/smiles_resolved.json — SMILES (newly resolved)
- comp-032's library has **zero SMILES**. Each of the 134 names + 1 appended
  negative control (novobiocin) was resolved to an isomeric SMILES via
  **PubChem PUG-REST** (`/compound/name/<name>/property/IsomericSMILES/JSON`),
  fetched 2026-07-14. 135/135 resolved; all RDKit-parseable. CIDs recorded.
- A small alias table handles non-standard names (e.g. `geldanamycin_17_aag`
  -> tanespimycin; `ko143` -> "Ko143"; `egcg` -> epigallocatechin gallate). See
  `resolve_smiles.py`.
- Control role tags (`role_tag`):
  - `cftr_corrector` (n=4): ivacaftor, tezacaftor, elexacaftor, lumacaftor —
    POSITIVE controls. Must EARN rank from docking, no prior.
  - `abcg2_inhibitor` (n=13): ko143, fumitremorgin_c, tariquidar, elacridar,
    ketoconazole, itraconazole, cyclosporine_a, novobiocin, and the ABCG2
    substrates mitoxantrone, topotecan, etoposide, sulfasalazine, methotrexate —
    NEGATIVE controls. Must NOT rank as top chaperone candidates.

### work/receptor/ — prepared receptors + grid boxes
- `abcg2_wt_clean.pdb` / `abcg2_q141k_clean.pdb`: chain A, standard residues,
  hydrogens/altlocs stripped (Biopython). Q141K built by **static side-chain
  substitution** (see `prep_receptor.py` header + README limitations).
- `abcg2_wt.pdbqt` / `abcg2_q141k.pdbqt`: rigid receptor PDBQT via **Open Babel
  3.1.1** (`-xr -p 7.4`; AutoDock atom types C/A/N/NA/OA/HD/S). Meeko's
  polymer/template receptor path failed on this AlphaFold model
  (H-reconciliation error); Open Babel is the robust fallback and is a standard
  Vina receptor-prep route. (Ligands use RDKit+Meeko; see README.)
- `boxes.json`: two 22 A cubic grid boxes —
  - `fold_site` center [1.09, 12.03, 10.33] (residue-141 side chain + contact
    shell 137-145) — candidate fold-stabilizing NBD site.
  - `transport_site` center [-21.76, -11.11, 12.75] (Walker A P-loop 80-87) —
    ATP/nucleotide site; docking here flags an ATP-competitive inhibitor.
  - Center separation 32.6 A (well-separated → fold-vs-transport contrast is
    meaningful).

### ChEMBL (Axis 2, live via bio-research MCP)
- Target ABCG2/BCRP = **CHEMBL5393** (single protein, UniProt Q9UNQ0),
  resolved 2026-07-14. 1307 human ABCG2 bioactivity records available; used to
  empirically confirm/refute known ABCG2 activity for candidates + controls
  (`chembl_axis2.json`).

## Toolchain
- Python 3.13 venv: RDKit 2026.03.3, Meeko, Open Babel 3.1.1 (openbabel-wheel),
  scipy, gemmi, biopython.
- AutoDock Vina 1.2.5 (x86_64 via Rosetta 2).
- Determinism: Vina `--seed 20260714 --cpu 4 --exhaustiveness 8`; RDKit ETKDGv3
  `randomSeed=42`. Exact scores depend on (seed, cpu, exhaustiveness) — all
  pinned in the repro command (README).
