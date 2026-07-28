# comp-017 — Intestinal ABCG2 sex-difference evidence audit

**Status:** Active qualitative evidence-audit artifact; the direct-human question is unresolved.

**Verdict boundary:** Direct healthy-human intestinal ABCG2 sex-stratification remains unresolved. The prior run extracted neither sex-stratified GTEx intestinal distributions nor sex-stratified HPA intestinal protein values, so it did not test the prespecified 1.5-fold population threshold. The retained literature can supply a qualitative cross-species prior only.

## Question and decision

1. **Direct human question:** Do healthy-human intestinal ABCG2 distributions differ by at least 1.5-fold between sexes?
2. **Evidence-audit question:** What source-bounded corrections survive from the four committed Hoque, Liu, Slepnev, and MacLean records?

The direct human question is resolved only if sex-stratified intestinal values are present and a declared population model tests the threshold. Their absence forces `DIRECT_HUMAN_BASELINE_UNRESOLVED`; secondary, animal, disease-state, hepatic, or snippet-tier evidence cannot substitute.

## Inputs and provenance

- `inputs/gtex_data.json` records that no direct sex-stratified GTEx intestinal values were extracted.
- `inputs/hpa_data.json` records that no direct sex-stratified HPA intestinal protein values were extracted.
- `inputs/full_text_extract.json` is a legacy filename containing mixed-tier records: Hoque and Liu were verified against primary full text, Slepnev against publisher abstract and metadata, and MacLean against the primary PubMed abstract. Each record carries its own verification tier.
- `inputs/provenance.md` records access routes and exact verification limits.

The English translation of the 2023 Caco-2 paper at DOI `10.1134/S1990747823050100` is by **Slepnev et al.**, not Klyushova et al. The minimum tested hormone concentration was a nominal **1 µM** in culture. COMP-017 will not report a serum-total or serum-free testosterone multiplier: nominal culture concentration is not measured free-tissue exposure, and the prior multiplier mixed total and free bases.

## Model, rules, and assumptions

`analyze.py` is a deterministic validator and renderer. It:

1. checks whether direct GTEx or HPA sex-stratified intestinal values exist;
2. refuses a quantitative human verdict when they do not;
3. normalizes the four paper records while preserving their recorded extraction tier;
4. requires `abstract_vs_fulltext_difference` at its corrected top-level P01 location;
5. separates healthy-human baseline, healthy-rat baseline, Q140K disease-state mouse evidence, nominal in-vitro Caco-2 exposure, and out-of-scope clomiphene/intervention claims;
6. requires the expected P01–P04 records, per-record verification tiers and evidence levels, exact no-data statuses for Part A, and a single input-owned set of evidence boundaries.

It does not weight evidence by string counts, infer an effect from source absence, estimate physiological hormone exposure, or select an intervention.

## Sensitivity and invalidation boundaries

- Changing the 1.5-fold threshold cannot produce a verdict while direct values are absent.
- A future direct-human analysis requires fixed dataset accession/version, donor inclusion rules, sex variable provenance, tissue definitions, normalization, uncertainty estimates, and a prespecified model.
- Hoque's 78% jejunal and 44% renal values are like-for-like Western-blot comparisons. Article HTML/XML, the version-of-record PDF, supplementary information, and the publisher source-data workbook contain no 53% or 88% intestinal reduction. Those values entered COMP-016 as an explicitly unverified search-summary claim and were mislabeled as verbatim in historical COMP-017; they are excluded. The separately significant jejunal immunofluorescence reduction remains a distinct measurement without a reported percentage.
- MacLean's null is an **Animal Model** observation and cannot establish a human null.
- Slepnev's Caco-2 result is **In Vitro** at nominal 1, 10, and 100 µM hormone concentrations; it does not establish a physiological androgen effect, clomiphene mechanism, or human urate flux.
- COMP-017 cannot decide intervention selection, clomiphene guidance, a pan-male responder rule, or Q141K-conditioned uricase response ordering.

## Planned outputs

- `outputs/results.json` — schema-versioned machine-readable unresolved direct-human verdict, normalized source records, and scope boundaries. Version 2 intentionally replaces the incompatible historical keys.
- `outputs/summary.md` — the same result in concise human-readable form.

The single canonical evidence home is [`wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`](../../../intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md). Proposed dependent deltas after execution are:

- [`wiki/computational-experiments.md`](../../../computational-experiments.md) — replace the quantitative-null status with the unresolved-human status and link to the evidence home.
- [`wiki/abcg2-modulators.md`](../../../abcg2-modulators.md) — correct Slepnev attribution, nominal exposure, non-exclusive receptor interpretation, and human-baseline boundary; link to the evidence home.
- [`wiki/androgen-urate-axis.md`](../../../androgen-urate-axis.md) — make the same local attribution and AR-scope correction; link rather than copy the audit.
- [`wiki/t-abcg2-suppression-evidence-mining-computational.md`](../../../t-abcg2-suppression-evidence-mining-computational.md) — preserve COMP-016 as a historical bounded scan, mark COMP-017 as superseding only its ABCG2 sex-difference interpretation, and link to the evidence home.
- [`wiki/etc/manual-literature-mining.md`](../../manual-literature-mining.md) — correct the author attribution and clarify that the bounded scan rejected a supported direct-suppression claim but did not resolve healthy-human baseline magnitude.

Dependents receive only a correction/status plus link. They receive no duplicated exposition, cross-track ranking, intervention advice, clomiphene guidance, pan-male rule, or Q141K-conditioned uricase-response ordering. Adjacent untested conjectures are neither decided nor deleted by this audit.

## Reproduction

Execution requires a passing current Gate 1 receipt:

```bash
cd wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining
python3 analyze.py
```

Run twice and compare output hashes. This command performs no network retrieval.
