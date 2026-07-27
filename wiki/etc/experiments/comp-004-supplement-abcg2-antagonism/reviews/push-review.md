COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 5a9ca14cae9a8beb2f7bb4ca8ba3f56b4ca5ffff2772ffa24e637fcf05c1b4c0
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of comp-004 invalidation and direct-assay routing boundaries
SYNTHESIS_ALLOWED_SCOPE: none when based on downstream ABCG2/TCM rankings; bounded lead-inventory synthesis may resume only after stale comp-013/014/TCM surfaces are corrected
FORBIDDEN_INFERENCES: nominal gut-concentration/IC50 as intestinal urate-transport occupancy; percent ABCG2 urate inhibition; clinical-risk tiers; supplement dosing/formulation/genotype/patient direction; downstream viability rankings that count inherited comp-004 occupancy

# Independent comp review — comp-004

## Reviewed snapshot
Independent daemon review for `SOURCE_COMMIT` 0ef99dcc9102323608fc4e5384e09617e95e17e8, bound to push manifest SHA-256 `5a9ca14cae9a8beb2f7bb4ca8ba3f56b4ca5ffff2772ffa24e637fcf05c1b4c0`. Authoring gates were reported modern and valid. Shard auditors inspected the manifest text spans; I reopened comp-004 README, code, output summary, and interpretive page for targeted cross-checks. Repository fixed-string search was unavailable because the `grep_repo` backend lacked `rg`; this is a review tooling limit, not a deterministic block because shard coverage supplied broad affected-surface inspection and targeted files were reopened.

## Bottom-line verdict
Action required. The comp-004 artifact itself is a valid corrective audit: it invalidates the prior quantitative gut-lumen occupancy verdict and preserves only qualitative routing to direct intestinal urate-flux assays. However, downstream corpus surfaces still contain or inherit the forbidden inference class, especially comp-013/comp-014/TCM pages. Corrective propagation is eligible with warning; synthesis using ABCG2/TCM rankings is blocked until reconciled.

## Implementation and constraint closure
The computation asks whether three cited ABCG2/BCRP interaction records for quercetin, curcumin, and EGCG support quantitative prediction of intestinal urate-transport inhibition. That is a model-fit correction, not a de novo literature census or physiological simulation.

I traced `inputs/assay_evidence.json` through `analyze.py` to both outputs. The code checks schema version, exact compound set, duplicate compound records, controlled evidence levels, controlled urate-evidence status, Boolean intestinal-model flag, nonempty substrates, and nonempty source fields. It classifies any record lacking direct intestinal urate flux as `DIRECT_INTESTINAL_URATE_FLUX_ASSAY_REQUIRED`; if a record reports direct intestinal urate flux, it routes to `DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED`. It never computes occupancy, percent inhibition, clinical risk, genotype risk, or dose.

Important limitation: README says the code validates “structured source identifiers,” but implementation only checks nonempty citation, PMID, verified location, and optional DOI string. It does not validate PMID/DOI syntax, uniqueness, source-location vocabulary, or primary-source contents. Current records are safe enough for a bounded audit, but provenance strength is abstract-tier unless separately verified.

Constraint closure is scientifically appropriate for a negative/corrective audit. The artifact explicitly rejects substituting nominal bulk gut concentration for free enterocyte-surface exposure; drug-substrate IC50 for urate transport; non-intestinal/cancer-cell context for intestinal epithelium; and Hill occupancy for clinical direction. It also identifies missing substrates/context closure: urate itself, intestinal epithelial localization, ABCG2 attribution, parent/metabolite exposure, exposure time, protein/surface abundance, barrier integrity, viability, and basolateral-to-apical urate flux. No numerical sensitivity analysis is expected because the computation intentionally produces no numerical biological verdict.

## Summary-fidelity audit
Comp-004 README, `outputs/summary.md`, machine-readable audit, `wiki/supplement-abcg2-antagonism-computational.md`, `wiki/computational-experiments.md`, `wiki/validation-experiments.md` §1.14, and H04 are materially aligned: ratios, predicted inhibition percentages, and VERY_HIGH/clinical-risk labels are invalid; only direct-assay routing survives.

Material drift remains outside the core comp-004 page set:
- comp-013 README and output summary still contain inherited gut-concentration/IC50 occupancy ratios, Hill-equation thresholds, percent inhibition, VERY_HIGH/HIGH risk levels, and GUT-LUMINAL viability labels. These are not decision-usable under comp-004.
- comp-014 scope summary says the comp-004 supplement screen “validated this target” for ABCG2. That overstates support; comp-004 validates neither target tractability nor quantitative target priority.
- TCM pages contain additional priority/clinical-evidence drift unrelated to comp-004’s core artifact but relevant to synthesis safety: outdated candidate mechanism attributions, possible self-experiment framing, and clinical Si Miao San quantitative claims needing primary-source adjudication.

## Reader-facing ownership audit
The focused comp-004 interpretive page owns the evidence boundary and points to validation §1.14 for the falsification experiment. It does not offer personalized supplement instructions or clinical risk ranking. This satisfies the reader-facing contract.

The remaining ownership problem is downstream duplication and portfolio leakage. Comp-013 and comp-014 outputs act as if cross-track rankings and viability labels can inherit comp-004 occupancy calculations. Those rankings belong, if at all, only on portfolio comparison surfaces after mechanism-matched evidence is rebuilt. Focused TCM/chassis/intervention pages must own their evidence, exposure, safety, and falsification gates rather than narrating comp history or using invalid ABCG2 occupancy as a foil or shortcut.

## Conjecture preservation audit
The unsupported factual assertion killed by comp-004 is narrow: nominal supplement gut concentration divided by ABCG2 drug-substrate IC50 does not establish intestinal urate-flux inhibition, percent inhibition, risk tier, dose/formulation direction, genotype susceptibility, or clinical effect.

Adjacent conjectures survive if rewritten compactly and explicitly:
- Quercetin, curcumin, and EGCG have ABCG2/BCRP interaction signals in non-matched contexts.
- Exposure time, metabolites, and intestinal context could alter ABCG2 effects, including EGCG’s net direction.
- These ideas should be preserved only as Research Conjectures with sourced premises, an unsupported leap, upside, and a discriminating intestinal urate-flux observation.

The negative result does not prove the compounds are safe, unsafe, beneficial, or inert for gout; it only invalidates the tested shortcut and decision rule.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/README.md` | proposed update / experiment doc | Yes | Correct boundary; overstates source-identifier validation slightly. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/analyze.py` | experiment code | Yes | Implements qualitative audit; no forbidden quantitative calculation; weak source syntax validation. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/inputs/assay_evidence.json` | input | Yes | Three bounded records; abstract-tier source locations. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/inputs/provenance.md` | provenance | Yes | Supports retirement of IC50 averaging and EGCG sign-switch claims; downstream correction required. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/outputs/assay_evidence_audit.json` | generated output | Yes | Faithful to code/input; all three routed to direct intestinal urate-flux assay; no quantitative ranking. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/outputs/summary.md` | generated output | Yes | Faithful; preserves “not a literature census” and forbidden inference boundaries. |
| `wiki/supplement-abcg2-antagonism-computational.md` | proposed interpretive update | Yes | Correctly reports quantitative verdict invalid. |
| `wiki/computational-experiments.md` | proposed/index update | Yes | Current comp-004 entry consistent; comp-013 entry reportedly downgraded, but its experiment outputs remain stale. |
| `wiki/validation-experiments.md` | proposed validation update | Yes | §1.14 correctly requires measured exposure/metabolites and ABCG2-attributed urate flux; other sections contain unrelated issues requiring separate action before synthesis. |
| `wiki/open-questions.md` | proposed planning update | Yes | Correctly forbids comp-013 reuse of comp-004 shortcut and sets rebuilt triage requirements. |
| `wiki/tcm-gout-compound-triage-computational.md` | affected interpretive page | Yes | Correctly marks comp-013 viability ranking invalid, but underlying comp-013 outputs remain stale. |
| `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/README.md` | affected experiment doc | Yes | Change required: still uses comp-004 occupancy/Hill thresholds and GUT-LUMINAL viability. |
| `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/outputs/summary.md` | affected generated output | Yes | Change required or quarantine: contains forbidden ratios, percent inhibition, risk tiers, viability rankings. |
| `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/scope-summary.md` | affected generated output | Yes | Change required: “validated this target” overstates comp-004. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md` | affected provenance | Yes | No direct conflict; future reuse must inherit comp-004 boundary. |
| `wiki/hypotheses/H04-tcm-rigor-intersection.md` | affected hypothesis | Yes | Consistent; preserves exposure/function requirement. |
| `wiki/tcm-modern-rigor-intersection.md` | affected reader page | Yes | Change required for TCM candidate/status and reader-facing framing issues; comp-004 boundary partly represented. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Exact compounds are quercetin, curcumin, EGCG | `analyze.py`, `assay_evidence.json` | Hard-coded exact set check | Directly inspectable input/code | Verified for bounded set. |
| Cited records lack direct intestinal urate-flux evidence | `assay_evidence.json`, output records | Drives direct-assay routing | Source locations are “primary abstract”; primary full text not verified here | Usable only as abstract-tier bounded audit. |
| Nominal gut concentration/IC50 cannot quantify intestinal urate transport | README, summary, wiki page | Basis for invalidating prior quantitative verdict | Mechanistic reasoning in artifact; no primary-source verification needed for the computational-substitution critique | Valid corrective conclusion. |
| `quantitative_risk_rank_allowed: false` | `analyze.py`, audit JSON | Emitted for all dispositions | Directly inspectable | Verified. |
| Source identifier validation | README vs `analyze.py` | README says structured validation; code checks nonempty fields only | Inspectable mismatch | Limitation; action to qualify wording or strengthen code. |
| Direct follow-up requires free parent/metabolites, ABCG2 protein/attribution, barrier/viability, urate flux | README, summary, validation §1.14 | Not computed; stated falsification gate | Corpus design claim; primary method qualification not independently verified | Appropriate as next-gate design boundary. |
| comp-013 ABCG2 occupancy/viability ranking remains usable | comp-013 README/output | Downstream decision artifact | Contradicted by comp-004 | Invalid; action required. |
| comp-014 “comp-004 validated ABCG2 target” | comp-014 scope summary | Downstream target framing | Contradicted by comp-004 | Overstated; action required. |

## Affected wiki pages
- `wiki/supplement-abcg2-antagonism-computational.md` — already consistent — reports invalid quantitative method and direct-assay route.
- `wiki/computational-experiments.md` — already consistent for comp-004 — warns against ratios/risk labels; ensure stale comp-013 outputs are visibly quarantined.
- `wiki/validation-experiments.md` — already consistent for §1.14 — requires matrix-qualified exposure/metabolite and ABCG2-attributed urate flux; unrelated sections need separate review actions before broad synthesis.
- `wiki/open-questions.md` — already consistent — instructs rebuilt TCM triage without comp-004 shortcut.
- `wiki/hypotheses/H04-tcm-rigor-intersection.md` — already consistent — preserves measured free exposure and mechanism-matched endpoint requirements.
- `wiki/tcm-gout-compound-triage-computational.md` — already consistent at interpretive level — marks comp-013 ranking invalid; depends on correcting source outputs.
- `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/README.md` — change required — still encodes invalid occupancy/Hill/viability framework.
- `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/outputs/summary.md` — change required — contains forbidden ratios, percent inhibition, risk tiers, and rankings.
- `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/scope-summary.md` — change required — replace “validated this target” with “identified direct urate-flux assay requirement.”
- `wiki/tcm-modern-rigor-intersection.md` — change required — update outdated candidate attributions and remove/qualify self-experiment or unadjudicated clinical claims.

## New connections or implications
Comp-004’s correction applies beyond supplements: any natural-product triage that uses transporter occupancy from nominal luminal concentration and off-substrate IC50 needs measured free exposure and a context-matched functional endpoint before ranking.

Research Conjecture boundary: polyphenol ABCG2 interactions may matter for intestinal urate handling if free parent/metabolite exposure at the enterocyte surface overlaps an urate-transport-relevant operating range and changes ABCG2-attributed basolateral-to-apical urate flux without barrier/viability artifacts. The discriminating observation is a prespecified intestinal epithelial flux assay with exposure analytics and ABCG2 attribution.

## Required actions
1. Correct or quarantine `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/README.md` and `outputs/summary.md`: remove decision use of comp-004-derived occupancy ratios, Hill percent inhibition, VERY_HIGH/HIGH risk tiers, and GUT-LUMINAL viability labels; verification criterion is no remaining claim that nominal gut-concentration/IC50 supports biological viability or hazard ranking.
2. Correct `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/scope-summary.md`: replace “comp-004 validated this target” with the bounded conclusion that comp-004 invalidated quantitative ABCG2 shortcut and routed to direct urate-flux assays.
3. Qualify comp-004 README wording or strengthen code: either state that source metadata validation is nonempty-field validation only, or add PMID/DOI/location vocabulary validation and regenerate outputs.
4. Audit `wiki/tcm-modern-rigor-intersection.md` for reader-facing ownership: update stale candidate mechanism attributions, avoid self-experiment framing, and mark Si Miao San quantitative clinical claims as requiring primary-source adjudication unless already verified.
5. Before any synthesis using TCM/supplement ABCG2 priorities, rebuild triage from primary evidence preserving compound/source/target/polarity, assay type, measured/justified free exposure, and mechanism-matched function.

## Review limits
No experiment code was executed in daemon mode. Primary sources were not independently retrieved; source support is limited to artifact citations and shard-inspected provenance, with several comp-004 inputs marked “primary abstract.” Fixed-string repository search could not run because the tool backend lacked `rg`; affected-surface review relies on supplied hash-bound shard coverage plus targeted file reopening. Binary artifacts were not present as deterministic blocks.
