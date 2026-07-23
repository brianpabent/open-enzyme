PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: a3616383b205ace269f069dfadd8ff381b4a1d782400dfb13e69570db5eb5ce7

# Adversarial pre-run review — comp-019

## Reviewed snapshot

Reviewer `/root/comp019_tombstone_pre_review`; canonical `pre-run.manifest.json` SHA-256 `a3616383b205ace269f069dfadd8ff381b4a1d782400dfb13e69570db5eb5ce7`; 2 design files; 0 prior-output baselines. The manifest matched the inspected `README.md` and `invalidation.json` exactly. Excluding `reviews/`, the live tree contains only those two files.

## Bottom-line verdict

The retirement transition may proceed to downstream authoring without a material design correction. The tombstone removes all live code, inputs, outputs, and cached bytecode; preserves Git-retrievable, hash-bound provenance for the nine retired files; invalidates the complete Phase B numerical and decision scope; and retains only the dated, searched-corpus Phase A observation. There is no experiment to execute and no live numerical artifact to misread as a current result.

## Question and model fit

This artifact answers an archival-governance question, not the original biological question: can comp-019 be retired without losing auditability or allowing its invalid model to remain decision-usable?

The design fits that purpose. The sole survivor—“The sources searched for comp-019 contained no Q141K-stratified uricase clinical outcome”—matches the frozen 2026-05-08 Phase A record and explicitly disclaims universal absence. Miyazaki 2025 supplies genotype-stratified intestinal urate secretion, not a genotype-stratified uricase treatment outcome, so it does not contradict the survivor.

The invalidation boundary is faithful. No Phase B ΔSUA estimate, capacity ratio, genotype-response ordering, dose, flat-dose classification, yield conclusion, trial-design implication, efficacy or safety inference, or topology/chassis conclusion survives. The categorical README statement that none of Phase B’s numerical outputs or decisions may be used also covers derived demographic or sex-response comparisons.

## Constraint and implementation audit

The current non-review tree has exactly two regular files: `README.md` and `invalidation.json`. No `scripts/`, `inputs/`, `outputs/`, `__pycache__/`, `.py`, or `.pyc` artifact remains. The README’s `git show` example retrieves a historical blob; it is not a reproduction or execution command.

Commit `dc7f4d2047dfb3bd378ee7a73618a11b67217257` resolves as a Git commit and contains exactly the nine listed non-review design/output files plus historical review files. Every listed byte count and SHA-256 matched the corresponding Git blob. The canonical file-set digest also matched: compact JSON serialization of `retired_files`, with recursively sorted keys and no trailing newline, hashes to `ce744f989acb744a78f365e3a61f0154dc300545b7b4843ae05851bb5722529e`.

The recorded retired post-run manifest identifier `116ae39ac8778e456024f85a4487f4064e859480c10bdf4f0cebe25eb5629f84` and last push-review manifest identifier `a62c6d224d82e89b68f383607693f6d4074e2918356e8d73f3bb9cf7f398bb1e` also match the manifests at the retired commit. The prior push-review requirement to reconcile live guarded execution with the hash-only invalidation policy is therefore closed by this design.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Live tombstone README | Current `README.md` | State invalidation, survivor, retrieval path, and evidence owners | 1,993 bytes; SHA-256 `3e1bdaeeb736f9a37b79d923a87ce31609b347b6976b9c4e8cb2ad5246e6a194`; manifest matched | Pass |
| Machine-readable invalidation record | Current `invalidation.json` | Bind retired tree, retired files, invalidated scope, survivor, and evidence home | 2,683 bytes; SHA-256 `960349dc7fd514bd94230a2d66d2868a7c7e533f7c58424b4cd1220e84ec5412`; manifest matched | Pass |
| Retired `README.md` | Retired commit | Recover last live experiment contract | 8,650 bytes; SHA-256 `154b8826f43fc0929c9fac40072d8ceca345ef5b096a5651eb00906a26d67cc1`; Git blob matched | Pass |
| Retired `inputs/flux_model_parameters.json` | Retired commit | Recover Phase B parameters | 7,585 bytes; SHA-256 `f5c4ac8cc324280ded4f87dec5a9b47b47ba565331f4b7ba021c76b78067bb63`; Git blob matched | Pass |
| Retired `inputs/phase_a_literature.json` | Retired commit | Recover dated Phase A source record | 19,965 bytes; SHA-256 `027b36b73ab811e87a774a42f5034645a32a3cb9f7778ab588790a73927d875c`; Git blob matched | Pass |
| Retired `inputs/query_strategy.md` | Retired commit | Recover searched-corpus boundaries | 3,424 bytes; SHA-256 `a4a02041d479eae707512f24b8c72fa93b62f6a96f4fb57146b3d5fabdfb0310`; Git blob matched | Pass |
| Retired `outputs/flux_model_results.json` | Retired commit | Audit invalidated machine output | 14,828 bytes; SHA-256 `d681d0ff723ad47b612fb5825cdafda82b347eb68dfb31cf06b7a7d3830c12a9`; Git blob matched | Pass |
| Retired `outputs/flux_model_summary.md` | Retired commit | Audit invalidated human-readable output | 3,756 bytes; SHA-256 `6738ac618de9557bf562a0fde110234c0d681e63cc93e6fa52d2bad42998cae9`; Git blob matched | Pass |
| Retired `outputs/phase_a_table.md` | Retired commit | Audit bounded Phase A survivor | 7,263 bytes; SHA-256 `ef87d4977be18dc3cc8bba7f4f582347cb2d1f8d081dbd31b7b7252ee70b6166`; Git blob matched | Pass |
| Retired `scripts/flux_model.py` | Retired commit | Audit invalid model implementation without retaining runnable code | 20,296 bytes; SHA-256 `63a6af2590f6901bed288fe44ca410af0606247daa8836547593fd2a3c564b58`; Git blob matched | Pass |
| Retired `scripts/verify_retirement.py` | Retired commit | Audit former guarded-reproduction contract | 5,977 bytes; SHA-256 `2871f25de60b112c87896fab743ea2564af4866de11065b3aeaf81acca5bb51b`; Git blob matched | Pass |
| Canonical retired-file-set digest | `invalidation.json` | Detect omission, reordering, or metadata alteration in the nine-file ledger | Independently recomputed as `ce744f989acb744a78f365e3a61f0154dc300545b7b4843ae05851bb5722529e` | Pass |
| Dated Phase A survivor | `invalidation.json` and README | Preserve only the searched-corpus observation | Exact frozen search date and non-universal modality retained | Pass |
| Phase B invalidated scope | `invalidation.json` and README | Prohibit all numerical and decision reuse | Covers model outputs, rankings, dose/yield, trial, efficacy/safety, and topology/chassis uses | Pass |

## Falsification, sensitivity, and output contract

This transition fails if the live non-review tree contains anything beyond the two tombstone files; if any retired blob’s bytes or hash differ; if the aggregate digest fails; if the retired commit cannot retrieve the files; if the Phase A statement loses its 2026-05-08 searched-corpus boundary; or if any Phase B numerical or decision claim remains eligible. None of those failure conditions occurred.

There is no sensitivity analysis or generated-output schema because the artifact is deliberately non-runnable. Auditability is supplied by the exact commit, per-file bytes and SHA-256 values, the canonical file-set digest, and the retained review identifiers.

## Downstream authoring contract

The canonical evidence home is `wiki/uricase-abcg2-genotype-stratification-computational.md`. Downstream authoring should preserve only the dated Phase A observation and replace its current statement that frozen inputs, code, and outputs are live in the experiment directory with an accurate tombstone/Git-retrieval description.

`wiki/gut-lumen-uricase-physiologic-regime-computational.md` remains the bounded COMP-044 consistency audit; validation §§1.33 and 1.36 remain the physiological efficacy and safety gates. No downstream surface may restore comp-019 ΔSUA values, ratios, response ordering, doses, flat-dose status, yield sufficiency, trial design, efficacy/safety, or topology/chassis selection. Cross-track comparisons remain portfolio-only, and the retirement transition introduces no personalized treatment instructions or reader-facing numerical residue.

No correction to the tombstone itself is required before that separately reviewed downstream authoring.

## Required actions before execution

None.

## Review limits

Static repository and Git-object inspection only. I did not execute the retired model or verifier, rerun the 2026-05-08 literature search, or independently retrieve the underlying primary publications. Scientific use of the Phase A survivor therefore remains limited to its explicit dated searched-corpus scope.
