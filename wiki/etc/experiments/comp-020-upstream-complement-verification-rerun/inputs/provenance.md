# comp-020 provenance + methodology notes

## Independence defect (load-bearing)

The agent did not directly inspect comp-018 / comp-019 output files, but the
brief embedded prior exclusions, named comparators, and an empty-class
conclusion in `target-nodes.json`. The run was therefore not independent and
cannot be used as a context-isolated confirmation.

The intended second-opinion comparison was not achieved. The retained value is
limited to query and source provenance that must be reverified before reuse.

## Pre-commit verification gate compliance (CLAUDE.md Rule 4)

The historical run recorded the following verification attempts. This table is
not exhaustive, and the quarantine does not treat any listed or unlisted value
as currently verified. Reuse requires a fresh primary-source check:

| Number | Paper | Verification anchor |
|---|---|---|
| Helicteres compound 5 CH50 0.009 ± 0.002 mM | PMC6273495 | grep result line 18 (verbatim from paper) |
| Helicteres compound 4 CH50 0.040 ± 0.009 mM | PMC6273495 | grep result line 18 |
| Luteolin CH50 0.19 mM, AP50 0.17 mM | PMC7126446 | grep result line 10 + Table 1 |
| Heparin LP 2 / CP 39 / AP 76 μg/mL | PMC7212410 | grep result line 45 |
| Heparin tetrasaccharide LP IC50 21 μg/mL | PMC7212410 | grep result line 45 |
| Bupleurum BCPs LP 0.098 mg/mL | PMC4629277 | grep result line 46 |
| Bupleurum BPs LP 1.057 mg/mL | PMC4629277 | grep result line 46 |
| Marine fucoidan ANW IC50 0.98 μg/mL | PMC4728500 | grep result line 39 |
| Marine SJW-3 IC50 3.11 μg/mL | PMC4728500 | grep result line 23 |
| Ligusticum LCP-I-I ICH50 26.3 ± 2.2 μg/mL | PMC6155779 | grep result line 18 |
| Rosmarinic-acid complement records | PMID 10353266 (Sahu 1999), 1761351 (Peake 1991), 3198307 (Englberger 1988) | Search-result snippets only; quantitative values withheld and non-citable pending primary-full-text verification |

The rosmarinic-acid values were extracted from search-result text rather than
primary full text. Other values absent from this table have no retained
verification receipt. The artifact-wide quarantine is the controlling status.

## Anti-pattern guard (DAF SCR1-4 disulfide-count incident)

The historical run attempted line-level verification for some values, but it
did not retain a complete verification receipt and the rosmarinic-acid values
came from search-result text. The artifact therefore does not satisfy the
current pre-commit gate. The DAF SCR1-4 disulfide incident motivated the gate;
it does not retroactively validate this run.

## Multilingual scope — partial execution disclosure

The CLAUDE.md §Global-multilingual research by default rule requires non-English sources to be scanned alongside PubMed. In this re-run:

- **Executed:** English-language scans, including English-journal publications by China-based groups.
- **Incomplete:** Chinese-keyword web searches were attempted, but CNKI, WanFang, J-STAGE, KISS/RISS, eLIBRARY.RU, and other relevant regional primary-source searches were not completed. English publication by a regional research group does not mitigate or measure this coverage gap.
- **Phase 2 follow-up explicitly flagged:** dedicated CNKI/WanFang Chinese-keyword query (补体抑制剂, 经典途径, 旁路途径, 凝集素途径) + J-STAGE Kampo query (補体 + 漢方医学) + KISS Korean query.

This partial-execution disclosure is per CLAUDE.md §Pre-commit verification gate — flag what was NOT done, don't paper over it.

## ChEMBL spot-check — quarantined

The historical run recorded several compound identifiers and informal
non-retrievals, but retained neither a reproducible query census nor an
immutable ChEMBL snapshot. It supports no coverage rate, systematic absence,
structural-bias conclusion, or cross-target comparison. Any identifier may only
seed a fresh dated query.

## What this re-run does NOT do

- Does NOT propose comp-NNN follow-ups to wet-lab any specific compound (recommendations are Phase 2 candidate flags, not gating decisions)
- Does NOT triage compounds by gut-luminal tractability (that's the comp-004/comp-013 framework, separate)
- Does NOT propose engineering routes (e.g., koji biosynthetic pathway expression of rosmarinic acid)
- Does NOT recommend supplements or clinical actions (Phase 0 — Research & Design)
