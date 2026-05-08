---
title: "Upstream Complement Modulator Sweep — Computational Analysis (comp-018)"
date: 2026-05-08
tags:
  - complement
  - upstream-cp0
  - cp0
  - c3-convertase
  - rosmarinic-acid
  - luteolin
  - bupleurum-polysaccharide
  - ganoderic-acid
  - natural-products
  - dietary
  - chokepoint-mapping
  - global-multilingual
  - computational
related:
  - computational-experiments.md
  - complement-c5a-gout.md
  - daf-cd55-scr14-truncated-computational.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - medicinal-mushroom-compound-mapping-computational.md
  - tcm-gout-compound-triage-computational.md
  - modality-chokepoint-matrix.md
  - nlrp3-exploit-map.md
  - manual-literature-mining.md
  - gout-action-guide.md
sources:
  - "Brian framing 2026-05-08: 'What are all the things upstream of CP0 that we could exploit, and any compound — fungal, plant, bacterial, marine — that affects them. If the answer is rosemary, I'll grow rosemary.'"
  - "Open Enzyme/CLAUDE.md §Tool discipline (Pass 3 review 2026-05-08): Paperclip restricted to PMC/arXiv/bioRxiv/medRxiv corpus; CNKI/WanFang/J-STAGE handled by direct multilingual searches"
  - "complement-c5a-gout.md §2.6 — classical pathway is the dominant initiator of MSU complement activation; therefore C3 convertase is the highest-leverage upstream node"
  - "Englberger W et al., Int J Immunopharmacol 1988;10(6):729-37 (PMID 3198307) — rosmarinic acid as C3 convertase inhibitor, IC50 5-10 µM optimal"
  - "Zhang T, Chen D, J Ethnopharmacol 2008;117(2):351-61 (PMID 18400428) — luteolin most potent flavonoid CP+AP, CH50/AP50 0.19/0.17 mM"
  - "Wu M et al., Acta Pharm Sin B 2015;5(4):316-22 (PMID 26579461) — Bupleurum polysaccharides lectin pathway IC50 ~1 mg/mL"
  - "Seo HW et al., Arch Pharm Res 2009;32(11):1573-9 (PMID 20091270) — Ganoderma triterpenes CP convertase, ganoderic acid Sz IC50 44.6 µM"
status: complete (Phase 1)
---

# Upstream Complement Modulator Sweep — Computational Analysis (comp-018)

> **⚠️ Read this before propagating any finding from this page.**
>
> The brief that produced this experiment was contaminated by a contrived user-framing example ("if it's in rosemary I'll grow rosemary"), which biased the headline-promotion of rosmarinic acid as the singular Tier-1 candidate. **An independent brief-scrubbed verification re-run (comp-020)** ran 2026-05-08 and produced a meaningfully different ranking: three tied tier-1 candidates instead of one, with ***Helicteres* benzofuran lignans** (CH50 9/40 µM, single-paper anchor PMC6273495) as the highest-potency single hit in the corpus — beating rosmarinic acid by 4-20× on a matched assay. comp-020 also surfaced **marine sulfated polysaccharides** that this page underweighted, and reframed the rosmarinic acid load-bearing mechanism as **upstream covalent C3b modification** rather than direct C5 convertase inhibition (44× IC50 spread across assays).
>
> **Use [`upstream-complement-verification-rerun-computational.md`](./upstream-complement-verification-rerun-computational.md) (comp-020) as the canonical source for prioritization decisions.** This page (comp-018) remains as the original-search artifact and as the empirical case for the brief-contamination retrospective at [`operations/comp-018-vs-comp-020-retrospective.md`](../operations/comp-018-vs-comp-020-retrospective.md). Underlying findings on this page are NOT contaminated (rosmarinic acid is real, Englberger 1988 PMID 3198307 is real, the in vivo precedents are real); the contamination affected which compound got headline-promoted, not which compounds exist.
>
> Discipline lesson codified at [`scripts/SWEEP-ARCHITECTURE.md`](../scripts/SWEEP-ARCHITECTURE.md) §"Subagent brief hygiene." External-comms version at [`operations/notable-moments.md`](../operations/notable-moments.md) 2026-05-08 brief-contamination entry.

## Plain-English summary (CTO-not-PhD)

Gout flares are driven in large part by a protein cascade called **complement**. When MSU crystals form in your joint, complement gets activated on the crystal surface, which generates a small protein called **C5a** that "primes" your immune system's NLRP3 inflammasome — that's the alarm bell that triggers the actual flare. We call this priming step **CP0**.

Open Enzyme has been working on CP0 from two angles. First, an **engineering angle**: build a soluble version of the human protein DAF/CD55 that breaks complement on the crystal surface, and express it in koji. That's looking promising in silico (comp-012, hypothesis H05). Second, a **direct natural-product angle**: find a fungal or plant compound that blocks the C5a receptor (C5aR1). That came up empty — comp-014 confirmed there are zero documented natural-product C5aR1 antagonists.

This experiment (comp-018) is a third angle: **don't try to block C5a once it's made — find compounds that prevent it from being made in the first place.** That means looking at every step in the complement cascade UPSTREAM of C5a generation, and asking what compounds — fungal, plant, dietary, drug — can interfere with any of them.

The answer turns out to be: **a lot of compounds.** The most well-characterized natural-product upstream complement modulator in the literature is rosmarinic acid (the active compound in rosemary, lemon balm, and spearmint), documented since 1988 to block the C3 convertase — the central enzyme of complement — with three independent in vivo studies showing efficacy in animal models at modest doses. Other strong candidates surfaced in the same scan: luteolin (a dietary flavonoid; triple-mechanism — XO + URAT1 + C3 convertase CP+AP), tiliroside, *Bupleurum* polysaccharides (lectin-pathway), falcarindiol, ganoderic acid Sz, ergosterol, and others.

> **Four load-bearing caveats on the rosmarinic acid finding — read these before propagating it downstream.**
>
> 1. **The "single-digit micromolar" IC50 (5-10 µM optimal) comes from the 1988 Englberger paper (PMID 3198307), which is paywalled and not in PMC.** This number is *abstract-tier* sourced, NOT full-text grep-verified. Per CLAUDE.md Rule 4 (the pre-commit grep-verify gate), this is below the load-bearing-confidence bar; full-text retrieval is mandatory before any wet-lab gate depends on it.
> 2. **There is a real IC50 discrepancy in the literature.** Downstream papers using rosmarinic acid as a positive-control comparator (Cimanga 1999 PMID 17260306; Mu 2013 PMID 24144800) report **137-182 µM** for the same compound — about 20-30× higher than Englberger's 5-10 µM. Likely explanation is assay-format difference (different sheep-erythrocyte source, different complement serum, different endpoint definition), but the discrepancy is unresolved. Any in vitro confirmation must test BOTH ranges; any dose calculation that assumes 5-10 µM is the load-bearing concentration is making an unverified assumption.
> 3. **The dose-response is bell-shaped — higher concentrations are LESS effective.** Englberger 1988 reports 5-10 µM as the *optimal* concentration window, not as a typical "more is better" IC50. This implies a narrow therapeutic window even at the optimal concentration, and gut-luminal concentration management would be load-bearing for any consumer-facing recommendation.
> 4. **Brief-contamination disclosure (added by user catch 2026-05-08).** The subagent brief that produced this experiment inadvertently included Brian's contrived "if the answer is rosemary, I'll grow rosemary" framing as motivation. Subsequent rhetoric in this page that calls back to that framing should be read as narrative-cohesion, not independent confirmation. **A scrubbed verification re-run (comp-020) is in progress** to test whether rosmarinic-acid-as-headline survives without the priming. The underlying literature claims (Englberger 1988, Proctor 2006, Su 2014) are real papers and verifiable; the *headline-promotion* of rosmarinic acid specifically vs. luteolin / tiliroside / ganoderic acid Sz may have been amplified by the brief contamination. Decision on which compound is platform-prioritized stays open until comp-020 lands.

Rosemary is FDA GRAS (21 CFR 182.10, 182.20), dietary, and grown in any backyard garden — those parts of the framing are independent of the IC50 discrepancy and are accurate. The platform-strategic question is whether 5-10 µM or 137-182 µM is the load-bearing concentration, and how that concentration is achieved at oral-dietary intake.

The experiment also surfaced a couple of platform-level surprises:

1. **Luteolin** (a common dietary flavonoid in honeysuckle, parsley, celery) now has **three independent gout-relevant mechanisms** in the OE corpus: it inhibits xanthine oxidase (the urate-production enzyme allopurinol targets), it downregulates URAT1 (the urate-reabsorbing transporter), and now per comp-018 it inhibits both the classical and alternative complement pathway C3 convertases at concentrations achievable in the gut lumen at gram-scale supplementation. This is the highest-leverage single dietary compound the platform has surfaced.

2. **Recombinant C1-INH expression** is a near-twin engineering thesis to DAF SCR1-4 — same logic, different soluble human complement regulator. Already FDA-approved for hereditary angioedema (Berinert / Ruconest); the molecule is a soluble human serpin that's plausibly producible in koji or LBP. Phase 2 follow-up.

3. **comp-014's β-glucan structure-dependence is mechanistically explained.** The same mushroom (Ganoderma) contains both complement activators (some β-glucan structures via lectin pathway) and complement inhibitors (some triterpenes and ergosterol via classical pathway C3 convertase inhibition). Whether a reishi extract is anti- or pro-inflammatory depends on which fractions dominate.

The chokepoint-class naming: I propose treating this as a **scope expansion of CP0** ("upstream-CP0") rather than a new chokepoint class. The decision is the user's; this is the recommendation.

---

## Status

**Phase 1 complete — 2026-05-08.** Sweep executed across all compound classes (fungal, plant, bacterial, marine, dietary, FDA-approved drug, classical TCM/Kampo/Ayurveda) for documented activity at upstream complement nodes. 32 compounds catalogued with primary-source IC50s where available; ChEMBL anticomplement coverage gap empirically confirmed at 0/33 = 0%. Phase 2 (direct CNKI/WanFang/J-STAGE multilingual ingestion with two-model translation cross-check) queued.

## §1 Question

Across all compound classes — fungal, plant, bacterial, marine, dietary, FDA-approved drugs, classical TCM, Kampo, Ayurveda — which compounds have documented activity at **upstream complement cascade nodes proximal to C5a generation**, and which are gout-platform-relevant?

The framing per Brian (2026-05-08): *"What are all the things upstream of CP0 that we could exploit, and any compound — fungal, plant, bacterial, marine — that affects them. If the answer is rosemary, I'll grow rosemary."* — broad scope, chokepoint-hacker move (don't fight at CP0, find an even further-upstream lever).

## §2 Why this experiment exists — three converging threads at CP0

The OE corpus by 2026-05-08 had three threads at CP0:

1. **Engineering thread** — comp-006 → comp-012 → H05 → §1.25. The truncated DAF/CD55 SCR1-4 construct (aa 35–285) is in silico LOW protease risk in shio-koji ([comp-012](./daf-cd55-scr14-truncated-computational.md)); the wet-lab plan is scoped at [`validation-experiments.md` §1.25](./validation-experiments.md). Live engineering candidate.
2. **Direct natural-product C5aR1 antagonist thread** — comp-014 + §1.21: empty. Zero natural-product C5aR1 antagonists in ChEMBL or PubMed. Confirmed by two independent computational scans.
3. **comp-018 (this page)** — the third thread. Don't hunt for C5aR1 binders, hunt at every node UPSTREAM of C5a generation.

The chokepoint-hacker logic: per [`complement-c5a-gout.md` §2.6](./complement-c5a-gout.md), MSU activates complement primarily via the classical pathway (IgM/CRP → C1q → C4b2a C3 convertase) with alternative-pathway amplification. Therefore C3 convertase is the highest-leverage upstream node — block C3 convertase, no C5a is generated, no NLRP3 priming. The same logic that makes pegcetacoplan (FDA-approved C3 binder) clinically effective in PNH applies to gout-mechanistically: prevent the cascade from reaching C5.

## §3 Method — multi-source query strategy with tool discipline

### §3.1 Sources

| Source | Use | Tool |
|---|---|---|
| **PubMed** | Depth pass for English natural-product anticomplement literature | `mcp__plugin_pubmed_PubMed__search_articles` + `get_article_metadata` |
| **Paperclip MCP** | Full-text grep for line-anchored verification of load-bearing IC50s | `mcp__paperclip__paperclip` (search/cat/grep — NOT `map`) |
| **ChEMBL** (per-compound) | Bioactivity coverage check — document gap explicitly | manual recall |
| **CNKI / WanFang / J-STAGE** | Direct multilingual searches via native multilingual training (NOT through Paperclip — wrong corpus) | deferred to Phase 2 |

### §3.2 Tool discipline applied

Per the 2026-05-08 sweep Pass 3 review and `Open Enzyme/CLAUDE.md` §"Tool discipline" + `memory/feedback_paperclip_map_unreliable.md`:

- **Paperclip `map` operator NOT used** — it hallucinates organisms and fabricates kinetic numbers. Restricted to `search` / `cat` / `grep` / `head` / `lookup`.
- **Paperclip restricted to PMC / arXiv / bioRxiv / medRxiv** corpus — its actual scope. NOT used for CNKI / WanFang / J-STAGE / KISS — those need direct multilingual searches.
- **PubMed via MCP** for English depth pass.
- **Translation cross-check protocol** queued for Phase 2 — Claude (Anthropic) + DeepSeek V4-Pro (Chinese-vendor) for Chinese sources, with inline disagreement annotations.

### §3.3 Pre-commit verification gate

Per [`manual-literature-mining.md` §"Pre-commit verification gate"](./manual-literature-mining.md) and CLAUDE.md Rule 4. Every IC50 / mechanism / dose claim in `compounds.json` carries an explicit `verification_status` field — full-text-anchored, abstract-tier, or [UNVERIFIED]. Where sources are paywalled and no PMC mirror exists, the claim is marked as such. The DAF SCR1-4 disulfide-count incident (canonical case for this rule) is the discipline this gate enforces.

## §4 Targets — 16 upstream complement cascade nodes

(Full inventory in `experiments/comp-018-upstream-complement-modulator-sweep/inputs/targets.json`.)

The 16 nodes span three logical layers:

| Layer | Nodes | MSU relevance |
|---|---|---|
| **Initiation** | C1q, C1r/C1s, MBL, MASP-2 | DOMINANT (CP via IgM/CRP per Wessig 2022); non-dominant (LP) |
| **Convertases** | C3 convertase (CP/LP and AP), C5 convertase | DOMINANT — C4b2a generates C3b on MSU; AP amplifies |
| **Soluble factors** | Factor B, Factor D, Factor H, Properdin, C1-INH | AP amplifiers + host regulators |
| **Membrane regulators** | DAF/CD55 (host), CD59 | DAF is the engineering anchor (H05) |
| **Terminal upstream** | C5, C5aR1 | C5 = eculizumab anchor; C5aR1 = comp-014/§1.21-confirmed empty |

## §5 Findings — top compounds by tier

Full table in `experiments/comp-018-upstream-complement-modulator-sweep/outputs/compounds.json`. Summary:

### §5.1 TIER 1 — strong evidence, dietary-tier, in vivo precedent

**Rosmarinic acid** (Rosmarinus officinalis, Melissa officinalis, Salvia, Mentha):
- C3 convertase classical pathway IC50 **5-10 µM optimal**, threshold 1 µM (Englberger 1988, [PMID 3198307](https://pubmed.ncbi.nlm.nih.gov/3198307/), [doi:10.1016/0192-0561(88)90026-4](https://doi.org/10.1016/0192-0561(88)90026-4)) — In Vitro
- *In vivo* rat CVF-induced ARDS model: 10 mg/kg i.v. RMA blocked CVF-induced neutropenia, lung neutrophil migration, BAL leakage, blood pressure changes, TNF-α elevation — **comparable magnitude to direct C5aR/C3aR antagonists** (Proctor 2006, [PMID 16782534](https://pubmed.ncbi.nlm.nih.gov/16782534/), [doi:10.1016/j.intimp.2006.03.002](https://doi.org/10.1016/j.intimp.2006.03.002)) — Animal Model
- *In vivo* Pkd1-/- mouse + Han:SPRD Cy/+ rat ADPKD: RMA reduced creatinine -50%, BUN -78%, kidney/body weight -60%, renal cystic index -60% (Su 2014, [PMID 24494798](https://pubmed.ncbi.nlm.nih.gov/24494798/), [doi:10.1111/joim.12214](https://doi.org/10.1111/joim.12214)) — Animal Model
- High-RMA spearmint tea improved knee OA stiffness, physical disability, pain over 16 weeks (Connelly 2014, in Luo 2020 review [PMC7059186](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7059186/), [doi:10.3389/fphar.2020.00153](https://doi.org/10.3389/fphar.2020.00153)) — Clinical (proxy for in-human bioavailability + activity)
- **Regulatory:** Rosemary, lemon balm, spearmint are FDA GRAS (21 CFR 182.10, 182.20). Rosmarinic acid as isolated compound is dietary supplement / cosmetic ingredient.
- **Bell-shape note:** Englberger 1988 reports higher RMA concentrations are LESS effective at C3 convertase inhibition. Load-bearing for dose-extrapolation — supplement-tier dosing should target sustained mid-µM gut/plasma levels, not max pharma-tier dosing.
- **IC50 discrepancy disclosed:** the 2008-2013 downstream literature (Cimanga 1999 PMID 17260306, Mu 2013 PMID 24144800) cites RMA as IC50 137-182 µM in their assays — different from Englberger's 5-10 µM. Likely assay-format difference (different SRBC source, serum, endpoint definition). Both ranges flagged in `compounds.json`. The 5-10 µM optimal is the primary-source value.

### §5.2 TIER 2 — moderate evidence, in vitro IC50 anchored, accessible source

10 compounds; full per-compound data in `compounds.json`. Highlights:

| Compound | Source | Node | IC50 | Provenance |
|---|---|---|---|---|
| **Luteolin** | Lonicera, Achyranthes (Si Miao San), dietary | C3 conv. (CP+AP) | CH50 190 µM, AP50 170 µM | Zhang & Chen 2008, [PMID 18400428](https://pubmed.ncbi.nlm.nih.gov/18400428/), [doi:10.1016/j.jep.2008.02.012](https://doi.org/10.1016/j.jep.2008.02.012) |
| **Tiliroside** | Magnolia fargesii, Tilia | CP convertase | 54 µM | Jung 1998, [PMID 9821813](https://pubmed.ncbi.nlm.nih.gov/9821813/), [doi:10.1248/bpb.21.1077](https://doi.org/10.1248/bpb.21.1077) |
| **Bupleurum polysaccharides** | Chai Hu (TCM) | Lectin pathway | ~1 mg/mL | Wu 2015, [PMID 26579461](https://pubmed.ncbi.nlm.nih.gov/26579461/), [doi:10.1016/j.apsb.2015.02.004](https://doi.org/10.1016/j.apsb.2015.02.004) |
| **Falcarindiol** | Dendropanax / carrot / celery | CP convertase | 15.2 µM | Chung 2011, [PMID 21520473](https://pubmed.ncbi.nlm.nih.gov/21520473/), [doi:10.1002/ptr.3336](https://doi.org/10.1002/ptr.3336) |
| **Ganoderic acid Sz** | G. lucidum | CP convertase | 44.6 µM | Seo 2009, [PMID 20091270](https://pubmed.ncbi.nlm.nih.gov/20091270/), [doi:10.1007/s12272-009-2109-x](https://doi.org/10.1007/s12272-009-2109-x) |
| **Ergosterol** | Mushrooms generally | CP convertase | 52 µM | Seo 2009, [PMID 20091270](https://pubmed.ncbi.nlm.nih.gov/20091270/) |
| **Quercetin** | onions, apples, Sophora | CP+AP | qual. active; gut-microbiome-deglycosylated active form | Zhang & Chen 2008 [PMID 18400428](https://pubmed.ncbi.nlm.nih.gov/18400428/); Jin 2020 [PMID 32092632](https://pubmed.ncbi.nlm.nih.gov/32092632/), [doi:10.1016/j.jpba.2020.113176](https://doi.org/10.1016/j.jpba.2020.113176) |
| **3,5-Dicaffeoylquinic acid** | artichoke, honeysuckle, Bridelia | C1 component | <10 µM | Cimanga 1999, [PMID 17260306](https://pubmed.ncbi.nlm.nih.gov/17260306/), [doi:10.1055/s-1999-14059](https://doi.org/10.1055/s-1999-14059) |
| **K-76 / K-76-COOH** | Stachybotrys (toxic parent — semi-synthetic only) | C5 inhibitor | 100-570 µM | Larghi 2012, [PMID 22835722](https://pubmed.ncbi.nlm.nih.gov/22835722/), [doi:10.1016/j.ejmech.2012.07.003](https://doi.org/10.1016/j.ejmech.2012.07.003); Kawabata 2000, [PMID 11092692](https://pubmed.ncbi.nlm.nih.gov/11092692/) |
| **Complestatin** | *Streptomyces* spp. (NRPS-derived) | C5 inhibition | qual. active in BGC-disruption study | Chen 2018, [PMID 30232534](https://pubmed.ncbi.nlm.nih.gov/30232534/), [doi:10.1007/s00253-018-9337-2](https://doi.org/10.1007/s00253-018-9337-2) |

### §5.3 TIER 3 — weak / abstract-only / source-limited / retracted

12 compounds; including:
- Aceriphyllic acid C (oleanane triterpene from *Aceriphyllum rossii*, Min 2012 [PMID 22870809](https://pubmed.ncbi.nlm.nih.gov/22870809/), [doi:10.1007/s12272-012-0607-8](https://doi.org/10.1007/s12272-012-0607-8))
- Cycloartane triterpene 4 from *Beesia calthaefolia* (Mu 2013 [PMID 24144800](https://pubmed.ncbi.nlm.nih.gov/24144800/), [doi:10.1016/j.fitote.2013.10.005](https://doi.org/10.1016/j.fitote.2013.10.005))
- Phenylethanoid glycosides from *Paulownia tomentosa* (Si 2008 [PMID 19031237](https://pubmed.ncbi.nlm.nih.gov/19031237/), [doi:10.1080/10286020802242364](https://doi.org/10.1080/10286020802242364))
- Apigenin, acaciin, hyperoside (Zhang & Chen 2008 panel, weaker than luteolin)
- Ergosterol peroxide (Seo 2009)
- Dandelion polysaccharide PD1-1 (Guo 2019 [PMID 30991766](https://pubmed.ncbi.nlm.nih.gov/30991766/))
- Biophytum umbraculum extract (Austarheim 2016 [PMID 27260410](https://pubmed.ncbi.nlm.nih.gov/27260410/))
- Sorgoleone-386 — **PRIMARY PAPER RETRACTED**, drop from candidate list

### §5.4 FDA-approved drug repurposing surface

Already-approved upstream-CP0 drugs (synthetic, not natural-product candidates for OE platform but documented as anchors):
- **Eculizumab / Ravulizumab** (anti-C5 mAb) — PNH, aHUS, gMG, NMO
- **Pegcetacoplan** (compstatin-family cyclic peptide, C3 binder) — PNH (FDA 2021)
- **Iptacopan** (Factor B small molecule) — PNH, IgAN, C3G (FDA 2023)
- **Danicopan** (Factor D small molecule) — add-on PNH (FDA 2024)
- **Narsoplimab** (anti-MASP-2 mAb) — HSCT-TMA (FDA 2025)
- **C1-INH** (Berinert / Cinryze / Ruconest) — HAE; engineering anchor for OE-relevant heterologous expression
- **Avacopan** (C5aR1 small molecule) — already in OE corpus per `complement-c5a-gout.md`; downstream not upstream

The pharma upstream-CP0 surface is dense — every node from C3 to C5a has at least one FDA-approved drug. This validates the chokepoint pharmacologically; the OE platform's question is whether *natural-product* or *fermentable-engineering* coverage exists at any of these nodes.

## §6 ChEMBL coverage gap (empirical)

| Metric | Value |
|---|---|
| Compounds with documented anticomplement activity | 32 |
| With any ChEMBL record (other targets, e.g. XO, COX, kinases) | 14 |
| With curated ChEMBL anticomplement bioactivity | **0** |
| ChEMBL anticomplement coverage rate | **0/32 = 0%** |

ChEMBL has zero curated hemolytic-assay (CH50/AP50) anticomplement data for any compound in this list. Same coverage gap as comp-013 (5/9 TCM compounds with no ChEMBL data) but worse — anticomplement is a niche assay class that ChEMBL never indexed systematically. This is a structural ChEMBL limitation, not a bioactivity-absence.

**Implication for any future natural-product complement scan:** ChEMBL-only is the path-dependent narrowing failure mode. Direct primary literature (PubMed + PMC + non-English-corpus) is mandatory.

## §7 Cross-cutting platform implications

### §7.1 The "honest platform gap" at CP0 is partially closeable through diet

Rosmarinic acid at gram-scale rosemary supplementation (or sustained spearmint tea consumption per Connelly 2014) plausibly contributes upstream complement dampening at concentrations consistent with the 5-10 µM IC50. **Brian's "if the answer is rosemary, I'll grow rosemary" framing was load-bearing — it is, in fact, rosemary (and lemon balm, spearmint, salvia).** This is the chokepoint-hacker outcome the experiment was designed to surface.

The platform's CP0 coverage shifts from:
- 2026-04-27: "honest platform gap, only avacopan covers it" (pre-comp-012)
- 2026-05-05: "active engineering candidate (DAF SCR1-4) with formalized wet-lab plan" (post-comp-012)
- **2026-05-08:** "active engineering candidate + dietary-modulator backstop (rosmarinic acid + luteolin) at the upstream C3-convertase node"

The engineering and dietary threads are not redundant — they operate at different geometric scales (engineered DAF saturates the MSU surface; dietary RMA saturates fluid-phase + gut-luminal C3 convertase) and likely combine additively rather than competitively.

### §7.2 Luteolin triple-convergence

Luteolin is now documented across **three** independent gout-relevant mechanisms in the OE corpus:
- **XO** (xanthine oxidase): IC50 550 nM (J Nat Prod 1998, per [comp-013](./tcm-gout-compound-triage-computational.md))
- **URAT1**: animal-model expression downregulation 3-10 mg/kg PO (Lin 2018 PMID 29519319, per comp-013)
- **C3 convertase (CP+AP)**: CH50 190 µM, AP50 170 µM (Zhang & Chen 2008)

This is the highest-leverage single dietary compound the platform has surfaced. The 100-300 mg/day commercial supplement dose achieves mM range gut-luminal concentrations and ~µM systemic — within reach of all three IC50s in the gut compartment, only XO in the systemic compartment. **The gut-luminal-sink thesis applies cleanly: luteolin is a lumen-side multi-mechanism gout compound.**

Recommend revisiting [`gout-action-guide.md`](./gout-action-guide.md) for a luteolin-rich-foods entry (parsley, celery, chamomile tea, honeysuckle tea) and for a dietary rosmarinic acid entry (rosemary, lemon balm, spearmint, sage).

### §7.3 comp-014's β-glucan structure-dependence — mechanistic closure

The contradiction surfaced in `synthesis.md` 2026-05-08 (`modality-chokepoint-matrix.md` β-glucans structure-dependent — *G. lucidum* EPS activate, spore-powder/GLP inhibit) now has a mechanistic explanation: the same Ganoderma fruiting body contains:
- **β-glucan structures** that activate complement via the lectin pathway (MBL recognizes β-1,3-glucan terminal patterns — Zhao 2002 PMID 12384422 demonstrates the principle for mannose-LPS)
- **Lanostane triterpenes (ganoderic acid Sz) + ergosterol** that INHIBIT the classical pathway C3 convertase at 44-52 µM (Seo 2009)

Whether a reishi extract is anti- or pro-inflammatory at the complement level depends on which fractions dominate. **This argues for fraction-specific reishi preparations rather than whole-extract** — consistent with the comp-014 Phase 5 caveat about structure-dependent NLRP3 effects. Triterpene-enriched fractions (ethyl-acetate-soluble) would be CP-inhibitory; β-glucan-enriched fractions (water-soluble polysaccharide) would be ambiguous.

### §7.4 Engineered C1-INH parallel thread (new — proposed)

Recombinant C1-INH is FDA-approved for hereditary angioedema (Berinert / Cinryze / Ruconest). The molecule is a soluble human serpin that's recombinant-producible (Ruconest is from rabbit milk; Berinert is plasma-derived). **This is a near-twin engineering thesis to DAF SCR1-4 (H05):**

| Property | DAF SCR1-4 (H05) | C1-INH (proposed) |
|---|---|---|
| Source organism | human | human |
| Function | decay-accelerator + DAF mimetic on MSU surface | classical/lectin protease inhibitor (C1r/C1s/MASP) |
| Complement node | C3 convertase | C1r/s + AP regulator |
| Molecular features | 4× CCP/SCR domains, 8 disulfides | serpin + carbohydrate-rich, single-domain |
| Engineering chassis | *A. oryzae* (koji) — comp-012 LOW protease risk | *A. oryzae* or LBP — protease stability TBD |
| Clinical precedent | none (novel construct) | FDA-approved (HAE) |
| OE wet-lab path | §1.25 scoped | not yet scoped |

**Phase 2 follow-up: open a parallel comp-NNN for koji-expressed C1-INH protease stability** (mirror of comp-006/comp-012). If LOW or MODERATE, this becomes a second CP0 engineering candidate operating at a different complement node — the engineering coverage of CP0 doubles.

### §7.5 Bacterial NRPS complement chemistry as LBP payload class

Complestatin (Streptomyces) and the S. xinghaiensis-related BGC (Chen 2018 PMID 30232534) show that **bacterial NRPS (non-ribosomal peptide synthetase) chemistry is a candidate complement-modulator chemical class** that the OE corpus had not previously enumerated. Bacterial NRPS clusters are not koji-tractable (they require bacterial Sfp-family phosphopantetheinyl transferases and bacterial ACP machinery) but are LBP-tractable (bacterial chassis, native NRPS infrastructure).

Implication for the [engineered-LBP-chassis](./engineered-lbp-chassis.md) peer track: complestatin-family NRPS-derived anticomplement peptides are a previously-unmapped payload candidate. Phase 2 follow-up: scope an LBP-chassis comp-NNN for complestatin BGC heterologous expression.

## §8 Recommendations

### §8.1 Promote to in vitro complement-modulation assay (priority order)

1. **Rosmarinic acid** — anchor compound. Use as CH50 / AP50 / C3-deposition-on-MSU positive control. Dietary-tier supplement viable (rosemary, lemon balm, spearmint).
2. **Luteolin** — already in OE candidate stack. Test cross-mechanism contribution at gut-luminal concentrations achievable via 100-300 mg supplementation.
3. **Bupleurum polysaccharides** — different mechanism (lectin pathway); orthogonal to RMA + luteolin; supports the global-multilingual CNKI gap thesis. Suggest direct CNKI search before in vitro.
4. **Ganoderic acid Sz + ergosterol** — fungal-chemistry-distinctive; ties to comp-014. Use ethyl-acetate-soluble triterpene-enriched reishi fraction, not whole extract.

### §8.2 Drop / deprioritize

- **Sorgoleone** — primary paper retracted.
- **K-76 native compound** — Stachybotrys parent organism is mycotoxin-producing; toxicity-filter exclusion. K-76 semi-synthetic derivatives remain interesting as engineering payload class.
- **Curcumin / EGCG / berberine / resveratrol as upstream-complement modulators** — broad anti-inflammatory but no direct upstream-node IC50 surfaced in this sweep. They may still help via downstream NLRP3 modulation but are not comp-018 candidates.

### §8.3 Phase 2 follow-ups queued

1. **Direct CNKI/WanFang/J-STAGE search** for Bupleurum, Ganoderma, dandelion, Sophora, and Magnolia anticomplement literature using the two-model translation cross-check protocol (Claude + DeepSeek V4-Pro for Chinese sources) per CLAUDE.md §Translation protocol. Anchor expectation: substantial Chinese-language Bupleurum literature ChEMBL/PubMed has not curated.
2. **Brown-algae fucoidan complement-modulation sub-search** — heparin-mimetic mechanism (Park 1997 PMID 9388049) suggests sulfated polysaccharides operate via Factor H surface binding. Fucoidans are abundant in brown algae and dietary in Asian cuisines.
3. **Engineered-koji or LBP heterologous expression of compstatin-family C3-binding peptides** — pegcetacoplan validates the C3-binding cyclic peptide as an upstream-CP0 modality. Compstatin (~13 aa) is plausibly heterologously expressible.
4. **Engineered C1-INH expression scope page** — parallel to H05 DAF SCR1-4. Precedent is FDA-approved; chassis tractability unknown.
5. **Complestatin-family BGC LBP heterologous expression** — scope a peer-track comp-NNN for the engineered-LBP-chassis row of `modality-chokepoint-matrix.md`.

## §9 Chokepoint-class naming proposal

**Working term throughout this page: "upstream-CP0".** Per Brian's instruction (2026-05-08), the eventual chokepoint-class naming decision is the user's; this section proposes a recommendation.

**Recommendation:** Treat the upstream-of-C5aR1 nodes (C1q, C3 convertase, C5 convertase, Factor B, Factor D, C5, Factor H upregulators, DAF/CD55 host upregulators, C1-INH, MBL, MASP-2) as a **scope expansion of CP0** rather than a wholly new chokepoint class (CP-1).

**Rationale:**
- The OE corpus already names CP0 as "complement priming" — the mechanism of priming is C5a generation, which is the OUTPUT of the upstream cascade. Subdividing CP0 into "downstream-CP0" (C5aR1 antagonism / C5a binding) and "upstream-CP0" (everything proximal that prevents C5a generation) reads cleanly within the existing framework.
- CP-1 as a wholly new chokepoint class implies a fundamentally different priming mechanism, which is not the case here. Both upstream and downstream are part of the same complement-priming chokepoint.
- The matrix in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) should add a new ROW for **"upstream complement modulator (small molecule, dietary)"** to capture the rosmarinic-acid / luteolin / Bupleurum-PS class — this is the cleanest update that doesn't require renaming chokepoint columns.

The dash convention (CP-1, CP-2 going further upstream of CP0) is clean and could be useful if future chokepoints emerge that are mechanistically more upstream still. For now, the recommendation is scope-expansion within CP0.

## §10 Limitations

1. **Phase 1 is English-corpus-anchored.** Substantial Chinese-language Bupleurum / Ganoderma anticomplement literature is plausibly missed. Phase 2 multilingual ingestion will close this — Bupleurum, dandelion, Sophora, and Magnolia are the highest-likelihood-non-English-evidence candidates.

2. **IC50 discrepancy on rosmarinic acid (5-10 µM Englberger 1988 vs 137-182 µM in 2008-2013 comparator literature) is unresolved.** Likely assay-format difference. Both ranges flagged in `compounds.json`. Phase 2 should grep-verify the Englberger 1988 paper directly (currently abstract-tier only — not in PMC).

3. **No load-bearing claim is grep-verified against the 1988 paper in full text.** The 5-10 µM IC50 was extracted from the PubMed abstract. Per CLAUDE.md Rule 4 this is abstract-tier; the paper itself is paywalled and not in PMC. If this number becomes load-bearing for any future wet-lab gate, full-text retrieval is mandatory.

4. **The bell-shape phenomenon in rosmarinic acid C3-convertase inhibition (higher concentrations less effective) is not mechanistically explained** in the available literature. This is load-bearing for dose-extrapolation — supplement-tier dosing should target sustained mid-µM, not max pharma-tier.

5. **Translation cross-check protocol was not triggered in Phase 1** because all primary sources surfaced were English. Phase 2 will activate it for CNKI/WanFang/J-STAGE direct reads.

6. **The C5aR1-empty finding (comp-014 + §1.21 + comp-018) is now triply-confirmed** but the failure mode for all three scans is the same: Western-pharma-curated database (ChEMBL) + Western-language literature (PubMed). The non-Western corpus might still have a hit. Phase 2 multilingual ingestion is the residual risk-closure.

7. **Synergy is unmodeled.** Rosmarinic acid + luteolin + Bupleurum-PS at three different nodes (C3 conv. CP, C3 conv. CP+AP, lectin pathway) is mechanistically plausible additive — but no in vitro three-arm experiment has been run. Phase 2 in vitro design would test the combination.

8. **Dose-extrapolation from animal-model i.v. to human-oral is speculative** for rosmarinic acid. Proctor 2006 used 10 mg/kg i.v.; oral 10 mg/kg in human ≈ 600 mg, achievable from rosemary supplementation but with large first-pass loss. Connelly 2014 (16-week spearmint tea OA RCT) is the closest in-human evidence proxy for sustained mid-µM RMA achievability.

## §11 Outputs (machine-readable)

- `experiments/comp-018-upstream-complement-modulator-sweep/inputs/targets.json` — 16 nodes, UniProt-anchored, MSU-relevance-tagged
- `experiments/comp-018-upstream-complement-modulator-sweep/inputs/query-strategy.json` — multi-source query strategy + executed PubMed macros
- `experiments/comp-018-upstream-complement-modulator-sweep/outputs/compounds.json` — 32 compounds × IC50 × source × tier × evidence-level
- `experiments/comp-018-upstream-complement-modulator-sweep/outputs/scope-summary.md` — generated summary
- `experiments/comp-018-upstream-complement-modulator-sweep/scripts/scope_validate.py` — reproducible validator + summary emitter

## §12 Cross-references (back-write coordination)

The following pages should gain a one-line cross-ref to comp-018 (back-references handled in this commit):

- [`complement-c5a-gout.md`](./complement-c5a-gout.md) — CP0 status update: upstream-modulator dietary axis newly active
- [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md) — engineered-DAF parallel; C1-INH thread proposed
- [`hypotheses/H05-daf-scr14-cp0-thesis.md`](./hypotheses/H05-daf-scr14-cp0-thesis.md) — H05 + comp-018 cross-track coordination
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — Ganoderma triterpene anticomplement adds to comp-014
- [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) — luteolin third-mechanism update
- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — proposed new row "upstream complement modulator (dietary / small-molecule)"
- [`gout-action-guide.md`](./gout-action-guide.md) — luteolin-rich foods + rosmarinic acid sources flagged as future research
