---
type: experiment
sweep_date: 2026-06-02
sweep_sha: 405b50a
section_index: 1
global_index: 5
pass3_verdict: Partial
overlap_tag: RESTATEMENT
---

# Tier 2 butyrate assay validation (HPLC-UV vs. GC-MS spike/recovery on culture supernatant).

1. **Tier 2 butyrate assay validation (HPLC-UV vs. GC-MS spike/recovery on culture supernatant).** Cost: ~$500. Time: 2 weeks. Decides: whether a decentralizable Tier 2 method exists for butyrate in engineered-strain supernatants, closing the quantification-ladder gap for the Q141K butyrate-emphasis stack. (source: tier-2-butyrate-assay-audit-computational.md, validation-experiments.md §1.31)

> **Pass 3 review — Partial.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The experiment is accurately referenced: HPLC-UV vs. GC-MS spike/recovery for butyrate in engineered-strain culture supernatant is proposed at `validation-experiments.md §1.31` with cost ~$500 and time ~2 weeks. The claim that this "closes the quantification-ladder gap for the Q141K butyrate-emphasis stack" overreaches. Per `tier-2-butyrate-assay-audit-computational.md` (comp-038) and `validation-experiments.md §1.31`, this method is validated for **culture supernatant only** — engineered-strain work. The patient-facing Q141K butyrate-emphasis stack at `genotype-informed-supplement-workflow.md` operates on **stool/serum butyrate**, which is a separate matrix. §1.31 explicitly states: "Stool/serum butyrate monitoring (the patient-facing future) is a *separate* matrix and a separate validation." Tighten the scope claim to "culture-supernatant butyrate for engineered-strain work" and note the stool/serum gap remains open.

---

## ✓ Actioned 2026-07-13 (batch-close)

**Restatement of `validation-experiments.md` §1.31** (Tier-2 Butyrate Assay Validation — HPLC-UV vs. GC-MS spike/recovery, culture supernatant; added 2026-06-01), fully specified there. Scope per §1.31: validated for culture supernatant only; stool/serum is a separate matrix + separate validation. No new wiki work. Closure.
