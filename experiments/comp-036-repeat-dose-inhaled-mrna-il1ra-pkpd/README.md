# comp-036: Repeat-dose inhaled mRNA-IL-1Ra PK/PD with receptor-occupancy framing

**Question:** Does multi-administration inhaled mRNA-IL-1Ra dosing achieve clinically-meaningful sustained IL-1R1 receptor occupancy over the 72h acute gout flare window — and how many doses, at what frequency, with what confidence bounds?

**Verdict: YELLOW.** Repeat dosing partially salvages the modality from comp-033's RED single-dose Cmax-equivalence verdict — but the high-confidence GREEN bar (median 95% of the 0-72h flare window above 80% receptor occupancy AND p25 confidence bound above 50%) is NOT reached by any of three dosing regimens tested (QD x1-14, BID x2-28, Loading 2x + QD-maintenance x0-14).

**The load-bearing result is the BID regimen reaching meaningful but sub-anakinra-grade occupancy at 2-4 days.** BID dosing (every 12h) at 4+ doses achieves median ~50% of the flare window above 80% occupancy with mean window occupancy ~73-74% — qualitatively superior to QD (which never sustains 80% occupancy at any dose count because troughs drop below threshold) or Loading+QD-Maintenance (which never exceeds ~32% of window above threshold). Anakinra steady-state achieves ~85-90% mean occupancy by comparison.

**The clinical implication for an operator-affected patient (Brian)**: repeat-dose inhaled mRNA-IL-1Ra is NOT a like-for-like replacement for anakinra at the receptor-occupancy level, but it IS a meaningfully better-than-nothing option that could displace prednisone for patients who can tolerate sub-anakinra occupancy in exchange for (a) no SC injections, (b) no glucocorticoid side-effect burden (glucose/BP/mood/sleep acute; bone/cataract/adrenal chronic), and (c) substantial cost edge vs canakinumab. The question is no longer "can inhaled mRNA-IL-1Ra match anakinra?" (answer: no, not at currently-feasible doses) but "is the partial-suppression × side-effect-profile-advantage trade-off worth it for the gout patient currently on prednisone?" (answer: plausibly yes, but needs wet-lab dose-finding to nail down).

**Three honest paths forward from YELLOW:**
1. **Wet-lab single-measurement that would tighten the verdict the most**: direct measurement of integrated translation-efficiency mass ratio (protein synthesized / mass of mRNA delivered) in human alveolar epithelium for inhaled m1Psi-mRNA-LNP. This is the #2 sensitivity driver in comp-036 (Spearman rho = +0.58 vs mean occupancy) and was the #1 driver in comp-033 single-dose (rho = +0.78). A ferret or NHP study with downstream protein quantification in BAL fluid would resolve this and tip the verdict toward GREEN or RED.
2. **Tighten the IL-1Ra-IL-1R1 Kd prior**. The 0.1-10 nM log-uniform prior is the #1 sensitivity driver in comp-036 (Spearman rho = -0.69). A modern SPR Kd measurement on recombinant IL-1Ra vs IL-1R1 ectodomain at physiological pH/salt would shrink this prior 10-100x.
3. **Pivot to intra-articular mRNA-IL-1Ra** (sister architecture to [comp-035 intra-articular uricase + catalase](../comp-035-ia-uricase-h2o2-reaction-diffusion/)). Local concentration at the affected joint bypasses systemic dilution that dominates the inhaled math.

**Informs:** [`wiki/chassis-pending-interventions.md` §4](../../wiki/chassis-pending-interventions.md) (the originating chassis-pending entry); [`wiki/inhaled-mrna-il1ra-pulse-computational.md`](../../wiki/inhaled-mrna-il1ra-pulse-computational.md) (comp-033 single-dose verdict); [`wiki/etc/open-enzyme-vision.md` §10](../../wiki/etc/open-enzyme-vision.md) (temporal-stack platform framing).

**Interpretive wiki page:** [`wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md`](../../wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md)

**Sister experiment (single-dose precursor):** [comp-033 inhaled mRNA-IL-1Ra pulse therapy](../comp-033-inhaled-mrna-il1ra-pulse-therapy/) — RED on Cmax-equivalence at single dose; comp-036 builds repeat-dose accumulation + receptor-occupancy framing on top.

---

## How to reproduce

```bash
cd experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd
python3 analyze.py
```

Stdlib-only Python 3 (no external packages). All inputs are committed in `inputs/`. Outputs are deterministic given RNG seed 36. Three RNGs (seeds 37, 38, 39) drive the QD, BID, and Loading-regimen scans respectively to keep sensitivity analyses independent.

---

## File index

```
comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/
  analyze.py                              ← analysis script (run this)
  README.md                               ← this file
  inputs/
    single_dose_pk_inherited.json         ← PK priors inherited from comp-033 (dose, translation eff, lung delivery, bioavail, expr duration, clearance, Vd)
    il1ra_receptor_binding.json           ← IL-1Ra-IL-1R1 Kd (0.1-10 nM log-uniform); competitive antagonism excess factor; anakinra steady-state occupancy reference; primary sources
    dosing_regimens.json                  ← QD / BID / Loading+QD-Maintenance schedules; flare window definition; clinical practicality bounds
    clinical_comparators.json             ← anakinra / canakinumab / prednisone per-flare and cumulative-over-years side-effect comparator data
    model_parameters.json                 ← Monte Carlo n, time grid, decision thresholds, regimen dose-count scans
    provenance.md                         ← Per CLAUDE.md Rule 4: source + verification status for every load-bearing claim
  outputs/
    dose_pkpd_prediction.json             ← Full Monte Carlo results: per-regimen scans, recommended regimens, sensitivity, threshold concentrations
    trajectory_data.json                  ← Median-parameter plasma + occupancy trajectories for plotting
    summary.md                            ← Human-readable result summary (auto-generated by analyze.py)
```

---

## Methodology — multi-dose superposition PK + receptor-occupancy model

### 1. Single-dose PK inheritance (Phase 1 sanity check)

The single-dose Monte Carlo reproduces comp-033's median single-dose Cmax (0.0256 ug/mL vs comp-033's 0.0251 ug/mL — matches within sampling noise) using the same priors:
- Dose: log-uniform [4, 24] mg per administration
- Translation efficiency mass ratio: log-uniform [1,000, 50,000] ng protein per ug mRNA
- Lung delivery: uniform [0.10, 0.40]
- Alveolar→systemic bioavail: uniform [0.10, 0.50]
- Expression duration: uniform [24, 96] hours
- IL-1Ra clearance: uniform [0.10, 0.25] /h (anakinra t1/2 4h)
- Vd: uniform [12, 25] L

PK model: zero-order input over expression duration, first-order elimination.

### 2. Multi-dose superposition

Multi-dose plasma concentration profile is the sum of single-dose profiles offset by dosing interval. Holds when expression machinery is not saturated — true at the 4-24 mg per-administration dose range per comp-033 sanity bounds. No LNP-induced tolerance, no anti-PEG buildup-driven clearance shift over the short (1-14 day) acute therapy window.

### 3. Receptor-occupancy framing (the load-bearing reframe)

comp-033 used plasma Cmax vs anakinra 1.5 ug/mL as the decision gate. comp-036 reframes to **receptor-occupancy fraction** because:

1. **IL-1Ra is a competitive antagonist** at IL-1R1 with Kd ~1 nM (Arend 1990 JCI [DOI 10.1172/JCI114622](https://doi.org/10.1172/JCI114622); Schreuder 1997 Nature [DOI 10.1038/386194a0](https://doi.org/10.1038/386194a0); Vigers 1997 Nature [DOI 10.1038/386190a0](https://doi.org/10.1038/386190a0)).
2. **Clinical efficacy is set by occupancy × time over flare window**, not Cmax-equivalence to anakinra.
3. **The brief speculated KD ~50-100 pM; this was incorrect.** Canonical Arend 1990 puts IL-1Ra at "affinity nearly equal to IL-1" — and IL-1 family Kd to IL-1R1 is in the **0.1-10 nM range**, not pM. The corrected log-uniform 0.1-10 nM prior is used throughout. (See `provenance.md` for the full correction note.)

Receptor occupancy = [IL-1Ra]_nM / ([IL-1Ra]_nM + Kd_nM). At Kd=1 nM, 80% occupancy requires [IL-1Ra] = 4 nM = ~70 ng/mL plasma.

### 4. Three dosing regimens

- **A. QD** (every 24h): doses at t = 0, 24, 48, 72, ... up to N doses
- **B. BID** (every 12h): doses at t = 0, 12, 24, 36, ... up to N doses
- **C. Loading + QD maintenance**: 2x dose at t=0, then 1x dose at t = 24, 48, ... up to (1 + N_maintenance) total doses

For each, the dose-count scan finds the smallest N that clears the GREEN bar (median 95% of 0-72h window above 80% occupancy AND p25 sustained-80%-window fraction >= 50%) or the YELLOW bar (median >= 50% of window above 80% occupancy).

### 5. Decision rule

- **GREEN**: at least one of the three regimens achieves GREEN-bar within 14-day, <=4-doses-per-day clinical-practicality envelope, with p25 confidence bound above 50%
- **YELLOW**: median 50%+ of window above 80% achievable but high-confidence GREEN bar not reached; modality viable but needs wet-lab dose-finding
- **RED**: even maximum-practical regimens (QD x14, BID x28, Loading + QD x14) cannot reach median 50% of window above 80% — drop the inhaled-systemic route, pivot to intra-articular mRNA-IL-1Ra or accept sub-anakinra exposure

### 6. Side-effect comparator framing

NOT a head-to-head side-effect study (would require real clinical data). Comparative framing across:
- **Inhaled mRNA-IL-1Ra repeat dose** (projected): cough during nebulization, mucosal irritation; cumulative anti-PEG / innate-immunity load is the load-bearing unknown
- **Anakinra 100 mg SC QD x5** (Saag 2021 Phase II RCT [DOI 10.1002/art.41699](https://doi.org/10.1002/art.41699)): injection-site reactions, modest infection risk; ADAs ~3-5%
- **Canakinumab 150 mg SC single** (FDA-approved gout 2023): injection-site (~5-10%), sustained immunosuppressive window of weeks; cost $18-23K/dose
- **Prednisone 30-40 mg taper x12-15d** (standard-of-care): acute glucose/BP/mood/sleep; cumulative bone/cataract/adrenal toxicity over 30-yr horizon

Per-flare and cumulative-over-years framing in `outputs/summary.md` and `outputs/dose_pkpd_prediction.json` "side_effect_comparator_table".

---

## Hard constraints honored

1. **CLAUDE.md Rule 4 pre-commit grep-verify gate.** Every load-bearing kinetic constant verified against primary source: IL-1Ra-IL-1R1 binding affinity (Arend 1990 JCI, Schreuder 1997 Nature, Vigers 1997 Nature — all retrieved via PubMed metadata 2026-05-16); anakinra clinical efficacy (Saag 2021 Arthritis Rheumatol Phase II RCT, retrieved via PubMed); anakinra PK (inherited from comp-033 provenance: Kineret USPI tier). See `provenance.md` for the full table with DOI links. The brief's speculated KD ~50-100 pM was caught at the pre-commit gate and corrected to 0.1-10 nM log-uniform prior with explicit primary-source citation.
2. **Receptor-occupancy is the clinical metric.** The shift from Cmax-vs-anakinra to receptor-occupancy-over-flare-window is the methodological load-bearing change in comp-036.
3. **Explicit confidence bounds throughout.** Monte Carlo n = 10,000 per regimen-and-dose-count combination (240,000 total iterations across the three regimen scans). Distribution reporting: median + 5th/25th/75th/95th percentiles. Sensitivity analysis via Spearman rank correlation against mean window occupancy.
4. **Inherited comp-033 uncertainty distributions.** Single-dose PK priors are re-used (verified via Phase 1 sanity check: median Cmax matches comp-033 within 2%). Added on top: IL-1Ra-IL-1R1 Kd prior, competitive-antagonism excess factor prior.
5. **Paperclip MCP** — only PubMed used for primary-source verification; `map` operator NOT used.
6. **Multilingual default** — CNKI and J-STAGE checked; no Chinese/Japanese inhaled-mRNA-IL-1Ra repeat-dose programs identified (documented in `provenance.md`).
7. **Tight wiki stub** — see `wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md` (≤60 lines).
8. **File restrictions honored** — only `experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/*` and `wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md` created. comp-033 read but not modified. `wiki/computational-experiments.md` NOT touched (orchestrator handles row add per brief).

---

## V1 simplifications (owned)

1. **Superposition principle** for multi-dose plasma profile. Strictly valid only when expression machinery is unsaturated (true at 4-24 mg) and PK is linear (true for IL-1Ra in the modeled range). The 14-day max-window also keeps anti-PEG / clearance-induction effects negligible per LNP repeat-dose literature.

2. **Receptor occupancy computed at instantaneous plasma free IL-1Ra concentration.** Assumes equilibrium binding on the seconds-to-minutes timescale (reasonable; IL-1Ra dissociation t1/2 is in the seconds range per SPR studies of similar nM-affinity ligands). Receptor turnover (internalization + resynthesis) on the hour timescale is not separately modeled.

3. **No tissue-specific occupancy distinction.** Plasma free IL-1Ra is assumed to equilibrate with IL-1R1 across circulating cells, synovial fibroblasts, endothelial cells at similar effective concentration. At the joint synovium during a flare, local IL-1Ra concentration may differ (vascular leak, inflammation-induced clearance changes) but this is beyond V1 scope.

4. **Single-compartment PK inherited from comp-033.** Two-compartment refinement would slightly change AUC distribution but not the verdict.

5. **No dose-response saturation in translation efficiency.** Reasonable at the 4-24 mg per-administration dose range; would need re-validation at >50 mg single-administration doses (which are not part of any practical regimen here).

6. **Anakinra comparator trajectory** is a simplified sawtooth approximation (ramp-up 0-6h to Cmax 1500 ng/mL, then exponential decay at t1/2 4h, repeated every 24h). Real anakinra PK has slightly different absorption phase but the difference is immaterial for the median-trajectory plot.

7. **Side-effect comparator framing is qualitative.** No head-to-head clinical study compares the four therapies at the side-effect level. The framing is the best synthesis from per-therapy literature. Per-patient choice between repeat-dose inhaled mRNA-IL-1Ra and prednisone taper would need real clinical data on the inhaled-route side; this is exactly the wet-lab measurement the YELLOW verdict requests.

---

## Disagreement protocol

If you reproduce the outputs and disagree with the methods or numbers, file a GitHub issue referencing this folder (`comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd`). Primary candidates for revision:

1. **IL-1Ra-IL-1R1 Kd prior** (0.1-10 nM log-uniform) — the #1 sensitivity driver. A direct modern SPR Kd measurement would tighten this prior 10-100x and shift the verdict toward GREEN (if Kd is in the 0.1-0.5 nM range) or further toward YELLOW/RED (if Kd is in the 3-10 nM range).
2. **Translation efficiency mass ratio prior** (1,000-50,000 ng/ug) — #2 driver; inherited from comp-033. Direct measurement in ferret/NHP inhaled-mRNA-LNP study with BAL protein quantification.
3. **Decision-rule bar at 80% receptor occupancy.** Anakinra clinical efficacy operates at ~85-90% mean occupancy; the comp-036 bar is intentionally at 80% (per brief) which is slightly below anakinra. A stricter 90% or 95% bar would push the verdict toward RED; a looser 70% bar (closer to anakinra's TROUGH occupancy of 74%) would push toward GREEN.
4. **Clinical practicality envelope** (14 days, 4 doses/day). For Brian's specific use case (operator-affected, currently on prednisone), a longer regimen may be acceptable in exchange for steroid avoidance — would push the practicality boundary out.
5. **Side-effect comparator framing** — qualitative; reasonable people may rank the per-flare and cumulative burdens differently. The framing tries to honestly enumerate what's known and what's a load-bearing unknown.
