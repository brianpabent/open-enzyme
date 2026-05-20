---
title: P0-4 edible mushroom / Ganoderma source-map note
date: 2026-05-20
status: source-map-complete
---

# P0-4 edible mushroom / Ganoderma source-map note

## Retrieval status

The P0-4 CNKI rerun nominated two useful source-map leads:

1. `Reevaluating the Purine Controversy and Health Effects of Edible Mushroom: Multidimensional Regulatory Mechanisms in Hyperuricemia and Gout Risk Management` (2025, *Food Science*, DOI `10.7506/spkx1002-6630-20250617-117`).
2. `Research Advances in the Structure Feature and Immunomodulatory Mechanisms of Ganoderma lucidum Polysaccharides` (2026, *Journal of Shanxi Agricultural Sciences*).

For the first lead, the public *Food Science* article page is visible at [`https://www.spkx.net.cn/EN/10.7506/spkx1002-6630-20250617-117`](https://www.spkx.net.cn/EN/10.7506/spkx1002-6630-20250617-117), and AGRIS/DOAJ exposes a PDF URL at [`https://www.spkx.net.cn/fileup/1002-6630/PDF/2025-46-24-040.pdf`](https://www.spkx.net.cn/fileup/1002-6630/PDF/2025-46-24-040.pdf). After `spkx.net.cn` was allowlisted, local curl could retrieve the PDF by carrying cookies from the article page and using a browser-like user agent and referrer. A direct bare PDF request still returned HTTP 403.

Local files:

- `/tmp/oe-p0-4/edible-mushroom-hua-gout-2025.pdf`
- `/tmp/oe-p0-4/edible-mushroom-hua-gout-2025.txt`
- DeepSeek counter-read: [`p0-4-spkx-deepseek-counterread-2026-05-20.json`](./p0-4-spkx-deepseek-counterread-2026-05-20.json)

For the second lead, the exact CNKI journal article remains CNKI-full-text-bound. A close open-access English review is available as Wu et al. 2025, `Structure-function insights of natural Ganoderma polysaccharides: advances in biosynthesis and functional food applications`, *Natural Products and Bioprospecting*, DOI `10.1007/s13659-025-00496-w`.

## Source-map read

The *Food Science* 2025 article is review-level, not primary evidence. It reviews mushroom consumption, serum uric acid, gout risk, and mechanisms by which medicinal/edible mushroom bioactives may affect uric-acid metabolism and gout pathogenesis. That makes it valuable as a source map for primary studies, but not enough to promote an evidence tier.

Codex/GPT-5.5 and DeepSeek agree on the core interpretation:

- The review argues that edible mushrooms may have a potential net protective effect despite purine-content concerns, but this is a review synthesis rather than a clinical finding.
- The mechanistic map covers XO/XOR inhibition, urate transporter regulation, anti-inflammatory/antioxidant effects, gut microbiota, and the TLR/NF-kB/NLRP3 inflammatory frame.
- The strongest value is the bibliography, not the review's own conclusion.

Translation note: DeepSeek flagged `净保护效应` as a nuance-sensitive phrase. Treat it as "the review argues for a possible net protective effect" rather than "edible mushrooms are protective." The distinction between `食用菌` (edible mushrooms) and `药用菌` (medicinal mushrooms) also matters because several cited active-extract studies are medicinal-mushroom/preclinical rather than ordinary dietary intake.

Priority primary sources mapped by the review:

- Yong et al. 2018, *Grifola frondosa* in hyperuricemic mice, DOI `10.1016/j.jff.2017.11.049`.
- Xiong et al. 2025, *Lentinula edodes* polysaccharide-protein complex via gut-kidney axis, DOI `10.1016/j.ijbiomac.2024.139370`.
- Zhou et al. 2022, *Phellinus igniarius* in vitro TLR4/NF-kB/NLRP3, DOI `10.3389/fphar.2022.1011406`.
- Li et al. 2021, *Phellinus igniarius* in hyperuricemia and acute gouty arthritis rat models, DOI `10.3389/fphar.2021.801910`.
- Chen et al. 2023, *Phellinus igniarius* total flavonoids, DOI `10.1016/j.heliyon.2023.e12979`.
- Sun et al. 2022, *Sanghuangporus vaninii* and *Inonotus hispidus* rodent hyperuricemia/gout, DOI `10.3390/nu14204421`.
- Lin et al. 2022, *Ganoderma lucidum* polysaccharide peptide, DOI `10.1039/d2fo02431d`.
- Huang et al. 2022, submerged culture of *Ganoderma lucidum* in PO-induced hyperuricemic rats, DOI `10.3390/metabo12060553`.
- Yong et al. 2018, cordycepin from *Cordyceps militaris* through URAT1 in hyperuricemic mice, DOI `10.3389/fmicb.2018.00058`.

The open Ganoderma polysaccharide review supports the P0-4 interpretation that Ganoderma is mainly an immunology/gut-barrier background lead at this stage. It emphasizes immune modulation, gut microbiota regulation, TLR signaling, Dectin-1 / TLR2 / TLR4 receptor engagement, downstream NF-κB/MAPK/PI3K-Akt pathways, IL-1β maturation via inflammasome-adjacent signaling, and colon-level microbiota/SCFA/barrier effects. It did not contain the string `NLRP3`, so it should not be cited as direct NLRP3 evidence.

## Implication

P0-4 should stay discovery-mixed:

- **Promote as source-map priority:** edible-mushroom HUA/gout review, now full-text read locally with Codex/GPT-5.5 and DeepSeek agreement.
- **Promote as mechanistic-background context only:** Ganoderma polysaccharide immunomodulation/gut-barrier literature.
- **Do not promote as direct gout/NLRP3 efficacy evidence:** Lingzhi spore powder, Yun Zhi PSP/PSK, Maitake/Grifola, or beta-glucan comparators from this pass.

## Next retrieval move

No wiki evidence-tier update from the review itself. Use the mapped bibliography to prioritize primary-source reads:

1. *Grifola frondosa* 2018 for the maitake/URAT1 question.
2. *Lentinula edodes* 2025 for dietary-mushroom/gut-kidney transporter coverage.
3. *Ganoderma lucidum* polysaccharide peptide and submerged-culture studies for Ganoderma-specific urate lowering.
