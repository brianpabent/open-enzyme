---
title: "Lactoferrin Inter-Lobe Linker Candidate Design (comp-034)"
date: 2026-05-16
tags: [computational, comp-034, lactoferrin, linker-redesign, proteinmpnn, protease, aspergillus-oryzae]
related:
  - lactoferrin.md
  - lactoferrin-protease-stability-computational.md
  - validation-experiments.md
  - etc/bio-ai-tools.md
  - computational-experiments.md
sources:
  - "UniProt P02788 (TRFL_HUMAN), entry v268 (28-JAN-2026), sequence v6"
  - "Ward PP et al. Nat Biotechnol 1992;10:784-789 (PMID 1368268)"
  - "Sun XL et al. Acta Crystallogr D 1999;55:403-407 (PMID 10089347)"
  - "PDB 1B0L — diferric human lactoferrin"
status: retired-invalid-model
---

# Lactoferrin Inter-Lobe Linker Candidate Design (comp-034)

The engineering question is whether an exact inter-lobe connector can be altered without disrupting lactoferrin's bilobal fold, and whether such a change improves retained function through shio-koji processing.

COMP-034 cannot answer that question. It reused an unverified legacy protease-preference table as a cleavage axis, then combined it with uncalibrated sequence, ProteinMPNN, and Rosetta scores. The resulting cleavage values, GREEN/STRICT tiers, concordance claims, candidate ordering, and wet-lab priorities are invalid. The [COMP-034 tombstone](./etc/experiments/comp-034-lactoferrin-linker-redesign/) is non-runnable.

> **Research conjecture — an observed linker-associated failure may be engineerable**{ .research-conjecture-label }
>
> **Grounded premises:** UniProt P02788 and PDB 1B0L define the short connector between the two lactoferrin lobes (**In Vitro** structural record; PMID 10089347). Section [§1.10](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) treats fragment formation and retained iron binding as unmeasured empirical gates.
>
> **Novel leap:** If a reproducible WT fragment maps to this connector, a sequence change might reduce that failure while preserving lobe geometry and lactoferrin function. No direct study has tested that failure-specific redesign in shio-koji.
>
> **Why it matters:** A successful redesign could preserve the payload and delivery route without deleting a structurally required connector.
>
> **Discriminating observation:** First establish a reproducible WT fragment and map its termini. Only then run a new gated design against verified specificity and structural constraints, followed by a matched diversity panel measuring intact abundance, fragment pattern, iron binding, and thermal stability.

No variant is currently selected. A negative WT fragmentation result redirects effort away from linker engineering without rejecting lactoferrin or the broader delivery portfolio.

Related: [§1.10 validation](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) · [lactoferrin evidence page](./lactoferrin.md) · [COMP-034 tombstone](./etc/experiments/comp-034-lactoferrin-linker-redesign/)
