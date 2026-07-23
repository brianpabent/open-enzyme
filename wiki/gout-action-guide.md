---
title: "Gout research decision guide — contexts, evidence, and falsification"
date: 2026-05-08
tags: ["application-surface", "gout", "evidence-map", "decision-tree"]
related:
  - supplements-stack.md
  - gout-pathophysiology.md
  - etc/open-enzyme-vision.md
  - personal-genome-protocol.md
status: research-surface
audience: "Researchers and collaborators mapping patient contexts to gout mechanisms and discriminating experiments."
---

# Gout research decision guide — contexts, evidence, and falsification

This page maps common gout contexts to the relevant biological weakness, the established-care comparator, and the next research gate. It is not a treatment protocol. Open Enzyme is Phase 0 (Research & Design); investigational compounds, engineered organisms, genotype-directed stacks, and novel delivery systems described in this wiki are research hypotheses, not clinical recommendations. Clinical decisions belong with a qualified clinician using established guidelines and patient-specific contraindications.

For a patient-facing overview, see [gout.care](https://gout.care). For mechanism depth, use the linked research pages below.

## Research contexts

| Context | Dominant question | Research route |
|---|---|---|
| No genotype information; diet-associated or under-excretor phenotype unknown | Which upstream production and disposal mechanisms dominate? | [Purine biosynthesis](./prps-purine-biosynthesis-chokepoint.md), [fructose](./fructose-connection.md), [urate transport](./gout-pathophysiology.md#step-2-renal-handling--the-excretion-bottleneck) |
| Androgen-elevated state | Does the hormone state change urate handling, and is clomiphene exposure coupled to urate in a susceptible phenotype? | [Androgen–urate axis](./androgen-urate-axis.md), [H10](./hypotheses/H10-clomiphene-dose-urate-coupling.md) |
| ABCG2 Q141K carrier | Does impaired ABCG2 trafficking identify a different response class? | [ABCG2 modulators](./abcg2-modulators.md), [genotype-informed workflow](./genotype-informed-supplement-workflow.md) |
| Active flare | Which inflammatory chokepoint is causal and tractable without confusing acute control with long-term urate disposal? | [NLRP3 exploit map](./nlrp3-exploit-map.md), [gout pathophysiology](./gout-pathophysiology.md#step-4-the-inflammatory-cascade--nlrp3-and-the-flare) |
| Receiving urate-lowering therapy | Can an adjunct improve a distinct mechanism without obscuring the established-care baseline? | [Compound evidence catalog](./supplements-stack.md), [ABCG2 modulators](./abcg2-modulators.md) |
| Family history or elevated urate without flare | Which measurable phenotype predicts progression rather than merely correlating with it? | [Genetic variants](./gout-genetic-variants.md), [open questions](./open-questions.md) |

## Default research path

The central uncertainty is whether excess production, renal under-excretion, impaired intestinal export, or combinations of these mechanisms dominate in a given phenotype. Standard dietary and clinical care provide the comparator; Open Enzyme research should not substitute an unvalidated stack for that baseline.

The engineered gut-lumen UOX hypothesis currently has no validated model that predicts serum-urate effect, genotype ordering, or adequate dose. [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) found that comp-019's unconditional flat-dose classification was not robust to the tested substrate-occupancy and finite-window diagnostics; it did not identify the true physiological regime or reverse the old conclusion. Comp-019's numerical outputs therefore cannot guide decisions. Q141K remains a prospective stratification variable, but it does not justify a response prediction or a fixed dose.

Research gates:

1. Establish the phenotype with reproducible urate, flare, medication, diet, and renal-function context rather than assuming a single cause.
2. Separate urate-formation and urate-disposal hypotheses from acute inflammatory control.
3. Use compound entries in the [evidence catalog](./supplements-stack.md) as candidate dossiers, not as a combined regimen.
4. For engineered UOX, build and characterize exact configurations in the relevant construct-supply work (§§1.1, 1.2, and 1.5) or obtain an exact external configuration before §1.33. Nominate topology only within a controlled host comparison, treat cross-host results as configuration-specific, and pass §1.36 safety before animal escalation.

## Androgen-elevated context

Human androgen-manipulation studies show that urate can move with hormone state, but the direction is context-dependent. No direct clomiphene study located measured serum urate, incident gout, or renal/intestinal urate handling. [H10](./hypotheses/H10-clomiphene-dose-urate-coupling.md) tests the exposure–urate relationship from a disclosed n=1 signal without presuming that intestinal ER antagonism, renal transport, or androgen signaling is dominant. The earlier intestinal mechanism card, [H07](./hypotheses/H07-clomid-intestinal-er-antagonism.md), is retracted.

Research gates:

- Establish a reproducible clomiphene–urate relationship before assigning a mechanism.
- Test any proposed estradiol-pathway mechanism directly in the relevant tissue and exposure range.
- Measure urate handling independently of testosterone-related outcomes.
- Treat carnosine, cordycepin, eurycomanone, butyrate, and related candidates as mechanism probes until human gout evidence establishes direction and magnitude.

## ABCG2 Q141K context

Q141K is a biologically plausible stratifier because it impairs ABCG2 trafficking, but the response implications remain unvalidated. Consumer genotype panels are not a sufficient basis for an intervention decision; the data-quality caveat and variant evidence are summarized in [gout genetic variants](./gout-genetic-variants.md).

Research gates:

- Confirm genotype with an appropriate-quality assay before using it as a study stratum.
- Distinguish increased wild-type ABCG2 expression from rescue of Q141K folding or trafficking.
- Require direct epithelial exposure, trafficking, and urate-flux evidence before claiming a bypass intervention.

The proposed Q141K × butyrate study is specified in the [genotype-informed workflow](./genotype-informed-supplement-workflow.md); it is an experiment, not a personalized supplement recommendation.

## Active-flare context

An active flare is a clinical-care situation, not a suitable moment to test an unvalidated multi-compound stack. Colchicine, NSAIDs, glucocorticoids, and IL-1-directed agents are established clinical comparator classes described in the [NLRP3 exploit map](./nlrp3-exploit-map.md); choice, route, and dose depend on clinical judgment, contraindications, access, and current guidance.

The research distinction is acute inflammatory control versus long-term prevention. IL-1 blockade can test CP5a, disulfiram is a CP6b hypothesis, and lipid-resolution candidates probe CP5b/CP6a. None demonstrates durable urate control by itself. Any study must include an established-care comparator, prespecified safety stopping rules, and a separate long-term urate-lowering plan.

Research gates:

- Test one mechanistically distinct addition at a time before evaluating combinations.
- Require human-relevant exposure and an MSU-gout assay rather than importing potency from unrelated inflammasome models.
- Track flare resolution and recurrence separately; an acute-abort result does not establish prophylaxis.
- Do not infer superiority from narrower mechanism or modeled receptor occupancy without head-to-head clinical evidence.

## Context of established urate-lowering therapy

Allopurinol, febuxostat, uricosurics, and clinically used uricase products define the established-care comparison space. Research adjuncts should be evaluated only for a nonredundant mechanism and should not be allowed to obscure whether the baseline therapy reached and maintained its clinical target.

Research gates:

- Predefine the adjunct's mechanism: upstream purine production, renal transport, intestinal export, luminal degradation, crystal biology, or inflammatory response.
- Hold background therapy stable where the study design permits.
- Measure drug–compound and drug–microbe interactions before interpreting apparent additivity.
- Treat the PDB × xanthine-oxidase-inhibitor interaction assay in [validation experiments](./validation-experiments.md#143-pdb--allopurinoloxypurinolfebuxostat-interaction-assay) as a prerequisite for that combination hypothesis.

## Pre-flare and prevention research

The prevention question is whether a measurable biological weakness predicts progression to crystal deposition or flare. Family history, serum urate, renal function, transporter genotype, diet, microbiome state, and inflammatory markers are candidate stratifiers; none should be collapsed into a universal preventive stack.

Research gates:

- Define the outcome prospectively: serum urate, crystal burden, incident flare, or inflammatory biomarker.
- Use genotype and biomarker measurements to stratify, not to backfill an explanation after the outcome.
- Prefer the cheapest experiment that can falsify the proposed mechanism.
- Escalate to engineered delivery only when the molecule, exposure, and target engagement are already supported.

## Cross-references

- [Gout pathophysiology](./gout-pathophysiology.md)
- [NLRP3 exploit map](./nlrp3-exploit-map.md)
- [Compound evidence catalog](./supplements-stack.md)
- [ABCG2 modulators](./abcg2-modulators.md)
- [Genotype-informed research workflow](./genotype-informed-supplement-workflow.md)
- [Validation experiments](./validation-experiments.md)
- [Open questions](./open-questions.md)
