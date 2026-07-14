---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-031
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-031

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-031-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-031-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-031

## Bottom-line verdict

Quantitative verdict invalid; comp-031 is a toy composition of hard-coded prior effect sizes, arbitrary competition/rescue factors, and unsupported CBT2.0→butyrate/Q141K assumptions. It does not resolve the stated physical question of whether EcN PDB + luminal UOX are additive under physiological substrate, oxygen, transit, localization, carbon-fate, and safety constraints.

The current interpretive wiki page correctly marks comp-031 invalidated, but stale stronger wording remains in at least `wiki/computational-experiments.md` planned-table text, `wiki/chassis-pending-interventions.md` M1, and `wiki/purine-degrading-bacteria.md` Tier 3 wording.

## Implementation and constraint closure

What I traced:

- `analyze.py` loads `inputs/model_parameters.json`, but most mechanistic inputs are not actually used in the computations that produce the headline:
  - `luminal_urate_concentration_uM` is sampled into `scenario["colonic_urate_uM"]` but never used.
  - UOX `Km`, `kcat`, `specific_activity`, `effective_activity`, substrate occupancy, active window, oxygen, and localization are not used in the UOX arm.
  - PDB `DOPDH_kcat`, `DOPDH_Km`, selenium/sulfur variant kinetics, and all reaction intermediates are not used in the PDB arm.
  - `daily_mass_balance` and renal/intestinal fractions are mostly replaced by hard-coded constants (`233.0`, `0.33`, `0.30`).
  - JSON parameters for butyrate background, Basseville EC50/Hill coefficient, and crypt attenuation are hard-coded in code rather than read from JSON.
- The `michaelis_menten_rate()` helper is defined but never used. The model therefore does not implement Michaelis–Menten competition, despite README/summary framing.
- UOX-alone effect is inherited as hard-coded comp-019 point estimates:
  - WT anchor `-0.83 mg/dL @ 8.0 baseline`.
  - Scaled by genotype relative function and baseline SUA.
  - Dose scaling is `sqrt(dose/25)` capped at 1.0.
  - This inherits the now-invalid comp-019 saturation regime and ignores comp-044’s substrate-occupancy/time-window correction.
- PDB-alone effect is not a kinetic or mass-balance calculation. It maps the CBT2.0 mouse fractional reduction to human ΔSUA through:
  - arbitrary mouse-to-human attenuation;
  - a fixed `0.70` renal-compensation multiplier;
  - a cap at 25% baseline SUA;
  - arbitrary log-density factor;
  - arbitrary genotype supply factor `0.5 + 0.5 * genotype_relative_function`.
- Competition is not physically closed:
  - `pdb_capacity_ratio = 30.0 * density/1e10` is not derived from enzyme expression, CFU, kcat, Km, volume, or substrate flux.
  - `substrate_competition_factor()` returns `1/sqrt(total_capacity)` in high-capacity cases, then this is used as a residual-capture fraction for the minor arm, not as a Michaelis–Menten partition.
  - The summary says residual capture is “~10%” and comments mention “10–30%”; this is just a constructed factor, not a derived consequence.
  - Because comp-044 invalidated the assumed UOX saturation regime, the competition premise is not established.
- Butyrate/Q141K synergy is not closed:
  - CBT2.0 carbon fate to butyrate is assumed from full-pathway anaerobes / *C. sporogenes* logic, not measured for engineered EcN.
  - `pdb_urate_consumed_mg` is back-calculated from predicted ΔSUA, not from urate disappearance or carbon isotope mass balance.
  - The concentration calculation uses an order-of-magnitude residence/volume simplification and then adds fixed background butyrate.
  - Central scenario PDB-derived crypt butyrate is only about `0.0437 mM`; total crypt butyrate is `0.8437 mM` because `0.8 mM` background is added. Most modeled Q141K rescue is therefore driven by unmatched background, not PDB output.
  - Basseville 2012 is misused as if it established direct 1–5 mM butyrate rescue in this system; current wiki corrections note it did not.
- Safety/constraint gaps:
  - No oxygen dependence for UOX.
  - No H₂O₂ production or catalase/peroxide closure.
  - No DOPDH anaerobic localization or UOX/PDB spatial segregation.
  - No urate replenishment, diffusion, radial/longitudinal gut niches, or residence-time dynamics.
  - No selenium/molybdenum cofactor sufficiency.
  - No ammonia, yanthine/intermediate, lactate, acetate, D-lactate, pH, redox, viability, or GMM-stability burden.
  - No live-biotherapeutic containment, strain compatibility, or payload stability analysis.
- Sensitivity ranges miss dominant uncertainties:
  - They vary density, mouse-to-human attenuation, butyrate yield, and crypt attenuation.
  - They do not vary the now-dominant UOX physiological regime variables from comp-044/045: substrate occupancy, active exposure time, oxygen, access, survival, topology, catalase/peroxide handling.
  - They do not include CBT2.0 carbon-fate uncertainty as a discrete “no butyrate” case.

Reproducibility contract:

- Code is stdlib-only and deterministic by seeded RNG, and committed outputs are plausibly generated by this code.
- README command path is likely wrong for the repository layout: it says `cd experiments/comp-031...`, while the tracked path is `wiki/etc/experiments/comp-031...`.
- I did not execute code. A deterministic reproduction would require running `python3 analyze.py` from the actual `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/` directory and diffing `outputs/results.json` and `outputs/summary.md`.

## Summary-fidelity audit

Artifact README and `outputs/summary.md` are internally consistent with `results.json`, but the artifact’s own interpretation is no longer scientifically valid.

Major mismatches/overstatements:

- README and output summary still state:
  - “Verdict: YELLOW (provisional)”
  - combined ΔSUA `−1.8 to −1.9 mg/dL`
  - “meaningfully better than either single arm”
  - separate-strain engineering handoff
  - PDB-derived butyrate as an independent ABCG2/Q141K axis
- Current `wiki/dual-chassis-ecn-pdb-uricase-computational.md` correctly invalidates these claims.
- Current `wiki/computational-experiments.md` main comp-031 entry correctly says **INVALIDATED**, but its lower “Planned Analyses” row still contains stale text: “Completed 2026-05-16 — YELLOW; combined ΔSUA −1.8 to −1.9 mg/dL; separate-strain handoff.”
- `wiki/chassis-pending-interventions.md` has corrected top-level PDB caution language, but its M1 “Cheapest first move” section still describes comp-031 as “YELLOW provisional” and repeats the separate-strain handoff as if active.
- `wiki/purine-degrading-bacteria.md` is mostly reconciled with the invalidation, but the Tier 3 intervention-ranking row still says “Dual-mechanism EcN (PULSE uricase + PDB pathway): optimal combination, highest complexity,” which is stronger than comp-044/046/031-invalidated evidence supports.
- `wiki/validation-experiments.md` sections §1.33, §1.34, §1.37, and §1.14 are already consistent with the corrected gating logic.
- `wiki/gut-lumen-sink.md`, `wiki/abcg2-modulators.md`, `wiki/disulfiram.md`, and `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` appear materially reconciled with the invalidation.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| UOX-alone WT ΔSUA `−0.83 mg/dL` at 25 mg/day | `analyze.py` `uricase_arm_dSUA()` | Direct hard-coded anchor | Inherited from comp-019; comp-044 now invalidates quantitative regime | Invalid load-bearing prior |
| UOX flat dose above ~5 mg/day | `analyze.py` comments and dose scaling | Encoded via capped sqrt scaling, with 25 mg/day fixed in MC | Inherited from comp-019; superseded by comp-044 | Invalid |
| UOX substrate-limited capacity ratios 32–1300× | README, summary, JSON `compositional_check_interaction`, code comments | Basis for competition model | Inherited from comp-019; comp-044 rejects legacy saturation regime | Invalid |
| Luminal urate 50–500 µM sensitivity | `model_parameters.json`; MC samples `colonic_urate_uM` | Sampled but unused | Corpus/brief + Miyazaki fasted floor cited | Stored but non-operative |
| UOX Km 25 µM | JSON `uricase_kinetic_priors` | Not used | Cited as rasburicase-label / comp-019 prior; not primary-verified here | Stored but non-operative |
| UOX kcat/specific activity | JSON `uricase_kinetic_priors` | Not used | Citation strings only in artifact | Stored but non-operative |
| CBT2.0 mouse plasma UA `463 → 172 µM`, `−63%` | JSON `cbt20_anchor_in_vivo`; code `fractional_reduction` | Direct PDB-effect anchor | Artifact says corpus-tier; not full-text verified in artifact | Usable only as animal-model anchor, not human ΔSUA |
| Mouse-to-human attenuation `0.3–0.7`, central `0.5` | JSON and MC | Direct multiplier | Heuristic/modeling choice; no named primary source | Unresolved, arbitrary |
| Renal compensation `30%` | JSON and code hard-coded `(1-0.30)` | Direct multiplier in PDB arm | Inherited from comp-019; no dynamic renal model | Weak / not validated |
| PDB density `1e9–1e11 CFU/g` | JSON and MC | Arbitrary log-density efficacy factor | “Brian’s brief / standard LBP” note; no primary verification | Sensitivity-only, not mechanistic |
| DOPDH kcat `412/s` and Km estimate | JSON `pdb_pathway_kinetics` | Not used in PDB efficacy or competition | Corpus-tier citation; Km explicitly extrapolated | Stored but non-operative |
| PDB capacity ratio `30×` at `1e10 CFU/g` | Code `pdb_capacity_ratio` | Direct competition factor input | No derivation from expression, enzyme amount, kcat/Km, volume, or substrate | Unsupported |
| Butyrate yield `0.3–0.7 mol/mol urate`, central `0.5` | JSON and MC | Direct crypt/luminal butyrate calculation | Mechanistic extrapolation from *C. sporogenes*/pathway; CBT2.0 not verified | Invalid for CBT2.0 unless measured |
| Background crypt butyrate `0.8 mM` | Hard-coded in `predict_dual_chassis_dSUA()` | Added to combination butyrate before Q141K rescue | Not read from JSON; unmatched comparator | Invalidates rescue attribution |
| Basseville EC50 `1 mM`, Hill `2` | Hard-coded | Drives Q141K rescue fraction | Artifact attributes butyrate rescue; current corpus says Basseville did not test direct butyrate in this system | Misattributed / unresolved |
| Q141K genotype functions WT 1.0, het 0.75, hom 0.5 | JSON and genotype scenarios | Direct UOX and PDB scaling | Inherited from comp-019; no active response model after comp-044 | Not sufficient for ΔSUA ranking |
| PPARγ bump `10% per mM`, cap `30%`, SUA sensitivity `0.05` | `abcg2_induction_dSUA_bump()` | Direct additive WT-allele ΔSUA bump | No explicit source in artifact | Unsupported |
| Combined ΔSUA `−1.8 to −1.9 mg/dL` | README, output summary, `results.json` | Headline output | Emerges from invalid hard-coded composition | Invalid quantitative verdict |
| Separate-strain engineering recommendation | README and output summary | Interpretive handoff | Based on invalid competition model | Retired as computational recommendation |

## Affected wiki pages

- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — explicitly invalidates comp-031 and retires ΔSUA, competition, butyrate, Q141K-rescue, and engineering recommendations.
- `wiki/computational-experiments.md` — change required — main comp-031 entry is consistent, but the lower “Planned Analyses” row still repeats stale YELLOW/ΔSUA/separate-strain wording.
- `wiki/validation-experiments.md` — already consistent — §1.33, §1.34, §1.37, and §1.14 implement the replacement gates.
- `wiki/chassis-pending-interventions.md` — change required — PDB entry is mostly corrected, but M1 still repeats the stale comp-031 YELLOW and separate-strain handoff under “Cheapest first move.”
- `wiki/purine-degrading-bacteria.md` — change required — mostly corrected, but Tier 3 still frames “dual-mechanism EcN (PULSE uricase + PDB pathway)” as “optimal combination,” which is unsupported after comp-031 invalidation and comp-044/046.
- `wiki/gut-lumen-sink.md` — already consistent — quantitative reset and comp-044/H08 references retire comp-019-style numerical priors.
- `wiki/abcg2-modulators.md` — already consistent — correctly separates PPARγ induction from Q141K rescue and notes Basseville/butyrate attribution caveat.
- `wiki/disulfiram.md` — already consistent — companion-PDB paragraph warns that comp-031 is retired.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — reopens gut-lumen UOX thesis without numeric ΔSUA prior.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — not inspected due tool-result budget; likely relevant because comp-031 inherits comp-019, and should remain marked superseded by comp-044.

## New connections or implications

- The Q141K “rescue” signal in comp-031 is largely a background-butyrate artifact, not a PDB-output result. This strengthens the need for validation §1.14 to test butyrate exposure directly and for comparators to include matched background fiber/butyrate.
- The invalid competition result should not be replaced by a naive “UOX and PDB are additive” claim. Comp-046 shows the correct next framing: spatial staging can help or hurt depending on overlap, residual transfer, and viability.
- CBT2.0 carbon fate is now the key branching point. If engineered EcN produces lactate/succinate/ethanol rather than butyrate from urate-derived pyruvate, the ABCG2/Q141K synergy disappears and safety/product-fate questions change.
- “Separate strains” may still be operationally attractive for manufacturing, containment, and regulatory modularity, but comp-031 provides no valid evidence that separate strains outperform dual-cassette EcN on efficacy.
- The UOX/PDB combination cannot be prioritized until UOX topology/oxygen/peroxide feasibility (§1.33) and PDB carbon fate (§1.37) are measured. The two uncertainties are independent and multiplicative.

## Required actions

1. Update `wiki/computational-experiments.md` planned-analysis row for `~~comp-031~~` to remove stale “YELLOW; combined ΔSUA −1.8 to −1.9 mg/dL; separate-strain handoff” wording. Verification: no active occurrence of comp-031 YELLOW/ΔSUA/separate-strain handoff remains outside explicit historical/frozen-artifact context.
2. Update `wiki/chassis-pending-interventions.md` M1 “Cheapest first move” section to replace the stale comp-031 YELLOW/separate-strain paragraph with the invalidated/replacement-gate framing already used elsewhere on the page. Verification: M1 points to comp-044/046 and validation §1.37/§1.43 as gates, not comp-031 as an efficacy prior.
3. Update `wiki/purine-degrading-bacteria.md` Tier 3 ranking to soften or remove “Dual-mechanism EcN … optimal combination.” Verification: wording says UOX+PDB combination topology is open and gated by comp-044/045/046 plus validation §1.33/§1.37, not optimal by comp-031.
4. Add an invalidation banner or note to the frozen artifact README and/or `outputs/summary.md`, or ensure all links to those files are clearly framed as frozen invalidated provenance. Verification: a reader landing directly in the artifact folder cannot mistake the committed summary for an active prior.
5. If the computation is ever replaced rather than retired, rebuild from conserved dynamic ledgers: measured UOX local kinetics/time/oxygen/peroxide; isotope-resolved PDB carbon fate; explicit substrate pools; matched background butyrate; and no ΔSUA mapping without a justified serum-pool model.

## Review limits

- I did not execute `analyze.py`; reproducibility was assessed by code/output inspection only.
- Repository `grep_repo` failed because `rg` is unavailable in the environment, so affected-page discovery relied on supplied bundle pages plus targeted `read_file` of omitted pages.
- Tool result budget prevented full inspection of every potentially affected page, including the full `wiki/validation-experiments.md` and `wiki/uricase-abcg2-genotype-stratification-computational.md`.
- Primary papers were not independently opened or verified; provenance status is based on artifact citations and corpus pages inspected here.
- This is Phase 0 research review only and does not imply clinical efficacy, dosing, or medical advice.
