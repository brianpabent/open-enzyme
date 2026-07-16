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

> This wiki stub remains so cross-references resolve and the page stays discoverable.
> Computational analyses are write-once artifacts; the daemon does not need to re-read
> them on every sweep, so the long content lives next to the experiment that produced it
> at `etc/experiments/comp-034-lactoferrin-linker-redesign/`.

> **✓ Tool-stack caveat RESOLVED 2026-05-19 (E2 walkthrough rerun complete).** ProteinMPNN was cloned to `tools/ProteinMPNN/` (repo-local fallback; sandbox blocked `/opt/` and `~/tools/`). Smoke test passed on `5L33` + `6MRR`; lactoferrin inter-lobe linker sampling runs in ~52 s/pool on CPU. **Headline rerun finding:** the substitute sampler's 15 GREEN candidates are NOT artifacts — mean MPNN log-likelihood 2.74 (GREEN) vs 3.74 (FAIL) gives clean separation. The substitute sampler's proline-bias + WT-mix-in heuristic was a coarse but functional proxy for what ProteinMPNN encodes structurally. **Plus: genuine MPNN identified 3 STRICT (5-of-5) candidates the substitute sampler never proposed:** `NEEEQQQEEEQ`, `NEEEEQQEQEQ`, `NEEEEEQEQEQ` — all reduce predicted cleavage 10.4× vs WT (0.039 vs 0.407) and pass concordance on all five comp-034 metrics simultaneously. **§1.10 wet-lab arm validated for gene synthesis** with the swap-in of `NEEEQQQEEEQ` as the aggressive arm in place of the substitute-sampler's `DEEDPANPQAH` / `EEEEPAAPPAP`. Full report + scoring artifacts: [`logs/proteinmpnn-comp-034-rerun-2026-05-19.md`](../logs/proteinmpnn-comp-034-rerun-2026-05-19.md). Scoring artifacts committed to [`./etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/`](./etc/experiments/comp-034-lactoferrin-linker-redesign/proteinmpnn_rerun/). **Install note 2026-05-19:** the subagent's `tools/ProteinMPNN/` clone was sandbox-ephemeral and did not persist. For durable `/opt/ProteinMPNN` install outside the sandbox: `git clone https://github.com/dauparas/ProteinMPNN /opt/ProteinMPNN` (PyTorch 2.12 + NumPy 2.4 already on system; smoke-test with `examples/submit_example_1.sh`).

> **★ Physics ΔΔG + structure-gated cleavage added 2026-05-30 (PyRosetta unblocked 2026-05-29).** Two orthogonal methods were added to the concordance gate — Cartesian ΔΔG (fold stability) and structure-gated cleavage (real SASA + secondary-structure conformation gate, replacing the pLDDT-as-accessibility proxy). **Headline: `NEEEQQQEEEQ` wins on both axes and is the wet-lab pick; the proline-rigidification arms are self-defeating.** One variable explains it — **inter-lobe helix retention.** The WT linker is a structured α-helix (9/11 residues); keeping it preserves fold stability *and* protease resistance (proteases need an extended substrate). Cartesian ΔΔG: both MPNN charge/polar arms are stability-neutral (`NEEEQQQEEEQ` +0.23 REU, `NEEEQEEQDQQ` +2.39, helix 0.818); every proline arm is destabilizing (`V357P` +20.11, `S353E+V357P` +21.26, multi-proline `EEEEPAAPPAP` +57.48 with helix collapsed to 0.364). Structure-gated cleavage on real relaxed mutant structures: MPNN arms −66% vs WT, proline arms only −9%/−17%/−3% (breaking the helix re-exposes the backbone and cancels the sequence-preference gain). **This inverts the original risk ordering: the proline single/double mutants were framed as the "conservative/safe" arms — physics shows they are the destabilizing, low-benefit ones.** Revised §1.10 plate: **WT control + `NEEEQQQEEEQ` (primary) + `NEEEQEEQDQQ` (sibling)**; proline arms demoted/optional. Full three-method analysis, honest magnitude corrections, and reproduce instructions: [`./etc/experiments/comp-034-lactoferrin-linker-redesign/rosetta_concordance/README.md`](./etc/experiments/comp-034-lactoferrin-linker-redesign/rosetta_concordance/README.md). Evidence level: Mechanistic Extrapolation (in silico); wet-lab proteolysis + Tm assays are the validators.

> **Original 2026-05-16 substitute-sampler caveat (kept for archival genealogy):** comp-034's candidate sequences were generated by a transparent substitute sampler because `protein_design_mcp` shells out to ProteinMPNN scripts at `$PROTEINMPNN_PATH` (default `/opt/ProteinMPNN`) — those were not present at the 2026-05-16 run. The substitute sampler is RNG-seeded for reproducibility, biased over the permitted residue pool `[E, D, N, Q, H, P]` with WT mix-in (15%) and proline-boost at ALP-hot WT positions. The 2026-05-19 rerun (resolved above) confirmed the substitute was a functional proxy and identified additional MPNN-native STRICT candidates.

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

## Open follow-up — does the linker protease-resistance design logic generalize? (added 2026-05-19, Cluster E walkthrough; re-scoped 2026-05-30 — see the ⚠ note below)

**The valid generalization question (re-scoped 2026-05-30):** does the design logic that actually *won* on lactoferrin's inter-lobe linker — **strip protease-preferred residues while preserving the protective secondary structure** (e.g. `NEEEQQQEEEQ`, helix-preserving, −66% cleavage) — generalize to **other secreted OE payloads with structured-mandatory-connector-type linker vulnerabilities**? **Note the inversion:** the original framing of this question was "does *proline-rigidification* generalize?" — but the 2026-05-30 physics analysis found proline-rigidification self-defeating on this structured (helical) connector (it breaks the protective helix; see the ⚠ note below). Proline-rigidification may still suit a genuinely *flexible/loop* connector with no helix to break, but that is a different candidate class than the one comp-034 actually had.

**Definition of the right candidate class** (the generalization domain):
- (a) The linker is **short and structured** (high pLDDT, ordered secondary structure).
- (b) It **cannot be removed** without breaking the protein's function (it connects two essential domains).
- (c) It shows **protease vulnerability** in koji proteomics (high predicted cleavage-site density).
- (d) The host's proteolytic environment (shio-koji or equivalent) is the production format.

**Examples of candidate cases worth watching as the platform's payload pipeline grows:**
- Multi-domain fusion proteins with short structured connectors
- Therapeutic peptides ≥3 kDa with structured architecture
- Future siRNA-protein conjugates if the linker is structured

**⚠ DAF SCR1-4 is NOT the right exemplar (Pass 3 2026-05-17 correction, ratified 2026-05-19 Cluster E walkthrough).** The original 2026-05-16 sweep proposed DAF SCR1-4 inter-SCR linkers as the generalization test. Pass 3 correctly pushed back: comp-012 says stalk truncation (aa 286–353 removal) eliminates 100% of exposed sites; the SCR1-4 core is LOW protease risk after truncation; the short inter-SCR linkers are NOT identified as remaining protease-liability targets. **DAF is solved by truncation, not by linker rigidification — fundamentally the opposite design strategy.** The daemon's Pass 2 conflation of "exposed protease-accessible region" between Lf's structured-mandatory linker (aa 353–363) and DAF's disordered-removable stalk (aa 286–353) is a documented Pass 2 failure mode — surface-level pattern-matching without structural-detail check. See [`etc/bio-ai-tools.md` §"Protease-vulnerability-to-redesign workflow"](./etc/bio-ai-tools.md) step 2 ("vulnerability classification — structural-mandatory vs structural-removable") for the discipline that catches this class of error.

**⚠ 2026-05-30 update — the proline-rigidification *strategy itself* is in question, not just its generalization.** The physics ΔΔG + structure-gated cleavage analysis (see the ★ note at the top of this page) found proline-rigidification **self-defeating on the original lactoferrin target**: because the inter-lobe linker is a structured α-helix, proline both destabilizes the fold (ΔΔG +20 to +57 REU) *and* breaks the helix that was conformationally protecting the backbone from proteases (net cleavage benefit only −3% to −17%). The winning strategy is **charge/polar substitution that preserves the helix** (`NEEEQQQEEEQ`: ΔΔG ≈ 0, cleavage −66%). So the generalization question below should be re-scoped: for a *structured* (helical) mandatory connector, the design logic is **"strip protease-preferred residues while preserving the protective secondary structure,"** NOT "insert proline to rigidify." Proline-rigidification may still suit a genuinely *flexible/loop* connector (where there is no helix to break) — but that is a different candidate class than the one comp-034 actually had.

**Status:** open question dormant until a new secreted payload candidate emerges with a structured-mandatory-connector vulnerability profile. Then the comp-005 → comp-034-style workflow re-fires on that target — now with the physics ΔΔG + structure-gated cleavage legs (PyRosetta) as part of the gate. Cluster J3's substrate engineering platform principle may surface relevant candidates (substrate-engineering reagents that boost cordycepin or ergothioneine could indirectly require structural redesign for new fungal payloads).
