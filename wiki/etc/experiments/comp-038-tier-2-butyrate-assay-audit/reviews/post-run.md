ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 8d73b1151b90b3d4e7011f2cf50952dbabb3ef52c5456e8e321e33ec7b9ee007

# Independent comp review — comp-038

## Reviewed snapshot

Reviewer `/root/comp038_gate2_20260728`; authoring-time Gate-2 manifest
`wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/reviews/post-run.manifest.json`.

The canonical manifest digest matched
`8d73b1151b90b3d4e7011f2cf50952dbabb3ef52c5456e8e321e33ec7b9ee007`.
All 16 entries matched their recorded byte counts and SHA-256 hashes and were
inspected completely.

The nine design/shared-dependency entries are identical between the pre-run
and post-run manifests. All six generated-output entries are byte-identical to
the pre-run prior-output baseline. Independent findings were recorded before
prior reviews were consulted.

## Bottom-line verdict

**Clean.** The bounded maintenance repair is scientifically and operationally
faithful. It adds no result-bearing computation, changes no generated output,
guards every legacy mutation mode behind explicit authorization, requires the
controlling verification JSON, and makes the default command read-only.

The sole proposed reader-facing change correctly:

- binds Gu performance to the exact published hardware–chemistry–model stack;
- identifies the 30-sample cohort as within-study rather than external
  replication;
- pairs the high fit statistics with the statistically nonzero negative bias;
- preserves complete-stack reproduction and independent external transfer as
  open;
- narrows the colorimetric conclusion to one reviewed protocol and explicitly
  leaves other future chemistries open.

No scientific, implementation, provenance, or reader-facing correction
remains.

## Implementation and constraint closure

`analyze.py` validates argument state before output-directory creation,
environment loading, source reads, network access, client construction, or
writes.

The current behavior is correctly partitioned:

- Default `python3 analyze.py` requires five regular files, including
  `primary-source-verification-2026-07-24.json`, and returns without reading or
  writing their contents.
- `--prepare-codex` and `--run-openrouter` are mutually exclusive.
- Either legacy mutation mode requires `--regenerate-current-outputs`.
- The authorization flag without a mutation mode is rejected.
- Exact content integrity remains assigned to the SHA-256-bound lifecycle, not
  the presence check.
- Authorized regeneration remains outside this maintenance run and requires a
  fresh reviewed lifecycle. The documented recovery rule rejects mixed
  partial-output states.

Permitted execution results:

- `python3 -m unittest -v test_maintenance.py`: **7/7 passed**.
- Two consecutive default `python3 analyze.py` runs: **exit 0**, each reporting
  that existing outputs were preserved.
- Before/after SHA-256 checks: all six generated outputs were unchanged.
- Pre-run baseline versus post-run generated outputs: no byte-count or digest
  differences.

## Summary-fidelity audit

The unchanged verification JSON, `results.json`, `summary.md`, discovery
packet, and PubMed snapshot retain the existing YELLOW result: no
ready-to-adopt Tier 1 or Tier 2 Open Enzyme butyrate assay; De Baere remains a
Tier 3 culture-supernatant transfer candidate, and Gu remains a separate Tier
2 stool candidate.

Independent review of [Gu et al.’s primary full
text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13114974/) confirmed:

- VBS-100 workstation and disposable G3 planar gold electrodes;
- stool preparation, alkaline butyrate pretreatment, voltammetric acquisition
  and feature extraction, and ANN prediction;
- a within-study 30-sample authentic fecal test cohort compared with GC-MS;
- butyrate MAE/RMSE/R² of 0.029 mM/0.034 mM/0.998;
- bias of −0.015 mM, limits of agreement −0.065 to 0.035 mM, and a
  statistically nonzero bias;
- no public reusable dataset, weights, or implementation package establishing
  external transfer.

The proposed index sentence preserves all load-bearing qualifications.

The colorimetric sentence is also properly bounded. The official [Abcam
ab65341 protocol
v17a](https://content.abcam.com/content/dam/abcam/product/documents/65/ab65341/Free-Fatty-Acid-Assay-protocol-book-v17a-ab65341%20%28website%29.pdf)
states that this kit is not designed to detect short-chain fatty acids such as
acetic, propionic, or butyric acid. Calling this one reviewed protocol a
representative mismatch—and explicitly refusing to generalize it to every
colorimetric chemistry—is faithful.

## Reader-facing ownership audit

`wiki/computational-experiments.md` remains a compact registry entry. It
contains the current verdict, matrix-specific candidates, quantitative
boundary, and links to the owning validation gates without adding maintenance
history or duplicating the focused evidence page.

The unchanged ownership surfaces remain consistent:

- The focused COMP-038 page owns evidence, sourcing, matrices, and
  falsification gates.
- Validation §1.31 owns culture-supernatant HPLC-UV transfer against GC-MS.
- Validation §1.45 owns exact-stack stool reproduction and independent
  transfer.
- The quantification ladder owns Tier 3/Tier 4 classification.
- The genotype-informed workflow and validation §1.14 own the separate
  biological exposure and ABCG2/Q141K questions.

No personalized treatment instruction, clinical recommendation, chassis foil,
or cross-track ranking was introduced.

## Conjecture preservation audit

The maintenance repair does not modify or invalidate biological conjectures.

The owning `wiki/abcg2-modulators.md` page still contains the full Research
Conjecture separating:

1. supported butyrate-associated endogenous ABCG2 induction through PPARγ in
   non-Q141K-specific preclinical systems; and
2. the untested possibility that a measured butyrate exposure could reproduce
   pharmacological Q141K trafficking rescue.

The COMP-007 registry entry likewise preserves the possible combined route as
a Research Conjecture rather than a COMP result. Validation §1.14 retains the
direct butyrate/Q141K surface-trafficking and attributed urate-flux test.

The representative free-fatty-acid protocol exclusion does not kill other
colorimetric approaches, and the lack of a qualified current assay does not
kill the adjacent butyrate biology.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/README.md` | design | Yes | Accurate read-only default, explicit mutation boundary, lifecycle integrity, recovery, and reproducibility contract. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/analyze.py` | design | Yes | Guards execute before all mutable/external paths; default is read-only and requires the controlling JSON. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/maintenance-repair-plan-2026-07-28.md` | design | Yes | Bounded, non-result-bearing plan; acceptance and failure criteria match implementation. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/model-config.json` | design | Yes | Frozen legacy discovery configuration; not represented as current execution evidence. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/primary-source-verification-plan-2026-07-24.md` | design | Yes | Two-source verification scope and prohibited inferences remain explicit. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/provenance.md` | design | Yes | Correctly separates May discovery from July source verification and future scans. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/query-strategy.json` | design | Yes | Frozen bounded search strategy; not presented as exhaustive or newly executed. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/test_maintenance.py` | design | Yes | Seven cases cover read-only behavior, file type/presence, authorization, and mutually exclusive modes. |
| `wiki/etc/experiments/lib/agentic_lit_synthesis.py` | shared_dependency | Yes | No import-time network or filesystem mutation; external/write helpers remain unreachable in reviewed execution. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/.gitkeep` | generated_output | Yes | Harmless legacy placeholder; unchanged and non-evidential. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/codex-synthesis-packet.md` | generated_output | Yes | Frozen abstract-level discovery packet; unchanged and not authority for corrected primary-source claims. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/primary-source-verification-2026-07-24.json` | generated_output | Yes | Unchanged two-source, 18-claim controlling verification map. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/pubmed-snapshot.json` | generated_output | Yes | Unchanged 27-query/74-record title-and-abstract discovery snapshot. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/results.json` | generated_output | Yes | Unchanged structured YELLOW result with separate matrix tracks and prohibited inferences. |
| `wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md` | generated_output | Yes | Unchanged compact summary; full-stack and external-transfer limits retained. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Only Gu scope/bias and representative-colorimetry boundaries change; both are faithful and adjacent content remains intact. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Canonical post-run snapshot | Post-run manifest | Binds complete review scope | Canonical digest and every entry independently checked | Pass |
| Pre/post executable design equality | Pre/post manifests | Preserves Gate-1 authorization | Nine design/shared entries byte-identical | Pass |
| Generated outputs unchanged | Pre-run baseline; post-run generated entries | Establishes non-result-bearing repair | Six byte counts and SHA-256 hashes identical | Pass |
| Default execution is read-only | `analyze.py`; tests; executed default command | Safe artifact presence check | Code inspection, 7 tests, two runs, before/after hashes | Pass |
| Explicit legacy-write authorization | `analyze.py` CLI guards | Prevents silent overwrite | Direct inspection and regression tests | Pass |
| Controlling verification JSON required | `CURRENT_OUTPUT_NAMES`; tests | Prevents incomplete current state from passing | Exact path and missing-file case verified | Pass |
| Gu exact implementation scope | Verification JSON; summary; proposed index | Bounds performance transfer | Primary full text §§2.2–2.8 | Pass |
| Gu within-study test cohort, n=30 | Verification JSON; proposed index | Prevents external-replication inflation | Primary full text §§3.3–3.4 | Pass |
| Gu MAE/RMSE/R² 0.029/0.034/0.998 | Verification JSON; proposed index | Quantitative performance summary | Primary full text Table 3/Figure 5 | Pass |
| Gu bias −0.015 mM, statistically nonzero | Verification JSON; proposed index | Prevents R²-only interpretation | Primary full text §3.3 and supplementary comparison | Pass |
| Representative colorimetric mismatch | Proposed index | Rejects one unsuitable protocol without class-wide exclusion | Abcam ab65341 v17a vendor protocol | Pass, protocol-specific only |
| No ready Tier 1/2 OE assay | Results, summary, registry | Current COMP verdict | Bounded scan and matrix-specific qualification state | Pass with existing YELLOW boundary |
| Adjacent butyrate–ABCG2 conjecture survives | ABCG2 owner, COMP-007 registry, validation §1.14 | Preserves useful untested connection | Direct corpus inspection | Pass |

## Affected wiki pages

- `wiki/computational-experiments.md` — proposed change is complete and
  faithful.
- `wiki/tier-2-butyrate-assay-audit-computational.md` — already consistent;
  owns current evidence and falsification gates.
- `wiki/validation-experiments.md` — already consistent; §1.31 and §1.45
  remain separate.
- `wiki/quantification-ladder.md` — already consistent; HPLC-UV remains Tier
  3.
- `wiki/open-questions.md` — already consistent; preserves the matrix-specific
  measurement gap.
- `wiki/genotype-informed-supplement-workflow.md` — already consistent; direct
  butyrate Q141K rescue remains unvalidated.
- `wiki/abcg2-modulators.md` — already consistent; adjacent dual-route Research
  Conjecture remains intact.

## New connections or implications

The repair reinforces one operational distinction: artifact-presence
verification, cryptographic artifact integrity, and scientific source
verification are separate controls and should remain separate.

For Gu transfer, “complete stack” materially includes electrode/workstation
choice, stool preparation, alkaline chemistry, acquisition, feature
extraction, and the locked ANN—not merely a nominal electrochemical sensor.

No new scientific conjecture or synthesis-queue item follows from this
maintenance review.

## Required actions

None. The prior push-review actions are closed:

1. Gu identifier/link hygiene is corrected on the focused and validation
   pages.
2. Legacy mutation modes now require explicit authorization.
3. The controlling verification JSON is required by default.
4. The propagated Gu performance summary now includes exact-stack scope,
   within-study n=30, statistically nonzero bias, and absent external transfer.
5. The colorimetric exclusion is explicitly representative rather than
   universal.

## Review limits

No files were edited. Neither mutation mode, result regeneration, model call,
nor networked discovery workflow was executed.

The repository-wide test suite was not run because the assignment limited
execution to the local maintenance tests and default `analyze.py`. Gu’s model
was not reproduced; the primary full text was independently inspected for
source fidelity. De Baere remains verified only at accessible primary-abstract
scope. The Abcam protocol was checked only to assess the bounded colorimetric
sentence, not to perform a broader vendor landscape scan.

Prior review receipts were inspected only after independent artifact, source,
affected-surface, and conjecture findings had been recorded.
