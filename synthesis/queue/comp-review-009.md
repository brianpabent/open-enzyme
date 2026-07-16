---
type: comp-review
comp: comp-009
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-009

**Why blocked:** Action required. The rerun computation appears to have corrected the original fatal substitution from artificial back-translated CDS to real NM_144585.4 mRNA, but the artifact and corpus still contain stale original-run claims, old guide sequences, old funnel counts, and over-strong “viable/accessible” wording. The computation supports only “filter-passing real-transcript candidate sites exist”; it does **not** establish accessible, off-target-cleared, cross-species-reusable, or wet-lab-ready siRNA guides.

## Required actions

1. Update `README.md` to fully reflect the rerun: real NM_144585.4 input, ViennaRNA dependency, 2711/222/120/76/31/8 funnel, new shortlist, no back-translation, no stdlib-only claim, no original guide table.
2. Update `wiki/urat1-sirna-target-site-selection-computational.md`: replace old funnel/top-5/limitations with rerun values and remove all invalidated original guide sequences.
3. Update `wiki/sirna-urat1-modality.md` and `wiki/chassis-pending-interventions.md` so comp-009 P2-2 is no longer queued; state “completed rerun, availability only; low accessibility and off-target clearance remain open.”
4. Reword `outputs/summary.md` and any wiki verdicts from “viable/accessibile sites” to “filter-passing candidate sites,” unless an explicit accessibility threshold is defined and met.
5. Pin the reproducibility environment: ViennaRNA version, Python version, install command, and ideally a lockfile or recorded package version; remove contradictory stdlib-only language.
6. Remove stale inputs/docs (`human_codon_usage.json`, old `structural_accessibility` and cross-species-reuse claims in `design_parameters.json` / `orthologs.json`) if the current rerun no longer uses them.
7. Fix region annotation for boundary-spanning windows, especially mRNA position 326, or explicitly exclude/report UTR/CDS-overlap targets.
8. Before any wet-lab handoff, run transcriptome seed/off-target clearance against relevant human transcript/3'UTR databases and, if cross-species reuse matters, repeat against real ortholog mRNAs.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
