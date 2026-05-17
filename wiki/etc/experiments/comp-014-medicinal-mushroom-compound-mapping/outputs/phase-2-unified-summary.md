# Phase 2 unified — fungal compound aggregation (post-Phase-3 re-run)

**Date:** 2026-05-17  
**Total unique compounds (deduped by InChIKey):** 9,778

## Database coverage

| Source | Compounds attributed (any) | Reachable from sandbox? |
|---|---:|---|
| LOTUS | 6,798 | yes |
| NPAtlas | 4,535 | yes |
| KNApSAcK | 20 | yes |
| NPASS | 0 | no — bidd.group HTTPS 200 intermittently, then 000 timeouts; can't reliably scrape |
| TCMSP | 0 | no — old.tcmsp-e.com returns 502 Bad Gateway; alternate hosts unreachable |
| HIT | 0 | no — badd-cao.net hosts time out (000); known intermittent for months in upstream community reports |
| SwissTargetPrediction | n/a | no — no programmatic POST endpoint verified reachable |

## Toxicity filter (applied)

- Inclusion: GRAS / QPS / pharmacopoeia / clinical-trial / grey-zone → 9,747 compounds
- Hard-excluded (WHO 2022 / mycotoxin / Schedule I/II): 31 compounds
- Inclusion-OR / Exclusion-precedence rule per `inputs/toxicity-filter.json`.
- Grey-zone default = include with `safety_review_pending` flag (rule in toxicity-filter.json).

## Database coverage gap

Three East-Asian-hosted databases (NPASS, TCMSP, HIT) and the SwissTargetPrediction prediction service were *not* reachable from the comp-014 sandbox on 2026-05-17:

- **NPASS** (bidd.group / bidd-group.org): the root HTML responded `200` on one probe but subsequent attempts returned `000` / connection-failed. Documented intermittently-up in upstream community channels. Re-run plan: retry from a non-sandboxed environment, prefer the bulk-CSV download `NPASSv2.0_download_naturalProducts*.txt` rather than the dynamic web interface.
- **TCMSP** (old.tcmsp-e.com): `502 Bad Gateway` on `https://old.tcmsp-e.com/tcmsp.php`; the new tcmsp-e.com root returns empty body. Re-run plan: the legacy TCMSP appears to have been folded into the BATMAN-TCM-2 platform; retry via BATMAN-TCM endpoints, or use the published TCMSP bulk download archived at Mendeley Data.
- **HIT** (hit2.badd-cao.net + badd-cao.net): timeouts on both. Re-run plan: HIT 2.0 ships a downloadable Excel file (one-time human-confirmed download) per upstream paper PMID 35136829.
- **SwissTargetPrediction**: requires a POST with SMILES; not verified accessible from this sandbox. Re-run plan: from a connected environment, batch the target-orphan compound subset (~75-80% of the table) through the POST API or the bulk Stardust pipeline.

The existing LOTUS-only Phase 2 outputs are not wrong, just incomplete. The unified table here is LOTUS + NPAtlas + KNApSAcK; the East-Asian-DB gap is documented and slated for re-run.

## Anchor-species sanity check

All 18 anchor species from `inputs/phase-5-anchor-species.json` resolve in the unified table (every species has ≥1 attributed compound). Sanity-check passed; no pipeline bug detected.
