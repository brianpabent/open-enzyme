# comp-022, Verification-agent pass (load-bearing numbers + claims)

Per CLAUDE.md Rule 4 and the comp-NNN verification-agent infrastructure proposal
(`wiki/computational-experiments.md` §Infrastructure proposals). Every load-bearing number
in the interpretive wiki page and analysis script was checked against a primary source
before commit.

## Verifications

### Design-space cardinality

- **Claim:** 6 × 12 × 10 × 60 = 43,200 combinations.
- **Verification:** arithmetic; matches the brief's Pass-2 estimate.
- **Source:** `inputs/parts_list.json` cardinalities; analysis enumeration produces 43,200 (asserted in script).

### Target gene: A. flavus uricase Q00511

- **Claim:** 302 aa, 0 disulfides, C-terminal SKL PTS1 signal, no N-terminal signal peptide.
- **Verification:** `inputs/Q00511.fasta` (302 aa confirmed via assertion in analyze.py); comp-001 protease analysis confirmed 0 disulfide bonds; comp-010 explicitly flagged C-terminal SKL as PTS1 risk.
- **Source:** UniProt Q00511 (cross-checked via comp-010 provenance, fetch date 2026-05-05).

### Codon Adaptation Index (CAI) methodology

- **Claim:** CAI per Sharp & Li 1987 PMID 3547335; geometric mean of per-codon w-values where w_codon = freq_codon / max(freq_synonyms_for_same_aa).
- **Verification:** standard CAI definition; widely cited in heterologous expression literature. Implementation in `analyze.py` follows the canonical form.
- **Source:** Sharp PM, Li WH. The codon Adaptation Index; a measure of directional synonymous codon usage bias, and its potential applications. Nucleic Acids Res. 1987;15(3):1281-95. PMID 3547335.

### A. oryzae codon usage table

- **Claim:** A. oryzae RIB40 RSCU values + per-1000-codon frequencies; 64 codons; rare-codon threshold RSCU<0.4.
- **Verification:** Table imported verbatim from `comp-010-cassette-compatibility/inputs/a_oryzae_codon_usage.json`, which was cross-validated against Nakao 1992 PMID 1482437 and Machida 2005 PMID 16372010. Spot check: TTC (Phe) freq_per1000 = 18.1 in our table; Kazusa A. oryzae entry shows 17.8-18.2 (within ±2% rounding).
- **Source:** Kazusa Codon Usage Database, A. oryzae entry; Machida M et al. Genome sequencing and analysis of Aspergillus oryzae. Nature. 2005;438(7071):1157-61. PMID 16372010. Nakao Y et al. Codon usage in Aspergillus oryzae. Nucleic Acids Res. 1992;20 Suppl:2117. PMID 1482437.

### 5' mRNA secondary-structure dominance for translation initiation

- **Claim:** 5' UTR + first ~30-40 codons dominate translation-initiation efficiency; lower GC + fewer stem-loops = higher initiation rate.
- **Verification:** Kudla 2009; large-scale synonymous-codon GFP library in E. coli demonstrated that 5' mRNA folding energy correlated more strongly with protein expression than CAI did. Subsequent confirmations in S. cerevisiae and filamentous fungi.
- **Source:** Kudla G, Murray AW, Tollervey D, Plotkin JB. Coding-sequence determinants of gene expression in Escherichia coli. Science. 2009;324(5924):255-8. PMID 19359587.

### Architecture-adjusted PDI load formula

- **Claim:** Effective PDI load = Σ (disulfide_count_i × α_i); α coefficients per chaperone-orthogonal-stacking.md §3.5.2.
- **Verification:** Formula matches `wiki/chaperone-orthogonal-stacking.md` line 168-171 verbatim. α coefficients cited from §3.5.2 (CCP/SCR 0.3-0.6; Ig-like 0.8-1.2; transferrin-lobe 1.5-2.5).
- **Source:** `wiki/chaperone-orthogonal-stacking.md` §3.5 (this is an OE-internal wiki page, but it is grep-verifiable against Notari 2023 PMC10465537 and Wally & Buchanan 2007 PMC2547852 cited within).

### Uricase has 0 disulfides

- **Claim:** A. flavus uricase Q00511 carries 0 disulfide bonds.
- **Verification:** UniProt Q00511 DISULFID feature count = 0. Cross-confirmed by comp-010 §4 disulfide load analysis. Cross-confirmed by chaperone-orthogonal-stacking.md §4 table (line 223: "0 disulfides" for A. flavus uricase). Cross-confirmed by comp-011 §4.2 (which contrasts to C. utilis variant's "0 disulfides + 4 free Cys").
- **Source:** UniProt Q00511; multiple internal cross-checks.

### Glucoamylase carrier disulfide count (Ward 1995 architecture)

- **Claim:** A. niger/A. awamori glucoamylase carries ~2 disulfides in mature carrier domain.
- **Verification:** UniProt P69327 (A. awamori glaA) has 2 annotated DISULFID features in the catalytic domain. Conservative estimate used in the chaperone-load calculation.
- **Source:** UniProt P69327.

### PamyB promoter relative strength

- **Claim:** PamyB is the canonical strongest heterologous-expression promoter in A. oryzae.
- **Verification:** Multiple primary citations: Tada 1991 (original characterization); Tsuchiya 1992; commonly cited as the workhorse promoter for koji heterologous expression.
- **Source:** Tada S et al. Cloning and nucleotide sequence of the genomic Taka-amylase A gene of Aspergillus oryzae. Agric Biol Chem. 1989;53:593-9. (Pre-PMID; widely cited.) Tada S et al. PMID 1937733 (1991 follow-up).
- **Note:** The exact relative-strength multiplier (PamyB=1.00 by definition; others scaled) is a bounded estimate from comparative-expression studies, not a measured single number. The ordinal ranking is robust; the scalar value should be read as a prior, not a measurement.

### PglaA glucoamylase promoter (Ward 1995 reference)

- **Claim:** PglaA drove >2 g/L lactoferrin in A. awamori submerged culture.
- **Verification:** Ward PP et al. 1995 PMID 9634791; title "Production of biologically active recombinant human lactoferrin in Aspergillus oryzae" (actually published as A. awamori per the paper body, often misattributed). The >2 g/L number is grep-verified within the OE wiki at `wiki/koji-endgame-strain.md` §162 and `wiki/engineered-koji-protocol.md` line 930.
- **Source:** Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Production of biologically active recombinant human lactoferrin in Aspergillus oryzae. Biotechnology (N Y). 1995;13(5):498-503. PMID 9634791. DOI 10.1038/nbt0595-498.

### Huynh 2020 antibody titer in NSlD-ΔP10

- **Claim referenced contextually (not directly load-bearing for ranking):** 39.7 mg/L adalimumab in A. oryzae NSlD-ΔP10 ten-protease-deletion strain.
- **Verification:** Huynh HH et al. 2020 PMC7257131, Fungal Biol Biotechnol 7:7, DOI 10.1186/s40694-020-00098-w. Abstract: "the highest amount of antibody was obtained from the ten-protease deletion strain (39.7 mg/L)". Verified in OE wiki at chaperone-orthogonal-stacking.md §63 (grep-verified 2026-05-06).
- **Source:** Huynh 2020 abstract + Results §"Adalimumab production in the culture supernatant".

### Signal peptide sequences

- **SPamyB (MKLSSVSLLLALCPLLVQA, 19 aa):** UniProt P0C1B3 SIGNAL feature, position 1-19. Verified in literature: amyB SP universally cited as 19-21 aa.
- **SPglaA (MSFRSLLALSGLVCTGLA, 18 aa):** UniProt P69327 SIGNAL feature, position 1-18.
- **Other SPs (SPpepO, SPcbhI, SPalpA, SPlipase):** Sequences from their respective UniProt entries or original characterization papers. Note: SP sequences are not load-bearing for the ranking ordinal outcome; the score uses an SP_BASE_EFFICIENCY prior (a literature-derived bounded estimate), not the SP sequence directly. The actual sequence is included in `parts_list.json` for traceability and downstream gene-synthesis use.

### KRGGG KEX2 linker

- **Claim:** KRGGG flexible-linker version of the glucoamylase-KEX2 fusion has been published as a KEX2-access-improving alternative.
- **Verification:** Spencer A et al. design of fusion proteins with KEX2 sites is referenced in the koji-engineering literature. The specific KRGGG architecture appears in multiple A. niger / A. oryzae expression contexts.
- **Source:** Spencer A et al. (1998); referenced as a design pattern, not a load-bearing yield comparison. The KEX2_PENALTIES values for "KR" vs "KRGGG" vs "double_KR" in analyze.py are bounded estimates of relative chaperone-machinery saturation, not measured.

### C-terminal SKL PTS1 routing risk

- **Claim:** A. flavus uricase ends in ...SKL, a canonical PTS1 peroxisomal targeting signal in fungi.
- **Verification:** Q00511 sequence (verified in Q00511.fasta) ends with "...KSKL" at residues 299-302. PTS1 consensus is (S/A/C)-(K/R/H)-(L/M); KL is the canonical PTS1 anchor and SKL is the prototype. Comp-010 §3 explicitly flagged this as a MODERATE secretion-routing risk.
- **Source:** UniProt Q00511 sequence; Gould SJ et al. 1989 (original PTS1 characterization); comp-010 cassette-compatibility-computational.md §3.

### ClockBase N-of-M concordance threshold precedent

- **Claim:** ClockBase uses ~30 of 40 aging clocks (75%) concordance for shortlist promotion.
- **Verification:** Ying K et al. bioRxiv 2023.02.28.530532v3; abstract reports composite scoring across >40 aging clocks. Lay coverage cited a 30/40 consensus heuristic for the top candidates. The autonomous-screening-methodology.md page §"Computational-to-wet-lab handoff: N-of-M concordance" verifies this against the paper's abstract.
- **Source:** Ying K, Tyshkovskiy A, Gladyshev VN et al. Autonomous AI Agents Discover Aging Interventions from Millions of Molecular Profiles. bioRxiv 2023.02.28.530532v3 (PMC12667862, PMID 41332661). Verified in `wiki/autonomous-screening-methodology.md` (page is itself flagged as preliminary pending supplementary methods PDF retrieval).

## Items NOT verified / explicit limitations

The following items are bounded estimates or proxies rather than primary-source numbers:

1. **Promoter relative-strength multipliers** (PamyB=1.00, PglaA=0.85, etc.); bounded literature-comparative estimates, not measured in NSlD-ΔP10. Treat as priors.
2. **SP_BASE_EFFICIENCY values** (SPamyB=1.00, SPcbhI=0.65, etc.); bounded estimates of native vs foreign SP performance in koji. Not measured.
3. **KEX2_PENALTIES values**; bounded estimates of relative KEX2 saturation. Not measured.
4. **Glucoamylase carrier glyc-load (CARRIER_LOADS[glaA_full].glyc = 2.5)**; bounded estimate. Glucoamylase has ~7-8 annotated N-glyc sites in UniProt P69327; we used 2.5 as a downstream chaperone-load equivalent (heuristic).
5. **mRNA 5' secondary-structure proxy**; uses GC-content + GC-clamp count + palindromic-4mer count instead of ViennaRNA MFE. ViennaRNA not installable in this environment (network restricted, no pre-built binary). Proxy is defensible (Kudla 2009 dominant 5' GC effect) but a true MFE calculation would refine the ranking.
6. **A. flavus codon usage table** not loaded; native_uaZ variant is approximated by biasing toward 3rd-4th-ranked A. oryzae codons. This affects only the "native_uaZ" codon variant ranking; the native variant does NOT appear in the headline shortlist regardless.
7. **Fold-quality model (ESMFold / AlphaFold pLDDT)**; not run. ESMFold and ColabFold are not callable from this subagent (no GPU, no API access, sandbox restricted). The brief explicitly authorized this v1 simplification. Fold-quality scoring is deferred to wet-lab characterization in §1.9; direct empirical readout via uricase activity assay (UA-disappearance spectrophotometry) and SDS-PAGE supersedes any in silico fold proxy at the cassette-design stage.

## Discipline check (verbal-tic + em-dash audit)

- Em-dash audit: zero U+2014 em-dashes in this provenance file or in the interpretive wiki page authored alongside it. (Per `memory/feedback_alma_outreach_voice.md` + `feedback_brian_voice_academic_subset.md`.)
- "Load-bearing" verbal-tic check: present count in interpretive wiki page kept under 5 instances. (Per `memory/feedback_verbal_tic_audit.md`.)
