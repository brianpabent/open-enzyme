# P0-1 CNKI Overseas rerun summary

Date: 2026-05-20

Scope: P0-1 comp-014 medicinal mushroom Phase 5b rescue scan, focused on CNKI Overseas after correcting the CNKI route from `kns.cnki.net` to `oversea.cnki.net`.

Method: for each focused P0-1 Chinese query, load the CNKI Overseas search page for cookies and POST the equivalent simple Subject query to `https://oversea.cnki.net/kns8s/brief/grid`. Parsed the first result page into title, source, date, CNKI abstract URL, and CNKI AI reading URL when present. These are discovery leads only; no wiki evidence tier should change until the lead papers are read from original text with two independent models.

## Query Yield

| Query | CNKI total | Notes |
|---|---:|---|
| `灵芝 多糖肽 分离纯化` | 39 | Strong fractionation/purification corpus; mostly Ganoderma polysaccharide extraction/structure papers. |
| `灵芝 高尿酸血症` | 7 | Includes 2024 Ganoderma aqueous extract hyperuricemia-rat paper and a 2023 medicinal-fungi conference abstract on GLPP / ADA / urate transporters. |
| `灵芝 痛风` | 6 | Weak direct gout signal; mostly treatment-pattern / popular-medical hits. |
| `灵芝 黄嘌呤氧化酶` | 13 | Includes the 2024 Ganoderma hyperuricemia-rat paper; several non-urate XOD physiology hits. |
| `灵芝孢子粉 高尿酸血症` | 0 parsed | No first-page result table returned through the direct grid extraction path. |
| `灵芝孢子粉 NLRP3 炎症小体` | 0 parsed | No first-page result table returned through the direct grid extraction path. |
| `桑黄 高尿酸血症` | 28 | Strongest P0-1 urate signal; multiple 2024-2026 review and primary leads. |
| `桑黄 黄嘌呤氧化酶` | 10 | Strong XO / urate-lowering lead set, including inhibitor-screening and Sanghuangporus vaninii chemistry/activity papers. |
| `蛹虫草 高尿酸血症` | 12 | Strong Cordyceps militaris hyperuricemia set. |
| `蛹虫草 痛风` | 7 | Includes older clinical/experimental hyperuricemia leads. |
| `蛹虫草 黄嘌呤氧化酶` | 8 | Includes Cordyceps metabolite / hyperuricemia and XO-oriented papers. |
| `云芝多糖肽 高尿酸血症` | 0 parsed | No first-page result table returned through direct grid extraction. |
| `云芝多糖肽 痛风` | 0 parsed | No first-page result table returned through direct grid extraction. |
| `云芝多糖肽 NLRP3` | 0 parsed | No first-page result table returned through direct grid extraction. |
| `舞茸 高尿酸血症` | 0 parsed | No first-page result table returned through direct grid extraction. |
| `菌草 灵芝 栽培` | 95 | Strong cultivation/substrate corpus; relevant to substrate and JUNCAO sourcing, not directly urate. |
| `菌草 灵芝 多糖` | 86 | Strong substrate/product-formulation corpus; relevant to cultivation/fractionation quality, not directly urate. |

## Highest-Priority Lead Articles

These were fetched as article pages and should be read next under the two-model non-English-source protocol:

1. `Effects of Ganoderma lucidum Aqueous Extract on Uric Acid Level and Renal Function of Rats with Hyperuricemia` — Acta Edulis Fungi, 2024-09-24.
2. `灵芝多糖肽通过调节腺苷脱氨酶和尿酸转运蛋白减轻高尿酸血症` — 12th Medicinal Fungi Academic Symposium proceedings, 2023-10-21.
3. `Study on the Mechanism of Anti-inflammatory and Lowering Uric Acid Effect by Total Flavonoids of Phellinus Igniarius in Vitro Based on Network Pharmacology` — Chinese Journal of Modern Applied Pharmacy, 2025-02-15.
4. `Rapid identification by UPLC-Q-TOF-MS of the chemical composition of Sanghuangporus vaninii alcohol extract from poplar and its urate-lowering activity and nephroprotective effect` — Journal of Jilin Agricultural University, 2025-01-20.
5. `Screening,separation and mass spectrometry analysis of xanthine oxidase inhibitors in Phellinus igniarius` — China Food Additives, 2023-12-19.
6. `Effect and Mechanism of Cordyceps militaris Extract on Lowering Uric Acid in Hyperuricemia Rats` — Biotechnology Bulletin, 2024-09-26.
7. `Analysis of metabolite components of Cordyceps militaris and their effects on hyperuricemia` — Mycosystema, 2020-09-15.
8. `Study on the Cordyceps militaris for lowering uric acid of patients with hyperuricemia` — Lishizhen Medicine and Materia Medica Research, 2014-10-20.
9. `蛹虫草防治高尿酸血症的实验研究` — Chinese Traditional Patent Medicine, 2013-08-20.

## Interpretation

P0-1 should be rerun. The corrected CNKI route materially changes the prior picture: Ganoderma, Sanghuang/Phellinus/Sanghuangporus, and Cordyceps militaris all have CNKI-native urate/hyperuricemia leads that were not visible in the earlier J-STAGE-only / broken-CNKI pass.

The highest-confidence next move is not to update the wiki yet. It is to perform a two-model source reading on the nine lead articles above, with special attention to: species identity, extract/fraction identity, animal vs human evidence tier, urate-lowering magnitude, XO / ADA / URAT1 / GLUT9 / ABCG2 mechanism attribution, renal-safety markers, and whether any NLRP3/MSU axis data exists in the full text.
