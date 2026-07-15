---
type: experiment
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 1
global_index: 5
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Tier 2 Butyrate Assay Validation — HPLC-UV vs. GC-MS spike/recovery.

1. **Tier 2 Butyrate Assay Validation — HPLC-UV vs. GC-MS spike/recovery.** Cost: ~$500. Time: 2 weeks. Decides: Whether a low-cost, decentralizable Tier 2 butyrate quantification method for engineered-strain culture supernatant validates against the Tier 3 GC-MS gold standard well enough to replace it for OE's near-term need. The quantification ladder needs a cheap Tier 2 surface between visual/user-facing proxies and Tier 3 GC-MS / HPLC / LC-MS anchors. For microbiome-derived metabolites, that gap is especially painful: the genotype-informed supplement workflow can recommend butyrate-emphasis interventions for ABCG2 Q141K carriers, but it cannot yet verify butyrate delivery with a validated home or community-biolab Tier 2 assay. comp-038 reframes that gap as two different problems: (1) culture-supernatant butyrate from engineered strains: plausible Tier 2-lab path exists via HPLC-UV, with GC-MS as anchor; (2) stool/serum/home butyrate exposure: no ready-to-adopt Tier 2 method surfaced; electrochemical fecal SCFA profiling is promising but not production-ready. This does not change §1.14's priority framing; it keeps concentration verification tied to a Tier 3 analytical anchor if butyrate exposure becomes load-bearing. (source: tier-2-butyrate-assay-audit-computational.md, validation-experiments.md §1.31)

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The HPLC-UV vs. GC-MS spike/recovery experiment is correctly scoped from comp-038's YELLOW verdict and the full-text verification pass (De Baere 2013, PMID 23542733, validated on bacterial culture supernatant, linear 0.5–50 mM, no derivatization). The tier-2-butyrate-assay-audit-computational.md page confirms the full-text verification was completed 2026-06-01 and the empirical spike/recovery is the remaining wet-lab gate. The cost estimate ($500) is plausible for a contract-lab paired run. The connection to the genotype-informed supplement workflow's Q141K butyrate-emphasis example is valid — without a validated Tier 2 butyrate ruler, butyrate-emphasis interventions cannot be cheaply verified, and the "silent underdosing" failure mode the workflow was designed to block remains unclosed. The reframe into two different problems (culture-supernatant vs. stool/serum/home) is honest and correctly scoped. This is the highest-leverage $500 experiment in the current queue.

---

## ✓ Actioned 2026-07-14

**Experiment already registered — no new validation entry needed.** validation-experiments.md **§1.31** "Tier 2 Butyrate Assay Validation — HPLC-UV vs. GC-MS spike/recovery" (added 2026-06-01) already operationalizes this as a tracked wet-lab gate with GREEN/YELLOW/RED criteria. Pass 3's "Confirmed, prioritize" verdict noted; the empirical spike/recovery is the remaining wet-lab gate (OE is Phase 0 — needs partner-CRO / community-biolab HPLC-UV + GC-MS access).

**De Baere 2013 verified against the primary source (do-the-work close of the comp-038 audit caveat).** The comp-038 comp-review flagged that the "full-text verification complete" claim was not in the comp-038 artifact. Per PubMed, all three load-bearing De Baere et al. 2013 specifics (*J Pharm Biomed Anal* 80:107–115, PMID 23542733, DOI 10.1016/j.jpba.2013.02.032) are confirmed from the source: bacterial-culture-supernatant matrix, linear 0.5–50 mM (r 0.9951–0.9993, LOQ 0.5–1.0 mM), underivatized (direct UV 210 nm). Re-anchored the load-bearing claim to the primary source directly across `open-questions.md`, `computational-experiments.md`, and the comp-038 interpretive page (partial-resolution note on its audit banner). The unverified electrochemical (PMID 42041444) + SCFA-ELISA rejections are flagged **provisional** rather than left as settled.

**Not done:** did not update the comp-038 *artifact* itself (would re-trigger the comp-review daemon; the interpretive page carries the resolution instead); did not verify PMID 42041444 (not load-bearing for §1.31 — a rejected alternative, flagged provisional).

### ↳ Loose ends tied up 2026-07-14

Both deferred loose ends from the close above were then resolved:
- **PMID 42041444 (electrochemical) verified — and the earlier "FAILS / do not re-surface" claim was WRONG.** Per PubMed, Gu et al. 2026 (*Biosensors* 16(4):223, DOI 10.3390/bios16040223) validated the electrochemical-ANN fecal SCFA platform against GC-MS in an independent fecal cohort (n=30), butyric-acid MAE/RMSE 0.029/0.034 mM — mM-range, butyrate-specific, no pg/mL mismatch. It is a genuine stool-track Tier-2 candidate (matching comp-038's own "most promising stool-specific direction"). Corrected in `open-questions.md`, the comp-038 interpretive page, and `quantification-ladder.md`. SCFA ELISA kits stay RED-provisional (no validation surfaced).
- **comp-038 artifact updated.** Added a dated "Full-text verification addendum" to `etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md` recording both verifications — closing the audit's core concern (verification now IN the artifact, not only on downstream pages). This artifact change will trigger a fresh comp-review-038 on push (correct backstop behavior).
