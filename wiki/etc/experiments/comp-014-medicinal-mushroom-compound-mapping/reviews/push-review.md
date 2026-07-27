COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 0e2c3eec4a1368d333fccc81058855d7281478cfa816da50859b5ef1c962c7a8
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective boundary only: comp-014 is an unranked historical lead inventory with no efficacy, safety, dose, ranking, sourcing, production, delivery, or chassis conclusion
SYNTHESIS_ALLOWED_SCOPE: none
FORBIDDEN_INFERENCES: ranked or top-tier mushroom candidates; toxicity_filter_pass means safe; query-hint species means confirmed source organism; database non-hit means biological absence; expression/binding/phenotype means direct gout-relevant function; Phase 6 PURSUE/DROP/readiness survives; Phase 7 practical SOP or purchase guidance is current advice; Cordyceps/GLPP/DAE/AMC-BFE/davallialactone results establish clinical gout efficacy

# Independent comp review — comp-014

## Reviewed snapshot
Independent daemon reviewer; reviewed snapshot bound to push-review manifest SHA-256 `0e2c3eec4a1368d333fccc81058855d7281478cfa816da50859b5ef1c962c7a8`. Shard coverage reports complete inspection of the text spans supplied, and targeted repository reads confirmed the current README, scope summary, focused interpretive page, portfolio index segment, and medicinal-mushroom track boundaries. `grep_repo` was unavailable because `rg` is absent, so additional corpus search was limited to supplied audits plus targeted `read_file` checks.

## Bottom-line verdict
Action required. The current reader-facing COMP-014 boundary is mostly corrected: it presents a partial, non-authoritative, unranked lead inventory and retires Phase 6. However, retained generated outputs still contain obsolete ranks, operational “what to buy”/SOP-style language, inconsistent quantitative cost/yield arithmetic, permissive “toxicity pass” semantics, query-hint species provenance, and mixed endpoint/polarity target mappings. These cannot support synthesis or automated prioritization. Corrective propagation is safe only to reinforce the quarantine.

## Implementation and constraint closure
The retained runnable path is only:

`cd wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping && python3 scripts/scope_validate.py`

Inspection shows this script validates limited JSON structure and regenerates `outputs/scope-summary.md`; it does not reproduce database pulls, LOTUS/NPAtlas/KNApSAcK/ChEMBL joins, Phase 3/4 target mapping, Phase 5 literature conclusions, Phase 7 cultivation claims, or retired Phase 6. It loads `toxicity-filter.json` only for shallow key checks, not for toxicology logic.

Load-bearing substitutions remain in historical outputs:
- `[query-hint]`/`[npatlas-query]` labels are often treated like species occurrence evidence.
- `toxicity_filter_pass: true` frequently means a taxonomic include/grey rule fired, not that a compound is safe or eligible; known toxins/drugs appear as passing.
- Full InChIKey keys are counted as unique compounds despite repeated `inchikey2D` variants; counts depend on stereochemistry/2D/name deduplication policy.
- Chokepoint tables mix IC50/Ki/Kd, percent inhibition, qHTS potency, null values, activation, expression, and phenotype records. Direction and function are not normalized.
- OAT4 mapping is suspect: a metadata join maps OAT4 UniProt to a ChEMBL pref_name for a voltage-gated potassium channel.

Constraint closure is not achieved for any candidate. Reaction substrates, transporter substrates, tissue compartment, free exposure, residence time, local peaks, off-targets, redox/immune burden, toxicity, production yield, batch reproducibility, and direct mechanism-matched function remain lead-specific gates. Whole extracts/formulas cannot assign component causality. ADA, PINK1/mitophagy, redox/disulfide, ABCG2, NLRP3, C5aR1, and cultivation/chassis ideas remain open leads, not decisions.

## Summary-fidelity audit
Current high-level surfaces are substantially faithful:
- `README.md`, `outputs/scope-summary.md`, `wiki/medicinal-mushroom-compound-mapping-computational.md`, and `wiki/computational-experiments.md` correctly retire Phase 6 and bound COMP-014 as a partial lead inventory.
- `wiki/medicinal-mushroom-complement-track.md` appropriately requires exact preparation identity, chemical standardization, exposure, and direct gout-relevant assays.

Material residual drift is inside retained generated outputs:
- Phase 2/3/4/5/7 files retain historical ranks, KEEP/DROP/Tier/readiness/top-tier language, wet-lab recommendations, and practical cultivation/purchase/SOP wording despite non-authoritative banners.
- Phase 2a ChEMBL summary has confusing 4-versus-5 row arithmetic and non-exhaustive top-200/targeted-query limitations.
- Phase 3/4 “potency-ranked” tables rank heterogeneous and sometimes negative/null/activation endpoints.
- Phase 5 deep reads downgrade several earlier claims: Cordyceps clinical evidence is transplant-context secondary SUA only; DAE URAT1 is expression-level; GLPP is heterogeneous and paywalled; davallialactone lacks in-vivo evidence in the read paper; AMC-BFE is extract-level and paywalled.
- Phase 7 cost/yield and comparator statements are internally inconsistent and should not drive production or chassis priorities.

## Reader-facing ownership audit
The focused COMP-014 page now owns the evidence boundary without portfolio ranking. The medicinal-mushroom track correctly hosts intervention conjectures and gates. Cross-track comparisons remain in portfolio surfaces.

Action is still required because generated Phase 7 outputs contain reader-facing “recommended,” “optimal,” “what to buy,” and SOP-like language that conflicts with the current contract. Historical generated outputs may remain as retrieval artifacts only if their quarantine is unmistakable and if no current page imports their obsolete rankings, purchase guidance, or chassis implications.

## Conjecture preservation audit
Unsupported factual assertions should be corrected, but useful leads survive as conjectures:
- C5aR1: bounded database non-retrieval rejects only the historical fungal-antagonist query result; it does not prove universal absence.
- Cordyceps: survives as a preparation-specific cordycepin/pentostatin exposure conjecture, not generic Cordyceps efficacy.
- GLPP: survives as an exact-fraction/batch-release conjecture, not “reishi” or single-compound ADA proof.
- DAE: survives as a pure-compound animal/XOD/renal-expression lead requiring full-text kinetics and source-abundance verification.
- AMC-BFE/Sanghuang/Phellinus extracts survive as extract-level leads requiring deconvolution.
- Berkeleyamide/CASP1 survives as a biochemical lead, not a food-Penicillium or medicinal-mushroom production claim.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `.gitignore` | support | yes | Raw/caches excluded; provenance artifacts, not live outputs. |
| `README.md` | summary | yes | Correctly retires ranks/Phase 6; only scope validator runnable. |
| `inputs/chokepoint-targets.json` | input | yes | Historical target leads; ADA/PINK1/redox not canonical decisions. |
| `inputs/data-sources.json` | input | yes | Source plan, not proof of successful querying; several endpoints need preflight. |
| `inputs/phase-5-anchor-species.json` | input | yes | Historical sanity set; safety/GRAS labels not authority. |
| `inputs/provenance.md` | input | yes | No Phase 1 fetches; later reproduction unavailable. |
| `inputs/toxicity-filter.json` | input | yes | Historical, non-authoritative; not a safety classifier. |
| `outputs/PHASE-2-FINDINGS.md` | generated_output | yes | Historical; counts/zero-hit/chokepoint claims overstrong. |
| `outputs/PHASE-5-FINDINGS.md` | generated_output | yes | Historical; KEEP/DROP/ranks and canonical additions invalid. |
| `outputs/phase-2-unified-fungal-compounds.json` | generated_output | yes via shards | Query-hint provenance, toxic pass records, duplicates, broad/out-of-scope compounds. |
| `outputs/phase-2-unified-summary.md` | generated_output | yes | Non-authoritative; coverage gaps; toxicity pass is grey-zone include. |
| `outputs/phase-2a-chembl-fungal-source.{json,md}` | generated_output | yes | Limited ChEMBL snapshot; row arithmetic and potency/tier caveats. |
| `outputs/phase-2b-compounds-by-inchikey.json` | generated_output | yes via shards | Query-hint species, InChIKey2D duplicates, null Wikidata, identity errors. |
| `outputs/phase-2b-lotus-fungal-compounds.{json,md}` | generated_output | yes | LOTUS query buckets; no toxicity filter; non-authoritative counts. |
| `outputs/phase-2c-pubmed-fungal-chokepoint.{json,md}` | generated_output | yes | Abstract/title breadth only; PPARα/γ label issue; formula/extract confounding. |
| `outputs/phase-3-compound-x-target.json` | generated_output | yes | Target mapping incomplete; SwissTargetPrediction not run; OAT4 mismatch; mixed/null endpoints. |
| `outputs/phase-3-fungal-chokepoint-hits.{json,md}` | generated_output | yes | Lead-only; limited scan; exact-match caveats. |
| `outputs/phase-3-target-mapping-summary.md` | generated_output | yes | Potency rankings invalid from mixed/negative/null endpoints. |
| `outputs/phase-4-chokepoint-intersection-v2.json` | generated_output | yes | Historical intersection; mixed polarity/readouts; duplicates; empty arrays not absence. |
| `outputs/phase-4-ranked-candidates.{json,md}` | generated_output | yes | Rank/score invalid; plant/query-hint and extract-level confounding. |
| `outputs/phase-5-deepread-PMID26457607.md` | generated_output | yes | Cordyceps evidence downgraded to transplant-context secondary SUA. |
| `outputs/phase-5-deepread-PMID35750011.md` | generated_output | yes | DAE high-dose animal lead; URAT1 expression only; full text needed. |
| `outputs/phase-5-deepread-PMID36385640.md` | generated_output | yes | GLPP heterogeneous/paywalled; ADA attribution unresolved. |
| `outputs/phase-5-deepread-PMID36801789.md` | generated_output | yes | Davallialactone closed-access biochemical/cell evidence only. |
| `outputs/phase-5-deepread-PMID41905012.md` | generated_output | yes | AMC-BFE extract/paywalled; no component causality. |
| `outputs/phase-5-deepseek-cross-check.md` | generated_output | yes | Mostly confirms needed downgrades and full-text gates. |
| `outputs/phase-7-cultivation-yield-meta-analysis.md` | generated_output | yes | Non-authoritative but contains SOP/purchase/ranking language and inconsistent costs. |
| `outputs/phase-7a-ganoderma-strain-scan.md` | generated_output | yes | GLPP identity/yield unresolved; taxonomy and Juncao gates. |
| `outputs/phase-7b-cordyceps-strain-scan.md` | generated_output | yes | ADA/pentostatin and engineered chassis claims gated; comparator ambiguity. |
| `outputs/phase-7c-pleurotus-strain-scan.md` | generated_output | yes | Exposure blocks consumption equivalence; extraction-yield nuance. |
| `outputs/scope-summary.md` | generated_output | yes | Correct current generated summary; only structural scope validation. |
| `scripts/scope_validate.py` | code | yes | Deterministic limited validator only. |
| `wiki/computational-experiments.md` | proposed/affected_update | targeted yes | Current COMP-014 index is correctly bounded. |
| `wiki/medicinal-mushroom-compound-mapping-computational.md` | proposed/affected_update | yes | Correct focused-page contract. |
| `wiki/medicinal-mushroom-complement-track.md` | affected_update | yes | Consistent conjecture and gating language. |
| COMP-007/016/020 supplied surfaces | affected context | yes | Relevant boundaries consistent; no COMP-014 expansion found in supplied spans. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 6,798 unique compounds / 9,409 records / 55 attributions | Phase 2 outputs | Historical count only | Database snapshot; no rerunnable pull; query-hint and dedup caveats | Not current quantitative evidence |
| `toxicity_filter_pass` | Phase 2/3/4 JSON | Used in rows/tables | Taxon/grey include logic; many toxins pass | Must not mean safety |
| Species provenance | Phase 2/2b/3/4 | Joins and counts | Often `[query-hint]`/`[npatlas-query]`, not primary occurrence | Lead only |
| ChEMBL target/potency rows | Phase 2a/3/4 | Target mapping/ranking | Mixed endpoint types, nulls, direction errors, duplicates | Not rankable |
| SwissTargetPrediction coverage | Phase 3 | Intended orphan mapping | Not run | Unsupported |
| DAE SUA 407→134 µmol/L | Phase 5 PMID35750011 | Lead evidence | Abstract/deep-read; high-dose mouse only; full text needed for kinetics | Narrow animal lead |
| GLPP 40.6% UA reduction / ADA | Phase 5 PMID36385640 | Lead evidence | Abstract/paywall; heterogeneous material; direct ADA unresolved | Conjecture only |
| Cordyceps −84.19 µmol/L SUA | Phase 5 PMID26457607 | Human-context lead | Secondary endpoint in transplant RCT subset; primary Chinese RCT not verified | Not general gout evidence |
| Davallialactone XO IC50 90 µM | Phase 5 PMID36801789 | Lead evidence | Abstract-level; no in-vivo evidence verified | Weak biochemical lead |
| AMC-BFE multi-chokepoint | Phase 5 PMID41905012 | Extract lead | Paywalled abstract; expression/pathway level; no component causality | Extract conjecture |
| Phase 7 cultivation costs/yields | Phase 7 outputs | Production implications | Inconsistent arithmetic/comparators; not reproduced by script | Not decision-grade |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — COMP-014 index states partial lead inventory and retired Phase 6.
- `wiki/medicinal-mushroom-compound-mapping-computational.md` — already consistent — owns COMP-014 boundary and forbids rankings/delivery claims.
- `wiki/medicinal-mushroom-complement-track.md` — already consistent — preserves research conjecture while requiring identity, exposure, and direct assays.
- `wiki/medicinal-mushroom-extract-sops.md` — not inspected — linked as method surface; verify it does not import Phase 7 purchase/SOP claims as current decisions.
- `wiki/validation-experiments.md` — not inspected in supplied shards — verify no wet-lab priority was promoted from retired COMP-014 ranks.

## New connections or implications
The strongest cross-corpus implication is negative: COMP-014 should serve as a provenance-stress test for natural-product pipelines. The same failure modes—query-hint source attribution, toxicology-by-taxon, stereochemical duplicate inflation, expression/phenotype-to-function substitution, and heterogeneous endpoint ranking—should be treated as reusable audit checks for TCM and complement screens.

Research Conjecture boundary: a reproducible, composition-controlled fungal material may still expose gout mechanisms, but COMP-014 only identifies where to rehydrate primary sources and design discriminating assays. It does not select the material.

## Required actions
1. Add or strengthen quarantine banners inside retained Phase 3/4/5/7 generated outputs that still contain ranks, KEEP/DROP/Tier/readiness, “recommended,” “optimal,” “what to buy,” SOP, cost, or chassis language; verification: no historical output can be mistaken for current decision authority.
2. Correct or annotate known mapping/identity defects: OAT4 ChEMBL mismatch, PPARα/PPARγ label mismatch, ATP/adenylosuccinate-like record, DPPH-under-XO row, and Phase 2a 4-versus-5 row boundary.
3. Define table semantics for future use: `toxicity_filter_pass` as retained-for-review, query-hint as non-provenance, and full-InChIKey versus 2D/name deduplication.
4. Prevent synthesis from Phase 7 production/cultivation outputs until cost/yield arithmetic, substrate comparator, strain/material identity, and biosafety constraints are recalculated from primary sources.
5. Inspect linked validation/SOP pages for accidental propagation of Phase 6/7 rankings, purchase guidance, or wet-lab priorities.

## Review limits
I did not execute code. Primary literature and paywalled full texts were not independently retrieved. `grep_repo` failed because `rg` is unavailable, so corpus-wide search was limited to supplied shard audits and targeted file reads. Binary/raw caches were not inspected beyond text representations. The review binds the supplied daemon manifest hash and source snapshot, not an independent rerun of historical database pulls.
