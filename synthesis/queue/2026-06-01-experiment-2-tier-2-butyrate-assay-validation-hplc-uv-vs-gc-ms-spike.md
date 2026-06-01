---
type: experiment
sweep_date: 2026-06-01
sweep_sha: 8a97f95
section_index: 2
global_index: 7
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Tier 2 butyrate assay validation — HPLC-UV vs. GC-MS spike/recovery on culture supernatant.

2. **Tier 2 butyrate assay validation — HPLC-UV vs. GC-MS spike/recovery on culture supernatant.** Cost: ~$500. Time: 2 weeks. Decides: whether a decentralizable Tier 2 method exists for butyrate in engineered-strain supernatants (the Q141K butyrate-emphasis stack's step-4 verification gap). If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant; if YELLOW, iterate extraction/gradient; if RED, stay on GC-MS and record the Tier-2 gap as unclosed for culture supernatant. This is the first step toward closing the class-level Tier 2 assay gap for microbiome-derived metabolites (SCFAs, secondary bile acids, microbial indoles, TMAO). (Speculative — the method is validated on fecal/cecal-derived cultures, not OE's medium matrix; matrix transfer is the primary risk.)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The Tier 2 butyrate assay validation proposal (HPLC-UV vs. GC-MS spike/recovery) is directly anchored to the 2026-06-01 full-text verification update in `tier-2-butyrate-assay-audit-computational.md`, which states that De Baere et al. 2013 (PMID 23542733) HPLC-UV "SURVIVES" as the candidate for culture supernatant (0.5-50 mM, no derivatization). The cost (~$500) and matrix-transfer risk caveat are both accurate. The experiment is correctly identified as "the first step toward closing the class-level Tier 2 assay gap." Operational note: this is now a tracked wet-lab gate at `validation-experiments.md §1.31` (added 2026-06-01), so the proposal here is consistent with existing corpus infrastructure rather than duplicative.
