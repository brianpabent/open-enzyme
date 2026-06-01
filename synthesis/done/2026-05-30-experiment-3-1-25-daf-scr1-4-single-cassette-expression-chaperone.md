---
type: experiment
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 3
global_index: 7
pass3_verdict: unknown
overlap_tag: RESTATEMENT
---

# §1.25 DAF SCR1-4 single-cassette expression + chaperone-framework calibration (two-arm RIB40 + NSlD-ΔP10).

3. **§1.25 DAF SCR1-4 single-cassette expression + chaperone-framework calibration (two-arm RIB40 + NSlD-ΔP10).** Cost: $4,445–6,745 (includes Plasmidsaurus QC). Time: 6–8 weeks. Decides: Whether SCR1-4 secretes as correctly-folded, complement-regulatory-active protein in *A. oryzae* solid-state koji. Mandatory calibration arm resolves the α-coefficient uncertainty in chaperone-orthogonal-stacking.md §3.5.4.

> **Claude review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The experiment is valid, but the cost/specification is not what the active validation dashboard says: `validation-experiments.md` lists §1.25 as DAF SCR1-4 single-cassette expression with a two-arm cost of **$3,500–5,500**, not $4,445–6,745, and the paired α-calibration priority is explicitly §1.9 + §1.25 under harmonized conditions. Topic right; quoted budget and arm framing need correction before emission.

---

## ✓ Actioned 2026-06-01

**RESTATEMENT of existing §1.25 — and Pass 3's push-back was itself wrong.** §1.25 (DAF/CD55 SCR1-4 truncated single-cassette expression in *A. oryzae*) is already fully built, with the mandatory two-arm RIB40 + NSlD-ΔP10 design and the chaperone-framework α-calibration role. No design change; wet-lab gated (Phase 0; CRO / community-biolab with *A. oryzae* protoplast-transformation capability; co-batches with §1.9).

**Doing the work surfaced a real internal inconsistency.** The synthesizer (Pass 2) quoted §1.25 cost $4,445–6,745; Pass 3 "corrected" it to $3,500–5,500 and called the synthesizer wrong. Verification showed the opposite: $4,445–6,745 is the **current** figure (§1.25 header + cost-breakdown, updated 2026-05-17 when the Plasmidsaurus QC pipeline was added), while $3,500–5,500 was a **stale summary-table** value (line 60) never updated after that re-scope. Grok read the current header; Pass 3 read the stale table; neither noticed they disagreed. The same staleness affected §1.9 (header $5,265–8,065 vs stale table $3,000–5,000) and the priority-gate combined figure ("~$5–7K", pre-re-scope).

**Fixed three stale cost references in [`validation-experiments.md`](../../wiki/validation-experiments.md):**
1. Summary table §1.9: $3,000–5,000 → **$5,265–8,065** (matches header)
2. Summary table §1.25: $3,500–5,500 → **$4,445–6,745** (matches header)
3. Priority-gate combined figure (line 32): "~$5–7K" → **"~$10–15K if run independently; less under co-batch execution"** (with the per-experiment breakdown + parallel-wall-time note)

All three traced to the 2026-05-17 Plasmidsaurus-QC + RNA-Seq re-scope that updated the detailed entries but not the summary table or combined figure. This is the internal-consistency fix the sweep should have produced instead of a contradictory restatement — and a clean instance of the do-the-work rule catching a Pass-3 error that rested on a stale corpus number.
