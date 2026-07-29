ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 05779a45f1f2845c53c4564317aa63a1834b4ce484f6adbbbd9028d9c99c5d12

# Independent comp review — comp-047

## Reviewed snapshot

Reviewer `/root/comp047_gate2_20260729`; authoring-time post-run manifest
canonical SHA-256
`05779a45f1f2845c53c4564317aa63a1834b4ce484f6adbbbd9028d9c99c5d12`.
The repository checker recomputed that digest and matched every manifest-bound
path, byte count, and file hash: 23 design files, seven generated outputs, and
three proposed updates. I inspected every entry before consulting historical
receipts.

The Gate-1 receipt is `PRE_RUN_GATE: GO` at canonical digest
`ac3bc8da40096a64c3c2c0f8e7cafd4fb01b2f937a9411bbea08c8cab0089fc0`.
The 23 pre/post design records are identical by path, byte count, and SHA-256.
The post-run receipt is excluded from the manifest and does not invalidate its
own binding.

## Bottom-line verdict

**Clean with limitations.** No required action remains. The bounded maintenance
repair makes the frozen COMP-047 artifact exactly reviewable and corrects
attempt/completion counts, sensitivity scope, and Axis-2 terminology without
changing any docking score, original tier, result identity, or exclusion flag.
The supported conclusion remains narrow: this static docking configuration
produces no defensible Q141K-chaperone ranking. It does not invalidate the
Q141K rescue hypothesis.

`python3 build_results.py` ran twice as authorized. Both runs produced the same
four hashes, which also match the post manifest: `results.json`
`8aaa8491…fe46cd`, `controls.md` `68481ce2…f66ba1`, `summary.md`
`0db1c6a5…4110a`, and `receptor_verification.json` `83bddfee…f17e`.
All 22 `CompReviewContractTests` passed.

## Implementation and constraint closure

`build_results.py` consumes only the frozen result, sensitivity, ChEMBL, and
DrugBank JSON artifacts. It invokes the standard-library receptor verifier
before writing reports and performs no docking, ligand preparation, sensitivity
execution, or network access. Its attempted-count guard requires metadata to
equal the 135 result rows; completeness requires numeric Q141K-fold, WT-fold,
and Walker-A scores. Exactly 134 rows meet that rule. `cyclosporine_a` alone is
incomplete, with all three scores null and original tier `error`; the UTF-8
`logs/run.log` records the same failed attempt.

The repair never assigns `chaperone_tier`, docking scores, margins, selectivity,
row identities, or curated control flags. An exact projection of every score,
tier, ChEMBL status, DrugBank relationship flag, substrate exclusion,
`final_known_abcg2`, and final candidate field is byte-identical to the
pre-repair Git version (projection SHA-256 `0820f2db…2076`).

Receptor verification hash-binds both clean PDBs, both PDBQTs, and `boxes.json`;
checks 5,087/655 clean-structure atoms/residues and 6,190/655 PDBQT
atoms/residues; verifies GLN141→LYS141 identity and byte-identical clean ATOM
records outside residue 141; and permits only the symmetric terminal
SER655→`UNK` warning. These checks establish frozen-file integrity, not
biological suitability.

The model remains a static side-chain substitution in an apo monomer. It does
not represent a folding intermediate, folding ΔΔG, the physiological composite
ATP site, the transmembrane substrate cavity, intracellular exposure, binding,
trafficking, urate flux, or safety. The recorded sensitivity artifact tests
only Q141K fold-site score/rank across base, x +2 Å, x −2 Å, y +2 Å, one +3 Å
xyz diagonal, 18/26 Å boxes, two alternate seeds, and neutral ligand
preparation. It omits y −2 Å, both separate z directions, Walker-A
perturbations, and recomputation of the full margin rule. Its 2–7 changed
positions therefore invalidate only robustness of the tracked base ordering.

## Summary-fidelity audit

The executable artifact contains 135 attempted rows, 134 complete rows,
original tiers of 132 `no`, two `uncertain`, and one `error`, and final output
of 134 `no`, one `uncertain`, and zero `yes`. Rosuvastatin is excluded by
independent substrate evidence plus a DrugBank relationship flag. Vorinostat is
the sole marginal `uncertain` executable row, but not a docking-backed wet-lab
priority.

README, `controls.md`, `summary.md`, and the proposed computational page agree
on those counts and conclusions. They distinguish a bounded ChEMBL activity
record from a UniProt-exposed DrugBank relationship and do not infer a
relationship subtype from the latter. They also state that Axis 2 can exclude
but cannot promote, that the sensitivity scope is fold-site-only, and that the
CFTR correctors are cross-protein comparators rather than validated ABCG2
positive controls.

The future-rerun contract is adequate: a new pre-run lifecycle, a pinned
environment, immutable raw docking results, hash-bound source SMILES/prepared
ligands/receptors/grids, captured return code/stdout/stderr for every Vina
call, exact live-query snapshots, and a predeclared sensitivity scope. It
correctly treats any new preparation, query, docking, or model change as a new
result-bearing lifecycle.

## Reader-facing ownership audit

The proposed focused page owns the experiment question, evidence axes, source
links, result, model and exposure limits, receptor warning, falsification
boundary, and next observation. It contains no cross-track winner table,
personalized treatment instruction, editorial history, page-placement
narration, or another track as a narrative foil. Portfolio summaries remain
compact pointers; validation experiment §1.22 owns the empirical trafficking,
urate-flux, inhibition, exposure, viability, and barrier resolver.

## Conjecture preservation audit

The artifact corrects unsupported ranking and database-absence interpretations
without erasing useful ideas. It kills only the decision-usable ranking from
this frozen static configuration. It preserves the broader Q141K rescue route,
the independent **In Vitro** HDAC-directed rescue precedent, direct-chaperone
possibilities outside this setup, and COMP-032 compounds only as an unranked
hypothesis inventory. The reader page explicitly states that failure to recover
CFTR comparators is not evidence that ABCG2 lacks a rescuable site.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `outputs/chembl_axis2.json` | generated output | Yes | Bounded-record semantics; exact rosuvastatin source separated |
| `outputs/controls.md` | generated output | Yes | Counts, controls, ranks, and exclusions agree |
| `outputs/drugbank_substrate_axis.json` | generated output | Yes | Relationship-only semantics; 31 flagged library rows |
| `outputs/receptor_verification.json` | generated output | Yes | Exact frozen integrity pass with declared symmetric warning |
| `outputs/results.json` | generated output | Yes | All 135 rows inspected; 134 complete; invariants unchanged |
| `outputs/sensitivity.json` | generated output | Yes | Sixteen targets, ten fold-site-only conditions, 2–7 rank changes |
| `outputs/summary.md` | generated output | Yes | Narrow inconclusive verdict and limitations are faithful |
| `scripts/comp-review.py` | proposed update | Yes | `.log` is now an inspectable text suffix |
| `tests/test_knowledge_workflows.py` | proposed update | Yes | Regression exercises `_segments()` on the real `.log` failure class |
| `wiki/abcg2-q141k-chaperone-rescreen-computational.md` | proposed update | Yes | Correct count, sensitivity scope, ownership, and hypothesis boundary |

The `.log` regression writes a `run.log`, passes it through the production
`_segments()` function, asserts one non-binary segment, and checks exact content.
ASCII test content is valid UTF-8 and reproduces the extension-based failure
that previously created the deterministic binary block.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 135 attempted; 134 complete; `cyclosporine_a` incomplete | `results.json`; `run.log` | Count guard and report denominator | Direct manifest-bound artifacts | Verified |
| Scores, tiers, identities, and exclusion flags unchanged | `results.json`; Git baseline; builder | Preserve frozen scientific result | Exact all-row projection comparison | Verified |
| Final 0 `yes`, 1 `uncertain` | `results.json`; reports | Bounded executable result | Deterministically recomputed | Verified |
| Limited fold-site sensitivity panel; 2–7 positions changed | `sensitivity.py`; `sensitivity.json` | Reject base-rank robustness only | Direct code/output agreement | Verified within stated scope |
| ChEMBL `false` means no bounded record | `chembl_axis2.json`; builder | Three-state activity rendering | Frozen query artifact; not refreshed | Correctly bounded |
| DrugBank flag means relationship, not subtype | `drugbank_substrate_axis.json`; builder | Conservative exclusion only | Frozen UniProt-exposed relationship set | Correctly bounded |
| Rosuvastatin substrate exclusion | `chembl_axis2.json`; provenance | Exclude one marginal docking row | Exact FDA-label URL/section cited; primary not reopened under no-live-query brief | Source modality preserved |
| Vorinostat Q141K phenotypic precedent | provenance; focused page | Validation control, never docking validation | PMID 22472121/PMCID PMC4163836 cited; primary not reopened | Scope and **In Vitro** tier preserved |
| Receptor integrity and 32.61 Å box separation | verifier, expected JSON, receptor files | Fail-closed frozen-input check | Direct manifest-bound files | Verified |
| Future-rerun contract | README; provenance | Prevent stale/resumed or unbound rerun | Prospective design requirements | Adequate |

## Affected wiki pages

- `wiki/abcg2-q141k-chaperone-rescreen-computational.md` — already consistent — canonical focused evidence home and only proposed reader delta.
- `index.md` — already consistent — compact inconclusive verdict without detail duplication.
- `wiki/computational-experiments.md` — already consistent — registry and tracking row preserve the setup-bounded null.
- `wiki/abcg2-q141k-chaperone-screen-computational.md` — already consistent — prior ranking retired; inventory remains unranked.
- `wiki/chassis-pending-interventions.md` — already consistent — route remains unvalidated and routed to direct assay.
- `wiki/abcg2-modulators.md` — already consistent — phenotypic rescue is separate from direct binding and butyrate extrapolation.
- `wiki/validation-experiments.md` §1.22 — already consistent — owns the discriminating observation and safety counterscreens.
- `wiki/etc/chembl-cross-check.md` and `wiki/etc/experiments/lib/target_interactors.py` — already consistent — activity, relationship, and subtype semantics are separated.

Corpus grep found no active stale COMP-047 count, full-axis sensitivity,
DrugBank-subtype, ChEMBL-absence, or Q141K-hypothesis-kill statement outside
historical review receipts.

## New connections or implications

The reusable implication is already routed: transporter screens should keep
bounded activity records, broad relationship flags, and independently verified
relationship subtypes as distinct evidence axes. No additional propagation or
new conjecture is justified by this maintenance repair.

## Required actions

1. None.

## Review limits

I did not execute `analyze.py`, `sensitivity.py`, `repair.py`, receptor/ligand
preparation, docking, or live queries. I did not reproduce the historical Vina
or sensitivity campaigns. External primary sources were not reopened under the
no-live-query brief; their exact identifiers and source modality were audited,
not independently refreshed. Coordinate artifacts were inspected through exact
hashes, complete structure-level parsing, residue/mutation comparison, and the
deterministic verifier. All manifest entries were readable and inspected; none
was omitted or truncated.
