---
type: experiment
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 2
global_index: 10
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# CFH Y402H × dietary flavonoid/polyphenol intake × gout incidence biobank-mining study.

2. **CFH Y402H × dietary flavonoid/polyphenol intake × gout incidence biobank-mining study.** Cost: $0 (subagent + existing biobank data). Time: ~1 hour (subagent query design + interpretation). Decides: whether the genotype-stratified dietary CP0 hypothesis (Connection 3 above) has empirical support in existing cohort data before any prospective trial is designed. Protocol: query UK Biobank (or equivalent CFH-genotyped cohort with dietary recall + gout ICD codes) for CFH rs1061170 × dietary flavonoid intake × incident gout. The prediction: CFH Y402H carriers with low dietary polyphenol intake have higher gout incidence than carriers with high intake; wild-type carriers show no dietary-polyphenol-dependent risk gradient. This is a free test of a stratification logic that would otherwise require a prospective trial to validate.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The biobank-mining experiment is worth doing, but its provenance should be corrected. The CFH Y402H hypothesis is anchored in `complement-c5a-gout.md` §6.3, which explicitly names Factor H variants as a database-only gout-severity opportunity; it is not anchored in `gout-genetic-variants.md`, which currently has no CFH/Y402H entry in the inlined file and no grep match. Revise the protocol to first add CFH Y402H to the variant index, then mine CFH genotype × dietary-polyphenol intake × gout outcomes.
