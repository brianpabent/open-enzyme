# comp-009 — URAT1 mRNA target site selection — Summary (RERUN 2026-07-14)

**Transcript:** NM_144585.4 (2792 nt; CDS 338-1999). **Accessibility:** real ViennaRNA RNAplfold (u=21, W=80, L=40).

> **This is a rerun.** The original comp-009 scanned an artificial back-translated CDS and its guide sequences did not map to the real transcript. This run uses the real NM_144585.4 mRNA (5'UTR + CDS + 3'UTR) and real local-accessibility folding.

## Pipeline

- Sliding 21-nt windows over the full mRNA: **2711** scored.
- Reynolds GC 30-52%: **222** survive.
- Immunogenicity (TLR7/8 + GU-rich): **120** survive (kills 102).
- 4-nt homopolymer exclusion: **76** survive.
- Reynolds ≥5/8 AND Ui-Tei AU≥4/7: **31** survive.
- Composite ranking + 60-nt diversity: **8**-candidate shortlist (regions: {"5'UTR": 1, 'CDS': 6, "3'UTR": 1}).

## Verdict

**GREEN (target-site availability only) — multiple viable real-transcript target sites.**

8 candidate sites on the real NM_144585.4 mRNA survive Reynolds GC, Ui-Tei seed asymmetry, TLR/GU-rich immunogenicity, homopolymer exclusion, and rank on real RNAplfold accessibility. The H03 target-site-availability assumption is **supported on the real transcript** — but this is target-site availability ONLY, not a validated knockdown guide: **no off-target clearance was performed** (see Limitations), and cross-species reuse is an amino-acid-level hint, not a nucleotide-level claim.

## Top shortlist

| Rank | mRNA pos | Region | Sense target (5'→3') | GC% | Reynolds | P(unpaired) | Cons hint | Score |
|---|---|---|---|---|---|---|---|---|
| 1 | 1029 | CDS | `CCUUGGUGAUGACCUUGAACU` | 47.6 | 7/8 | 0.0007 | 95.2% | 65.54 |
| 2 | 1468 | CDS | `CAUCUUCCUGCUCCAAAUGUU` | 42.9 | 6/8 | 0.0021 | 90.5% | 62.53 |
| 3 | 438 | CDS | `AGAGCAUGCUGGAGAACUUCU` | 47.6 | 5/8 | 0.0 | 90.5% | 56.59 |
| 4 | 865 | CDS | `AACCUGGAGCUACCUUCAGAU` | 47.6 | 5/8 | 0.0 | 90.5% | 56.59 |
| 5 | 752 | CDS | `UGUGACUCUCAUGCUCUGAAG` | 47.6 | 5/8 | 0.0011 | 76.2% | 50.2 |
| 6 | 1932 | CDS | `ACCAGGCAGUAAAGAAGGCAA` | 47.6 | 5/8 | 0.0022 | 71.4% | 48.79 |
| 7 | 2025 | 3'UTR | `GGUCAGAGGAAGAGACUUCUU` | 47.6 | 6/8 | 0.0 | 0.0% | 33.2 |
| 8 | 326 | 5'UTR | `UGAGUAGGUUCCAUGGCAUUU` | 42.9 | 6/8 | 0.0047 | 0.0% | 31.18 |

## Limitations (correctly scoped)

1. **No off-target clearance.** No seed-region (antisense pos 2-8) search against the human RefSeq transcriptome / 3'UTRome was performed (no local transcriptome BLAST DB in this environment). Guides are **target-site candidates only**, not off-target-cleared.
2. **Conservation is an amino-acid REGION HINT** from the ortholog protein set, not a nucleotide-level alignment of ortholog mRNAs. A shared amino acid can differ at the wobble position, so cross-species siRNA reuse must be re-verified on real ortholog transcripts.
3. **Accessibility** is RNAplfold local-window folding (Tafer 2008 correlation r≈0.6-0.7 with measured knockdown) — good for prioritisation, not absolute knockdown prediction.
4. **Isoform:** transcript variant 1 (NM_144585.4) only; other SLC22A12 isoforms not scanned.
