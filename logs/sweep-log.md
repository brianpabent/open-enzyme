# Doc Sweep Log

Records of when findings from ai-analysis/ were propagated to docs/ and wiki/.

---

## Sweep: April 21, 2026

**Trigger:** Initial creation of 8 analysis files (01–08) from Bio AI Tools Playbook prompts.

**Files checked:** All 8 ai-analysis files (01 through 08).

**Docs updated:**
- `docs/engineered-yeast-uricase-proposal.md` — Added "AI Analysis Updates — April 2026" section with variant selection, GI survival (36-42%), protein engineering tiers (SB-1/BAL-1/OPT-1), expression cassette (TDH3p, intracellular, ADH1t), cross-validation (5.8/10 feasibility)
- `docs/nlrp3-exploit-map.md` — Added "AI Analysis Updates — April 2026: Microbial Production Candidates" with ursolic acid (8.59 g/L), quercetin (930 mg/L), carnosine (hyperuricemia data), taurine, kojic acid (flagged for screening), potency gap analysis
- `docs/engineered-koji-protocol.md` — Added "AI Analysis Updates — April 2026" with amyB promoter, codon optimization (48-52% GC), yield predictions (40-80 mg/g), RIB40 strain, fermentation optimization, CRISPR tglA plan

**Wiki pages updated:**
- `wiki/INDEX.md` — Added "AI Analysis (April 2026)" section with all 8 entries
- `wiki/uricase.md` — Variant comparison, GI survival, mutation tiers
- `wiki/nlrp3-inflammasome.md` — Production candidates, kojic acid screening flag
- `wiki/saccharomyces-cerevisiae.md` — Expression cassette recommendation
- `wiki/aspergillus-oryzae.md` — amyB promoter, yield, RIB40, dose equivalence
- `wiki/digestive-enzymes.md` — Fermentation optimization, CRISPR tglA

**Not updated (no relevant new findings):**
- `docs/gout-deep-dive.md` — No new pathophysiology data
- `docs/open-enzyme-vision.md` — No changes to vision/strategy
- `docs/blood-barrier-exploits.md` — No new barrier biology
- `docs/enzyme-deficit-deep-dive.md` — No new epidemiology
- `docs/peptide-gout-addendum.md` — No new peptide data
- `wiki/GRAPH.md` — Should be updated in next sweep (new nodes: ursolic acid, carnosine, kojic acid, protein engineering tiers)

**Known gaps for next sweep:**
1. `wiki/GRAPH.md` needs new Mermaid nodes for ursolic acid, carnosine, kojic acid, and the SB-1/BAL-1/OPT-1 variants
2. Validation experiments page (`wiki/validation-experiments.md`) should incorporate the de-risking experiments from cross-validation (05)
3. Bio-AI tools wiki page (`wiki/bio-ai-tools.md`) should reference the ai-analysis outputs as examples of completed analysis
