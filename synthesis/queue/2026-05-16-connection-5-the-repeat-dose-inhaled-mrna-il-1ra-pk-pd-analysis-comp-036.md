---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 5
global_index: 5
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# The repeat-dose inhaled mRNA-IL-1RA PK/PD analysis (comp-036, YELLOW) re-frames the clinical comparison from "does it match anakinra Cmax?" to "is partial receptor occupancy × cleaner side-effect profile worth it vs. prednisone over decades of recurrent flares?" — a 3-level chain connecting PK/PD modeling to clinical-decision framing to the platform's temporal-stack logic.

5. **The repeat-dose inhaled mRNA-IL-1RA PK/PD analysis (comp-036, YELLOW) re-frames the clinical comparison from "does it match anakinra Cmax?" to "is partial receptor occupancy × cleaner side-effect profile worth it vs. prednisone over decades of recurrent flares?" — a 3-level chain connecting PK/PD modeling to clinical-decision framing to the platform's temporal-stack logic.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md`, `inhaled-mrna-il1ra-pulse-computational.md`, `chassis-pending-interventions.md`, `gout-action-guide.md`, `nlrp3-inflammasome.md`

   - *Page-pair linkage:* **Weak to medium.** `chassis-pending-interventions.md` §4 (inhaled mRNA-IL-1RA) was updated 2026-05-16 with the comp-033 + comp-036 verdicts and the prednisone-displacement argument, but `gout-action-guide.md` has no entry for inhaled mRNA-IL-1RA as a future acute-flare-abort option, and the acute-flare comparator table in `gout-action-guide.md` does not include it.

   - *Why It Matters:* comp-033 (single-dose) returned RED — plasma Cmax of 0.025 µg/mL is 2% of anakinra's 1.5 µg/mL benchmark. But comp-036 (repeat-dose PK/PD with receptor-occupancy framing) found that **BID × 4–28 doses reaches median 50–56% of the 0–72h flare window above 80% receptor occupancy** — not a match for anakinra, but not nothing either. The re-frame changes the clinical question from "is this as good as anakinra?" (no) to "is this meaningfully better than prednisone for a patient facing decades of recurrent flares?"

     The comparison is: prednisone 30–40 mg/day × 5 days delivers full symptom suppression but carries cumulative steroid burden (bone loss, cataracts, adrenal suppression, glucose intolerance, mood/sleep/BP effects) that compounds across 3–6 flares/year × 30 years. Inhaled mRNA-IL-1RA at BID × 4–14 days per flare delivers partial receptor occupancy (50–56% of flare window above 80%) with negligible cumulative burden (no bone/glucose/adrenal effects; the main open safety question is chronic LNP exposure lifetime). The economic comparison is also decisive: $25–200/flare vs canakinumab $3,000/dose → 15–120× cost edge.

     This re-frame has two practical consequences: (a) it changes how partner conversations should be framed — lead with the prednisone-displacement argument, not the anakinra-equivalence argument; (b) it changes which wet-lab measurements are load-bearing — the top two sensitivity drivers from comp-036 are IL-1Ra Kd (ρ = −0.69, log-uniform 0.1–10 nM) and translation-efficiency mass ratio (ρ = +0.58). A modern SPR measurement of IL-1Ra vs IL-1R1 at physiological conditions would tighten the Kd prior from the current 100× range to <2×, collapsing the dominant uncertainty. A ferret/NHP inhaled-LNP + BAL protein quantitation would resolve the translation-efficiency prior.

     The re-frame also connects to the anakinra SC bridge protocol already in `gout-action-guide.md` — anakinra is the same mechanism (IL-1Ra competitive antagonism) at the same chokepoint (CP5a) via a different delivery route (SC injection vs pulmonary mRNA). The temporal stack logic (`open-enzyme-vision.md` §10) positions chronic urate-lowering (koji daily food) + pulsatile flare-abort (mRNA inhaler) as complementary time-regimes; this re-frame sharpens the pulsatile-arm's clinical rationale.

   - *Suggested Action:* (1) Add inhaled mRNA-IL-1RA as a "future (5–10 yr horizon)" row in the `gout-action-guide.md` acute-flare-abort comparator table, with the prednisone-displacement argument as the framing. (2) Queue the two wet-lab measurements (SPR Kd, ferret/NHP translation efficiency) as the comp-036 handoff to any partner conversation. (3) Add a cross-reference from `nlrp3-inflammasome.md` §"Inhaled mRNA-IL-1RA pulse" to the comp-036 re-frame.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The PK/PD and clinical-framing core is correct: `repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md` reports BID ×4–28 doses reaching median 50–56% of the 0–72 h window above 80% occupancy, with Kd and translation efficiency as the top uncertainties, and explicitly reframes the comparator as prednisone displacement rather than anakinra equivalence. The economic numbers in the synthesis are wrong: comp-033 gives $2–120/flare and comp-036 gives $10–600/flare for inhaled mRNA, while comp-036 lists canakinumab at $18,000–23,000 per flare, not $3,000/dose; `chassis-pending-interventions.md` therefore frames the cost edge as 50–3,000×, not 15–120×. Fix the cost comparison, but keep the prednisone-displacement action.
