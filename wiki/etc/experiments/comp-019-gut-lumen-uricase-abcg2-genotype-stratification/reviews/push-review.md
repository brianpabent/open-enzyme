COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: a62c6d224d82e89b68f383607693f6d4074e2918356e8d73f3bb9cf7f398bb1e
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of comp-019 invalidation and bounded Phase A search absence
SYNTHESIS_ALLOWED_SCOPE: bounded synthesis that comp-019 Phase B is retired and Q141K remains an unvalidated prospective stratifier
FORBIDDEN_INFERENCES: comp-019 ΔSUA predictions; dose selection; genotype-response ranking; flat-dose/substrate-limited verdict; yield or chassis sufficiency; trial-arm design; clinical efficacy or safety claims; comp-044 regime reversal

# Independent comp review — comp-019

## Reviewed snapshot
Independent daemon consolidation reviewer; bound to supplied `push-review.manifest.json` SHA-256 `a62c6d224d82e89b68f383607693f6d4074e2918356e8d73f3bb9cf7f398bb1e`. Shard coverage reports complete inspection of all listed text spans and no deterministic blocks. I performed targeted repository cross-checks on the comp-019 script and the main comp-019/comp-044 interpretive pages. Local `grep_repo` was unavailable because `rg` is absent; local manifest file was not readable, so binding is to the daemon-supplied hash and shard coverage receipt.

## Bottom-line verdict
**Action required, but bounded propagation/synthesis remains eligible with warning.** The active corpus now correctly treats comp-019 Phase B as invalidated and non-decision-usable. The only surviving result is a bounded Phase A negative search: no Q141K-stratified uricase clinical outcome or direct human ΔSUA-per-luminal-uricase-unit measurement was found in searched sources as of 2026-05-08. Required action is process/documentation cleanup: the computational-experiments policy says fully invalidated COMPs retain only a hash-bound invalidation record and are not rerun, while comp-019 retains guarded executable reproduction scripts and outputs.

## Implementation and constraint closure
The historical `flux_model.py` is now guarded by `--reproduce-invalidated-history` and writes invalidation metadata. The implemented historical model still demonstrates why the Phase B verdict cannot stand: it converts nominal uricase specific activity into daily capacity using a full 24-hour activity assumption, applies a fixed 0.75 in-vivo activity factor, a fixed 0.40 sink-amplification factor, genotype-scaled intestinal flux, renal compensation, and a first-order steady-state ΔSUA mapping. It does **not** implement a dynamic gut compartment, finite residence/exposure, local substrate replenishment/depletion, oxygen limitation, diffusion/access, microbial/protease survival, peroxide handling, reabsorption dynamics, or serum-pool/renal feedback sufficient for ΔSUA prediction.

Stored/declared physiology that is load-bearing for real uricase feasibility is not closed by comp-019: physiological luminal urate, UOX Km, oxygen, active window, and gut localization are not used in the historical decision rule. Reaction closure is incomplete for decision use: uricase consumes urate and oxygen and produces allantoin plus hydrogen peroxide/intermediates, but the historical model treats enzyme capacity as if substrate and electron acceptor access are unconstrained and does not close redox or local coproduct safety. Comp-044 later supplies only a bounded consistency diagnostic showing comp-019’s unconditional flat-dose classification is not robust; it does not repair serum-effect, dose, topology, genotype, or safety modeling.

## Summary-fidelity audit
The comp-019 README, output summary, phase table, machine-readable output metadata, interpretive page, comp-044 page, computational-experiments index, gout action guide, genetic-variants page, open-questions page, dual-chassis comp-031 page, and related methodology pages are materially aligned on the important boundary: Phase B numbers, rankings, dose/yield/trial-design implications, and flat-dose conclusions are retired.

No stronger replacement claim was found in the inspected relevant surfaces. Comp-044 is consistently framed as an internal consistency audit, not a physiological-regime reversal. Q141K remains a prospective stratification variable, not an established responder ordering. ALLN-346 evidence is correctly kept at conference/press-release or incomplete-study tier and not treated as genotype-stratified efficacy evidence.

One summary/process mismatch remains: `wiki/computational-experiments.md` states fully invalidated COMPs retain only a hash-bound invalidation record and are not rerun, but comp-019 retains live executable scripts and a guarded reproduction path. The warnings substantially reduce scientific propagation risk, but the policy should be reconciled.

## Reader-facing ownership audit
Focused comp-019 and comp-044 pages mostly satisfy the reader contract: they own their evidence tier, constraints, falsification boundary, and forbidden uses. Portfolio-style cross-track comparisons are not being smuggled into the comp-019 focused page. The gout action guide preserves the research-surface boundary and defers clinical decisions to qualified clinicians.

No personalized treatment instructions or home-use path was found as an active comp-019-derived claim. The remaining reader-facing risk is archival: live reproduction commands and numerical tables can look usable despite invalidation banners. Keep those outputs framed as provenance-only.

## Conjecture preservation audit
The invalidated Phase B result kills only the exact computational claims it tested: comp-019 ΔSUA magnitudes, genotype response ordering, unconditional flat-dose/substrate-limited classification, yield sufficiency, and trial-design implications. It does not kill the broader gut-lumen uricase hypothesis, ABCG2 as a plausible stratification axis, or the need for direct UOX topology/oxygen/peroxide/access validation.

Preserved Research Conjecture boundary: Q141K may alter luminal UOX response if epithelial urate supply limits the sink, but the unsupported leap is genotype-specific clinical response; the discriminating observation is direct genotype-stratified epithelial/luminal urate flux and serum outcome under a manufactured, characterized UOX product.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | comp artifact/update | Yes | Correct invalidation boundary. |
| `.../inputs/flux_model_parameters.json` | comp input | Yes | Contains historical priors; several not decision-verified. |
| `.../inputs/phase_a_literature.json` | comp input | Yes | Supports bounded search absence; weak/secondary clinical evidence limits. |
| `.../inputs/query_strategy.md` | comp input | Yes | Date/source-bounded Phase A claim. |
| `.../outputs/flux_model_results.json` | generated output | Yes | Machine-readable invalidation metadata forbids decision use. |
| `.../outputs/flux_model_summary.md` | generated output | Yes | Historical numbers retained with clear invalidation banner. |
| `.../outputs/phase_a_table.md` | generated output | Yes | Preserves “no responder ordering survives.” |
| `.../scripts/flux_model.py` | code | Yes | Guarded archival reproduction; still implements retired assumptions. |
| `.../scripts/verify_retirement.py` | code/check | Yes | Retirement verification artifact inspected by shard. |
| `wiki/computational-experiments.md` | proposed/affected wiki | Yes | Substantively faithful; policy conflict on rerunnable invalidated COMPs. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | affected wiki | Yes | Correctly keeps comp-031 invalidated; no inherited comp-019 claim. |
| `wiki/etc/autonomous-screening-methodology.md` | affected wiki | Yes | Correctly frames comp-019/044 boundary; unrelated methodology caveats noted. |
| `wiki/etc/bio-ai-tools.md` | affected wiki | Yes | No comp-019 misuse found; several general tool-evidence caveats. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/*` | affected corpus surface | Yes | Mostly unrelated complement findings; no comp-019 propagation issue. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/*` | dependent comp | Yes | Correctly retired inherited flat-UOX/additivity claims. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/*` | superseding comp | Yes | Correct bounded non-robustness verdict; no replacement dose/efficacy. |
| `wiki/gout-action-guide.md` | affected wiki | Yes | Correct research-only boundary and UOX uncertainty. |
| `wiki/gout-genetic-variants.md` | affected wiki | Yes | Correct genotype tiers and modality-specific safety separation. |
| `wiki/gout-multihop-research-program.md` | affected wiki | Yes | Correct ordering: build/characterize exact UOX configurations before validation. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed/affected wiki | Yes | Faithful comp-044 boundary and limitations. |
| `wiki/open-questions.md` | affected wiki | Yes | Correctly keeps gut-lumen sink and Q141K questions open. |
| `wiki/uricase-abcg2-genotype-stratification-computational.md` | proposed/affected wiki | Yes | Clear “historical/not decision-usable” status. |
| `wiki/validation-experiments.md` | affected wiki | Yes | UOX gates broadly consistent; several protocol/dashboard issues exist, mostly outside comp-019. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| No Q141K-stratified uricase clinical outcome found as of 2026-05-08 | Phase A inputs/table; README; interpretive page | Surviving non-quantitative result | Search-bounded, not universal absence | Usable only with boundary. |
| ALLN-346 lacks ABCG2 genotype stratification | Phase A literature | Not in model; informs Phase A | Conference/press-release/incomplete trial tier | Cannot support efficacy or genotype ranking. |
| Miyazaki 2025 jejunal urate / ABCG2 evidence | Phase A literature; comp-044 page | Historical rationale; comp-044 inherited input | Direct citation present; small/generalizability limits | Planning-grade only. |
| 0.59 µM luminal urate | comp-044 page/provenance | Not used in comp-019 Phase B; used by comp-044 diagnostic | Inherited grep-verified extraction per comp-044 | Supports bounded non-robustness test, not dose selection. |
| UOX Km 25 µM/range | comp-044; comp-019 inputs | Omitted from comp-019 decision rule | Inherited/not newly primary-source verified | Must verify before quantitative planning. |
| 8.3 U/mg specific activity | comp-019 inputs; comp-044 | Used in capacity conversion | Inherited/not newly primary-source verified | Not enough for dose/yield claims. |
| 24 h saturated activity | comp-019 script | Historical core assumption | Model assumption, not physiological closure | Invalidates Phase B use. |
| 2–4 h active window | comp-044 | Finite-window diagnostic | Inherited prior | Diagnostic only; needs measurement. |
| Sink amplification factor 0.40 | comp-019 script | Directly scales ΔSUA | Mechanistic extrapolation | Not decision-valid. |
| Renal compensation 0–50%, central 30% | comp-019 inputs/script | Directly scales ΔSUA | Not measured in oral UOX trials | Cannot rescue ΔSUA model. |
| Genotype functional classes 100/75/50/25% | comp-019 script | Drives responder ordering | Simplifying extrapolation | Retired for response prediction. |
| UOX reaction oxygen/peroxide constraints | comp-044/open questions/validation | Absent from comp-019 model | Requires direct assay | Must close before animal/efficacy inference. |

## Affected wiki pages
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — comp-019 historical, Phase B forbidden.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — comp-044 only shows non-robustness, no replacement physiology.
- `wiki/computational-experiments.md` — change required — reconcile “fully invalidated COMPs are not rerun / retain only hash-bound invalidation record” with comp-019’s guarded executable reproduction path.
- `wiki/gout-action-guide.md` — already consistent — research-only and no validated UOX dose/genotype model.
- `wiki/open-questions.md` — already consistent — gut-lumen sink feasibility and Q141K remain open.
- `wiki/gout-genetic-variants.md` — already consistent — Q141K effect tiers and UOX modality safety boundaries preserved.
- `wiki/gout-multihop-research-program.md` — already consistent — exact UOX configurations and safety gates precede escalation.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 remains invalidated and not rehabilitated by comp-019/044.
- `wiki/validation-experiments.md` — limited change required outside the core comp-019 verdict — fix UOX-adjacent protocol/dashboard ambiguities if they are used for scheduling or execution.

## New connections or implications
Comp-019’s failure and comp-044’s diagnostic jointly imply that UOX yield optimization cannot be deprioritized merely because nominal Vmax looks large. The discriminating gate is not enzyme mass alone but configuration-specific urate access, oxygen, survival, topology, and peroxide control under physiological substrate.

Research Conjecture: ABCG2 Q141K may matter most after a UOX configuration demonstrates real luminal substrate capture; before that, genotype stratification could be swamped by oxygen/access/survival limits. Unsupported leap: Q141K predicts human response magnitude. Discriminating observation: matched genotype-stratified epithelial/luminal flux plus product-specific serum-urate and safety readouts.

## Required actions
1. Reconcile `wiki/computational-experiments.md` policy with comp-019’s retained guarded executable scripts: either revise the convention to allow clearly marked archival reproduction or move comp-019 to a non-rerunnable hash-only record. Verification: no reader-facing contradiction remains.
2. Keep all comp-019 numerical outputs marked provenance-only in any future propagation. Verification: no page cites comp-019 ΔSUA, capacity ratios, genotype ordering, flat-dose status, yield sufficiency, or trial design as evidence.
3. If UOX validation sections are used operationally, resolve the UOX-adjacent `validation-experiments.md` protocol/dashboard ambiguities identified by shards before execution scheduling. Verification: queue, dependencies, assay panels, and success criteria are internally consistent.

## Review limits
No experiment code was executed. Primary sources were not independently retrieved; provenance status is based on committed citations, extracted tables, and shard-inspected text. Local fixed-string repository search failed because `rg` is unavailable, and the local `push-review.manifest.json` file was not readable; review binding relies on the supplied daemon hash and complete shard coverage. Binary artifacts were not present as deterministic blocks.
