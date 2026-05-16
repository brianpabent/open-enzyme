# comp-029 — Combined CP0 Systems Model Summary

## Overall verdict: **YELLOW**

| Accessibility prior | DAF α | RA alone median | DAF alone median | Combined median | Combined/better-singleton ratio | Verdict |
|---|---|---|---|---|---|---|
| Low | 0.05 | 0.886 | 0.568 | 0.956 | 1.08 | YELLOW |
| Medium | 0.20 | 0.886 | 0.815 | 0.979 | 1.10 | YELLOW |
| High | 0.80 | 0.886 | 0.914 | 0.989 | 1.08 | YELLOW |

## Headline findings

1. **Both arms individually saturate** at their operative concentrations, so multiplicative composition has no room to grow. RA gut-luminal hits a median 0.886 inhibition (at 50-1100 μM exposure post-200 mg oral). DAF SCR1-4 hits median 0.57-0.91 across the three accessibility priors. When each arm already produces 60-90% reduction, the combined ratio against the better singleton is mathematically capped near 1.1×.

2. **The 95% CIs do NOT separate** at any accessibility prior. The wide singleton CIs (RA p5=0.44 to p95=0.99; DAF p5=0.18-0.77) overlap the combined CIs. The combined effect is **probably** larger than either alone, but not provably-large-enough under current prior uncertainty to clear the GREEN threshold.

3. **No interaction blocker found.** RA's covalent mechanism targets C3b nucleophilic acceptor sites; it does not target SCR/CCP-domain proteins like DAF. DAF SCR1-4 is comp-012-LOW-protease-risk under gut-luminal conditions where RA is bioavailable. The two mechanisms are mechanistically complementary, not competitive. The RED verdict path is closed.

4. **Dominant uncertainty drivers (sensitivity Spearman r, α=0.20):**
   - RA gut-luminal IC50 vs combined: r = -0.658 (largest single driver)
   - RA gut-luminal [RA] vs combined: r = +0.552
   - DAF effective [DAF] vs combined: r = +0.480
   The TWO biggest knobs are RA IC50 (currently 36× spread, 5-180 μM) and gut-luminal RA exposure (22× spread, 50-1100 μM).

5. **The fluid-phase systemic free-RA regime contributes essentially 0% inhibition.** Baba 2004 free plasma Cmax of 20 nM is ~1700× below the central IC50 (34 μM). RA's CP0 leverage comes from the **gut-luminal transient** during digestion, not from steady-state systemic exposure. This sharpens the wet-lab framing: a gut-luminal complement-activation assay (not a plasma-based one) is the right readout for the RA arm.

## Decision

Per the comp-029 brief decision rule:
- GREEN if combined-effect range meaningfully larger than either alone (median ≥ 1.5× better singleton AND 95% CI separation)
- YELLOW if combined CI overlaps either alone
- RED if interaction blocker

**Verdict: YELLOW** at all three accessibility priors. The combined median is only 1.10× the better singleton — well below the 1.5× GREEN threshold — AND the combined 95% CI overlaps both singleton 95% CIs. The honest read: both arms are saturated enough individually that the multiplicative-composition gain is structurally capped, and the underlying prior uncertainty is wide enough that the small gain is not statistically separable from the singleton CIs.

## Wet-lab handoff

The cheapest path to upgrading this verdict from YELLOW to GREEN (or to RED) is:

**Measure DAF SCR1-4 MSU-surface engagement fraction** in a cell-free MSU-crystal + complement assay (zymosan-validated format, e.g., the Wessig 2022 PMC8924570 setup adapted to DAF supplementation). One experiment, one parameter, currently a 4-160× prior spread. Recommend pulling forward the [validation-experiments.md §1.25](../../../validation-experiments.md) wet-lab gate; the §1.25 functional readout (zymosan or MSU C5a-generation assay ± DAF) directly resolves α.

If §1.25 returns α ≥ 0.5 (mid-to-high range), comp-029 re-runs to GREEN and the rosmarinic-acid co-treatment arm is justified at marginal cost. If §1.25 returns α < 0.2, comp-029 stays YELLOW and the combined-strategy thesis is parked.

If GREEN is achieved on §1.25 outcome, the recommended addition to §1.25 (in the existing DAF SCR1-4 expression screen) is:

> Add a third co-treatment arm to the §1.25 zymosan / MSU-crystal C5a-generation assay: DAF SCR1-4 expressed material (mature, ELISA-quantified) + rosmarinic acid (final concentration 100 μM, matching the median Sahu 1999 C3b-deposition IC50 region) co-incubated 30 min at 37°C with the complement-competent serum + MSU substrate. Compare C5a (and C5b-9) generation against (i) DAF SCR1-4 alone, (ii) RA alone, (iii) vehicle. The marginal cost is one additional condition per plate; the wet-lab read-out is the same ELISA.
