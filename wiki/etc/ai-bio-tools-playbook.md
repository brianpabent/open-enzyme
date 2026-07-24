---
title: "AI Biology Tools — Evidence-Bounded Playbook"
date: 2026-04-21
tags: [AI, biology, protein-design, computational-methods, evidence]
related:
  - ../computational-experiments.md
  - autonomous-screening-methodology.md
  - manual-literature-mining.md
  - ../validation-experiments.md
sources:
  - "Hugging Science resource index: https://huggingscience.co/llms.txt"
  - "Hugging Science biology topic file: https://huggingscience.co/topics/biology.md"
  - "Hugging Science chemistry topic file: https://huggingscience.co/topics/chemistry.md"
---

# AI Biology Tools — Evidence-Bounded Playbook

**Phase:** Phase 0 — Research & Design

AI tools can help Open Enzyme search a large design space, expose disagreement, and choose the next falsifying experiment. They do not establish a biological mechanism, physiological exposure, human dose, serum effect, safety margin, production sufficiency, or winning chassis.

The mission is to use red-teaming techniques to identify exploitable weaknesses in gout and use creative engineering to exploit them. Protein design, microbial engineering, transporter modulation, local delivery, and compound discovery are separate candidate tracks. Tool choice follows the decision under study; no tool or chassis defines the project.

## Decision Contract

Before using a model, record:

1. the gout weakness being tested;
2. the exact claim the run may support;
3. the source-bound inputs and their evidence levels;
4. the search space, exclusions, controls, and decision rule;
5. the empirical observation that would advance, redirect, or kill the hypothesis; and
6. conclusions the run is not permitted to make.

If the task cannot be written this way, it is not ready for result-bearing computation.

## Capability Map

| Question | Candidate computational role | Required empirical boundary |
|---|---|---|
| Which sequence variants should enter a small matched panel? | conservation, sequence-likelihood, and stability priors | exact construct identity, active expression, and direct biochemical comparison |
| Does a construct appear structurally plausible? | structure or complex prediction | prediction confidence is not folding, localization, oligomerization, binding, or activity |
| Which residues or junctions deserve inspection? | cleavage-site, disorder, motif, and accessibility hypotheses | measured structure or exposure where the property is load-bearing; then the relevant activity assay |
| Which cassette designs should be built first? | codon, RNA, promoter, signal-peptide, and burden ranking | sequence-verified build plus transcript, total/soluble/active protein, localization, and host-effect measurements |
| Which compounds deserve a first assay? | target, docking, affinity, and ADMET triage | direct target assay, gout-relevant cellular assay, exposure, selectivity, and safety evidence |
| Which public data might answer a question? | catalog and dataset discovery | license, provenance, population, assay, leakage, and benchmark-fit review |
| Which literature claim is credible? | multilingual retrieval and contradiction search | primary-source inspection and the repository's translation and grep-verification rules |

[Hugging Science](https://huggingscience.co/) is one routing index for open datasets and models. A catalog entry is a lead, not evidence that a model is suitable for an Open Enzyme decision.

## Evidence Rules

### Predictions are priors

- A structure prediction is a coordinate hypothesis.
- A confidence score is not a measurement of solvent exposure or protease resistance.
- A docking score is not binding affinity, target engagement, selectivity, or efficacy.
- A sequence-likelihood score is not expression, folding, activity, or safety.
- Agreement among models is candidate-prioritization evidence only. Shared data and abstractions can make errors correlated.

### Exact identity is load-bearing

Every sequence-bearing run must record the accession and version, exact input sequence, residue-numbering convention, modifications, construct junctions, and checksum. For the current UOX comparators, **Q00511 is the *Aspergillus flavus* UOX record and P78609 is the *Candida utilis* / *Cyberlindnera jadinii* UOX record.** They are distinct payload identities; evidence, mutations, and numbering do not transfer between them.

### A model result cannot skip a gate

For luminal UOX, exact configurations must first be built or supplied and characterized. Qualified configurations then enter [validation §1.33](../validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial); a surviving configuration enters [§1.36](../validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) before animal escalation. High-substrate activity, total protein, or a favorable ranking does not establish physiological product formation or safety.

COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology or chassis selection, production-sufficiency target, or safety conclusion.

## Computational Workflow

### 1. Define and source

- Start with one decision, not an open-ended request for a solution.
- Inspect primary records for every load-bearing sequence, structure, kinetic constant, residue position, cohort count, and evidence-tier claim.
- Preserve assay conditions and uncertainty. Do not mix values from incompatible systems into a synthetic benchmark.

### 2. Enumerate

- Make the candidate space explicit and reproducible.
- Separate hard exclusions from ranking preferences.
- Keep negative and positive controls in the same design space where possible.
- Freeze inputs, code, parameters, and decision rules before result-bearing execution.

### 3. Score with orthogonal roles

Use models that interrogate different failure modes rather than several versions of the same proxy. Examples include sequence plausibility, RNA behavior, structural integrity, expression burden, and reaction-site constraints. Record where the axes share inputs or training data.

### 4. Review before promotion

- Check arithmetic, units, accession identity, residue numbering, data provenance, and code-to-claim alignment.
- Inspect disagreement rather than averaging it away.
- Apply the [COMP review lifecycle](../../skills/new-comp-experiment/SKILL.md) to new or materially revised computational experiments.
- Treat an empty or failed positive-control result as assay or method failure, not evidence that all candidates are poor.

### 5. Measure

Build only the smallest matched set needed to discriminate the live hypotheses. Measure the property the model claimed to prioritize and the downstream function it was intended to protect. Report failed builds and uninterpretable assays without converting them into biological verdicts.

### 6. Update at the tested scope

A failed sequence, model, topology, chassis, or delivery route narrows that configuration. It does not kill the mission or prove another track. Feed measured failure modes back into the next design round without erasing the prior result.

## Open Enzyme Task Templates

### Sequence or construct shortlist

```text
Decision: [one bounded question]

Inputs:
- exact host and strain background
- accession/version and exact payload sequence
- topology and construct boundaries
- primary-source assay constraints

Enumerate a matched candidate set. For each candidate, report:
1. which input or model supports promotion;
2. shared assumptions and known blind spots;
3. the smallest discriminating measurement;
4. the result that redirects or kills the candidate; and
5. conclusions the computation cannot support.

Do not infer expression, physiological activity, dose, efficacy, safety, production sufficiency, or chassis superiority from computational ranking.
```

### Compound shortlist

```text
Decision: Which candidates warrant a gout-relevant first assay for [target/chokepoint]?

For each candidate, separate:
- direct target evidence;
- gout-relevant cellular or animal evidence;
- compartment and exposure constraints;
- selectivity and safety evidence;
- docking or model-derived priors; and
- the cheapest assay that would advance, redirect, or kill the hypothesis.

Rank by evidence directness, plausible compartment exposure, safety/selectivity evidence, and testability. Do not infer a human dose from in-vitro potency or discuss a production chassis unless sourcing or delivery makes it an active decision.
```

### Adversarial review

```text
Audit this result from first principles.

Check:
- exact source and sequence provenance;
- units, denominators, time windows, compartments, and mass balance;
- substrate occupancy, cosubstrates, coproducts, and access;
- whether the code implements the stated model;
- positive and negative controls;
- sensitivity to each load-bearing assumption;
- whether any conclusion exceeds the measured or computed property; and
- the observation that would falsify the interpretation.

Return actionable discrepancies. Do not repair a failed model by inventing replacement physiology, dose, efficacy, or safety claims.
```

## Known Proxy Failure: COMP-001

COMP-001 maps adjacent Q00511 pairs that match three unverified legacy preference filters and attaches AlphaFold per-residue confidence. The arrays are not established exhaustive protease-specificity rules. pLDDT is not solvent accessibility, protease survival, retained activity, or fermentation performance. Any claim about UOX survival in shio-koji requires the empirical [§1.10 assay](../validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) or another preregistered direct measurement; a structure/SASA calculation can refine candidate selection but cannot replace that gate.

## Reporting Contract

Every result-bearing computational page should state:

- question and permitted interpretation;
- inputs, versions, and provenance;
- executable method and frozen decision rules;
- outputs with units and uncertainty;
- positive and negative controls;
- sensitivity and failure branches;
- evidence level;
- exact empirical next gate; and
- explicit non-claims.

Keep provider access, pricing, installation, procurement, and product forecasts out of the research page. Those are volatile operational details and do not strengthen the scientific decision.

## Related

- [Computational Experiments](../computational-experiments.md)
- [Autonomous AI Screening Methodology](./autonomous-screening-methodology.md)
- [Manual Literature Mining](./manual-literature-mining.md)
- [Validation Experiments](../validation-experiments.md)
- [Cross-Vendor Heterogeneity Guard](../../papers/cross-vendor-heterogeneity-guard/draft.md)
