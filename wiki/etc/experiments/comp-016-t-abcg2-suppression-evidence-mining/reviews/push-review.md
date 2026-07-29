COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: c7a3227c87ed0d954f6d7e73c4a83a297eca0faa99e817caadad80b6a806f4fb
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of the fixed-inventory COMP-016 boundary and corrected source anchors
SYNTHESIS_ALLOWED_SCOPE: none
FORBIDDEN_INFERENCES: literature-wide absence of androgen-suppression studies; healthy-human intestinal ABCG2 sex null; physiological human testosterone increase of intestinal ABCG2; male-specific quantified gut export ceiling; clomiphene mechanism or treatment implication; mechanistic ChIP-seq/ARE absence beyond the fixed inventory; use of legacy-summary rows as mechanistic evidence

# Independent comp review — comp-016

## Reviewed snapshot
Independent daemon review for COMP-016; reviewed snapshot bound to `push-review.manifest.json` SHA-256 `c7a3227c87ed0d954f6d7e73c4a83a297eca0faa99e817caadad80b6a806f4fb` at source commit `14833b44e90fe92f7aa6738a3f85edde188dabe9`. Shard coverage reported complete inspection of the listed text files and no deterministic binary blocks. Targeted repository cross-check reopened key files. Snapshot was treated as matched to inspected files.

## Bottom-line verdict
Action required. The repaired COMP-016 artifact supports a narrow fixed-inventory result: no record in the 17-record inventory directly demonstrates androgen-driven suppression of intestinal ABCG2; this is not a universal literature absence, not a healthy-human sex-stratification result, and not a quantitative physiology result. The core artifact is bounded and mostly internally coherent, but downstream wiki text overstates mechanistic absence/legacy evidence and imports adjacent quantitative claims without adequate provenance separation. Synthesis should be blocked until those surfaces are corrected.

## Implementation and constraint closure
`analyze.py` loads `inputs/studies.json`, validates schema version 2, exactly 17 records, allowed `test_class`, `target_outcome`, `verification_tier`, strict Boolean fields, direct-test requirements, citable constraints, and unresolved-placeholder constraints. It computes direct in-vivo/in-vitro records, direct suppressions, `result_code`, counts, corrected findings, record classifications, `results.json`, and `summary.md`. The decision rule is explicit: only direct `in_vivo` or `in_vitro` records with `target_outcome=decrease` demonstrate direct suppression.

Important limitation: this is a repaired fixed-inventory classifier, not a literature retrieval workflow. It can kill only the premise “direct androgen suppression of intestinal ABCG2 is established by this scan.” It cannot close the broader literature, healthy-human baseline magnitude, physiological exposure response, AR involvement, ChIP-seq/ARE status, clomiphene mechanism, or functional urate flux.

Implementation closure concern: `results.json` `record_classifications` omit `verification_tier`, although the summary table includes verification and the README planned source-verification tiers. This does not change the computed verdict because `corrected_source_findings` and summary retain tiers, but it weakens machine-readable auditability.

Constraint closure: COMP-016 is not a reaction-capacity or mass-balance experiment. It does not measure urate transport, epithelial localization, apical ABCG2 protein, residence time, Km/transport operating regime, free hormone/tissue concentrations, coproducts, or safety. Its biology is evidence-classification only. The only direct target record is Slepnev 2023, official-English-abstract tier, Caco-2 nominal 1/10/100 µM sex steroid exposure, reporting increase rather than decrease; it does not establish physiological exposure or exclude androgen receptor involvement.

## Summary-fidelity audit
Artifact summary and `results.json` agree on the narrow result: `NOT_DEMONSTRATED_IN_FIXED_INVENTORY`, 17 records, 16 citable, 0 direct in-vivo tests, 1 direct in-vitro test, and 0 direct decreases. Corrected anchors are Hoque 78% jejunal vs 44% renal Western reduction in Q140K+/+ mice, Liu 100 µM estradiol-benzoate Caco-2 mRNA increase without dose-dependence, Slepnev nominal hormone Caco-2 ABCG2 increase, and MacLean healthy-rat qualitative null.

Downstream mismatches requiring action:
- `wiki/abcg2-modulators.md` says “No published ChIP-seq study in that scan located a classical androgen-response element.” The COMP-016 inventory contains no citable ChIP-seq record; this is stronger than the repaired artifact supports. It should be rewritten as “the fixed inventory did not supply a citable direct promoter/ARE record,” or removed.
- `wiki/abcg2-modulators.md` calls Jeong 2015 the “closest mechanistic anchor” for an indirect CREB/CRTC2 axis. In COMP-016 it is a legacy-search-summary adjacent row, not a source-verified mechanistic finding. This must not be presented as a COMP-016-supported mechanistic anchor unless independently sourced outside COMP-016.
- `wiki/abcg2-modulators.md` includes an 84.2% modeled jejunal urate-flux reduction in the Hoque paragraph. That value is supported on the COMP-017 human/animal evidence page, not by COMP-016’s retained corrected source anchors, which preserve only the 78% jejunal and 44% renal Western comparison. If retained, provenance must point to the separate COMP-017/source-workbook verification and maintain genotype-stressed mouse boundaries.

Other reviewed pages generally preserve the repaired boundary: `wiki/computational-experiments.md`, `wiki/t-abcg2-suppression-evidence-mining-computational.md`, `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`, and `wiki/open-questions.md` state the fixed-inventory and unresolved-human limitations.

## Reader-facing ownership audit
The COMP page owns its evidence-inventory result and forbidden inferences. `abcg2-modulators.md` is a focused mechanism page and may summarize hormone context only if it owns evidence levels, provenance, tissue/exposure boundaries, and falsification gates. It currently drifts into unsupported mechanistic narrative around ChIP-seq and Jeong, and mixes COMP-016/COMP-017 quantitative anchors without adequate ownership separation.

Portfolio/index pages reviewed mostly keep COMP-016 as historical/bounded rather than using it as a ranking or treatment surface. No personalized treatment instructions were found in the inspected COMP-016 surfaces. The proposed use of validation §1.14/direct apical-protein and urate-flux measurement is appropriate as the falsification gate.

## Conjecture preservation audit
The unsupported factual claim that COMP-016 establishes absence of a ChIP-seq/ARE record should be corrected, not used as a mechanistic conclusion. Jeong 2015 may survive as a compact research lead only if independently sourced and explicitly labeled non-intestinal/prostate-cancer, legacy or primary-source status clarified, and not presented as a COMP-016 mechanistic anchor.

The negative COMP-016 result kills only the claim that this fixed inventory demonstrates direct androgen-driven intestinal ABCG2 suppression. It does not kill adjacent androgen–urate cohort relevance, renal hormone mechanisms, healthy-human intestinal sex-stratification questions, clomiphene-urate coupling hypotheses, or direct enterocyte hormone/TNFα factorial experiments. Those survive as bounded conjectures requiring direct apical ABCG2 protein and urate-flux measurement.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/README.md` | experiment documentation | yes | Bounded fixed-inventory framing reported by shard; no blocker. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/analyze.py` | experiment code | yes | Validates schema and renders outputs; no retrieval; result limited to fixed inventory. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/maintenance-repair-plan-2026-07-29.md` | input/provenance support | yes | Repair context inspected by shard; no independent blocker reported. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/provenance.md` | input/provenance support | yes | Source-tier corrections inspected by shard; primary-source verification not independently repeated here. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/studies.json` | input data | yes | 17-record fixed inventory; source classifications are load-bearing. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/results.json` | generated_output | yes | Correct bounded result; `record_classifications` omit `verification_tier`. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/summary.md` | generated_output | yes | Faithful bounded summary and forbidden inferences. |
| `wiki/abcg2-modulators.md` | proposed_update / affected wiki | yes | Change required: ChIP-seq/ARE, Jeong mechanistic-anchor, and Hoque flux provenance issues. |
| `wiki/androgen-urate-axis.md` | proposed_update / affected wiki | yes | Inspected by shard; no material COMP-016 drift reported. |
| `wiki/computational-experiments.md` | proposed_update / index surface | yes | Consistent; preserves COMP-016 and COMP-017 boundaries. |
| `wiki/etc/manual-literature-mining.md` | method/governance surface | yes | Consistent; reinforces primary-source verification and Tier 0 limitations. |
| `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` | affected wiki | yes | Consistent; keeps healthy-human sex stratification unresolved and Hoque provenance separate. |
| `wiki/open-questions.md` | affected wiki | yes | Consistent; uses COMP-016 only as bounded evidence scan. |
| `wiki/t-abcg2-suppression-evidence-mining-computational.md` | interpretive COMP page | yes | Consistent; correct fixed-inventory and forbidden-inference framing. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Fixed inventory size = 17 | `studies.json`, `analyze.py`, outputs | Enforced by validator; counts output | Directly inspectable in artifact | Supported. |
| Direct suppression requires direct in-vivo/in-vitro test with `target_outcome=decrease` | `analyze.py`, `decision_rule` | Determines `result_code` | Directly inspectable code | Supported as a classification rule. |
| No direct in-vivo tests; one direct in-vitro test S04; zero decreases | `results.json`, `summary.md` | Main result | Derived from inspected fixed records; no retrieval | Supported within fixed inventory. |
| S04 Slepnev: nominal 1/10/100 µM sex steroids increased Caco-2 ABCG2 | `studies.json`, outputs | Only direct target record; outcome `increase` | Official publisher abstract tier, not primary full text | Usable only with official-abstract and exposure-boundary caveat. |
| Hoque: 78% jejunal vs 44% renal Western reduction in Q140K+/+ mice | corrected source anchors | Adjacent corrected quantitative anchor | Marked primary full text; primary re-verification not performed by this reviewer | Supported as artifact-retained primary-tier anchor; animal genotype-stressed only. |
| Hoque: 84.2% modeled jejunal urate flux reduction | `abcg2-modulators.md`; COMP-017 page | Not generated by COMP-016 | Supported, if at all, by COMP-017/source-workbook boundary, not COMP-016 | Requires provenance separation on `abcg2-modulators.md`. |
| Liu: 100 µM estradiol benzoate increased Caco-2 ABCG2 mRNA without dose-dependence | corrected source anchors | Adjacent corrected anchor | Marked primary full text; primary re-verification not performed here | Supported only as pharmacological in-vitro estradiol result. |
| MacLean: healthy-rat intestinal transporter scan reported no sex-specific difference | corrected source anchors | Adjacent null context | Primary database abstract tier | Not a healthy-human effect-size estimate. |
| ChIP-seq/ARE absence | `abcg2-modulators.md` | Downstream mechanistic summary | No citable ChIP-seq record in COMP-016 artifact | Unsupported as written. |
| Jeong 2015 indirect CREB/CRTC2 “closest mechanistic anchor” | `abcg2-modulators.md`; record S07 | Downstream mechanism narrative | Legacy-search-summary adjacent row in COMP-016 | Unsupported as COMP-016 mechanistic finding. |
| Machine-readable verification tiers in all classifications | README expectation, `summary.md`, `results.json` | Auditability | Summary has tiers; `record_classifications` lacks them | Action recommended for `results.json`. |

## Affected wiki pages
- `wiki/abcg2-modulators.md` — change required — overstates COMP-016 ChIP-seq/ARE absence, uses a legacy-summary Jeong row as mechanistic anchor, and imports Hoque 84.2% flux without explicit COMP-017/source provenance separation.
- `wiki/androgen-urate-axis.md` — already consistent — shard inspection found no material drift from COMP-016 boundaries.
- `wiki/computational-experiments.md` — already consistent — states COMP-016 as historical/bounded; rejects unsupported 53%/88% Hoque values; preserves unresolved healthy-human question and COMP-017 limitations.
- `wiki/t-abcg2-suppression-evidence-mining-computational.md` — already consistent — accurately states fixed-inventory negative result and forbidden inferences.
- `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` — already consistent — keeps healthy-human intestinal ABCG2 sex difference unresolved and anchors Hoque quantitative details separately.
- `wiki/open-questions.md` — already consistent — uses COMP-016 only as a bounded scan in genotype/substrate-supply context.
- `wiki/etc/manual-literature-mining.md` — already consistent — its primary-source verification rules support the required correction.

## New connections or implications
A useful cross-page implication is that COMP-016 and COMP-017 together force a two-step resolver for androgen/sex ABCG2 claims: first extract direct healthy-human intestinal sex-stratified RNA/protein/apical localization/flux data, then separately test hormone exposure in enterocyte models under physiologic free-exposure conditions. Animal Q140K genotype-stress and Caco-2 pharmacological hormone responses cannot substitute for either step.

Research Conjecture boundary: if Jeong 2015 remains scientifically interesting, it should be reframed as a non-intestinal prostate-cancer androgen-withdrawal signaling precedent that might motivate, but does not support, enterocyte AR/CREB/CRTC2 testing. The discriminating observation is direct intestinal epithelial hormone manipulation with AR perturbation, apical ABCG2, and ABCG2-attributed urate flux.

## Required actions
1. In `wiki/abcg2-modulators.md`, revise the ChIP-seq/ARE sentence to avoid claiming published-study absence or promoter-location nonfinding unless a citable ChIP-seq/promoter source is added and verified. Verification criterion: wording is limited to “not established by COMP-016 fixed inventory” or independently sourced.
2. In `wiki/abcg2-modulators.md`, remove or relabel Jeong 2015 as a COMP-016 legacy-adjacent, non-intestinal lead rather than “closest mechanistic anchor,” unless primary-source verification is added outside COMP-016. Verification criterion: no legacy-summary row carries mechanistic authority.
3. In `wiki/abcg2-modulators.md`, attach the 84.2% modeled jejunal urate-flux number to the correct COMP-017/source-workbook provenance or remove it from the COMP-016-context paragraph. Verification criterion: readers can distinguish COMP-016 Western-only corrected anchor from COMP-017 flux/source verification.
4. Update `outputs/results.json` generation or schema so `record_classifications` include `verification_tier`, matching the summary’s auditability. Verification criterion: rerendered `results.json` exposes verification tier for each classification row.
5. Do not enable synthesis from COMP-016 until the above summary-fidelity corrections are reviewed.

## Review limits
Arbitrary experiment code was not executed in daemon mode. Primary articles were not independently re-read; source tiers and corrected anchors were evaluated by artifact inspection and shard reports. Repository fixed-string search failed because the underlying `rg` executable was unavailable; targeted `read_file` cross-checks were used instead. No binary artifacts or deterministic blocks were present.
