---
title: "Agentic Search and Computational-Experiment Boundary"
date: 2026-05-20
status: active
tags: [operational, methodology, agentic-search, comp-nnn, literature]
related:
  - ../wiki/etc/autonomous-screening-methodology.md
  - ../skills/lit-scan/SKILL.md
  - ../skills/new-comp-experiment/SKILL.md
  - ../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/
sources:
  - "Ghareeb et al. 2026 — Robin: A multi-agent system for automating scientific discovery — doi:10.1038/s41586-026-10652-y"
  - "Google DeepMind 2025 — Towards an AI co-scientist — arXiv:2502.18864"
  - "FutureHouse 2024 — PaperQA2 / Aviary — arXiv:2409.13740; arXiv:2412.21154"
---

# Agentic Search and Computational-Experiment Boundary

## Current decision

Use agentic search to find evidence, expose blind spots, and nominate testable
leads. Do not treat search consensus, model voting, or candidate ranking as
experimental validation.

- **Literature-only work routes through
  [`lit-scan`](../skills/lit-scan/SKILL.md).** It updates canonical wiki pages
  and leaves one compact method receipt with exact queries, sources attempted,
  counts, failures, translation checks, and claim verification status.
- **Executable scientific models route through
  [`new-comp-experiment`](../skills/new-comp-experiment/SKILL.md).** A COMP
  requires frozen inputs, implementation, decision rules, outputs, and
  independent pre- and post-run review.
- **Git is the archive.** Current files hold current evidence and operating
  rules, not append-only retrospectives or superseded narratives.

This boundary keeps literature work source-centered and COMPs
computation-centered. A ranked literature result may motivate a COMP or wet-lab
experiment, but ranking does not change the evidence tier.

## Patterns worth retaining

### Multiple trajectories as sensitivity

Independent trajectories can reveal prompt-sensitive omissions or assumptions.
Report the variation when it affects a decision. Multiple trajectories from
one model and one source packet are not independent scientific replication and
must not be described as such.

Use additional models or reviewers when their independence is decision-relevant
and worth the cost. Do not multiply calls merely to create a vote count.

### Pairwise comparison after evidence qualification

Pairwise comparison can be more stable than free-form numeric scoring when
the candidate properties are already source-qualified and the comparison rule
is explicit. It cannot calibrate invented coefficients, repair missing
properties, or turn heterogeneous evidence into a biological winner.

Keep component evidence visible. A tournament rank is a triage device unless
it has been validated against the outcome it predicts.

### Shallow versus deep search

Use a bounded triage scan to decide whether a thread deserves a deeper source
read. Once a claim becomes load-bearing, inspect the primary source and record
its exact access scope.

“Full text” is a source-access status, not a quality adjective. An abstract,
publisher metadata page, supplementary table, preprint, and complete article
must not be collapsed into one label.

### Search-to-experiment handoff

Search may:

- identify a method, target, mechanism, delivery route, or source;
- establish published parameters within their reported matrix and design;
- preserve a grounded Research Conjecture and its cheapest discriminating
  observation.

Search may not:

- establish local reproducibility, matrix transfer, dose, efficacy, or safety;
- substitute a published source-study cohort for independent external
  replication;
- imply that failure to find evidence proves biological impossibility;
- declare an entire project blocked because one lower-cost assay is absent.

If no lower-tier assay is validated for an exact analyte and matrix, a Tier 3
method can be used directly. The consequence is cost and access, not automatic
failure of every downstream research track.

## COMP-038 lesson

COMP-038 began as a 27-query, 74-record PubMed abstract scan with five
in-session Codex trajectories. That structure was useful for candidate
discovery, but it exposed why literature synthesis is no longer a COMP
sub-type:

1. the executable runner captured discovery metadata, not the later
   primary-source reads;
2. a narrative addendum claimed a full-text pass without a source-read
   artifact;
3. the structured result, summary, provenance, and downstream pages drifted;
4. HPLC-UV was initially mislabeled as Tier 2 even though the equipment
   ceiling makes it Tier 3;
5. one paper’s within-study test cohort was at risk of being described as
   independent external validation.

The corrected artifact keeps the useful result:

- De Baere et al. supports a Tier 3 HPLC-UV culture-supernatant
  method-transfer candidate at primary-abstract scope.
- Gu et al. supports a separate Tier 2 electrochemical/ANN stool candidate at
  full-text scope.
- Neither is qualified for an Open Enzyme workflow.

The source-specific repair and matrix-specific gates live in the
[Butyrate Measurement Audit](../wiki/tier-2-butyrate-assay-audit-computational.md).

## Operating checklist

For a literature question:

1. Define the decision and claim boundary.
2. Run multilingual search frames appropriate to the domain.
3. Record exact queries, sources, failures, and translation checks.
4. Verify load-bearing claims in primary sources.
5. Write findings once in the canonical wiki page.
6. Leave a compact method receipt under `logs/lit-scans/`.
7. Propagate only to direct dependents.

For an executable model:

1. Freeze the question, inputs, provenance, code, parameters, decision rules,
   sensitivity plan, and output contract.
2. Pass context-isolated Gate 1.
3. Execute the frozen design.
4. Reconcile generated output and every proposed interpretation.
5. Pass context-isolated Gate 2.
6. Let current push review bind the committed artifact and active dependents.

The reusable evidence and screening rules are maintained in
[Autonomous AI Screening Methodology](../wiki/etc/autonomous-screening-methodology.md).
