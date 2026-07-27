COMP_VERDICT: quantitative_verdict_invalid
REVIEWED_SNAPSHOT: d48d5ef4581bf789a91d28a3397ee04ba7a0fd5421f3202203f01dbcd10ec209
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of provenance limits, no direct GTEx/HPA quantitative result, Hoque 78% vs 88% clarification, supraphysiological hormone-exposure caveats, and rejection of direct AR-mediated intestinal ABCG2 suppression
SYNTHESIS_ALLOWED_SCOPE: none
FORBIDDEN_INFERENCES: quantified healthy-human intestinal ABCG2 sex-null; resolved GTEx/HPA population effect size; physiological estradiol/testosterone regulation magnitude from 100 µM or 1–100 µM cell assays; clomiphene urate mechanism or intervention recommendation; pan-male non-responder rule; Q141K genotype-response ordering for gut-lumen uricase

# Independent comp review — comp-017

## Reviewed snapshot
Independent daemon consolidation reviewer; reviewed snapshot bound to `push-review.manifest.json` SHA-256 `d48d5ef4581bf789a91d28a3397ee04ba7a0fd5421f3202203f01dbcd10ec209` at source commit `0ef99dcc9102323608fc4e5384e09617e95e17e8`. Authoring gates are reported modern/valid. Shard coverage plus targeted re-reads matched the inspected text files. No deterministic binary blocks were reported.

## Bottom-line verdict
**Quantitative verdict invalid.** comp-017 is useful as a qualitative literature-reframing artifact, especially against the old direct androgen/AR-suppression model, but it does **not** resolve its stated Part A question: healthy-human GTEx/HPA sex-stratified intestinal ABCG2 distributions were not directly mined, and no ≥1.5× human intestinal population threshold was tested. The artifact’s generated outputs still overstate “full-text” provenance and contain a schema bug that drops the Hoque abstract-vs-fulltext correction from generated summaries.

## Implementation and constraint closure
Traced `inputs/gtex_data.json`, `hpa_data.json`, and `full_text_extract.json` through `analyze.py` into `outputs/results.json` and `outputs/summary.md`.

Key closure failures:
- **Part A substitution:** direct GTEx/HPA healthy-human sex-stratified intestinal expression/protein values are null or “not directly extracted.” The implementation substitutes secondary literature/snippet consensus plus animal and hepatic-adjacent evidence for direct human intestinal dataset mining.
- **Aggregation bug:** `aggregate_part_b()` reads `p["full_text_extract"]["abstract_vs_fulltext_difference"]`; P01 Hoque stores that field top-level. Generated outputs therefore show P01 `abstract_vs_fulltext_difference: null`, omitting the load-bearing 78% Western-jejunum vs 88% combined-measurement clarification.
- **Evidence counting is not quantitative:** `null_baseline_hits` is a string-match count over secondary facts, not a weighted, independent, tissue-specific evidence model.
- **Schema drift:** code docstring lists verdict options, but emitted verdict code is a longer non-enumerated string. Downstream consumers should not treat it as one of the declared codes.
- **Reproduction caveat:** script is stdlib-only and plausibly deterministic if run from the committed directory with `outputs/` present, but it does not create `outputs/`. I did not execute code.

Constraint closure:
- **Concentration/exposure:** Yu 2021 Caco-2 estradiol benzoate effect is at 100 µM; Klyushova sex-hormone assays are 1–100 µM. These are pharmacological/supraphysiological cell exposures, not proof of physiological serum-hormone regulation of intestinal ABCG2.
- **Compartment/species:** MacLean/Tubic are rat intestinal baseline data; Hoque is Q140K mouse disease-state genetic stress; Prasad hepatic human protein is adjacent-tissue evidence, not intestinal validation.
- **Mechanism polarity:** Klyushova argues against direct AR-mediated suppression in Caco-2 under tested supraphysiological conditions; it does not directly test clomiphene, human urate flux, or physiologic testosterone variation.
- **Mass balance/transport/function:** no finite human intestinal urate flux model, residence time, genotype response, or uricase response prediction is implemented.

## Summary-fidelity audit
Generated `summary.md` mostly mirrors `results.json`, so it inherits the P01 omission, “full-text-tier” overstatement, and Part A substitution.

Current wiki surfaces are materially improved compared with the raw artifact: the interpretive stub explicitly warns that comp-017 does **not quantitatively resolve** GTEx/HPA human intestinal sex stratification, and the computational index labels the verdict provisional with direct GTEx/HPA blocked. However, the index still headlines “NULL OR NEAR-NULL at healthy baseline,” which is acceptable only as a provisional qualitative synthesis, not as a resolved database-mining result.

`androgen-urate-axis.md` largely preserves the correct boundary: direct androgen suppression of intestinal ABCG2 is unsupported; clomiphene urate effect is unknown; measurement gates remain. `abcg2-modulators.md` is broadly reconciled but has wording that could be misread as baseline intestinal sex dimorphism unless Q140K/disease-state context is kept explicit. No page may reuse comp-017 as quantitative human GTEx/HPA proof.

## Reader-facing ownership audit
The comp-specific interpretive page is now mostly a discoverability stub and appropriately owns the caveat. Cross-track ranking and intervention selection are not placed on the comp page. The index’s compact summary is acceptable only with its provisional qualifier retained.

No comp-017-derived personalized treatment instruction is supported. Affected pages should avoid narrative foils such as “male ceiling” or “pan-androgen-dominant non-responder” unless explicitly marked as retracted/unsupported. Portfolio or genotype-response claims belong on comparison/validation surfaces, not on comp-017.

## Conjecture preservation audit
Unsupported factual assertions should be corrected, not deleted wholesale:
- Killed: “direct androgen/AR suppression of intestinal ABCG2” as a supported mechanism; “healthy-human GTEx/HPA quantitative null resolved”; “clomiphene causes high UA through intestinal ABCG2” as established.
- Preserved as bounded conjecture: Q141K/Q140K male vulnerability may be a disease-state genetic-stress interaction; physiological estrogen/PI3K/Akt intestinal ABCG2 activity could exist but magnitude is unmeasured; hormone state may be a stratification variable requiring direct urate-flux and hormone measurements.
- Adjacent gut-lumen uricase/genotype response ideas survive only as prospective stratification hypotheses, not as response ordering or dose rules.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/results.json` | generated_output | yes | Quantitative Part A verdict unsupported; P01 correction dropped; provenance overstated. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/outputs/summary.md` | generated_output | yes | Faithful to flawed JSON; inherits P01 omission and “full-text” overclaim. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/README.md` | experiment artifact | yes | States provisional direct-GTEx limitation but still titles method as full-text re-read. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/analyze.py` | experiment artifact | yes | Deterministic aggregator; schema bug; output dir assumption. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/full_text_extract.json` | experiment input | yes | Snippet-tier, not Paperclip/full-text grep; several mechanistic inferences too strong. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/gtex_data.json` | experiment input | yes | Direct GTEx values absent. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/hpa_data.json` | experiment input | yes | Direct sex-stratified intestinal HPA protein absent. |
| `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/provenance.md` | experiment input | yes | Citation trail only; many primary values unverified. |
| `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` | proposed/affected update | yes | Correctly caveats non-quantitative status. |
| `wiki/computational-experiments.md` | proposed/affected update | yes | Mostly consistent; headline needs provisional interpretation only. |
| `wiki/androgen-urate-axis.md` | proposed/affected update | yes | Consistent with no AR-suppression and clomiphene unknown. |
| `wiki/abcg2-modulators.md` | proposed/affected update | yes | Mostly reconciled; baseline-vs-Q140K wording needs care. |
| `wiki/gout-genetic-variants.md` | affected update | yes | Correctly keeps Q141K prospective, not response-ordering. |
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` | affected update | yes | Correctly depends on comp-017 correction lifecycle. |
| `wiki/open-questions.md` | affected update | yes | No comp-017-specific contradiction; contains unrelated portfolio caveats. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Direct healthy-human GTEx intestinal sex-stratified ABCG2 TPM | `inputs/gtex_data.json` | `gtex_direct_data = null` | Not extracted; sandbox blocked | Cannot support quantitative Part A verdict |
| Direct HPA sex-stratified intestinal ABCG2 protein | `inputs/hpa_data.json` | reported as not directly extracted | Not available at artifact tier | Cannot support protein sex-null |
| Healthy baseline null/near-null | `results.json` overall verdict | emitted as headline | Indirect snippets; rat data; secondary literature; hepatic-adjacent human | Qualitative/provisional only |
| Hoque Q140K jejunum Western decrease 78% vs kidney 44% | `full_text_extract.json` P01 | should appear in summary; bug omits abstract-vs-fulltext note | Snippet quoting source; not independently primary-verified here | Usable as snippet-tier correction, not full-text-verified |
| Hoque 88% intestinal decrease | P01 combined measurement | included in key findings | Snippet-tier | Must not be used as like-for-like Western-vs-renal contrast |
| Yu EB 100 µM Caco-2 ABCG2 induction | P02 | supports pharmacological E2 mechanism caveat | Snippet-tier | Supports supraphysiological in-vitro mechanism only |
| Klyushova 1–100 µM T/E2/P induction via PXR/FXR | P03 | supports anti-AR-suppression rationale | Snippet-tier; fold changes absent | Rejects tested AR-suppression framing; no physiologic magnitude |
| MacLean healthy-rat intestinal ABCG2 no sex difference | P04 / GTEx secondary | counted as null-baseline hit | Snippet/citing context; p-values absent | Qualitative animal baseline evidence |
| Tubic “replication” of ABCG2 null | `gtex_data.json`, P04 notes | strengthens null narrative | Inferred from non-reporting/context | Weaker than direct replication unless directly verified |
| Hosoyamada renal URAT1 mRNA not protein under baseline | outputs/wiki | used for renal mechanism correction | Related literature, outside 4 anchors | Useful only with explicit bounded role |

## Affected wiki pages
- `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` — already consistent — explicitly says no quantitative GTEx/HPA resolution.
- `wiki/computational-experiments.md` — change required — preserve provisional label wherever headline “NULL OR NEAR-NULL” appears; do not let it read as resolved GTEx/HPA mining.
- `wiki/androgen-urate-axis.md` — already consistent — rejects direct androgen suppression and keeps clomiphene unknown.
- `wiki/abcg2-modulators.md` — change required — tighten any “intestinal ABCG2 is sex-dimorphic” wording to Q140K/disease-state context unless discussing baseline null separately.
- `wiki/gout-genetic-variants.md` — already consistent — Q141K remains prospective stratification, not predictor/order.
- `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` — already consistent — treats comp-017 as cleanup dependency, not validation.
- `wiki/open-questions.md` — already consistent for comp-017; unrelated inconsistencies noted by shard auditors should not be imported into comp-017 synthesis.

## New connections or implications
A useful design implication survives: future hormone/transporter experiments should not test only expression. They need physiological hormone concentration ladders, ABCG2 protein/localization, and basolateral-to-apical urate flux with genotype stratification. The strongest comp-017-supported negative is not “intestinal ABCG2 cannot matter,” but “sex or androgen state alone is insufficient to infer a healthy-baseline intestinal ABCG2 ceiling.”

## Required actions
1. Fix `analyze.py` or input schema so P01 top-level `abstract_vs_fulltext_difference` is emitted into `results.json` and `summary.md`; verify Hoque 78% vs 88% wording appears in generated output.
2. Replace “full-text re-read/full-text-tier verification” language in generated outputs and README with “WebSearch snippet-tier extraction” unless line-anchored primary full text is actually inspected.
3. Downgrade the generated overall verdict wording: state that direct GTEx/HPA human intestinal sex-stratified data were not extracted and the healthy-baseline null is a qualitative provisional synthesis.
4. Standardize Klyushova testosterone multiplier language across comp outputs and `abcg2-modulators.md`, specifying basis: total vs free testosterone and 1 µM minimum active concentration.
5. Tighten affected wiki wording so Hoque/Q140K disease-state sex dimorphism is not read as healthy-baseline human intestinal sex dimorphism.
6. Do not synthesize comp-017 into intervention selection, clomiphene guidance, Q141K uricase response ordering, or pan-male responder/non-responder rules.

## Review limits
I did not execute the experiment. Primary papers were not independently re-fetched or line-verified; provenance assessment is limited to committed text and shard audits. Repository fixed-string search tool failed because `rg` was unavailable, so affected-surface discovery rests on supplied shard coverage plus targeted `read_file` cross-checks. No binary artifacts were present.
