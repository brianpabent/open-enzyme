# comp-045 — Uricase topology × oxygen × peroxide decision design

**Status:** Pre-run design. Result-bearing execution is prohibited until the exact pre-run manifest receives `PRE_RUN_GATE: GO`.

## Question and decision

How can exact published and proposed UOX configurations be compared across substrate concentration, dissolved-oxygen context, KatG, VHb, and reaction-site catalase without attributing the published joint KatG+VHb effect to either component or encoding a topology winner?

This computation can decide only whether the declared evidence vocabulary and candidate plate layout are internally valid. It does not ingest biological outcomes and therefore cannot advance, eliminate, or rank a topology.

## Model

The input enumerates 18 physical configurations rather than crossing ambiguous global factors:

- four PULSE intracellular UOX+YgfU configurations: no support, VHb only, KatG only, and joint KatG+VHb;
- six LamB-secreted configurations: the same four support states plus proposed co-secreted catalase with and without VHb;
- six InaK-N-display configurations: the same four support states plus proposed surface-matched catalase with and without VHb;
- two proposed *A. oryzae* secreted-UOX configurations: native intracellular catalase background only and proposed co-secreted catalase.

The three exact PULSE topologies have published baseline and joint KatG+VHb construct precedents. The Gao/PULSE records are stored separately from the related Li and Zhao intracellular configurations; related sources do not make a PULSE construct exact. KatG-only and VHb-only configurations are isolation tests from the joint precedent. The cited sources do not establish either isolated component effect. The *A. oryzae* configurations have no cited direct UOX precedent.

Evidence is separated into four axes:

1. exact whole-configuration precedent;
2. component attribution;
3. peroxide reaction-site alignment;
4. oxygen sufficiency/support.

An exact construct precedent does not imply that a new urate concentration or dissolved-oxygen target matches the source regime.

## Candidate layout

The 18 unique configurations are preregistered as 20 assignments in two equal blocks. `lamb_no_support` and `lamb_vhb_only` repeat as within-block comparators for the reaction-site-catalase contrasts. Each plate contains:

- ten configuration assignments;
- active UOX and an otherwise matched inactive-UOX control for every configuration;
- 0, 0.59, 50, and 250 µM urate for every active/control pair;
- unengineered EcN, unengineered *A. oryzae*, medium blank, and a proposed PULSE-KV mixed-cell cross-plate anchor at all four concentrations.

This uses all 96 wells. Samples are allocated over the full plate with a stable SHA-256 key derived from the declared layout seed, run, oxygen context, block, and sample identity. Three biological runs × two oxygen contexts × two blocks require 12 plates. Every declared KatG, VHb, joint-module, and reaction-site-catalase contrast has its comparator in the same block.

The PULSE-KV mixture is a proposed cross-plate anchor based on a published mixture composition. It is not labeled a published in-vitro positive control.

## Concentration and oxygen contract

- **0 µM:** matched no-urate control.
- **0.59 µM:** rounded terminal-ileal human-fluid prior from a clinical balloon-enteroscopy cohort; not tested in the cited UOX configurations and not a healthy-population baseline.
- **50 µM:** sensitivity scenario only.
- **250 µM:** lowest reported PULSE topology-assay concentration.

The wet-lab protocol must predeclare and measure the actual dissolved-oxygen target for both `microoxic_screen` and `oxic_screen`. PULSE used filled, sealed tubes without a reported DO target; Zhao used approximately 15% of normal DO. Those conditions are not interchangeable and neither proves oxygen sufficiency for this design.

## Controls and readouts

Every construct-level comparison requires an exact active/inactive UOX pair. Shared chassis, medium, and mixed-cell anchors cannot substitute for those matched controls. The exact inactive-UOX mutation and criteria for matched expression and localization have not yet been chosen; that blocks wet-lab execution rather than being silently represented as solved.

Required readouts:

- urate;
- allantoin or another pathway product;
- hydrogen peroxide;
- dissolved oxygen;
- viability;
- UOX localization.

Expression/activity and localization must be qualified before using the complete plate set. Exact strain stocks, cell normalization, dissolved-oxygen targets, sampling times, well volumes, aliquoting, and compatibility of destructive readouts must also be fixed. Proposed compartment-matched catalase configurations additionally require retained catalase activity and localization at the claimed reaction compartment.

## Decision and failure rules

Successful execution may emit only:

- `CANDIDATE_LAYOUT_GENERATED` for the design disposition; and
- `NOT_EVALUATED` for the biological verdict.

It must also emit `BLOCKED_PENDING_EXACT_CONTROL_AND_SAMPLING_QUALIFICATION` for wet-lab readiness. The program must stop without outputs if IDs or states are duplicated, an enum is unknown, a module is incompatible with its topology, block repetition is undeclared, a planned contrast lacks a same-block comparator, an exact or related precedent is mislabeled, a matched zero-urate control is absent, a load-bearing control/readout/category contract is unknown, or a plate exceeds 96 wells.

No outcome of this computation can establish:

- activity at 0.59 or 50 µM;
- oxygen sufficiency;
- isolated KatG or VHb effects;
- extracellular peroxide closure;
- surface accessibility of InaK-N-smUOX;
- secreted UOX activity in *A. oryzae*;
- epithelial safety, efficacy, dose, or a topology/chassis winner.

## Sensitivity plan

There is no numerical efficacy sensitivity analysis because no biological response model is used. The two oxygen contexts and the 0.59/50/250 µM nonzero concentrations are wet-lab design regimes. They must remain separately labeled; grid occupancy is not evidence or probability.

## Planned outputs

- `outputs/results.json` — validated configuration table, one unique configuration × oxygen evidence row, and 12 complete plate maps;
- `outputs/summary.md` — compact design disposition, evidence boundary, layout, wet-lab gates, and limitations.

Output schema 2 replaces the historical duplicated evidence rows and hardcoded biological verdict. It records exact and related precedents separately, enumerates same-block contrasts, and preserves `NOT_EVALUATED`.

The canonical interpretation home is `wiki/uricase-topology-oxygen-peroxide-design-computational.md`. Planned direct dependents are:

- `index.md`;
- `wiki/computational-experiments.md`;
- `wiki/delivery-route-matrix.md`;
- `wiki/gout-kill-chain-delivery-routes.md`;
- `wiki/gout-multihop-research-program.md`;
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md`;
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md`;
- `wiki/validation-experiments.md`;
- `papers/cross-vendor-heterogeneity-guard/draft.md`;
- `synthesis/queue/comp-review-045.md` — delete only after the corrective actions, regenerated outputs, propagation, and Gate 2 review close.

The 0.59 µM terminal-ileum label also affects COMP-044's historical design inputs. That separate runnable artifact requires its own exact lifecycle before its input keys can be changed.

Current-reference audit with no planned decision delta:

- `wiki/aspergillus-oryzae.md` already treats intracellular catalase protection as a hypothesis and keeps the reaction-site measurement gate open.
- `wiki/etc/GRAPH.md` is a link-only discovery edge.
- `wiki/gout-deep-dive.md` contains no current COMP-045 reference.
- `mkdocs.yml` is navigation-only and already reaches COMP-045 through the existing indexes; no direct entry changes.
- `operations/notable-moments.md` says COMP-045 motivates a comparison and explicitly places exact-configuration supply before §1.33.
- `papers/cross-vendor-heterogeneity-guard/revisions.md` records only that COMP-045 framed a coupled empirical comparison.
- The COMP-019 tombstone and invalidation record contain successor links only.
- The COMP-044 README already says COMP-045 supplies a candidate layout, not materials or a winner. COMP-019/044 review receipts are immutable historical review records.
- `logs/sweep-state.json` is automation-owned and will not be hand-edited.

## Assumptions and invalidation boundary

- The code treats Gao/PULSE exact construct signatures as provenance metadata, not as efficacy grades. Li and Zhao are retained only as related intracellular precedents.
- Blocking is a nuisance-control device; it does not make cross-block comparisons equivalent to within-block contrasts.
- Native *A. oryzae* intracellular catalase is background context, not a separate engineered arm and not evidence of secreted-UOX peroxide closure.
- The published C6 periplasmic EcN UOX architecture is outside this four-topology design and supports no current row.
- The generated layout is a blocked template, not a wet-lab-ready protocol, until the exact control and sampling identities listed above are fixed and reviewed.

A later biological result can kill only the tested construct × concentration × oxygen × control regime. Failure of one topology or chassis does not kill gut-lumen UOX or the Open Enzyme mission.

## Reproduce after Gate 1

Python standard library only.

```bash
cd wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design
python3 ../../../../scripts/comp-review-manifest.py check \
  --manifest reviews/pre-run.manifest.json \
  --review reviews/pre-run.md \
  --required-line 'PRE_RUN_GATE: GO'
python3 analyze.py
sha256sum outputs/results.json outputs/summary.md
python3 analyze.py
sha256sum outputs/results.json outputs/summary.md
```

Both output hashes must be identical across the two runs.

## Files

- `analyze.py` — validation, evidence-state evaluation, and candidate plate-map generator
- `inputs/design_factors.json` — exact configurations, precedents, states, controls, and regimes
- `inputs/provenance.md` — primary-source scope and inference boundary
- `inputs/query-strategy.json` — literature-query framing
- `outputs/` — generated only after Gate 1
