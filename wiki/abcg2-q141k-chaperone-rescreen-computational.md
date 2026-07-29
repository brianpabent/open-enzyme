---
title: "ABCG2 Q141K Pharmacological-Chaperone Re-screen — Computational Analysis (comp-047)"
date: 2026-07-14
tags:
  - abcg2
  - q141k
  - pharmacological-chaperone
  - autodock-vina
  - docking
  - drug-repurposing
  - computational-experiment
  - null-result
related:
  - abcg2-q141k-chaperone-screen-computational.md
  - abcg2-modulators.md
  - chassis-pending-interventions.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "UniProt Q9UNQ0 (ABCG2_HUMAN)"
  - "AlphaFold AF-Q9UNQ0-F1-model_v6"
  - "AutoDock Vina 1.2.5"
  - "ChEMBL CHEMBL5393 (ABCG2/BCRP)"
  - "FDA CRESTOR label 2026 — rosuvastatin is a BCRP substrate"
  - "Basseville et al. 2012, PMID 22472121 — Q141K rescue by selected HDAC inhibitors"
---

# ABCG2 Q141K pharmacological-chaperone re-screen (comp-047)

## Question

Can this static-receptor docking configuration rank an FDA-approved molecule for
Q141K ABCG2 trafficking rescue after known ABCG2 relationships are excluded?

The run attempted 135 molecules; 134 produced complete docking-score rows, and
cyclosporine A did not. It compared a modeled region around residue 141 with a
Walker-A box, then applied a separate ABCG2 exclusion layer. The scores are
computational triage signals, not binding, folding, trafficking, or
urate-transport measurements.

## Verdict: inconclusive — no defensible docking-backed ranking

After both exclusion checks, the executable result contains **0 `yes` rows and
1 `uncertain` row: vorinostat**. Rosuvastatin was the other original
`uncertain` docking-tier row, but it is excluded because the
[FDA CRESTOR label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/021366s047lbl.pdf)
identifies it as a BCRP substrate and the UniProt/DrugBank relationship set also
flags it.

Vorinostat's margin is small and its position is not robust enough to make it a
docking-backed wet-lab priority. It has a separate reason to appear in the
validation assay: Basseville et al. reported increased Q141K ABCG2 expression,
surface trafficking, and substrate efflux after vorinostat treatment
(**In Vitro**; [PMID 22472121](https://pubmed.ncbi.nlm.nih.gov/22472121/)).
That phenotypic precedent does not establish direct binding to the modeled site
or validate the docking row.

The result invalidates the ranking configuration. It does **not** invalidate
the Q141K rescue route or establish that no druggable rescue site exists.

## Why the ranking is not decision-usable

### The modeled system does not represent the rescue mechanism

Q141K was modeled as a static side-chain substitution in an AlphaFold apo
monomer. A pharmacological chaperone acts on a folding-competent state or
ensemble. This experiment does not model a folding intermediate, folding
free-energy change, mutant-selective stabilization, the ATP-bound ABCG2 dimer,
or intracellular exposure at the folding compartment.

The residue-141 box is a local structural region, not an experimentally
validated pocket. The Walker-A box is neither the physiological composite ATP
site nor the transmembrane substrate cavity. Their score difference therefore
does not establish a selective fold-site interaction.

### The base ordering is unstable

The recorded sensitivity run re-docked only the Q141K fold-site box. Its
limited panel used x +2 Å, x -2 Å, y +2 Å, one +3 Å xyz diagonal, two box
sizes, two alternate Vina seeds, and a neutral-ligand condition. It did not
test y -2 Å, either z direction, the Walker-A box, or the complete executable
margin rule. Across its non-base perturbations, **2–7 of the eight tracked
candidate positions changed**. That makes the base-run fold ordering
descriptive for this setup, not a robust shortlist. It does not prove that a
pocket is absent or establish robustness of the complete classification.

### There is no ABCG2 chaperone positive control

The four CFTR correctors are cross-protein chaperone mechanism comparators.
None reached the executable tier. Because they are not validated ABCG2
fold-site binders, this is a setup diagnostic—not a sensitivity estimate for
ABCG2 chaperones.

The curated ABCG2 inhibitor/substrate controls remain excluded. That shows the
declared exclusion layer functions for those controls; it does not validate the
fold-site ranking.

## Evidence-axis boundary

- **Axis 1:** frozen Vina scores and the original transparent docking tier.
- **Axis 2a:** bounded ChEMBL ABCG2 activity checks. No ChEMBL record is not
  evidence of no transporter relationship.
- **Axis 2b:** UniProt-exposed DrugBank ABCG2 relationship flags, used as
  conservative exclusions. A flag is not relabeled as proof that every listed
  molecule is a substrate.
- **Independent substrate evidence:** the FDA label establishes rosuvastatin's
  BCRP-substrate status.

Axis 2 can exclude a row. It cannot promote a survivor or establish
pharmacological rescue.

## Receptor-integrity result

The frozen WT and Q141K PDB/PDBQT files and grid boxes pass exact SHA-256,
atom/residue-count, residue-141, mutation-scope, and geometry checks. The clean
WT and Q141K structures differ only at residue 141.

The verifier records one declared preparation warning: Open Babel renamed
terminal SER655 to `UNK` in both PDBQT files. This symmetric warning does not
repair the missing score-to-receptor provenance of the historical docking run
and does not justify retroactive re-docking for this inconclusive result.

## Decision and next observation

- Do not use the comp-032 class-prior list or COMP-047 base-score ordering to
  choose a compound.
- Preserve the direct-chaperone route as an unvalidated hypothesis.
- Treat vorinostat, romidepsin, panobinostat, valproate, and tubastatin according
  to their independent Basseville control roles—not according to COMP-047 rank.
- Resolve the route in
  [validation experiment §1.22](./validation-experiments.md#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue):
  Q141K surface trafficking, ABCG2-attributed urate flux, direct inhibition,
  intracellular exposure, viability, and barrier integrity.

Another pass through the same static docking configuration is not the next
experiment. A future folding-ensemble or ΔΔG model would be a new computational
experiment with its own lifecycle.

## Artifact

[Experiment README](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/) ·
[machine result](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/results.json) ·
[summary](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md) ·
[control read-out](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md) ·
[receptor verification](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/receptor_verification.json)
