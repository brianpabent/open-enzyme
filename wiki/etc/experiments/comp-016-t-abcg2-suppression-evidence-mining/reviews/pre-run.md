PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 260b5a07aa2f65b147b896e6cb8519c1a1c1caebff1999fafa25b315cb52fa3d

# Adversarial pre-run review — comp-016

## Reviewed snapshot

Reviewer/subagent: `/root/comp016_gate1_r3_20260729`.

Canonical `pre-run.manifest.json` SHA-256:
`260b5a07aa2f65b147b896e6cb8519c1a1c1caebff1999fafa25b315cb52fa3d`.
The manifest bound five design files and two prior-output baseline files. Every
bound file's byte count and SHA-256 matched the file inspected. Independent
design findings were recorded before the historical baselines and prior REVISE
receipt were read. Both baseline files were then inspected completely for
schema and stale-claim risks, not used as evidence for the proposed result.

## Bottom-line verdict

This exact snapshot may run. It asks a bounded, decision-useful question:
whether any record in the fixed 17-record inventory directly demonstrates
decreased intestinal ABCG2 under an androgen exposure or androgen-state
manipulation in the same tested context. The validator now enforces the
same-context, citable, verification-tier, and strict-Boolean admission
requirements; the computation derives both result codes and every positive or
negative result-bearing JSON/Markdown sentence from the admitted direct rows.
The documented CPython 3.14.5 two-run procedure is sufficient to test the
byte-determinism claim before the outputs are accepted.

The earlier receipt's four required corrections are closed. The fixed result
cannot become a universal literature-absence claim, a healthy-human baseline
claim, a physiological culture-exposure claim, a male export ceiling, a
clomiphene claim, or a rejection of the broader androgen–urate prior.

## Question and model fit

This is a deterministic fixed-inventory validator and renderer, not a
physiological model, current literature search, systematic review, or
statistical analysis. Its valid decision is whether the committed extraction
contains a verified same-context androgen manipulation plus intestinal-ABCG2
measurement whose recorded target outcome is `decrease`. A qualifying decrease
can produce the positive status; zero qualifying decreases produces only
`NOT_DEMONSTRATED_IN_FIXED_INVENTORY`.

The design excludes the historical proxy substitutions. Genotype effects,
unmanipulated sex comparisons, estradiol-only exposure, serum urate, renal
transporters, non-intestinal cancer-cell mechanisms, and reviews remain
adjacent evidence. In the current input, S04_Slepnev2023 is the only admitted
direct test: testosterone exposure and Caco-2 ABCG2 were linked in the same
context, the outcome is `increase`, and the record is limited to the official
publisher abstract and nominal in-vitro conditions. No inference converts that
record into physiological-human direction, free-tissue exposure, direct
androgen-receptor involvement, or literature-wide completeness.

The unsearched multilingual sources are disclosed. Expanding the inventory or
reclassifying a source requires a new exact-snapshot lifecycle, so the bounded
negative cannot silently stand in for an exhaustive result.

## Constraint and implementation audit

`load_inventory()` reads only the fixed UTF-8 JSON. `validate_inventory()`
requires schema version 2, exactly 17 unique records, enumerated test classes,
outcomes, and verification tiers, and uses `type(...) is bool` for `citable`,
`androgen_manipulated`, `intestinal_abcg2_measured`, and
`same_context_target_outcome`. Every `in_vivo` or `in_vitro` row must:

- manipulate androgen;
- measure intestinal ABCG2;
- link the target outcome to that same tested context;
- be citable;
- use `primary_full_text`, `official_publisher_abstract`, or
  `primary_database_abstract`; and
- carry an outcome other than `not_tested`.

Adjacent and unresolved rows cannot carry a same-context target outcome or any
result-bearing target direction. Thus a legacy search summary or unresolved
placeholder cannot produce a demonstrated result.

`analyze()` enumerates in-vivo and in-vitro direct rows, selects suppression
only from direct rows whose outcome is `decrease`, and maps the empty/non-empty
set to the two preregistered result codes. Both `bounded_interpretation`
branches and both `scope_conclusion` branches are conditional on that same
computed set. `build_results()` carries the computed counts, direct IDs,
direct outcomes, corrected anchors, complete classifications, and forbidden
inferences into JSON. `render_summary()` enumerates the computed direct rows
and outcomes rather than naming a presumed record, and all positive and
negative prose is drawn from the computed branch.

The four retained source anchors preserve their distinct compartments,
models, evidence levels, and verification tiers. The Hoque 78% jejunal versus
44% renal comparison, Liu nominal 100 µM/48-hour and 50 µM LY294002
conditions, Slepnev nominal 1/10/100 µM and 24-hour conditions, and MacLean
qualitative rat null match the repository-local primary/official-abstract
verification record and retain explicit exposure and inference boundaries.
No calculation combines those contexts.

There is no mass-balance, transport, diffusion, kinetic, dose-conversion,
random, or external-service model to audit. Those constraints are outside this
finite classification question and are not silently defaulted. The script uses
the Python standard library, sorted JSON keys, fixed record order, UTF-8, and
explicit LF output. The installed and declared runtime is CPython 3.14.5. The
README supplies an exact two-run checksum/diff procedure covering both output
files. No result-bearing code was executed during this review.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| The bounded denominator is the fixed 17-record inventory collected on 2026-05-07 | `inputs/studies.json`; `inputs/provenance.md`; `validate_inventory()` | Prevents silent record addition or loss and scopes both statuses | Exact original queries, access failures, repair policy, and all 17 positions are retained | Pass as a fixed inventory; not a literature-completeness denominator |
| A direct test must manipulate androgen and measure intestinal ABCG2 in the same tested context | README; per-record strict booleans; `validate_inventory()` | Admits rows to `in_vivo` or `in_vitro` direct-test sets | Current direct record is citable and official-publisher-abstract verified; legacy summaries cannot qualify | Pass |
| Direct suppression requires `target_outcome=decrease` in an admitted direct row | `analyze()` | Computes `direct_suppression_ids` and selects the positive or negative result code | Direction is a fixed source classification, not inferred from citation text or adjacent endpoints | Pass |
| Positive and negative JSON interpretations and Markdown sentences must agree with the status | `analyze()`; `build_results()`; `render_summary()` | Allows a contrary decrease result to win without stale negative prose and enumerates all direct rows | Both branches and direct-record sentences derive from computed sets | Pass |
| Hoque, Liu, Slepnev, and MacLean corrected findings remain context-separated | `inputs/studies.json`; `inputs/provenance.md`; corrected-anchor output | Replaces unsupported historical attribution/magnitudes without deciding untested physiology | Primary-full-text, official-publisher-abstract, or primary-database-abstract tiers are named with stable DOI/PMID/PMCID identifiers | Pass at the stated evidence tiers and boundaries |
| No universal absence, healthy-human null, physiological opposite effect, male ceiling, broad androgen–urate rejection, or clomiphene implication | `forbidden_inferences`; both planned outputs | Constrains downstream interpretation | Preregistered in the fixed input and rendered verbatim | Pass |
| Outputs are byte-identical on two consecutive runs | README reproduction contract; deterministic writers | Accepts or rejects the maintenance run's two planned output files | CPython 3.14.5, standard library only, UTF-8/LF, no randomness, no external service, exact checksum/diff commands | Pass as a preregistered execution-time check |
| Gate 2 binds the complete current interpretation set | README downstream authoring set | Prevents stale or over-broad downstream use | Exactly seven named files; no external reader-facing text change is proposed by this run | Pass |

## Falsification, sensitivity, and output contract

Contrary results can win. At least one admitted `decrease` row selects
`DIRECT_SUPPRESSION_DEMONSTRATED_IN_FIXED_INVENTORY`, names every qualifying
record, and limits the statement to those tested model contexts. With no
qualifying decrease, the negative branch rejects only use of direct
androgen-driven intestinal ABCG2 suppression as an established premise from
this inventory. Neither branch discards the need for direct apical-protein and
urate-flux measurement.

No numerical sensitivity analysis is warranted for a finite categorical
inventory. The dominant uncertainties are record classification,
source-verification tier, and search coverage. The planned JSON and Markdown
retain the denominator, citable/unresolved accounting, test-class and
verification-tier counts, all direct IDs and outcomes, corrected anchors,
complete record classifications, boundaries, and forbidden inferences. A new
record, retrieval, or source reclassification is correctly treated as a new
result-bearing lifecycle rather than a sensitivity run.

The historical baselines contain obsolete attribution, unsupported numbers,
cross-context aggregation, a hard male-ceiling narrative, and a COMP-014-based
limitation. They are schema baselines only. Static inspection confirms that
the proposed renderer overwrites both files and emits none of that historical
residue. The README's exact two-run check then detects any nondeterministic
byte change before acceptance.

## Downstream authoring contract

The canonical historical result home is
`wiki/t-abcg2-suppression-evidence-mining-computational.md`. The corrected
source record and unresolved healthy-human question remain owned by
`wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`
(COMP-017). Gate 2 must bind exactly these seven current surfaces:

1. `wiki/t-abcg2-suppression-evidence-mining-computational.md`
2. `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`
3. `wiki/computational-experiments.md`
4. `wiki/abcg2-modulators.md`
5. `wiki/androgen-urate-axis.md`
6. `wiki/open-questions.md`
7. `wiki/etc/manual-literature-mining.md`

No external reader-facing edit is proposed by this run; Gate 2 still inspects
the exact current interpretations. Focused pages retain only their own
evidence and falsification boundaries, and no cross-track ranking, treatment
guidance, personalized dosing, editorial history, or duplicated exposition is
authorized.

The result may retire only the claim that this fixed inventory demonstrated
direct androgen suppression of intestinal ABCG2. The broader androgen–urate
relationship and direct-measurement question remain explicit on their current
pages. The repaired design has no operative COMP-014 dependency: COMP-014
appears only in the maintenance plan's defect history, not in executable
inputs, decision rules, or planned output prose. The independently sourced DAE
idea remains at `wiki/medicinal-mushroom-complement-track.md`, with its own DOI,
evidence boundaries, and discriminating tests; removing COMP-014 as provenance
does not delete that adjacent conjecture.

## Required actions before execution

None.

## Review limits

This was a static exact-snapshot review. All five manifest-bound design files
and both prior-output baselines were available and inspected completely, and
their hashes matched. The earlier REVISE receipt was read only after
independent findings were recorded; every earlier required action was then
traced to its implemented correction. Current downstream ownership,
COMP-014-removal, broader androgen–urate preservation, and independent DAE
preservation were checked in the repository.

External papers were not re-retrieved. Source adequacy was assessed from the
stable identifiers, declared verification tiers, and repository-local
primary/official-abstract verification records. The installed runtime was
checked, but `analyze.py`, its output writers, and all result-bearing logic
were not executed.
