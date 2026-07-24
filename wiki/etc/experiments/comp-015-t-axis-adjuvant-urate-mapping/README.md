> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** The retired artifact converted heterogeneous literature records into compound-level categorical verdicts without preserving material identity, assay comparability, exposure, or a valid scoring basis.

# comp-015 — T-axis Adjuvant Urate-Target Mapping

**Status:** Invalidated for candidate comparison, compound-level gout-direction verdicts, H-AN-02 adjudication, evidence-cell counting, concentration-threshold inference, and experimental prioritization.

No `GOUT-FAVORABLE`, `MECHANISM-UNCLEAR`, uniqueness, “partially falsified,” evidence-count, candidate-priority, or genotype-aware selection conclusion survives.

The implementation combined purified compounds, botanical extracts, mixed quassinoid fractions, animal expression changes, cell-uptake assays, a human safety-laboratory table, negative screens, and mechanistic extrapolations as if they were commensurate compound-by-target observations. In particular, the `eurycomanone` row inherited results from 70% ethanol *Eurycoma longifolia* stem extract, isolated quassinoids as a class, purified eurycomanol, and Physta. Those are different materials.

The code also:

- treated `UNKNOWN — POSSIBLY INDUCER` as favorable because it searched direction text for favorable keywords;
- collapsed a negative screen into `No-Data`;
- assigned ordinal weights to heterogeneous evidence classes without validation;
- called a candidate `GOUT-FAVORABLE` from one favorable transporter label without a coherent exposure or whole-system model;
- estimated plasma concentration as dose × bioavailability ÷ volume of distribution, then treated concentration/IC50 ratios as fractional inhibition with an assumed Hill coefficient of one; and
- attributed its local ratio thresholds to COMP-007 even though COMP-007 did not implement them.

The artifact therefore cannot determine which candidate is more gout-favorable or whether cordycepin is unique. Its old executable files and outputs are retained in Git only.

## What survives

Three source-specific leads survive without a cross-candidate ranking:

1. **Cordycepin lead — Animal Model.** Yong et al. administered purified cordycepin at 15, 30, and 60 mg/kg in a mouse hyperuricemia model; serum urate was lower than hyperuricemic control and renal URAT1 mRNA/protein decreased (PMID 29422889). This does not establish human exposure, human urate lowering, or an androgen–urate dual benefit.
2. ***Eurycoma longifolia* extract/quassinoid lead — Animal Model + In Vitro.** Bao et al. tested a 70% ethanol stem extract at 100, 200, and 400 mg/kg in hyperuricemic rodents, with renal urate-transporter changes. In hURAT1-expressing cells, eurycomanol-type compounds 4–7 at 50 µM inhibited urate uptake; pure eurycomanone was compound 3 and showed comparatively low activity. Eurycomanol was then tested in vivo (PMID 31920654). Extract-level transporter effects and eurycomanol activity do not become pure-eurycomanone effects.
3. **Eurycomanol lead — Animal Model.** Bao et al. tested purified eurycomanol at 5–20 mg/kg orally in hyperuricemic mice and reported lower serum urate, increased urate clearance, decreased hepatic PRPS expression, and renal/intestinal transporter modulation (PMID 34785103). This does not establish a human effect or show that Physta acts through eurycomanol or PRPS.

The 2021 Physta trial enrolled 105 men and reported urate in a safety-outcomes table. At week 12, neither Physta arm differed from placebo for urate (100 mg, p=0.88; 200 mg, p=0.52), while the placebo arm also declined from baseline (PMCID PMC8254464). The table does not support a Physta urate-treatment effect or connect any observed value to eurycomanone, eurycomanol, transporters, or PRPS.

These observations remain leads because their exact materials, evidence levels, and compartments can motivate direct experiments. They do not restore the retired matrix or verdicts.

## Current evidence owners and correction cascade

The [focused COMP page](../../../t-axis-adjuvant-urate-mapping-computational.md) owns the invalidated verdict and source-specific surviving evidence. The [androgen-natural-modulation page](../../../androgen-natural-modulation.md) owns the compact Research Conjecture and the matched-identity wet-lab discriminator. The [validation plan](../../../validation-experiments.md) owns the experiment.

Correction targets in this retirement batch are:

- `wiki/t-axis-adjuvant-urate-mapping-computational.md`
- `wiki/computational-experiments.md`
- `wiki/androgen-natural-modulation.md`
- `wiki/medicinal-mushroom-complement-track.md`
- `wiki/prps-purine-biosynthesis-chokepoint.md`
- `wiki/gout-pathophysiology.md`
- `wiki/gout-kill-chain-delivery-routes.md`
- `wiki/gout-action-guide.md`
- `wiki/personal-genome-protocol.md`
- `wiki/validation-experiments.md`
- `wiki/etc/chembl-cross-check.md`
- `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/analyze.py`
- `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/results.json`
- `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/summary.md`
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md`
- `operations/notable-moments.md`
- `papers/cross-vendor-heterogeneity-guard/draft.md`
- `papers/cross-vendor-heterogeneity-guard/audit-2026-05-13-catch-history.md`
- `papers/cross-vendor-heterogeneity-guard/revisions.md`
- `papers/cross-vendor-heterogeneity-guard/figures/figure2_catches.py`
- `papers/cross-vendor-heterogeneity-guard/figures/figure2_catches.pdf`
- `papers/cross-vendor-heterogeneity-guard/figures/figure2_catches.png`
- `papers/future-work-pipeline.md`

References in historical review receipts remain review provenance, not active evidence. `operations/global-lit-scan-gap-audit-2026-05-20.md` preserves an unresolved multilingual search gap and does not reuse a retired verdict.

COMP-017's decision text is corrected through COMP-017's own exact-snapshot lifecycle before the COMP-015 queue item closes.

Before deleting `synthesis/queue/comp-review-015.md`, a repository-wide readback must show that every remaining COMP-015 or eurycomanone-verdict reference is corrected source-specific evidence, an explicitly untested conjecture, or clearly marked historical review provenance. All changed external surfaces are bound in the post-run manifest. After that readback and the independent post-run review pass, the queue file is deleted in the same commit.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds every retired non-review file to the exact pre-retirement Git tree by byte count and SHA-256 and defines the invalidated and surviving scopes.

There is no reproduction command. Git retains the retired code, inputs, outputs, and reviews.
