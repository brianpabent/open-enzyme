# comp-034 — Inputs Provenance

Every input file with source, fetch date, and citation. Per CLAUDE.md Rule 4 (pre-commit grep-verify gate), every load-bearing number used by `analyze.py` is traceable to an entry below.

## `P02788.fasta`
- **Source:** UniProt KB entry P02788 (TRFL_HUMAN, Lactotransferrin), copied unchanged from `experiments/comp-005-lactoferrin-shio-koji-protease-stability/inputs/P02788.fasta`.
- **Sequence version:** 6 (last sequence update 24-JAN-2006; entry version 268, 28-JAN-2026).
- **Length:** 710 aa (signal peptide 1–19, mature chain 20–710).
- **Verified 2026-05-16** against UniProt REST (rest.uniprot.org/uniprotkb/P02788.txt) — header `ID TRFL_HUMAN Reviewed; 710 AA.`

## `alphafold_P02788_plddt.json`
- **Source:** AlphaFold DB model AF-P02788-F1-model_v6, per-residue pLDDT column extracted to JSON dict (1-indexed, string keys).
- **Copied unchanged** from `experiments/comp-005-lactoferrin-shio-koji-protease-stability/inputs/alphafold_P02788_plddt.json`.
- **Linker region (residues 353–363, UniProt numbering) pLDDT:** 95.12, 93.38, 94.69, 95.75, 94.50, 95.25, 96.25, 96.75, 95.44, 96.88, 97.75. **All high — well-folded helix**, NOT the disordered loop framing in the brief.
- **Verified 2026-05-16** by direct read of the JSON file; values match comp-005 inputs.

## `a_oryzae_codon_usage.json`
- **Source:** Copied unchanged from `experiments/comp-022-clockbase-uricase-cassette-ranking/inputs/a_oryzae_codon_usage.json`.
- **Primary references:** Kazusa Codon Usage Database (A. oryzae entry); Nakao Y et al. Nucleic Acids Res 1992;20 Suppl:2117 (PMID 1482437); Machida M et al. Nature 2005;438:1157-61 (PMID 16372010).
- **GC content of coding regions:** ~54%.
- **Verified 2026-05-16** by direct read; codon table loads correctly via Python json.load.

## `linker_residue_range.json` (authored fresh)
- **Linker boundary (UniProt 353–363):** Verified against UniProt P02788 FT DOMAIN annotations 2026-05-16:
  - `FT DOMAIN 25..352` (N-lobe)
  - `FT DOMAIN 364..695` (C-lobe)
  - The 11-residue gap 353–363 is the inter-lobe linker.
- **Mature-protein numbering 334–344:** Derived from UniProt 353–363 minus 19 (the signal peptide cleavage offset, `FT SIGNAL 1..19` + `FT CHAIN 20..710`).
- **WT linker sequence `SEEEVAARRAR`:** Extracted from positions 353–363 of `P02788.fasta`; cross-verified against the AlphaFold structure context (residue 352 = K, residue 364 = V).

### Multi-source reconciliation: linker boundary

- **UniProt P02788 domain features** say N-lobe is 25–352, C-lobe is 364–695 → linker is 353–363 (11 residues).
- **Wiki page `wiki/lactoferrin.md` §3.1** says N-lobe is residues 1–333 and C-lobe is residues 345–703 — this is **mature-protein numbering**, with the chain renumbered starting at the cleaved N-terminus (UniProt position 20 = mature position 1). Subtracting 19: 1–333 mature = 20–352 UniProt, 345–703 mature = 364–722 UniProt. The end-residue 703 mature would be 722 UniProt but mature ends at 710 UniProt — minor mismatch in the wiki text but the **lobe boundaries agree** (mature 333 ≈ UniProt 352; mature 345 ≈ UniProt 364). The 11-residue gap in mature numbering is 334–344 (= UniProt 353–363).
- **Brief framing** ("~residues 333–345 in bovine, ~residues 333–344 in human, depending on numbering") matches the mature-protein numbering convention to within ±1, and is internally consistent.
- **PDB 1B0L** (diferric hLf, 2.2 Å resolution; Sun et al. 1999 PMID 10089347 used 1B0L for refinement) covers residues 20–710 (no signal peptide) with all linker residues resolved. Residues 353–363 are visible as a structured α-helix/turn.

### Resolution: this experiment uses **UniProt numbering (353–363)** as the canonical reference and reports mature-protein numbering (334–344) as a parallel coordinate system for biologists who prefer that convention. Both conventions appear side-by-side in `outputs/candidates.json` and `outputs/summary.md`.

## Inputs intentionally NOT included

- **comp-005 `cleavage_sites.json`** — referenced (not copied) at `../comp-005-lactoferrin-shio-koji-protease-stability/outputs/cleavage_sites.json`. Verified that NONE of comp-005's top-5 ALP exposed sites land within residues 353–363 — the WT linker is not the most vulnerable region. The redesign rationale therefore is **precautionary** (improve a plausible secondary vulnerability) rather than corrective (fix a clear-cut primary cleavage site).
- **comp-005 `protease_specificities.json`** — referenced (not copied) at `../comp-005-lactoferrin-shio-koji-protease-stability/inputs/protease_specificities.json`. Per CLAUDE.md "shared library lockdown" we re-use the comp-005 reference unchanged.

## Multilingual sources checked

Per CLAUDE.md "Global-multilingual research by default":

- **J-STAGE (jstage.jst.go.jp)** — searched for ラクトフェリン × 麹菌 × タンパク質発現 × プロテアーゼ. Recovered: oleoscience 23(8):423 (2023) review of lactoferrin biology (Japanese); nskkk 53(3):193 review; Gekkeikan brewery R&D notes on A. oryzae proteolysis. None address linker engineering specifically. The hLf-in-A.oryzae secretion at 25 mg/L (Ward 1992 PMID 1368268) and the Sun 1999 fungal-expression structural confirmation are cited in the English literature; no Japanese-language follow-up on linker engineering surfaced.
- **CiNii (ci.nii.ac.jp)** — searched for the same Japanese terms. No additional precedent on inter-lobe linker variant design for A. oryzae or other expression systems.
- **CNKI / WanFang (Chinese)** — searched for 乳铁蛋白 × 米曲霉 × 表达 × 蛋白酶. Cellular Chinese journals confirm A. oryzae lactoferrin expression as a topic of industrial interest (largely from Hebei + Shandong dairy biotech groups, ~2018-2023) but again no specific linker-redesign precedent.
- **Conclusion:** the inter-lobe linker redesign space for shio-koji-environment protease resistance appears genuinely unpublished. comp-034 is novel-ground in the cross-language literature, not just the English literature.

No language barrier flagged; all non-English sources read directly. Translation cross-check (per CLAUDE.md §"Translation protocol") was not load-bearing here because no quantitative claim from a non-English source landed in the experiment outputs — the multilingual scan confirmed *absence* of prior art rather than recovering a load-bearing number.
