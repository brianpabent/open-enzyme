---
type: open-question
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 2
global_index: 14
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# What is the real-world accessibility of off-label anakinra SC for gout — insurance coverage rates, rheumatologist willingness to prescribe, and patient-reported experience with the 3-day protocol?

2. **What is the real-world accessibility of off-label anakinra SC for gout — insurance coverage rates, rheumatologist willingness to prescribe, and patient-reported experience with the 3-day protocol?** The `gout-action-guide.md` anakinra protocol is now the most detailed acute-flare-abort guidance in the corpus (dosing, route, cost, cumulative-burden framing), but the gap between protocol and patient access is uncharacterized. This is a pragmatic research question that determines whether the anakinra recommendation is mechanism-grounded-but-inaccessible or actually actionable. *(Supported by Clinical Trial precedent for anakinra in other indications; the gout-accessibility question is unstudied. See Proposed Experiment #3 above.)*

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the right practical question: `gout-action-guide.md` gives the anakinra acute-flare protocol in enough detail to affect patient behavior, but the "Access" column still says rheumatologist/off-label and insurance variable. Real-world coverage and prescriber willingness determine whether anakinra is a usable bridge away from recurrent prednisone burden or merely a mechanistic ideal.

---

**WALKED 2026-05-19 — Closed (scope narrowed per Brian's call; patient-experience lit scan firing).**

**Brian's 2026-05-19 walkthrough scope-tightening:** the original "accessibility audit" framing conflated three questions:
1. Insurance coverage rates — **OUT of scope.** Cost is documented at $900/flare. Payers vary; this is operational variability, not a platform-relevant research question.
2. Rheumatologist willingness to prescribe — **OUT of scope.** "It's easy to find a doctor who will prescribe anything off-label with enough money." Money + market solves access; this is not a research gap.
3. Patient-reported clinical experience with the 3-day protocol — **IN scope.** Real-world effectiveness, injection-site reactions, comparison to prednisone in user experience, bridge-away-from-prednisone patterns. This is genuinely uncharacterized in the corpus and platform-relevant.

This is **another Pass 3 failure mode worth logging** for the end-of-walk retrospective: Pass 3 confirmed the original audit's full scope ("real-world coverage and prescriber willingness determine whether anakinra is a usable bridge") without pushing back on the platform-irrelevance of the insurance + prescriber-willingness questions. Pass 3 caught the L1 propagation factual error but missed the L2 scope error. Scope-tightening was Brian-only.

Actioned:
- 🔄 Patient-experience lit-scan subagent firing in background with narrowed scope: PubMed real-world / observational data, Reddit r/gout patient experience, injection-site reaction patterns from RA/AS/CAPS adjacent indications, bridge-away-from-prednisone reports. Output → `logs/anakinra-3day-gout-patient-experience-2026-05-19.md`.
- ✗ Insurance coverage research dropped per Brian's scope call.
- ✗ Rheumatologist willingness research dropped per Brian's scope call.

**Personal context from Brian:** he has personally ruled out anakinra because of cost ($900/flare too expensive for his recurrent-flare frequency). Anakinra stays in the wiki because some patients will accept the cost — but the platform's job is documenting mechanism + clinical positioning, not solving individual-payer questions.

Also closes:
- 2026-05-17 experiment-3 (Anakinra SC accessibility audit — narrowed-scope version of same subagent task).
