# comp-015 — T-axis Adjuvant Urate-Target Mapping (v2)

## Question

For each of four T-axis-active natural compounds (cordycepin, eurycomanone, icariin, echinacoside), what is the curated bioactivity evidence at the **five** dominant urate-handling targets (URAT1, ABCG2, OAT1, SHBG, **XO** — added v2), and which compound is the most gout-favorable T-axis adjuvant?

## v1 → v2 change (2026-05-07)

Added xanthine oxidase (XO/XDH, CHEMBL1929, UniProt P47989) as 5th target. v1 4-target panel was systematically incomplete because XO — the upstream urate-PRODUCTION enzyme that allopurinol/febuxostat target and that classical TCM gout compounds modulate — was excluded. Trigger: parallel Sci-Hub-second-pass verification subagent on `wiki/androgen-natural-modulation.md` discovered eurycomanone-related XO claims (PMID 31920654 / 34785103) — which on closer reading actually establish multi-target transporter + purine-synthesis modulation for eurycomanone, NOT direct XO inhibition. But adding XO was still correct (panel completeness), AND the v2 re-read of those primary sources surfaced previously-missed eurycomanone × URAT1/ABCG2/OAT1 evidence that v1's PubMed search did not find. **v2 dual contribution: panel completeness (XO column) + eurycomanone evidence reversal (v1 GOUT-UNFAVORABLE → v2 GOUT-FAVORABLE).** H-AN-02 status: v1 SUPPORTED → v2 PARTIALLY FALSIFIED.

## Hypothesis under test

**H-AN-02** (from [`androgen-natural-modulation.md`](../../wiki/androgen-natural-modulation.md) §10): *Cordycepin is uniquely positioned as a gout-favorable T-axis adjuvant — its T-elevation effect is small, but its URAT1 modulation works opposite to the URAT1 upregulation that high T usually produces. Predicted: net UA effect favorable or neutral despite T elevation.*

This experiment falsifies or strengthens H-AN-02 by mapping all four T-axis adjuvants against the urate transporter axis in silico, BEFORE any wet-lab spend.

## Method (target shape)

1. **ChEMBL bioactivity lookup** for each compound × target pair (UniProt → ChEMBL target → curated bioactivity records). Per the [`chembl-cross-check.md`](../../wiki/chembl-cross-check.md) discipline, this distinguishes "claimed mechanism" from "curated nanomolar binding."
2. **Literature-claim aggregation** for compound × target pairs where ChEMBL coverage is sparse (common for natural products at transporter targets — comp-013 found 5 of 9 TCM compounds had no ChEMBL records at all). Animal-model in vivo dose-response data is admissible per the comp-013 methodology adaptation.
3. **Achievable-concentration check** — for each compound, compute serum + gut-luminal concentration ranges based on oral dose × bioavailability × plausible distribution. Compare to the IC50/Ki at each target. The comp-007 pattern: a 100× achievable/Ki ratio is "decisively active"; <10× is "concentration unclear"; <1× is "below threshold."
4. **Direction-of-effect tagging** — inhibitor / inducer / substrate / unknown for each compound × target.
5. **Net-UA verdict per compound** based on aggregated evidence: gout-favorable / gout-neutral / gout-unfavorable / mechanism-unclear.

## Files

- `analyze.py` — stdlib-only analysis script (Python 3); reproduces all `outputs/` from `inputs/`.
- `inputs/compounds.json` — 4 compounds with PubChem CIDs, ChEMBL IDs, MW, oral bioavailability ranges from primary literature.
- `inputs/targets.json` — 4 targets with UniProt accessions, ChEMBL target IDs, gout-mechanism role.
- `inputs/chembl_bioactivity.json` — pre-fetched ChEMBL records for compound × target pairs (date-stamped, per-record provenance).
- `inputs/literature_claims.json` — non-ChEMBL evidence (animal models, primary papers) per compound × target.
- `inputs/concentration_estimates.json` — per-compound achievable serum + gut-luminal concentrations with primary-source citations.
- `inputs/provenance.md` — every input source (URL, fetch date, paper PMID) for reproducibility.
- `outputs/results.json` — machine-readable per-compound × target matrix + verdicts.
- `outputs/summary.md` — human-readable; the artifact cited in the wiki page.

## Cross-references

- [`wiki/t-axis-adjuvant-urate-mapping-computational.md`](../../wiki/t-axis-adjuvant-urate-mapping-computational.md) — interpretive wiki page.
- [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — comp-015 entry in tracking index.
- [`wiki/androgen-natural-modulation.md`](../../wiki/androgen-natural-modulation.md) §10 H-AN-02 — the falsifiable hypothesis this experiment tests.
- [`wiki/medicinal-mushroom-complement-track.md`](../../wiki/medicinal-mushroom-complement-track.md) — cordycepin URAT1 modulation evidence (337→203 µmol/L animal data) referenced as the prior.
- [`experiments/comp-013-tcm-gout-compound-triage/`](../comp-013-tcm-gout-compound-triage/) — methodological precedent (compound × chokepoint mapping with verdict tagging).
- [`experiments/comp-014-medicinal-mushroom-compound-mapping/`](../comp-014-medicinal-mushroom-compound-mapping/) — methodological precedent (breadth aggregation + chokepoint intersection).

## Reproduction

```bash
cd experiments/comp-015-t-axis-adjuvant-urate-mapping
python3 analyze.py
# Verify outputs/results.json and outputs/summary.md regenerate identically.
```

Python 3 stdlib only (json, pathlib). No `pip install` required.
