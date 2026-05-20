---
title: P0-4 NLRP3 mushroom immunomodulation CNKI rerun summary
date: 2026-05-20
status: discovery-mixed
---

# P0-4 NLRP3 mushroom immunomodulation CNKI rerun summary

## Method

The P0-4 pass reused the corrected CNKI Overseas route: load the search page through local curl for cookies, then replay the browser-captured `POST /kns8s/brief/grid` request shape and parse the first result page. Results are saved in [`p0-4-cnki-overseas-rerun-2026-05-20.json`](./p0-4-cnki-overseas-rerun-2026-05-20.json); raw grid HTML and provenance records are under [`retrieval-probes-raw/`](./retrieval-probes-raw/).

This is a discovery artifact only. It should not promote wiki evidence tiers unless priority records are retrieved/read at full-text level and handled with the two-model translation protocol.

## Query-count results

| Query frame | CNKI total | Takeaway |
|---|---:|---|
| `灵芝孢子粉 NLRP3炎症小体` / `灵芝孢子粉 白细胞介素1β` / `灵芝孢子粉 痛风` | 0 / 0 / 0 | Spore-powder-specific framing did not recover a CNKI corpus for NLRP3, IL-1β, or gout. |
| `灵芝 NLRP3炎症小体` | 9 | Real Lingzhi/Ganoderma NLRP3 signal, mostly review/thesis/conference-level leads. |
| `灵芝 高尿酸血症 NLRP3` | 1 | One directly relevant hyperuricemia/gout risk-management review lead; not primary efficacy evidence. |
| `灵芝多糖 NLRP3炎症小体` | 4 | Fraction-specific Ganoderma polysaccharide/NLRP3 signal; likely immunology background until source-read. |
| `灵芝肽 NLRP3炎症小体` / `灵芝肽 GLP4 NLRP3` | 4 / 2 | Direct GLP4/NLRP3 conference/thesis leads, but in myocardial ischemia/reperfusion rather than gout. |
| `云芝多糖肽 NLRP3炎症小体` / `云芝多糖肽 白细胞介素1β` / `云芝多糖肽 痛风` | 0 / 0 / 0 | Yun Zhi PSP-style exact product framing did not recover gout/NLRP3 records. |
| `PSP NLRP3炎症小体` / `PSK NLRP3炎症小体` | 2346 / 2346 | Too noisy: top records are generic NLRP3 papers, not Yun Zhi PSP/PSK. Do not treat as PSP/PSK evidence. |
| `云芝多糖肽 抗炎` | 1 | One old antitumor/co-administration record; not gout/NLRP3 evidence. |
| `灰树花 NLRP3炎症小体` / `灰树花 白细胞介素1β` / `灰树花 痛风` | 0 / 0 / 0 | Maitake/Grifola exact gout/NLRP3 framing was cold. |
| `灰树花多糖 炎症` | 37 | Broad Grifola polysaccharide inflammation/bioactivity literature, not gout-specific and not NLRP3-specific in this pass. |
| `β-葡聚糖 NLRP3` | 14 | Useful fungal beta-glucan / NLRP3 background corpus. |
| `香菇多糖 NLRP3` | 8 | Comparator beta-glucan/lentinan NLRP3 corpus; outside target mushrooms but useful for mechanism context. |

`None` totals in the JSON correspond to CNKI's `Sorry, no data temporarily` response and are treated as zero-result searches for this pass.

## Highest-priority reads

1. **Direct hyperuricemia/gout mushroom review lead.**
   - `Reevaluating the Purine Controversy and Health Effects of Edible Mushroom: Multidimensional Regulatory Mechanisms in Hyperuricemia and Gout Risk Management` (2025, *Food Science*).
   - Why: the only CNKI hit in this pass that directly combines edible mushrooms, hyperuricemia/gout risk management, and NLRP3 in the query frame. It is likely review-level, so use it as a source map rather than promotion evidence.

2. **Ganoderma polysaccharide immunomodulation review.**
   - `Research Advances in the Structure Feature and Immunomodulatory Mechanisms of Ganoderma lucidum Polysaccharides` (2026, *Journal of Shanxi Agricultural Sciences*).
   - Why: may explain how Ganoderma beta-glucan/polysaccharide structure maps onto innate immune pathways; relevant to safety/immunomodulation framing even if not gout-specific.

3. **Lingzhi peptide GLP4 / NLRP3 lead.**
   - `灵芝肽GLP4通过调节精氨酸生物合成并抑制NLRP3炎症小体激活减轻心肌缺血/再灌注炎症反应` (2025, China conference abstract).
   - Why: direct NLRP3 language and active-fraction specificity, but tissue/disease context is myocardial ischemia/reperfusion, not gout.

4. **Grifola polysaccharide inflammation background.**
   - `Current situation and prospect of research on bioactivity and mechanism of Grifolia frondose polysaccharide` (2024).
   - `Effect of polysaccharides from Grifola frondosa on gastrointestinal flora and oxidative damage in rats with gastric ulcers` (2025).
   - Why: could inform gut/barrier and inflammatory safety context, but this pass found no direct gout/HUA/NLRP3 Grifola lead.

5. **Beta-glucan comparator corpus.**
   - `β-葡聚糖 NLRP3` and `香菇多糖 NLRP3` hits.
   - Why: useful for mechanism-background calibration of fungal polysaccharides, but should not be mistaken for Lingzhi/Yun Zhi/Maitake efficacy evidence.

## Interpretation

P0-4 is discovery-mixed. The corrected CNKI route recovered a real Lingzhi/Ganoderma NLRP3/polysaccharide/peptide background corpus and one directly relevant mushroom-HUA/gout review lead. It did not recover strong CNKI evidence that Lingzhi spore powder, Yun Zhi PSP/PSK, or Maitake/Grifola have gout-specific or hyperuricemia-specific NLRP3 evidence.

The key operational lesson is query granularity. `灵芝孢子粉` was cold, while `灵芝`, `灵芝多糖`, and `灵芝肽` produced signal. For maitake, the Chinese common name `灰树花` is the right CNKI frame, but it still yielded inflammation/bioactivity background rather than gout/NLRP3 hits. For PSP/PSK, English abbreviations are too ambiguous in CNKI Subject TOPRANK and should be paired with `云芝多糖肽`, `云芝多糖`, or article-title filtering before interpretation.

## Non-promotion caveat

Do not upgrade mushroom/NLRP3 wiki claims from this artifact. The next useful move is source-map reading of the 2025 edible-mushroom HUA/gout review and the 2026 Ganoderma polysaccharide immunomodulation review, then decide whether any primary animal/cell papers they cite merit full-text two-model reads.
