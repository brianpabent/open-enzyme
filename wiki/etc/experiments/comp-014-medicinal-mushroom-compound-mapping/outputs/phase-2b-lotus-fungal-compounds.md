# Phase 2b — LOTUS fungal-compound aggregation

**Source:** LOTUS REST API (https://lotus.naturalproducts.net/api/search/simple)
**Date:** 2026-05-06
**Queries run:** 56 fungal genera/species
**Total records seen:** 9,409
**Unique compounds (by InChIKey):** 6,798
**Unique species/taxa with compound attributions:** 55

## Top 30 species by compound count

| Rank | Species | Compound count |
|---:|---|---:|
| 1 | *[query-hint] Ganoderma* | 1,938 |
| 2 | *[query-hint] Ganoderma lucidum* | 914 |
| 3 | *[query-hint] Aspergillus terreus* | 457 |
| 4 | *[query-hint] Lactarius* | 380 |
| 5 | *[query-hint] Ganoderma applanatum* | 341 |
| 6 | *[query-hint] Aspergillus niger* | 302 |
| 7 | *[query-hint] Phellinus* | 292 |
| 8 | *[query-hint] Cordyceps* | 283 |
| 9 | *[query-hint] Fomitopsis* | 282 |
| 10 | *[query-hint] Penicillium chrysogenum* | 240 |
| 11 | *[query-hint] Russula* | 232 |
| 12 | *[query-hint] Hericium* | 224 |
| 13 | *[query-hint] Agaricus* | 221 |
| 14 | *[query-hint] Wolfiporia* | 219 |
| 15 | *[query-hint] Ophiocordyceps* | 200 |
| 16 | *[query-hint] Hericium erinaceus* | 194 |
| 17 | *[query-hint] Cyathus* | 186 |
| 18 | *[query-hint] Inonotus* | 186 |
| 19 | *[query-hint] Polyporus* | 145 |
| 20 | *[query-hint] Cordyceps sinensis* | 140 |
| 21 | *[query-hint] Trametes* | 123 |
| 22 | *[query-hint] Flammulina* | 118 |
| 23 | *[query-hint] Hypholoma* | 118 |
| 24 | *[query-hint] Pleurotus* | 114 |
| 25 | *[query-hint] Suillus* | 114 |
| 26 | *[query-hint] Antrodia* | 111 |
| 27 | *[query-hint] Inonotus obliquus* | 108 |
| 28 | *[query-hint] Aspergillus oryzae* | 107 |
| 29 | *[query-hint] Ganoderma sinense* | 101 |
| 30 | *[query-hint] Auricularia* | 99 |

## Notable findings

- The `[query-hint]` prefixed species are records where LOTUS did not attach explicit organism metadata, so we attribute by the query name. Real-species records (without prefix) take precedence and are higher confidence.
- Per-InChIKey full compound table at `phase-2b-compounds-by-inchikey.json` — Phase 3 target mapping reads from this.

## Caveats

- LOTUS aggregates upstream sources (NPAtlas, Wikidata-fed, etc.); some compounds may have weak species-of-origin evidence in the underlying primary literature.
- Same-genus searches (e.g., 'Ganoderma') may have returned compounds attributed to multiple Ganoderma species; we capture all attributions via the .organisms field.
- The 200-limit per query may have truncated very-rich species (Ganoderma lucidum had 28MB returned, suggesting 200 records returned for many queries — re-running with limit=2000+ would expand coverage).
- No toxicity filter applied yet — that's the next step (Phase 2 toxicity-filter pass).
