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
