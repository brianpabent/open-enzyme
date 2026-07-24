---
title: Fructose-driven urate production
date: 2026-05-07
aliases: [fructose-gout, fructose-link, KHK, ATP-depletion]
tags:
  - fructose
  - ketohexokinase
  - purine-catabolism
  - urate
  - ABCG2
related:
  - gout-pathophysiology.md
  - prps-purine-biosynthesis-chokepoint.md
  - abcg2-modulators.md
  - validation-experiments.md
sources:
  - PMID 19158351
  - PMID 24177030
  - PMID 19926891
  - PMCID PMC8050029
status: draft
---

# Fructose-driven urate production

## Gout weakness

Ketohexokinase (KHK, fructokinase) consumes ATP while phosphorylating
fructose. Under a sufficiently strong fructose load, ATP and phosphate
depletion can increase AMP turnover through AMP deaminase; the pre-existing
adenine nucleotide pool is then degraded through IMP, inosine, hypoxanthine,
xanthine, and urate. KHK-dependent ATP loss and urate generation have been
measured in human proximal-tubule cells (**In Vitro**; PMID 19158351).

```text
fructose
  ↓ KHK consumes ATP
fructose-1-phosphate + ADP
  ↓ ATP/phosphate depletion
AMP → IMP → inosine → hypoxanthine → xanthine → urate
```

This is **purine catabolism**, not creation of new purines through de-novo
synthesis. PRPS supplies PRPP to de-novo purine synthesis, purine salvage, and
pyrimidine synthesis; the current evidence does not establish that
fructose-driven urate production works by relieving PRPS inhibition or
increasing PRPP supply. See
[PRPS / PRPP supply](./prps-purine-biosynthesis-chokepoint.md).

## SLC2A9 / GLUT9 boundary

SLC2A9 is a major renal urate transporter. Homozygous loss-of-function
mutations impair urate reabsorption and cause severe renal hypouricemia, often
with very high fractional urate excretion and risks including nephrolithiasis
and exercise-induced acute kidney injury (**Human Observational + In Vitro**;
PMID 19926891).

Therefore:

- SLC2A9 loss-of-function is not evidence of impaired urate excretion or
  increased hyperuricemia risk.
- A common-variant association at the SLC2A9 locus does not specify the
  direction of an individual's transporter function.
- The historic claim that GLUT9 creates a two-way fructose-and-urate genetic
  vulnerability is not decision-usable. Fructose transport, renal urate
  reabsorption, and KHK-driven metabolism require separate measurements.
- SLC2A9 genotype does not justify a KHK intervention, a dietary rule, or a
  fructose challenge.

The canonical variant direction belongs in
[gout genetic variants](./gout-genetic-variants.md).

## KHK as an experimental intervention

PF-06835919 provides a defined KHK-inhibitor precedent. It has been evaluated
in preclinical systems and in human metabolic-disease studies
(**Animal Model + Clinical Trial**; PMID 32910646, PMCID PMC8050029, and DOI
10.1111/dom.14946). Those studies establish that KHK can be pharmacologically
engaged; they do not establish gout efficacy, a serum-urate effect in gout, or
a clinical use rule.

A gout-relevant KHK experiment must keep these readouts separate:

1. target engagement and fructose-1-phosphate formation;
2. ATP and phosphate depletion;
3. AMP turnover and isotope-resolved purine catabolism;
4. urate production and mass balance;
5. off-target transporter and metabolic effects; and
6. viability and recovery after exposure.

The relevant evidence object is a compositionally verified inhibitor at a
measured free exposure. A dietary ingredient, botanical extract, docking hit,
or predicted KHK binder cannot inherit PF-06835919's evidence.

## Possible intestinal feed-forward loop

Rat ileal evidence and KHK-dependent intestinal-cell evidence motivate a
second question: could fructose-associated KHK/ROS signaling reduce functional
intestinal ABCG2 urate export while KHK-driven metabolism increases urate
production? The complete causal chain and its relevance to human gout remain
unmeasured.

> **Research conjecture — fructose can raise urate while narrowing intestinal export**{ .research-conjecture-label }
>
> **Grounded premises:** KHK-dependent fructose metabolism can consume ATP and
> generate urate in human proximal-tubule cells (**In Vitro**; PMID 19158351).
> Rat ileal and intestinal-cell work motivates a NOX/ROS–ABCG2 link
> (**Animal Model + In Vitro**; source and assay boundary in
> [validation §1.39](./validation-experiments.md#139-fructose--khk--nox--abcg2-human-enteroid-test)).
>
> **Novel leap:** The two arms might operate together, so the same exposure increases urate production while reducing intestinal urate export. No direct evidence tests the complete chain in a human intestinal system.
>
> **Why it matters:** A coupled result would expose a feed-forward weakness
> and distinguish a production-only intervention from one that must also
> preserve gut urate transport.
>
> **Discriminating observation:** In polarized human ileal enteroids, compare
> matched fructose and glucose conditions with KHK and NOX perturbations.
> Measure ATP, ROS, ABCG2 surface state, directional urate flux, and viability.
> Advance the conjecture only if the perturbations separate KHK-dependent ATP
> loss from NOX/ABCG2-dependent flux loss.

## Falsification program

- **Production arm:** Use isotope-resolved fructose and purine measurements to
  test whether KHK inhibition changes urate production under a defined
  exposure. A change in serum or media urate without mass balance does not
  locate the mechanism.
- **Export arm:** Run
  [validation §1.39](./validation-experiments.md#139-fructose--khk--nox--abcg2-human-enteroid-test).
  A high-dose toxicity result, expression-only change, or nondirectional
  transporter assay does not support the feed-forward loop.
- **PRPP arm:** Measure PRPP and de-novo/salvage flux directly before assigning
  a PRPS mechanism. The AMP-catabolism result does not imply it.
- **Genetic arm:** Use isogenic SLC2A9 models only for a specified urate-
  transport question. Do not infer fructose sensitivity from risk-locus
  status.

A negative result narrows the tested exposure, compartment, and mechanism; it
does not erase fructose-driven AMP catabolism or other KHK-dependent disease
biology.

## Related evidence

- [Gout pathophysiology](./gout-pathophysiology.md)
- [PRPS / PRPP supply](./prps-purine-biosynthesis-chokepoint.md)
- [ABCG2 modulators](./abcg2-modulators.md)
- [Multihop gout program](./gout-multihop-research-program.md)
