# Provenance — comp-047

## Structural inputs inherited from comp-032

### `alphafold_Q9UNQ0_model_v6.pdb`

- Source: AlphaFold Protein Structure Database,
  `https://alphafold.ebi.ac.uk/files/AF-Q9UNQ0-F1-model_v6.pdb`, fetched
  2026-05-16.
- Model: AF-Q9UNQ0-F1 v6, full-length 655-residue ABCG2 monomer.
- Q141 CA pLDDT in the committed confidence artifact: 97.06.
- Boundary: this is an apo monomer. It does not represent the physiological
  ATP-bound NBD dimer or a Q141K folding intermediate.

### `Q9UNQ0.fasta` and `alphafold_Q9UNQ0_confidence_v6.json`

- UniProt Q9UNQ0, ABCG2_HUMAN, 655 residues.
- UniProt identifies rs2231142 as p.Gln141Lys and places residue 141 in the
  nucleotide-binding domain.

### `fda_approved_drug_library.json`

- Hand-curated for comp-032 and retained as the identity, class-label, and
  control-role set.
- The comp-032 descriptors and `class_prior` are not used in COMP-047 scoring.

## Frozen derived inputs

### `work/ligands/smiles_resolved.json`

- 134 library names plus novobiocin were resolved through PubChem PUG-REST on
  2026-07-14; 135/135 entries contain a SMILES and PubChem CID.
- The file is frozen for this correction. Re-querying PubChem would create a
  new input snapshot and require a new pre-run gate.

### `work/receptor/`

- `prep_receptor.py` cleaned the AlphaFold structure and created the static
  GLN141→LYS141 side-chain substitution.
- Open Babel 3.1.1 produced the rigid receptor PDBQT files with `-xr -p 7.4`.
- `verify_receptors.py` independently checks the exact committed hashes,
  atom/residue counts, residue-141 identities, clean-structure difference
  scope, and grid geometry against `inputs/receptor_expected.json`.
- Declared warning: Open Babel renamed terminal SER655 to `UNK` in both PDBQT
  files. No other nonstandard PDBQT residue name is accepted by the verifier.

### Original docking and sensitivity artifacts

- `outputs/results.json`: original Vina result, seed 20260714, exhaustiveness 8,
  CPU 4; 135 attempted molecules and 134 complete score rows.
- `outputs/sensitivity.json`: recorded fold-site perturbations for box centers,
  box sizes, Vina seeds, and ligand protonation. The exact center panel is
  x +2 Å, x -2 Å, y +2 Å, and one +3 Å xyz diagonal. It omits y -2 Å and both
  z directions, and it does not perturb the Walker-A box or recompute the
  complete fold-versus-transport margin rule.
- This correction consumes both as frozen result-bearing artifacts. It does not
  re-dock.

## Axis 2 exclusion evidence

### ChEMBL

- Target: CHEMBL5393, ABCG2/BCRP, UniProt Q9UNQ0.
- `outputs/chembl_axis2.json` is a bounded per-molecule inhibition/bioactivity
  check, not a full-library transport-substrate catalog.
- An absent ChEMBL activity record is not evidence that a molecule lacks an
  ABCG2 substrate relationship.

### UniProt/DrugBank relationship set

- `outputs/drugbank_substrate_axis.json` records DrugBank identifiers exposed
  as ABCG2 cross-references by the UniProt Q9UNQ0 flat file.
- The source establishes an ABCG2 relationship/interactor flag. It does not
  prove that all 286 cross-referenced drugs are substrates, and the executable
  merge does not relabel them as such.
- The relationship flag is used as conservative exclusion evidence because the
  screen's stated requirement is no known ABCG2 interaction that could confound
  urate transport.

### Rosuvastatin

- The current FDA CRESTOR label states that rosuvastatin is a substrate of BCRP
  and OATP1B1:
  `https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/021366s047lbl.pdf`.
- That primary label supports the independent substrate exclusion. The
  UniProt/DrugBank relationship flag is corroborating relationship evidence,
  not the sole substrate proof.

### Vorinostat

- Basseville et al. reported increased Q141K ABCG2 expression, improved
  cell-surface trafficking, and improved substrate efflux after vorinostat,
  romidepsin, or panobinostat treatment (**In Vitro**; PMID 22472121,
  PMCID PMC4163836).
- This is phenotypic rescue evidence. It does not establish direct binding to
  the modeled residue-141 pocket and is not used to validate the docking rank.

## Historical toolchain record

- Python 3.13
- RDKit 2026.03.3
- Open Babel 3.1.1
- AutoDock Vina 1.2.5
- Meeko, Biopython, NumPy, SciPy, and Gemmi were present, but exact committed
  versions are not available for all packages.

This is provenance for the historical run, not a claim that an exact current
environment exists. Any new docking run must pin a rebuilt environment and pass
a new lifecycle gate. Its reviewed design must preserve raw docking output
separately from postprocessing, hash-bind prepared ligands and source SMILES,
capture every Vina return code/stdout/stderr, and snapshot live-query requests
and responses before interpretation.
