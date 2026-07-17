---
title: Scientific Linter Design
date: 2026-04-24
tags: [methodology, falsification, quality-control, automation]
---

# Scientific Linter Design

Two complementary linters apply rigor at different stages without constraining hypothesis generation.

| Linter | Trigger | Scope | Output | Enforcement |
|---|---|---|---|---|
| **Document Lint** | Every changed research document | Structure, provenance, links, evidence labels, and claim calibration | Findings with rule ID, severity, location, and suggested fix | Advisory by default; selected structural rules may block publication |
| **Falsification Lint** | On demand for a committed hypothesis | Assumptions, kill tests, thresholds, failure modes, and retraction state | A versioned Falsification Card | Review gate for hypothesis promotion, not for ideation |

## Design principles

1. **Generation remains unconstrained.** Lint applies after an idea is written or committed as a hypothesis.
2. **Rules are explicit and versioned.** Each finding names the rule and rule version that produced it.
3. **Severity reflects consequence.** Structural invalidity, unsupported load-bearing claims, and broken provenance rank above style.
4. **Findings are actionable.** A finding identifies the affected text and the smallest defensible correction.
5. **Automation does not replace scientific judgment.** Semantic findings remain reviewable and may be dismissed with a recorded rationale.
6. **Git provides artifact identity.** Store the reviewed commit SHA with every lint result and Falsification Card.

## Document Lint

### Output contract

Each finding contains:

```yaml
rule_id: evidence-tag-required
rule_version: 1.0
severity: error
file: wiki/example.md
line: 42
message: Quantitative intervention claim lacks an evidence-level tag.
suggested_fix: Add Clinical Trial, Animal Model, In Vitro, or Mechanistic Extrapolation.
```

### Rule catalog

| Rule ID | Severity | Check |
|---|---|---|
| `evidence-tag-required` | Hard | Empirical or mechanistic claims carry an evidence-level tag. |
| `inline-provenance` | Soft | Load-bearing claims identify a source near the claim. |
| `cross-ref-resolves` | Hard | Relative Markdown links resolve. |
| `mkdocs-nav-coverage` | Hard | Published pages are represented in navigation when required. |
| `chokepoint-label-v1.2` | Soft | Chokepoint labels use the current vocabulary. |
| `species-gap-caveat` | Soft | Cross-species extrapolations state the gap. |
| `no-inline-revision-history` | Hard | Research pages do not carry Git-owned revision narratives. |
| `frontmatter-complete` | Hard | Required frontmatter fields are present and parseable. |
| `standard-markdown-links` | Style | Externally shared pages use standard Markdown links. |
| `claim-calibration` | Soft | Wording does not exceed the cited evidence level. |
| `orphan-page` | Soft | New pages have an inbound link or index entry. |
| `duplicate-frontmatter-date` | Style | Metadata does not duplicate revision history in prose. |

Regex or parser-based rules should run first. Semantic rules should operate only on changed claim-bearing passages to control cost and reduce false positives.

## Falsification Lint

The Falsification Lint creates or evaluates one card per committed hypothesis.

### Card schema

```yaml
---
id: H00
title: Short falsifiable hypothesis
committed: <git-sha>
status: active        # active | weakened | retracted | survived
survival_count: 0
---

## Claim

## Assumption stack

## Killshot menu

## Failure-mode references

## Quantitative thresholds

## Kill switches

## Test log

## Survival score

## Retraction history
```

### Killshot prioritization

Rank candidate tests by expected information gained per unit cost and delay:

\[
\text{priority} = \frac{P(\text{kill}) \times \text{information weight}}
{\text{cost} \times \text{time penalty}}
\]

The probabilities are explicit judgment calls, not measured frequencies. Their value is comparative: they reveal why one test precedes another.

### Failure-mode ontology

1. **Species gap** — evidence in one species does not transfer to the target species.
2. **Chokepoint collapse** — the targeted mechanism is not rate-limiting in the intended context.
3. **Assay specificity** — the assay readout does not uniquely measure the proposed mechanism.
4. **Substrate or compartment mismatch** — substrate, oxygen, pH, localization, or tissue context differs from the assumed regime.
5. **Expression or localization failure** — the construct is not expressed, folded, secreted, or retained where required.
6. **Kinetics or concentration failure** — achievable exposure does not reach the mechanistically relevant range.
7. **Dose-translation failure** — animal or in-vitro exposure does not support the proposed human exposure.
8. **Purity or formulation failure** — the tested material differs materially from the intervention being interpreted.
9. **Literature or training-distribution gap** — the evidence search missed relevant sources, terminology, languages, or negative results.

Cards should link failure modes rather than redefine them, so related hypotheses can be compared across the same vocabulary.

### Test independence

Repeated tests add less information when they share assumptions. A simple overlap diagnostic is Jaccard similarity:

\[
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
\]

where \(A\) and \(B\) are the assumption sets exercised by two tests. High overlap should reduce the second test's information weight.

### Survival score

A card may summarize accumulated evidence with a time-decayed score:

\[
S = \sum_i w_i \times o_i \times e^{-\lambda t_i}
\]

where \(w_i\) is test weight, \(o_i\) is the signed outcome, \(t_i\) is evidence age, and \(\lambda\) is a declared decay constant. The score is a navigation aid, not a posterior probability. A prespecified kill switch overrides the aggregate score.

### Calibration and retraction

- Define thresholds before observing the result when practical.
- Record null and adverse results with the same detail as supportive results.
- Treat a weakened hypothesis as distinct from a retracted one.
- Preserve the prior claim and reason for retraction in the card's retraction history; use Git for document-level revision history.
- Reopen a survived hypothesis when a new, materially independent failure mode appears.

## N-of-1 evidence

The linter may improve an N-of-1 design but cannot remove confounding, regression to the mean, expectancy effects, or uncontrolled co-interventions. Cards should distinguish exposure verification, target engagement, and clinical outcome; a change in one does not establish the others.

## Boundaries

Document Lint does not judge whether a hypothesis is scientifically important. Falsification Lint does not generate hypotheses, certify safety, or turn a passed test into clinical evidence. Neither substitutes for primary-source verification, independent review, or appropriate ethical and regulatory oversight.

## Implementation questions

- Which hard rules block publication versus create advisory findings?
- What false-positive rate is acceptable for semantic claim calibration?
- Which ontology changes require migration of existing cards?
- What minimum independent-test set is required before a hypothesis may be labeled `survived`?
- How should dismissed findings be sampled for periodic quality review?
