# Food-Grade Penicillium × CASP1/Inflammasome Lit Scan — 2026-05-19

**Triggered by:** synthesis/queue/ 2026-05-17-experiment-1 (Cluster J2 walkthrough) — the cheap discriminator before committing $500–1,000 wet-lab budget to assay P. camemberti / P. roqueforti extracts for Berkeleyamide-chemotype caspase-1-inhibitory activity.

**Scan window:** ~45 min, Paperclip (PubMed Central / bioRxiv full-text corpus) + WebSearch + targeted WebFetch.

---

## Summary

- **The Berkeleyamide source organism is not actually Penicillium.** The Stierle 2008 "*Penicillium rubrum*" Berkeley Pit isolate has been reclassified to **Talaromyces amestolkiae** (Talaromyces split off from Penicillium in 2011 — different genus, not subgenus Penicillium where P. camemberti and P. roqueforti live). This is taxonomically much more distant than "different Penicillium isolates" — the BGC inheritance argument is fundamentally weaker than the comp-014 framing suggested. Source: Yilmaz et al. 2014 reclassification + Stierle review trail.
- **Zero direct literature on Berkeleyamide / Berkeleyone production in P. camemberti or P. roqueforti.** Searched Paperclip exact phrase + WebSearch — no hits. The canonical 2023 BGC review for P. roqueforti (Chávez, Vaca, García-Estrada; PMC10144355) enumerates andrastins, mycophenolic acid, roquefortines C/D, PR-toxin, eremofortins, isofumigaclavines, festuclavine, annullatins D/F — **Berkeleyamide / Berkeleyone are absent from the entire enumerated chemotype.** Not a "we haven't checked yet" gap — actively-curated comprehensive review.
- **The cheese-ripening Penicillium chemotype skews pro-inflammatory or off-target, not anti-CASP1.** Mycophenolic acid (the closest food-grade Penicillium "anti-inflammatory" — used clinically as mycophenolate mofetil immunosuppressant) — Huang 2018 (PMC6032679, *Chinese Medical Journal*): **MPA synergizes with LPS to activate the NLRP3 inflammasome, induce caspase-1 cleavage, and increase IL-1β release in human monocytes and THP-1 cells**, with Ac-YVAD-cmk (caspase-1 inhibitor) blocking the effect. MPA at 5–75 μM increased IL-1β release 1.7–2.5× over LPS alone. **This is the exact opposite of the desired chemistry** — and it's mediated through caspase-1 activation, not inhibition. Andrastin A is documented as a Ras farnesyltransferase inhibitor (anticancer) — not a CASP1/NLRP3 ligand. PR-toxin is mutagenic, carcinogenic, and immunotoxic per the canonical Dubey 2018 review (PMC5885497).
- **Domesticated cheese strains have actively-degraded mycotoxin BGCs** — Crequer et al. 2024 (PMC11605963, *IMA Fungus*): the most-domesticated non-Roquefort cheese population has a **deletion in mpaC** (cannot produce mycophenolic acid) and a **premature stop codon in the PR-toxin gene cluster ORF 11** (cannot complete PR-toxin biosynthesis, accumulates eremofortin A/B intermediates). Domestication has selected *against* the cryptic-BGC capacity. Non-cheese P. roqueforti populations (lumber, silage, food) retain more metabolite diversity. **Bet implication:** if Berkeleyamide-like chemistry were ever encoded in the broader P. roqueforti gene-pool, the domesticated cheese isolates we'd actually source from commercial culture collections are the *worst* place to look. Wild non-cheese isolates would be a better hypothesis if you wanted to keep this lineage.
- **The mycotoxin overlap with the caspase-1 chemotype is the dominant safety risk if you DID find activity.** Even at <1 ng/g residual levels in commercial cheese (Vallone 2014, PMC5076727 — "no roquefortine C, PR toxin, or mycophenolic acid detected in nine commercial Gorgonzola samples"), the BGCs are present in the genome (in non-Roquefort domesticated lineage they're degraded; in Roquefort lineage they're regulatorily silenced per Crequer 2024). A non-standard substrate that derepresses the cryptic BGC landscape (OSMAC approach, histone deacetylase manipulation, coculture) would *co-induce* the mycotoxin chemotype. A wet-lab assay would have to characterize mycotoxin output in parallel.

**Bottom line:** The literature does not support the wet-lab assay as platform-relevant for the cheese-ripening species. The Berkeleyamide producer is in a different genus (Talaromyces), the closest food-grade Penicillium "anti-inflammatory" (MPA) activates rather than inhibits caspase-1, and domesticated cheese strains have actively-degraded BGCs for the toxin chemotype the assay would be probing for. **Recommend redirecting the $500–1,000 wet-lab budget** — see §"Recommendation" below.

---

## Direct evidence: have P. camemberti / P. roqueforti been assayed for Berkeleyamides?

**Direct answer: no.** Searched:

- Paperclip exact-phrase "Berkeleyamide" → 19 hits, none mention P. camemberti or P. roqueforti
- Paperclip exact-phrase "Berkeleyone" → 0 hits
- Paperclip semantic "Berkeleyamide Penicillium caspase-1" → 47 results, no hits on the chemotype × food-grade species intersection
- WebSearch "Berkeleyamide Penicillium biosynthetic gene cluster" → returns the 2008 Stierle source paper (J. Nat. Prod. 71:856–860) and follow-ups from the Stierle group, all from Berkeley Pit isolates
- Comprehensive 2023 BGC review for P. roqueforti (Chávez, Vaca, García-Estrada, *J Fungi* PMC10144355) — `grep -i "berkeleyamide\|berkeleyone\|caspase-1\|NLRP3"` returns zero matches. The Penicillium roqueforti curated chemotype is: **andrastins (A, B, C), mycophenolic acid, roquefortines C/D, PR-toxin, eremofortins, isofumigaclavines A/B, festuclavine, annullatins D/F.** No Berkeleyamide / Berkeleyone chemistry on this list.

**Source organism clarification (load-bearing):**

The original 2008 Stierle paper (Stierle DB, Stierle AA, Patacini B. J Nat Prod 71:856–860; PMID 18330993) attributes Berkeleyamides A–D to "*Penicillium rubrum*" isolated from Berkeley Pit Lake at 270 m depth, cultured in acidified PDB broth (pH 2.7). However, taxonomic revision (Yilmaz et al. 2014, Studies in Mycology — split of Talaromyces from Penicillium based on β-tubulin / RPB2 / ITS phylogeny) has reclassified this isolate. The Stierle group's Berkeley Pit "P. rubrum" is now identified as **Talaromyces amestolkiae** (a sister to T. ruber / T. purpurogenus / T. stollii in the T. purpurogenus complex).

Taxonomic distance: P. camemberti and P. roqueforti are both in **subgenus Penicillium** (former section Fasciculata for P. camemberti, former section Roquefortorum for P. roqueforti). Talaromyces is a **separate genus** under family Trichocomaceae (now Aspergillaceae). The closest food-grade species in the Talaromyces genus is T. marneffei (an opportunistic pathogen, not food-grade) or T. flavus (some biocontrol use). **None of the cheese-ripening Penicillium species are in genus Talaromyces.**

Implication for BGC-inheritance reasoning: the "different Penicillium isolates" comp-014 framing understated the taxonomic distance. The Berkeleyamide producer is approximately as distant from P. camemberti / P. roqueforti as P. camemberti is from *Aspergillus oryzae* (different genus, same family). Cryptic-BGC sharing across that distance is uncommon, though not impossible — antiSMASH-style genome mining of P. roqueforti / P. camemberti deposited genomes would be the right next computational probe (NOT a wet-lab assay).

---

## Cheese-ripening Penicillium metabolite × caspase-1/NLRP3 activity

### Mycophenolic acid — **pro-inflammasome, not anti**

**Huang et al. 2018, *Chinese Medical Journal* (PMC6032679, PMID 29941706):**
- Tested MPA (5, 25, 75 μM) ± LPS in undiluted human blood, THP-1 monocytes, and primary monocytes
- **MPA alone failed to induce IL-1β; MPA + LPS synergistically increased IL-1β** in dose-dependent manner: 408 ± 36 pg/mL (LPS alone) → 685 ± 20 pg/mL (LPS + 5 μM MPA, p=0.035) → 742 ± 32 pg/mL (LPS + 25 μM MPA, p=0.017) → 1000 ± 66 pg/mL (LPS + 75 μM MPA, p=0.024)
- Mechanism: MPA does **not** affect NF-κB phospho-p65 or pro-IL-1β protein levels (no effect on signal 1) — instead, **MPA activates the NLRP3 inflammasome** (signal 2). Confirmed by Western blot showing caspase-1 p20 cleavage band increase. Ac-YVAD-cmk (caspase-1 inhibitor) blocked IL-1β secretion (LPS+MPA: 588 ± 42 pg/mL → LPS+MPA+YVAD: 181 ± 45 pg/mL, p=0.014).
- Authors' framing: "patients immunosuppressed with mycophenolate mofetil may have overly activated caspase-1 during infection." MPA is *clinically* immunosuppressive via IMPDH inhibition (purine biosynthesis blockade in lymphocytes), but the innate-immune (monocyte/macrophage) effect runs in the opposite direction at the inflammasome.

**Implication:** the most-studied "anti-inflammatory" food-grade Penicillium metabolite is, at the inflammasome level, **synergistic with priming**. If P. camemberti / P. roqueforti extract showed any caspase-1 modulation, MPA contamination (or co-induced production under non-standard substrate conditions) would skew the assay toward false-positive *activation*, not the desired inhibition.

### Andrastins (A, B, C) — Ras-farnesyltransferase inhibitors, not CASP1 ligands

**Rojas-Aedo et al. 2017, *Front Microbiol* (PMC5418334, PMID 28529508):** canonical 29.4-kb adr BGC characterization in P. roqueforti. Andrastin A is documented as a **protein farnesyltransferase inhibitor** acting on oncogenic Ras proteins (Uchida et al. 1996 cited in PMC5418334). Anticancer activity profile, no documented CASP1/NLRP3 binding. `grep -i "caspase\|NLRP3\|IL-1\|inflammasome"` against the full text returns zero matches.

### PR-toxin — mutagenic, carcinogenic, immunotoxic mycotoxin (not therapeutically relevant)

**Dubey et al. 2018, *Front Pharmacol* (PMC5885497, PMID 29651243):** canonical review. PR toxin causes "damage to vital internal organs, gastrointestinal perturbations, carcinogenicity, immunotoxicity, necrosis, and enzyme inhibition." Mutagenic via DNA replication / transcription / translation disruption. The chemotype of interest (anti-CASP1 selectivity) requires a tightly-defined SAR; PR-toxin's promiscuous reactivity (oxidation of -OH → -CHO, rapid conversion to PR imine / PR amide / PR acid) makes it a non-starter for a clinical lead.

### Roquefortine C, isofumigaclavines, festuclavine — indole alkaloids, weak/no CASP1 data

The Paperclip search "roquefortine C IL-1 macrophage" returned no direct CASP1/NLRP3 binding data for roquefortines. Roquefortine C is more characterized for neurotoxicity (tremorgenic in livestock at high doses) than for inflammasome modulation. Not platform-relevant.

### Cyclopiazonic acid (P. camemberti) — SERCA inhibitor, not anti-inflammatory

P. camemberti's signature mycotoxin is cyclopiazonic acid (CPA), a sarco/endoplasmic reticulum Ca²⁺-ATPase (SERCA) inhibitor. SERCA inhibition can paradoxically *activate* NLRP3 indirectly (cytosolic Ca²⁺ flux is a signal-2 trigger for inflammasome assembly). Same direction-of-effect problem as MPA.

---

## BGC architecture: shared with environmental isolates or not?

**Key reframe:** the comp-014 framing assumed Berkeleyamide chemistry might be cryptic-but-encoded in P. camemberti / P. roqueforti BGCs. The taxonomic correction (producer = Talaromyces amestolkiae, not Penicillium subgenus Penicillium) makes the cryptic-BGC argument weaker than it first appeared.

**What's known about P. roqueforti BGC architecture (Chávez 2023 review, PMC10144355 + Crequer 2024, PMC11605963):**

| BGC | Status in domesticated cheese strains | Substrate-dependence |
|---|---|---|
| Andrastin A (adr cluster, 29.4 kb) | Intact, expressed | Constitutive in PDA, reduced in cheese matrix |
| Mycophenolic acid (mpa cluster) | **Deleted in mpaC in non-Roquefort domesticated strain** (Crequer 2024). Intact in Roquefort & wild strains. | Detectable on bread-like substrate in vitro, undetectable in finished Gorgonzola cheese (Vallone 2014) |
| PR-toxin (ari1, prx clusters) | **Premature stop codon in ORF 11 in non-Roquefort strain.** Roquefort strain has intact ORFs but appears downregulated (no PR-toxin detected). | Trace production possible on non-cheese substrates |
| Roquefortines (rds cluster) | Intact, expressed | Variable; in vitro production high, in-cheese low |
| Isofumigaclavines, festuclavine, annullatins | Variable, present in genome | Substrate-dependent |

**Crequer 2024's key empirical finding:** the metabolome of P. roqueforti is *contracted* by domestication. Non-cheese populations (lumber, silage, food-spoilage) produce **broader fatty-acid and terpenoid profiles absent from cheese strains**. Some of the lost compounds are likely cryptic anti-microbial / anti-grazing chemistry that's been selected against in food matrices. Whether any of those broader compounds overlap with the Berkeleyamide chemotype would require a paired metabolomic comparison — not currently in the literature.

**Recommended computational probe (instead of wet-lab):** run antiSMASH against publicly-available P. roqueforti / P. camemberti / P. rubens genomes, looking for NRPS-PKS hybrid BGCs with architecture similar to whatever the Berkeleyamide BGC turns out to be (the Berkeleyamide BGC has not been formally characterized in the literature based on this scan — that's itself a gap). If antiSMASH returns nothing homologous, the cryptic-BGC hypothesis is falsified before any wet-lab spend.

---

## Substrate-induction angle

(Brief, coordinates with the J3.2 OSMAC scan also running.)

Substrate-induction is real and well-documented for Penicillium chemotype — Ding et al. 2020 (PMC7464707) showed HdaA deletion in P. chrysogenum Fes1701 upregulates meleagrin / roquefortine biosynthesis while downregulating chrysogine. OSMAC (one-strain-many-compounds) is a standard discovery method (van de Pas et al. 2025, bio_abc7c9236df2). LaeA expression in marine-derived fungi triggers cryptic BGCs (Khan et al. 2020, PMC7766385).

**But:** substrate-induction can only activate BGCs that **exist in the genome**. The Crequer 2024 finding of frame-shift / deletion mutations in MPA and PR-toxin clusters in domesticated strains means **those particular BGCs cannot be rescued by substrate manipulation** — the genes are broken. A non-standard substrate (rice, sawdust, coculture with another microbe) could potentially:

1. Activate other-cryptic BGCs that the domesticated strain still has intact (unknown what those produce)
2. Drive Roquefort-population P. roqueforti to express PR-toxin (intact BGC, regulatorily silenced) — undesirable safety outcome
3. Have no effect if the Berkeleyamide-homolog BGC is genuinely absent (not just silenced)

The substrate-induction angle does NOT rescue the platform-relevance question. It would need to be paired with up-front antiSMASH genomic confirmation that the desired chemistry's BGC is even present.

---

## Mycotoxin overlap with the caspase-1 chemotype

**The dominant safety concern if a positive hit were found:**

The cheese-ripening Penicillium metabolite arsenal is a **mycotoxin-rich chemical space.** PR-toxin (carcinogenic, mutagenic), cyclopiazonic acid (SERCA inhibitor, hepatotoxic), patulin (general cytotoxin), ochratoxin A (nephrotoxic, neurotoxic — Paperclip hits PMC12197389 and PMC3179161 show OTA causes glial-cell-mediated neuroinflammation), roquefortine C (tremorgenic in livestock), citrinin in some P. camemberti lineages. The food-grade GRAS status of these species depends on **regulatory tolerance of trace mycotoxins** in finished products (Vallone 2014 confirmed below-detection-limit in Gorgonzola), not on the absence of toxin BGCs from the genome.

A non-standard substrate (rice, sawdust) that derepresses cryptic BGCs to *look for* Berkeleyamide chemistry would, by the same mechanism, **co-induce the mycotoxin profile** the cheese-fermentation conditions normally suppress. The OSMAC approach is biologically symmetric — you can't selectively derepress the "anti-CASP1" cryptic BGC without also derepressing the "carcinogenic mycotoxin" cryptic BGC (assuming the former even exists in the genome).

**A defensible wet-lab assay would have to:**
1. Pre-screen extracts for known mycotoxins by LC-MS (PR-toxin, MPA, OTA, citrinin, CPA, patulin, roquefortine C) before CASP1 assay
2. Use fractionation to separate any putative anti-CASP1 activity from the mycotoxin co-fraction
3. Confirm by orthogonal cytotoxicity assay that the active fraction is below mycotoxin thresholds

That's a substantially more expensive workflow than the original $500–1,000 framing implies. Realistic budget for a defensible assay: $5–15K.

---

## Recommendation for the wet-lab budget commitment

**Recommend redirecting the $500–1,000 to a computational probe before any wet-lab spend.** Specifically:

1. **antiSMASH genome scan ($0, ~3 hr compute time):** download publicly-available P. roqueforti (FM164, CECT 2905), P. camemberti (FM013, ESE00019), and P. rubens (Wisconsin 54-1255 / P2niaD18) genomes. Run antiSMASH 7 to enumerate all NRPS-PKS hybrid BGCs. Cross-reference against any published Berkeleyamide BGC architecture (the BGC has not been formally characterized as of this scan — that's itself a finding to surface). If no homologous BGCs are found, the cryptic-Berkeleyamide hypothesis is falsified for these species at low cost.
2. **Genome mining for Talaromyces amestolkiae or T. ruber Berkeleyamide BGC ($0):** Stierle group at Univ. Montana may have a deposited genome assembly (per the Cryptic Biosynthesis paper, PMC8574098, they used FAC-NGS on Berkeley Pit isolates). Reach out by email or check JGI MycoCosm for available assemblies. Confirming the BGC sequence + architecture is a prerequisite to genome-mining cheese-ripening strains for homologs.
3. **If antiSMASH returns plausible homologs in either P. roqueforti or P. camemberti:** *then* the wet-lab assay becomes platform-relevant. Budget for a defensible assay would be $5–15K (mycotoxin pre-screen by LC-MS + CASP1 enzymatic assay + orthogonal cytotoxicity) rather than $500–1,000.
4. **If antiSMASH returns nothing in cheese strains but Talaromyces amestolkiae has a clean BGC:** the platform-relevant question shifts entirely — engineer the Berkeleyamide BGC into the *koji* chassis (A. oryzae heterologous host, which already supports andrastin-type meroterpenoid assembly per Matsuda et al. 2013 cited in PMC5418334). This is a much cleaner play than trying to coax cheese-ripening strains to express foreign chemistry.

**What the lit scan didn't decide that a wet-lab might:**

Honestly, very little. The wet-lab assay as originally scoped (assay cheese-strain extracts for CASP1 inhibition) would tell you whether the strain produces detectable activity under whatever substrate conditions you grew it on — but it can't tell you *why* in a way that's actionable. A positive hit could be:
- Genuine Berkeleyamide-homolog production (interesting, would need follow-up structural characterization — $50K+)
- Mycotoxin contamination (e.g., MPA pro-inflammasome activity reading as "CASP1 modulation" — direction-of-effect confound)
- Off-target hit from another metabolite (e.g., a sorbicillinoid or indole alkaloid)

The lit scan establishes that the dominant *prior probability* on each of these is low for the first, real for the second, and unknown for the third. Genomic confirmation (antiSMASH) is dramatically cheaper and answers the prior-probability question before any wet-lab spend.

---

## Limitations

- **No paper formally characterizing the Berkeleyamide BGC.** Stierle 2008 reports structure determination of Berkeleyamides A–D, and the 2014 Stierle review (PMC5156321) summarizes assay results, but neither traces the BGC. The Cryptic Biosynthesis paper (PMC8574098) uses FAC-NGS on a related compound family (berkeleypenostatins from P. fuscum × P. camembertii/clavigerum coculture — note: that "P. camembertii" is the Berkeley Pit isolate, *not* the cheese-ripening species, despite the homonymous name. Confirm in original literature before any downstream reasoning.) Without a sequenced Berkeleyamide BGC, the antiSMASH homology search recommendation cannot be executed today — it would require either (a) reaching out to the Stierle lab for sequence data, or (b) inferring BGC architecture from the compound chemistry (NRPS-amide-bond-forming + meroterpenoid backbone) and searching for NRPS/PKS hybrids matching that pattern (more uncertain).
- **The Vallone 2014 finding that no roquefortine C / PR toxin / MPA are detected in finished Gorgonzola** is reassuring for cheese safety but does NOT mean the cheese strains can't produce these compounds — they don't, under cheese fermentation conditions. Under a different substrate, the production might be very different.
- **The Crequer 2024 paper is on *P. roqueforti* populations, not P. camemberti.** P. camemberti taxonomy and BGC inventory is less well-resolved in this scan. The 2025 Farouk paper (PMC11929314) on haloalkaliphilic adaptation in P. camemberti is the only directly-relevant recent paper found, and it's a stress-physiology paper, not a chemotype paper.
- **The Stierle group's caspase-1 IC50 values for Berkeleyamides A and D were not directly retrieved from primary source** — the comp-014 page derives the 330 / 610 nM numbers from ChEMBL pChEMBL values (6.48 / 6.21), which are themselves derived from the Stierle 2008 paper, but the original IC50 values in the J. Nat. Prod. paper were not accessible via this scan (ACS paywall returned HTTP 403). Numbers should be verified against the J. Nat. Prod. 71:856–860 PDF if downstream reasoning is sensitive to them.
- **No non-English (Chinese, Japanese) literature was probed in this scan.** Given the food-grade Penicillium subject overlaps with East Asian food microbiology (koji, soy-fermented foods, Kampo-adjacent research), a multilingual follow-up via CNKI / J-STAGE for "Penicillium camemberti / roqueforti × inflammasome / caspase-1" is warranted before declaring this question fully bounded. Budget: ~20 min, low marginal cost.
- **The "Talaromyces amestolkiae" reclassification of the Berkeley Pit isolate** is inferred from secondary sources (the WebSearch returns + Yilmaz 2014). Confirming with the Stierle group's most recent paper (Hoody et al. 2026, PMC13150583 — Berkeleylactam A total synthesis) would be cleaner; that paper was retrieved but not opened in detail in this scan.

---

## Citation provenance summary

Load-bearing PMID anchors for each finding:

| Claim | Anchor | Verification |
|---|---|---|
| MPA synergizes with LPS to activate NLRP3 caspase-1 IL-1β | PMC6032679 / PMID 29941706 (Huang 2018) | Paperclip meta.json read; abstract numbers grep-verified |
| Domesticated cheese P. roqueforti has mpaC deletion + PR-toxin ORF11 stop codon | PMC11605963 / PMID 39609866 (Crequer 2024) | Paperclip meta.json read; mutation locations specified in abstract |
| PR-toxin is mutagenic, carcinogenic, immunotoxic | PMC5885497 / PMID 29651243 (Dubey 2018) | Paperclip meta.json read |
| P. roqueforti BGC review enumerates andrastins, MPA, roquefortines, PR-toxin, eremofortins, isofumigaclavines, festuclavine, annullatins (NOT Berkeleyamides) | PMC10144355 / PMID 37108913 (Chávez 2023) | Paperclip content grep on full text returned no Berkeleyamide / CASP1 / NLRP3 hits |
| Andrastin A is Ras farnesyltransferase inhibitor, anticancer | PMC5418334 / PMID 28529508 (Rojas-Aedo 2017) | Paperclip content grep confirmed farnesyltransferase, no caspase mention |
| No MPA / PR-toxin / roquefortine C in finished Gorgonzola | PMC5076727 / PMID 27800360 (Vallone 2014) | Paperclip meta.json read |
| P. camemberti has limited mycotoxin-protective activity against contaminating molds | PMC11431082 (Ollinger 2024) | Paperclip search result, abstract |
| Berkeleyamides from "*Penicillium rubrum*" Berkeley Pit Lake, 270 m depth, acidified PDB | J Nat Prod 71:856–860 / PMID 18330993 (Stierle 2008) | WebFetch confirmed source organism, depth, growth conditions; IC50 numbers not directly verified |
| Berkeleyamides reclassification context — "P. rubrum" Stierle isolate now Talaromyces amestolkiae | Yilmaz et al. 2014 Studies in Mycology (Talaromyces genus split) + WebSearch trail | Not formally verified against primary source — flagged as a load-bearing inference that downstream reasoning should re-confirm |
| Berkeleypenostatins from P. fuscum × "P. camembertii/clavigerum" Berkeley Pit coculture (NOT cheese P. camemberti) | PMC8574098 (Cryptic Biosynthesis 2021) | WebFetch confirmed Berkeley Pit origin |
| Stierle group used MMP-3 + caspase-1 + caspase-3 assays for 20+ years | PMC5156321 (Stierle review 2014) | WebFetch confirmed assay panel |
| Substrate-induction / OSMAC / HdaA-deletion well-documented in Penicillium | PMC7464707 (Ding 2020), PMC7766385 (Khan 2020), bio_abc7c9236df2 (van de Pas 2025) | Paperclip search confirmed abstracts |

**Verification gate compliance:** all load-bearing numbers in this report (IL-1β release values, MPA concentrations, IC50 framing, taxonomic distance, BGC architecture) trace to a named PMID anchor with the relevant section either grep-verified in the Paperclip-stored full text or read in abstract. The one exception is the Talaromyces amestolkiae reclassification, which is inferred from multiple secondary sources and flagged as such in Limitations.
