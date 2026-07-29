PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: ac3bc8da40096a64c3c2c0f8e7cafd4fb01b2f937a9411bbea08c8cab0089fc0

# Adversarial pre-run review — comp-047

## Reviewed snapshot

Reviewer `/root/comp047_gate1_20260729`; canonical
`pre-run.manifest.json` SHA-256
`ac3bc8da40096a64c3c2c0f8e7cafd4fb01b2f937a9411bbea08c8cab0089fc0`;
23 design files; seven prior-output baselines. I independently recomputed the
canonical payload digest and ran the repository manifest checker. Every
recorded path, byte count, and file SHA-256 matched the files inspected.

I reconstructed the question, decision, code path, frozen inputs, and output
contract before reading the historical review receipts. I did not execute
`build_results.py` or any docking, sensitivity, receptor-preparation,
ligand-resolution, repair, or live-query command.

## Bottom-line verdict

This bounded maintenance correction may run exactly as authorized:
`python3 build_results.py` twice. It makes the frozen artifact exactly
reviewable and corrects count, sensitivity-scope, and evidence-axis wording
without changing a docking score, original scientific tier, candidate
ordering, or the inconclusive disposition.

The exact baselines establish 135 attempted rows, 134 complete three-score
rows, and only `cyclosporine_a` incomplete. The limited sensitivity panel and
both Axis-2 evidence boundaries are represented faithfully. No required
design, implementation, provenance, output, or reproducibility action remains.

## Question and model fit

The maintenance question is whether the exact frozen COMP-047 run supports a
reproducible docking-backed ranking after receptor-integrity and ABCG2
exclusion checks. The answer remains no: one marginal `uncertain` executable
row is not a defensible ranking or a wet-lab priority.

The computation remains a static apo-monomer docking proxy. It does not model
folding intermediates, folding free energy, mutant-selective stabilization,
intracellular exposure, direct transport rescue, or clinical efficacy. The
artifact states these substitutions explicitly and limits invalidation to this
ranking configuration rather than the Q141K rescue hypothesis.

## Constraint and implementation audit

`build_results.py` uses only committed frozen JSON plus the standard-library
receptor verifier. It invokes no docking, sensitivity, ligand-preparation, or
network path. Receptor hashes, counts, GLN141→LYS141 identity, clean-structure
difference scope, box geometry, and the symmetric SER655→`UNK` warning are
checked before corrected reports are written.

The attempted count comes from `_meta.n_molecules` and must equal the result-row
count. Completeness requires numeric Q141K-fold, WT-fold, and Walker-A scores.
The bound baseline has 135 rows, 134 complete rows, and exactly one incomplete
row (`cyclosporine_a`, all three scores null, original tier `error`); the text
run log corroborates that incomplete attempt.

The sensitivity artifact contains 16 molecules across exactly 10 conditions:
base; x +2 Å; x -2 Å; y +2 Å; one +3 Å xyz diagonal; 18 Å and 26 Å boxes; two
alternate seeds; and neutral ligand preparation. All recorded base values equal
the frozen result scores. It does not contain y -2 Å, either z-axis shift, a
Walker-A perturbation, or a recomputation of the complete margin rule.

The merger never assigns `chaperone_tier` or alters affinities, margins,
selectivity values, or result identities. It recomputes only conservative
Axis-2 annotations and `wetlab_candidate`; the current rows already agree with
that union. The `.log` tooling change is outside the scientific code path: it
adds UTF-8 logs to push-review text sharding and does not enter the COMP model
or decision. Its targeted regression and the full 22-test review-contract class
passed.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 135 attempted rows | `outputs/results.json` `_meta` and rows | Report attempted denominator; fail if metadata and rows differ | Direct manifest-bound artifact | Supported |
| 134 complete; `cyclosporine_a` incomplete | `outputs/results.json`; `logs/run.log` | Require all three docking scores for completeness and name the incomplete row | Direct manifest-bound artifacts | Supported |
| Original tiers and ranking remain fixed | `outputs/results.json`; `build_results.py` | Preserve `chaperone_tier`, scores, margins, selectivity, and row identity | Static code trace plus exact baseline | Supported |
| Limited 10-condition fold-site panel | `sensitivity.py`; `outputs/sensitivity.json` | Describe Q141K fold-score/rank instability only | Code and direct artifact agree | Supported within declared scope |
| ChEMBL false means no bounded record | `outputs/chembl_axis2.json`; `build_results.py` | Render `record present`, `no bounded record`, or `unqueried` | Frozen bounded-query artifact; not refreshed | Correct |
| DrugBank flag means ABCG2 relationship, not subtype | `outputs/drugbank_substrate_axis.json`; `build_results.py` | Conservative exclusion only | Frozen UniProt-exposed relationship set | Correct |
| Rosuvastatin substrate subtype is independently sourced | `outputs/chembl_axis2.json`; `inputs/provenance.md` | Separate subtype-specific exclusion from generic relationship evidence | Primary FDA label is explicitly cited | Correctly separated |
| Future rerun requires a new lifecycle | `README.md`; `inputs/provenance.md` | Require pinned environment, immutable raw result, ligand/receptor/grid hashes, process logs, live-query snapshots, and predeclared sensitivity scope | Prospective reproducibility contract | Adequate |
| UTF-8 run log is inspectable text | `logs/run.log`; `scripts/comp-review.py`; regression test | Remove the Gate-3 binary-classification block | Process-only tooling; test verified | No scientific-design effect |

## Falsification, sensitivity, and output contract

Contrary evidence can still win within the bounded decision: receptor mismatch
or count/schema inconsistency stops the build; Axis-2 evidence can exclude but
cannot promote; and the absence of a validated ABCG2 chaperone positive control
plus recorded rank instability prevents interpreting the sole marginal row as
a ranking. The sensitivity result is confined to fold-site score and relative
rank within its implemented panel.

The planned reports expose attempted/complete/incomplete counts, all executable
rows, original tiers, Axis-2 statuses, exclusion reasons, controls, fold ranks,
score spans, sensitivity scope and rank-change range, receptor verification,
and load-bearing biological limitations. Running the standard-library builder
twice and requiring identical hashes for its four written outputs is an
adequate determinism check for this maintenance correction.

## Downstream authoring contract

The canonical evidence home remains
`wiki/abcg2-q141k-chaperone-rescreen-computational.md`. The bounded maintenance
plan proposes only its count and sensitivity-scope corrections, with any
additional page limited to an active stale statement found by correction-
cascade grep. The existing proposed delta does not change a tier, compound
rank, evidence level, validation priority, or portfolio comparison.

No direct binding, pharmacological-chaperone activity, absence of an ABCG2
rescue site, relationship subtype from DrugBank, transporter clearance from a
negative ChEMBL lookup, new hypothesis card, intervention page, or cross-track
ranking is authorized. Independent phenotypic rescue evidence remains separate
from the docking row, and empirical resolution remains in validation experiment
§1.22.

## Required actions before execution

None.

## Review limits

This was static exact-snapshot inspection. I did not refresh PubChem, ChEMBL,
DrugBank, UniProt, or external literature, and I did not reproduce the
historical docking or sensitivity runs. Those historical results are frozen
inputs to this maintenance operation. I inspected prior receipts only after
recording independent design findings; they do not substitute for this review.
