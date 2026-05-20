---
title: P0-3 TCM gout formula CNKI rerun summary
date: 2026-05-20
status: discovery-positive
---

# P0-3 TCM gout formula CNKI rerun summary

## Method

The static CNKI query page was not enough; the usable route is the browser-captured `POST /kns8s/brief/grid` request shape from CNKI Overseas, replayed through local `curl` so traffic egresses from Brian's whitelisted laptop network path. Results are saved in [`p0-3-cnki-overseas-rerun-2026-05-20.json`](./p0-3-cnki-overseas-rerun-2026-05-20.json); raw grid HTML and provenance records are under [`retrieval-probes-raw/`](./retrieval-probes-raw/).

This is a discovery artifact only. Do not promote evidence-tier claims until the priority records are retrieved/read at full-text level and translated with the two-model protocol.

## Query-count results

| Query frame | CNKI total | Takeaway |
|---|---:|---|
| `四妙散 痛风` | 424 | Dense formula-level gout corpus; top result is 2026 network pharmacology / molecular dynamics. |
| `四妙散 高尿酸血症` | 69 | HUA-specific formula corpus, including 2026 hyperuricemic-rat renal-fibrosis work and 2025 clinical/mechanism reviews. |
| `四妙散 URAT1` | 4 | Low count but high signal: 2010 HK-2 UAT/URAT1, 2016 hyperuricemic-rat urate-transporter expression, 2025 review. |
| `四妙散 尿酸转运体1` | 0 / unparsed | Synonym sensitivity matters; English `URAT1` found records where the Chinese transporter phrase did not. |
| `白虎加桂枝汤 痛风` | 73 | Strong acute-gout formula corpus, including clinical and animal-model/NLRP3 records. |
| `白虎加桂枝汤 高尿酸血症` | 8 | Smaller but high signal; includes benzbromarone-combination clinical records and rat anti-inflammatory mechanism work. |
| `乌梅丸 痛风` / `乌梅丸 高尿酸血症` | 3 / 1 | Weak gout/HUA relevance in this pass; likely not a first follow-up. |
| `土茯苓 痛风` | 610 | Very dense gout corpus; many formula/mining records, plus direct Smilax review hits. |
| `土茯苓 高尿酸血症` | 477 | Very dense HUA corpus. |
| `土茯苓 URAT1` | 24 | High-value mechanistic corpus; top records include Smilax multi-target review and a 2025 AMPK/PGC-1α/PPARγ/ABCG2 mechanism paper. |
| `姜黄 痛风` / `姜黄 高尿酸血症` / `姜黄 黄嘌呤氧化酶` | 34 / 50 / 21 | Curcumin/turmeric remains a real NLRP3/XO/HUA lead, though many records are thesis/network-pharmacology tier. |
| `知母 痛风` / `知母 高尿酸血症` | 243 / 67 | Dense because Zhimu appears in gout formulas, especially Guizhi Shaoyao Zhimu Tang; needs formula-context parsing. |
| `黄柏 痛风` / `黄柏 URAT1` | 630 / 8 | Dense because Huangbai is a Simiao component; direct URAT1 hits mostly route back to formula-level work. |
| `中药复方 痛风 URAT1` | 11 | Useful mechanism-oriented follow-up; top records include Jinqian Xuduan Decoction, Simiao Wan pharmacodynamic-substance work, and urate-transporter review. |
| `中药复方 高尿酸血症 黄嘌呤氧化酶` | 63 | Broad formula/XO/gut-microbiome corpus; useful second-pass field map, not a first promotion source. |

## Highest-priority full-text reads

1. **Simiao / URAT1 transporter pair.**
   - `Effects of Si MiaoSanJia WeiFang on the expression of human UAT and URAT1 transporter genes in HK-2 cells` (2010, *Chinese Journal of Clinical Pharmacology and Therapeutics*).
   - `Effect of Simiao Modified Formula in Rats with Hyperuricemia and Expression in Uric Acid Transporter` (2016, *Journal of Chinese Medicinal Materials*).
   - Why: these directly test the formula against urate-transporter expression rather than merely infer targets.

2. **Simiao Wan pharmacodynamic-substance work.**
   - `Study on the Pharmacodynamic Substances of Simiao Wan for Treatment of Hyperuricemia and Gout Based on Disease and Syndrome Model` (2024, *Traditional Chinese Drug Research and Clinical Pharmacology*).
   - Why: this could separate the formula into active fractions/components and may connect to the existing comp-013 compound-level triage.

3. **Smilax glabra / ABCG2 pathway lead.**
   - `Mechanism of Smilacis Glabrae Rhizoma in treating hyperuricemia due to dampness-heat through the AMPK/PGC-1α/PPARγ/ABCG2 pathway` (2025, *Natural Product Research and Development*).
   - Why: direct ABCG2 pathway language makes this relevant to the gut-lumen sink and Q141K-rescue tracks, not just TCM background.

4. **Baihu plus Guizhi Decoction / acute-gout inflammation.**
   - `Effects of Baihu Plus Guizhi Decoction on TLRs and NALP3 Signaling Pathways in Rats with Acute Gouty Arthritis` (2023, *Chinese Archives of Traditional Chinese Medicine*).
   - `Anti-inflammatory mechanism of Baihu Jiaguizhi Decoction on hyperuricemia and acute gouty arthritis in rats` (2019, *China Journal of Traditional Chinese Medicine and Pharmacy*).
   - Why: these likely map to CP1/CP2/CP3 inflammatory chokepoints rather than renal urate handling.

5. **Jinqian Xuduan Decoction / URAT1 formula lead.**
   - `Research on the Chinese Medicine Formula Jinqian Xuduan Decoction for Reducing Uric Acid and Treating Gout` (2025 doctoral dissertation).
   - Why: appears across both `黄柏 URAT1` and `中药复方 痛风 URAT1`; thesis-level work may contain full mechanistic panels absent from journal abstracts.

## Interpretation

P0-3 is strongly discovery-positive. The corrected CNKI route plus native formula/species/pathology framing recovers exactly the class of literature the audit predicted was being missed: formula-anchored TCM studies with urate-transporter, XO, gut-microbiome, and NLRP3/IL-1β mechanisms.

Two query-framing lessons are now operational:

- **Formula names are the highest-yield entry point.** `四妙散 痛风` and `白虎加桂枝汤 痛风` recover clinical and mechanistic records that a pure `URAT1` or `NLRP3` search would under-sample.
- **Synonym breadth is mandatory.** `四妙散 URAT1` recovered four high-signal records, while `四妙散 尿酸转运体1` returned no parsed records. Native-script terms are necessary but not sufficient; the scan needs English target abbreviations plus Chinese mechanism terms plus formula/pathology anchors.

## Non-promotion caveat

No wiki evidence-tier upgrade should land from this summary alone. The next unit of work is full-text acquisition for the five priority reads above, followed by Codex/GPT-5.5 plus DeepSeek two-model reading of methods/results. Until then, treat this as a source-route and priority-list artifact, not proof that any formula should move tiers.
