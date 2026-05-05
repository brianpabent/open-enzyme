---
title: "Ward 1995 §1.9 Wet-Lab Access — Global Landscape (Japan / China / Europe)"
date: 2026-05-05
tags:
  - validation-experiments
  - lab-access
  - aspergillus-oryzae
  - dual-cassette
  - NSlD-deltaP10
  - strain-repository
  - international-collaboration
  - scope-page
related:
  - validation-experiments.md
  - team.md
  - hypotheses/H01-ward-dual-cassette.md
  - cassette-compatibility-computational.md
  - koji-endgame-strain.md
  - engineered-koji-protocol.md
  - aspergillus-oryzae.md
sources:
  - "Huynh et al. 2020, *Fungal Biology and Biotechnology* — PMC7257131 (NSlD-ΔP10 origin paper, Maruyama lab, University of Tokyo)"
  - "Yoon, Maruyama, Kitamoto 2011, *Appl Microbiol Biotechnol* — PMID 20957357 (NSlD-ΔP10 strain creation paper)"
  - "Bi, Huang, Pan, Wang, Pan 2025, *Synth Syst Biotechnol* — PMC12513303 (zhongshengmycin transformation, South China Univ of Tech)"
  - "Li, Zhang, Li, Du, Li, Zhou, Zhang 2024, *Synth Syst Biotechnol* — PMC11742560 (A. oryzae C19 mutant lipase platform, Jiangnan University)"
  - "Sheng, Qiu, Deng, Zeng 2025, *J. Fungi* — PMC12299000 (Aspergillus heterologous expression review)"
  - "Wang, Zhong, Xiao 2020, *Microbial Cell Factories* — PMC7156587 (filamentous fungi protein engineering review)"
  - "JCM (Japan Collection of Microorganisms, RIKEN BRC) catalog — https://jcm.brc.riken.jp/en/"
  - "CGMCC (China General Microbiological Culture Collection Center) — Budapest Treaty IDA, https://www.cgmcc.net/english/"
  - "FGSC (Fungal Genetics Stock Center) — https://www.fgsc.net/"
  - "Maruyama lab (University of Tokyo, Department of Biotechnology) — http://park.itc.u-tokyo.ac.jp/Brew-Microbio/"
  - "Wösten lab (Utrecht University, Microbiology) — long-running A. oryzae / A. niger work"
  - "Mortensen group (DTU, Eukaryotic Biotechnology) — CRISPR-Cas9 and Mad7 toolkits for filamentous fungi"
status: scope-page
---

# Ward 1995 §1.9 Wet-Lab Access — Global Landscape (Japan / China / Europe)

**Status:** scope-page (2026-05-05). Maps the global parallel options for executing [validation-experiments.md §1.9](./validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate--1-priority-gate) — the project's #1 priority gate. Companion to the US-only scope (covered separately in the Lauren Collier-Hyams contact thread; see [team.md](./team.md)). This page exists so that if the US lead doesn't move forward, or if an alternative path is cheaper / faster / better-positioned, Brian has a pre-mapped order-of-operations to fall back on.

---

## Why this page exists

§1.9 is the single experiment that decides whether the [koji-endgame-strain](./koji-endgame-strain.md) thesis stands as a one-strain construct or collapses to a two-strain co-fermentation fallback. It needs:

- *A. oryzae* genetic-engineering capability (PEG/CaCl₂ protoplast transformation; Agrobacterium also acceptable)
- Solid-state rice koji fermentation infrastructure (plus parallel submerged-culture controls)
- A protease-deletion chassis — H01 Killshot #1 made the **NSlD-ΔP10** ten-protease-knockout strain the default, not a fallback (Huynh 2020 PMC7257131; Yoon 2011 PMID 20957357)
- pyrG / niaD / amdS / ptrA selection markers — the food-grade-compatible set
- qPCR (cassette copy number), ELISA + Western (heterologous protein quantification), spectrophotometric uricase activity assay, HPLC for kojic acid baseline

Lauren Collier-Hyams at Emory was emailed today and replied "ok lemme try to dig into this and i'll get back to ya" — engaged, no timeline. This page de-risks her timeline by mapping global parallel options; if she comes back without direct execution capacity, several leads here can carry the experiment.

US-based options were scoped separately and are intentionally out of scope here.

---

## A. Japan — natural geographic + cultural fit

Industrial koji is a $10B+ Japanese market, and almost all of the foundational *A. oryzae* engineering literature originated in Japanese academic groups. The strain Brian wants (NSlD-ΔP10) is from one specific Tokyo lab.

### Maruyama / Kitamoto group — University of Tokyo (NSlD-ΔP10 origin)

**The single most important contact globally.** Jun-ichi Maruyama is Professor at the University of Tokyo, Department of Biotechnology (Graduate School of Agricultural and Life Sciences). His group is the **origin lab for the NSlD-ΔP10 ten-protease-deletion strain** (Yoon, Maruyama, Kitamoto 2011, PMID 20957357), and is the corresponding author group on Huynh et al. 2020 (PMC7257131) — the paper Killshot #1 used to validate the dual-cassette architecture.

- **Verified contact:** amarujun@mail.ecc.u-tokyo.ac.jp; Department of Biotechnology, The University of Tokyo, 1-1-1 Yayoi, Bunkyo-ku, Tokyo 113-8657
- **Lab homepage:** http://park.itc.u-tokyo.ac.jp/Brew-Microbio/
- **Realistic engagement model:** academic collaboration with MTA for the NSlD-ΔP10 strain. The group has published collaborations with researchers outside Japan (Vietnam — Huynh first-author on PMC7257131; with AIST Tsukuba and AMED). A targeted "we've cited your strain in our pre-experimental design rationale, we're a small open-source therapeutic-enzyme research project, can we obtain NSlD-ΔP10 under MTA?" inquiry has a reasonable hit rate.
- **What's unverified:** MTA fee (likely modest, possibly free for academic use), turnaround time (Japanese academic MTAs typically 4–12 weeks once requested), whether they'd consider doing the dual-cassette transformation in-house as a fee-for-service or co-author collaboration. Direct outreach required.

### Other University of Tokyo *A. oryzae* groups

- **Tanokura group** (Department of Applied Biological Chemistry — co-author on Huynh 2020): structural biology, antibody glycoengineering. Less likely to do the transformation itself, but could be a collaboration entry point if Maruyama's lab is overcommitted.
- **Mizuki Tanaka group** (corresponding author on bio_09f1a2aa7b1a, peptidase regulation in *A. oryzae*, April 2025) — active publication record on *A. oryzae* protease genetics, which is directly relevant to the cassette + protease-deletion intersection. Publication status verifies an active program; affiliation needs confirmation (the bioRxiv preprint covers Yamagata + Kawarasaki — verify via direct outreach).

### National Research Institute of Brewing (NRIB) — Higashihiroshima, Japan

Japan's national institute for brewing science. Long-standing *A. oryzae* genome and EST work (collaborated on the original RIB40 genome sequencing — Machida et al. 2005, *Nature* 04300). Public-sector research institute — mandate is industry-supporting science; engagement model is closer to standards-body / consortium membership than bilateral academic collaboration. **Most plausible role for Open Enzyme: strain authentication and metabolite-baseline reference data**, not direct dual-cassette transformation work. Verification of current *A. oryzae* engineering programs requires direct outreach (no obvious external partnership program on the public site).

### Other Japanese academic groups (Tohoku, Tokyo Univ Sci & Tech, Akita)

- **Tohoku University Graduate School of Agricultural Science** (Faculty of Agriculture, Sendai) — historical *A. oryzae* engineering presence (Osamu Akita and others; AtfB transcription factor work). Active program status as of 2025 needs direct verification.
- **Akita Prefectural University, Tokyo University of Science and Technology** — appear in some recent *A. oryzae* literature but neither shows the focused multi-cassette / protease-deletion engineering depth of the Maruyama group. Lower-priority outreach targets.

### Industrial Japanese groups (Kikkoman, Marukome, Asahi Kasei, Hakkaisan)

These are the largest commercial users of engineered or selected *A. oryzae* strains in Japan. Their R&D arms have decades of unpublished know-how. **Engagement model is structurally incompatible with a small open-source academic-style request:** they protect strain IP, would require NDA structures Open Enzyme cannot reasonably enter, and have no public open-collaboration program. **Map but don't pursue.** If a partnership becomes valuable later (e.g., Open Enzyme has reached commercial-strain validation and is licensing, not requesting), revisit.

### Japanese culture collections — strain repository deep-dive

- **JCM (Japan Collection of Microorganisms, RIKEN BRC)** — the natural strain repository for Japanese-derived *A. oryzae*. Catalog is searchable at https://jcm.brc.riken.jp/en/. Distribution fees updated April 2026 (specific pricing not visible without direct catalog query). Contact: inquiry.jcm@riken.jp. **NSlD-ΔP10 is not a routinely listed JCM strain** — it's a research-lab construct held by Maruyama's group at Tokyo. RIB40 (the genome reference strain) is widely distributed including via JCM, ATCC, and NBRC. Data on NSAR1 5-marker auxotroph (Oikawa 2020 PMC7725655) availability via JCM unverified — direct catalog query required.
- **NBRC (NITE Biological Resource Center)** — Japanese national strain repository. Holds RIB40 and many wild-type *A. oryzae* strains. NSlD-ΔP10 deposit status unverified; NBRC site fetch failed during this scope (TLS cert issue), needs direct browser query.
- **NRRL / IFO** — older Japanese-affiliated culture collections; mostly subsumed into NBRC. Not a separate path.

**Bottom line on Japan strain side:** **NSlD-ΔP10 appears to live only at the Maruyama lab** (Tokyo). The path to obtaining it is: direct email to Maruyama → MTA → strain shipment. There is no public-repository fallback for NSlD-ΔP10 specifically. Acceptable substitutes: the NSAR1 5-marker auxotroph (Oikawa 2020) plus *de novo* construction of protease deletions — substantially more wet-lab work, not a free swap.

---

## B. China — most-active fungal-engineering output globally by paper count

China leads global publication volume in *Aspergillus* engineering since ~2020. Multiple groups have CRISPR-Cas9 toolkits, multi-locus integration platforms, and industrial-strain engineering programs running in parallel.

### Jingwen Zhou / Guoqiang Zhang group — Jiangnan University (Wuxi)

**Most-direct dual-cassette-relevant Chinese lead.** The group at the Science Center for Future Foods + Key Laboratory of Industrial Biotechnology of Ministry of Education, Jiangnan University, published the C19 *A. oryzae* mutant strain platform with multi-locus integration into α-amylase loci (Li et al. 2024, PMC11742560 / PMID 39830075) — a 3.3× boost in heterologous lipase activity from 3-amylase-site integration. **This is functionally adjacent to what §1.9 needs** (multi-cassette integration into a *A. oryzae* chassis at validated high-expression loci). The group runs 5-L bioreactor capacity in addition to shake-flask scale.

- **Affiliation:** Jiangnan University, Wuxi 214122, Jiangsu, China
- **Realistic engagement model:** academic collaboration. Jiangnan has a strong international-collaboration culture in food science / fermentation. The group's engineering toolkit and the NSlD-ΔP10 chassis are not obviously compatible (their C19 strain is independently derived), so a Jiangnan path likely means using their **C19** chassis instead of NSlD-ΔP10 — which is a meaningful design change that needs cross-checking against Killshot #1 / comp-010 assumptions before committing. The C19 strain has not been characterized for the protease-deletion profile that Huynh 2020 found necessary for antibody-grade titers.
- **What's unverified:** Specific PI contact emails (would come from the publication corresponding-author info); MTA terms for the C19 strain; cost / timeline for fee-for-service work if offered. Direct outreach required.

### Bin Wang / Li Pan group — South China University of Technology (Guangzhou)

Recent (Aug 2025) publication on a novel zhongshengmycin / NAT-based transformation system for both *A. oryzae* and *A. niger* (Bi et al. 2025, PMC12513303). 85.7% selection efficiency, attB/attP-mediated integration. This is a brand-new tool that could simplify the §1.9 transformation workflow — particularly if pyrG-based selection is constrained.

- **Affiliation:** School of Biology and Biological Engineering + Guangdong Provincial Key Laboratory of Fermentation and Enzyme Engineering, South China University of Technology, Guangzhou
- **Realistic engagement model:** academic collaboration; tool licensing or co-development. The zhongshengmycin transformation system is recent enough that the group is likely to be receptive to early adopters — there's a built-in incentive for them to see the tool used in a multi-cassette context. Engagement likelihood: moderate-to-high.

### Tianjin Institute of Industrial Biotechnology (TIB), Chinese Academy of Sciences

Hosts the State Key Laboratory of Engineering Biology for Low-Carbon Manufacturing. Published recently on the **AnN2** *A. niger* chassis (Gou et al. 2025, PMC12236015) — 13/20 glucoamylase copies deleted + PepA disruption + multi-copy modular integration. This is the *A. niger* sibling of the §1.9 strategy; the group has the engineering infrastructure but their published work is *A. niger*-focused, not *A. oryzae*. Realistic engagement model: collaboration on *A. oryzae* extension if they have parallel strains; direct outreach to verify.

### Wang Shihua group — Fujian Agriculture and Forestry University (Fuzhou)

Important correction to the original task scope: **Wang Shihua is at Fujian Agriculture and Forestry, not Jiangnan.** His Key Laboratory of Pathogenic Fungi and Mycotoxins works on *Aspergillus flavus* / aflatoxin biology — directly adjacent to *A. oryzae* (sister species) but with a mycotoxin / pathogenesis emphasis rather than heterologous protein production. Lower-priority outreach for §1.9 specifically; would be a strong contact for an aflatoxin-clearance safety review of any engineered *A. oryzae* strain.

### Chinese culture collections — CGMCC

**CGMCC (China General Microbiological Culture Collection Center)**, Institute of Microbiology, Chinese Academy of Sciences, Beijing. **Recognized as a Budapest Treaty International Depositary Authority** (alongside ATCC, JCM, DSMZ). Holds multiple *A. oryzae* strains under accession numbers like CGMCC 3.407, CGMCC 11645 (soy sauce isolate). MTA process: register as CGMCC user → sign MTA → cannot transfer to third parties without permission. Email: cgmcc@im.ac.cn. **Holds Chinese-derived industrial *A. oryzae* lineages but does not appear to hold NSlD-ΔP10.** Useful as a source of alternative protease-attenuated industrial strains (e.g., the soy-sauce-domesticated 3.042 lineage) and as a Budapest Treaty deposit destination if Open Enzyme ever needs to deposit a strain itself.

### Commercial Chinese CROs

WuXi AppTec, Pharmaron, and others are dominantly mammalian / yeast / *E. coli* CROs. **Filamentous-fungus capacity at major Chinese CROs is substantially smaller than their bacterial / yeast / mammalian capacity** and direct-outreach pricing for an *A. oryzae* dual-cassette transformation project is not publicly listed. The most promising commercial CRO path is likely a smaller specialized fermentation-services company near the Jiangnan / Wuxi cluster — **data unavailable; would require direct outreach to confirm.**

### Realistic engagement note (China)

Foreign-PI collaboration with Chinese academic labs on biotech generally works fine — the projects move through MOFCOM (Ministry of Commerce) approval for international agreements but this is procedural, not prohibitive. Strain export from China (CGMCC outbound) may have additional review depending on strain type, but for non-pathogenic GRAS *A. oryzae* should be straightforward.

---

## C. Europe — strong industrial fungal engineering tradition

European fungal engineering is concentrated in Netherlands (Wageningen / Utrecht / Delft), Denmark (DTU + the Novonesis ecosystem), and to a lesser extent France (INRAE) and Germany (Fraunhofer).

### Han Wösten group — Utrecht University (and historical Wageningen ties)

Wösten is at the Microbiology department, Utrecht University. Long publication record on *A. oryzae* and *A. niger* cell-factory work, including hyphal subpopulation / colony heterogeneity (PMC6972715, with Bleichrodt and Ram 2019), micro-colony secreted-protein expression (PMC6992626, 2020), and a 2025 paper on Trichoderma-medium-based *A. niger* protoplasting (PubMed 40935084). **Ongoing active program.** Westerdijk Fungal Biodiversity Institute (Utrecht) connection adds culture-collection access.

- **Realistic engagement model:** academic collaboration, possibly via a graduate student / postdoc rotation framing if Open Enzyme can offer a clear scientific question and modest funding. The group's emphasis on hyphal-population heterogeneity is directly relevant to single-strain dual-cassette stability — a natural collaboration framing.

### Uffe Mortensen group — Technical University of Denmark (DTU)

Eukaryotic Molecular Cell Biology Section, DTU. Authored two foundational toolkits used widely in *Aspergillus* engineering: the original CRISPR-Cas9 system for filamentous fungi (Nødvig et al. 2015, PMC4503723, PLOS One — 1000+ citations) and a more recent Mad7-based system applied to *A. oryzae*. Single-stranded-oligo CRISPR repair templates demonstrated in *A. oryzae*. **The technical depth here is the strongest in Europe for the precise CRISPR / multi-cassette work §1.9 needs.**

- **Realistic engagement model:** academic collaboration; potentially a fee-supported visiting-researcher arrangement. DTU's Novozymes (now Novonesis) alumni network means strain expertise is dense in Copenhagen.

### CBS-KNAW Westerdijk Fungal Biodiversity Institute — Utrecht

Major European fungal culture collection plus active research institute. Strong genomics + comparative-genomics depth on *Aspergillus*. Catalog likely holds wild-type *A. oryzae* RIB40 and related strains; **NSlD-ΔP10 deposit status unverified — direct catalog query needed.** Useful as a fallback strain source and for any strain-authentication or genome-resequencing work.

### INRAE (France) — Jouy-en-Josas / Marseille

INRAE has multiple *Aspergillus* genetics programs distributed across Jouy-en-Josas (food microbiology) and Marseille (BBF / fungal biotechnology). Specific PI mapping for active *A. oryzae* dual-cassette work was not deeply verified during this scope — direct outreach to the INRAE BBF group at Marseille would be the right entry point.

### Novonesis (formerly Novozymes) — Denmark

**Important update:** Novozymes merged with Chr. Hansen in early 2024 to form **Novonesis**. The DSM-Firmenich / Novozymes Feed Enzyme Alliance was dissolved in 2025 (Novonesis bought DSM-Firmenich's stake for €1.5B, completed June 2025). Novonesis is the world-leading industrial enzyme company; their *A. oryzae* and *A. niger* engineering know-how is enormous and protected. **Engagement model is structurally incompatible with a small open-source academic-style request.** Novonesis alumni now consulting independently or at DTU is the realistic path to indirect access.

### DSM-Firmenich (Netherlands / Switzerland)

Merged DSM + Firmenich (2023). Industrial fungal engineering at scale. Has historically run open / pre-competitive innovation partnership programs (specific 2026 program status not deeply verified during this scope). **Realistic engagement model: open-innovation challenge framework** if and when they post one matching enzyme-platform topics. Direct cold outreach for a small academic project is unlikely to yield engagement.

### Fraunhofer IGB (Germany)

Applied biotech with some filamentous-fungi capability. Engagement model: structured contract research; pricing for an *A. oryzae* transformation project is not publicly listed. **Data unavailable — direct outreach required.** Would be a viable commercial-CRO path if Open Enzyme is willing to fund at the EU institutional rate.

---

## D. Strain repository deep-dive — the NSlD-ΔP10 question

This is the single highest-leverage strain-side consideration. Synthesis of the search:

| Repository | Country | RIB40 (WT ref) | NSAR1 (5-marker) | NSlD-ΔP10 (10-protease del) |
|---|---|---|---|---|
| **JCM (RIKEN BRC)** | Japan | Likely available; verify catalog | Unverified | **Not deposited (unverified — most likely no)** |
| **NBRC (NITE)** | Japan | Available | Unverified | Unverified — site fetch failed |
| **CGMCC** | China | Available (3.407, 3.042 lineage) | Unverified | Likely no |
| **CBS-KNAW (Westerdijk)** | Netherlands | Likely | Unverified | Likely no |
| **ATCC** | USA | Available | Unverified | Likely no |
| **FGSC** | USA | Catalog-listed for *A. oryzae* | Unverified | Likely no |

**Bottom line:** NSlD-ΔP10 is not in any public repository this scope could verify. **The Maruyama lab at the University of Tokyo is the only source.** This makes the Tokyo email lead structurally non-substitutable for the strain side.

**Acceptable substitutes (more wet-lab work, but plausible):**

1. **NSAR1 5-marker auxotroph (Oikawa 2020, PMC7725655)** — the platform comp-010 already analyzed for marker-slot capacity. Doesn't have the 10-protease background but provides 5 simultaneous integration slots. Lactoferrin titer would likely fall short of Huynh 2020's 39.7 mg/L benchmark (not the right benchmark anyway — Ward 1995 at >2 g/L is) but uricase is much less protease-sensitive and should work.
2. **AUT1-lD-v10-sD strain** (Huynh 2020 Table 1) — intermediate hyper-producer mutant with double deletion of *AosedD* + *Aovps10* + tppA + pepE. Published precedent for high heterologous expression. Same Maruyama lab.
3. ***De novo* protease-knockout in NSAR1 background** — substantial wet-lab work (~12+ months for ten knockouts), but doable using the same CRISPR-Cas9 toolkit Maruyama and DTU groups have published. This is the "plan C" if the Maruyama lab path closes entirely.
4. **C19 from Jiangnan** — published high-expression mutant; protease profile not characterized; would need separate validation work but the multi-locus integration toolkit is published and strong.

---

## E. Brian-specific recommendation

### The 2–3 GLOBAL paths most likely to execute §1.9 within 6 months at <$10K (cheap CRO option, if it exists) or <$30K (academic collaboration realistic)

1. **Maruyama lab, University of Tokyo — academic collaboration** *(highest priority, single most-actionable lead)*. The strain origin lab; the only verified source of NSlD-ΔP10; published collaborator with foreign groups; corresponding author on the exact paper Killshot #1 cited. Cost likely modest ($5–15K range for materials + MTA + Brian-side gene synthesis), timeline 3–9 months from first email. Specific person: **Jun-ichi Maruyama, amarujun@mail.ecc.u-tokyo.ac.jp.**

2. **Jingwen Zhou / Guoqiang Zhang group, Jiangnan University — academic collaboration with C19 chassis** *(parallel-path option if Tokyo doesn't engage)*. Functionally adjacent (multi-locus α-amylase integration), strong fermentation infrastructure, paper already cited in [koji-endgame-strain.md](./koji-endgame-strain.md). Engagement requires accepting that the chassis becomes C19 instead of NSlD-ΔP10 — design swap, not equivalent. Specific contact: corresponding author from PMC11742560 (verify via paper; likely Guoqiang Zhang or Jingwen Zhou). Cost similar range; timeline likely 4–9 months given international-collaboration paperwork.

3. **Mortensen group, DTU — academic collaboration on the toolkit + co-development** *(parallel-path Europe option)*. Strongest CRISPR-Cas9 / Mad7 toolkit in Europe; Novonesis-alumni density in Copenhagen; would be a natural collaboration if Open Enzyme can frame the §1.9 work as a published toolkit-validation case study. Cost 10–30K range; timeline 6–12 months. Less direct strain access than Tokyo, more methodological depth than Jiangnan.

### Single most-actionable lead — what to send tomorrow

**Email Jun-ichi Maruyama tomorrow morning.** Draft skeleton:

> Dear Prof. Maruyama,
>
> I'm Brian Abent, the founder of Open Enzyme — an open-source research project building food-grade engineered koji strains expressing therapeutic enzymes (uricase for gout, digestive enzymes for EPI). Our project files are public at [GitHub link].
>
> I'm writing because your 2020 *Fungal Biology and Biotechnology* paper (Huynh et al., PMC7257131) is the foundational reference for our #1 priority experiment: a dual-cassette feasibility test layering *A. flavus* uricase on the Ward 1995 lactoferrin architecture in an *A. oryzae* chassis. Our just-completed in silico cassette-compatibility analysis (1.06× the disulfide load of your adalimumab work; no blocking issues) and the Killshot #1 falsification check both depend critically on the **NSlD-ΔP10** strain you constructed (Yoon, Maruyama, Kitamoto 2011).
>
> Two specific asks:
>
> 1. Would your group be willing to provide NSlD-ΔP10 under an MTA for our research use?
> 2. More ambitiously: would you have interest in a small collaboration (or fee-for-service arrangement) where your group performs the dual-cassette transformation? We have full cassette designs ready and ~$10K in seed funding allocated to this experiment specifically.
>
> Brief project context: [link to wiki/koji-endgame-strain.md and wiki/validation-experiments.md §1.9]. Falsification card: [link to wiki/hypotheses/H01-ward-dual-cassette.md].
>
> Happy to send fuller technical detail. Thank you for considering.
>
> Brian Abent
> brian@headsupresults.com
> Open Enzyme

### If Lauren falls through — order-of-operations parallel pursuit

1. **Week 0:** Email Maruyama (above).
2. **Week 0 (parallel):** Email Jingwen Zhou + Guoqiang Zhang (Jiangnan, corresponding authors of PMC11742560) with a similar but C19-chassis-framed request.
3. **Week 2:** If neither responds, email Mortensen at DTU with a CRISPR-toolkit framing.
4. **Week 4:** If still no engagement, query JCM (inquiry.jcm@riken.jp) and CGMCC (cgmcc@im.ac.cn) for the closest-available substitute strains (NSAR1 + protease-attenuated lineages).
5. **Week 6:** If all academic paths are stalled, reframe as a paid CRO request — first to Fraunhofer IGB (Germany), then to specialized fermentation-services companies in the Wuxi cluster (would require local-language outreach).

---

## Limitations of this page

- **No PI emails verified beyond Maruyama.** The Jiangnan, DTU, and Wösten leads were verified by published affiliation only. Specific corresponding-author emails should be pulled from each paper's correspondence section before outreach.
- **No CRO pricing verified.** Filamentous-fungus engineering CROs do not publish pricing. The cost ranges above are estimates based on academic-collaboration norms, not CRO quotes. Direct RFQs would refine.
- **Strain availability data is inferential outside Maruyama lab.** JCM, NBRC, CGMCC, CBS-KNAW, and ATCC catalog entries for specific NSlD / NSAR1 / protease-deletion strains were not exhaustively queried in this scope. Direct catalog queries (or a single batch email per repository asking "do you hold the following accessions?") would close this.
- **No Japanese / Chinese language search.** All searches in this scope were English-language. Some Japanese industrial-koji R&D groups and Chinese academic groups have substantially more depth in their native-language publications and websites than English summaries reflect. A bilingual collaborator (or a follow-up sweep with Japanese / Chinese language search) would surface leads this scope missed.
- **Industrial partners (Novonesis, DSM-Firmenich, Kikkoman, etc.) are mapped but flagged as structurally incompatible with current Open Enzyme posture.** This may change once Open Enzyme has commercial-strain validation in hand and is licensing or partnering rather than requesting.
- **The US scope (covered separately) intentionally excluded.** This page is the global parallel set, not the full landscape.

---

## Cross-References

- [`validation-experiments.md`](./validation-experiments.md) §1.9 — the experiment this page is about
- [`team.md`](./team.md) — Brian + named collaborator (Lauren Collier-Hyams, Emory) plus the addendum pointing here
- [`hypotheses/H01-ward-dual-cassette.md`](./hypotheses/H01-ward-dual-cassette.md) — the falsification card; Killshot #1 surfaced NSlD-ΔP10 as the default chassis
- [`cassette-compatibility-computational.md`](./cassette-compatibility-computational.md) — comp-010, the in silico cassette-design analysis (LOW risk verdict)
- [`koji-endgame-strain.md`](./koji-endgame-strain.md) — the endgame strain thesis §1.9 gates
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) — the construct-design and assay protocol stack
- [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) — chassis-level reference page
