# P0-1 CNKI Two-Model Source Read

Date: 2026-05-20

Scope: conservative source-read pass over the nine highest-priority P0-1 medicinal-mushroom / hyperuricemia CNKI lead records recovered after the CNKI Overseas route correction.

Protocol: Codex/GPT-5.5 performed the primary synthesis in-session from CNKI Overseas article abstract pages. DeepSeek (`deepseek/deepseek-chat-v3` via OpenRouter) performed the native-Chinese counter-read from the same abstract records. OpenRouter usage for the DeepSeek pass was 5,481 tokens / $0.00276738.

Important limitation: CNKI full-text HTML/PDF/CAJ order endpoints redirected local curl to CNKI Overseas login pages. This pass therefore ingests CNKI article metadata and abstracts only. Do not promote wiki evidence tiers from this artifact as if full text had been read.

Source artifacts:

- `p0-1-cnki-lead-abstract-records-2026-05-20.json` - parsed title, abstract, and keyword records.
- `p0-1-cnki-deepseek-counterread-2026-05-20.json` - native-Chinese counter-read.
- `fulltext-probes/fulltext-fetch-index.json` - full-text endpoint probes showing login redirects.

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
