---
type: experiment
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 1
global_index: 5
pass3_verdict: unknown
overlap_tag: RESTATEMENT
---

# Tier 2 butyrate assay validation (comp-038 next step).

1. **Tier 2 butyrate assay validation (comp-038 next step).** Cost: $500. Time: 2 weeks. Decides: Whether a home/community-biolab Tier 2 method exists for butyrate (HPLC-UV or electrochemical fecal SCFA) that can be validated against GC-MS. Gating for genotype-informed workflow §4 (Q141K butyrate stack) and all future microbiome-metabolite interventions.

> **Claude review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` comp-038 already concludes there is no ready-to-adopt home butyrate Tier 2 assay and names the next move: full-text/protocol verification of PMID 23542733 and PMID 42041444 plus sodium-butyrate spike/recovery against GC-MS. This is operationally high leverage because the Q141K butyrate workflow currently uses exposure proxies rather than input-potency verification, as `genotype-informed-supplement-workflow.md` explicitly warns.

---

## ✓ Actioned 2026-06-01

**Did the work to the edge of our tooling.** The wet-lab spike/recovery itself is gated (OE Phase 0, no analytical instruments). But comp-038's "Next Step" had a literature half we *could* run now — and it was the gate before any wet lab.

**1. Promoted to a tracked experiment.** Added [`validation-experiments.md` §1.31](../../wiki/validation-experiments.md) "Tier 2 Butyrate Assay Validation — HPLC-UV vs. GC-MS spike/recovery," mirroring §1.28's shape, scoped to the single decision (does a Tier-2 method validate against GC-MS for culture supernatant?). Moved it out of comp-038 prose into the runnable queue.

**2. Ran the full-text verification pass** (foreground Opus subagent, multilingual — English + Chinese analytical-chemistry sources). Resolved the candidate question decisively:
- **HPLC-UV (De Baere 2013, PMID 23542733) — SURVIVES** the Tier-2 gate: culture-supernatant matrix (OE's need), 0.5–50 mM linear, no derivatization, butyrate resolved. Community-biolab tier (needs HPLC). → the candidate to validate.
- **Electrochemical+ANN (Gu 2026, PMID 42041444) — FAILS**: vendor-locked hardware + dual derivatization + unreleased ANN that requires GC-MS to retrain (so GC-MS is a prerequisite, not replaced). Fecal-only.
- **ELISA kits — FAIL**: pg/mL range vs mM samples (5–6 orders off); unvalidated specificity.

**3. Recorded the verification canonically** in [`tier-2-butyrate-assay-audit-computational.md` §"Full-text verification — completed 2026-06-01"](../../wiki/tier-2-butyrate-assay-audit-computational.md) so the failed candidates don't get re-surfaced, with a [TRANSLATION NOTE] on the derivatization-vs-direct-UV distinction from the Chinese literature.

**Net:** candidate-selection question closed; only the empirical spike/recovery remains, now tracked at §1.31 with GREEN/YELLOW/RED criteria, awaiting wet-lab access. This is the butyrate-specific instance of the class-level gap in **Item 13** (open-question-6).
