PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 0d309f67efc46529fc8d2a61fe31dbf60c28461aeca4d2c318685b3f7aa93b49

# Adversarial pre-run review — comp-047

## Reviewed snapshot

The exact manifest check passed for 22 design files and seven frozen
prior-output baselines, including `outputs/receptor_verification.json`.

Relative to the approved `9cba1e…` snapshot, README is the only changed design
file; all experiment code, inputs, parameters, receptor artifacts, rules, and
planned outputs retain their reviewed hashes. Reviewer `/root/comp047_gate1`
read the amended README and inspected the relevant semantics in both newly
authorized process dependents. The reviewer made no edits and performed no
result-bearing execution.

## Bottom-line verdict

The nine-surface propagation contract is appropriate and narrowly scoped. The
two additions are direct reusable dependents of the corrected finding and
currently encode the substrate-typing error COMP-047 is correcting.

This scope change does not alter the experiment question, implementation,
result interpretation, or prior GO verdict. No new docking or result-bearing
rerun is required.

## Question and model fit

The design still asks whether the exact frozen COMP-047 run supports a
reproducible docking-backed ranking after both ABCG2 evidence checks and
receptor-integrity checks.

It does not claim binding, molecular chaperoning, transport rescue, relationship
subtype, or clinical efficacy. The result remains a setup-bounded failure of the
ranking configuration rather than a rejection of the Q141K rescue hypothesis.

## Constraint and implementation audit

- All 21 non-README design-file hashes are unchanged from the prior approved
  snapshot.
- The authoritative build still performs fail-closed receptor verification
  before corrected-report processing.
- Axis 2a remains a bounded conservative exclusion screen.
- Axis 2b remains the UniProt-exposed DrugBank ABCG2 relationship exclusion; it
  is not substrate-subtype proof or positive rescue evidence.
- The `chembl-cross-check.md` delta corrects source-selection guidance that
  treats generic DrugBank cross-references as substrate annotations.
- The `target_interactors.py` delta corrects a shared helper whose documentation,
  output names, metadata, and union rule make the same unsupported subtype
  assignment.
- Both additions require independent evidence for substrate typing while
  preserving generic relationship flags as conservative exclusions.

## Load-bearing pre-run table

| Item | Reviewed conclusion |
|---|---|
| Exact manifest | Passed at `0d309f…` |
| Experiment design delta | README propagation contract only |
| Code/input/model delta | None |
| Frozen receptor identity | Unchanged from prior approved review |
| Axis 2 semantics | Relationship evidence may exclude; it cannot establish subtype |
| Added process dependents | Necessary to prevent recurrence |
| Generated outputs | Seven frozen prior baselines for Gate 2 |
| New docking or result execution | Not required |

## Falsification, sensitivity, and output contract

The falsification rules, sensitivity interpretation, controls, and
output-generation contract are unchanged. The generated outputs remain
prior-output baselines until Gate 2 reviews the complete artifacts and proposed
interpretations.

## Downstream authoring contract

Propagation is limited to:

1. `index.md`
2. `wiki/abcg2-q141k-chaperone-rescreen-computational.md`
3. `wiki/computational-experiments.md`
4. `wiki/abcg2-q141k-chaperone-screen-computational.md`
5. `wiki/chassis-pending-interventions.md`
6. `wiki/abcg2-modulators.md`
7. `wiki/validation-experiments.md` §1.22
8. `wiki/etc/chembl-cross-check.md`
9. `wiki/etc/experiments/lib/target_interactors.py`

The last two changes represent UniProt-exposed DrugBank entries as relationship
flags and require independent evidence before assigning substrate subtype. No
hypothesis card, new intervention page, portfolio reranking, or unrelated
Q141K/butyrate propagation is authorized.

## Required actions before execution

None.

## Review limits

The review reused the prior full audit for exact-hash-unchanged files and read
the complete changed README plus affected portions of the two newly authorized
dependents. Gate 2 remains responsible for the outputs and all nine propagated
changes.
