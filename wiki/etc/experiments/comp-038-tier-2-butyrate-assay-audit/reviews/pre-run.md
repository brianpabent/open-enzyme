PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 4c8e8aa62d3d6801a5469d0fac4b345b1be95b4426af314be4d89ab3c5d2fd01

# Adversarial pre-run review — comp-038

## Reviewed snapshot

Reviewer `/root/comp038_gate1_r3_20260728`; canonical
`pre-run.manifest.json` SHA-256
`4c8e8aa62d3d6801a5469d0fac4b345b1be95b4426af314be4d89ab3c5d2fd01`;
8 design files plus 1 shared dependency; 6 prior-output baseline files. Every
recorded SHA-256 and byte count matched. The repository manifest checker
independently returned the same digest, and the manifest matched the complete
current design/dependency and prior-output sets.

## Bottom-line verdict

This bounded, non-result-bearing maintenance revision may run. The
authorization checks precede every environment, network, directory-creation,
and output-write path; the default command is read-only; its missing-file
diagnostics are path-independent; and the controlling
primary-source-verification JSON is required as a regular-file target. Exact
content integrity remains explicitly assigned to the manifest-bound COMP
lifecycle rather than being conflated with the presence check.

The regression design, scientific non-inference boundary, reproducibility
commands, and recovery contract for future partial regeneration are complete.
No mandatory design, implementation, provenance, output-contract, or
reproducibility correction remains.

## Question and model fit

The proposed run does not answer the underlying biological question of which
assay should be adopted. It answers the narrower maintenance question: can the
current artifact be checked without mutation, and can legacy mutation modes be
prevented from silently replacing verification-controlled outputs?

The implementation fits that decision directly:

- ordinary `python3 analyze.py` checks five declared artifact paths and returns
  without entering discovery logic;
- `--prepare-codex` and `--run-openrouter` are mutually exclusive and each
  requires `--regenerate-current-outputs`;
- the authorization flag alone is rejected;
- authorized regeneration is explicitly outside this maintenance execution
  and requires a new reviewed lifecycle before interpretation.

There is no hidden substitution of file presence for content validity: the
README identifies the required-file check as presence/type validation and the
COMP lifecycle as the SHA-256 content-integrity authority.

## Constraint and implementation audit

`argparse` validation and both authorization-state checks occur before
`OUTPUTS.mkdir`, `.env` loading, input reads, PubMed access, model-client
construction, or output writes. The imported shared helper has no import-time
network or filesystem mutation.

`CURRENT_OUTPUT_NAMES` contains:

- `pubmed-snapshot.json`
- `codex-synthesis-packet.md`
- `primary-source-verification-2026-07-24.json`
- `results.json`
- `summary.md`

The default branch applies `Path.is_file()` to every target, accumulates all
failures, emits only stable `outputs/<basename>` diagnostics, exits 1 on
failure, and does not create a missing output directory. Successful execution
prints a status line and returns without reading or rewriting result contents.

The manifest-bound test suite uses isolated temporary output trees, guards
downstream environment/network/write facilities, compares file hashes across
relevant cases, and covers default success, absent output directories, a
missing controlling verification JSON, directory-shaped targets, unauthorized
mutation modes, authorization without a mode, and mutually exclusive mutation
modes.

No substrate, concentration, unit, time, compartment, transport, coproduct, or
safety model is introduced. Culture-supernatant HPLC-UV and stool
electrochemical/ANN remain distinct tracks, and the maintenance run cannot
alter the YELLOW scientific result.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Legacy mutation requires explicit authorization | `analyze.py`, argument parsing and guard block | Stops discovery modes before mutable or external-service paths | Direct inspection of manifest-bound code and regression cases | Adequate |
| Mutation modes are mutually exclusive | `analyze.py`, `argparse` mutually exclusive group | Prevents ambiguous combined regeneration | Direct implementation inspection; dedicated regression case | Adequate |
| Diagnostics are path-independent | `analyze.py`, default failure branch | Reports stable `outputs/<basename>` entries regardless of checkout location | Direct code inspection | Adequate |
| Controlling verification JSON is mandatory | `CURRENT_OUTPUT_NAMES`; maintenance plan item 5 | Makes its absence or non-file shape fail the default check | Exact filename matches the prior-output baseline and current structured result | Adequate |
| Default success and failure are read-only | `analyze.py`; `test_maintenance.py` | Preserves output contents and avoids creating an absent directory | Temporary-tree hash assertions, guarded-call assertions, and planned Git diff | Adequate |
| Presence checking is not content verification | README lifecycle section | Keeps cryptographic integrity under the exact-snapshot lifecycle | Manifest workflow and explicit documentation | Adequate |
| Scientific result remains unchanged | README decision boundary; maintenance repair plan | Prevents maintenance behavior from changing assay qualification or inference scope | Existing output identity verified; historical results consulted only after independent design findings | Adequate |
| Maintenance environment is reproducible | README and maintenance plan | Fixes interpreter, dependencies, commands, expected exits, and mutation checks | CPython 3.14.5 present; standard library plus one manifest-bound shared helper | Adequate |
| Partial authorized regeneration has a recovery rule | README and maintenance plan | Prevents interpretation of a mixed output set | Requires a committed reviewed starting snapshot and complete output-delta restoration | Adequate |

## Falsification, sensitivity, and output contract

Contrary outcomes can win. The repair fails if an unauthorized mode reaches
any guarded facility, the controlling verification JSON can be absent without
failure, an absent output directory is created, a directory-shaped expected
target is accepted, current outputs change, or the scientific boundary
changes.

There is no numerical sensitivity analysis because the maintenance decision
consists of Boolean CLI and filesystem invariants. The relevant state space is
represented by explicit invalid argument combinations, missing/type-invalid
filesystem states, repeated default execution, before/after hashes,
deterministic exit expectations, and an output-directory Git diff.

The maintenance run emits diagnostics only and produces no scientific output.
Any future authorized regeneration is non-atomic, must begin from a committed
reviewed snapshot, and must discard the complete output-directory delta after
partial failure before retrying.

## Downstream authoring contract

The canonical evidence home remains
`wiki/tier-2-butyrate-assay-audit-computational.md`. This maintenance run
authorizes no new scientific interpretation or comparison.

Any retained Gu performance summary must remain scoped to the exact published
hardware–chemistry–model stack, the within-study 30-sample fecal cohort, the
statistically nonzero negative bias, and unresolved independent external
transfer. Current inspected surfaces preserve those qualifications and use
the correct PubMed link for PMID 42041444.

The run cannot decide assay adoption, matrix transfer, target-compartment
exposure, ABCG2 or Q141K effects, gout efficacy, treatment, safety, or clinical
validity. It cannot invalidate neighboring biological hypotheses. No
cross-track ranking, personalized instruction, duplicated evidence narrative,
or reader-facing maintenance history is authorized.

## Required actions before execution

None.

## Review limits

Static inspection only. I did not execute `analyze.py`, the maintenance tests,
repository tests, either mutation mode, network access, or any result-bearing
path. All manifest-listed design and shared-dependency files were available
and inspected completely. Historical outputs were consulted only after
recording independent design findings and only for schema, compatibility, and
scientific-boundary checks; the large discovery packet and PubMed snapshot
were inspected structurally rather than scientifically re-adjudicated. Prior
reviews were used only to verify closure of earlier required actions. Primary
scientific sources were not independently re-reviewed because this maintenance
revision changes no scientific claim.
