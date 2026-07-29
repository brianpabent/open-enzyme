# COMP-016 — bounded androgen × intestinal ABCG2 evidence inventory

## Biological question

Within the fixed 17-record inventory collected on 2026-05-07, did any record
directly demonstrate that androgen exposure or androgen-state manipulation
decreases intestinal ABCG2?

This is a bounded inventory test, not a current or systematic literature
review. It cannot establish that no such study exists outside the committed
search set.

## Decision

The computation decides whether the old direct-suppression mechanism may remain
as a demonstrated premise in Open Enzyme. It does not decide:

- the broader androgen–urate relationship;
- healthy-human intestinal ABCG2 sex stratification;
- a male-specific ceiling on gut-lumen urate export;
- physiological effects from nominal cell-culture exposures; or
- clomiphene mechanism, dosing, or treatment.

[COMP-017](../comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/)
owns the corrected Hoque, Liu, Slepnev, and MacLean source record and the
unresolved healthy-human question.

## Model and decision rules

`analyze.py` validates and renders `inputs/studies.json`; it performs no
retrieval or statistical inference.

A record is a **direct in-vivo test** only when it both manipulates androgen
exposure/state and measures intestinal ABCG2 in vivo. A record is a **direct
in-vitro test** only when it manipulates androgen exposure and measures ABCG2
in an intestinal cell model. In either class, the target outcome must be
explicitly linked to the same tested manipulation and model context, the record
must be citable, and the outcome must be verified against primary full text,
an official publisher abstract, or a primary database abstract. A legacy
search summary or unresolved placeholder cannot produce a demonstrated result.
Direct suppression is demonstrated within a tested context only when the
recorded target outcome is `decrease`.

Animal genotype/sex comparisons, healthy-baseline sex comparisons, renal or
systemic urate endpoints, non-intestinal cancer-cell mechanisms, and reviews
remain adjacent evidence. They may motivate a new experiment, but they do not
satisfy the direct-test rule.

The output status is:

- `DIRECT_SUPPRESSION_DEMONSTRATED_IN_FIXED_INVENTORY` if one or more direct
  target tests record a decrease; or
- `NOT_DEMONSTRATED_IN_FIXED_INVENTORY` otherwise.

The second status is bounded to these inputs. It is not a universal absence
claim and does not prove the opposite mechanism.

## Fixed inputs and source boundary

- `inputs/studies.json` retains all 17 original inventory rows, with corrected
  attribution and explicit source-verification tiers.
- Four load-bearing source records were corrected from the primary or official
  abstract record: Hoque 2020, Liu 2021, Slepnev 2023, and MacLean 2008.
- Records supported only by the old search-summary extraction carry no
  quantitative or mechanistic finding in this repaired artifact.
- The vague legacy `S15` row is retained as an unresolved inventory trace but
  excluded from citable evidence because the original row lacked a stable
  author and article identity.
- `inputs/provenance.md` preserves exact queries, access failures, correction
  sources, and the scope not searched.

## Planned outputs

- `outputs/results.json` — validated counts, record classifications, corrected
  source findings, bounded result, and forbidden inferences.
- `outputs/summary.md` — compact human-readable inventory and evidence boundary.

## Reproduction

From the repository root:

```bash
python3 wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/analyze.py
```

The script uses only the Python standard library. A valid maintenance run must
produce byte-identical outputs on two consecutive executions. The reviewed
runtime is CPython 3.14.5. The renderer uses UTF-8 and explicit LF newlines,
uses no randomness, and calls no external service.

From the repository root, the exact two-run check is:

```bash
python3 wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/analyze.py
shasum -a 256 \
  wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/results.json \
  wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/summary.md \
  > /tmp/comp-016-run-1.sha256
python3 wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/analyze.py
shasum -a 256 \
  wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/results.json \
  wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/summary.md \
  > /tmp/comp-016-run-2.sha256
diff -u /tmp/comp-016-run-1.sha256 /tmp/comp-016-run-2.sha256
```

## Falsification and revision boundary

The fixed-inventory result changes if a source-backed correction shows that an
included record directly measured androgen manipulation, intestinal ABCG2, and
a decrease in the same tested context. A new literature search, new record, or
new direct-human dataset is a new result-bearing lifecycle, not an edit to this
run.

The narrow result may reject the old direct-suppression premise. It cannot
reject the broader androgen–urate prior or the research value of measuring
intestinal ABCG2 response directly.

## Downstream authoring set

No external reader-facing text change is proposed by this run: the correction
cascade already brought the current pages inside the repaired boundary. Gate 2
must nevertheless bind and inspect these exact current interpretation
surfaces:

- `wiki/t-abcg2-suppression-evidence-mining-computational.md` — historical
  bounded-scan result;
- `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` —
  current corrected source-evidence home;
- `wiki/computational-experiments.md` — COMP registry;
- `wiki/abcg2-modulators.md` — mechanism boundary;
- `wiki/androgen-urate-axis.md` — broader androgen–urate prior;
- `wiki/open-questions.md` — unresolved measurement question; and
- `wiki/etc/manual-literature-mining.md` — method example and source-tier
  boundary.

[Testosterone × intestinal ABCG2 suppression — bounded evidence
scan](../../../t-abcg2-suppression-evidence-mining-computational.md)
