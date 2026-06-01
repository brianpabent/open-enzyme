---
type: open-question
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 8
global_index: 15
pass3_verdict: unknown
overlap_tag: RESTATEMENT
---

# What is the quantitative relationship between dietary rosmarinic acid intake and gut-luminal + plasma concentrations?

8. **What is the quantitative relationship between dietary rosmarinic acid intake and gut-luminal + plasma concentrations?** (Gates the dietary-CP0 strategy and the dormant C1-INH + rosmarinic acid composition in complement-c5a-gout.md §9.9.) (source: open-questions.md §"Riskiest assumption #3")

> **Claude review — Confirmed.** `[OVERLAP: RESTATEMENT]` The rosmarinic-acid PK question is already a named dietary-CP0 uncertainty: `open-questions.md` and comp-039 both treat the dietary intake → gut-luminal/plasma concentration chain as unresolved, and comp-029’s sensitivity to rosmarinic-acid IC50 makes that uncertainty load-bearing. It should remain open until a human dietary-source PK anchor exists.

---

## ✓ Actioned 2026-06-01 (did the work — multilingual RA PK scan)

Ran a foreground multilingual PK scan (English + Chinese 迷迭香酸 + Japanese ロスマリン酸) on the lead dietary-CP0 candidate. Result: does **not** anchor the assumption; leaves it unanchored and **mildly weakens the distal-gut version** of the thesis — but sharpened it materially:

- **No direct gut-luminal RA measurement exists field-wide** (not just our corpus). The 252–1,100 µM figure is a *calculation*, located stated-as-such in Sasaki et al. PMC7828042. (Flagged: reconcile the corpus's "Kang 2021" attribution vs Sasaki lineage — both are calculated, so the point stands.)
- **Plasma route confirmed out** (corroborates comp-029): oral BA ~1–2%; free plasma RA ~0.02–0.16 µM (human) to ~0.6–2 µM (rat) — order-of-magnitude below the complement IC50.
- **NEW — proximal vs. distal:** RA survives the proximal small intestine intact but colonic microbiota degrade it to caffeic acid before the distal gut (microbiota-mediated, shown in antibiotic-treated animals). Since comp-020 verified C3b modification by *intact* RA, the CP0 mechanism is most defensible **proximally**; the colonic/distal framing is weakest (metabolites, not intact RA).
- **Cheapest de-risking experiment:** direct segmental rat intestinal-content RA assay (proximal→distal, LC-MS/MS) — "the single highest-value PK datum the project lacks."

**Both updates landed (per Brian):**
1. [`open-questions.md` §"Riskiest assumption #3"](../../wiki/open-questions.md) — ✓ scan note with the above (calculated-not-measured field-wide, plasma shortfall, proximal-vs-distal metabolite nuance, cheapest experiment, PK detail with citations).
2. [`complement-c5a-gout.md` §9.9](../../wiki/complement-c5a-gout.md) (dormant C1-INH + RA composition) — ⚠ gut-compartment co-localization caveat: C1-INH/EcN-LBP colonizes the distal gut/colon while intact RA is proximal, so the two arms may not co-localize; sharpens reactivation condition #2 to require *segmental* PK.

Genuine do-the-work payoff: not "gap confirmed" but a new proximal-vs-distal compartment insight that re-shapes where the dietary-CP0 mechanism (and the C1-INH+RA composition) is defensible.
