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

> **⚠️ Root verdict STALE — superseded by its own extensions (comp-review 2026-07-14).** The original 2026-05-16 substitute-sampler result is **materially superseded by comp-034 later ProteinMPNN + Rosetta/PyRosetta extensions**. Cite the later-extension results, NOT the original substitute-sampler verdict.

> Full artifacts live at `etc/experiments/comp-034-lactoferrin-linker-redesign/`.

> **ProteinMPNN result.** Mean MPNN log-likelihood separated GREEN (2.74) from FAIL (3.74) candidates. ProteinMPNN identified three STRICT candidates: `NEEEQQQEEEQ`, `NEEEEQQEQEQ`, and `NEEEEEQEQEQ`; all reduce predicted cleavage 10.4× versus WT and pass all five comp-034 metrics. §1.10 uses `NEEEQQQEEEQ` as the primary aggressive arm. Full report: [`logs/proteinmpnn-comp-034-rerun-2026-05-19.md`](../logs/proteinmpnn-comp-034-rerun-2026-05-19.md).

> **Physics result.** Cartesian ΔΔG and structure-gated cleavage both favor `NEEEQQQEEEQ`; proline-rigidification is destabilizing and low-benefit because it breaks the protective inter-lobe helix. The §1.10 plate is **WT + `NEEEQQQEEEQ` + `NEEEQEEQDQQ`**; proline arms are optional. Evidence level: **Mechanistic Extrapolation**; wet-lab proteolysis and Tm assays remain required.

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
- Experiment directory (inputs, scripts, outputs): [`./etc/experiments/comp-034-lactoferrin-linker-redesign/`](./etc/experiments/comp-034-lactoferrin-linker-redesign/)
- Computational experiments index: [`computational-experiments.md`](./computational-experiments.md)

**Evidence level:** Mechanistic Extrapolation (in silico only). Wet-lab validation
required — comp-034 expands the [`validation-experiments.md §1.10`](./validation-experiments.md) lactoferrin arm from a single-variant feasibility test into a multi-variant
ranked design study (recommended plate: WT control + V357P conservative + DEEDPANPQAH
aggressive).

---

## Open follow-up — does the linker protease-resistance design logic generalize?

**Generalization question:** does the winning design logic — **strip protease-preferred residues while preserving protective secondary structure** — generalize to other secreted payloads with structured, mandatory connector vulnerabilities? Proline-rigidification may still suit genuinely flexible connectors but is not the rule for structured helices.

**Definition of the right candidate class** (the generalization domain):
- (a) The linker is **short and structured** (high pLDDT, ordered secondary structure).
- (b) It **cannot be removed** without breaking the protein's function (it connects two essential domains).
- (c) It shows **protease vulnerability** in koji proteomics (high predicted cleavage-site density).
- (d) The host's proteolytic environment (shio-koji or equivalent) is the production format.

**Examples of candidate cases worth watching as the platform's payload pipeline grows:**
- Multi-domain fusion proteins with short structured connectors
- Therapeutic peptides ≥3 kDa with structured architecture
- Future siRNA-protein conjugates if the linker is structured

**DAF SCR1-4 is not the right exemplar.** Comp-012 indicates that stalk truncation removes the exposed sites and leaves a LOW-risk core; the inter-SCR linkers are not identified liabilities. DAF is addressed by truncation, not linker redesign.

**Proline-rigidification is not the selected strategy for the lactoferrin linker.** It destabilizes the fold (ΔΔG +20 to +57 REU) and yields only −3% to −17% cleavage benefit. The winning strategy is charge/polar substitution that preserves the helix (`NEEEQQQEEEQ`: ΔΔG ≈ 0, cleavage −66%).

**Status:** open question dormant until a new secreted payload candidate emerges with a structured-mandatory-connector vulnerability profile. Then the comp-005 → comp-034-style workflow re-fires on that target — now with the physics ΔΔG + structure-gated cleavage legs (PyRosetta) as part of the gate. Cluster J3's substrate engineering platform principle may surface relevant candidates (substrate-engineering reagents that boost cordycepin or ergothioneine could indirectly require structural redesign for new fungal payloads).
