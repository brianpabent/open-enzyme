---
title: P0-4 edible mushroom / Ganoderma source-map note
date: 2026-05-20
status: retrieval-partial
---

# P0-4 edible mushroom / Ganoderma source-map note

## Retrieval status

The P0-4 CNKI rerun nominated two useful source-map leads:

1. `Reevaluating the Purine Controversy and Health Effects of Edible Mushroom: Multidimensional Regulatory Mechanisms in Hyperuricemia and Gout Risk Management` (2025, *Food Science*, DOI `10.7506/spkx1002-6630-20250617-117`).
2. `Research Advances in the Structure Feature and Immunomodulatory Mechanisms of Ganoderma lucidum Polysaccharides` (2026, *Journal of Shanxi Agricultural Sciences*).

For the first lead, the public *Food Science* article page is visible at [`https://www.spkx.net.cn/EN/10.7506/spkx1002-6630-20250617-117`](https://www.spkx.net.cn/EN/10.7506/spkx1002-6630-20250617-117), and AGRIS/DOAJ exposes a PDF URL at [`https://www.spkx.net.cn/fileup/1002-6630/PDF/2025-46-24-040.pdf`](https://www.spkx.net.cn/fileup/1002-6630/PDF/2025-46-24-040.pdf). However, local curl from the laptop currently fails to connect to `www.spkx.net.cn` / `spkx.net.cn` at `218.245.60.46` on ports 80 and 443. The web fetch path can read the abstract page, while the PDF URL returned HTTP 403 through the web fetch path. Operationally, add `spkx.net.cn` and `www.spkx.net.cn` to the China-literature firewall allowlist before treating this as a reproducible local full-text route.

For the second lead, the exact CNKI journal article remains CNKI-full-text-bound. A close open-access English review is available as Wu et al. 2025, `Structure-function insights of natural Ganoderma polysaccharides: advances in biosynthesis and functional food applications`, *Natural Products and Bioprospecting*, DOI `10.1007/s13659-025-00496-w`.

## Source-map read

The *Food Science* 2025 article is review-level, not primary evidence. The public abstract says it reviews mushroom consumption, serum uric acid, gout risk, and mechanisms by which medicinal/edible mushroom bioactives may affect uric-acid metabolism and gout pathogenesis. That makes it valuable as a source map for primary studies, but not enough to promote an evidence tier.

The open Ganoderma polysaccharide review supports the P0-4 interpretation that Ganoderma is mainly an immunology/gut-barrier background lead at this stage. It emphasizes immune modulation, gut microbiota regulation, TLR signaling, Dectin-1 / TLR2 / TLR4 receptor engagement, downstream NF-κB/MAPK/PI3K-Akt pathways, IL-1β maturation via inflammasome-adjacent signaling, and colon-level microbiota/SCFA/barrier effects. It did not contain the string `NLRP3`, so it should not be cited as direct NLRP3 evidence.

## Implication

P0-4 should stay discovery-mixed:

- **Promote as source-map priority:** edible-mushroom HUA/gout review, once full PDF is locally reachable.
- **Promote as mechanistic-background context only:** Ganoderma polysaccharide immunomodulation/gut-barrier literature.
- **Do not promote as direct gout/NLRP3 efficacy evidence:** Lingzhi spore powder, Yun Zhi PSP/PSK, Maitake/Grifola, or beta-glucan comparators from this pass.

## Next retrieval move

Whitelist:

- `spkx.net.cn`
- `www.spkx.net.cn`

Then retry:

```bash
curl -L -A 'OpenEnzyme-lit-synthesis/1.0 (local curl; Brian laptop egress)' \
  -o /tmp/oe-p0-4/edible-mushroom-hua-gout-2025.pdf \
  https://www.spkx.net.cn/fileup/1002-6630/PDF/2025-46-24-040.pdf
```

If the PDF downloads, run `pdftotext` and do a two-model Chinese-source read before extracting primary-study leads or changing any wiki evidence tier.
