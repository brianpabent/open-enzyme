# COMP-001 — Q00511 Legacy Preference-Filter and pLDDT-Context Audit

**Question:** Which adjacent residue pairs in *Aspergillus flavus* uricase (Q00511) match three fixed legacy preference filters, and what AlphaFold confidence surrounds each match?

**Decision boundary:** This COMP supplies an auditable inventory of fixed filter matches and pLDDT context. The legacy arrays do not have claim-level provenance and are not treated as exhaustive protease specificity rules. The computation does not model solvent accessibility, cleavage probability, exposure time, protease concentration, retained activity, or fermentation survival. It cannot issue a LOW/MODERATE/HIGH protease-risk verdict. The empirical [§1.10 shio-koji retained-activity assay](../../../validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) remains the feasibility gate for every possible result.

## Planned computation

1. Load and validate the fixed Q00511 sequence and the reviewed position–residue–pLDDT mapping.
2. Load three legacy Boolean preference filters. A nonempty list is an inclusion filter; an empty list leaves that side of the adjacent pair unrestricted.
3. Enumerate every adjacent pair satisfying each fixed filter.
4. For each pair, report pLDDT over an inclusive window containing P1 and P1' plus up to three flanking residues on each side. Boundary windows truncate at the sequence termini.
5. Emit filter arrays, pair positions, exact window bounds, residue counts, and unrounded calculation values.
6. Emit no biological recognition claim, accessibility class, risk score, survival prediction, or fermentation verdict.

The script is self-contained. It validates canonical sequence and filter residues, uniqueness and schema constraints, finite pLDDT values in `[0,100]`, exact positions, the Q00511 sequence hash, and the reviewed position–residue–pLDDT mapping hash. Built-in checks cover the first peptide bond, an internal bond, and the terminal K301/L302 pair so residue 302 cannot be dropped from its window.

## Result and sensitivity map

All possible results have the same verdict:

> **PROXY ONLY — EMPIRICAL PROTEASE RISK UNRESOLVED**

This is an exact enumeration of fixed inputs, so no inferential sensitivity analysis is planned. A different preference-filter encoding or pLDDT window width is a new design requiring its own pre-run review. Neither favorable nor unfavorable descriptive output can convert §1.10 from feasibility testing to confirmation.

## Reproduce

```bash
python3 analyze.py
```

Requirements: Python 3.8+ and the committed inputs; no third-party packages. Run twice and require byte-identical outputs.

## File index

```text
inputs/
  Q00511.fasta
  alphafold_Q00511_plddt.json
  legacy_preference_filters.json
  provenance.md
outputs/
  cleavage_sites.json
  summary.md
reviews/
  pre-run.manifest.json
  pre-run.md
  post-run.manifest.json
  post-run.md
analyze.py
README.md
```

## Canonical and downstream surfaces

- Interpretive evidence home: [`wiki/uricase-protease-stability-computational.md`](../../../uricase-protease-stability-computational.md)
- Tracking index: [`wiki/computational-experiments.md`](../../../computational-experiments.md)
- Empirical gate: [`wiki/validation-experiments.md` §1.10](../../../validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment)
- Direct UOX dependent: [`wiki/uricase-shio-koji-thermal-stability-computational.md`](../../../uricase-shio-koji-thermal-stability-computational.md)

Before post-run review, search the active corpus for COMP-001-derived accessibility, burial, LOW-risk, survival, and “confirmation experiment” claims. Correct direct UOX dependents in this batch. Shared-proxy conclusions for other payloads remain separately reviewable under their own COMP queue items; they must not use COMP-001 as a validated benchmark.
