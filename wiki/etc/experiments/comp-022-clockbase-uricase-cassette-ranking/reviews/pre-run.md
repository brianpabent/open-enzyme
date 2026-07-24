PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 05295607e9d85e60979e7dbf58f5dcf169b958450da1749b64b7ee951c705e0e

# Adversarial pre-run review — comp-022

## Reviewed snapshot

Reviewer `/root/comp022_pre_review_v2`; 21 design files and 6 prior-output baselines. The manifest payload, byte counts, and file hashes matched every inspected file.

## Bottom-line verdict

GO for this provenance/narrative correction only. No result-bearing execution is planned or justified. The changes correct source ownership and epistemic labels without altering executable parameters, ranking logic, decision rules, outputs, or existing corrective actions.

## Question and model fit

COMP-022’s ranking question and downstream decision remain unchanged. The correction:

- Relabels COMP-010 and COMP-011 consistently with their non-runnable invalidation tombstones.
- Attributes Q00511 sequence and zero-`DISULFID` annotation to UniProt rather than retired COMPs.
- Attributes the fixed codon table directly to Kazusa/Nakao/Machida.
- Treats terminal SKL as motivation for a routing test, not evidence of partial peroxisomal loss.
- Labels the rare-codon threshold and glycan/PTS1 penalties as heuristics or hypotheses.

## Constraint and implementation audit

The five changed files contain 23 added and 23 removed lines. After stripping documentation strings, the `analyze.py` executable AST is identical to HEAD. The four `parts_list.json` changes affect only `_meta.target_gene` and three unused `evidence` strings; all numeric fields and enumerated parts are unchanged.

The v1 output tree, complete v2 tree, and all six prior-output baselines are byte-identical to HEAD. No score, cutoff, cohort, shortlist, composite, verdict mapping, output schema, or reproduction command changed.

Current COMP-010/011 tombstones explicitly invalidate their cassette, codon, PTS1, glycosylation, folding, routing, and chassis conclusions. COMP-022 no longer presents either retired model as evidence.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| COMP-010/011 status | `README.md:13` | Related-experiment labels | Matches current invalidated tombstones | Pass |
| Q00511 sequence and disulfide annotation | Input and root provenance | Existing sequence assertion and load input | Reattributed to UniProt; FASTA/value unchanged | Pass |
| Terminal SKL/PTS1 penalty | `analyze.py:23-24`; input provenance | Existing 0.3 heuristic penalty | Explicitly a routing hypothesis; value unchanged | Pass |
| Intrinsic glycan penalty | `analyze.py:363` | Existing 0.2 heuristic load | Explicitly heuristic with occupancy unmeasured; value unchanged | Pass |
| Rare-codon rule | `parts_list.json:224`; input provenance | Existing fixed codon heuristic | No longer sourced to retired COMP-010; logic unchanged | Pass |
| Ranking and outputs | v1/v2 code and outputs | Historical result set | Byte-identical; no rerun | Pass |

## Falsification, sensitivity, and output contract

No falsification rule, sensitivity plan, baseline, threshold, diagnostic, or output contract changed. Running the experiment would incorrectly imply new numerical evidence.

## Downstream authoring contract

The existing seven-item `synthesis/queue/comp-review-022.md` action list remains unchanged and open. This correction does not resolve the v1/v2 strict-tier wording, PTS1 interpretation, README v2 note, `v2_top25.md` ambiguity, ESM2 naming, corpus-wide stale claims, or exhaustive row-audit action.

## Required actions before execution

None. No result-bearing execution is planned or authorized by this receipt.

## Review limits

This GO is strictly scoped to the manifest-bound provenance/narrative correction. It does not revalidate historical COMP-022 rankings, independently reverify primary literature, or close any existing COMP-022 queue action.
