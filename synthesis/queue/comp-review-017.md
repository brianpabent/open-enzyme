---
type: comp-review
comp: comp-017
source_commit: 0ef99dcc9102323608fc4e5384e09617e95e17e8
propagation_eligibility: eligible_with_warning
synthesis_eligibility: blocked
---

# Current independent artifact review: comp-017

Current receipt: [`wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/reviews/push-review.md`](../../wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/reviews/push-review.md)

**Why action remains open:** **Quantitative verdict invalid.** comp-017 is useful as a qualitative literature-reframing artifact, especially against the old direct androgen/AR-suppression model, but it does **not** resolve its stated Part A question: healthy-human GTEx/HPA sex-stratified intestinal ABCG2 distributions were not directly mined, and no ≥1.5× human intestinal population threshold was tested. The artifact’s generated outputs still overstate “full-text” provenance and contain a schema bug that drops the Hoque abstract-vs-fulltext correction from generated summaries.

## Required actions

1. Fix `analyze.py` or input schema so P01 top-level `abstract_vs_fulltext_difference` is emitted into `results.json` and `summary.md`; verify Hoque 78% vs 88% wording appears in generated output.
2. Replace “full-text re-read/full-text-tier verification” language in generated outputs and README with “WebSearch snippet-tier extraction” unless line-anchored primary full text is actually inspected.
3. Downgrade the generated overall verdict wording: state that direct GTEx/HPA human intestinal sex-stratified data were not extracted and the healthy-baseline null is a qualitative provisional synthesis.
4. Standardize Klyushova testosterone multiplier language across comp outputs and `abcg2-modulators.md`, specifying basis: total vs free testosterone and 1 µM minimum active concentration.
5. Tighten affected wiki wording so Hoque/Q140K disease-state sex dimorphism is not read as healthy-baseline human intestinal sex dimorphism.
6. Do not synthesize comp-017 into intervention selection, clomiphene guidance, Q141K uricase response ordering, or pan-male responder/non-responder rules.
