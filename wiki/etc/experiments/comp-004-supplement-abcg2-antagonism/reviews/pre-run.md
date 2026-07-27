PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 4d1a41ff214e1e17c4d5fcc065078b7a6c4074f8c00ff4bab4b803daf94b5d26

# Adversarial pre-run review — comp-004

## Reviewed snapshot

Reviewer `/root/comp004_gate1_refresh`; four design files and two prior-output baseline files. The manifest payload and every bound file byte count and SHA-256 matched the inspected snapshot. The review was static and read-only; result-bearing code was not executed.

## Bottom-line verdict

The bounded correction may run. It audits exactly three cited primary records and can route them only to direct intestinal urate-flux testing. It cannot infer occupancy, inhibition magnitude, clinical risk, dose, delivery, or compound rank.

## Question and model fit

The model asks whether three reported ABCG2 interaction signals establish direct intestinal urate transport inhibition. They do not. The model preserves the interaction signals while rejecting transfer from nominal concentration or drug-substrate assays to intestinal urate flux.

## Constraint and implementation audit

- Cooray (PMID 15047179) supports a quercetin/BCRP functional signal with drug substrates in non-intestinal cells, not intestinal urate transport.
- Karibe (PMID 29358184) supports an intestinal curcumin/BCRP interaction in cynomolgus monkeys with sulfasalazine and rosuvastatin, not direct urate flux.
- Farabegoli (PMID 20149610) supports reduced mitoxantrone-assayed BCRP activity after EGCG exposure in tamoxifen-resistant MCF-7 cells without changed BCRP mRNA or protein, not an intestinal urate effect.
- Yu (PMID 38757391) reports no ABCG2 result and cannot supply the missing urate-flux evidence.
- The input gate validates the exact compound set, normalized duplicates, vocabularies, Boolean fields, nonempty substrates, and nonempty source-metadata fields. It does not validate identifier syntax or source contents.
- The deterministic standard-library script writes only the declared UTF-8 JSON and Markdown outputs.

## Load-bearing pre-run table

| Boundary | Evidence and implementation | Verdict |
|---|---|---|
| Direct intestinal urate evidence | None of the three records measures it | Preserved |
| Interaction evidence | Each record retains its actual assay, substrate, system, and polarity | Preserved |
| Source metadata | Structurally required and nonempty; content checked independently against the named abstracts | Adequate for this fixed set |
| Quantitative risk, rank, dose, or delivery | Prohibited in both output branches | Preserved |
| Contrary outcome | A record with direct intestinal urate evidence takes a prespecified evidence-present branch | Preserved |

## Falsification, sensitivity, and output contract

The exact fixed records, deterministic decision rules, and two declared outputs are preregistered. A contrary direct-evidence record cannot silently receive the default assay-required disposition. There is no justified quantitative sensitivity analysis because the correction makes no transferable kinetic or exposure estimate.

## Downstream authoring contract

The downstream map assigns transporter evidence and the bounded Research Conjecture to `abcg2-modulators.md`, EGCG-specific evidence to `egcg.md`, and the context-matched exposure/protein/attribution/barrier/viability/urate-flux experiment to `validation-experiments.md`. Unsupported COMP-013 occupancy ratios, predicted inhibition percentages, VERY_HIGH labels, and derived clinical uses may be invalidated; the individual interaction signals and untested context connection survive.

## Required actions before execution

None.

## Review limits

The review covered the exact manifest-bound design, prior-output baselines, and named primary abstracts. It did not conduct a literature census or inspect future outputs and downstream edits; those require the post-run gate.
