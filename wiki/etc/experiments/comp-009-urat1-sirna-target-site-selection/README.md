> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** COMP-009 does not establish a usable URAT1 siRNA guide, target-site tractability, accessibility, specificity, cross-species reuse, or support for H03.

# comp-009 — URAT1 mRNA Target-Site Selection

**Status:** Invalidated for every candidate sequence, filter funnel, rank, composite score, shortlist, GREEN verdict, target-site-availability conclusion, H03-support claim, and P2-2 closure.

The rerun corrected the original use of an artificial back-translated CDS by scanning RefSeq NM_144585.4, but the revised model still could not support its decision:

- The Reynolds implementation applied the cited sense-strand positional preferences to the antisense strand, omitted the source's terminal-stability and inverted-repeat criteria, and substituted a four-base homopolymer check.
- The Ui-Tei gate did not require the cited terminal-composition, A/U-richness, and long-GC-stretch rules simultaneously.
- The composite score combined raw RNAplfold unpaired probability with arbitrary, uncalibrated weights. Its protein-conservation term could dominate the target-accessibility term. This is not the RNAxs model calibrated and independently tested by Tafer et al.
- No transcriptome or 3′-UTR off-target clearance was performed, only one SLC22A12 transcript was scanned, protein conservation cannot establish cross-species siRNA reuse, and midpoint-based region annotation mislabeled a window spanning the 5′-UTR/CDS boundary.
- No candidate was tested for intracellular activity, URAT1 knockdown, target-cell uptake, urate transport, or renal safety.

The governing primary methods are [Reynolds et al. 2004](https://doi.org/10.1038/nbt936), [Ui-Tei et al. 2004](https://doi.org/10.1093/nar/gkh247), and [Tafer et al. 2008](https://doi.org/10.1038/nbt1404).

## What survives

The URAT1-siRNA hypothesis survives independently of COMP-009. The historical rerun did examine NM_144585.4, but that fact has no predictive or decision use and does not establish that SLC22A12 is tractable for therapeutic siRNA design.

Kidney-tropic delivery remains the upstream gate. [COMP-048](../comp-048-human-proximal-tubule-delivery-handle-screen/) is the planned human proximal-tubule delivery-handle screen. A new guide-design COMP is deferred until a delivery route survives. It must use a validated current design method, cover relevant SLC22A12 transcripts and human variation, perform transcriptome-wide off-target analysis, separate target accessibility from other evidence dimensions, and require empirical URAT1 knockdown before any guide advances.

## Current evidence owners and correction cascade

The [focused COMP page](../../../urat1-sirna-target-site-selection-computational.md) owns the invalidated verdict. The [siRNA/URAT1 modality page](../../../sirna-urat1-modality.md) owns the surviving track, delivery dependency, and conditional guide-design gate.

Correction targets in this retirement batch are:

- `wiki/urat1-sirna-target-site-selection-computational.md`
- `wiki/sirna-urat1-modality.md`
- `wiki/hypotheses/H03-sirna-urat1-thesis.md`
- `wiki/chassis-pending-interventions.md`
- `wiki/computational-experiments.md`
- `wiki/open-questions.md`
- `operations/operational-search-template.md`
- `operations/todos.md`
- `index.md`

References inside the retained review receipts are historical review provenance, not current scientific evidence. After the nine correction targets are reconciled, `synthesis/queue/comp-review-009.md` is deleted in the same commit.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds every retired non-review file to the exact pre-retirement Git tree by byte count and SHA-256 and defines the invalidated and surviving scopes.

There is no reproduction command. Git retains the retired code, inputs, outputs, and reviews.
