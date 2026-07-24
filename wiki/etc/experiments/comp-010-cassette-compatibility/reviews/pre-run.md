PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 26fe87e4bc062a30c19607177cddaf843bc0dfb5b133230bc0c64a0143bec3e8

# Adversarial pre-run review — comp-010

## Reviewed snapshot

Reviewer `/root/comp010_011_pre_review_v2`; 2 design files; 0 prior-output baseline files. The manifest digest, byte counts, and file hashes match the inspected files exactly.

## Bottom-line verdict

GO authorizes the non-runnable retirement tombstone only. No executable, input, or output survives in the live COMP directory. The retirement ledger exhaustively matches the ten historical non-review files at commit `70e60ea9a7c84a92cec37164f38b456aaa6d6881`.

## Question and model fit

The design retires COMP-010 rather than attempting to repair or rerun it. It correctly withdraws all biological and engineering interpretations while retaining Git as the historical record.

## Constraint and implementation audit

The invalidated scope covers the known defects:

- Protein-level codon proxies without a planned CDS.
- Cross-species Kex2 preference transfer and unsupported cleavage classes.
- Unverified direct-secretion, PTS1, and topology assumptions.
- Glycosylation coordinate and occupancy errors.
- Bulk disulfide proxies presented as folding or secretion capacity.
- Huynh/Ward comparator overreach.
- Overall risk, process, chassis, and cross-payload conclusions.

The retirement-scope digest recomputes to `d8cdbbf3359c9edc230061f02d7397533b30ee2dc1f5d28735db1f177f90ed3b`.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| COMP-010 is non-runnable | `README.md`; `invalidation.json` | Prevent reuse or execution | Confirmed against live tree | Pass |
| Historical inventory is exact | `invalidation.json` | Locate retired artifacts in Git | All paths, sizes, and hashes match recorded commit | Pass |
| No model verdict survives | `invalidated_scope` | Bound interpretation | Covers all known defect classes | Pass |
| Junction/topology idea remains conjectural | Canonical evidence owner | Preserve a useful untested connection | Explicitly labeled; direct evidence absence stated | Pass |
| Direct falsification test exists | Canonical evidence owner | Advance, redirect, or kill conjecture | Exact constructs, termini, compartment, abundance, and activity specified | Pass |

## Falsification, sensitivity, and output contract

There is no planned computation, sensitivity analysis, or generated output. Any repaired analysis must be a new COMP with a new lifecycle. The surviving conjecture can be tested directly and does not inherit evidence from the retired model.

## Downstream authoring contract

The evidence owner is `wiki/cassette-compatibility-computational.md`, inspected separately at SHA-256 `26a1f04ab9db82e68694b885bd4a6ca9465eeb15fae8a5294a5adfeb3c0e6e65`. It prohibits cassette, carrier, junction, tag, chassis, and cross-payload selection. The only retained engineering connection is a labeled Research Conjecture with a discriminating observation.

## Required actions before execution

None.

## Review limits

Read-only static inspection; the retired program was not executed. Primary literature was not independently revalidated. The canonical evidence owner is not part of the pre-run manifest and was inspected as the current worktree surface.
