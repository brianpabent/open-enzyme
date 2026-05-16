# comp-021: Upstream-Complement Compound × Assay-Format × IC50 Stratification

**Date:** 2026-05-16
**Status:** Phase 1 complete.

## Purpose

comp-020 documented a **44× IC50 spread** for rosmarinic acid (RA) as a C3-convertase inhibitor: Englberger 1988 (PMID 3198307) 5–10 µM in purified C3 convertase assay; Sahu 1999 (PMID 10353266) 34 µM cell-based C3b covalent attachment, 160–180 µM hemolytic CP/AP, 1500 µM direct C5 convertase; Cimanga 1999 (PMID 17260306) / Mu 2013 (PMID 24144800) 137–182 µM in sheep-erythrocyte hemolytic format. The spread is a **load-bearing input uncertainty** in comp-029's combined-CP0 systems model: comp-029 modelled the operative RA IC50 as log-uniform [5 µM, 180 µM] (modeling choice in `inputs/rosmarinic_acid_ic50_data.json` L47), and the resulting wide singleton CI is the reason comp-029 returned YELLOW rather than GREEN on the dietary-CP0 + engineered-DAF combined-coverage thesis.

**comp-021's question:** is the 44× spread a real biology signal (different assay formats are measuring genuinely different mechanistic steps, and the operative IC50 for gut-luminal MSU-relevant biology is a specific narrower range), or assay-noise (the same biology, different sheep blood lots / different serum sources / different endpoint definitions, and the 44× is irreducible)?

The same question applies to **every** upstream-complement natural-product modulator in the OE corpus, not just RA. Stratify by assay format → see which compounds collapse uncertainty (now tight) vs. which remain wide → produce a compound × assay-format matrix → use it as a direct input upgrade to any downstream systems model (comp-029 re-run with stratified prior; future combined-CP0 / chaperone-orthogonal-stacking analyses).

## Question

For each compound surfaced by comp-018 (rosmarinic acid, luteolin, tiliroside, *Bupleurum* polysaccharides, falcarindiol, ganoderic acid Sz, ergosterol, quercetin, dicaffeoylquinic acid, K-76 / complestatin) and the comp-020 additions (*Helicteres* benzofuran lignans, marine sulfated polysaccharides ANW/SC/SJW-3, heparin and heparin-derived oligosaccharides):

1. Pull every published IC50 with its assay format.
2. Classify each assay by **what it actually measures**: hemolytic CH50 / AP50 / LP50, ELISA C3b/C3c/C5b-9 deposition, fluorometric C5a generation, direct convertase enzymatic, cell-based C3b deposition.
3. Tag each IC50 with: serum source (guinea pig / NHS / mouse / human MBL-deficient / pooled), serum dilution, RBC source (sheep / rabbit), readout timing, presence/absence of CRP / IgM (Wessig 2022 showed both are required for robust MSU-driven C5a).
4. Map IC50s into a compound × assay-format matrix.
5. Interpret which compound + assay-format combinations are most relevant to **gut-luminal complement activity** (per comp-029's gut-luminal-transient finding).
6. Flag compounds where assay-stratified IC50s **converge to a tight range** (low uncertainty, narrow-prior candidates) vs. compounds where they **spread widely** (load-bearing uncertainty remains).

## Methodology

1. **Compound list** from `inputs/compound-list.json` — comp-018 + comp-020 surface plus the comp-029 RA prior anchor papers.
2. **Per-compound IC50 inventory** from primary-literature anchors already verified in comp-018 + comp-020 + comp-029 provenance (Paperclip-grep-anchored where the source PMC is available; abstract-tier flagged where not).
3. **Assay-format taxonomy** in `inputs/assay-formats.json` — 6 canonical formats: H-CP (hemolytic classical pathway, sheep EA + guinea pig or NHS serum), H-AP (hemolytic alternative pathway, rabbit E + Mg-EGTA NHS), H-LP (hemolytic lectin pathway, mannan-coated EA or LPS-coated), ELISA-CP/AP/LP (WieLISA or C3c-ELISA), CELL-C3b (cell-based C3b deposition), CONV-ENZ (purified convertase enzymatic), C4-CLEAVAGE (purified C4 cleavage by MASPs).
4. **Compound × assay matrix** at `outputs/matrix.json` — IC50 values with units normalized (µM for small molecules, µg/mL for polysaccharides), assay-format tag, primary source, serum/dilution metadata, evidence tier.
5. **Gut-luminal relevance scoring** — each (compound, assay-format) combo scored 0-3 for gut-luminal mechanistic match:
   - 3 = directly measures gut-luminal-relevant mechanism (cell-based C3b deposition on a particulate surface; C3c-ELISA in dilute serum approximating gut-luminal IgM/CRP load)
   - 2 = measures upstream convertase formation step (hemolytic CP at 1:80 serum approximates dilute extracellular fluid; ELISA-CP with mannan or IgM coating)
   - 1 = measures downstream amplification (hemolytic AP at higher serum concentrations; direct convertase enzymatic with purified components)
   - 0 = orthogonal mechanism (direct C5 convertase post-assembly; not the deposition step)
6. **Uncertainty-collapse analysis** — per compound, compute log-spread of stratified IC50s within the gut-luminal-relevant subset (scores 2-3) and compare to log-spread of the full unstratified set.
7. **comp-029 re-run sensitivity** — re-derive what comp-029 would output if its RA IC50 distribution were narrowed from log-uniform [5, 180] µM to the assay-format-stratified gut-luminal-relevant subset.

## Hard constraints honored

- File scope: only `experiments/comp-021-*/*` + `wiki/upstream-complement-assay-format-mapping-computational.md`.
- No subagents spawned.
- Pre-commit grep-verify gate (CLAUDE.md Rule 4): every IC50 in `outputs/matrix.json` either grep-verified line-anchored against Paperclip-corpus source OR explicitly flagged abstract-tier / cross-reference-tier.
- Multilingual default: CNKI Bupleurum complement literature checked; Zhang & Chen 2008 (PMC7126446) and Wu 2015 (PMC4629277) are the Daofeng Chen Fudan group's English-language reporting of work that originally appeared in Chinese-language conference proceedings — the partial-execution disclosure from comp-020 §4.3 still applies.
- No subagent contamination: brief read, scope respected, no compounds added from speculation.

## Time budget

Target 45-60 min. Actual: see `outputs/summary.md`.

## Outputs

- [`inputs/compound-list.json`](inputs/compound-list.json) — compounds in scope.
- [`inputs/assay-formats.json`](inputs/assay-formats.json) — 6-format taxonomy with metadata fields.
- [`inputs/provenance.md`](inputs/provenance.md) — per-IC50 verification table.
- [`outputs/matrix.json`](outputs/matrix.json) — compound × assay × IC50 matrix.
- [`outputs/summary.md`](outputs/summary.md) — uncertainty-collapse analysis, gut-luminal-relevance scoring, comp-029 re-run sensitivity.
- [`analyze.py`](analyze.py) — stdlib-only Python; reads the matrix and emits the summary.
- Wiki page: [`wiki/upstream-complement-assay-format-mapping-computational.md`](../../wiki/upstream-complement-assay-format-mapping-computational.md) — ≤60-line tight stub.

## Reproducibility

```bash
cd experiments/comp-021-upstream-complement-assay-format-mapping
python3 analyze.py  # reads inputs/* and outputs/matrix.json, emits outputs/summary.md
```

This is a literature-curation experiment with a small analysis layer. Reproducing means re-pulling primary papers and re-grep-verifying the IC50 values listed in `inputs/provenance.md`.
