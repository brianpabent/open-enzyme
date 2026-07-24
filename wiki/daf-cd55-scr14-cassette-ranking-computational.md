---
title: "DAF/CD55 SCR1-4 Cassette Configuration (comp-030)"
date: 2026-05-15
tags:
  - computational
  - comp-030
  - cassette-design
  - daf
  - cd55
  - scr14
  - signal-peptide
  - secretion-scaffold
  - aspergillus-oryzae
related:
  - validation-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - computational-experiments.md
sources:
  - "Ward PP et al. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791); glucoamylase-KEX2 expression architecture"
status: retired-invalid-model; matched construct comparison unresolved
---

# DAF/CD55 SCR1-4 Cassette Configuration

Which expression and processing configuration can produce intact, natively folded, functional DAF SCR1-4 in *Aspergillus oryzae*?

COMP-030 does not answer that question. Its candidate scores, promoted sets, max-CAI preference, direct-secretion ranking, ESM2 pseudo-pLDDT, chaperone-load coefficients, and cross-target generalizations are invalid. The [COMP-030 tombstone](./etc/experiments/comp-030-daf-cassette-ranking/) is non-runnable; Git retains the retired implementation and outputs.

> **Research conjecture — processing route may determine usable DAF SCR1-4 production**{ .research-conjecture-label }
>
> **Grounded premises:** Direct signal-peptide secretion and a GlaA-KEX2 fusion expose a heterologous protein to different expression and processing contexts (**Mechanistic Extrapolation**; source: Ward et al. 1995 documents the GlaA-KEX2 architecture for a different human protein). An exact DAF SCR1-4 product must be recovered with its native fold and retained complement-regulatory function before the configuration is useful (**Mechanistic Extrapolation**; source: [DAF SCR1-4 evidence](./daf-cd55-scr14-truncated-computational.md)).
>
> **Novel leap:** One route may yield more correctly processed, natively folded, functional DAF SCR1-4 than the other. No direct evidence establishes a winner for these exact constructs. Codon variants may also interact with route, but the retired computation supplies no preferred variant.
>
> **Why it matters:** A route-specific result can select a build without mistaking a sequence heuristic for product formation.
>
> **Discriminating observation:** Compare exact direct-secretion and GlaA-KEX2 constructs under matched promoter, integration, host, culture, and quantification conditions. Optionally cross a prespecified small codon-variant panel. Measure transcript and protein abundance, processing fidelity, native-fold attainment, intact secreted product, and concentration-dependent retained complement-regulatory function. Advance only the exact configuration that passes prespecified quality and function gates.

A negative result kills only the tested construct × processing route × codon configuration. It does not reject DAF-mediated complement regulation or another production chassis.

Related: [validation §1.25](./validation-experiments.md) · [H05 falsification card](./hypotheses/H05-daf-scr14-cp0-thesis.md) · [COMP registry](./computational-experiments.md)
