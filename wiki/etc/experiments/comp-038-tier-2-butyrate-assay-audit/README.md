# COMP-038 — Butyrate Measurement Audit

**Status:** YELLOW. The 2026-05-20 run was an abstract-level literature audit. The newly dated forensic source verification under
[`inputs/primary-source-verification-plan-2026-07-24.md`](./inputs/primary-source-verification-plan-2026-07-24.md)
corrects an unsupported July claim that both leading candidates had been
full-text verified. Its current result is recorded in
[`outputs/primary-source-verification-2026-07-24.json`](./outputs/primary-source-verification-2026-07-24.json).

## Question

Which accessible methods could quantify butyrate in culture supernatant,
stool, serum, or breath, and what validation would each matrix require?

## Current decision boundary

- No ready-to-adopt Tier 1 or Tier 2 butyrate assay has been established for
  Open Enzyme.
- De Baere et al. 2013 is a Tier 3 HPLC-UV culture-supernatant
  method-transfer candidate.
- Gu et al. 2026 is a separate Tier 2 electrochemical/ANN stool candidate.
- Neither source validates an Open Enzyme matrix, workflow, operator, or
  intervention study.
- Culture-supernatant transfer is specified in
  [validation §1.31](../../../validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms).
  Stool-stack reproduction and independent transfer are specified in
  [validation §1.45](../../../validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate).

## Artifact chronology

### 2026-05-20 — original run

The legacy `analyze.py` workflow executed 27 PubMed queries, captured 74
title/abstract records, and produced five in-session Codex synthesis
trajectories. It made no OpenRouter calls. The result was YELLOW: useful
candidate directions surfaced, but no method was ready for adoption.

The dated discovery inputs remain:

- [`inputs/query-strategy.json`](./inputs/query-strategy.json)
- [`inputs/model-config.json`](./inputs/model-config.json)
- [`outputs/pubmed-snapshot.json`](./outputs/pubmed-snapshot.json)
- [`outputs/codex-synthesis-packet.md`](./outputs/codex-synthesis-packet.md)

### 2026-07-15 — unsupported addendum

An addendum labeled “2026-07-14” was appended manually to
`outputs/summary.md`. Git history and the committed artifact do not contain a
July 14 full-text retrieval, extraction, or verification record. The addendum
therefore cannot establish that both papers were full-text verified.

### 2026-07-24 — corrective source verification

The completed repair is a targeted source read of the two named primary
papers, not a new assay-landscape search. Its compact claim-to-source map
controls the current summary and structured result. Unsupported details are
retracted rather than inferred.

## Reproduction and maintenance

The default `python3 analyze.py` command is a read-only required-file check. It
requires each expected output to be a regular file: the discovery snapshot,
synthesis packet, current structured result, current summary, and the
controlling 2026-07-24 primary-source-verification JSON. Exact content
integrity is enforced by the SHA-256-bound COMP lifecycle command below.

The legacy discovery modes cannot reproduce the later primary-source
verification. `--prepare-codex` and `--run-openrouter` therefore refuse to
proceed unless they are paired with `--regenerate-current-outputs`. That
explicit flag prevents accidental replacement; it does not make regenerated
outputs eligible without a new reviewed lifecycle. The bounded repair design
is recorded in
[`inputs/maintenance-repair-plan-2026-07-28.md`](./inputs/maintenance-repair-plan-2026-07-28.md).

Future literature updates route through the repository's `lit-scan` workflow
with a compact method receipt; they do not append narratives to this artifact.

The bounded maintenance checks use CPython 3.14.5 and the Python standard
library plus the manifest-bound repository helper
`wiki/etc/experiments/lib/agentic_lit_synthesis.py`. They do not require a
random seed, environment secret, network service, or model endpoint because
the reviewed commands must stop before those paths. From this directory:

```bash
python3 -m unittest -v test_maintenance.py
python3 analyze.py
python3 analyze.py
```

Each command must exit 0. From the repository root,
`python3 -m unittest discover -s tests` must also exit 0. The exact no-mutation
check is `git diff --exit-code -- wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs`
before and after the two default runs.

Authorized regeneration is intentionally outside this maintenance run. Before
any future use, the outputs directory must match a committed, reviewed
snapshot. If an authorized regeneration fails after a partial write, discard
the entire outputs-directory working-tree delta and restore that committed
snapshot before retrying; never retain or interpret a mixed output set.

Current artifact integrity is checked through the exact-snapshot COMP
lifecycle:

```bash
python3 scripts/comp-review-manifest.py check-lifecycle \
  --comp-dir wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit
```

## File index

```text
comp-038-tier-2-butyrate-assay-audit/
├── README.md
├── analyze.py
├── test_maintenance.py
├── inputs/
│   ├── model-config.json
│   ├── maintenance-repair-plan-2026-07-28.md
│   ├── primary-source-verification-plan-2026-07-24.md
│   ├── provenance.md
│   └── query-strategy.json
├── outputs/
│   ├── codex-synthesis-packet.md
│   ├── primary-source-verification-2026-07-24.json
│   ├── pubmed-snapshot.json
│   ├── results.json
│   └── summary.md
└── reviews/
```

## Canonical interpretation

- [Butyrate Measurement Audit](../../../tier-2-butyrate-assay-audit-computational.md)
- [Computational Experiments](../../../computational-experiments.md)
- [Quantification Ladder](../../../quantification-ladder.md)
- [Validation Experiments](../../../validation-experiments.md)
