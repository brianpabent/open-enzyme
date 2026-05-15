---
type: open-question
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 1
global_index: 8
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# Can the compounding pharmacy track’s repurposed-drug formulations be combined with the engineered-koji daily food to create a layered intervention — a pharma pill for CP6a/CP6b plus a food for CP1-CP5 and urate degradation?

1. **Can the compounding pharmacy track’s repurposed-drug formulations be combined with the engineered-koji daily food to create a layered intervention — a pharma pill for CP6a/CP6b plus a food for CP1-CP5 and urate degradation?** The two tracks target non-overlapping chokepoints and consumption modes (Rx pill + daily condiment). The combination is mechanistically clean, but no protocol exists for co-administration, and the patient experience (daily pill + daily fermented food) has not been modeled. (Context: `compounding-pharmacy-track.md` §“Combined / hybrid candidates”; `koji-endgame-strain.md` coverage matrix.)

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` This open question is already named almost verbatim in `compounding-pharmacy-track.md` under "Combined / hybrid candidates," which gives the example of compounded low-dose disulfiram ER plus daily shio-koji delivering uricase. The synthesizer correctly identifies the missing next layer — no co-administration protocol or patient-experience model exists — but the question itself is a first-class existing page element.

---

## ✓ Actioned 2026-05-15

The combined-intervention question lived only on `compounding-pharmacy-track.md` §"Combined / hybrid candidates" — not surfaced in `wiki/open-questions.md`, which means daemon sweeps weren't re-surfacing it as an open question.

**Files shipped:**
- **`wiki/open-questions.md` §Platform/Strategic** — new section "Layered intervention — combining a compounded repurposed-drug pill with the engineered-koji daily food" added above the H08 riskiest-assumption section. Lists four concrete sub-questions (timing, patient experience, endpoints/biomarkers, drug-food interactions); cross-links to the canonical scope pages.
- **Explicit "Fires when" trigger:** dormancy is gated on two upstream products that don't exist yet — (a) compounding-pharmacy first prescription pathway opens, (b) engineered-koji strain becomes available (Phase 0 currently). Until both, drafting a co-administration protocol is path-dependent speculation. The trigger language follows the same discipline added to compounding-pharmacy-track.md Phase 2 items in Item 10's follow-up commit.

**Why no protocol draft:** Pass 3 correctly noted the missing layer is the protocol, but neither the compounded pill nor the engineered koji exists in production form. Drafting a co-administration protocol for two non-existent products would be path-dependent — better to surface the question with a clear trigger and revisit when the gates clear. This is the "first-principles framing" rule per umbrella CLAUDE.md: don't gate exploration by current-chassis assumptions; do gate execution by load-bearing constraints.
