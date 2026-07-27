COMP_VERDICT: quantitative_verdict_invalid
REVIEWED_SNAPSHOT: 62d17bef9d42994394848f2271d5fedfe2c5e6667c56292782023c9a4937b20a
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: no
PROPAGATION_ALLOWED_SCOPE: corrective propagation only: prior nominal gut-concentration/IC50 ratios, percent inhibition, VERY_HIGH risk tiers, and clinical/patient inferences are invalid; direct intestinal ABCG2-attributed urate-flux testing is the surviving route
SYNTHESIS_ALLOWED_SCOPE: bounded synthesis of evidence-gap routing for quercetin, curcumin, and EGCG from the three cited records; no ranking, dose, genotype, formulation, or clinical direction
FORBIDDEN_INFERENCES: dose or formulation guidance; percent intestinal urate-transport inhibition; clinical-risk tiers; genotype-specific susceptibility; dietary/extract direction; extrapolation from drug-substrate BCRP assays to urate flux; treating this bounded correction set as a literature census

# Independent comp review — comp-004

## Reviewed snapshot
Independent daemon reviewer; push manifest SHA-256 `62d17bef9d42994394848f2271d5fedfe2c5e6667c56292782023c9a4937b20a`, source commit `65e78cbd3d101e6883a73209bbf1f48cf9ac8f4c`. Authoring gates are modern and valid. Shard auditors reported complete inspection of the comp artifact, generated outputs, `wiki/computational-experiments.md`, `wiki/validation-experiments.md`, and the interpretive page; I reopened the load-bearing comp files and affected mechanism pages for targeted cross-checks. No deterministic binary block was reported.

## Bottom-line verdict
Quantitative verdict invalid. The revised comp correctly kills the prior nominal bulk gut concentration ÷ drug-substrate IC50 model and preserves only a qualitative evidence-routing result: the three cited ABCG2/BCRP interaction records do not establish intestinal ABCG2-attributed urate flux, so quercetin, curcumin, and EGCG require direct intestinal urate-flux testing.

## Implementation and constraint closure
The code implements a bounded structural audit, not a pharmacokinetic or transporter model. It validates schema version, exact compound set, controlled vocabularies, nonempty metadata, reported substrates, Boolean intestinal-model flags, and source-metadata presence. It does not validate PMID/DOI syntax or primary-source contents, and it does not calculate dose, solubility, free exposure, IC50 occupancy, percent inhibition, clinical risk, genotype effects, chronicity, or formulation effects.

The route from inputs to outputs closes: all three input records have `urate_evidence_status: not_established_by_cited_record`, so all three are classified as `DIRECT_INTESTINAL_URATE_FLUX_ASSAY_REQUIRED` with `quantitative_risk_rank_allowed: false`. The contrary condition is implemented: if a record reports direct intestinal urate flux, the code routes to `DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED` rather than silently keeping the default result.

Constraint closure is appropriate for a negative qualitative audit. The relevant substrates are drug probes, not urate: quercetin records use mitoxantrone and BODIPY-FL-prazosin in non-intestinal BCRP systems; curcumin uses sulfasalazine and rosuvastatin in a cynomolgus-monkey intestinal BCRP interaction study; EGCG uses mitoxantrone in MCF-7Tam cells. No Km/Ki/IC50, ATP-dependent transport rate, free enterocyte-surface concentration, metabolite exposure, residence time, barrier integrity, viability, transporter attribution, intestinal segment, or coproduct/safety burden is measured. The artifact correctly treats those as wet-lab variables, not tunable model parameters.

## Summary-fidelity audit
The generated `outputs/assay_evidence_audit.json`, generated `outputs/summary.md`, experiment README, interpretive page, computational-experiments index entry, and validation §1.14 are materially aligned. They invalidate the old ratios, percent-inhibition estimates, and VERY_HIGH labels; they do not reintroduce ranking or clinical-risk claims; and they route to measured free parent/metabolites, ABCG2 protein/surface abundance, ABCG2 attribution, barrier/viability controls, and basolateral-to-apical urate flux.

Targeted cross-checks of `abcg2-modulators.md`, `egcg.md`, `supplements-stack.md`, `theaflavins.md`, TCM pages, mushroom mapping, and index surfaces found the main comp-004 corrections propagated: EGCG/Yu is no longer described as a favorable ABCG2/Nrf2 sign switch; Farabegoli is bounded to cancer-cell mitoxantrone-assayed BCRP activity; supplement pages present ABCG2 effects as assay-design warnings rather than contraindication or patient timing rules; comp-013 reuse of the occupancy shortcut is invalidated.

## Reader-facing ownership audit
The focused mechanism page `abcg2-modulators.md` owns the transporter evidence, sourcing boundaries, conjecture, and falsification gate. The EGCG page owns EGCG-specific evidence, exposure, safety, and the direct ABCG2 open question. Cross-compound comparison remains in catalog/index surfaces without promoting a portfolio rank or clinical instruction. The inspected pages avoid narrative “old artifact” clutter except where needed to mark invalidated COMP scope, and they do not present supplement use, discontinuation, genotype personalization, or dosing advice.

## Conjecture preservation audit
The unsupported factual assertion that Yu 2024 showed an ABCG2/Nrf2 favorable sign switch has been corrected. The useful adjacent idea survives in bounded form: EGCG’s net intestinal ABCG2 effect may depend on free exposure, metabolites, time, and intestinal context, but this is explicitly a Research Conjecture with a discriminating polarized intestinal urate-flux assay. The negative COMP result kills only the exact quantitative shortcut and the claim that the three cited records establish intestinal urate-transport inhibition. It does not kill quercetin, curcumin, or EGCG as broader gout/inflammation leads, nor does it prove safety or benefit.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/outputs/assay_evidence_audit.json` | generated output | Yes | Faithful to inputs/code; all three records route to direct intestinal urate-flux assay; quantitative ranking forbidden. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/outputs/summary.md` | generated output | Yes | Matches JSON and README; no unsupported numerical or clinical inference. |
| `wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/README.md` | experiment summary/update | Yes | Correct verdict boundary and downstream claim map; broader than executable but framed as follow-up surfaces. |
| `wiki/supplement-abcg2-antagonism-computational.md` | interpretive wiki update | Yes | Consistent with artifact; compound-specific boundaries and direct-assay route preserved. |
| `wiki/computational-experiments.md` | index update | Yes via shard; targeted context reopened | Comp-004 entry is corrective and bounded; no rank or risk tier propagated. |
| `wiki/validation-experiments.md` | validation update | Yes via shards | §1.14 records comp-004 invalidation and required direct urate-flux controls. Future hard statistical thresholds should remain pilot-qualified before verdict use. |
| `wiki/abcg2-modulators.md` | affected mechanism page | Targeted relevant sections inspected | Owns evidence boundaries and Research Conjecture; consistent. |
| `wiki/egcg.md` | affected focused page | Targeted relevant sections inspected | Yu/Farabegoli boundary corrected; no favorable ABCG2 claim. |
| `wiki/supplements-stack.md` | affected catalog page | Targeted relevant sections inspected | Presents ABCG2 interactions as experimental variables, not personalized rules. |
| `wiki/theaflavins.md` | affected related compound page | Targeted relevant sections inspected | Does not use EGCG as a class-pattern proof; notes no EGCG/theaflavin class inference. |
| `wiki/tcm-modern-rigor-intersection.md`, `wiki/hypotheses/H04-tcm-rigor-intersection.md`, `wiki/tcm-gout-compound-triage-computational.md`, `wiki/medicinal-mushroom-compound-mapping-computational.md`, `wiki/open-questions.md`, `index.md`, `wiki/nlrp3-inhibitor-screen.md` | affected synthesis/index pages | Targeted relevant sections inspected | Correctly reject occupancy shortcut reuse or preserve only measured-exposure/function gates where relevant. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Exact compound set is Curcumin, EGCG, Quercetin | `analyze.py`, `inputs/assay_evidence.json` | Enforced by `EXPECTED_COMPOUNDS` equality | Internal artifact | Closed. |
| Quercetin cited record used drug substrates in non-intestinal systems | input/provenance/output | Classification reason; no numerical use | Citation string + “primary abstract”; source content not independently reverified here | Sufficient for bounded audit; not a full source verification. |
| Curcumin cited record is intestinal BCRP interaction with sulfasalazine/rosuvastatin, not urate | input/provenance/output | Routes to direct urate-flux assay despite intestinal model flag | PMID/DOI present; abstract-level verification claimed | Sufficient for bounded audit. |
| EGCG Farabegoli record reduced mitoxantrone-assayed BCRP activity in MCF-7Tam without mRNA/protein change | input/provenance/output; `egcg.md` | Routes to direct urate-flux assay; no kinetic parameter used | PMID/DOI present; abstract-level verification claimed | Sufficient for bounded audit. |
| Yu 2024 does not report ABCG2 or Nrf2-mediated ABCG2 sign switch in primary abstract | provenance; `abcg2-modulators.md`; `egcg.md` | Not used in code; supports wiki correction | Abstract-level provenance only | Correctly bounded; do not treat as full-paper exclusion. |
| Quantitative risk/rank not allowed | code/output/summary/wiki | Set false for every record; invalidated-scope list | Internal computational rule | Closed. |
| Direct intestinal ABCG2-attributed urate flux is required resolver | README/output/wiki/validation §1.14 | Output disposition and downstream experiment routing | Mechanistic reasoning from substrate/system mismatch | Valid qualitative routing; no biological effect inferred. |

## Affected wiki pages
- `wiki/supplement-abcg2-antagonism-computational.md` — already consistent — bounded comp result and direct assay route.
- `wiki/computational-experiments.md` — already consistent — comp-004 listed as invalidating quantitative occupancy/risk verdict.
- `wiki/validation-experiments.md` — already consistent for comp-004 — §1.14 captures assay mismatch and direct flux requirements; pilot variance should qualify future hard thresholds.
- `wiki/abcg2-modulators.md` — already consistent — owns transporter evidence and EGCG context conjecture.
- `wiki/egcg.md` — already consistent — corrected Yu/Farabegoli boundary and open ABCG2 question.
- `wiki/supplements-stack.md` — already consistent — no patient-facing ABCG2 contraindication; direct flux required.
- `wiki/theaflavins.md` — already consistent — no EGCG/theaflavin class-pattern inference.
- `wiki/tcm-modern-rigor-intersection.md` — already consistent — poor absorption/occupancy shortcuts rejected in favor of measured exposure/function.
- `wiki/hypotheses/H04-tcm-rigor-intersection.md` — already consistent — cites comp-004 as a method caution, not validation.
- `wiki/tcm-gout-compound-triage-computational.md` — already consistent — comp-013 occupancy-derived rank/viability labels invalidated.
- `wiki/medicinal-mushroom-compound-mapping-computational.md` — already consistent — ABCG2 drug-substrate/expression records not treated as urate flux.
- `index.md` — already consistent — comp-004 public summary is corrective, not a risk ranking.

## New connections or implications
Comp-004 strengthens a general corpus rule: transporter evidence must preserve substrate identity and compartment. This applies beyond supplements to TCM/fungal lead inventories, theaflavin transporter-expression claims, and any UOX substrate-supply enhancer. A drug-probe BCRP interaction can nominate a control arm, but only ABCG2-attributed urate flux under measured epithelial exposure can support a urate-transport conclusion.

Research Conjecture boundary: EGCG’s cancer-cell BCRP inhibition and Yu’s mouse serum-urate phenotype may reflect context-dependent exposure/metabolism/tissue differences, but the direct link is unsupported until the polarized intestinal urate-flux experiment is run.

## Required actions
1. None for comp-004 propagation or synthesis. Use only the bounded corrective result and forbidden-inference list above.

## Review limits
Code was inspected but not executed in daemon mode. Primary papers were not independently rehydrated beyond artifact-provided citation/abstract-level provenance. Repository full-text search tooling failed because `rg` was unavailable, so affected-surface checks relied on shard coverage plus targeted file reopening rather than a fresh exhaustive grep. Future use of validation §1.14 as a verdict-bearing wet-lab protocol should freeze statistical thresholds from pilot variance rather than treating current planning numbers as biologically validated.
