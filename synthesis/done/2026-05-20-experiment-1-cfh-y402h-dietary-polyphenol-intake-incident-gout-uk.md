---
type: experiment
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 1
global_index: 8
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# CFH Y402H × dietary polyphenol intake × incident gout — UK Biobank cross‑tabulation via existing gout‑GWAS collaborator.

1. **CFH Y402H × dietary polyphenol intake × incident gout — UK Biobank cross‑tabulation via existing gout‑GWAS collaborator.**  
   Cost: $0 (collaboration request). Time: ~3 months. Decides: whether the CFH‑×‑diet interaction hypothesis survives a real‑world association test; negative result would close the question at near‑zero cost. See `gout-genetic-variants.md` §Category 5 CFH row for the full biobank‑mining feasibility analysis.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` The UK Biobank / AoU mining proposal is already scoped in `gout-genetic-variants.md` under CFH Y402H and is the cheapest real falsification move for this genotype × diet hypothesis. A negative result would retire the interaction at near-zero platform cost; a positive result would immediately stratify CP0 dietary candidates by genotype. Prioritize as a Tier 0 collaboration request, not an OE solo-data-access project.

---

## ✓ Actioned 2026-05-21 (upgraded to candidate-stratified spec via comp-039)

The generic "polyphenol × CFH" UKB cross-tab has been upgraded to a **candidate-stratified ask** via [comp-039](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md) (2026-05-21). The collaborators (Merriman/Otago, Major-Wrigley/Auckland, Choi/MGH) now have a specific, falsifiable, mechanism-grounded query set rather than a generic "any-polyphenol" sum:

**Lead query (highest power):** rs1061170 × Phenol-Explorer-derived rosmarinic-acid intake quartiles × incident gout M10.x in UKB participants without prior gout at baseline (target n ≈ 450K). Pre-specify BOTH directions:
- Negative direction (Model A — carriers benefit MORE because Y402H baseline severity amplifies absolute effect size)
- Null direction (Model B — mechanism independence implies genotype indifference)
- AMD-paradox direction (HR > 1.5 in carriers × high-intake vs non-carriers × high-intake, p<0.05) **refutes** both and forces retiring rosmarinic acid from the CP0 stack.

**Secondary queries:** (a) rs1061170 × Apiaceae-family intake × incident gout (luteolin proxy + 24h-urate intermediate readout to dissociate from XO/URAT1 modes); (b) rs1061170 × dietary CFH-bypass diversity score × incident gout (composite over rosemary / lemon balm / perilla / celery / parsley, generalizing Bondonno 2025 Nature Food methodology, against Yokose 2024 Rheumatology cohort framework).

**Operational deferrals (real, useful):**
- **HCP/Houttuynia NOT UKB-actionable** — rare in UK dietary corpus. [comp-041 queued](../../wiki/computational-experiments.md) — East Asian cohort feasibility scan (KoGES, China Kadoorie Biobank, Singapore Chinese Health Study) for the Houttuynia-tractable population. Y402H allele frequency lower (~5-6% East Asian vs ~36-39% European) but Houttuynia exposure captured.
- **Helicteres NOT actionable in any biobank yet** — non-dietary + comp-018 Phase 2 replication required first.

**Wet-lab definitive test ([comp-040 queued](../../wiki/computational-experiments.md), blocked on OE wet-lab access):** CFH-depleted-serum MSU-crystal complement-activation assay for rosmarinic acid, luteolin, and HCP. Retained suppression in CFH-depleted serum confirms CFH-independence; loss of suppression refutes.

Cost / time unchanged from Pass 2's framing: $0 OE cost (collaboration request) + ~3 months. Now carrying per-candidate hypotheses + falsification thresholds + ancestry-stratification guidance + confound-adjustment list (BMI, baseline CRP, eGFR, hypertension per Volcik 2008 ARIC + Hecker 2023 CRP, Mediterranean-diet correlation, ancestry-stratification per Volcik 2008 effect-direction differences).

The specific cross-tab spec landed in [`gout-genetic-variants.md`](../../wiki/gout-genetic-variants.md) Category 5 CFH row + [`complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §6.3 during this walk's comp-039 propagation.

Pairs with [Item 1 closure](./2026-05-20-connection-1-cfh-y402h-rs1061170-the-most-common-complement.md), [Item 7 closure](./2026-05-20-contradiction-1-cfh-y402h-dietary-supplementation-the-predicted-beneficial.md), [Item 13 closure](./2026-05-20-priority-action-2-add-the-cfhdietarycp0-biobankmining-proposal-to-gout-action.md).
