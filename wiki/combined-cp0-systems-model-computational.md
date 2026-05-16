---
title: "Combined CP0 Systems Model — Dietary Rosmarinic Acid + Engineered DAF SCR1-4 (Computational, comp-029)"
date: 2026-05-16
tags:
  - computational
  - comp-029
  - complement
  - CP0
  - rosmarinic-acid
  - DAF
  - CD55
  - systems-model
  - monte-carlo
  - gout
related:
  - complement-c5a-gout.md
  - daf-cd55-scr14-truncated-computational.md
  - upstream-complement-modulator-sweep-computational.md
  - upstream-complement-verification-rerun-computational.md
  - chaperone-orthogonal-stacking.md
  - validation-experiments.md
  - computational-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
sources:
  - "Sahu A, Rawal N, Pangburn MK. Biochem Pharmacol 1999;57(12):1439-46 (PMID 10353266); rosmarinic acid C3b covalent IC50 34 μM + 44× assay-format spread"
  - "Englberger W et al. Int J Immunopharmacol 1988;10(7):729-37 (PMID 3198307); rosmarinic acid C3 convertase IC50 5-10 μM optimal lower bound"
  - "Baba S et al. Life Sci 2004;75:165-78 (PMID 15120569); human Perilla 200 mg single-dose plasma free RA Cmax 20 nM / conjugated 1200 nM"
  - "Wang J et al. RSC Adv 2017;7:9057-63 (DOI 10.1039/C6RA28237G); rat oral RA absolute bioavailability 0.9-1.7%"
  - "Kang YJ et al. Pharmaceutics 2021;13:83 (PMC7828042); RA gut-luminal concentration 252-1100 μM after 200 mg oral; plasma protein binding 91.4%"
  - "Veras KS et al. Pharmaceutics 2022;14:2663 (PMC9784852); RA gastric stability ≥98%, intestinal recovery 69-75%"
  - "Fischer E, Kazatchkine MD. J Exp Med 1981;153:1671-1681 (PMC2186394); CP convertase C4b2a intrinsic t₁/₂ = 7.5 min at 37°C"
  - "Medof MD, Kinoshita T, Nussenzweig V. J Exp Med 1984;160:1558-1578 (PMC2187498); 10² DAF/cell profoundly inhibits convertase assembly"
  - "Kinoshita T et al. J Exp Med 1987;166:1376-1389 (PMC2189641); DAF dissociates C2a from C4b2a and Bb from C3bBb"
  - "Medof MD et al. J Exp Med 1987;165:848-864 (PMC2188295); soluble DAF detected in synovial fluid"
  - "Wessig AK et al. Sci Rep 2022;12:4423 (PMC8924570); MSU + IgM + CRP serum drives C3a/C5a generation"
  - "Khameneh HJ et al. Front Pharmacol 2017;8:10 (PMC5253373); murine i.p. MSU → C5a-dependent IL-1β + neutrophil recruitment"
status: complete (v1; verdict YELLOW; gated on wet-lab α measurement from §1.25)
---

# Combined CP0 Systems Model — Dietary Rosmarinic Acid + Engineered DAF SCR1-4 (Computational, comp-029)

> **Frozen analysis lives at [`../experiments/comp-029-combined-cp0-systems-model/`](../experiments/comp-029-combined-cp0-systems-model/) — README + analyze.py + inputs/ + outputs/ all committed for reproducibility.**
> This wiki page is the interpretive layer; the analysis script is stdlib-only Python 3 and reproduces deterministically with RNG seed 29.

## The question

[`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) added the **combined-CP0-coverage hypothesis** on 2026-05-15: two CP0 threads (dietary rosmarinic acid + engineered DAF SCR1-4) operate at different geometric scales (fluid-phase / gut-luminal vs. MSU crystal surface), use different mechanisms (covalent C3b modification vs. decay-acceleration), and might therefore compose into additive CP0 coverage without relying on avacopan (the only OE CP0 candidate with serious clinical-development infrastructure, but expensive and on-patent).

Does the predicted combined-effect range, with explicit confidence bounds over published priors, meaningfully exceed either intervention alone?

## Verdict: YELLOW

| DAF accessibility prior | DAF α | RA alone median | DAF alone median | Combined median | Combined/better-singleton ratio | Verdict |
|---|---|---|---|---|---|---|
| Low | 0.05 | 0.886 | 0.568 | 0.956 | 1.08 | YELLOW |
| Medium | 0.20 | 0.886 | 0.815 | 0.979 | 1.10 | YELLOW |
| High | 0.80 | 0.886 | 0.914 | 0.989 | 1.08 | YELLOW |

**Per the comp-029 brief decision rule** (GREEN needs combined ≥ 1.5× the better singleton AND combined 95% CI strictly above singleton 95% CI), none of the three accessibility priors clears either threshold. The combined median is only 1.08-1.10× the better singleton, and the combined 95% CI overlaps both singleton CIs.

## Why YELLOW, mechanistically

**Both arms individually saturate at their operative concentrations.** RA in the gut-luminal regime (50-1100 μM after 50-200 mg oral dose) hits the C3 convertase IC50 range (5-180 μM) hard — median inhibition fraction 0.886. DAF SCR1-4 at 10-500 nM secreted concentration with even modest accessibility hits decay fraction 0.5-0.9 across the three accessibility priors. When two interventions each already produce 60-90% reduction independently, multiplicative composition (the standard treatment of two independent fractional reductions: f_combined = 1 - (1-f_RA)(1-f_DAF)) has structurally little room to grow — the combined ratio against the better singleton is mathematically capped near 1.1×.

This is **not a refutation of the combined-coverage hypothesis.** It's a mathematical feature of saturated singletons. The two interventions DO compose as the §9.7 hypothesis claimed; the issue is that under current input uncertainty, the combined effect is **probably** larger than either alone but not provably-large-enough to justify wet-lab co-administration cost.

## What comp-029 rules OUT

The **RED verdict path is closed.** No interaction blocker found at any of three candidate failure modes:

1. **RA covalently inactivates DAF SCR1-4 via the catechol / α,β-unsaturated ester** — no published evidence. RA's covalent chemistry targets activated C3b nucleophilic acceptor sites; SCR/CCP-domain proteins do not present the same chemistry, and DAF binds C3b through reversible protein-protein interaction.
2. **DAF degraded under gut-luminal RA-bioavailable conditions** — comp-012 explicitly verified DAF SCR1-4 LOW protease risk in shio-koji and gut-luminal conditions. RA does not alter pH or protease activity in a way that would compromise DAF stability.
3. **RA + DAF compete for C3b binding** — RA modifies C3b post-deposition (covalent); DAF accelerates C2a/Bb dissociation from already-assembled C3b complexes. The two operate at different time points on different C3b states. Mechanistically complementary, not competitive.

(Mechanistic Extrapolation.)

## What comp-029 rules IN

1. **The two interventions hit the geometric scales the §9.7 hypothesis claimed.** RA contributes via the **gut-luminal transient**, not systemic plasma — Baba 2004 free plasma Cmax of 20 nM is ~1700× below the central IC50 (34 μM), giving essentially 0% inhibition (median 0.0007). The gut-luminal regime at 252-1100 μM (Kang 2021) DOES reach mechanistically active concentrations — median 0.886. **This sharpens the wet-lab framing: the right RA readout is a gut-luminal complement-activation assay, not a plasma-based one.** (Mechanistic Extrapolation over In Vitro Sahu 1999 + Clinical Trial Baba 2004 anchors.)

2. **DAF SCR1-4 contributes via MSU-surface decay-acceleration**, with effective concentration in the 10-500 nM range and accessibility α as the single load-bearing wet-lab unknown (comp-012's explicit Limitations section).

3. **The combined-effect distribution is broadly higher than either singleton**, just not separated under current prior uncertainty. The wide singleton CIs (RA p5=0.44, DAF p5=0.18-0.77 depending on α) leak into the combined CI.

## Dominant uncertainty drivers

| Input | Spearman r vs combined (α=0.20) | Prior spread |
|---|---|---|
| RA gut-luminal IC50 | **-0.658** (largest) | 36× (5-180 μM) |
| RA gut-luminal [RA] | +0.552 | 22× (50-1100 μM) |
| DAF effective [DAF] | +0.480 | 50× (10-500 nM); accessibility α adds another 16× |

**Top wet-lab measurement that would tighten the prediction most:**

**Measure DAF SCR1-4 MSU-surface engagement fraction.** This is the load-bearing wet-lab unknown per comp-012's explicit Limitations section and the dominant uncertainty driver in comp-029's sensitivity analysis. One experiment, one parameter, currently a 16× prior spread.

[`validation-experiments.md` §1.25](./validation-experiments.md) DAF SCR1-4 expression screen already provides the right functional readout (zymosan or MSU-crystal C5a-generation assay ± DAF). The §1.25 functional arm directly resolves α as a side product of its primary experimental aim. **No new wet-lab experiment is gated by comp-029 — only an optional co-treatment arm WITHIN the already-planned §1.25 experiment, gated on §1.25's own functional readout.**

## Wet-lab handoff to §1.25

If §1.25 returns α ≥ 0.5 (mid-to-high MSU-surface engagement), comp-029 re-runs to GREEN — DAF alone saturates and the combined ratio improves. The marginal-cost RA co-treatment arm is then justified:

> **Optional co-treatment arm (gated on §1.25 functional readout showing DAF SCR1-4 mid-to-high MSU-surface engagement):** Add a co-treatment condition to the §1.25 zymosan / MSU-crystal C5a-generation assay: DAF SCR1-4 expressed material (mature, ELISA-quantified) + rosmarinic acid at 100 μM (gut-luminal regime; matches the median Sahu 1999 C3b-deposition IC50) co-incubated 30 min at 37°C with complement-competent serum + MSU crystals. Compare C5a + C5b-9 generation across (i) DAF SCR1-4 alone, (ii) RA alone, (iii) DAF + RA combined, (iv) vehicle. Marginal cost: one additional condition per plate; readout: same ELISA already in the §1.25 plan.

If §1.25 returns α < 0.2, comp-029 stays YELLOW and the combined-strategy thesis is parked. RA alone via the gut-luminal regime survives as a stand-alone dietary intervention; engineered DAF SCR1-4 survives as a stand-alone CP0 candidate at the MSU surface; the combined-coverage claim is shelved until a new mechanism or geometry surfaces.

## Pass 3 softening discipline honored

This page explicitly does **not** claim:

1. **The two interventions are "mechanistically additive."** Multiplicative composition of independent fractional reductions is the standard treatment; super-additivity would require coupling we did NOT find.
2. **Rosmarinic acid "saturates fluid-phase and gut-luminal C3 convertase."** It saturates the GUT-LUMINAL regime (post-meal, transient), and contributes essentially 0% at SYSTEMIC free-RA concentrations. The two are 4-5 orders of magnitude apart.
3. **Downstream clinical effect size.** Even if the mechanism prediction holds, downstream clinical SUA / IL-1β effect-sizes are gated by the H08-class clinical-translation question covered separately.

## Evidence levels

- **In silico systems composition over published kinetic constants:** Mechanistic Extrapolation.
- **Sahu 1999 / Englberger 1988 IC50 values:** In Vitro.
- **Baba 2004 human plasma Cmax:** Clinical Trial (single-dose human PK).
- **Wang 2017 rat oral absolute bioavailability:** Animal Model.
- **Kang 2021 gut-luminal concentration calculation:** Mechanistic Extrapolation (calculation from oral dose + intestinal volume assumptions).
- **Fischer 1981 C4b2a half-life:** In Vitro.
- **Medof 1984 DAF effective threshold:** In Vitro.

## Cross-references

- [comp-018 upstream complement modulator sweep](./upstream-complement-modulator-sweep-computational.md) (the dietary thread origin)
- [comp-020 upstream complement verification re-run](./upstream-complement-verification-rerun-computational.md) (where the 44× assay-format IC50 spread is documented)
- [comp-012 DAF SCR1-4 truncated construct](./daf-cd55-scr14-truncated-computational.md) (the engineered surface-decay thread origin; the wet-lab MSU-surface engagement unknown)
- [comp-030 DAF cassette ranking](./daf-cd55-scr14-cassette-ranking-computational.md) (cassette-design refinement)
- [chaperone-orthogonal-stacking.md §3.5.3](./chaperone-orthogonal-stacking.md) (DAF effective PDI load)
- [H05 DAF SCR1-4 CP0 thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md) (the formal hypothesis card)
- [`validation-experiments.md` §1.25](./validation-experiments.md) (the gating wet-lab experiment)
- [complement-c5a-gout.md §9.7](./complement-c5a-gout.md) (originating section, 2026-05-15)
