# Input Provenance — comp-024

| File | Source | Version / Date fetched | URL |
|---|---|---|---|
| `bgc_architecture.json` | MIBiG BGC0000326 + Chiu HT et al. PNAS 2001 PMID 11447274 (PMC37473 full text) + Park JW et al. ChemBioChem 2016 PMID 27383040 | Hand-encoded from canonical primary literature; fetched 2026-05-16 | https://www.pnas.org/doi/10.1073/pnas.151246498 ; https://mibig.secondarymetabolites.org/repository/BGC0000326/ |
| `chassis_profiles.json` | Synthesized from canonical microbiology references — E. coli Nissle 1917 (Sonnenburg lab toolkit; Synlogic precedent literature); Bacteroides thetaiotaomicron VPI-5482 reference; F. prausnitzii A2-165 reference | Hand-encoded 2026-05-16 | Multiple |

## BGC identity
- **Compound family:** Complestatin / chloropeptin / isocomplestatin (closely related NRPS-derived cyclic peptides; same structural class)
- **MIBiG ID:** BGC0000326 (isocomplestatin from *S. lavendulae*)
- **Producer:** *Streptomyces lavendulae* (also *S. chartreusis* AN1542 per Park 2016)
- **Cluster size:** 48.7 kb in the originally cloned sequence (Chiu 2001); 54.5 kb in the *S. lividans* TK24 reconstituted cosmid (Park 2016)
- **Total ORFs:** 16
- **NRPS genes:** *comA*, *comB*, *comC*, *comD* (4 polypeptides encoding 7 modules: 1 loading + 6 extension + terminal thioesterase)
- **Tailoring enzymes:** *comI*, *comJ* (P450 oxidative phenolic coupling); *comH* (nonheme halogenase); ferredoxins; β-hydroxylase (OxyD-type, inferred)
- **Non-canonical AA biosynthesis genes:** *hmaS*, *hmo*, *hpgT*, *pd* (4-hydroxyphenylglycine pathway from tyrosine)
- **Regulatory + transporter:** putative transcriptional regulator + *comL* (ABC transporter / self-resistance)

## Heterologous expression precedent
- ***S. lividans* TK24:** successful (Park 2016 PMID 27383040). Phylum-internal (Actinomycetota → Actinomycetota). Yields sub-mg/L without optimization. Used to generate the complestatin M55 / S56 monocyclic deletion derivatives via ComI/ComJ P450 knockout.
- ***E. coli*:** no precedent for the full complestatin cluster. Individual NRPS modules (including a Hpg-loading module from the related chloroeremomycin cluster, Trauger & Walsh 2000 PNAS PMID 10737789) have been expressed in *E. coli* with Sfp PPTase coexpression. Full megacluster (>30 kb) NRPS expression in *E. coli* remains a major engineering challenge.
- ***Bacteroides* or other obligate anaerobes:** no precedent for any complestatin-class compound. No NRPS megacluster (>30 kb) heterologous expression precedent in *Bacteroides* in the published literature.

## Comparator: C1-INH recombinant expression
- **Protein:** single-chain serpin (SERPING1), 478 aa mature, heavily N- and O-glycosylated
- **Approved forms:** plasma-derived (Berinert, Cinryze); recombinant rabbit-milk transgenic (Ruconest / conestat alfa)
- **Pichia pastoris developmental titers:** ~0.5–2 g/L reported; full inhibitory activity retained after glycoengineering
- ***E. coli*:** very low feasibility — aglycosylated recombinant C1-INH from *E. coli* is poorly secreted and rapidly cleared in vivo (pattern shared with other serpins)
- ***E. coli* Nissle 1917 as LBP-chassis:** new framing — continuous luminal release dodges the plasma-half-life problem that drives the Pichia glycoengineering effort. Protease vulnerability in the gut lumen is the load-bearing concern, parallel to the comp-006 DAF/CD55 stalk-driven HIGH risk verdict.

## Key load-bearing numbers (pre-commit grep-verified)
- **48.7 kb cluster size (original clone):** Chiu HT et al. PNAS 2001;98(15):8548-53 — verified from PMC37473 full text via WebFetch 2026-05-16
- **54.5 kb cluster size (S. lividans reconstituted):** Park JW et al. ChemBioChem 2016;17(15):1442-7 PMID 27383040 — verified from WebSearch 2026-05-16
- **16 ORFs:** Chiu 2001 PMC37473 — verified
- **7 NRPS modules (1 loading + 6 extension + TE):** Chiu 2001 PMC37473 — verified
- **4 Hpg-biosynthesis genes (hmaS, hmo, hpgT, pd):** Chiu 2001 PMC37473 — verified
- **GC content Streptomyces lavendulae ~72%:** typical for genus (canonical microbiology reference; not patient-load-bearing)
- **GC content E. coli Nissle 1917 ~50.7%:** canonical reference genome value
- **GC content B. thetaiotaomicron ~42.8%:** canonical reference genome value (Xu J et al. Science 2003 PMID 12663928)

## Limitations of input data
- Module-by-module substrate specificity predictions for the complestatin NRPS are partly inferred from sequence homology to vancomycin/chloroeremomycin-class NRPSs (Trauger & Walsh 2000); not all A-domain specificity codes are individually validated in vitro for complestatin specifically.
- The β-hydroxytyrosine biosynthesis gene is inferred (OxyD-class P450) but not explicitly annotated in the original Chiu 2001 cluster description; this is a known gap.
- Codon Adaptation Index (CAI) numbers in `chassis_profiles.json` are rough estimates from genus-typical codon-usage tables; actual codon-optimized cassettes can vary ±0.1 in CAI from the values shown.
- The "no precedent for *Bacteroides* NRPS megacluster expression" claim is a negative-evidence statement; absence of precedent does not prove infeasibility, only that no validated path exists today.
- C1-INH titer ranges in *Pichia* (0.5–2 g/L) are from secondary-source summaries, not full-text verified to a specific primary publication.
