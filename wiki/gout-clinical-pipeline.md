---
title: "Gout Clinical Pipeline: Current Snapshot and Implications for Open Enzyme"
date: 2026-04-23
tags: ["clinical-trials", "gout", "hyperuricemia", "uricase", "NLRP3", "IL-1", "competitive-landscape", "pipeline"]
related:
  - gout-deep-dive.md
  - gout-pathophysiology.md
  - uricase.md
  - nlrp3-inflammasome.md
  - nlrp3-exploit-map.md
  - gut-lumen-sink.md
  - engineered-yeast-uricase-proposal.md
sources:
  - "ClinicalTrials.gov via Anthropic life-sciences MCP (search date: 2026-04-23)"
  - "PubMed via Anthropic life-sciences MCP"
  - "J Inflamm Res 2026;19 PMID: 41867470"
  - "Lancet Rheumatol 2020;2(5):e270-e280 PMID: 33005902"
  - "Curr Rheumatol Rep 2023;26(3):69-80 PMID: 38133712"
  - "Ann Rheum Dis 2024;83(7):945-956 PMID: 38373842"
---

# Gout Clinical Pipeline: Current Snapshot and Implications for Open Enzyme

Data compiled from ClinicalTrials.gov and PubMed via the Anthropic life-sciences MCP plugins on 2026-04-23. This page replaces scattered pipeline references across the wiki with a single, refreshable snapshot. Rerun the queries quarterly to keep it current — the underlying MCP calls are documented at the bottom.

**Bottom line up front:**

1. **ALLN-346 (oral gut-lumen uricase) program appears dead.** The Phase 2a CKD trial was terminated September 2022 with only 19 patients enrolled against a 17-site protocol. Allena Pharmaceuticals has no active gout trials. This is a meaningful update — the wiki referenced ALLN-346 as the clinical proof-of-concept for gut-lumen uricase. The concept remains valid, but its commercial champion is gone.

2. **Dapansutrile (OLT1177) in gout: published Phase 2a, but no current late-phase trial.** The 2020 Phase 2a proof-of-concept (N=34) showed 52–68% pain reduction at day 3 across four dose levels. Olatec's subsequent gout development appears stalled; their active programs moved to heart failure (completed) and COVID-19 (terminated). Phase 2b/3 in gout is **not registered on ClinicalTrials.gov as of April 2026.**

3. **Canakinumab finally got FDA approval for gout in August 2023** — the first biologic formally indicated for gout in the US, 12 years after its initial rejection. Our wiki references canakinumab but does not reflect this regulatory update.

4. **The real competitor to Open Enzyme's thesis is PRX-115 (Protalix)**, whose Phase 2 RELEASE trial began recruiting December 2025. It's a systemic pegylated uricase + methotrexate — same immunomodulator strategy as SEL-212/Krystexxa+MTX. PRX-115 being in Phase 2 proves the systemic-uricase-with-tolerance-induction path is alive. Open Enzyme's gut-lumen-uricase angle remains the untested and uncompeted path.

5. **URAT1 inhibitors are crowded.** AR882 (Arthrosi), Epaminurad (JW Pharma), Dotinurad (Eisai), SAP-001 (Shanton), and ABP-671 (Atom) are all in Phase 2b/3. Competing here is not the Open Enzyme wedge.

---

## 1. Approved Therapies and Current Standard of Care

Source: ClinicalTrials.gov via the Anthropic life-sciences MCP; regulatory status synthesized from *J Inflamm Res* 2026;19 ([DOI: 10.2147/JIR.S592891](https://doi.org/10.2147/JIR.S592891), PMID: 41867470).

| Therapy | Target | Status | Notes |
|---|---|---|---|
| Allopurinol | Xanthine oxidase | Generic (1966) | First-line urate-lowering; HLA-B*58:01 hypersensitivity risk |
| Febuxostat | Xanthine oxidase | Generic (2009 US) | CARES trial cardiovascular signal |
| Pegloticase (Krystexxa) | Uricase (PEGylated pig/baboon chimera) | FDA 2010 | **Refractory gout only**; now co-administered with methotrexate (Phase 4 NCT04772313) to mitigate anti-drug antibodies |
| Rasburicase (Elitek/Fasturtec) | Uricase (*A. flavus*, in *S. cerevisiae*) | FDA 2002 | **Tumor lysis syndrome only** — not approved for chronic gout. Open Enzyme's uricase is the same enzyme. |
| Lesinurad | URAT1 | FDA 2015, withdrawn 2019 | Commercial failure; Ardea Biosciences |
| Canakinumab (Ilaris) | IL-1β (mAb) | **FDA approved August 2023 for gout** — first biologic indication | Novartis; previously approved for CAPS/JIA. *J Inflamm Res* 2026 (PMID: 41867470). |
| Anakinra (Kineret) | IL-1 receptor antagonist | Off-label for gout | 2018 Sobi trial (NCT03002974) showed non-inferiority to triamcinolone |
| Rilonacept (Arcalyst) | IL-1 trap | Rejected 2012 for gout | Recent Regeneron Phase 3 (NCT00856206) in 1,315 patients — demonstrated efficacy but FDA declined |
| Colchicine | β-tubulin (ASC speck block) | Generic | Narrow therapeutic window; CP3 of NLRP3 pathway |
| NSAIDs | COX-1/2 | Generic | Symptomatic only |

**Implication for Open Enzyme:** Pegloticase + methotrexate (Amgen/Horizon Krystexxa+MTX) and canakinumab are the "biologics" standard-of-care for refractory/hard-to-treat gout. Both are expensive and IV/SC. The oral, food-derived positioning (engineered koji as adjunct to allopurinol) avoids direct competition with these.

---

## 2. The Critical Update: ALLN-346 Program Discontinued

Source: NCT04987294, NCT04987242, NCT04236219, NCT05168683 via the Anthropic life-sciences ClinicalTrials.gov MCP.

**Wiki references to ALLN-346 as "clinical proof-of-concept for gut-lumen uricase" are now backward-looking, not forward-looking.** Status by trial:

| Trial | Phase | Status | N | Dates |
|---|---|---|---|---|
| NCT04236219 | 1 (SAD) | Completed | 24 | 2020-09 to 2020-11 |
| NCT05168683 | 1 (scintigraphy, enteric coating) | Completed | 12 | 2022-01 to 2022-02 |
| NCT04987242 | 2 (inpatient hyperuricemia) | Completed | 16 | 2021-07 to 2022-03 |
| **NCT04987294** | **2a (CKD, multicenter)** | **TERMINATED** | **19** (of planned >200 across 17 sites) | **Started and terminated 2022-09-02** |

The Phase 2a CKD trial — which was the pivotal study — was terminated on its scheduled primary completion date with 19 enrolled patients across 17 US sites. No published efficacy results.

**Allena Pharmaceuticals** has no active trials on ClinicalTrials.gov after September 2022. The ALLN-346 asset appears to be commercially dead.

**Why this matters for Open Enzyme:**

- The *scientific rationale* for gut-lumen uricase remains intact. ABCG2-mediated gut secretion of uric acid is responsible for ~1/3 of total urate excretion (see [gut-lumen-sink.md](gut-lumen-sink.md)), and enzymatic degradation of luminal urate should reduce systemic load.
- The *commercial* proof-of-concept is absent. ALLN-346 is not a precedent for "gut-lumen uricase works in Phase 2"; it's a precedent for "one company tried this and the trial did not deliver a pivotal readout."
- This reframes Open Enzyme's positioning: we are no longer "the citizen-science version of a validated clinical program." We are "the citizen-science version of a promising mechanism that pharma has not yet validated."
- The open-source, food-grade positioning may be an advantage here — a fermented koji supplement does not need a Phase 3 trial to reach users.

**Action:** update the following pages to reflect ALLN-346's current status (not an endorsement, but an unfinished precedent):
- [gout-deep-dive.md](gout-deep-dive.md) — "Current Treatments" section
- [gut-lumen-sink.md](gut-lumen-sink.md) — remove ALLN-346 as "live clinical precedent"
- [engineered-yeast-uricase-proposal.md](engineered-yeast-uricase-proposal.md) — reframe the commercial context
- `index.md` — "Key Science References" table (the ALLN-346 row is current truth, but should note terminated status)

---

## 3. The NLRP3 Inflammasome Gout Program: Dapansutrile Stalled, Pipeline Moved Elsewhere

According to PubMed, Dapansutrile (OLT1177) Phase 2a proof-of-concept in gout was published in *Lancet Rheumatology* 2020 ([DOI: 10.1016/s2665-9913(20)30065-5](https://doi.org/10.1016/s2665-9913(20)30065-5), PMID: 33005902, Klück et al., Dinarello/Joosten groups at Radboud + Olatec).

**Phase 2a results (N=34):**
- Open-label, 4 dose levels (100, 300, 1000, 2000 mg/day × 8 days)
- Target joint pain reduction, baseline to day 3: 52.4% (100 mg), 68.4% (300 mg), 55.8% (1000 mg), 57.6% (2000 mg) — all p ≤ 0.063
- Target joint pain reduction, baseline to day 7: 82.1%, 84.2%, 68.9%, 83.9% — all p ≤ 0.031
- 25/34 patients had treatment-emergent AEs (mostly metabolism and GI); 2 SAEs (one flare worsening, one coronary stenosis unrelated)
- **Conclusion:** "Dapansutrile is a specific NLRP3 inflammasome inhibitor with a satisfactory safety profile and efficacy in the reduction of target joint pain."

**Potency reframing (ChEMBL v34 cross-check, 2026-04-23):** Dapansutrile's curated cellular IC50 is **1.0 nM in mouse J774A.1 cells but 1.0 μM (1,000 nM) in human MDM cells — a 1,000× species gap** (*Eur J Med Chem* 2020/2023; *Bioorg Med Chem Lett* 2021). The 100–2,000 mg/day Phase 2a oral doses are consistent with human-cell μM potency at high systemic exposure, not with sub-nanomolar MCC950-class potency. This does not diminish the Phase 2a efficacy — the clinical result stands — but it reframes how the compound class should be described to potential collaborators: dapansutrile is an oral, μM-class human NLRP3 inhibitor with a very wide mouse-vs-human potency cliff, not a sub-nanomolar miracle drug. It also validates Open Enzyme's preference for human-cell (THP-1) validation assays over rodent cellular screens. (In Vitro; source: nlrp3-inhibitor-screen.md)

**What happened next:**
- No Phase 2b or Phase 3 in gout on ClinicalTrials.gov (as of 2026-04-23)
- Olatec pivoted to heart failure (Phase 1b NCT03534297, completed 2019) and COVID-19 (Phase 2 NCT04540120, terminated 2022)
- A 2026 review (*J Inflamm Res*, [DOI: 10.2147/JIR.S592891](https://doi.org/10.2147/JIR.S592891), PMID: 41867470) describes dapansutrile as having "advanced through clinical development after incorporating safety lessons from the hepatotoxicity experience associated with MCC950" — but does not cite any pivotal gout readout beyond the 2020 paper

**NLRP3 inhibitor pipeline has moved OUT of gout:**

| Compound | Sponsor | Indication | Phase | Trial |
|---|---|---|---|---|
| DFV890 | Novartis | Knee osteoarthritis | 2 completed 2024-12 | NCT04886258 |
| NT-0796 | NodThera | Obesity (+ semaglutide) | 2a active 2025-10 | NCT07220629 |
| VTX3232 | Zomagen | Parkinson's | 2a completed 2025-04 | NCT06556173 |
| VENT-02 | Ventus Therapeutics | Parkinson's | 1b **TERMINATED 2025-10** | NCT06822517 |
| Inzomelid | Inflazome (Roche) | CAPS (orphan) | 1 completed | NCT04015076 |
| ZYIL1 | Zydus | Healthy volunteers | 1 completed | NCT04972188 |

**No active NLRP3-specific trials in gout as of April 2026.** The unmet need is real (pegloticase flares during dissolution, MSU-driven pyroptosis), but the pharma interest has drifted to metabolic and neurological indications where NLRP3 biology has broader appeal.

**Implication for Open Enzyme:** the NLRP3 multi-target stack (oridonin + BHB + KPV + disulfiram) is not being pre-empted by a pharma success in gout. Dapansutrile's dormancy actually supports the project's "food-derived NLRP3 adjunct" positioning — the prescription pipeline isn't delivering.

### Zileuton — Latent CP6a Repurposing Candidate (Pharma Blind Spot)

> **Zileuton (Zyflo / Zyflo CR) — latent CP6a repurposing candidate.** FDA-approved oral 5-LOX inhibitor for asthma (1996; Critical Therapeutics then Cornerstone Therapeutics, now generic). The only approved direct 5-LOX drug in the US. **Never tested in gout** despite direct mechanism match at CP6a (5-LOX → LTB4 → neutrophil chemotaxis, the amplification loop that drives the neutrophil infiltration phase of a flare). Dose precedent: 1,200 mg BID (controlled-release). Safety: hepatotoxicity boxed warning — requires LFT monitoring. Zileuton's gout potential has been overlooked because gout → NLRP3 (CP2) attracted the pharma R&D attention; the 5-LOX neutrophil-amplification branch (CP6a) is unrepresented in gout trial registries. ClinicalTrials.gov search (2026-04-24) returns zero gout trials for zileuton. (Clinical Trial; source: Pass 2 synthesis 2026-04-24 via wiki/nlrp3-exploit-map.md)

---

## 4. The Direct Competitor to Watch: PRX-115 (Protalix)

Source: NCT07280156 via the life-sciences ClinicalTrials.gov MCP.

**PRX-115 RELEASE Phase 2 trial:**
- Sponsor: Protalix (Karmiel, Israel — known for ProCellEx plant-cell expression platform; taliglucerase alfa precedent)
- Started: 2025-12-22, primary completion 2027-12, full completion 2028-06
- N=150, multicenter Phase 2, randomized, double-blind, placebo-controlled
- Intervention: Pegylated recombinant uricase, IV infusion, 24 weeks, with and without methotrexate (MTX) co-administration
- Primary endpoint: % of patients with sUA <6 mg/dL for ≥80% of time during Month 6
- **Key exclusion:** "Prior exposure to any experimental or marketed uricase" — targeting treatment-naive gout patients
- **Key exclusion:** eGFR ≤ 40, kidney transplant, dialysis → excludes the CKD population that ALLN-346 specifically targeted

**Why this matters:**

1. **Same strategy as SEL-212 (Sobi) and Krystexxa+MTX (Amgen):** systemic uricase + immunomodulator to prevent anti-drug antibody formation. Three programs now pursuing this exact approach. The anti-drug antibody problem is real and well-characterized.

2. **PRX-115 is targeting the treatment-naive gout population,** not just refractory/CKD. This is a more ambitious commercial positioning than pegloticase's current label.

3. **The gut-lumen angle is uncontested.** Every competitor uses systemic delivery. None use gut-retained/lumen-active uricase. Open Enzyme's engineered koji path remains the only gut-lumen approach in any form of development, clinical or otherwise.

4. **Watch for RELEASE readouts.** Primary completion Dec 2027 means pivotal data by Q1 2028. A positive PRX-115 readout would validate IV-uricase-with-tolerance-induction as the dominant commercial path. A negative readout would reopen the mechanism question — systemic uricase may not be tolerable long-term regardless of immunomodulation.

---

## 5. SSS11 (China): Pegylated *Candida utilis* Uricase

Source: NCT06629376 via the life-sciences ClinicalTrials.gov MCP.

- Sponsor: Shenyang Sunshine Pharmaceutical (China)
- Phase 1, N=60, recruiting since 2023, completion 2026-12
- Single center: Huashan Hospital, Fudan University, Shanghai
- Intervention: Pegylated recombinant *Candida utilis* uricase (PEG-CuU)

**Why this is interesting to Open Enzyme:**

- *Candida utilis* is a food-grade yeast; its uricase is one of the variants discussed in [uricase-variant-selection.md](uricase-variant-selection.md) alongside *A. flavus* (rasburicase source), *A. globiformis*, and *B. subtilis* uricases
- This is the first clinical use of a *C. utilis*-derived uricase
- SSS11 is still systemic IV, not gut-lumen, so it doesn't contest Open Enzyme's delivery angle
- Higher specific activity vs. *A. flavus* uricase is the main engineering rationale (from published biochem data); clinical-grade confirmation pending

---

## 6. Other Gout Pipeline Programs (Phase 2b / Phase 3)

Aggregate from the ClinicalTrials.gov MCP query: 153 total Phase 2/3 gout trials in the registry. Filtered to active or recent-pivotal programs not already covered above:

### URAT1 Inhibitors (crowded field)

| Compound | Sponsor | Phase | Status | Trial |
|---|---|---|---|---|
| AR882 | Arthrosi Therapeutics | 3 | Active, not recruiting | NCT06846515, NCT06439602 (both 750 patients, ending 2026) |
| Epaminurad | JW Pharmaceutical | 3 | Active, not recruiting | NCT05815901 (588 patients) |
| Dotinurad | Eisai | 3 | Completed 2023-06 | NCT05007392 (451 patients vs. febuxostat) |
| SAP-001 | Shanton Pharma | 2b | Active, not recruiting | NCT05690204 (87 patients) |
| ABP-671 | Atom Therapeutics | 2 | Not yet recruiting (start 2026-06) | NCT07323095 (80 patients, CKD) |

### Novel Xanthine Oxidase Inhibitors

| Compound | Sponsor | Phase | Status | Trial |
|---|---|---|---|---|
| Tigulixostat | LG Chem | 3 | Completed 2024-11 | NCT05586958 (354 patients) |
| HR091506 | Jiangsu Hengrui | 3 | Completed 2025-08 | NCT06139393 (765 patients) |

### Uricase Programs (systemic, all IV)

| Compound | Sponsor | Phase | Status | Trial |
|---|---|---|---|---|
| **PRX-115** | Protalix | 2 (RELEASE) | Recruiting | NCT07280156 |
| **SSS11** | Shenyang Sunshine | 1 | Recruiting | NCT06629376 |
| SEL-212 | Selecta → Sobi | 3 | Completed 2022-07 | NCT04513366 (112 patients) |
| Pegloticase + MTX | Amgen (Horizon) | 4 | Completed 2022-08 | NCT04772313 |

### IL-1β / Inflammasome Downstream

| Compound | Sponsor | Phase | Status | Trial |
|---|---|---|---|---|
| Genakumab | GeneScience (China) | 3 | Completed 2024-04 | NCT05983445 (313 patients) — Chinese canakinumab competitor |
| Anakinra vs. Prednisone in CKD gout | APHP (academic) | 2 | **Suspended** | NCT04844814 |

### Acute Flare Novel

| Compound | Sponsor | Phase | Status | Trial |
|---|---|---|---|---|
| ABP-745 | Atom Therapeutics | 2 | Recruiting | NCT07145229 (380 patients, colchicine-controlled) |

---

## 7. Emerging Biology Worth Tracking

According to PubMed:

**TNFSF14 as a new gout biomarker** — Ea et al. *Annals of the Rheumatic Diseases* 2024 ([DOI: 10.1136/ard-2023-225305](https://doi.org/10.1136/ard-2023-225305), PMID: 38373842). Olink 92-protein inflammation panel on gout flare vs. intercritical vs. treat-to-target. TNFSF14 (TNF superfamily 14, also called LIGHT) was the highest fold-change biomarker during flare after IL-6. Ex vivo TNFSF14 blockade reduced LPS + MSU-induced cytokine response. Single-nucleotide polymorphisms in TNFSF14 affected myeloid cytokine production. **This is a candidate new therapeutic target, distinct from NLRP3 and IL-1β.** Not yet in any clinical program — worth tracking.

---

## 8. How to Refresh This Page

The data above was pulled from ClinicalTrials.gov and PubMed via the Anthropic life-sciences MCP plugins (see [bio-ai-tools.md](bio-ai-tools.md) for install instructions). To regenerate a current snapshot:

**ClinicalTrials.gov queries used:**

```text
search_trials(
  condition="gout OR hyperuricemia",
  phase=["PHASE2","PHASE3"],
  status=["RECRUITING","ACTIVE_NOT_RECRUITING","NOT_YET_RECRUITING","COMPLETED"],
  page_size=50
)

search_trials(intervention="dapansutrile OR OLT1177 OR NLRP3", page_size=20)
search_trials(intervention="ALLN-346 OR uricase OR rasburicase OR pegloticase",
              condition="gout OR hyperuricemia", page_size=20)
search_trials(intervention="rilonacept OR canakinumab OR firsekibart OR anakinra",
              condition="gout", page_size=20)

get_trial_details(nct_id=<NCT>)  # for each program of interest
```

**PubMed queries used:**

```text
search_articles(query="dapansutrile OR OLT1177 AND gout", sort="pub_date")
search_articles(query="ALLN-346 OR \"Allena Pharmaceuticals\" AND gout", sort="pub_date")
get_article_metadata(pmids=[...])
```

Recommended cadence: quarterly refresh. Trial statuses change (especially TERMINATED events), and new Phase 2/3 programs emerge ~1 per quarter in this therapeutic area.

---

## Related Pages

- [Gout Deep Dive](gout-deep-dive.md) — core pathophysiology and treatment landscape
- [Gout Pathophysiology](gout-pathophysiology.md) — purine metabolism, MSU crystal formation, NLRP3 activation
- [Uricase](uricase.md) — enzyme biology and evolutionary loss
- [Gut-Lumen Sink](gut-lumen-sink.md) — ABCG2 pathway; the insight that systemic absorption isn't needed
- [NLRP3 Inflammasome](nlrp3-inflammasome.md) — six-chokepoint model
- [NLRP3 Exploit Map](nlrp3-exploit-map.md) — multi-target stack strategy
- [Engineered Yeast Uricase Proposal](engineered-yeast-uricase-proposal.md)
- [Bio-AI Tools](bio-ai-tools.md) — MCP plugin install and workflow

---

*Generated 2026-04-23 using the Anthropic life-sciences marketplace MCP plugins (pubmed, clinical-trials). Citations include DOI links per the PubMed MCP's attribution requirement.*
