# comp-047 — ABCG2 Q141K pharmacological-chaperone re-screen

**Phase:** 0 — Research & Design

**Disposition:** INCONCLUSIVE — no defensible docking-backed candidate ranking

**Supersedes:** comp-032's descriptor/class-prior result

## Decision boundary

The original run asked whether an FDA-approved molecule could be prioritized for
Q141K ABCG2 trafficking rescue using a modeled residue-141 fold-site score, a
Walker-A comparison score, and known-ABCG2 exclusion.

This correction asks the narrower question the frozen artifacts can answer:
**does that exact run support a reproducible docking-backed ranking after both
ABCG2 evidence checks and receptor-integrity checks are applied?**

It does not. The executable merge leaves vorinostat as one marginal `uncertain`
row, but that row is not a docking-backed wet-lab priority. Rosuvastatin is
excluded because the FDA label identifies it as a BCRP substrate and the
UniProt/DrugBank relationship set also flags it. The base fold-site ordering is
unstable under the recorded perturbations, the Walker-A comparison does not
separate a selective fold-site signal, and the screen has no validated ABCG2
chaperone positive control.

This is a failure of this ranking configuration, not a failure of the Q141K
rescue hypothesis.

## Frozen evidence consumed by the correction

- `outputs/results.json` — 135 attempted molecules; 134 with complete docking
  scores from the original Vina run.
- `outputs/sensitivity.json` — the original 10-condition perturbation run for
  eight top base-run scores plus comparator/control molecules.
- `outputs/chembl_axis2.json` — bounded ChEMBL ABCG2 inhibition checks plus the
  independently sourced rosuvastatin substrate exclusion.
- `outputs/drugbank_substrate_axis.json` — UniProt-exposed DrugBank ABCG2
  relationship flags. The filename is historical: a flag is treated as
  conservative exclusion evidence, not proof that every flagged drug is a
  substrate.
- `work/receptor/` — exact WT/Q141K PDB and PDBQT intermediates and grid boxes.

The correction does **not** refresh PubChem, prepare new ligands, alter a docking
score, or run another docking campaign.

## Executable rule

`build_results.py` applies two layers:

1. **Axis 1:** retain the original transparent docking tier from the frozen run.
2. **Axis 2 exclusion:** set the final row to `no` when any of these is true:
   curated ABCG2 control, ChEMBL ABCG2 activity, independently identified
   substrate, or UniProt/DrugBank ABCG2 relationship.

Axis 2 can exclude a row. It cannot provide evidence that a surviving molecule
is a pharmacological chaperone.

## Controls and interpretation

The four CFTR correctors are cross-protein chaperone mechanism comparators, not
validated ABCG2 fold-site binders. Their failure to earn a tier shows that this
setup did not recover them; it does not prove that ABCG2 lacks a rescuable site.

The curated ABCG2 inhibitors/substrates are negative controls for the exclusion
layer. Their rejection shows that the declared exclusion logic is functioning,
not that the fold-site ranking is biologically valid.

Vorinostat has direct **In Vitro** Q141K surface-trafficking and efflux-rescue
precedent in Basseville et al. (PMID 22472121). That phenotypic result is
independent of the docking row and does not validate this modeled pocket.

## Files

```text
inputs/
  alphafold_Q9UNQ0_model_v6.pdb
  Q9UNQ0.fasta
  alphafold_Q9UNQ0_confidence_v6.json
  fda_approved_drug_library.json
  provenance.md
  receptor_expected.json
prep_receptor.py          receptor-preparation source for a future new run
resolve_smiles.py         PubChem refresh source for a future new run
analyze.py                original full docking implementation
sensitivity.py            original perturbation implementation
repair.py                 targeted re-dock utility; not used in this correction
verify_receptors.py       exact-hash, count, residue-141, and box verification
build_results.py          deterministic Axis-2 merge and report generation
work/                     frozen receptor and resolved-SMILES intermediates
outputs/
  results.json
  sensitivity.json
  chembl_axis2.json
  drugbank_substrate_axis.json
  receptor_verification.json
  controls.md
  summary.md
```

## Reproduce the approved correction

From this directory:

```bash
python3 build_results.py
shasum -a 256 outputs/results.json outputs/controls.md outputs/summary.md outputs/receptor_verification.json
```

`build_results.py` invokes receptor verification in-process before it reads or
writes the corrected reports. Any receptor-integrity failure stops the merge.
Run the same Python command again. The four hashes must remain identical. The
correction uses only the Python standard library and committed frozen artifacts.

## Full re-docking is outside this correction

The historical full run recorded Python 3.13, RDKit 2026.03.3, Meeko, Open
Babel 3.1.1, Biopython, NumPy, and AutoDock Vina 1.2.5. The old private
environment no longer exists and is not represented as a current lock file.

The source no longer contains machine-private paths. A future authorized
re-dock must supply `OE_VINA_BIN` and `OE_OBABEL_BIN` or place `vina` and
`obabel` on `PATH`, rebuild and pin the complete Python environment, and pass a
new pre-run lifecycle gate. Refreshing `work/ligands/smiles_resolved.json`,
re-preparing receptors, changing parameters, or regenerating any docking score
also starts that new lifecycle.

## Receptor verification boundary

`verify_receptors.py` binds every frozen receptor file and `boxes.json` to an
expected SHA-256, checks atom/residue counts, verifies GLN141→LYS141 atom
identity, and asserts that the clean structures differ only at residue 141.
It can be run alone for diagnosis, but the authoritative correction command
calls it directly and cannot continue after failure.

The PDBQT files carry one declared preparation warning: Open Babel renamed the
terminal SER655 residue to `UNK` in both WT and Q141K files. The warning is
symmetric and does not justify retroactively re-preparing or re-docking this
negative/inconclusive experiment.

## Canonical evidence home and permitted propagation

The canonical reader-facing evidence home is
[`wiki/abcg2-q141k-chaperone-rescreen-computational.md`](../../../abcg2-q141k-chaperone-rescreen-computational.md).
After deterministic execution, propagation is limited to these nine surfaces:

| Surface | Permitted delta |
|---|---|
| `index.md` | Replace the overbroad failed-positive-control summary with the corrected setup-bounded verdict. |
| `wiki/abcg2-q141k-chaperone-rescreen-computational.md` | Own the complete interpretation: rosuvastatin excluded; vorinostat is the sole marginal executable row but not a docking-backed priority; comparator, sensitivity, and receptor limits; §1.22 handoff. |
| `wiki/computational-experiments.md` | Correct the registry and tracking row; remove stale claims that sensitivity did not run and Axis 2 remained thin. |
| `wiki/abcg2-q141k-chaperone-screen-computational.md` | Preserve the comp-032 hypothesis set while replacing ABCG2-positive-control language with cross-protein comparator language. |
| `wiki/chassis-pending-interventions.md` | Preserve the route as an unvalidated small-molecule option, record the corrected COMP-047 boundary, and route empirical resolution to §1.22. |
| `wiki/abcg2-modulators.md` | Distinguish the failed docking ranking from independent **In Vitro** HDAC-directed rescue evidence and link the direct-chaperone question to §1.22. |
| `wiki/validation-experiments.md` §1.22 | Register how direct-chaperone hypotheses enter the existing trafficking, urate-flux, and inhibition-counterscreen protocol. |
| `wiki/etc/chembl-cross-check.md` | Correct the reusable routing rule: UniProt-exposed DrugBank cross-references are conservative relationship flags, not substrate-subtype proof. |
| `wiki/etc/experiments/lib/target_interactors.py` | Make the shared helper emit relationship semantics and require an independent source for substrate typing. |

No hypothesis card, new intervention page, portfolio ranking, or unrelated
Q141K/butyrate page is authorized by this correction. Any broader connection
belongs in a later synthesis decision.

## Load-bearing limitations

1. The Q141K receptor is a static side-chain substitution, not a folding-ΔΔG
   calculation or a folding-intermediate ensemble.
2. The receptor is an apo monomer. The Walker-A box is not the physiological
   composite ATP site or the transmembrane substrate cavity.
3. The fold-site region is a modeled local box, not an experimentally validated
   pocket. Recorded rank instability prevents treating the base ordering as
   robust.
4. Vina scores and close score margins are not binding-affinity measurements.
5. Intracellular free exposure at the folding compartment is not modeled.
6. UniProt/DrugBank cross-references establish a curated ABCG2 relationship;
   they do not by themselves establish the relationship subtype for every drug.

## Next discriminating observation

Use [validation experiment §1.22](../../../validation-experiments.md#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue):
reproduce the Basseville control pattern, then measure Q141K surface trafficking,
ABCG2-attributed urate flux, direct transporter inhibition, intracellular
exposure, viability, and barrier integrity. Another pass through this static
docking setup is not the next experiment.
