# P0-1 CNKI Two-Model Source Read

Date: 2026-05-20

Scope: conservative source-read pass over the nine highest-priority P0-1 medicinal-mushroom / hyperuricemia CNKI lead records recovered after the CNKI Overseas route correction.

Protocol: Codex/GPT-5.5 performed the primary synthesis in-session from CNKI Overseas article abstract pages. DeepSeek (`deepseek/deepseek-chat-v3` via OpenRouter) performed the native-Chinese counter-read from the same abstract records. OpenRouter usage for the DeepSeek pass was 5,481 tokens / $0.00276738.

Important limitation: CNKI full-text HTML/PDF/CAJ order endpoints redirected local curl to CNKI Overseas login pages. This pass therefore ingests CNKI article metadata and abstracts only. Do not promote wiki evidence tiers from this artifact as if full text had been read.

Source artifacts:

- `p0-1-cnki-lead-abstract-records-2026-05-20.json` - parsed title, abstract, and keyword records.
- `p0-1-cnki-deepseek-counterread-2026-05-20.json` - native-Chinese counter-read.
- `fulltext-probes/fulltext-fetch-index.json` - full-text endpoint probes showing login redirects.

## CNKI Retrieval Links

Use these CNKI Overseas article pages as the starting point for browser/manual full-text retrieval. On the article page, try the `HTML Reading`, `Original Reading`, `PDF`, or `CAJ` actions while logged in through whatever CNKI access route works locally.

Alternative routes should be checked before paying CNKI per-page fees. For the priority Cordyceps paper, the publisher/JATS page is available outside CNKI:

- `Effect and Mechanism of Cordyceps militaris Extract on Lowering Uric Acid in Hyperuricemia Rats` - [Biotechnology Bulletin publisher page](https://biotech.aiijournal.com/CN/10.13560/j.cnki.biotech.bull.1985.2024-0379)

The publisher-page read is now captured in `p0-1-cordyceps-biotech-source-read-2026-05-20.md`. It supports a cautious wiki update as **Animal Model** evidence for whole *C. militaris* water extract in hyperuricemia rats, not human evidence and not an MSU-flare model.

CNKI records:

1. `Effect and Mechanism of Cordyceps militaris Extract on Lowering Uric Acid in Hyperuricemia Rats` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-CyrYCiF-YxoIDQk7aZfTn4UoXjxU5pAz5UXuaMgf0skSD5b_zZks7HF4jxJHIClW-Y6rpye1KwjQUJDVH-1ITCfdPf9LgWIgZb82QxFPFVpaynreUIiSLGTVRYxYRSfRtvFFM-2Q2IY8_oN--5k0S9IXLElrjkvBklvDksrNt4aQ==&uniplatform=OVERSEA&language=EN)
2. `Study on the Cordyceps militaris for lowering uric acid of patients with hyperuricemia` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-BGqgfXYjMImcM2E7wCFdPUGJfK3rH2VB2k17289dORkaAYb7T72V6X58bEzU8Svn1YVA46cu6M18OuXdW3DmBEB_SLZq5449Q3SJ_k3St8lLDanA0jEXw9dyft2YI_pPXJKRex5kEgpk8P40-aF48uyIlqZJwE8W7ChefXNCW62w==&uniplatform=OVERSEA&language=EN)
3. `Rapid identification by UPLC-Q-TOF-MS of the chemical composition of Sanghuangporus vaninii alcohol extract from poplar and its urate-lowering activity and nephroprotective effect` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-ApuU8cmHNU8r26TctfD1UxD-f5uR__773Cfp9yOlVY4lcolxC9GH3vCMFzCrBp8NvdOy7fMxa1aXxtOxThn--PHnZxSBqExrhAsjXMM4RHy4fVYJ_zwwKrLSWLpVS0DjlO2m7ei1HDyJHVBvO5LLnnYP1TTapQOO1JntLxnPD4OQ==&uniplatform=OVERSEA&language=EN)
4. `Study on the Mechanism of Anti-inflammatory and Lowering Uric Acid Effect by Total Flavonoids of Phellinus Igniarius in Vitro Based on Network Pharmacology` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-ApuU8cmHNU8r26TctfD1UxkamAi4H0cxLWgYsLSsyam5rVD8hOEKCiCA8SZuVxm-HYZ6Vns_GVmSyx1OBjJrV0Eu0eAe4c23DpzYdS15B-G-XTcFUhooAsjT_mrDofnXuh9OA4qsyiijTT37Z8vUVDiqI4LB5iiJPQwE-_t6fwIg==&uniplatform=OVERSEA&language=EN)
5. `Effects of Ganoderma lucidum Aqueous Extract on Uric Acid Level and Renal Function of Rats with Hyperuricemia` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-AUV-0z3lXKgJkU8KBlGy-lm690oAHlbBLAVWksGRhz6qTclTLoY-Gxe8r0LdJzo46avAL4h-lPkT5OvnZPXJd7Bc_zrNK4e8Cjr2SWT9xOPovF9eFST4ptUZRciJGVmw3USvemafJAXfMhpD84FOGede-sdTm9i_x02-qs-VO8MQ==&uniplatform=OVERSEA&language=EN)
6. `Analysis of metabolite components of Cordyceps militaris and their effects on hyperuricemia` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-CyrYCiF-YxoIDQk7aZfTn4UoXjxU5pAz7FtYgE_A1LXLArrgr9nl4l4ikjI0OK4KXIXkGgOgumGvgquYQtfhi6ouWTXay6k8dIY5RTz0s9Iu2SBdCocwQpR0JiuPdulgwV_K5C7Z4LxeZjVbb0JFVP9piNVwmWpRCMhYU8DqmtzQ==&uniplatform=OVERSEA&language=EN)
7. `Screening,separation and mass spectrometry analysis of xanthine oxidase inhibitors in Phellinus igniarius` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-AbqQTLh8593bKaAnrn2ytw4nm5_5VZsEKyHUnW2GjcJys6xSCq5hRjpNb8Bu7kL47HduXWQe4Lj1u7zXrUE0FHi-AnPxR1Z17_KaHo17jt7uKyQg_KNC8KSYawmDT4tIPqXM_p8OpJiC_uhZCYdHWISg8C-zmw4NmeaHSdS8nnSg==&uniplatform=OVERSEA&language=EN)
8. `灵芝多糖肽通过调节腺苷脱氨酶和尿酸转运蛋白减轻高尿酸血症` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-DXTOfRQnJizbk6GAwEWnacUBVMdOPRJn4G_YgikeMqgyogXet0_nvS2rOYlivNpyaqzc8-qAx0GODnlNl__FPlk6Pf6fdqoa3ioWhaVInzJE6z-Ky9JRfitRfLwUjSHypQuxbdB7Ds6Z7i_2bU3q4yFpGA8X9RG1COUteIw-iWa6cpChHvssct&uniplatform=OVERSEA&language=EN)
9. `蛹虫草防治高尿酸血症的实验研究` - [CNKI Overseas](https://oversea.cnki.net/kcms2/article/abstract?v=g8n7TwuHW-BGqgfXYjMImcM2E7wCFdPUGJfK3rH2VB3KU1KWcXzt4qWijz-dULwDFClSt8MNK1jAnGPeMRFEXBfyjGrAeZ67sMGXPkUIIzGDmDsXqfHuzsdZqCMptLiG6zv60zFCAxD37sAiKc635LZ4hSSwjLUiNd7DPYZjwUqEdfI8hihF2w==&uniplatform=OVERSEA&language=EN)

## Consensus Read

The corrected CNKI route materially changes P0-1: Ganoderma, Sanghuang/Phellinus/Sanghuangporus, and Cordyceps militaris all have CNKI-native urate/hyperuricemia leads. The correct next action is full-text retrieval / reading, not immediate wiki evidence-tier promotion.

The strongest follow-up priority is Cordyceps militaris. It has multiple independent CNKI records spanning animal models, metabolomics, XOD/urate-transporter mechanisms, and one small uncontrolled human patient report.

Sanghuang/Phellinus is also strong, but its mechanistic claims need careful full-text verification because one TFPI abstract reports transporter protein and mRNA directions that do not trivially align.

Ganoderma remains a real lead, but weaker than Cordyceps/Sanghuang for OE prioritization because the strongest available record is a 2024 animal/cell abstract and includes a cautionary kidney-urate nuance.

## Article-Level Assessment

| Lead | Evidence tier from abstract | Main signal | Caution before wiki promotion |
|---|---|---|---|
| Ganoderma lucidum aqueous extract, 2024 | Animal model plus L-O2 cell model | Serum urate decreased at medium/high gavage doses; serum/hepatic XOD decreased; creatinine/BUN decreased | Abstract also says kidney uric acid increased at all doses. This needs full-text interpretation before renal-benefit language. |
| Ganoderma lucidum polysaccharide peptide / GLPP, 2023 conference | Abstract insufficient / conference abstract only | Title claims GLPP regulates adenosine deaminase and urate transporters | CNKI abstract snippet only contains background and keywords; no model, dose, or results visible. Do not promote. |
| Phellinus igniarius total flavonoids, 2025 | Network pharmacology plus MSU-induced HK-2 cell validation | Anti-inflammatory signal in renal tubular cell injury model; IL-6, IL-1beta, IL-18, TNF-alpha reduction; NLRP3/TLR4/NF-kB axis implicated | Transporter readout is internally nuanced: protein-level ABCG2/OAT1 decreased and URAT1 increased, while mRNA-level ABCG2/OAT1 increased and URAT1 decreased. Full text required before mechanism mapping. |
| Sanghuangporus vaninii alcohol extract, 2025 | Animal model plus in vitro XOD | UPLC-Q-TOF-MS identified 42 compounds; extract inhibited XOD in vitro and reduced UA/BUN/CRE/XOD markers in HUA mice | CNKI English abstract says "compared with the allopurinol group" for reductions, which is biologically/statistically surprising. Verify original Chinese/full text before treating magnitude/comparator as load-bearing. |
| Phellinus igniarius XOD inhibitors, 2023 | In vitro biochemical | Isolated three >90% purity XOD inhibitors: phelligridin D > phelligridin E > fibrocidin A | No animal or urate outcome in abstract; useful for mechanism/fractionation leads, not efficacy. |
| Cordyceps militaris extract, 2024 | Animal model | Rat HUA model; best dose 0.5 g/(kg*d) reduced serum urate from 281.62 to 93.27 micromol/L; URAT1/GLUT9 down, OAT1/ABCG2 up; hepatic XOD down; microbiota diversity improved | Strongest abstract-level lead, but full text needed for group sizes, controls, assay timing, and exact extract identity. |
| Cordyceps militaris metabolites, 2020 | Animal model plus metabolomics | 233 metabolites identified; middle/high dose decreased serum urate and XOD activity in mice; purine metabolism / ABC transporter pathways implicated | Abstract lacks dosing and magnitude; treat as corroborating mechanism lead. |
| Cordyceps militaris powder in hyperuricemia patients, 2014 | Human uncontrolled | 22 patients; after one month, UA/BUN/CREA indicators changed significantly; reported UA "efficiency rate" 77.3% | Not randomized, no control group visible, and "efficiency rate decreasing UA" is ambiguous. This is a lead for full-text clinical-method review, not clinical evidence. |
| Cordyceps militaris anti-HUA experimental study, 2013 | Animal model | Ethanol extract lowered serum creatinine, urate, and XOD activity in HUA mice; petroleum ether and n-butanol fractions identified as active parts | Model induction, doses, and exact magnitudes absent from abstract. Full text needed. |

## Translation / Nuance Flags

No direct model-vs-model disagreement changed the top-line ranking. The disagreements/flags that matter are source-level ambiguity and abstract-only incompleteness:

- `[SOURCE-NUANCE]` Ganoderma: serum urate improved but kidney uric acid increased. Do not describe as clean nephroprotective evidence until full text explains tissue urate handling.
- `[SOURCE-NUANCE]` Phellinus TFPI: transporter mRNA and protein directions diverge in the abstract. Do not collapse into "ABCG2/OAT1 up, URAT1 down" without full text.
- `[TRANSLATION-SOURCE-AMBIGUITY]` Sanghuangporus vaninii: the English abstract comparator phrase "compared with the allopurinol group" is suspicious. Verify original Chinese wording before using any comparative efficacy claim.
- `[EVIDENCE-TIER]` Cordyceps human record: uncontrolled 22-person report is discovery-positive but not clinical-trial evidence.
- `[ABSTRACT-INSUFFICIENT]` GLPP conference item: title is interesting, visible abstract is background-only.

## Priority List

1. Retrieve/read full text for 2024 Cordyceps militaris extract in HUA rats.
2. Retrieve/read full text for 2014 Cordyceps militaris powder in 22 hyperuricemia patients, focused on design, dose, population, endpoint definition, and control/comparator absence.
3. Retrieve/read full text for 2025 Sanghuangporus vaninii alcohol extract, focused on comparator wording and renal pathology.
4. Retrieve/read full text for 2025 Phellinus TFPI, focused on transporter protein/mRNA interpretation and whether NLRP3/MSU claims are cellular-only.
5. Retrieve/read full text for 2024 Ganoderma aqueous extract, focused on kidney urate increase and renal markers.
6. Treat 2023 GLPP conference and 2023 Phellinus inhibitor-isolation records as follow-up mechanistic/fractionation leads unless full text is easy to access.

## Bottom Line

P0-1 is upgraded from "possibly missed due to CNKI failure" to "real Chinese-literature lead set recovered." The OE-relevant near-term action is not a wiki claim update yet; it is full-text acquisition for Cordyceps militaris and Sanghuang/Phellinus, using the two-model protocol again on methods/results sections before any evidence-tier changes land in the wiki.
