# comp-022 inputs: provenance

All inputs grep-verified against primary sources before commit per CLAUDE.md Rule 4.

## Q00511.fasta: A. flavus uricase (uaZ)

- **Source:** UniProt Q00511, 302 aa, sequence verified 2026-05-05 (carried over from comp-010).
- **Fetch date:** 2026-05-05 (copied from comp-010-cassette-compatibility/inputs/Q00511.fasta).
- **Notes:** Same target gene as comp-001 (protease stability), comp-010 (cassette compatibility). C-terminal SKL = PTS1 peroxisomal targeting signal; flagged by comp-010 as routing risk; secretion scaffolds in this experiment include PTS1-blocking 3xAla and His6 C-terminal tag variants.

## a_oryzae_codon_usage.json: A. oryzae RIB40 codon usage

- **Source:** Codon Usage Database (Kazusa); A. oryzae entry; cross-validated against Nakao et al. 1992 PMID 1482437 and Machida et al. 2005 PMID 16372010 (A. oryzae genome).
- **Fetch date:** 2026-05-05 (copied from comp-010).
- **Notes:** RSCU + freq_per1000 for all 64 codons. Rare-codon threshold: RSCU<0.4 AND freq<10/1000. Used for CAI computation.

## parts_list.json: enumerated combinatorial parts list

- **Promoters (6):** PamyB, PglaA, PenoA, PgpdA, PtefI, PnmtA. Relative strengths assigned from published heterologous-expression literature in A. oryzae / A. nidulans:
  - PamyB: Tada 1991 PMID 1937733; canonical strongest heterologous promoter in A. oryzae.
  - PglaA: Ward 1995 PMID 9634791 (>2 g/L Lf in A. awamori); Huynh 2020 PMC7257131 (39.7 mg/L adalimumab in A. oryzae NSlD-ΔP10).
  - PenoA: Toda 2001; A. oryzae enolase promoter characterization; constitutive strong.
  - PgpdA: Punt 1990 PMID 2113023; A. nidulans GAPDH; constitutive moderate; widely used for selection markers.
  - PtefI: Kitamoto 1998; A. oryzae TEF1 promoter; constitutive; used as orthogonal driver in koji-endgame-strain.md §3.4.
  - PnmtA: Shoji 2005; thiamine-repressible; tunable expression; lower industrial deployment.

  **Relative strengths** are bounded estimates from literature. Exact promoter-strength benchmarks vary by host strain (RIB40 vs NSlD-ΔP10), substrate (rice vs submerged), and reporter gene. The relative ranking PamyB > PglaA > PenoA ≈ PtefI > PnmtA > PgpdA is qualitatively consistent across published comparisons (e.g., Tsuchiya 1992, Kitamoto 1998, Shoji 2005); specific quantitative values are bounded estimates not load-bearing for ranking ordinal outcomes.

- **Signal peptides (12):** 6 native A. oryzae / A. niger / T. reesei SPs × 2 pro-region states (with / without). All SP sequences cross-verified against UniProt where possible:
  - SPamyB: UniProt P0C1B3 (A. oryzae α-amylase Taka-amy), aa 1-19 signal peptide annotation.
  - SPglaA: UniProt P69327 (A. niger / A. awamori glucoamylase), aa 1-18.
  - SPpepO: A. oryzae aspergillopepsin O, Kanda 1989; original characterization.
  - SPcbhI: UniProt P00725 (T. reesei cellobiohydrolase I).
  - SPalpA: A. oryzae alkaline protease; Cheevadhanarak 1991.
  - SPlipase (tglA): A. oryzae triacylglycerol lipase; Toida 1995.

  **Pro-region sequences** for native pro-regions (SPglaA_pro, SPpepO_pro, SPalpA_pro, SPlipase_pro) are taken from primary characterization papers. Synthetic pro-regions (SPamyB_pro, SPcbhI_pro) are ablation controls; 6-aa Ala/Pro-rich linker and 8-aa Gly/Ser linker respectively.

- **Codon variants (10):** 10 strategies; native, max-CAI, balanced, max-CAI GC-constrained, harmonized (Angov 2008 PMID 18851725), rare-avoid (comp-010 threshold), low-GC (48%), high-GC (62%), 5'-softened (Kudla 2009 PMID 19359587), 5'-softened-balanced. Each strategy is deterministic given the input AA sequence (Q00511) plus codon table; the analysis script reproduces them.

- **Secretion scaffolds (60):** 10 base scaffolds × 3 propeptide states × 2 N-glyc states = 60.
  - 10 base scaffolds cover direct-secretion (3 C-term tag variants), glaA-full KEX2 fusion (Ward 1995 architecture, 4 KEX2 site / tag variants), glaA-truncated KEX2 fusion (Gouka 1997, 2 variants), tandem-KEX2 (Spencer 1998).
  - 3 propeptide states: none, native target propeptide, synthetic flexible Gly/Ser 10-aa linker.
  - 2 N-glycosylation states: native (NSS sequon at uricase pos 191 retained) vs ablated (N191Q).

## Design-space cardinality

**6 × 12 × 10 × 60 = 43,200 combinations.** Matches the brief's Pass-2 estimate.

## Discipline notes

1. Several literature_use_count_proxy values in parts_list.json are heuristic estimates (order-of-magnitude counts of published heterologous expression studies citing each promoter). They are NOT load-bearing for the ranking ordinal outcome; they appear in the JSON for traceability only.
2. Promoter relative_strength values are bounded estimates from published comparative studies; the analysis treats them as multiplicative priors only and does not use them for the cheap-filter pass (which is purely sequence-driven).
3. Pro-region sequences (especially synthetic ones) are bounded approximations to documented architectures; the analysis treats them as length-equivalents for downstream computation and does NOT depend on exact pro-region sequence identity.
