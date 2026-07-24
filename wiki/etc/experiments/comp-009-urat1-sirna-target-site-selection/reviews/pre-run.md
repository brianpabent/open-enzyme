PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 5c4c8b1e07ba1de5d57a24d7bf311b625db797886ae0cc3ecdd7cc65a440bee0

# Adversarial pre-run review — comp-009

## Reviewed snapshot

Reviewer: `/root/comp009_retirement/comp009_retirement_pre_review_v2`.

The pre-run manifest contains two design files and zero prior-output baselines. Its canonical payload SHA-256 is `5c4c8b1e07ba1de5d57a24d7bf311b625db797886ae0cc3ecdd7cc65a440bee0`; the literal manifest-file SHA-256 is `f76efe16ca62f1ec078d4f28601f0bb2709a682cfc5a60d47c4015c7e8256776`.

The manifest matched the inspected files:

- `README.md`: 3,849 bytes; `ee8dd2b7b5adde7f91f195aff3c96e09c557bb8be0122dd64cf43b710316edd7`
- `invalidation.json`: 4,136 bytes; `f696e0f00a1988439631576b16c9bb92662cc7d756a64ee6d8113898897b0a09`

The retirement record’s canonical digest independently recomputed to `5d53e3d4972f61cb043c9b955d1b3316ad46c1f54e32c9bcdfc415b7ed6d08aa`, matching the record. All ten retired non-review blobs at commit `b6ca51a489e4ac321fda5f7a1f2e073d884ae0b7` matched their recorded byte counts and SHA-256 hashes.

## Bottom-line verdict

This non-runnable retirement may proceed. The design does not attempt to rescue or rerun COMP-009. It invalidates every result-bearing sequence, funnel count, rank, score, shortlist, GREEN/viability label, accessibility or tractability conclusion, H03-support claim, and P2-2 closure. It preserves only the independently motivated URAT1-siRNA hypothesis and correctly defers new guide design until COMP-048 establishes a plausible proximal-tubule delivery route.

The historical implementation cannot support its verdict. Most decisively, GREEN was determined solely by shortlist length: five or more shortlisted windows produced GREEN even if every accessibility probability were zero.

## Question and model fit

The present question is whether the historical computation can be retired without over-killing the independent therapeutic hypothesis. The two-file tombstone answers that question directly.

Static reconstruction of the retired computation found these proxy substitutions:

- It treated a partial, strand-misoriented approximation of Reynolds criteria as a guide-efficacy score. Reynolds reports sense-strand positional preferences, low stability at the sense-strand 3′ terminus, and absence of inverted repeats; the code applied positional checks to the reverse-complemented antisense strand, omitted terminal-stability and inverted-repeat criteria, and substituted a four-base-run check ([Reynolds et al., 2004](https://doi.org/10.1038/nbt936)).
- It reduced Ui-Tei to an A/U count over the first seven antisense bases. It did not simultaneously require antisense 5′ A/U, sense 5′ G/C, terminal A/U richness, and absence of a GC stretch longer than nine bases as the primary method requires ([Ui-Tei et al., 2004](https://doi.org/10.1093/nar/gkh247)).
- It treated an arbitrary weighted sum as an accessibility-informed design model. Tafer’s RNAxs combined multiple functionality criteria with calibrated accessibility filters and was tested on an independent dataset; the historical `3.75×Reynolds + 2.14×Ui-Tei + 25×P(unpaired) + 0.30×protein conservation` expression is not that model ([Tafer et al., 2008](https://doi.org/10.1038/nbt1404)).
- It substituted amino-acid conservation for nucleotide-level guide conservation, one transcript for relevant isoform coverage, and shortlist size for demonstrated target accessibility or tractability.

The retirement document explicitly rejects all resulting proxies and does not infer that URAT1-siRNA itself is biologically disproven.

## Constraint and implementation audit

The retired code hard-coded the Reynolds/Ui-Tei approximations; `design_parameters.json` was loaded but used only to obtain the desired shortlist size. The filtering path required GC range, absence of selected immunogenic motifs, absence of four-base runs, `reynolds_score >= 5`, and antisense first-seven A/U count `>= 4`. It imposed no minimum RNAplfold accessibility.

The verdict mapping was:

- shortlist length ≥5: GREEN
- shortlist length ≥2: YELLOW
- otherwise: RED

Thus any five candidates surviving the non-accessibility filters could force GREEN regardless of accessibility. In the retained historical shortlist, reported unpaired probabilities ranged from `0` to `0.0047`; accessibility contributed at most `0.1175` points, while amino-acid conservation contributed up to 30 points.

Additional verified defects were:

- No transcriptome-wide or 3′-UTR off-target analysis.
- Only NM_144585.4 was scanned.
- Protein conservation could not establish cross-species guide reuse.
- `region_of()` classified by midpoint. The 326–346 window had midpoint 336 and was labelled 5′-UTR despite spanning the CDS boundary at position 338.
- No intracellular activity, URAT1 knockdown, proximal-tubule uptake, urate-transport effect, or renal-safety measurement existed.

The tombstone covers each of these limitations and correctly provides no reproduction command.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| COMP-009 is non-runnable | Current `README.md`; `invalidation.json:runnable` | Prevent execution or reuse as an active COMP | Explicit and hash-bound | Supported |
| All sequences, ranks, scores, shortlists, GREEN labels, accessibility/tractability conclusions, H03 support, and P2-2 closure are invalid | Current `README.md`; `invalidation_scope` | Define the correction cascade | Historical code and outputs inspected; all retired hashes matched | Supported |
| Reynolds implementation was partial and strand-misoriented | Historical `scripts/analyze.py:117–138`; `design_parameters.json` | Explain why sequence scores cannot survive | Primary Reynolds method identifies sense-strand preferences, terminal stability, and inverted repeats | Supported |
| Ui-Tei enforcement was incomplete | Historical `scripts/analyze.py:136–142, 310–311` | Explain why filter survivors cannot survive | Primary method requires the defining conditions simultaneously | Supported |
| Composite score was arbitrary and not RNAxs | Historical `scripts/analyze.py:221–224, 302` | Invalidate scores and ranks | No calibration or validation provenance for weights; differs materially from Tafer’s calibrated model | Supported |
| Accessibility was not an acceptance criterion | Historical `scripts/analyze.py:305–320, 390–401` | Invalidate GREEN and tractability claims | Direct static code trace | Supported |
| GREEN depended only on shortlist length | Historical `scripts/analyze.py:390–401` | Invalidate GREEN/H03/P2-2 | Direct static code trace; no accessibility threshold | Supported |
| No off-target clearance and only one isoform | Historical `scripts/analyze.py:231–245, 347`; outputs | Invalidate specificity and transcript-coverage claims | Direct static code trace | Supported |
| Protein conservation cannot establish guide reuse | Historical `scripts/analyze.py:190–208, 270–302` | Invalidate cross-species reuse | Model measures aligned amino acids, not target nucleotides | Supported |
| Boundary window was mislabeled | Historical `scripts/analyze.py:211–218`; candidate at 326 | Invalidate region annotation | Midpoint 336 lies before CDS start 338 although the window crosses the boundary | Supported |
| Independent URAT1-siRNA hypothesis survives | Current `README.md`; `surviving_scope` | Preserve the untested therapeutic hypothesis | Explicitly independent of COMP-009; no predictive use assigned | Supported |
| Guide design waits behind COMP-048 delivery | Current `README.md`; `successor` | Sequence future work behind the upstream delivery gate | Explicit successor and decision question named | Supported |

## Falsification, sensitivity, and output contract

The retirement has no result-bearing execution, parameter sensitivity, or generated output. Its falsification boundary is appropriately narrow: it invalidates what the historical implementation claimed to establish, not the URAT1-siRNA mechanism itself.

A future result cannot revive any retired guide merely by reproducing the old shortlist. Revival requires a new, independently reviewed design experiment using a validated current method, relevant transcript and human-variation coverage, transcriptome-wide off-target analysis, explicit accessibility criteria separated from other evidence dimensions, and empirical URAT1 knockdown.

The retirement record exposes the retired commit, per-file hashes, invalidated scope, surviving scope, successor, and deterministic canonical digest. That is sufficient to audit the non-runnable verdict.

## Downstream authoring contract

The focused computational page is the evidence home for COMP-009’s invalidated verdict. The siRNA/URAT1 modality page owns the surviving hypothesis, delivery dependency, and conditional guide-design gate.

The retirement names all nine correction surfaces:

- `wiki/urat1-sirna-target-site-selection-computational.md`
- `wiki/sirna-urat1-modality.md`
- `wiki/hypotheses/H03-sirna-urat1-thesis.md`
- `wiki/chassis-pending-interventions.md`
- `wiki/computational-experiments.md`
- `wiki/open-questions.md`
- `operations/operational-search-template.md`
- `operations/todos.md`
- `index.md`

Those surfaces may retain no candidate sequence, rank, score, shortlist, GREEN/viable label, accessibility or tractability conclusion, H03 support, or P2-2 closure derived from COMP-009. They may retain only the independent URAT1-siRNA hypothesis, its delivery-first dependency, and the future discriminating work. No cross-track ranking, treatment instruction, or historical COMP result should survive as current scientific evidence.

## Required actions before execution

None.

## Review limits

This was a static retirement review. No retired code was executed, and no attempt was made to reproduce historical outputs. The primary-method comparison was limited to Reynolds, Ui-Tei, and Tafer as requested; no broad literature scan was performed. Downstream correction files were named by the design but were not included in this two-file pre-run manifest, so their completed textual reconciliation remains a later exact-snapshot review concern.
