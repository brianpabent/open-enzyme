---
title: "Lactoferrin Inter-Lobe Linker Redesign Pilot (Computational, comp-034)"
date: 2026-05-16
tags:
  - computational
  - comp-034
  - lactoferrin
  - linker-redesign
  - protein-design-mcp
  - proteinmpnn
  - biodesignbench
  - protease-stability
  - aspergillus-oryzae
  - koji
  - shio-koji
related:
  - lactoferrin.md
  - lactoferrin-protease-stability-computational.md
  - validation-experiments.md
  - etc/bio-ai-tools.md
  - etc/autonomous-screening-methodology.md
  - uricase-cassette-ranking-computational.md
  - daf-cd55-scr14-cassette-ranking-computational.md
  - computational-experiments.md
sources:
  - "UniProt P02788 (TRFL_HUMAN), entry v268 (28-JAN-2026), sequence v6 — DOMAIN 25..352, DOMAIN 364..695, SIGNAL 1..19, CHAIN 20..710"
  - "Ward PP et al. Nat Biotechnol 1992;10:784-789 (PMID 1368268) — first hLf expression in A. oryzae"
  - "Sun XL et al. Acta Crystallogr D 1999;55:403-407 (PMID 10089347) — recombinant hLf 2.2 Å structure, 0.3 Å RMSD vs native"
  - "PDB 1B0L — diferric human lactoferrin, 2.2 Å resolution"
  - "Verkuil R et al. bioRxiv 2022; Hsu C et al. 2022 — ESM2 pseudo-likelihood fold-quality proxy"
  - "Kim & Romero 2026 (BioDesignBench) — multi-candidate / multi-metric / head-to-head / filter discipline"
status: complete (pilot v1, 2026-05-16)
---

# Lactoferrin Inter-Lobe Linker Redesign Pilot (Computational, comp-034)

> **Frozen analysis archived to [`../experiments/comp-034-lactoferrin-linker-redesign/wiki-archive.md`](../experiments/comp-034-lactoferrin-linker-redesign/wiki-archive.md).**
> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `experiments/comp-034-lactoferrin-linker-redesign/`.

Can the human lactoferrin inter-lobe linker (UniProt 353-363, mature 334-344, sequence
`SEEEVAARRAR`) be redesigned to reduce predicted shio-koji protease cleavage while
preserving lobe-lobe geometry and *A. oryzae* codon compatibility?

**Headline verdict:** 15 of 60 candidates pass the N-of-5 ≥ 3 concordance gate (GREEN tier).
Zero pass STRICT (5-of-5). The WT linker passes 3-of-5 — confirming the redesign premise
(WT is the most protease-rich linker in the candidate pool). Top primary wet-lab variant
`EEEEPAARRAR` (S353E + V357P; mature S334E + V338P; 2 substitutions, 82% WT identity) passes
4-of-5 with cleavage drop ~29%. True single-V357P variant `SEEEPAARRAR` (91% WT identity)
passes 3-of-5 (fails loop_pLDDT band by 1.6) — secondary wet-lab anchor. Aggressive
4-of-5 variant `EEEEPAAPPAP` (multi-proline, 55% WT identity) is second-line option.

This is the **first concrete use of the protein-design-mcp tool stack** ([`etc/bio-ai-tools.md`](./etc/bio-ai-tools.md) §BioDesignBench). The MCP wrapper loaded correctly on this
host but the external ProteinMPNN repository at `/opt/ProteinMPNN` was not present, so a
**structure-conditioned biased sampler** was substituted with transparent flagging. The
substitution is documented in detail in the archive page; regenerating the candidate pool
with genuine ProteinMPNN when the repo is installed is a single-command rerun.

**Where the analysis lives:**
- Full archived analysis: [`../experiments/comp-034-lactoferrin-linker-redesign/wiki-archive.md`](../experiments/comp-034-lactoferrin-linker-redesign/wiki-archive.md)
- Experiment directory (inputs, scripts, outputs): [`../experiments/comp-034-lactoferrin-linker-redesign/`](../experiments/comp-034-lactoferrin-linker-redesign/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)

**Evidence level:** Mechanistic Extrapolation (in silico only). Wet-lab validation
required — comp-034 expands the [`validation-experiments.md §1.10`](./validation-experiments.md) lactoferrin arm from a single-variant feasibility test into a multi-variant
ranked design study (recommended plate: WT control + V357P conservative + DEEDPANPQAH
aggressive).
