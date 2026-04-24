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

---

## Sweep: 2026-04-23 14:17

**Trigger:** wiki/cannabinoids-terpenes.md
**Pass 1 updates:** wiki/nlrp3-inflammasome.md, wiki/supplements-stack.md, wiki/oridonin.md, wiki/bhb-ketones.md
**Pass 2 synthesis:** Beta-caryophyllene + BHB may be the evidence-strongest non-pharma gout NLRP3 pairing — direct MSU animal model data that oridonin + BHB lacks; also flagged a systematic Tier-4 audit gap in the inhibitor screen.

## Sweep: 2026-04-23 18:27

**Trigger:** wiki/gout-clinical-pipeline.md
**Pass 1 updates:** wiki/uricase.md, wiki/nlrp3-inflammasome.md, wiki/nlrp3-exploit-map.md, wiki/gout-deep-dive.md, wiki/gout-pathophysiology.md, wiki/GRAPH.md
**Pass 2 synthesis:** Three of the last three industry/academic uricase programs (ALLN-346, SSS11, ACS Synth Bio S. boulardii) chose enzymes other than A. flavus — the wiki's "A. flavus default" inherited from rasburicase may be lagging revealed preference; ALLN-346's termination may have made the 20× protease-resistance mutations public-domain (1-hour patent search could yield free pharma-validated engineering); pharma's gout success is now at CP5 (canakinumab approved Aug 2023) while CP2 stagnates (dapansutrile no Phase 2b/3 in gout) — supplement stack's CP1+CP2 emphasis may be mirroring pharma's *failing* chokepoint.

## Sweep: 2026-04-23 18:38

**Trigger:** wiki/nlrp3-inhibitor-screen.md (ChEMBL IC50 cross-check appendix)
**Pass 1 updates:** wiki/oridonin.md, wiki/nlrp3-exploit-map.md, wiki/nlrp3-inflammasome.md, wiki/supplements-stack.md, wiki/cannabinoids-terpenes.md, wiki/gout-clinical-pipeline.md, wiki/GRAPH.md
**Pass 2 synthesis:** Quercetin's most potent curated ChEMBL activity is 5-LOX (IC50 = 300 nM) — 36× more potent than its cited NLRP3-pathway activity; should be reframed as a 5-LOX inhibitor with NLRP3 side activity, not the reverse. Dapansutrile's 1,000× mouse-vs-human species gap casts suspicion on every mouse-derived IC50 in the wiki — new methodological standard: prefer human-cell IC50 over rodent cellular data; add standing caveat to rodent citations. Two-tier labeling ("direct NLRP3 inhibitor" vs "NLRP3 pathway modulator") aligns with CP5-vs-CP2 pharma track record: Open Enzyme stack is overwhelmingly pathway modulators, and pharma hasn't rigorously tested that class in gout — better positioning than "supplement-grade version of MCC950." Proposed new Chokepoint 2.5 / Parallel Path (5-LOX / LTB4 / Neutrophil Chemotaxis) for exploit map. ChEMBL cross-check should become standing rigor tool on remaining 10–15 stack compounds.
**Note:** Pass 3 log entry added manually; original sweep's Pass 3 hit an API 500 error after Pass 1+2 completed successfully.

## Sweep: 2026-04-24 16:12

**Trigger:** wiki/GRAPH.md, wiki/chembl-cross-check.md, wiki/complement-c5a-gout.md, wiki/nlrp3-exploit-map.md, wiki/self-experiment-protocol.md, wiki/spm-resolution-pathway.md, wiki/tnfsf14-gout-target.md
**Diff base:** 9d09dcbad8992fbd1416f4034e86302001d80f7b
**Pass 1 updates:** wiki/nlrp3-inflammasome.md, wiki/gout-pathophysiology.md, wiki/supplements-stack.md, wiki/index.md, index.md
**Pass 2 synthesis:** DHA should be prescribed over EPA for gout (RvD1/MaR1 direct MSU animal model evidence + TNFSF14/LIGHT inverse association); current supplement-stack EPA-heavy recommendation is unsupported by gout-specific SPM literature — immediate correction needed. EGCG spans four chokepoints via proteasome→IκBα mechanism (86 nM) + CP1a TNFSF14 suppression — widest-spectrum natural compound in stack. Self-experiment protocol misses CP0 (serum C5a) and CP6a (urinary LTB4) biomarkers. Zileuton (FDA-approved 5-LOX inhibitor) is the closest pharma-grade CP6a analog with zero gout trials — low-cost off-label candidate.
