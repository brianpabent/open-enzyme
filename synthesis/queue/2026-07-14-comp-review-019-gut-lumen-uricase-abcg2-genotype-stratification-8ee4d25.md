---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-019
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-019

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-019-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-019-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-019

## Bottom-line verdict

**Quantitative verdict invalid.** comp-019’s Phase A negative finding remains useful: the artifact did not identify any Q141K-stratified uricase clinical outcome trial. But the Phase B flux model does **not** establish the reported ΔSUA magnitudes, flat dose-response, substrate-limited regime, genotype response ranking, or “yield no longer matters” engineering conclusion.

The implementation assumes the decisive result: once enzyme capacity exceeds a daily-flux denominator, uricase is treated as extracting a fixed 40% of genotype-scaled intestinal flux. The stored physiological substrate concentration, uricase Km, ABCG2 Km/Vmax, finite residence time, oxygen, access/localization, survival, peroxide, and product constraints are not used to determine whether that extraction can actually occur.

## Implementation and constraint closure

I traced `inputs/flux_model_parameters.json` into `scripts/flux_model.py` and committed outputs. The outputs are plausible products of the code, but the code answers a much narrower and more assumption-driven question than the README/wiki claims.

Key implementation findings:

- **Luminal urate concentration is stored but not used.** The model records Miyazaki 2025’s ~0.59 µM jejunal urate baseline, but capacity is computed from label Vmax-like activity and compared to daily intestinal flux without Michaelis–Menten substrate occupancy.
- **Uricase Km is stored but not used.** `Km_uricase_uM` is never used in the capacity calculation, so the model treats all delivered enzyme as operating at its specific-activity assay rate after only a fixed 0.75 pH/activity factor.
- **Finite active window is absent.** The capacity calculation effectively grants activity over 1,440 min/day. No 2–4 h small-intestinal window, colonic residence, enzyme decay, or local replenishment term is implemented.
- **ABCG2 kinetics are stored but not used.** Km/Vmax are documentation-only in this model. They do not set transporter flux or genotype-specific flux.
- **Miyazaki empirical ratios are not implemented as claimed.** The README/wiki says median Miyazaki ratios are propagated, but the code hard-codes `functional_class` values of 1.00 / 0.75 / 0.50 / 0.25. The empirical 100%:75% and 100%:50% secretion ratios are not sampled or used.
- **Sink amplification is a hard-coded assumption.** `sink_amplification_factor = 0.40` is not an input and is not varied in Monte Carlo, despite being one of the dominant determinants of ΔSUA.
- **Dose flatness is structurally forced.** At all tested doses, the model’s capacity ratio is above 1 by construction, so `delta_intestinal = 0.40 * delivered_intestinal_flux`. Once above the arbitrary boundary, dose cannot affect ΔSUA.
- **Genotype ordering is mostly baked in.** ΔSUA is proportional to `functional_class × baseline_SUA × gut_fraction × (1 - renal_compensation) × 0.40`. The WT-largest conclusion follows from the chosen functional classes and baseline SUA values, not from an independent transporter/enzyme system simulation.
- **Serum mapping is a first-order shortcut, not a physiological pool model.** `delta_SUA = -SUA_baseline * net_delta_flux / total_daily_production`. The extracellular urate pool size is stored but unused; no equilibration kinetics or time-to-steady-state derivation is implemented.
- **Monte Carlo omits dominant uncertainties.** It varies production, intestinal fraction, and renal compensation only. It does not vary luminal urate, uricase Km, pH, oxygen, enzyme survival, residence time, access/localization, sink amplification, genotype-function uncertainty, Miyazaki small-n ratios, baseline SUA, or reabsorption fraction.

Constraint closure:

- **Reaction closure:** Uricase reaction requires urate + O₂ + H₂O and produces allantoin/5-HIU-derived products plus H₂O₂/CO₂. The model tracks only urate mass; it does not track oxygen limitation, allantoin/product formation, peroxide burden, or antioxidant loss.
- **Operating regime:** The model asserts substrate-limited excess enzyme capacity but does not apply substrate occupancy using `[urate] / (Km + [urate])`. That is the central physical failure.
- **Mass balance:** The model uses total daily production and an intestinal fraction but does not dynamically conserve local luminal urate, reabsorption, renal compensation, transporter delivery, or serum pool equilibration.
- **Localization/access:** No topology, cell-associated vs secreted enzyme, epithelial access, diffusion, mucus layer, food matrix, or transit model is implemented.
- **Safety/off-targets:** Peroxide and local oxidative burden are absent; coproducts and local peaks are absent.
- **Sensitivity:** The sensitivity range covers convenient high-level mass-balance variables, not the dominant physical uncertainties.

## Summary-fidelity audit

The current top-level corpus has mostly reconciled comp-019 by superseding it with comp-044/045, but the comp-019 artifact itself remains internally inconsistent and overclaims relative to its code.

- **README.md:** Overstates the result as complete and actionable. Claims non-Q141K males show largest predicted ΔSUA, dose is flat, mechanism is substrate-limited, and primary demographic should not be narrowed. These are not supported by the implementation once substrate occupancy and finite residence are considered.
- **outputs/flux_model_summary.md:** Faithfully reports the code outputs, but the interpretation is too strong. It presents “mechanism works across genotypes” and “target demographic should not be narrowed” as if model-resolved.
- **wiki-archive.md:** Contains the same retired conclusions plus downstream recommendations: single-dose Phase 2b, yield deprioritization, Caco-2 gate not triggered, cross-validation upgrade. These are now invalid.
- **Current interpretive page `wiki/uricase-abcg2-genotype-stratification-computational.md`:** Already correctly marks comp-019 as superseded by comp-044 and retires ΔSUA, genotype magnitudes, capacity ratios, flat-dose, and yield-priority recommendations.
- **`wiki/computational-experiments.md`:** Already marks comp-019 as superseded and preserves only the literature-scan result.
- **`wiki/validation-experiments.md`:** Already reflects comp-044/045 by making §1.33 the Gate 0 UOX topology/oxygen/peroxide experiment and preventing §1.9B UOX commitment before topology selection.
- **`wiki/H08-gut-lumen-sink-platform-thesis.md`:** Already correctly retracts comp-019’s numeric prior and reopens the hypothesis.
- **`wiki/gut-lumen-sink.md`:** Already carries a quantitative reset and patient-stratification reset.
- **`wiki/open-questions.md`:** Already reopens genotype stratification and core H08 questions.
- **`wiki/abcg2-modulators.md`:** Already corrects butyrate/Q141K attribution and notes comp-019/comp-031 reset.
- **`wiki/cross-validation.md`:** Mostly reconciled in Claim 1, but one later summary table still lists “Gut-lumen mechanism” as 6/10 while the Claim 1 text says 5.5/10 after comp-044. That stale rating should be harmonized.
- **`wiki/uricase.md`:** Mostly reconciled on the gut-lumen insight, but its older H₂O₂ passage still says expected gut-lumen H₂O₂ would be “not a safety concern.” Given comp-019 omitted peroxide and current §1.36 exists specifically to test this risk, that wording should be softened.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Total urate production 700 mg/day, 600–900 range | `inputs/flux_model_parameters.json`; `flux_model.py` MC | Used directly in mass-balance denominator and MC | Citation string / “standard physiology”; primary sources not included | Usable as rough prior, not independently verified here |
| Intestinal excretion fraction 0.33, range 0.30–0.40 | `inputs/flux_model_parameters.json`; `flux_model.py` MC | Used directly for baseline intestinal flux | Citation string to Takada/reviews/tracers; primary sources not included | Load-bearing and only secondary-verified in artifact |
| Renal compensation 0.30, range 0–0.50 | `inputs/flux_model_parameters.json`; `flux_model.py` MC | Used directly as offset to gut delta | Explicitly mechanistic extrapolation | Major uncertainty; not empirically closed |
| Sink amplification factor 0.40 | Hard-coded in `flux_model.py` | Directly determines ΔSUA magnitude | Cited in comments to review-tier reabsorption estimate; not input-controlled | Major hidden load-bearing assumption; not sensitivity-tested |
| Uricase specific activity 8.3 U/mg with 0.75 in-vivo factor | `inputs/flux_model_parameters.json`; `flux_model.py` | Used for capacity ratio | Regulatory/label-tier citation string; source not included | Used, but applied as if substrate-saturating |
| Uricase Km ~25 µM | `inputs/flux_model_parameters.json` | **Not used** | Label/regulatory-tier citation string | Stored-but-unused; invalidates capacity-regime claim |
| Luminal urate ~0.59 µM | `inputs/flux_model_parameters.json`; `phase_a_literature.json` | **Not used** | Claimed full-text grep-verified from Miyazaki; primary text not included | Stored-but-unused; central physical constraint omitted |
| ABCG2 Km 8.24 mM, Vmax 6.96 nmol/min/mg | `inputs/flux_model_parameters.json`; `phase_a_literature.json` | **Not used** | Abstract-tier citation strings | Cannot support implemented flux; documentation-only |
| Miyazaki functional-class secretion ratios | `inputs/flux_model_parameters.json`; `phase_a_literature.json` | **Not used as ratios**; code hard-codes 1/0.75/0.5/0.25 | Claimed full-text verified; primary text not included | Summary says propagated, implementation does not |
| Genotype functional classes 1.00/0.75/0.50/0.25 | Hard-coded in `flux_model.py`; also in inputs | Directly controls ranking | Matsuo/Miyazaki framework, mostly abstract/citation-tier in artifact | Used, but uncertainty not sampled |
| Baseline SUA by genotype/sex | Hard-coded in `flux_model.py`; partial reference values in inputs | Directly controls absolute ΔSUA and ranking | No primary source named for genotype-specific baselines | Load-bearing but weakly sourced |
| Extracellular urate pool 1200 mg | `inputs/flux_model_parameters.json` | **Not used** | Standard physiology citation string | Stored-but-unused; no time-course closure |
| Capacity ratios 32×–1300× | `outputs/flux_model_results.json`; summary/wiki | Derived from Vmax-like capacity / daily flux | Reproducible from code | Physically invalid regime diagnostic because substrate occupancy and active window omitted |
| ΔSUA −0.5 to −0.83 mg/dL band | outputs/README/wiki-archive | Derived from simplified mass-balance formula | Reproducible from code | Quantitative verdict invalid |
| “No Q141K-stratified uricase trials found” | `phase_a_literature.json`; `phase_a_table.md` | Not used in code; Phase A conclusion | Search strategy documented; primary search not reproducible from committed raw query outputs | Useful negative finding, but not fully audit-reproducible |

## Affected wiki pages

- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — clearly supersedes comp-019 and retires quantitative claims.
- `wiki/computational-experiments.md` — already consistent — comp-019 marked SUPERSEDED; comp-044/045 named as replacements.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — numeric prior retracted and assumption stack rebuilt.
- `wiki/gut-lumen-sink.md` — already consistent — quantitative and patient-stratification resets are present.
- `wiki/open-questions.md` — already consistent — genotype stratification and H08 are reopened.
- `wiki/abcg2-modulators.md` — already consistent — comp-019/031 quantitative resets and butyrate/Q141K caveats propagated.
- `wiki/gout-multihop-research-program.md` — already consistent — lists old oral-UOX regime as invalid and points to comp-044/045/046.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — invalidates comp-031 partly because it inherited comp-019.
- `wiki/validation-experiments.md` — already consistent — §1.33/§1.36 now gate physiological UOX topology, oxygen, peroxide, and safety.
- `wiki/cross-validation.md` — change required — Claim 1 text is reset to 5.5/10, but a later summary table still lists the gut-lumen mechanism as 6/10; harmonize the rating and de-risking language.
- `wiki/uricase.md` — change required — older H₂O₂ language says expected gut-lumen peroxide is “not a safety concern”; should be softened to “unresolved; §1.36/§1.33 gate peroxide and redox safety.”
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` — change required — should carry a prominent superseded/invalid quantitative banner or link to comp-044.
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_summary.md` — change required — should be labeled historical output only; not an active interpretation.
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md` — change required — if retained as archive, add a top supersession note so readers do not treat its recommendations as live.

## New connections or implications

- The most durable comp-019 contribution is not the ΔSUA model; it is the **negative clinical-literature gap**: uricase trials did not report Q141K response stratification. That remains a useful design requirement for future studies.
- Miyazaki 2025’s sub-micromolar luminal urate datum cuts both ways: it supports that ABCG2 is operating far below its own Km, but it also makes UOX substrate occupancy and local replenishment central. The short summary kept the first implication and missed the second.
- The genotype question cannot be answered independently of topology/physiology. A Q141K responder-ordering model is downstream of measured local UOX product formation under physiologic urate, oxygen, residence, peroxide, and access constraints.
- The comp-019 failure explains why comp-031’s later UOX+PDB additivity model had to be invalidated: it inherited the same fully depleted luminal-pool assumption.
- Trial-design advice should shift from “single 25 mg/day dose; Q141K as secondary” to “measure topology/dose regime first; record Q141K as a prospective stratification variable once a physiologic UOX system exists.”

## Required actions

1. **Add supersession banners to comp-019 artifact surfaces.** Owner surface: `README.md`, `outputs/flux_model_summary.md`, and `wiki-archive.md` inside the comp-019 folder. Verification criterion: a reader opening any comp-019 artifact sees that ΔSUA, capacity ratios, genotype ranking, flat-dose, and yield recommendations are retired by comp-044.
2. **Harmonize remaining wiki rating drift.** Owner surface: `wiki/cross-validation.md`. Verification criterion: all gut-lumen mechanism ratings and summary tables match the post-comp-044 5.5/10 reopened framing.
3. **Soften residual peroxide closure wording.** Owner surface: `wiki/uricase.md` and any related route pages. Verification criterion: gut-lumen H₂O₂ is framed as a testable safety gate under §1.33/§1.36, not as already closed.
4. **Do not use comp-019 outputs for design decisions.** Owner surface: computational-experiment index, validation priorities, hypothesis cards, engineering pages. Verification criterion: no active page recommends dose, yield deprioritization, genotype ranking, or Phase 2b arm design from comp-019.
5. **If a replacement model is built, implement the missing physical terms.** Owner surface: future comp or dynamic model. Verification criterion: uses luminal urate, UOX Km, finite residence/exposure time, pH, oxygen, access/localization, enzyme survival, peroxide/product tracking, reabsorption, renal compensation, and measured/sampled genotype transporter supply.
6. **Primary-source verification remains needed for load-bearing literature numbers.** Owner surface: Phase A provenance. Verification criterion: committed line-anchored primary-source extracts or explicit “citation-tier only” labels for Miyazaki, Matsuo, Nakayama, Takada, ALLN-346, PRX-115, and allele-frequency values.
7. **Fix reproduction path documentation.** Owner surface: comp-019 `README.md`. Verification criterion: command uses the actual repo path `wiki/etc/experiments/...` or clearly states the working-directory convention.

## Review limits

- I did not execute `scripts/flux_model.py`; reproducibility was assessed by static inspection of code, inputs, and committed outputs.
- Repository fixed-string search failed because the environment lacked `rg`; affected-page discovery relied on the supplied bundle plus direct reads of key omitted pages until tool-result budget was exhausted.
- Primary literature was not available in the artifact, so I did not independently verify the cited Miyazaki, Matsuo, Nakayama, Takada, ALLN-346, PRX-115, rasburicase, or allele-frequency values against original sources.
- `wiki/engineered-yeast-uricase-proposal.md` was only partially inspected before the tool budget ended; it may contain additional stale “mechanism validated” or dosing language requiring the same comp-044 reset.
- This review is Phase 0 research scrutiny only and does not convert computational outputs into clinical evidence.
