PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 9acd8643748d3774f6738ebdc3e49edbf2cb6df1f2d6b52fdc35a7f5fe5abefb

# Adversarial pre-run review — comp-038

## Reviewed snapshot

Reviewer `/root/comp038_gate1_final`; manifest SHA-256 `9acd8643748d3774f6738ebdc3e49edbf2cb6df1f2d6b52fdc35a7f5fe5abefb`; 6 design files; 6 prior-output baseline files. Every listed file matched its recorded SHA-256. The README is current and time-stable: it describes the completed corrective source verification, distinguishes it from the historical run, and does not predict a future repair.

## Bottom-line verdict

The bounded static repair may proceed. It asks whether two specific historical verification claims can be reconstructed from two named primary sources, not whether the assay landscape is complete. Its source-access labels, retraction rules, matrix boundaries, and acceptance criteria prevent abstract evidence, within-study validation, or published method performance from being promoted into stronger Open Enzyme claims.

## Question and model fit

The repair directly resolves the unsupported claim that both candidates received a July 14 full-text verification. De Baere is constrained to primary-abstract method fields; Gu is constrained to accessible primary full text and a within-study independent test cohort. The plan explicitly excludes a refreshed landscape search, external replication claims, method adoption, clinical validity, gout efficacy, safety, and cross-matrix transfer. No hidden proxy is substituted for the stated forensic question.

## Constraint and implementation audit

This is a source-audit repair with no result-bearing code execution, so biological mass balance, transport, exposure, and kinetic modeling are not applicable. The plan nevertheless closes the relevant analytical constraints: matrix, sample preparation, hardware, acquisition mode, comparator, cohort type, calibration and performance fields, implementation transfer, and Open Enzyme qualification.

`analyze.py` is the frozen legacy discovery workflow and is explicitly excluded from this repair. The README correctly warns that it cannot reproduce the primary-source verification and must not overwrite the corrected outputs. The claim-map specification traces each retained detail to source identity, access scope, location, evidence level, reviewer/date, disposition, and an Open Enzyme boundary.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| De Baere access is abstract-only | Verification plan, frozen source set §1 | Limits retainable method fields and prohibits “full-text verified” | PMID, DOI, EPA HERO access named | Adequate |
| Gu access is primary full text | Verification plan, frozen source set §2 | Supports bounded methods and within-study test-cohort fields | PMID, PMCID, DOI, NCBI PMC access named | Adequate |
| Gu cohort is not external replication | Verification plan and retraction rules | Prevents validation-tier inflation | Explicitly preregistered | Adequate |
| “Underivatized” requires explicit source text | Required claim map and retraction rules | Forces retraction when absent | Source-controlled rule | Adequate |
| Published performance does not qualify an OE method | Decision boundary and acceptance criteria | Keeps source validation separate from transfer/adoption | Explicit matrix and workflow boundaries | Adequate |
| Overall verdict may remain YELLOW only within narrower support | Acceptance criteria | Allows source contradiction or failed reconstruction to tighten/retract claims | Contrary outcomes can win | Adequate |

## Falsification, sensitivity, and output contract

The decision rule is source-reconstructable retain/tighten/retract, with mandatory retraction when a detail lacks support. Contrary source evidence can therefore defeat prior claims. The dominant uncertainty—De Baere full-text unavailability—is represented as an access-scope limit rather than inferred away. The planned structured output retains claim-level provenance, bounded support, dispositions, source-study versus OE boundaries, and separate culture-supernatant and stool validation tracks.

## Downstream authoring contract

The canonical evidence home is `wiki/tier-2-butyrate-assay-audit-computational.md`. The plan names each permissible downstream surface and restricts changes to the local decision delta. It prohibits focused-page comparison rankings, editorial or corpus-maintenance narration, universal matrix transfer, adoption, and clinical or gout conclusions. The repair decides historical and source-supported assay claims only; adjacent research possibilities remain outside its invalidation scope.

## Required actions before execution

None.

## Review limits

Static inspection only. I did not execute `analyze.py`, rerun the historical search, or independently broaden the frozen two-source set. Existing outputs were inspected only after the independent design assessment and treated as prior baseline artifacts.
