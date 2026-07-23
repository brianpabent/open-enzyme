ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 643ad2cf43268ba93a34c7b884a73ef43e1dc7249c7709d5c702c4af6627cd9a

# Independent comp review — comp-019

## Reviewed snapshot

Reviewer `/root/comp019_tombstone_post_review_v4`; authoring-time Gate 2 manifest canonical SHA-256 `643ad2cf43268ba93a34c7b884a73ef43e1dc7249c7709d5c702c4af6627cd9a`. The manifest file itself has SHA-256 `749ab7ef244d9a4f3eae222b6b78f0d19f2e0c6e5244bf5d7e76a7910d39c7d1`. All ten entries matched their recorded byte counts and SHA-256 hashes.

The nine-file retired ledger was independently recovered from commit `dc7f4d2047dfb3bd378ee7a73618a11b67217257`; every blob matched `invalidation.json`, and the canonical ledger digest recomputed to `ce744f989acb744a78f365e3a61f0154dc300545b7b4843ae05851bb5722529e`.

## Bottom-line verdict

Clean. The proposed retirement leaves a policy-compliant, non-runnable tombstone; preserves only the dated Phase A searched-corpus observation; prohibits every Phase B numerical or decision use; closes the current COMP-019 and COMP-044 maintenance actions; and adds a deterministic dashboard-fidelity guard.

Both `synthesis/queue/comp-review-019.md` and `synthesis/queue/comp-review-044.md` may be deleted as queue closure in the same change. Their current required actions are resolved.

## Implementation and constraint closure

The live non-review COMP-019 tree contains exactly `README.md` and `invalidation.json`. It contains no code, input, output, executable, symlink, bytecode, reproduction path, or generated numerical artifact. The README’s `git show` example retrieves a historical blob for provenance; it neither runs the model nor recreates outputs.

The tombstone matches the repository convention that invalidated COMPs are not rerun and retain a hash-bound invalidation record while Git preserves history. `runnable: false`, the retired commit, nine exact blob hashes, retired manifest digests, invalidated scope, survivor scope, and current evidence owners are internally consistent.

The retired code was inspected statically only. Its historical Phase B failure remains correctly characterized: physiological substrate occupancy and finite exposure were absent from the decision model. No current surface rehabilitates its ΔSUA, capacity, genotype, dose, yield, trial, efficacy, safety, or topology conclusions.

## Summary-fidelity audit

The surviving statement is consistently limited to: the sources searched for COMP-019 as of 2026-05-08 contained no Q141K-stratified uricase clinical outcome. Each current statement rejects universal absence.

`README.md`, `invalidation.json`, `wiki/computational-experiments.md`, and `wiki/uricase-abcg2-genotype-stratification-computational.md` consistently prohibit all Phase B decision use. The broader active corpus likewise describes COMP-044 only as an internal-consistency counterexample, not a replacement dose, ΔSUA, genotype-order, physiological-regime, efficacy, topology/chassis, production, or safety model.

The paper update replaces a dead live-tree script path with the exact retirement commit. Its approximate luminal-urate and Km values are used only to document the omitted-input failure, not as surviving COMP-019 output or decision evidence.

The validation maintenance closes the queued discrepancies:

- §1.10 now carries `$2,460–4,460`, `3–4` weeks, a four-lane core, and a fifth lane explicitly excluded from the core and permitted only as separately costed optional work.
- §1.20 is a 3×3 full factorial, with a separately declared tenth midpoint condition if the prespecified midpoint is not among the nine cells.
- §1.22 consistently carries `$5,000–8,000` and `8–10` weeks.
- §1.25 consistently budgets a two-arm experiment and explicitly requires parallel RIB40 and NSlD-ΔP10 hosts.
- Previously omitted §§1.26–1.32 and all other numbered sections now appear in the dashboard.
- Every numbered section has Cost and Weeks metadata agreeing exactly with its dashboard row.
- §1.34’s `yanthine` nomenclature is source-justified.

## Reader-facing ownership audit

The focused COMP-019 interpretation owns the historical model failure, bounded survivor, current experimental gates, and provenance without cross-track ranking, personalized dosing, or editorial-history exposition. The tombstone is concise and does not duplicate the retired artifact.

The validation changes remain experiment-planning metadata and protocol clarification. They do not promote computational priors into wet-lab results or clinical claims.

## Conjecture preservation audit

The retirement kills only COMP-019’s Phase B numerical and decision scope. It does not kill the broader gut-lumen UOX hypothesis, ABCG2 as a prospective stratification axis, or configuration-specific substrate/oxygen/access/survival/peroxide questions.

Q141K remains an unvalidated prospective stratifier. No genotype-response direction, magnitude, fixed dose, or responder ordering survives.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | design | Yes | Non-runnable tombstone; scope and Git provenance correct. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` | design | Yes | Retirement ledger, scopes, digests, and evidence owners verified. |
| `.githooks/pre-push` | proposed update | Yes | Dashboard guard runs from repository root and blocks failure. |
| `.github/workflows/corpus-integrity.yml` | proposed update | Yes | Server-side guard integrated; YAML valid. |
| `.github/workflows/wiki-propagate.yml` | proposed update | Yes | Post-propagation guard integrated before state advancement; YAML valid. |
| `papers/cross-vendor-heterogeneity-guard/draft.md` | proposed update | Yes | Dead script path replaced by exact Git provenance. |
| `scripts/check-validation-dashboard.py` | proposed update | Yes | Deterministic stdlib-only completeness and metadata checker. |
| `wiki/computational-experiments.md` | proposed update | Yes | “Hash-bound tombstone” accurately describes the live artifact. |
| `wiki/uricase-abcg2-genotype-stratification-computational.md` | proposed update | Yes | Git recovery and forbidden-use boundary are explicit. |
| `wiki/validation-experiments.md` | proposed update | Yes | All enumerated queue discrepancies closed without new result claims. |

There are no generated outputs in this retirement manifest.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Manifest canonical digest | `post-run.manifest.json` | Exact Gate 2 binding | Independently recomputed | Pass |
| Ten bound files | Manifest and current tree | Exact snapshot | Every byte count/hash matched | Pass |
| Retired nine-file tree | `invalidation.json`; Git commit `dc7f4d…` | Historical provenance only | Every blob hash and byte count matched | Pass |
| Retired-file-set digest | `invalidation.json` | Detect ledger alteration | Canonical JSON digest independently recomputed | Pass |
| Dated Phase A survivor | README, invalidation record, interpretive pages | Only surviving COMP-019 observation | Search-bounded to 2026-05-08 | Pass |
| Phase B prohibited scope | README and invalidation record | Blocks all numerical/decision reuse | Explicitly enumerated | Pass |
| §1.10 cost/core lanes | Validation dashboard and §1.10 | Planning metadata | Internal cost breakdown and core/optional split agree | Pass |
| §1.20 matrix | Validation §1.20 | Experimental design | Nine factorial conditions plus declared midpoint rule | Pass |
| §1.22 cost/weeks | Dashboard and §1.22 | Planning metadata | Exact equality | Pass |
| §1.25 hosts | Dashboard and §1.25 protocol | Experimental design | Both RIB40 and NSlD-ΔP10 mandatory | Pass |
| `yanthine` | Validation §1.34 | Analyte identity | Li et al., DOI `10.1093/lifemeta/loaf031`, identifies UA reduction to 2,8-dioxopurine (yanthine), experimentally confirmed by LC-MS/co-elution and distinguished from the xanthine route | Pass |
| Dashboard coverage | Validator and validation page | Maintenance guard | 52 dashboard IDs equal 52 numbered sections | Pass |
| Cost/week equality | Validator | Maintenance guard | Exact string comparison for every shared ID | Pass |

Read-only negative-path checks confirmed rejection of missing and orphaned entries, duplicate dashboard rows or sections, malformed row columns, intervening prose before status metadata, absent Cost or Weeks, and either dashboard-side or section-side cost/week drift. A blank Markdown separator between heading and status is intentionally accepted.

## Affected wiki pages

- `wiki/computational-experiments.md` — already consistent — policy and tombstone now agree.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — Git provenance replaces live-artifact wording.
- `wiki/validation-experiments.md` — already consistent — all current COMP-044 planning-maintenance findings are closed.
- `wiki/open-questions.md`, `wiki/gout-action-guide.md`, `wiki/gout-genetic-variants.md`, `wiki/gut-lumen-sink.md`, and H08 — already consistent — no COMP-019 Phase B decision use found.
- `papers/cross-vendor-heterogeneity-guard/draft.md` — already consistent — exact retirement commit replaces the deleted script path.
- `synthesis/queue/comp-review-019.md` — current actions closed; eligible for deletion.
- `synthesis/queue/comp-review-044.md` — current actions closed; eligible for deletion.

## New connections or implications

None beyond the already documented boundary: tombstoning invalidated executable history removes accidental reuse risk while preserving auditable Git provenance. The dashboard guard generalizes the queue correction into a deterministic maintenance invariant.

## Required actions

None.

## Review limits

No COMP experiment or result-bearing code was executed. Review used static inspection, Git object/hash verification, the non-result-bearing dashboard checker, in-memory negative-path mutations, shell/YAML syntax checks, and independent inspection of the cited Life Metabolism primary article. No binary artifact required representation, and no bound file was missing or unreadable.
