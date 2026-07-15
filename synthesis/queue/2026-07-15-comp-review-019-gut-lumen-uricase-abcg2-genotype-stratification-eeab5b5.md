---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-019
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-019

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-019-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-019-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-019

## Reviewed snapshot
Independent API reviewer; daemon-mode review of commit `eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the supplied complete comp-019 tracked-file contents, the trigger diff, all supplied top-level wiki pages explicitly referencing comp-019, and additional omitted affected pages via repository reads where load-bearing (`gut-lumen-sink.md`, `cross-validation.md`, `open-questions.md`, `abcg2-modulators.md`). Repository fixed-string grep was unavailable because the tool backend lacked `rg`, so affected-page discovery was partly limited to bundle-supplied references plus targeted file reads.

## Bottom-line verdict
Action required. The current corpus-level interpretation correctly supersedes comp-019 with comp-044 and retires the ΔSUA, genotype-ranking, flat-dose, and yield-deprioritization conclusions. However, the invalidation propagation is incomplete inside the actual artifact: `outputs/phase_a_table.md` still contains an active “model predicts the mechanism works MORE in non-Q141K patients” statement with no invalidation banner, and `outputs/flux_model_results.json` remains a machine-readable invalid result file with no invalidation metadata. The model’s quantitative verdict is invalid.

## Implementation and constraint closure
I traced `inputs/flux_model_parameters.json` into `scripts/flux_model.py` and compared the script against all generated outputs.

Major implementation/constraint findings:

- The script does **not** use luminal urate concentration or uricase Km in the capacity calculation. It computes enzyme capacity as dose × specific activity × 24 h/day label turnover, then compares that Vmax-like capacity directly to a daily intestinal flux denominator. This is the same omitted substrate-occupancy and finite-exposure defect now identified by comp-044.
- ABCG2 Km and Vmax are stored in inputs but not used in the numerical model. They are cited only in assumptions/comments to justify a linear-regime statement.
- Luminal urate concentration (`0.59 µM`) is stored and repeatedly described as load-bearing, but it is not used to calculate uricase occupancy, local depletion, replenishment, or reaction rate.
- Finite residence/exposure time is absent. The code grants all delivered uricase activity access to a full-day substrate flux.
- The model’s “capacity ratio” denominator is `baseline_intestinal_genotype_adjusted_mg` in mg/day, not a local concentration × residence-time substrate supply. That makes the “substrate-limited at all doses” conclusion physically unclosed.
- The “sink amplification factor” is hard-coded at `0.40`; it is not read from inputs and is not varied in Monte Carlo despite the narrative describing 0.20–0.60 sensitivity.
- The Monte Carlo varies only total daily production, intestinal excretion fraction, and renal compensation. It does not vary uricase Km, luminal urate, residence time, oxygen, access, survival, sink amplification, ABCG2 functional ratios, baseline SUA, or enzyme specific activity.
- The artifact claims genotype scaling is empirically anchored to Miyazaki 2025 secretion ratios. The code actually uses nominal functional classes (`1.00`, `0.75`, `0.50`, `0.25`) and does not implement the Miyazaki median ratios (`100%:75%:50% ≈ 1:0.72:0.38`) except indirectly as narrative support. This is a separate mismatch from the comp-044 invalidation.
- The model substitutes nominal ABCG2 capacity for physiological urate delivery rate. It does not close local concentration, diffusion, transporter access, luminal mixing, oxygen availability, catalase/peroxide handling, microbial metabolism, or epithelial barrier safety.
- Reaction closure: uricase substrate/product/coproduct handling is incomplete. Uricase consumes urate and O₂ and produces allantoin plus H₂O₂/oxidative equivalents; oxygen and peroxide are not represented. Allantoin fate is not modeled. Redox burden and local peaks are not modeled.
- Mass balance is simplified to a one-step steady-state ΔSUA proportional to net daily flux / production. No extracellular urate pool, clearance kinetics, reabsorption dynamics, renal saturation, or compensation time base is modeled, despite some of these values being stored in inputs.
- Reproducibility path is plausible for reproducing the invalid outputs: stdlib Python script, fixed random seed, committed inputs/outputs, and corrected `cd` path. I did not execute the code. By inspection, the committed JSON and summary are consistent with the code structure and seed-dependent Monte Carlo, but reproducing them would only reproduce the invalid calculation.

## Summary-fidelity audit
Current top-level wiki propagation is mostly correct:

- `wiki/computational-experiments.md` marks comp-019 as **SUPERSEDED**, preserves only the useful Phase A negative finding, and retires ΔSUA, genotype ranking, capacity ratios, flat dose-response, and engineering recommendation.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` is now a superseded stub and explicitly says comp-019’s quantitative results must not guide dose or efficacy decisions.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` correctly identifies the comp-019 regime error.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` correctly retracts the −0.5 to −1.0 mg/dL prior and reopens the biological hypothesis.
- `wiki/validation-experiments.md` correctly promotes §1.33 and §1.36 as UOX topology/physiology and redox/safety gates.
- `wiki/gut-lumen-sink.md`, `wiki/cross-validation.md`, `wiki/open-questions.md`, and `wiki/abcg2-modulators.md` contain explicit 2026-07-13/14 resets and generally avoid treating comp-019 as active quantitative evidence.

But artifact-level summary fidelity remains incomplete:

- `README.md` now has a clear invalidation banner and reproduction path fix, but the body still says `Status: Complete` and repeats the retired verdict. The banner probably prevents downstream misuse for a human reader, but the internal status line is stale.
- `outputs/flux_model_summary.md` has a clear invalidation banner but still displays retired tables. Acceptable only if treated as frozen invalidated provenance.
- `wiki-archive.md` has a clear invalidation banner and is explicitly archived.
- `outputs/phase_a_table.md` has **no invalidation banner** and ends with the invalid active sentence: “the mechanism works MORE in non-Q141K patients than Q141K-positive patients.” This is a generated output and must be corrected or marked invalidated.
- `outputs/flux_model_results.json` has no machine-readable invalidation flag. Any downstream script consuming the JSON would see the invalid numbers as current `comp-019 v1.0` results.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_results.json` | generated output | Yes | Reproduces the invalid Vmax/daily-flux model; no invalidation metadata; action required to mark machine-readable results retired/superseded. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_summary.md` | generated output + proposed update | Yes | Invalidation banner added; body retains retired numbers as frozen provenance. Acceptable if all generated outputs are similarly marked. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/phase_a_table.md` | generated output | Yes | No invalidation banner; still contains invalid active Phase B conclusion about non-Q141K response. Action required. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | proposed update / summary | Yes | Invalidation banner and reproduction path fix added. Body still says `Status: Complete` and repeats retired verdict; should be softened or status marked superseded to avoid ambiguity. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md` | proposed update / archived wiki summary | Yes | Invalidation banner added; archived body remains historical. Materially acceptable as frozen provenance. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Total daily urate production 700 mg/day, range 600–900 | `inputs/flux_model_parameters.json`; `evaluate_scenario`; MC | Used in mass balance and ΔSUA denominator; cancels with intestinal fraction in substrate-limited branch except central flux reporting | “Standard physiology” citation string only; primary sources not directly verified here | Plausible but not sufficient for local luminal kinetics. |
| Intestinal excretion fraction 0.33, range 0.30–0.40 | Inputs; central and MC | Used as daily intestinal flux denominator | Multi-source consensus by citation string; not primary-verified in review | Used, but daily flux is incorrectly substituted for local accessible substrate. |
| ABCG2 functional classes 1.00/0.75/0.50/0.25 | Inputs; hard-coded `genotypes` in script | Used directly to scale daily intestinal flux | Cited to Matsuo/Miyazaki framework; not primary-verified here | Implemented, but does not actually use Miyazaki measured secretion ratios claimed in narrative. |
| Miyazaki 2025 secretion ratios | `phase_a_literature.json`; `flux_model_parameters.json`; narrative | Not used numerically in code | Artifact says full-text grep-verified; I did not independently verify PMC text | Load-bearing claim misrepresented: stored but not implemented. |
| Luminal urate 0.59 µM | Inputs and narrative | Not used | Artifact claims full-text grep verification | Stored-but-unused; central reason comp-019 fails. |
| ABCG2 Km 8.24 mM | Inputs and narrative | Not used in calculation | Abstract-tier per artifact | Stored-but-unused; only rhetorical support for linear-regime claim. |
| Uricase Km 25 µM | Inputs | Not used | Regulatory/label tier citation string | Stored-but-unused; central reason capacity ratio is invalid. |
| Uricase specific activity 8.3 U/mg with 0.75 in-vivo factor | Inputs; `evaluate_scenario` | Used to compute enzyme capacity | Regulatory/label tier citation string | Arithmetic use is clear, but Vmax is applied without substrate occupancy or finite exposure. |
| Uricase dose scenarios 5/25/50 mg/day | Inputs; scenario sweep | Used | Anchored to ALLN-346 / engineered-yeast feasibility by citation string | Dose-response conclusion invalid because local substrate/time/oxygen/access omitted. |
| Sink amplification factor 0.40 | Hard-coded in script; narrative says 30–50% reabsorption | Used directly to generate ΔSUA | Review-tier/mechanistic extrapolation; not directly measured | Hard-coded, not input-driven, not varied; unsupported load-bearing constant. |
| Renal compensation 0.30, range 0–0.50 | Inputs; MC | Used | Mechanistic extrapolation | Used, but sensitivity does not cover dominant uncertainties. |
| Baseline SUA by genotype/sex | Hard-coded in `genotypes` | Used for ΔSUA scaling | Input file has only generic male/female gout values; genotype-specific values are code-only | Provenance weak; not the main invalidating error but contributes to unsupported magnitude. |
| No Q141K-stratified uricase trial identified | `phase_a_literature.json`; `phase_a_table.md`; wiki summaries | Literature conclusion, not model input | Mixed abstract/press/conference-tier; direct primary verification not independently redone | Useful Phase A negative finding survives, with verification-tier caveats. |
| “WT/non-Q141K largest response; Q141K less response” | README, summary, archive, phase_a_table, JSON outputs | Output of invalid model | Unsupported by implemented physiological model | Retired; must not remain unbannered in any generated output. |
| “Flat dose above 5 mg/day; yield not limiting” | README/archive/summary | Output of invalid capacity ratio | Unsupported | Retired by comp-044; machine-readable JSON and phase table need invalidation marking. |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — comp-019 marked superseded; only Phase A gap retained.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — superseded stub with explicit retired-result warning.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — comp-044 clearly explains the substrate-occupancy/residence-time error.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — numerical prior retracted and biological hypothesis reopened.
- `wiki/validation-experiments.md` — already consistent in supplied sections — §1.33/§1.36 now gate UOX physiology and redox safety.
- `wiki/gut-lumen-sink.md` — already consistent with caveat — top quantitative reset and patient-stratification reset retire comp-019. Some older dose-feasibility language remains, but it is not explicitly based on comp-019 and is covered by the reset.
- `wiki/cross-validation.md` — already consistent — Claim 1 rating reset to 5.5/10 and comp-019 quantitative bridge retired.
- `wiki/open-questions.md` — already consistent — genotype stratification and H08 are reopened; comp-019 Phase A negative finding retained.
- `wiki/abcg2-modulators.md` — already consistent — no active comp-019 response magnitude; Q141K rescue remains prospective.
- `wiki/gout-multihop-research-program.md` — already consistent — immediate correction retires comp-019’s UOX dose regime.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 invalidation explicitly cites inherited comp-019 regime failure.

## New connections or implications
The useful surviving connection is narrower than the original comp-019 conclusion: Phase A’s negative finding—no Q141K-stratified uricase clinical outcome was identified—remains important, but it now supports **trial stratification and measurement design**, not any predicted responder ordering. The correct next model must combine genotype-dependent ABCG2 supply with substrate occupancy, local residence time, oxygen, peroxide handling, topology, and measured product formation. This is already reflected in H08 and validation §1.33.

A second implication: because `phase_a_table.md` mixes the surviving Phase A literature gap with the invalid Phase B responder conclusion, it is a particularly risky file for future readers. It should be split or bannered so the Phase A negative finding is preserved without reactivating the invalid model.

## Required actions
1. Add an invalidation/supersession banner to `outputs/phase_a_table.md`, or edit its closing Phase B statement to say the model prediction is retired and only the “no Q141K-stratified uricase trial found” result survives. Verification criterion: no unbannered generated Markdown output states that non-Q141K patients respond more or that comp-019 predicts genotype ordering.
2. Add machine-readable invalidation metadata to `outputs/flux_model_results.json` (for example `_metadata.status: "invalidated/superseded"`, `superseded_by: "comp-044"`, and `do_not_use_for: [...]`), or provide a clearly named sidecar consumed by downstream tooling. Verification criterion: any programmatic reader of the JSON can detect that ΔSUA, capacity ratios, genotype ranking, flat dose-response, and yield recommendations are retired.
3. Update `README.md` status/verdict lines, or add an immediately adjacent note after them, so they do not appear to be the current verdict beneath the banner. Verification criterion: a skim reader sees `Status: Invalidated/Superseded` before encountering the historical retired verdict.
4. Optional but recommended: state explicitly in the artifact README that `phase_a_table.md` preserves a valid literature-gap table but its Phase B extrapolation is retired. Verification criterion: Phase A surviving result and Phase B invalid result are separable.

## Review limits
I did not execute `scripts/flux_model.py`; reproducibility was assessed by inspection only. I did not independently retrieve or verify primary sources such as Miyazaki 2025, Matsuo 2014, Nakayama 2011, ALLN-346 abstracts, or regulatory labels; provenance assessment is therefore limited to citation strings and artifact-stated verification tiers. Repository grep failed because the backend `rg` binary was missing, so I could not perform a full fixed-string corpus search; I compensated by inspecting the supplied referencing pages and targeted omitted pages most likely to carry comp-019-derived claims. The validation page supplied in the bundle was truncated after section 1.16, but the relevant §1.33/§1.36 framing was visible in supplied top sections and cross-referenced pages.
