# COMP-048 — Human proximal-tubule surface-candidate screen

**Status:** Pre-run design only. Do not execute until the exact Gate 1 receipt
says `PRE_RUN_GATE: GO`.

## Decision

Does the frozen human surface-protein universe contain one or more proteins
whose RNA co-occurs with `SLC22A12`-positive proximal-tubule cells across
reference donors, whose kidney and cross-tissue expression is sufficiently
selective under preregistered gates, and whose surface/topology evidence is
strong enough to justify candidate-specific receptor, internalization, and
polarity work?

This asks whether a surface-expression/topology **follow-up candidate** exists
in the screened data. It does not establish receptor status, ligand binding,
internalization, accessibility, or a working delivery handle.

## Why this replaces guide-first screening

Plausible guide windows do not resolve the upstream delivery bottleneck. This
COMP moves the first computational decision to the human surface-candidate
problem. Guide design remains downstream of a validated delivery route.

## Frozen inputs

- Lake et al. integrated adult human kidney single-cell/single-nucleus atlas,
  fixed CELLxGENE dataset version: donor-level target coverage, kidney
  off-target expression, condition and assay sensitivity.
- Bausch-Fluck et al. human surfaceome supplement: fixed candidate universe,
  surface-evidence class, extracellular topology prior.
- Human Protein Atlas 25.1 cell-type RNA, tissue RNA, and normal-tissue IHC:
  cross-cell-type, systemic-tissue, and protein-localization axes.
- `inputs/controls.tsv`: ASGR1/ASGR2 positive-pattern control; kidney-context,
  target-marker, and negative-surface controls.

Exact identities and checksums live in `inputs/source-manifest.json`.

## Analysis contract

### Candidate universe

Only genes labelled `surface` in Bausch-Fluck sheet `11.7_Surfaceome` enter the
screen. The computation preserves whether support came from direct CSPA,
curated positive-training, or machine-learning evidence. Candidates must have
at least 20 annotated noncytoplasmic residues to pass the topology prior.

### Donor-level expression

The target compartment is an atlas proximal-tubule cell with nonzero
`SLC22A12` expression. Reference donors require at least 20 proximal-tubule
cells and at least five target-positive cells. Candidate detection is computed
per donor in target-positive proximal tubule, target-negative proximal tubule,
and non-proximal-tubule cells. Donors, assays, specimens, and disease conditions
are never collapsed before their sensitivity outputs are written.

### Separate axes

The output keeps these axes separate:

1. target-cell coverage and donor robustness;
2. other-kidney-cell expression;
3. HPA cross-cell-type and cross-tissue expression;
4. direct versus predicted surface evidence;
5. noncytoplasmic topology;
6. HPA IHC protein localization;
7. AKI/CKD stability; and
8. candidate-specific internalization and membrane-polarity evidence.

Axis 8 is `unknown` for an uncurated candidate. Endosome annotation, a cytoplasmic
tail, or the word “receptor” cannot fill it.

### Hard gates and sensitivity

All primary thresholds, eligible-donor rules, method controls, and permissive
and stringent sensitivity sets are frozen in `inputs/design-rules.json`.
Thresholds are engineering decision rules, not biological constants. The
primary gate requires donor coverage, kidney selectivity, HPA cell-type and
tissue selectivity, and the surface/topology prior. Protein localization,
disease stability, surface-evidence class, and internalization evidence are
reported independently and control what follow-up is allowed.

### Pareto output

Candidates passing each threshold set are reduced to nondominated Pareto sets.
No weighted sum, average rank, or declared winner is permitted. A candidate
cannot compensate for broad systemic expression by scoring highly on target
coverage.

## Controls and failure branches

- ASGR1/ASGR2 must reproduce hepatocyte and liver enrichment in HPA and appear
  in the surfaceome. Failure makes the cross-tissue/surface method
  uninterpretable.
- ALB and GAPDH must not enter the transmembrane surfaceome universe.
- `SLC22A12` must be detected above the frozen donor sufficiency rule.
- LRP2/CUBN are proximal-tubule context controls, not expected winners.
- A missing `SLC22A12` mapping, duplicate surfaceome genes, duplicate kidney
  observation or feature IDs, missing donor IDs, zero eligible reference
  donors, incompatible schema, failed checksums, or a failed control produce
  `METHOD_FAILURE`, not a negative biological result. Multiple exact
  Ensembl-ID matches for one symbol are retained as a union under the frozen
  mapping policy. Unresolved candidate mappings are reported as technical
  missingness, enter the completeness threshold, and always block a
  zero-candidate biological negative.

Each gene is resolved once. When a surfaceome row supplies one or more Ensembl
IDs, every supplied ID must exist in the kidney atlas and all are used; a
partial subset and symbol fallback are prohibited. Exact `feature_name` symbol
matching is used only when that row supplies no Ensembl ID. `SLC22A12` reuses
its surfaceome-row mapping when present and receives a separate symbol lookup
only when absent from the frozen surfaceome.

For every mapped candidate, each HPA RNA axis records whether any data exist,
whether the required target category (`proximal tubule cells` or `kidney`)
exists, whether at least one non-target comparison category exists, and the
reason a ratio is undefined. A zero-candidate run cannot emit the bounded
negative branch while any candidate has incomplete HPA ratio inputs.

Possible result branches are:

- `METHOD_FAILURE`;
- `SCREEN_INCOMPLETE_TECHNICAL_MISSINGNESS`;
- `NO_SURFACE_EXPRESSION_TOPOLOGY_CANDIDATE_AT_PRIMARY_GATES`; or
- `SURFACE_EXPRESSION_TOPOLOGY_CANDIDATES_NEED_RECEPTOR_INTERNALIZATION_AND_POLARITY_VALIDATION`.

No preferred branch is embedded.

## Planned outputs

- `outputs/results.json` — verdict, controls, gates, sensitivity counts, full
  axis values, Pareto membership, missingness, and failure states.
- `outputs/candidates.csv` — one row per frozen surfaceome candidate.
  Unresolved candidates retain their mapping status and failure reason with
  computed axes blank and every gate false; no composite score is present.
- `outputs/donor-metrics.csv` — pooled donor-level denominators and detection
  metrics, including target-negative proximal-tubule diagnostics.
- `outputs/stratum-metrics.csv` — donor × assay × specimen × condition
  denominators and detection metrics written before the declared donor pooling.
- `outputs/controls.json` — exact control observations and pass/fail reasons.
- `outputs/missingness.json` — mapping coverage, candidate-level presence of
  any HPA data, the required proximal-tubule and kidney categories, non-target
  comparison categories, per-axis reason codes, label conflicts, and any
  technical condition that blocks a negative verdict.
- `outputs/summary.md` — branch-controlled human summary and explicit nonclaims.
- `outputs/run-manifest.json` — input checksums and dependency versions.

An exception before the complete audit finishes clears stale outputs and
writes only the five minimal files frozen under
`failure_output_contract.preflight_exception`. A method-control failure found
after the candidate, donor, stratum, control, and missingness audits finish
writes the full eight-file set under
`failure_output_contract.completed_audit`, marks the run manifest
`METHOD_FAILURE_COMPLETED_AUDIT`, exits nonzero, and permits no biological
interpretation. The two failure classes therefore preserve different amounts
of diagnostic evidence without sharing an ambiguous output contract.

## Reproduction after Gate 1

```bash
cd wiki/etc/experiments/comp-048-human-proximal-tubule-delivery-handle-screen
python3.11 -c 'import sys; assert sys.version.split()[0] == "3.11.9"'
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.lock.txt
.venv/bin/python -c 'import sys; assert sys.version.split()[0] == "3.11.9"'
python3 ../../../../scripts/comp-review-manifest.py check \
  --manifest reviews/pre-run.manifest.json \
  --review reviews/pre-run.md \
  --required-line 'PRE_RUN_GATE: GO'
.venv/bin/python fetch_inputs.py
python3 ../../../../scripts/comp-review-manifest.py check \
  --manifest reviews/pre-run.manifest.json \
  --review reviews/pre-run.md \
  --required-line 'PRE_RUN_GATE: GO'
.venv/bin/python analyze.py
```

Fetched inputs and temporary output staging live only under
`.comp-runtime-env/`. That runtime cache is canonically excluded by the
snapshot tool's `*-env` rule, while `fetch_inputs.py` and `analyze.py`
independently verify every source byte count and SHA-256 against the bound
source manifest. The second manifest check demonstrates that fetching did not
alter the reviewed design.

Run `analyze.py` twice from clean `outputs/` directories and require identical
SHA-256 values for all planned outputs before Gate 2.

## Planned authoring boundary

The canonical result home will be
`wiki/proximal-tubule-surface-candidate-computational.md`. The future post-run
manifest must bind that page and every planned dependent exactly:

- `index.md`;
- `operations/todos.md`;
- `wiki/chassis-pending-interventions.md`;
- `wiki/computational-experiments.md`;
- `wiki/delivery-route-matrix.md`;
- `wiki/hypotheses/H03-sirna-urat1-thesis.md`;
- `wiki/open-questions.md`;
- `wiki/sirna-urat1-modality.md`;
- `wiki/urat1-sirna-target-site-selection-computational.md`; and
- `wiki/validation-experiments.md`.

The canonical and modality pages may carry only the local surface-expression
and topology result. Cross-route implications belong only in the delivery
matrix or other portfolio surfaces. A negative result narrows candidate
availability within the frozen surfaceome, datasets, mappings, and thresholds.
It does not establish receptor absence or kill URAT1, siRNA, other
kidney-targeting chemistries, urinary-side delivery, nanoparticles, or the gout
mission.

No creation-date narrative, candidate winner, delivery claim, guide claim,
clinical recommendation, dose, safety claim, or efficacy claim may be authored
from this computation.
