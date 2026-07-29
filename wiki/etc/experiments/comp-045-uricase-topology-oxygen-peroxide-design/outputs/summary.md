# comp-045 summary — uricase topology × oxygen × peroxide

**Design disposition: CANDIDATE_LAYOUT_GENERATED. Biological verdict: NOT_EVALUATED.**

This computation validates an evidence vocabulary and generates a randomized candidate plate layout. It contains no biological measurements and therefore does not advance, eliminate, or rank a topology.

**Wet-lab readiness: BLOCKED_PENDING_EXACT_CONTROL_SAMPLING_AND_ANALYSIS_QUALIFICATION.** The layout is a blocked template until the listed control, stock, oxygen, sampling, and analysis qualifications are fixed and reviewed.

**Statistical decision status: BLOCKED_PENDING_PREREGISTERED_WET_LAB_ANALYSIS_PLAN.** The three biological-run slots are a provisional plate-layout assumption, not a power or precision claim.

## Evidence boundary

- 6 configurations reproduce exact published baseline or joint KatG+VHb construct signatures.
- KatG-only and VHb-only rows are proposed isolation tests from joint-module precedent; neither component was isolated in the cited PULSE or Zhao comparisons.
- The PULSE LamB and InaK-N joint constructs are direct whole-configuration precedents, but they do not establish extracellular reaction-site peroxide closure.
- The koji-secreted UOX rows are proposed configurations without a cited direct UOX precedent.
- The InaK-N fusion has whole-cell activity precedent; dedicated surface-accessibility localization was not reported.

## Candidate layout

- 18 candidate configuration classes and 20 block assignments in 2 balanced blocks
- 16 preregistered contrasts, each with its comparator on the same plate block
- 3 provisional biological-run slots × 2 oxygen contexts × 2 blocks = 12 plates
- 96 used and 0 empty wells per 96-well plate
- Every active-UOX configuration has a planned support-module-matched inactive-UOX control at every urate concentration, including zero; the exact inactive mutation and equivalence criteria remain a wet-lab blocker.
- All samples are allocated across the full plate by a stable SHA-256 key.

## Urate roles

- 0 µM — `matched_no_urate_control`
- 0.59 µM — `direct_human_terminal_ileum_prior_not_tested_in_published_uox_configurations`
- 50 µM — `sensitivity_scenario_not_evidence`
- 250 µM — `lowest_published_pulse_topology_assay_concentration`

## Wet-lab gates

- Predeclare and measure the actual dissolved-oxygen target for each oxygen context; PULSE sealed-tube and Zhao ~15%-normal-DO conditions are not interchangeable.
- Bind exact active/inactive constructs; UOX, KatG, VHb, and reaction-site-catalase expression, activity, localization or oxygen-function qualifications as applicable; strain stocks; cell normalization; sampling times; and assay compatibility before wet-lab execution.
- Preregister the estimand, effect metric, biological threshold, variance and effect-size assumptions, power or precision target and justified run count, model and multiplicity control, exclusion and failure handling, and sensitivity rules before wet-lab execution.
- Interpret 250 µM as a published PULSE assay concentration, 0.59 µM as a terminal-ileal human-fluid prior not tested in the published UOX configurations, and 50 µM as sensitivity only.
- The mixed PULSE-KV composition is a proposed cross-plate anchor, not a published in-vitro positive control.

### Blocking qualifications

- exact active and inactive UOX construct identities and matched expression, retained-activity, and localization qualification criteria
- exact UOX topology construction and compartment-specific localization and accessibility qualification
- exact KatG construct, expression, and retained-activity qualification
- exact VHb construct, expression, and oxygen-function qualification
- exact reaction-site-catalase construction, expression, retained activity, localization, and co-secretion or co-display compatibility
- exact chassis and PULSE-mixture stock identities and cell normalization
- exact dissolved-oxygen targets, measurement method, and oxygen-context qualification
- sampling times, well volume, aliquoting, and destructive-assay compatibility
- assay sensitivity and quantification limits at the 0.59 uM terminal-ileum prior
- estimand, effect metric, and biological decision threshold
- variance and effect-size assumptions, power or precision target, and justified biological-run count
- analysis model and multiplicity control
- exclusion, missing-data, and assay-failure rules
- sensitivity-analysis rules

## Required readouts

- urate
- allantoin_or_pathway_product
- hydrogen_peroxide
- dissolved_oxygen
- viability
- uox_expression
- uox_activity
- uox_localization
- katg_expression
- katg_activity
- vhb_expression
- vhb_oxygen_function
- reaction_site_catalase_activity
- reaction_site_catalase_localization

## Limitations

- The artifact contains no biological outcomes and cannot select or eliminate a topology.
- Published evidence applies to exact whole configurations and source regimes, not isolated KatG or VHb effects.
- A construct signature precedent does not establish activity at 0.59 or 50 uM or at a newly chosen dissolved-oxygen target.
- Proposed secreted and surface catalase modules require expression, localization, activity, and safety qualification.
- The candidate layout does not model expression burden, proteolysis, mucus residence, colonization, oxygen kinetics, or epithelial injury.
- Only the preregistered same-block contrasts are supported by the layout; other cross-block comparisons remain confounded with plate block.
- The inactive-UOX identities, sampling times, and assay multiplexing plan are intentionally unresolved and block wet-lab execution.
- The three biological-run slots are a provisional plate-layout assumption; no estimand, effect metric, decision threshold, variance or effect-size assumption, power or precision target, model, multiplicity control, exclusion rule, missing-data rule, assay-failure rule, or sensitivity rule has been preregistered.
