---
title: P0-3 TCM gout formula full-text retrieval and source read
date: 2026-05-20
status: partial-source-read
---

# P0-3 TCM gout formula full-text retrieval and source read

## Verdict

P0-3 is complete as a corrected discovery scan, but only partially complete as a promotion-grade source-read pass. The native-query CNKI rerun recovered a dense formula/pathology corpus, but CNKI article-order endpoints still redirect local curl to login pages for the priority Simiao, Smilax, and Baihu+Guizhi records. One open full-text Baihu Guizhi acute-gout animal paper was retrieved and read; it can support an Animal Model mechanism note, not clinical efficacy.

## Retrieval results

### CNKI priority records

The P0-3 CNKI rerun nominated these highest-priority source reads:

- `Effects of Si MiaoSanJia WeiFang on the expression of human UAT and URAT1 transporter genes in HK-2 cells` (2010).
- `Effect of Simiao Modified Formula in Rats with Hyperuricemia and Expression in Uric Acid Transporter` (2016).
- `Effect of Simiao Wan on pharmacodynamic substances for treating hyperuricemia` (2024).
- `Smilax glabra Roxb. Ameliorates Hyperuricemic Nephropathy via the AMPK/PGC-1α/PPARγ/ABCG2 Pathway` (2025).
- Baihu+Guizhi TLR/NALP3 rat work (2023/2019).

Article pages were reachable through `oversea.cnki.net`, but the HTML/PDF/CAJ order/download routes returned CNKI login pages rather than full text. These records remain discovery-positive only. They should not change wiki evidence tiers until manually downloaded or retrieved through a legitimate open route and then read with the two-model translation protocol.

### 2016 Simiao rat paper

SinoMed exposes an abstract page for `Effect of Simiao Modified Formula in Rats with Hyperuricemia and Expression in Uric Acid Transporter` at `https://www.sinomed.ac.cn/article.do?ui=2017365548`. The abstract reports a potassium-oxonate/ethambutol hyperuricemic rat design and transporter readouts for URAT1, OAT1, and GLUT9, but this is abstract-level only. Use it as a retrieval locator, not a source for promotion.

### 2010 Simiao HK-2 paper

The non-CNKI publisher route for the 2010 HK-2 paper appears to be:

- Article page: `https://manu41.magtech.com.cn/Jweb_clyl/EN/abstract/abstract11076.shtml`
- PDF route: `https://manu41.magtech.com.cn/Jweb_clyl/CN/article/downloadArticleFile.do?attachType=PDF&id=11076`

Local curl currently cannot connect to `manu41.magtech.com.cn` (`112.124.103.14`) on ports 80 or 443. Add `manu41.magtech.com.cn` to the China-literature firewall allowlist, then retry this route before paying CNKI for that paper.

### Open Baihu Guizhi animal-model full text

Retrieved and read:

Liu G, Wu J, Song H. `Baihu Guizhi decoction alleviates inflammation in rats with acute gouty arthritis by targeting miR-17-5p to regulate the TLR4/Myd88/NF-kB signaling pathway`. *Clinics*. 2025;80:100665. DOI `10.1016/j.clinsp.2025.100665`.

Local files:

- `/tmp/oe-p0-3/baihu-guizhi-clinics-2025.pdf`
- `/tmp/oe-p0-3/baihu-guizhi-clinics-2025.txt`

Evidence level: Animal Model.

What the full text supports:

- MSU-induced acute gouty arthritis rat model.
- Baihu Guizhi decoction reduced ankle swelling/inflammation and reduced synovial TLR4/MyD88 and NF-kB pathway readouts.
- Serum IL-1β and IL-6 decreased; TNF-α did not materially change in the decoction-only group.
- This is an inflammation-axis paper, not a urate-lowering paper.

Promotion cautions:

- It is not human efficacy evidence.
- The decoction dose is very high (`28 g/kg` intragastric in the methods), so it should not be translated into a practical human dosing claim.
- The miR-17-5p mimic / TLR4 inhibitor arm is mechanistically interesting but pharmacologically artificial; use the paper only as support for BHGZ touching the TLR4/MyD88/NF-kB inflammatory axis in a rat MSU model.

## Two-model translation status

The only promotion-grade P0-3 source recovered in this pass is English full text, so the non-English two-model translation protocol was not needed for the wiki update. The Chinese-language CNKI records still require two-model source reads once full text is obtained.

## Next action

1. Whitelist `manu41.magtech.com.cn` and retry the 2010 Simiao HK-2 PDF before spending money on CNKI.
2. For the 2016 Simiao rat paper and 2024/2025 CNKI records, use manual CNKI access only if no legitimate mirror/publisher route appears.
3. After full text is obtained, run Codex/GPT-5.5 plus DeepSeek or Qwen counter-read before any Simiao/Smilax evidence-tier promotion.
