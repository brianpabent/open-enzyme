---
title: "Medicinal Mushroom Compound × Chokepoint Mapping — Computational Analysis (comp-014)"
date: 2026-05-06
tags:
  - medicinal-mushrooms
  - fungi
  - natural-products
  - chokepoint-mapping
  - breadth-aggregation
  - global-multilingual
  - computational
  - lotus
  - npatlas
  - knapsack
  - tcmsp
  - hit
  - mibig
  - antismash
  - ergothioneine
  - redox-disulfide
  - peer-track
  - scope-page
related:
  - computational-experiments.md
  - modality-chokepoint-matrix.md
  - tcm-modern-rigor-intersection.md
  - tcm-gout-compound-triage-computational.md
  - nlrp3-exploit-map.md
  - complement-c5a-gout.md
  - abcg2-modulators.md
  - manual-literature-mining.md
  - open-source-platform.md
  - open-enzyme-vision.md
sources:
  - "Brian framing 2026-05-06: 'pull in all of the known compounds from as many species as possible and then map that to our chokepoints... whether that's directly in the body or, who knows, something else like helping disulfides'"
  - "Open Enzyme/CLAUDE.md §Global-multilingual research by default — corpus must include CNKI, Wanfang, J-STAGE, KISS — non-English sources are not 'language barrier'"
  - "Open Enzyme/CLAUDE.md §Translation protocol — two-model independent cross-check with inline disagreement annotations for non-English source ingestion"
  - "comp-013 TCM gout compound triage — established the ChEMBL coverage gap pattern for non-Western-pharma compounds; same gap applies to fungi"
  - "wiki/modality-chokepoint-matrix.md — canonical chokepoint inventory used as the right-hand side of the mapping"
status: scoped — Phase 1 only
---

# Medicinal Mushroom Compound × Chokepoint Mapping — Computational Analysis (comp-014)

## Status

**Phase 1 (Scope) — Committed 2026-05-06.** Phases 2–6 are queued, not executed. This page documents the scope and the rationale for the multi-phase plan; it is NOT a results page. Per Open Enzyme convention, this page will be revised in place when each subsequent phase lands, with a status promotion (`scoped` → `in progress` → `complete`) tracked in the YAML frontmatter and the [`computational-experiments.md`](./computational-experiments.md) tracking index.

## §1 Question

Across all known characterized fungal natural products — aggregated from sources that span the global research corpus, not just Western pharma — which compounds map onto Open Enzyme's existing chokepoints, and which fungal species are the highest-leverage producers?

The framing question per chokepoint, per Brian (2026-05-06): **"What open biological problem might fungal chemistry answer at this chokepoint that we don't yet have a fermentable lever for?"** — not "is fungus useful here?" The inversion is the same load-bearing one applied in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — guard against path-dependent narrowing.

## §2 Why this experiment exists

Three converging reasons:

1. **Path-dependent narrowing risk if we default to ChEMBL-only.** comp-013 already surfaced the named gap: 5 of 9 candidate TCM compounds had no ChEMBL bioactivity records of any kind, forcing reliance on animal-model in vivo evidence to assign verdicts. The gap is downstream of which compounds got into Western-pharma curation pipelines, not whether the compounds have evidence. Fungal compounds will hit the same coverage gap or worse — most medicinal-mushroom clinical evidence sits in Chinese (CNKI, Wanfang) and Japanese (J-STAGE) corpora that ChEMBL has never seen. Per `Open Enzyme/CLAUDE.md` §Global-multilingual research, treating these as "language barrier" is the wrong frame: in 2026 the AI substrate reads them natively.

2. **Fungi are biochemically distinctive in chemistries that adjacent kingdoms don't produce in volume.** Ergothioneine biosynthesis is essentially fungal-and-mycobacterial; epipolythiodioxopiperazine (ETP) compounds with internal disulfide bridges are fungal-specific; lanostane triterpenoid diversity (Ganoderma genus alone has 400+ characterized) dwarfs plant triterpenoid diversity at the species level. A breadth-first aggregation that ignores this is biased; one that includes it might surface chokepoint coverage that no single existing OE wiki page would predict.

3. **The "redox/disulfide" angle in Brian's framing points at a chokepoint Open Enzyme has not formally mapped on the patient side.** The DAF SCR1-4 disulfide-count incident (2026-05-06, [CLAUDE.md §Pre-commit verification gate](https://github.com/brianpabent/Open-Enzyme/blob/main/CLAUDE.md)) shows disulfide chemistry is already load-bearing for engineering. The patient-side mechanism — TXNIP/thioredoxin axis as an NLRP3 priming layer; PDI as ER folding capacity for disulfide-rich therapeutic proteins; ergothioneine as a uniquely-fungal thiol antioxidant with cardiovascular evidence — has not been worked up. comp-014 may produce the evidence to formalize it as a named chokepoint.

## §3 Scope (Phase 1)

### §3.1 Phase 5 anchor species (18 — sanity-check, NOT the breadth gate)

**Reframed 2026-05-06 per Brian's correction:** breadth means species-agnostic pull from LOTUS/NPAtlas/KNApSAcK/NPASS/TCMSP filtered by `toxicity-filter.json`, not a curated medicinal-fungus list. The 18 species below serve two roles: (1) **Phase 2 sanity-check** — every one of them MUST appear in the Phase 2 output, else the pipeline has a bug; (2) **Phase 5 deep-dive seed** — they are the well-studied anchor when Phase 4 chokepoint intersection produces hits, since they have established CNKI/J-STAGE clinical-evidence corpora to ingest first.

Selected for substantive characterized chemistry + human-use precedent + regulatory tractability. Exclusions: psychoactive (Schedule I — Psilocybe), toxic (Amanita, Claviceps), culinary-only (truffles). Full rationale per species in `experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/candidate-species.json`.

| Common name | Scientific | Distinctive chemistry | Redox-chokepoint relevance |
|---|---|---|---|
| reishi / lingzhi | *Ganoderma lucidum* | 400+ ganoderic acid triterpenoids, β-glucans | — |
| cordyceps (cultivated) | *Cordyceps militaris* | cordycepin (3'-deoxyadenosine — purine analog, abundant in *militaris*) | — |
| caterpillar fungus (wild) | *Ophiocordyceps sinensis* | adenosine + cordyceps acid (mannitol); chemistry diverges from *C. militaris* | — |
| lion's mane | *Hericium erinaceus* | erinacines, hericenones (NGF inducers) | — |
| turkey tail / yun zhi | *Trametes versicolor* | PSK / PSP (FDA-approved adjuvant in Japan) | — |
| chaga | *Inonotus obliquus* | betulinic acid, lanostanes, melanin | — |
| maitake | *Grifola frondosa* | D-fraction β-glucan | — |
| shiitake | *Lentinula edodes* | lentinan, **eritadenine** (cholesterol-lowering) | — |
| **oyster mushroom** | ***Pleurotus ostreatus*** | **lovastatin (originally discovered here), highest known ergothioneine producer** | **PRIMARY** |
| almond mushroom | *Agaricus blazei* | β-glucans (agaritine = toxicity flag) | — |
| antrodia | *Antrodia camphorata* | antrocins, antroquinonol (Phase II oncology) | — |
| sang hwang | *Phellinus linteus* | hispolon | — |
| fu ling / poria | *Wolfiporia cocos* | pachymic acid, lanostane triterpenes | — |
| zhu ling | *Polyporus umbellatus* | polyporusterones (TCM diuretic) | — |
| tremella | *Tremella fuciformis* | acidic heteropolysaccharides | — |
| wood ear | *Auricularia auricula-judae* | acidic polysaccharides (anticoagulant) | — |
| **koji (chassis)** | ***Aspergillus oryzae*** | kojic acid, **ergothioneine producer**, secreted enzymes | secondary |
| *A. terreus* | *Aspergillus terreus* | lovastatin (industrial origin), terrein | — |

Phase 2 expansion criteria documented in the JSON — KNApSAcK / TCMSP / MIBiG may surface less-studied species worth adding.

### §3.2 Chokepoint targets

18 entries, drawn from canonical wiki sources and joined by UniProt accession. 17 canonical, 1 proposed (Phase 5 confirm/reject).

**Canonical chokepoints carried over from existing wiki:**

- **Urate axis:** uricase substrate (luminal sink), URAT1, GLUT9, ABCG2, OAT1/OAT3, Xanthine Oxidase
- **NLRP3 axis:** NLRP3, ASC, Caspase-1, IL-1β, TNFα
- **Complement (CP0):** DAF/CD55 (engineering chassis target, not patient target), C5aR1
- **Vessel-wall:** Lp-PLA2
- **Transcriptional / regulatory:** HDAC6 (per comp-007), PPARγ (per [`abcg2-modulators.md`](./abcg2-modulators.md)), Nrf2/KEAP1

**Proposed addition (Phase 5 decision):** redox/disulfide-modulator chokepoint — candidate human targets PDI (P4HB), PDIA3, Thioredoxin (TXN), TXNIP (Q9H3M7), Glutaredoxin (GLRX). The TXNIP entry is bidirectional with the NLRP3 chokepoint: TXNIP is a direct NLRP3 activator under oxidative stress, so fungal compounds suppressing TXNIP would suppress NLRP3 priming.

**Phase 5 verdict tiers** (three-way decision, not binary — refined in Phase 1 peer review):
- **ADMIT:** ≥20 fungal compounds across ≥3 mechanistic classes → formal chokepoint addition to [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) as a new column.
- **PRELIMINARY:** 10–19 compounds across ≥2 mechanistic classes → provisional column in the matrix with explicit "needs Phase 5b expansion" tag.
- **REJECT:** <10 compounds OR dominated by one mechanistic class → fold surfaced compounds into the existing NLRP3 sub-chokepoint map as an additional priming axis (TXNIP/redox), without elevating to a standalone chokepoint.

**One canonical-wiki gap surfaced in Phase 1:** OAT4 (SLC22A11, UniProt Q9NS40) is a known apical urate exchanger and benzbromarone target but is not currently in any wiki page. Added to `chokepoint-targets.json` for comp-014 scope and flagged for closure in a separate sweep — `abcg2-modulators.md` or `gout-pathophysiology.md` should incorporate OAT4 as part of the canonical urate-transporter inventory.

### §3.3 Data sources

**12 compound and bioactivity databases:**
- LOTUS, NPAtlas, KNApSAcK, NPASS, TCMSP, TCMID, TCM Database@Taiwan, HIT, BATMAN-TCM, COCONUT (compound coverage)
- ChEMBL, PubChem BioAssay, SwissTargetPrediction, STITCH (bioactivity / target mapping)
- MIBiG, antiSMASH-DB (genomic-encoded compound space — for hypothesis generation about uncharacterized chemistry)

**6 multilingual literature corpora:** PubMed, CNKI, Wanfang, J-STAGE, CiNii, KISS, RISS. Phase 5 ingestion follows `Open Enzyme/CLAUDE.md` §Translation protocol — two-model cross-check with inline annotations on disagreement.

**Per-language model pairing for Phase 5** (specified now to avoid Phase-5-time drift):
- **Chinese-language sources (CNKI, Wanfang):** Model A = Claude (Anthropic) or Gemini (Google); Model B = DeepSeek or Qwen (Chinese-vendor — native-language depth catches idiomatic and classical-TCM-terminology nuance Western-trained models miss).
- **Japanese-language sources (J-STAGE, CiNii):** Model A = Claude; Model B = Gemini OR another competent Japanese-fluent model. No Japanese-vendor model is currently a clear best-in-class option — two competent Western-trained models is acceptable per CLAUDE.md.
- **Korean-language sources (KISS, RISS):** Model A = Claude; Model B = GPT-5 OR Gemini. No Korean-vendor model is currently in the standard frontier-model set — two competent Western-trained models is acceptable per CLAUDE.md. If a Korean-fluent vendor model becomes available before Phase 5 lands, prefer it for Model B.

Translation cost is small (~$0.05 per paper at 2026 API pricing) and applies only to the Phase 5 deep-dive subset (top 3-5 species), not the full breadth pass.

Full source list with URLs, access methods, expected yield, and license terms in `experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/data-sources.json`.

## §4 Method (planned for Phases 2-6)

### §4.1 Phase 2 — Breadth aggregation (species-agnostic)
Pull every fungal compound record from LOTUS, NPAtlas, KNApSAcK, NPASS, TCMSP, COCONUT — Kingdom = Fungi filter at the database level, NO pre-curated species list. Apply `toxicity-filter.json`: include any species with FDA GRAS / EFSA QPS / pharmacopoeia / clinical-trial precedent OR any species in compound DBs without coexisting mycotoxin flag (default-include with `safety_review_pending` for grey-zone species); hard-exclude WHO Fungal Priority Pathogens 2022, documented mycotoxin producers, DEA Schedule I/II producers. Dedup by InChIKey across all sources. Expected yield: **500-2000 unique species after filtering** (vs. 18 in the curated anchor list). Output: a unified table of fungal compounds × producer species × source provenance × safety status.

### §4.2 Phase 3 — Target mapping
For each compound, query empirical bioactivity in this priority order:
1. ChEMBL via `mcp__plugin_chembl_ChEMBL__get_bioactivity` (highest curation, Western-pharma-skewed)
2. HIT (curated TCM ingredient → target)
3. PubChem BioAssay (broader corpus, less curated)
4. SwissTargetPrediction (similarity-based prediction — used only when 1-3 return nothing; flagged as predicted, not empirical)

Output: compound × target table with empirical/predicted flag and source provenance per row.

### §4.3 Phase 4 — Chokepoint intersection
Join compound × target × `chokepoint-targets.json`. For each compound, score:
- **Empirical chokepoint hits:** count of validated bioactivity entries against UniProt accessions in chokepoint-targets.json
- **Predicted chokepoint hits:** count of SwissTargetPrediction hits against the same
- **Site fit:** does the compound's known bioavailability profile (where available from LOTUS / NPASS) match the chokepoint's anatomical site?
- **Mechanism diversity:** does the compound hit ≥2 mechanistically distinct chokepoints (rare and high-leverage)?

Output: ranked candidate compound × chokepoint pairs.

### §4.4 Phase 5 — Multilingual literature ingestion (parallel, all chokepoint-hit species)
Run multilingual primary-literature ingestion for **every species with a chokepoint hit from Phase 4**, parallelized via subagents. NOT capped at top 3-5 — Brian's correction 2026-05-06: capping was the exact path-dependent narrowing CLAUDE.md flags ("Never gate exploration by cost or wall-time-to-build"). Translation cost via DeepSeek is ~$0.05/paper; even thousands of papers totals a couple hundred USD, not a real gate.

**Two-model cross-check pairing per CLAUDE.md §Translation protocol:**
- **Chinese sources (CNKI, Wanfang):** Claude (Sonnet 4.6 or Opus 4.7) + **DeepSeek V4-Pro** via OpenRouter. DeepSeek is the cheap (~$0.14/M tokens vs. Claude $15-75/M) Chinese-vendor model with native Mandarin fluency — same heterogeneity-guard pattern the wiki sweep daemon already uses (Pass 4 DeepSeek peer review).
- **Japanese sources (J-STAGE, CiNii):** Claude + Gemini 2.5 Pro (or DeepSeek as backup — DeepSeek's Japanese is reasonable despite Chinese-vendor).
- **Korean sources (KISS, RISS):** Claude + Gemini OR GPT-5.

**The actual constraint on this phase, honestly stated:** CNKI / Wanfang / KISS need institutional subscriptions for full text; J-STAGE / CiNii / PubMed are public. Paywall access is its own operational task — work with open-access subset and flag the paywalled gap explicitly per ingestion run.

Phase 5 deliverable: redox/disulfide chokepoint admit/PRELIMINARY/reject decision (criteria in §3.2).

### §4.5 Phase 6 — Per-compound triage
comp-013-style IC50 occupancy + composite scoring. Verdicts: GUT-LUMINAL VIABLE / SYSTEMIC VIABLE / MECHANISM UNCLEAR / NON-VIABLE. Subset gets shio-koji protease stability comp-NNN follow-ups (the same comp-001/005/006/012 pattern for any compound that becomes a candidate engineering payload — though most fungal-compound hits will be small molecules where the relevant downstream decision is supplement-stack inclusion rather than koji engineering).

## §5 Why this matters (platform context)

**For the Open Enzyme platform thesis broadly:**
- The platform claim is "we explore all angles, every avenue, fully open." The matrix in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) operationalizes the "all modalities × all targets" search space. comp-014 systematically scans the **fungal natural products row** of that matrix — the row most likely to surface chemistry the wiki has not enumerated, because fungal pharmacognosy has historically been explored in non-English-corpus traditions.

**For comp-013 (TCM gout compound triage):**
- comp-014 is the breadth follow-up to comp-013's hand-curated 9-compound triage. comp-013 established the methodology; comp-014 scales the candidate-pool acquisition.
- Several comp-013 verdicts are likely re-tested under comp-014 if the same compound-species (e.g., berberine in *Coptis*) appears as a fungal-co-occurring metabolite — though the primary candidate pool for comp-014 is fungal natural products, not herbal.

**For the "honest platform gap" at CP0 (complement priming):**
- `validation-experiments.md` §1.21 (executed 2026-04-27) confirmed via ChEMBL/NPASS/LOTUS/Open Targets scan that NO validated natural-product C5aR1 antagonists exist. comp-014's broader corpus — particularly KNApSAcK and HIT — may surface candidates the §1.21 scan missed, especially if there's CNKI clinical evidence for a fungus-derived anti-complement effect that never made it into the Western-curated databases. **Even one validated fungal C5aR1 antagonist would partially close the avacopan-dependence gap.** Highest single-leverage potential outcome of the breadth pass.

**For the proposed redox/disulfide chokepoint:**
- If Phase 5 confirms the warrant for adding this chokepoint to the formal inventory, [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) gets a new column. Existing rows (small molecules, peptides, engineered organisms) light up with whatever fungal-compound coverage the breadth pass surfaced, plus implications for the engineered-koji and engineered-LBP rows (since fungi themselves are producers of ergothioneine and related thiols — koji is already a producer).

## §6 Limitations (Phase 1)

1. **Phase 1 has no actual data — only an execution plan.** All quantitative claims about coverage, hit count, mechanism diversity will be filled in Phase 2-4. Anyone reviewing this page should treat Phase 1 as a hypothesis to be tested, not a finding.

2. **Database coverage may be uneven.** KNApSAcK is decades-old and well-maintained but not API-first; some Asian-hosted databases (TCMID notably) have had maintenance gaps. Phase 2 will verify each source is actually accessible before fetching; sources that prove inaccessible will be documented as gaps in the Phase 2 provenance update, not silently dropped.

3. ~~**Translation cost is real.**~~ **REMOVED 2026-05-06** — this was the exact failure mode the umbrella `CLAUDE.md` Curiosity & First-Principles Framing rule warns against ("Never gate exploration by cost or wall-time-to-build. Both have collapsed in the AI era"). Translation via DeepSeek is ~$0.05/paper × thousands of papers = a couple hundred USD total. Not a gate. Phase 5 runs for every chokepoint-hit species in parallel via subagents, not the top-3-5 subset I originally imposed.

4. **SwissTargetPrediction outputs are hypotheses, not validated bioactivity.** Phase 3's predicted-target rows must remain flagged as such all the way through to Phase 6 verdict assignment. Pretending a SwissTargetPrediction hit equals a ChEMBL IC50 would produce false confidence — same epistemic discipline as comp-013's animal-model-evidence rule (admissible but visibly distinguished from biochem IC50).

5. **The proposed redox/disulfide chokepoint is speculative until Phase 5.** Naming it in the chokepoint-targets.json with `_PROPOSED_` prefix is deliberate — it must not propagate into other wiki pages (modality-chokepoint-matrix, nlrp3-exploit-map, complement-c5a-gout) until Phase 5 confirms or rejects. This is the same discipline Brian's [pre-commit grep-verify gate](./manual-literature-mining.md#pre-commit-verification-gate) imposes on quantitative claims.

6. **Fungal taxonomy is messy.** *Ganoderma lucidum* in Western literature often refers to a species complex (multiple genuine species sold under one name). *Cordyceps sinensis* was renamed *Ophiocordyceps sinensis* in 2007. Phase 2 will use NCBI Taxonomy IDs as the canonical join key; common-name and TCM-name fields are for human readers, not joins.

7. **Genome-coverage upstream provenance gap.** antiSMASH-DB and MIBiG predicted-BGC entries are downstream of fungal genome assembly + annotation. For candidate species lacking an assembled genome in MycoCosm/JGI or NCBI RefSeq Fungi, predicted-BGC coverage is zero — not because the fungus encodes nothing relevant, but because no genome has been sequenced. Phase 2c will explicitly flag which candidate species lack assembled genomes; absence-of-evidence ≠ evidence-of-absence for those species.

8. **Paywalled comprehensive databases are excluded.** Dictionary of Natural Products (DNP, Chapman & Hall), SciFinder (CAS), and Reaxys are the most comprehensive curated natural-product databases but are institutionally paywalled. Their exclusion from comp-014 is a coverage limitation, not a methodology defect — but it means a true "complete fungal compound space" remains out of reach until institutional access is acquired.

9. **Marine fungi are deliberately excluded from this scope.** Marine *Penicillium* and *Aspergillus* species (and many less-studied marine basidiomycetes) produce ETP-class compounds with internal disulfide bridges (gliotoxin, sirodesmin, chetomin family) that would directly affect the redox/disulfide chokepoint thesis. The exclusion is for tractability — marine fungi sit in a different corpus (MarinLit) with different access conventions, and integrating them at Phase 2 would substantially expand scope. Effect on the redox chokepoint warrant: comp-014's evidence base for the chokepoint addition is *terrestrial-fungi-only*. A future comp-NNN extending to marine fungi could expand the warrant or convert a Phase-5-PRELIMINARY verdict to ADMIT.

10. ***Cordyceps sinensis* / *militaris* split as a join-key risk.** The Phase 1 candidate file initially conflated these two genuinely distinct organisms (different taxonomy IDs, different chemistry — cordycepin abundant in *militaris*, sparse in *sinensis*). Updated 2026-05-06 to treat them as separate candidate rows. Phase 2 dedup on NCBI Taxonomy ID rather than common-name; any Phase 2 LOTUS / NPAtlas record listing only "Cordyceps sinensis" with the wild/cultivated origin ambiguous gets routed to a manual-resolution queue rather than auto-merged.

## §7 Six Phase 2 follow-ups queued

Same pattern as [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) and [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) — Phase 2 starts when Brian green-lights:

1. **Phase 2a — LOTUS + NPAtlas pull.** Two open-license, well-API'd Western-hosted sources first. Establishes the deduplication infrastructure and the first compound × species table. Lowest-cost, fastest signal on whether the methodology is sound before committing to harder-to-pull sources.

2. **Phase 2b — KNApSAcK + NPASS + TCMSP + HIT pull.** The Asian-hosted compound and target databases. May require scraping where bulk download is not exposed; budget includes time for that. This is where ChEMBL-coverage-gap compounds get their first target hypotheses.

3. **Phase 2c — MIBiG + antiSMASH-DB BGC scan.** Genomic-encoded compound space. For each candidate species with a sequenced genome, enumerate predicted BGCs; intersect predicted-product class with chokepoint-relevant chemistry. Surfaces "compounds we should be looking for that haven't been isolated yet."

4. **Phase 3 — target mapping.** ChEMBL → HIT → PubChem BioAssay → SwissTargetPrediction cascade. Output joined to Phase 2 compound table.

5. **Phase 4 — chokepoint intersection + ranked candidate list.** Output: top-N candidate compound × chokepoint pairs, ranked by empirical-evidence weight + site fit + mechanism diversity.

6. **Phase 5 — multilingual deep-dive on top 3-5 species + redox/disulfide chokepoint confirm/reject.** CNKI, Wanfang, J-STAGE, KISS primary literature. Two-model translation cross-check. Final Phase 5 deliverable: a single decision document — does the redox/disulfide chokepoint enter the canonical wiki inventory or not?

Phase 6 (per-compound triage) is gated on Phase 5; budget separately when it lands.

## §8 Cross-references

- [`computational-experiments.md`](./computational-experiments.md) — tracking index entry for comp-014 (Status: Scoped — execution pending)
- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — canonical chokepoint inventory; comp-014 reads from this and Phase 5 may write back a new column to it
- [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) — comp-013, the methodological precedent for triage; comp-014 scales the candidate-pool acquisition
- [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md) — peer scope page for TCM × modern-rigor; comp-014 sits adjacent (medicinal mushrooms × modern rigor)
- [`complement-c5a-gout.md`](./complement-c5a-gout.md) — CP0 platform gap; comp-014 may surface fungal C5aR1 antagonists the §1.21 scan missed
- [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md) — NLRP3 sub-chokepoints; the TXNIP / redox proposal connects to this map
- [`open-source-platform.md`](./open-source-platform.md) — platform-strategy framing; comp-014 operationalizes "global-multilingual research by default" and "explore-every-avenue" claims
- [`open-enzyme-vision.md`](./open-enzyme-vision.md) — top-level mission

## Maintenance

- **Status promotions:** when each phase completes, update YAML frontmatter `status` and the `computational-experiments.md` row simultaneously. Phase 5 may trigger updates to `modality-chokepoint-matrix.md` (new column) and possibly `nlrp3-exploit-map.md` (TXNIP layer) — those propagations are sweep-daemon territory once the page transitions out of `scoped`.
- **Per-phase output files:** add to `experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/` (e.g., `phase-2-compound-table.json`, `phase-4-chokepoint-intersection.csv`). Do not gitignore.
- **Per-phase scripts:** add to `experiments/comp-014-medicinal-mushroom-compound-mapping/scripts/` (e.g., `phase_2_aggregate.py`, `phase_3_target_map.py`). Stdlib + documented external API calls only.
- **Translation provenance for Phase 5:** for each non-English source ingested, log original-language title, both translation outputs (Model A + Model B), the disagreement annotations, and the final translated text actually used in the wiki. Same discipline as [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) verification-gate disclosure.
