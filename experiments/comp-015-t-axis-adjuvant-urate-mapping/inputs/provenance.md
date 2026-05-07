# comp-015 Provenance — All Inputs

**Date assembled:** 2026-05-07

This file documents every source for `inputs/*.json` per Open Enzyme reproducibility standard. Subagent orchestrators verifying this experiment can re-run the data fetch using the URLs/PMIDs below.

## ChEMBL API access status

**ChEMBL REST API was BLOCKED in this analysis environment.** All fetches via `urllib.request` (Python stdlib) and via the WebFetch tool returned HTTP 403 Forbidden. The same applied to PubChem REST. This is an environment-level restriction — not a ChEMBL outage.

**Consequence:** `inputs/chembl_bioactivity.json` is populated with `[API-BLOCKED-INFERRED]` and `[API-BLOCKED-WORKING-ID]` annotations rather than fresh fetched records. Compound ChEMBL IDs (CHEMBL474958 cordycepin, CHEMBL448739 icariin) are inferred from references in published ChEMBL-using studies; eurycomanone and echinacoside lack ChEMBL records (consistent with comp-013 finding that 5/9 TCM compounds had zero ChEMBL coverage).

**To restore full provenance:** the orchestrator should re-fetch the 16 compound × target pairs via direct ChEMBL REST API once access is restored:
```
https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=<X>&target_chembl_id=<Y>
```
The `analyze.py` regenerates outputs deterministically — re-running with refreshed `chembl_bioactivity.json` will update the verdict.

## Compound identity sources

| Compound | PubChem CID | MW (g/mol) | InChIKey source |
|---|---|---|---|
| Cordycepin (3'-deoxyadenosine) | 6303 | 251.24 | PubChem CID 6303; canonical |
| Eurycomanone | 6437226 | 408.40 | PubChem CID 6437226; major C20 quassinoid |
| Icariin | 5318997 | 676.66 | PubChem CID 5318997; flavonol glycoside parent |
| Echinacoside | 5281772 | 786.73 | PubChem CID 5281772; phenylethanoid glycoside |

PubChem CIDs cross-referenced against published natural-product database citations. WebFetch to `pubchem.ncbi.nlm.nih.gov/compound/<name>` was blocked (403), so identities are anchored from the ChEMBL/published-literature corpus rather than direct PubChem fetch in this run.

## Bioavailability primary sources (PMIDs)

| Compound | F (oral) | Primary PMID | Citation |
|---|---|---|---|
| Cordycepin | <2% intact | 31654017 (PMC6823370 Sci Rep 2019); 36377517 (Wang 2022) | Tsai/Sci Rep 2019 — no intact cordycepin systemic; ADA-deamination dominant; permeability Papp = 0.11 ± 0.01 × 10⁻⁶ cm/s |
| Eurycomanone | 10.5% | 16206032 (Low 2005, Planta Med); 29997335 (Han 2015 — replication 11.8%) | Bioavailability and Pharmacokinetic Studies of Eurycomanone from E. longifolia; absolute oral BA 10.5% in rats |
| Icariin | ~12% (1.2% intact parent) | 29259982 (Xu 2017, BioMed Res Int); 26633326 (Cheng 2015) | Pharmacokinetics, Tissue Distribution, and Metabolism Study of Icariin in Rat; 91.2% icariin → icariside II conversion |
| Echinacoside | 0.83% | 16931184 (Jia 2006); 25686726 (Wang 2015 phospholipid complex) | Determination of echinacoside in rat serum; absolute BA 0.83% |

All BA values verified via WebSearch on PubMed 2026-05-07. Effect-size numbers (Cmax, Tmax, F) cross-checked against multiple search-result sources where available.

## Direct urate-target evidence sources (PMIDs)

**v1 evidence (4-target panel):**

| Compound × Target | Evidence | PMID | Verification status |
|---|---|---|---|
| Cordycepin × URAT1 | Animal Model — Kunming mice, 15/30/60 mg/kg PO, SUA 337→216/210/203 µmol/L; URAT1 protein/mRNA dose-dependent down | 29422889 | VERIFIED via WebSearch |
| Cordycepin × ABCG2/OAT1/SHBG | NO-DATA | — | PubMed search 2026-05-07 found nothing |
| Eurycomanone × URAT1/ABCG2/OAT1 | NO-DIRECT-DATA *(v1; OVERRIDDEN by v2 — see below)* | — | v1 PubMed search missed PMID 31920654 |
| Eurycomanone × SHBG | Indirect: Clinical | 36013514 (Leisegang 2022 meta) + 21671978 + 23705671 | Cross-referenced against androgen-natural-modulation.md §1.2 |
| Icariin × URAT1 | NO-DIRECT — anti-inflammatory adjacent only | 33135192 | VERIFIED via WebSearch |
| Icariin × ABCG2/OAT1/SHBG | NO-DATA | — | PubMed search 2026-05-07 |
| Echinacoside × all 4 targets | NO-DATA | — | PubMed search 2026-05-07 |

**v2 NEW evidence (5-target panel; XO column + eurycomanone re-opens):**

| Compound × Target | Evidence | PMID | Verification status |
|---|---|---|---|
| **Cordycepin × XO** | In Vitro IC50 0.014 mg/mL = 55.7 µM (allopurinol comparator 8.94 µM same assay); fluorescence-quenching binding; gouty-nephropathy mouse model SUA reduction | **38141695** (Yang 2024, Int J Biol Macromol) | VERIFIED via WebSearch — IC50 0.014 mg/mL grep-matches abstract; 55.7 µM derived value is unit-conversion (MW 251.24) |
| **Eurycomanone × URAT1** *(v2 RE-OPEN)* | In Vitro + Animal Model — *Eurycoma longifolia* stem extract URAT1 + GLUT9 protein DOWNREGULATION in kidney; quassinoids inhibit urate uptake in hURAT1-expressing cells in vitro | **31920654** (Bin Mohamad Salleh 2019, Front Pharmacol; PMC6914847) | VERIFIED via WebSearch — abstract directly documents URAT1 downregulation + quassinoid in vitro hURAT1 inhibition |
| **Eurycomanone × ABCG2** *(v2 RE-OPEN)* | Animal Model — ABCG2 protein UPREGULATION in kidney of EL-treated HUA rats/mice (Western blot, dose-dependent at 100/200/400 mg/kg PO) | **31920654** | VERIFIED — same paper, abstract directly mentions ABCG2 upregulation |
| **Eurycomanone × OAT1** *(v2 RE-OPEN)* | Mechanistic Extrapolation — eurycomanol modulates 'GLUT9, ABCG2, OAT1, NPT1' transporters; specific OAT1 direction not in abstract | **34785103** (J Ethnopharmacol 2022) | Direction-extrapolated from mechanism coherence; NOT VERIFIED at OAT1-specific direction |
| **Eurycomanone × XO** | NO-DIRECT-XO-EVIDENCE — trigger papers actually establish transporter + purine-synthesis (PRPS) suppression, NOT XO | — | **v2 CITATION-LAUNDERING FINDING** — supplement-industry summary mis-attributed XO mechanism to PMID 31920654/34785103 |
| **Icariin × XO** | Negative Screen (Animal Model) — 15-flavonoid panel; icariin tested but NOT in significant-XO-inhibitor group (quercetin/morin/myricetin/kaempferol/puerarin were) | **17666819** (Mo 2007 Biol Pharm Bull) | VERIFIED via WebSearch — abstract explicitly lists 5 significant-effect flavonoids; icariin not in that subset |
| **Echinacoside × XO** | NO-DATA | — | PubMed search 2026-05-07 |

## v1 → v2 changes summary

- **+1 new target:** Xanthine Oxidase (XO, CHEMBL1929, UniProt P47989, gene XDH) added to `inputs/targets.json`.
- **+1 new chembl_bioactivity entry with direct IC50:** Cordycepin × XO, IC50 = 55700 nM (PMID 38141695, manual curation — not yet in ChEMBL).
- **+4 new XO literature claims:** Cordycepin × XO (in vitro positive, ratio 0.001 below threshold); Eurycomanone × XO (no direct XO data, citation-laundering finding documented); Icariin × XO (negative screen, Mo 2007); Echinacoside × XO (no data).
- **+3 RE-OPENED v1 NO-DATA pairs:** Eurycomanone × URAT1 (in vitro + animal model, PMID 31920654); Eurycomanone × ABCG2 (animal model, PMID 31920654); Eurycomanone × OAT1 (mechanistic extrapolation, PMID 34785103).
- **+1 site_for_concentration narrowing:** XO target site originally written as "plasma + liver/intestinal mucosa" — narrowed to "plasma" only because the analyze_pair function uses substring matching on "gut" / "plasma" to pick concentration source. Site_note preserved for context.
- **+1 verdict logic addition:** `classify_xo_contribution()` function added to analyze.py — XO is mechanism-orthogonal to transporter direction; XO inhibition is gout-favorable regardless of transporter effects.
- **Net evidence-tier verdict change:** Eurycomanone v1 GOUT-UNFAVORABLE → v2 GOUT-FAVORABLE. H-AN-02 v1 SUPPORTED → v2 PARTIALLY FALSIFIED.

## T-axis (PDE5) cross-references

For icariin's PDE5 mechanism (a different drug-target axis, not in the 4-target panel of this experiment but mechanistically relevant):
- PMID 12646997 (Xin 2003, Asian J Androl) — icariin PDE5 IC50 ≈ 0.43 µM
- PMID 18778098 (Dell'Agli 2008, J Nat Prod) — icariin PDE5 IC50 ≈ 5.9 µM; synthetic 3,7-bis(2-hydroxyethyl)icaritin IC50 ≈ 75 nM (close to sildenafil's ~74 nM)

These are anchored in `androgen-natural-modulation.md` §5.2 and not duplicated in the comp-015 `analyze.py` pipeline (PDE5 is outside the URAT1/ABCG2/OAT1/SHBG target panel).

## Wiki cross-references for prior claims

| Wiki page | What it provides |
|---|---|
| `wiki/androgen-natural-modulation.md` §1, §5.1, §5.2, §5.3 | Per-compound T-axis mechanism + dose + BA + UA caveat narrative |
| `wiki/androgen-natural-modulation.md` §10 (H-AN-02) | The hypothesis under test |
| `wiki/medicinal-mushroom-complement-track.md` | Cordycepin URAT1 prior (337→203 µmol/L), pentostatin co-pairing context |
| `experiments/comp-014-medicinal-mushroom-compound-mapping/` | Phase-4 PMID inventory for cordycepin × URAT1; phase-7b cordyceps strain scan |

## Methodology cross-references (for reviewers)

| Precedent experiment | Methodological inheritance |
|---|---|
| comp-013 TCM compound triage | "5 of 9 had no ChEMBL records" pattern; verdict-tagging when ChEMBL is sparse; site-aware gut-vs-plasma concentration use |
| comp-014 Medicinal mushroom mapping | Multi-PMID aggregation + chokepoint × compound matrix; this experiment narrows to 4 compounds × 4 targets |
| comp-007 Food-grade HDACi screen | "100× achievable/IC50 = decisively active; <10× = unclear; <1× = below threshold" framing |
| comp-004 Supplement ABCG2 antagonism | Achievable concentration discipline applied directly to ABCG2 — direct precedent for this experiment's ABCG2 column |

## What's NOT verified (open gaps the orchestrator should know about)

1. **ChEMBL REST API access blocked.** All bioactivity records are inferred or pending. A future re-run with API access will replace `[API-BLOCKED]` annotations with curated activity records.
2. **PubChem REST blocked.** Compound ChEMBL IDs (CHEMBL474958 for cordycepin, CHEMBL448739 for icariin) are working IDs from the published literature, not freshly verified.
3. **SHBG ChEMBL ID (CHEMBL3286) not verified.** UniProt P04278 → ChEMBL target: this is a working pattern from published SHBG-binder screens (Avvakumov, Hammond), not directly fetched in this run.
4. **Eurycomanone human Cmax for low pure-compound dose.** Rat PK data (PMID 16206032) used 100+ mg/kg; scaling to 2 mg pure eurycomanone in 70 kg human is order-of-magnitude estimate.
5. **Cordycepin whole-fermentate vs purified PK.** PMC6823370 shows no intact cordycepin systemic from purified oral; whole-fermentate Cordyceps with native pentostatin co-delivery is plausibly higher BA but no human PK study found.
6. **Chinese-language clinical literature (CNKI / WanFang) not accessed.** The CLAUDE.md global-multilingual discipline applies; CNKI access not available in this verification environment. Likely there are Chinese-language papers reporting echinacoside × urate or icariin × urate effects that this scan missed.

## Date stamp + sweep daemon expectation

- Inputs assembled: 2026-05-07
- analyze.py run: 2026-05-07
- All inputs immutable post-commit; reruns regenerate `outputs/` deterministically
- No `[skip-wiki-sweep]` marker — this experiment's wiki page should trigger the daemon to propagate findings into androgen-natural-modulation.md, medicinal-mushroom-complement-track.md, validation-experiments.md (if applicable)
