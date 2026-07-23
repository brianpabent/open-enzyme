# comp-044 — Gut-lumen uricase physiological regime

**Status:** Deterministic design; generated output controls the verdict

## Question

Does comp-019's conclusion that 5–50 mg/day oral uricase is always substrate-limited survive when its own luminal-urate concentration and Km are actually used, together with finite residence time, oxygen availability, substrate access, and enzyme survival?

## Method

The script converts uricase dose and label specific activity to a bounded urate-degradation capacity, then explicitly multiplies by Michaelis–Menten substrate occupancy, active-window duration, and nonmechanistic pH/activity, effective oxygen-dependent activity, substrate-access, and active-enzyme-survival scenario multipliers. It evaluates five named scenarios and a discrete full-factorial grid of 1,620 cells per dose (4,860 across all three doses). Grid occupancy is not a probability distribution. It deliberately does not map capacity to serum urate.

## Reproduce

```bash
cd wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime
python3 analyze.py
```

Python standard library only. Outputs are deterministic.

## Output authority

This design does not embed a result. The current verdict must be read from a freshly generated `outputs/results.json` and `outputs/summary.md` produced from an exact pre-run-reviewed snapshot. The three possible verdicts and their distinct propagation permissions are defined below; no prior output authorizes a branch.

## Files

- `analyze.py` — deterministic bounded sensitivity analysis
- `inputs/model_parameters.json` — evidence priors and clearly labeled scenario values
- `inputs/provenance.md` — claim-level provenance and exclusions
- `inputs/query-strategy.json` — literature-query framing artifact
- `outputs/results.json` — machine-readable results
- `outputs/summary.md` — human-readable result

## Key limitation

The analysis still holds concentration fixed within each active window and compares it with a whole-day flux denominator. The 8.3 U/mg activity, Km range, 2–4-hour window, and 233 mg/day denominator remain inherited or derived priors rather than newly verified quantitative-planning inputs. The 0.25 and 4 regime bins are descriptive; only ratio 1 has direct mass-balance meaning. A later dynamic model requires measured local urate replenishment, topology-specific oxygen and enzyme survival, reabsorption, and spatial residence. Therefore comp-044 is a regime-audit prior, not a clinical efficacy model or a basis for dose selection.

## Conditional authoring contract

The actual generated verdict controls what may be written:

- **`LEGACY FLAT-DOSE REGIME NOT ROBUST`:** apply the corrective propagation inventory below. State only that comp-019's unconditional classification is not robust; do not claim a physiological-regime reversal.
- **`LEGACY ROBUSTNESS NOT REJECTED`:** do not publish the pre-authored wide corrective branch or use comp-044 to retract the legacy classification. Update the canonical evidence home and run the contrary-result correction cascade below before publishing. Keep the COMP-044 queue action open.
- **`LEGACY CONTROL NOT REPRODUCED`:** do not publish the pre-authored wide corrective branch or use comp-044 to adjudicate robustness. Update the canonical evidence home and run the contrary-result correction cascade below before publishing. Keep the COMP-044 queue action open.

For either contrary branch, build a fresh repository-wide inventory of every active comp-044 reference and every paraphrase of its result. Correct each result-dependent consumer; a direct link or a claim sourced elsewhere may remain only after inspection shows that it is branch-invariant. The current minimum inventory includes `index.md`; the canonical comp-044 page; `wiki/computational-experiments.md`; `wiki/gout-kill-chain-delivery-routes.md`; `wiki/gout-action-guide.md`; `wiki/gout-pathophysiology.md`; `wiki/gout-clinical-pipeline.md`; `wiki/supplements-stack.md`; `wiki/modality-chokepoint-matrix.md`; `wiki/enzyme-deficit-deep-dive.md`; `wiki/crispr-uricase.md`; `wiki/open-questions.md`; `wiki/validation-experiments.md`; `wiki/uricase-abcg2-genotype-stratification-computational.md`; `wiki/blood-barrier.md`; `wiki/blood-barrier-exploits.md`; `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md`; `wiki/dual-chassis-ecn-pdb-uricase-computational.md`; `wiki/gi-survival-prediction.md`; `wiki/etc/GRAPH.md`; `wiki/uricase.md`; `wiki/purine-degrading-bacteria.md`; `wiki/protein-engineering-strategy.md`; `wiki/etc/autonomous-screening-methodology.md`; `wiki/genotype-informed-supplement-workflow.md`; `wiki/codon-optimization-expression-cassette.md`; `wiki/engineered-koji-protocol.md`; `wiki/gout-multihop-research-program.md`; `wiki/gout-genetic-variants.md`; `wiki/nlrp3-exploit-map.md`; `wiki/uricase-variant-selection.md`; `wiki/gut-lumen-sink.md`; `wiki/abcg2-modulators.md`; `wiki/engineered-yeast-uricase-proposal.md`; `wiki/chassis-pending-interventions.md`; and the comp-019/comp-031 records that name comp-044 as their rationale. Preserve any separate comp-019 or comp-031 status only where its rationale is independently supported; do not leave comp-044 named as evidence for a result the fresh run did not produce.

For the `LEGACY FLAT-DOSE REGIME NOT ROBUST` branch, the canonical evidence home is [`wiki/gut-lumen-uricase-physiologic-regime-computational.md`](../../../gut-lumen-uricase-physiologic-regime-computational.md). Corrective propagation is local to oral luminal-UOX feasibility and permits changes only to:

- [`wiki/gut-lumen-sink.md`](../../../gut-lumen-sink.md) — remove or qualify low-local-UOX sufficiency, 20–50 mg/day feasibility, “dosing is achievable,” and initial-proof-of-concept readiness claims.
- [`wiki/uricase.md`](../../../uricase.md) — remove the 20–50 mg/day culture-volume arithmetic and fixed survival/mutation-validation claims; state that neither dose sufficiency nor current production sufficiency is established.
- [`wiki/engineered-yeast-uricase-proposal.md`](../../../engineered-yeast-uricase-proposal.md) — remove the inherited oral-dose requirement, predicted GI-stability gains, fixed expression yield, intracellular-topology recommendation, mouse-first tier progression, and downstream biomass/chassis-serving comparisons.
- [`wiki/blood-barrier-exploits.md`](../../../blood-barrier-exploits.md) — replace the claim that gut-lumen delivery “may be sufficient” with the current physiological feasibility gate.
- [`wiki/codon-optimization-expression-cassette.md`](../../../codon-optimization-expression-cassette.md) — remove claims that intracellular release or the predicted per-CFU activity is sufficient for efficacy; return topology and delivered activity to validation §1.33.
- [`wiki/engineered-koji-protocol.md`](../../../engineered-koji-protocol.md) — delete the unvalidated dose/serving calculation and personalized titration instructions; replace PULSE-derived sufficiency, ALLN “science works,” and koji-superiority claims with bounded animal/human evidence and the unresolved physiological gate.
- [`wiki/aspergillus-oryzae.md`](../../../aspergillus-oryzae.md) — remove the conversion from rough expression yield to sufficient therapeutic dosing; require measured delivered activity before dose or format conclusions.
- [`wiki/koji-construct-design.md`](../../../koji-construct-design.md) — remove the unvalidated therapeutic-dose and ALLN-346-based achievability conversion while retaining expression yield as an assay target rather than efficacy evidence.
- [`wiki/protein-engineering-strategy.md`](../../../protein-engineering-strategy.md) — remove the predicted administrable oral product dose and return GI-survival improvements to an activity-preservation hypothesis pending physiological validation.
- [`wiki/gi-survival-prediction.md`](../../../gi-survival-prediction.md) — remove the unsupported 500–800 mg dosing model, serum-urate predictions, patient-stratified recommendations, and biomass conversions; retain the survival question as an empirical gate.
- [`wiki/koji-endgame-strain.md`](../../../koji-endgame-strain.md) — remove the 40–80 mg/g, 150–400 mg-per-meal, and ALLN-dose-matching planning values from the active configuration.
- [`wiki/saccharomyces-cerevisiae.md`](../../../saccharomyces-cerevisiae.md) — replace links and summaries that present urate-budget and yeast-to-dose arithmetic as current dosing mathematics with the measured-delivered-activity gate.
- [`wiki/computational-experiments.md`](../../../computational-experiments.md) — report the actual generated verdict, label the specific-activity/Km/window/flux inputs as inherited and non-planning-grade, and retain the no-serum/no-dose boundary.
- [`wiki/delivery-route-matrix.md`](../../../delivery-route-matrix.md) — remove the unsupported dollars-versus-cents per-dose comparison and chassis-economics ranking; retain route-specific engineering gates without inferring oral production sufficiency.
- [`index.md`](../../../../index.md) — replace predicted yeast/koji UOX yields, fixed survival fractions, validated-mutation language, and host-choice framing with the delivered-activity measurement gate.
- [`wiki/uricase-variant-selection.md`](../../../uricase-variant-selection.md) — remove the daily enzyme-mass, activity-unit, CFU-dose, and formulation-volume arithmetic; route variant selection through §1.33 before dose or production conclusions.
- [`wiki/open-questions.md`](../../../open-questions.md) — remove the fixed whole-cell survival advantage and human self-experiment path; keep topology and genotype response as controlled experimental questions.
- [`wiki/validation-experiments.md`](../../../validation-experiments.md) — remove the “koji-realistic dose,” fixed GI-survival threshold, validated-OPT-1 claim, and host-choice interpretation; make §1.16 a matched retained-active-UOX screen feeding §1.33.
- [`wiki/chassis-pending-interventions.md`](../../../chassis-pending-interventions.md) — remove the stale “chassis solves peroxide” reference and keep intra-articular architectures behind measured reaction-site peroxide and tissue-safety gates.
- [`wiki/gout-pathophysiology.md`](../../../gout-pathophysiology.md) — do not present an engineered-koji UOX construct, its serum effect, or its evidence tier as though it has been tested.
- [`wiki/supplements-stack.md`](../../../supplements-stack.md) — remove provisional biomass doses, expected serum effects, home-fermentation formats, personal-use timing, and UOX pairing recommendations.
- [`wiki/gout-kill-chain-delivery-routes.md`](../../../gout-kill-chain-delivery-routes.md) — keep ABCG2-plus-UOX and anti-inflammatory-plus-UOX combinations as untested coupled-flux hypotheses; do not predict additivity or a serum effect.
- [`wiki/modality-chokepoint-matrix.md`](../../../modality-chokepoint-matrix.md) — do not transfer parental GRAS or food-use status to engineered constructs, treat planned payloads as realized, or select a chassis before measurement.
- [`wiki/enzyme-deficit-deep-dive.md`](../../../enzyme-deficit-deep-dive.md) — remove food-safety transfer, personal consumption, build-ease, and yeast-winner claims.
- [`wiki/crispr-uricase.md`](../../../crispr-uricase.md) — remove forecasts that engineered yeast or koji UOX is validated, in use, or an interim therapy.
- [`wiki/genotype-informed-supplement-workflow.md`](../../../genotype-informed-supplement-workflow.md) — exclude engineered-UOX home production or personal intervention paths.
- [`wiki/nlrp3-exploit-map.md`](../../../nlrp3-exploit-map.md) — do not infer that a payload-bearing engineered organism is a food from the parent organism's status.
- [`wiki/blood-barrier.md`](../../../blood-barrier.md) — treat oral tolerance versus sensitization for repeated engineered-UOX exposure as an unresolved safety question.
- [`wiki/gout-clinical-pipeline.md`](../../../gout-clinical-pipeline.md) — remove product-in-development, food-derived adjunct, regulatory-ease, dose-sparing, and chassis-ownership claims; keep the clinical scan as a dated comparator landscape.
- [`wiki/gout-deep-dive.md`](../../../gout-deep-dive.md) — separate ALLN-346 Study 201's published interim cohort from Study 202's terminated, results-unposted record; remove delivery or efficacy generalizations unsupported by either trial.
- [`wiki/etc/ai-bio-tools-playbook.md`](../../../etc/ai-bio-tools-playbook.md) — remove prompts that presuppose a consumer dose, serum effect, default chassis, food format, or personal experiment before configuration-level feasibility and safety are measured.
- [`papers/cross-vendor-heterogeneity-guard/draft.md`](../../../../papers/cross-vendor-heterogeneity-guard/draft.md) — narrow the COMP-044 interpretation to the legacy flat-dose classification and remove the personal engineered-UOX experiment.
- [`operations/notable-moments.md`](../../../../operations/notable-moments.md) — describe the result at its actual model scope rather than as a general physiological-dose adjudication.
- [`wiki/digestive-enzymes.md`](../../../digestive-enzymes.md) — remove home-koji treatment and dose extrapolations; retain delivered activity and safety as empirical gates.
- [`wiki/etc/practitioner-toolkit.md`](../../../etc/practitioner-toolkit.md) — keep the PERT record confined to its direct commercial-enzyme observation and remove transfer to engineered ingestion or production.
- [`wiki/gout-multihop-research-program.md`](../../../gout-multihop-research-program.md) — make construct supply precede the configuration-level physiological screen and prevent §1.33 from selecting an abstract topology before host implementation.
- [`wiki/hypotheses/H01-ward-dual-cassette.md`](../../../hypotheses/H01-ward-dual-cassette.md) — bind the downstream dual-cassette work to an exact §1.5-built, §1.33-advanced koji configuration rather than transferring a topology into the host after selection.
- [`wiki/hypotheses/README.md`](../../../hypotheses/README.md) — align H09 with controlled, specification-based production rather than home delivery of therapeutic doses.
- [`operations/ward-1995-lab-access.md`](../../../../operations/ward-1995-lab-access.md) — request access for exact configuration-level testing without implying that an abstract topology or parent-organism status settles host, safety, or delivery questions.
- [`operations/wet-lab-collaboration-leads.md`](../../../../operations/wet-lab-collaboration-leads.md) — describe engineered microbial UOX as one candidate track and sequence construct supply before configuration-level physiological testing.
- [`wiki/abcg2-modulators.md`](../../../abcg2-modulators.md) — keep ABCG2 modulation and luminal UOX as separately unresolved flux levers rather than presuming a combined serum effect.
- [`wiki/cordycepin-cassette-burden-computational.md`](../../../cordycepin-cassette-burden-computational.md) — keep cassette-burden computation as a prioritization proxy and remove product, dosing, or home-use extensions.
- [`wiki/dual-chassis-ecn-pdb-uricase-computational.md`](../../../dual-chassis-ecn-pdb-uricase-computational.md) — prevent parent-host status or computational scores from selecting a delivered configuration before controlled measurement.
- [`wiki/etc/autonomous-screening-methodology.md`](../../../etc/autonomous-screening-methodology.md) — require exact built configurations and controlled measurements before topology, chassis, dose, or delivery conclusions.
- [`wiki/gout-action-guide.md`](../../../gout-action-guide.md) — state the exact non-robustness boundary and keep the page as a research roadmap rather than a personal treatment guide.
- [`wiki/gout-genetic-variants.md`](../../../gout-genetic-variants.md) — keep genotype effects as controlled stratification hypotheses rather than automatic intervention rules.
- [`wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md`](../../../hypotheses/H08-gut-lumen-sink-platform-thesis.md) — preserve the sink as a falsifiable platform hypothesis whose dose, delivery, and chassis remain unresolved.

No other corpus conclusion is authorized by this run. It does not rank koji, yeast, or bacterial chassis; establish a physiological-regime reversal; predict serum urate; or establish dose/yield sufficiency. Configuration supply in validation §§1.1, 1.2, and 1.5—or acquisition and verification of an exact external configuration—precedes the configuration-level [§1.33 screen](../../../validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial). Comp-045 supplies a candidate plate layout, not materials or a winner; §1.36 then owns the pre-animal safety gate.
