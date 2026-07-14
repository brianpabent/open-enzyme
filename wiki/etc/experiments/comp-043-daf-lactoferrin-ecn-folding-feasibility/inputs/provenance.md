# Provenance — comp-043 inputs

comp-043 reuses the frozen sequence + AlphaFold inputs of comp-005 (lactoferrin), comp-006
(DAF/CD55) and comp-037 (C1-INH), plus the comp-037 colonic-EcN protease panel, so all three
payloads are scored under one harmonized environment. Every disulfide count and every Cys position
below was **re-verified against the primary UniProt flatfile on 2026-07-13** (not merely inherited).

## Disulfide counts — grep-verified against UniProt (2026-07-13)

Fetched `https://rest.uniprot.org/uniprotkb/<ACC>.txt` and counted `^FT   DISULFID`:

| Payload | UniProt | `grep -c '^FT   DISULFID'` | Notes |
|---|---|---|---|
| C1-INH (SERPING1) | P05155 | **2** | C123-C428, C130-C205 (canonical serpin) |
| DAF / CD55 | P08174 | **8** | 36-81, 65-94, 98-145, 129-158, 163-204, 190-220, 225-267, 253-283 — 2 per Sushi domain, all within SCR1-4 (aa 35-285) |
| Lactoferrin (LTF) | P02788 | **16** | bilobal; long-range C-lobe bonds 424-705, 446-668, 502-696 |

Each `(a,b)` pair is asserted in `analyze.py` (`seq[a-1] == 'C' and seq[b-1] == 'C'`), and the
per-payload count is asserted against the expected value. The run aborts if any assertion fails.
This is the CLAUDE.md Rule 4 pre-commit grep-verify gate — the same gate whose absence produced the
2026-05-06 DAF SCR1-4 disulfide-count hallucination ("12 disulfides"); the correct count is 8.

## Sequence + AlphaFold inputs (reused, frozen)

| File | Source | Provenance |
|---|---|---|
| `P05155.fasta` + `alphafold_P05155_plddt.json` | UniProt P05155 (SV=2, 500 aa) + AF-P05155-F1-model_v6 | copied from comp-037 inputs (originally fetched 2026-05-17) |
| `P08174.fasta` + `alphafold_P08174_plddt.json` | UniProt P08174 (SV=4, 381 aa) + AF-P08174-F1-model_v6 | copied from comp-006 inputs (originally fetched 2026-05-05) |
| `P02788.fasta` + `alphafold_P02788_plddt.json` | UniProt P02788 (SV=6, 710 aa) + AF-P02788-F1-model_v6 | copied from comp-005 inputs (originally fetched 2026-05-05) |

## `colonic_ecn_protease_panel.json`

Copied verbatim from comp-037 (`protease_specificities.json`). Five-protease colonic-luminal EcN
panel: pancreatic trypsin (S01.151), chymotrypsin (S01.001), elastase (S01.153) at residual colonic
activity; EcN outer-membrane OmpT (A26.001, di-basic P1-P1'); EcN periplasmic DegP/HtrA (S01.273).
Conditions: colonic lumen pH 6-7, 37 C, ~0.15 M NaCl (salt inhibition negligible). Bile-acid and
commensal-microbiome protease load out-of-model. The shared-library JSON key `shio_koji_conditions`
is retained for API compatibility but carries colonic-lumen values. Panel source citations
(MEROPS 12.4; Dekker 2001 PMID 11226160; Krojer 2008 PMID 18261546; Schechter & Berger 1967;
Largman 1976 PMID 988044; Fallingborg 1999 PMID 10204470) are documented in comp-037's provenance.

## `disulfide_topology.json`

Grep-verified DISULFID pairs, sushi/lobe boundaries, N-glyc sites, engineering-construct boundaries,
and folded-core / RCL regions for the three payloads. All positions are UniProt full-sequence
numbering. N-glyc site counts grep-verified against `^FT   CARBOHYD`: C1-INH 7 N-sites, DAF 1 (N95),
lactoferrin 3 (N156/N497/N642).

## Axis-1 capacity anchors — NOT measurements (load-bearing honesty note)

The DsbA/DsbC reference-capacity band (conservative 5.0 / moderate 8.0 / optimistic 12.0, in
architecture-weighted effective-demand units) is derived from E. coli periplasmic-expression
**precedent**, not from any measured DsbA/DsbC oxidative-folding capacity:

- **5.0** — certolizumab pegol (Cimzia) Fab', an industrially-manufactured secreted periplasmic
  E. coli therapeutic with ~5 disulfides (mostly local). The demonstrated routine ceiling for a
  functional secreted disulfide-bonded protein in a near-wild-type periplasm.
- **8.0** — Fab-class precedent + credit for DsbC-isomerase co-expression.
- **12.0** — engineered oxidizing strains (SHuffle: trxB/gor knockout + cytoplasmic DsbC). Set
  deliberately BELOW full aglycosyl-IgG (16 disulfides), which is a low-yield heavily-engineered
  achievement, not a "routinely viable LBP payload" bar.

**Per `chaperone-orthogonal-stacking.md` §8 item 8, no published DsbA/DsbC capacity metric exists at
the 8-16 disulfide scale.** The band is the single biggest optimistic assumption in this analysis
and is sensitivity-tested across all three anchors; the DAF SCR1-4 verdict is PROVISIONAL precisely
because its viability flips across the band.
