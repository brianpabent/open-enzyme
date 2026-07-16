---
type: comp-review
comp: comp-038
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-038

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** **Action required.** The original 2026-05-20 YELLOW assay-landscape conclusion is broadly plausible and internally consistent for an abstract-level desk audit. The new 2026-07-14 `outputs/summary.md` full-text-verification addendum, however, is not backed by a reproducible verification artifact, source excerpts, updated `results.json`, or updated provenance. It also conflicts with stale or contradictory downstream wiki text, especially the interpretive page’s older “electrochemical FAILS” section.

## Required actions

1. **Commit a 2026-07-14 verification artifact** under comp-038, e.g. `outputs/full-text-verification-2026-07-14.md` or JSON, containing for each source: DOI/PMID, access path, full-text/protocol availability, exact extracted method fields, quotes or bounded excerpts, page/section/table references where possible, and reviewer/date. Verification criterion: every “VERIFIED” claim in `outputs/summary.md` maps to a row in this artifact.
2. **Update `outputs/results.json` and `inputs/provenance.md`** or add an explicit second-run provenance file so the artifact no longer simultaneously says “full text not extracted” and “full-text gap closed.” Verification criterion: `results.json`/provenance accurately distinguish 2026-05-20 abstract-level run from 2026-07-14 manual/full-text addendum.
3. **Reconcile `wiki/tier-2-butyrate-assay-audit-computational.md`.** Remove or clearly supersede the 2026-06-01 table saying electrochemical-ANN FAILS. Verification criterion: the page has one current verdict for Gu 2026, with hardware/ANN/external-validation caveats but no contradiction.
4. **Update `wiki/computational-experiments.md` comp-038 entry.** Verification criterion: entry reflects HPLC full-text details, Gu 2026 butyric-acid MAE/RMSE if accepted, and states the next gate as paired spike/recovery + GC-MS / independent validation, not “full-text verification” if that is now closed.
5. **Verify and reconcile `validation-experiments.md` §1.31.** Verification criterion: the anchor exists, is linked from the dashboard if decision-relevant, and separately specifies culture-supernatant HPLC-UV vs GC-MS and stool electrochemical-ANN vs GC-MS criteria if both are retained.
6. **Run a corpus-wide affected-page search once repository search works.** Search by `42041444`, `electrochemical FAILS`, `HPLC-UV`, `butyrate assay`, `SCFA ELISA`, `De Baere`, `Gu et al.`, and `validation §1.31`. Verification criterion: no page still claims electrochemical stool SCFA profiling “fails / do not re-surface” unless clearly marked as superseded history.
7. **Tighten wording of “full-text verified.”** Verification criterion: all pages distinguish “primary-source method details verified” from “OE assay validated.” The latter remains untrue until spike/recovery and paired GC-MS are completed.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
