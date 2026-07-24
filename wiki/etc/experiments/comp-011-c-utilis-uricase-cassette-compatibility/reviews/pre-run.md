PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 6939ba0b2585f43178ebfb06093fe5387e9c4d08c18cfbc135ee147be9a262f8

# Adversarial pre-run review — comp-011

## Reviewed snapshot

Reviewer `/root/comp010_011_pre_review_v2`; 2 design files; 0 prior-output baseline files. The manifest digest, byte counts, and file hashes match the inspected files exactly.

## Bottom-line verdict

GO authorizes the non-runnable retirement tombstone only. No executable, input, or output survives in the live COMP directory. The retirement ledger exhaustively matches the ten historical non-review files at commit `70e60ea9a7c84a92cec37164f38b456aaa6d6881`.

## Question and model fit

The design correctly retires COMP-011 rather than treating the wild-type P78609 plus seven-mutation proxy as the exact clinical ALLN-346 construct. It withdraws the old variant comparison and all derived engineering recommendations.

## Constraint and implementation audit

The invalidated scope covers the known defects:

- Protein-level codon inference without a planned CDS.
- Conflation of wild-type P78609, a synthetic mutation proxy, and clinical ALLN-346.
- WT-only main comparisons despite mutant-specific side analysis.
- Cross-species Kex2 scoring and hard-coded topology assumptions.
- Glycosylation coordinate and occupancy errors.
- Conversion of native cysteine annotations into folding, aggregation, and secretion verdicts.
- Unsupported protease-resistance, stability, clinical-sequence-equivalence, and freedom-to-operate claims.
- Huynh/Ward capacity, overall risk, chassis, process, and cross-payload conclusions.

The retirement-scope digest recomputes to `9797acf65e77b29fa1ad466342b8f6a078d1b0764d462a9bb4e7791126cece51`.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| COMP-011 is non-runnable | `README.md`; `invalidation.json` | Prevent reuse or execution | Confirmed against live tree | Pass |
| Historical inventory is exact | `invalidation.json` | Locate retired artifacts in Git | All paths, sizes, and hashes match recorded commit | Pass |
| Exact clinical ALLN-346 sequence is unavailable | Ledger and canonical evidence owner | Prohibit proxy-to-product equivalence | Stated explicitly and repeatedly | Pass |
| Patent mutation set establishes no benefit or FTO | `invalidated_scope`; `surviving_scope` | Bound patent observations | Benefit, equivalence, stability, and FTO conclusions invalidated | Pass |
| Mutation-dependent processing remains conjectural | Canonical evidence owner | Preserve a useful untested connection | Explicitly labeled; direct evidence absence stated | Pass |
| Direct falsification test exists | Canonical evidence owner | Distinguish sequence from platform effects | Sequence verification plus matched termini, folding, secretion, abundance, and activity tests specified | Pass |

## Falsification, sensitivity, and output contract

There is no planned computation or output. A future comparison must define the exact sequence objects and topology in a new COMP lifecycle. The retained conjecture permits either construct-specific effects or no difference to win.

## Downstream authoring contract

The evidence owner is `wiki/c-utilis-uricase-cassette-compatibility-computational.md`, inspected separately at SHA-256 `0db981d0f485d9948a8dd990c1429530da3bb6a5c48fbb24f117bc303ca8064b`. It expressly prohibits inferring the clinical ALLN-346 sequence from the patent mutation list and selects no variant, cassette, carrier, tag, or chassis.

## Required actions before execution

None.

## Review limits

Read-only static inspection; the retired program was not executed. The patent and primary literature were not independently revalidated. The canonical evidence owner is not part of the pre-run manifest and was inspected as the current worktree surface.
