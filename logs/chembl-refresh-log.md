# ChEMBL Quarterly Refresh Log

Append-only. One entry per quarterly refresh run. Dates in ISO-8601 (UTC).

---

## 2026-07-01 — Q3 Refresh (ChEMBL v34 → v37)

**Trigger:** Scheduled quarterly sweep (`event=schedule`, `ci=github-actions-chembl-quarterly`, `2026-07-01T12:59:22Z`)
**Executed by:** Claude Sonnet 4.6 (automated agent)
**ChEMBL version at time of refresh:** v37 (release date 2026-05-01; 24,527,044 activities; 2,921,148 compounds; 18,552 targets; up from v34 used in the 2026-04-24 baseline)
**API method:** REST API (`https://www.ebi.ac.uk/chembl/api/data/`); MCP plugin unavailable

### Compounds Re-Queried (Pass 1 — Baseline Compounds)

17 baseline compounds re-queried against ChEMBL v37.
- 15 returned results (pChEMBL-ranked activity data)
- 2 remain not indexed: KPV (peptide), Ergothioneine

| Compound | ChEMBL ID | Material change vs. v34 baseline? |
|---|---|---|
| Quercetin | CHEMBL50 | No — 5-LOX entry (J Med Chem 1991, 300 nM) still present; DPPH antioxidant assay now ranks #1 by pChEMBL (non-protein target; excluded from pharmacological interpretation) |
| Oridonin | CHEMBL1164920 | Minor — 3 new 2024 percent-inhibition entries in human THP-1 added; IC50 5.18 μM unchanged |
| Dapansutrile | CHEMBL3989943 | No — baseline confirmed |
| β-Caryophyllene | CHEMBL445740 | **Yes (minor)** — CB2 Ki 150 nM now curated in ChEMBL v37 (was external-literature-only at baseline) |
| BHB | CHEMBL1162496 | No |
| KPV | Not indexed | No |
| Carnosine | CHEMBL242948 | No |
| Ursolic acid | CHEMBL169 | **YES (MAJOR)** — 16 new curated entries pChEMBL ≥ 6 (zero in v34). Top: ROR-γ IC50 = 0.75 nM (J Med Chem 2023), SENP1 IC50 = 6.4 nM (Eur J Med Chem 2022), NF-κB IC50 = 31 nM (Bioorg Med Chem 2018) |
| Taurine | CHEMBL239243 | No |
| EGCG | CHEMBL297453 | Minor — PC-12 neuroprotection IC50 30 nM (Eur J Med Chem 2024) added at rank 5 |
| Sulforaphane | CHEMBL48802 | No |
| Berberine | CHEMBL295124 | Minor — dsDNA EC50 100 nM (J Nat Prod 2024) added at rank 4; TDO 30 nM and CYP1B1 44 nM confirmed |
| Resveratrol | CHEMBL165 | Minor — cell-line antiproliferative IC50s (HeLa, MCF7, etc.) now rank above DPP-4 by pChEMBL; DPP-4 IC50 0.6 nM unchanged at rank-5 molecular target |
| Curcumin | CHEMBL140 | **YES** — DYRK2 IC50 = 2.5 nM (J Med Chem 2023, pChEMBL 8.60) now rank-2 molecular target; not in v34 |
| Ergothioneine | Not indexed | No |
| Ferulic acid | CHEMBL32749 | Minor — CK2 Ki 410 nM (J Med Chem 2023) added at rank 5 |
| Kojic acid | CHEMBL287556 | Minor — mushroom tyrosinase INHIBITOR 1.0 nM (Eur J Med Chem 2023, activity_type "INHIBITOR" not IC50) noted; human tyrosinase IC50 7–10 μM unchanged |

### New Compounds Queried (Pass 2 — Stack Additions Since Baseline)

10 new stack compounds added to the cross-check file:

| Compound | ChEMBL ID | Notable finding |
|---|---|---|
| Theaflavin | CHEMBL346119 | Bcl-2 Ki 691 nM (sole curated hit); no NLRP3 |
| Zileuton | CHEMBL93 | 5-LOX IC50 840 nM confirmed (J Med Chem 1993); no NLRP3. Canonical ALOX5 = CHEMBL215 |
| Tranilast | CHEMBL415324 | Phenotypic screen hits: NPC1 ~89 nM, Rab-9A ~92 nM (null journal — unvalidated); no NLRP3 |
| Disulfiram | CHEMBL964 | LOXL4 IC50 59 nM (Bioorg Med Chem Lett 2018); ALOX15 potency 63 nM (phenotypic); no GSDMD; no NLRP3 |
| Limonene (D-) | CHEMBL449062 | No curated activity pChEMBL ≥ 6 |
| NAC | CHEMBL600 | ALOX15 potency 25 nM (phenotypic, null journal — unvalidated); COX-1 AC50 890 nM (Nat Commun 2023); no NLRP3 |
| Spermidine | CHEMBL19612 | CA4 Ki 112 nM (J Med Chem 2010); no NLRP3 |
| Vitamin D3 | CHEMBL1042 | VDR EC50 0.21 nM confirmed (Bioorg Med Chem Lett 2014); no NLRP3 (expected) |
| Eurycomanone | CHEMBL1171981 | No curated activity pChEMBL ≥ 6 |
| Talactoferrin alfa | CHEMBL2108651 | No curated bioactivity (biologic) |

### Summary

- **Total compounds in cross-check file after this refresh:** 27 (17 baseline + 10 new)
- **Material discrepancies surfaced:** 2
  1. Ursolic acid — 16 new curated entries pChEMBL ≥ 6 (ROR-γ at 0.75 nM; major)
  2. Curcumin — DYRK2 IC50 = 2.5 nM new rank-2 target (minor; single paper)
- **Status corrections:** 1 (β-Caryophyllene CB2 now ChEMBL-curated; was external-lit-only)
- **ChEMBL version advance:** v34 → v37 (+3 versions; ~9 months of curation)

### Files Modified

- `wiki/etc/chembl-cross-check.md` — updated master table (27 rows), all last-refreshed dates updated to 2026-07-01, 10 new compound rows added, ursolic acid and curcumin expanded findings sections added, β-Caryophyllene status corrected, ChEMBL version updated to v37, refresh cadence updated to next 2026-10-01
- `synthesis/queue/2026-07-01-chembl-discrepancy-1-ursolic-acid-ror-gamma.md` — new (ursolic acid ROR-γ major finding)
- `synthesis/queue/2026-07-01-chembl-discrepancy-2-curcumin-dyrk2.md` — new (curcumin DYRK2 minor finding)
- `logs/chembl-refresh-log.md` — created (this file)

### Commit

`chembl-refresh: quarterly sweep 2026-07-01 — 27 compounds, 2 discrepancies [skip-chembl-refresh] [skip-wiki-sweep]`

### Notes

- ChEMBL MCP plugin (`mcp__plugin_chembl_ChEMBL__*`) was unavailable; REST API used as fallback. No functional gap — the REST API covers all required endpoints (molecule, activity, status).
- Canonical ALOX5 target in ChEMBL is CHEMBL215, not CHEMBL2185 — note in refresh recipe.
- GSDMD (gasdermin D) is not meaningfully curated in ChEMBL for the compound class that uses it (covalent modifiers like disulfiram); the absence is expected and not a gap in the cross-check methodology.
- Phenotypic screen hits (null journal annotation) from the Broad/NIH HTS repositories appear in multiple compound profiles; these are treated as unvalidated until independently replicated in a named journal assay.
