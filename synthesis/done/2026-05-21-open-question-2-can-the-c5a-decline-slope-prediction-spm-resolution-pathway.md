---
type: open-question
sweep_date: 2026-05-21
sweep_sha: 3edb643
section_index: 2
global_index: 10
pass3_verdict: Defer
overlap_tag: EXTENSION
---

# Can the C5a decline-slope prediction (spm-resolution-pathway.md §7.3) be tested retrospectively on existing flare events in the self-experiment log, and if so, does the slope correlate with omega-3 index at the time of each flare?

2. **Can the C5a decline-slope prediction (spm-resolution-pathway.md §7.3) be tested retrospectively on existing flare events in the self-experiment log, and if so, does the slope correlate with omega-3 index at the time of each flare?** This requires: (a) that the self-experiment log has dated flare events with onset/resolution timestamps, (b) that concurrent omega-3 index measurements exist (or can be approximated from supplementation records), and (c) that serum C5a was measured at both onset and resolution for at least one flare. If any of these three conditions is already met in the existing data, this retrospective test costs $0 and takes an afternoon — the highest insight-per-dollar experiment in the entire queue. If none are met, the prospective design in Proposed Experiment #1 above is the path forward.

   

---

> **Pass 3 review — Defer.** `[OVERLAP: EXTENSION]` The retrospective C5a-slope analysis is a good zero-dollar question, but the repository cannot answer it because `self-experiment-protocol.md` §7 explicitly keeps raw n=1 lab data and logs in private storage and only allows stripped qualitative summaries in the public repo. The necessary facts — dated flare events, contemporaneous omega-3 index or supplementation records, and paired onset/resolution C5a values — are private-data dependent. Defer to Brian’s private self-experiment archive; if the three data elements exist, the analysis should be run before adding more prospective burden.

---

## ✓ Actioned 2026-05-22

**Closure (retrospective analysis impossible; forward path captured):** Pass 3 correctly deferred to the private archive. The deferred check was performed 2026-05-22 by reading Brian's `abent-family-health/` repo directly. Three required data elements assessed:

- **(a) Dated flare events with onset/resolution timestamps:** ✓ Present. 2023-02-20 documented podagra flare, 2026-05-07 ULT-mobilization flare (in taper washout window at the time of this walk), ~6–12 self-suppressed prodromes 2023–2025 (undated; standing prednisone-taper pattern documented in `abent-family-health/brian/notes/2026-04-27_gout-flare-rescue-prednisone.md` and `abent-family-health/brian/symptoms/gout-flare-log.md`).
- **(b) Concurrent omega-3 index measurements:** ✗ Never tested. Daily 1,250 mg fish oil supplementation documented in 2026-04-09 baseline panel stack, but no omega-3 index (RBC fatty-acid %) assay in any historical panel.
- **(c) Serum C5a at onset/resolution:** ✗ Never tested. C5a not in any historical Quest/LabCorp panel.

**Two of three required data elements absent → retrospective C5a-decline-slope analysis cannot be run on historical data.** Pass 3's defer is converted to a closed verdict: retrospective is structurally impossible from the existing record.

**Forward-looking path captured:**
- `abent-family-health/brian/notes/velez-ask-list.md` updated 2026-05-22 with three new rows under "🟡 Labs to add to next draw" — serum C5a (with pre-analytics note), omega-3 index (with home-DBS alternative), CFH Y402H genotype (with consumer-array raw-data alternative). Next draw is ~2 weeks out.
- `abent-family-health/brian/notes/personal-monitoring-protocol.md` updated 2026-05-22 with §6.5 "Home-monitoring formats — brand specifics" — names OmegaQuant DBS kit, 23andMe rs1061170 raw-data path, BeneCheck Uni UA (already in use). Companion to the generic format taxonomy added to OE wiki `self-experiment-protocol.md` §4 the same day.

**First prospective C5a-decline-slope data point becomes scoreable** at the next flare following the upcoming Vélez draw, assuming the three labs land. No public-wiki action remains — this open question closes with the private-repo updates plus the OE wiki protocol-tightening done in parallel.
