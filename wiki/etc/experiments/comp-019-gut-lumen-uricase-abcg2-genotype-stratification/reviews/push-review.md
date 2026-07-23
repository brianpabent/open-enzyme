COMP_VERDICT: quantitative_verdict_invalid
REVIEWED_SNAPSHOT: 72e91804f22b65993e0d92b09abcae042ff98afb360a3d6ff51bee1c00b32ec3
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation that comp-019 is an invalidated tombstone plus its bounded no-Q141K-stratified-uricase-outcome search observation
SYNTHESIS_ALLOWED_SCOPE: use only as negative provenance for retired comp-019 quantitative model and as a bounded literature-search gap
FORBIDDEN_INFERENCES: comp-019 ΔSUA estimates; capacity ratios; genotype-response ordering; flat-dose classification; oral-UOX dose sufficiency; yield conclusions; trial-design implications; efficacy or safety claims; topology or chassis selection; comp-031 rehabilitation from comp-019; comp-044 replacement dose or serum-urate model

# Independent comp review — comp-019

## Reviewed snapshot
Independent daemon consolidation review for comp-019; push-review manifest SHA-256 `72e91804f22b65993e0d92b09abcae042ff98afb360a3d6ff51bee1c00b32ec3`. Shard coverage reported complete inspection of supplied text spans. Targeted repository reads confirmed the live comp-019 tombstone, invalidation record, computational index, comp-019 interpretive page, and comp-044 interpretive page. No deterministic binary block was reported.

## Bottom-line verdict
Quantitative verdict invalid. The live corpus correctly retires comp-019 as a non-runnable invalidated tombstone: Phase B omitted physiological substrate occupancy and finite exposure, and none of its numerical outputs or decisions may be used. Action remains required for minor but material tracking/surface consistency issues: “SUPERSEDED” versus `invalidated_tombstone` status vocabulary, and a methodology page retaining “Monte Carlo n=5000” without equally prominent non-decision historical framing.

## Implementation and constraint closure
The retired implementation is not in the live tree; the live artifact preserves only `README.md` and `invalidation.json` with hashes for retired files at commit `dc7f4d2047dfb3bd378ee7a73618a11b67217257`. By inspection of the tombstone and downstream corrective pages, the load-bearing implementation failure is closed negatively: the comp-019 code did not use stored luminal urate concentration or UOX Km and assumed 24 hours of saturated activity. Therefore nominal enzyme capacity substituted for physiological reaction rate.

Constraint closure is not satisfied for the retired model. Substrate concentration relative to Km, finite active window, oxygen, enzyme survival, substrate access, localization/topology, peroxide/H₂O₂ safety, dynamic luminal replenishment/depletion, intestinal reabsorption, renal compensation, and genotype-specific supply were not modeled adequately for dose or serum-urate inference. COMP-044 supplies an internal-consistency counterexample, not a replacement physiological model: under inherited central priors, 0.59 µM urate, Km 25 µM, and a three-hour window give ratios 0.0932/0.4660/0.9320 for 5/25/50 mg, versus legacy saturated 24-hour ratios ≥32. These ratios only invalidate comp-019’s unconditional flat-dose framing; they do not establish the true operating regime or a sufficient oral-UOX dose.

## Summary-fidelity audit
The comp-019 tombstone, comp-019 interpretive page, gut-lumen uricase physiologic-regime page, gout action guide, open questions, comp-031 materials, and validation §§1.33/1.36 are materially aligned: no comp-019 ΔSUA, dose, genotype ordering, topology/chassis, efficacy, or safety conclusion survives.

Two fidelity issues require action:
1. `wiki/computational-experiments.md` labels comp-019 as “SUPERSEDED,” while the artifact/invalidation record says `invalidated_tombstone`. Both retire decision use, but inconsistent vocabulary can confuse eligibility and archival tracking.
2. `wiki/etc/autonomous-screening-methodology.md` retains a quantitative implementation descriptor for comp-019 (“Monte Carlo n=5000”). If kept, it must be explicitly historical/non-decision-grade wherever it appears.

## Reader-facing ownership audit
The focused comp-019 page now owns the retired-evidence contract: it states exactly what is invalidated, what survives, and where current evidence lives. The interpretive page correctly prevents clinical, dosing, and genotype-response use. Portfolio-style rankings or topology comparisons are not assigned to comp-019; current validation pages require exact configurations and configuration-level measurements before any topology claim. No personalized treatment instruction was found on the reviewed comp-019-relevant reader surfaces.

## Conjecture preservation audit
The unsupported factual claims killed by comp-019 are narrow: the old saturated-capacity/dose/ΔSUA/genotype-order decision rule and any inherited comp-019 topology or production sufficiency. The idea value survives as a Research Conjecture only: a gut-lumen uricase sink might still be useful if exact configurations demonstrate physiological urate access, oxygen/activity, persistence, product formation, mass balance, and H₂O₂/barrier safety. Q141K remains a prospective stratification variable because the surviving search observation found no Q141K-stratified uricase clinical outcome in searched sources as of 2026-05-08; this is not proof of universal absence.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | push text / comp artifact | Yes | Invalidated tombstone; non-runnable; only bounded search observation survives. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` | push text / comp artifact | Yes | Hash-bound retirement record; retired files preserved by Git only. |
| `wiki/computational-experiments.md` | push text / index | Yes | Correctly retires quantitative use, but status vocabulary differs from tombstone. |
| `wiki/uricase-abcg2-genotype-stratification-computational.md` | push text / interpretive page | Yes | Faithful: historical model not decision-usable; bounded search preserved. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | push text / superseding interpretive page | Yes | Faithful corrective scope; no replacement efficacy model. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | push text / superseding comp artifact | Yes | Supports non-robustness only; inherited inputs non-planning-grade. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | push text / provenance | Yes | Several inherited inputs not newly primary-verified. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md` | push text / review | Yes | Clean-with-limitations; corrective propagation only. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | push text / downstream comp | Yes | Correctly invalidates comp-019 inherited saturation use. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/inputs/provenance.md` | push text / provenance | Yes | Rejects comp-019 UOX effect sizes/regime. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/reviews/post-run.md` | push text / review | Yes | Confirms hard-coded unsupported comp-019 anchor in retired model. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | push text / interpretive page | Yes | Consistent: comp-031 cannot be rehabilitated via comp-019. |
| `wiki/gout-action-guide.md` | push text / reader page | Yes | Correctly blocks clinical/personal decision use. |
| `wiki/gout-genetic-variants.md` | push text / affected mechanism page | Yes | Comp-019 boundaries consistent; unrelated evidence-tier issues noted in review limits/actions only if separately triaged. |
| `wiki/open-questions.md` | push text / affected queue | Yes | Correctly keeps UOX/gut-sink questions open and gated. |
| `wiki/gout-multihop-research-program.md` | push text / program page | Yes | Requires exact UOX configurations before escalation; consistent. |
| `wiki/validation-experiments.md` | push text / validation plan | Yes | §§1.33/1.36 correctly gate UOX topology and H₂O₂/barrier safety; many unrelated validation issues found. |
| `wiki/etc/autonomous-screening-methodology.md` | push text / methodology | Yes | Retains comp-019 Monte Carlo detail; needs historical/non-decision-grade labeling. |
| `wiki/etc/bio-ai-tools.md` | push text / methodology | Yes | Does not rescue comp-019; reinforces need for primary verification. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md` | push text / comparison provenance | Yes | No direct comp-019 issue; useful contrast for verification discipline. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/query-strategy.md` | push text / comparison provenance | Yes | No material comp-019 finding. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md` | push text / comparison output | Yes | No material comp-019 finding. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md` | push text / output | Yes | No material comp-019 finding. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Comp-019 is non-runnable invalidated tombstone | comp-019 `README.md`, `invalidation.json` | Governs live artifact use | Directly present and hash-bound | Accepted. |
| Retired files preserved at commit `dc7f4d...` with file-set SHA-256 `ce744f...2529e` | `invalidation.json` | Provenance only; not active reproduction | Hashes listed, not independently Git-verified in this review | Adequate for tombstone; historical verification would require Git/hash check. |
| Luminal urate concentration and UOX Km were stored but unused | comp-019 interpretive page; comp-031/044 corroboration | Invalidates Phase B model fit | Supported by corpus review; retired code not reopened | Accepted as live-corpus invalidation basis. |
| 24-hour saturated UOX activity assumed | tombstone and comp-044 pages | Invalidates capacity-ratio and flat-dose conclusions | Supported by corrective comp-044 | Accepted. |
| 0.59 µM jejunal urate | comp-044 interpretive/provenance | Used in corrective diagnostic, not comp-019 | Reported as grep-verified extraction from Miyazaki 2025; primary not rechecked here | Adequate only for bounded counterexample. |
| Km 25 µM, 8.3 U/mg activity, 2–4 h window, 233 mg/day denominator | comp-044 interpretive/provenance | Corrective diagnostic sensitivity inputs | Inherited/derived, not newly primary-source verified | Non-planning-grade; cannot support dosing. |
| Ratios 0.0932/0.4660/0.9320 at 5/25/50 mg | comp-044 output/interpretive/review | Internal-consistency counterexample | Derived within comp-044; code not executed here | Supports only non-robustness of comp-019. |
| No Q141K-stratified uricase clinical outcome in searched sources as of 2026-05-08 | comp-019 tombstone and interpretive page | Surviving Phase A observation | Search logs not independently rerun; statement is bounded | Usable only as dated searched-source gap. |

## Affected wiki pages
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` — already consistent — tombstone prohibits all quantitative decision use.
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` — already consistent — scope and surviving observation are explicit.
- `wiki/computational-experiments.md` — change required — harmonize “SUPERSEDED” with `invalidated_tombstone` or define both statuses unambiguously.
- `wiki/etc/autonomous-screening-methodology.md` — change required — mark comp-019 “Monte Carlo n=5000” as historical/non-decision-grade if retained.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — blocks dose/efficacy/genotype/topology use.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — corrective scope only; no replacement model.
- `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/` — already consistent — supersedes only flat-dose robustness.
- `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/` — already consistent — rejects inherited comp-019 assumptions.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 requires replacement UOX physiology.
- `wiki/gout-action-guide.md` — already consistent — no clinical/personal decision use from comp-019.
- `wiki/open-questions.md` — already consistent — keeps genotype-stratified gut-lumen sink as gated research question.
- `wiki/gout-multihop-research-program.md` — already consistent — requires exact UOX configurations and validation gates.
- `wiki/validation-experiments.md` — already consistent for comp-019-relevant §§1.33/1.36 — direct configuration, product, mass-balance, and safety gates are required.

## New connections or implications
Research Conjecture: Q141K-stratified gut-lumen urate-sink response remains a plausible but untested stratification idea. Sourced premises in the corpus: ABCG2/Q141K is relevant to urate transport biology; comp-019’s bounded search did not find Q141K-stratified uricase clinical outcomes; comp-044 shows any oral-UOX dose claim must account for substrate occupancy and finite exposure. Unsupported leap: genotype-specific intestinal urate supply could materially change luminal UOX response. Discriminating observations: configuration-level §1.33 measurements with genotype/transport-relevant urate flux, followed only if safe by regulated stratified human evidence.

## Required actions
1. In `wiki/computational-experiments.md`, reconcile comp-019 status wording with the artifact status `invalidated_tombstone`, or explicitly define “SUPERSEDED” as non-runnable invalidated tombstone for eligibility purposes. Verification: index, tombstone, and interpretive page use compatible status semantics.
2. In `wiki/etc/autonomous-screening-methodology.md`, revise the comp-019 “Monte Carlo n=5000” entry to state it is historical invalidated implementation detail and not decision-grade evidence. Verification: no methodology table can be read as preserving active comp-019 quantitative support.
3. Do not propagate any comp-019 numerical outputs, including via comp-031 or portfolio summaries. Verification: searches for comp-019-derived ΔSUA, −0.83 mg/dL anchors, capacity ratios, flat-dose classifications, genotype ordering, dose/yield, topology/chassis, or safety claims either find none or label them invalidated.

## Review limits
I did not execute code and did not reopen retired Git artifacts; the live tree intentionally contains no runnable comp-019 implementation. Historical hash verification would require Git access to commit `dc7f4d2047dfb3bd378ee7a73618a11b67217257`. Primary sources for Miyazaki 2025, UOX activity, Km, active window, and intestinal flux denominator were not independently verified here. Repository fixed-string search tooling failed because `rg` was unavailable; targeted `read_file` checks and complete shard coverage were used instead. Several unrelated evidence-tier and validation-design issues were found in broad affected pages but are outside the comp-019 decision unless those pages are separately reviewed.
