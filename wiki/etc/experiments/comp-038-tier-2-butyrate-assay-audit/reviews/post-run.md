ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: dfa4849dc75254846279d996a3c296fc488b3595c5c02728051da578d76cfcb2

# Independent comp review — comp-038

## Reviewed snapshot

Reviewer `/root/comp038_gate2_clean`; authoring post-run manifest SHA-256 `dfa4849dc75254846279d996a3c296fc488b3595c5c02728051da578d76cfcb2`. All 21 manifest entries matched their recorded SHA-256. The six design files are byte-identical between the pre-run and post-run manifests. All six generated outputs and nine proposed updates were inspected.

## Bottom-line verdict

**Clean with limitations.** The repair retracts the unsupported blanket full-text claim, preserves only source-reconstructable details, distinguishes the two matrices and validation tracks, and does not upgrade published method performance into Open Enzyme qualification. The queue item may be deleted.

## Implementation and constraint closure

This is a static forensic source-verification repair, not a result-bearing computation. The frozen design explicitly excludes execution of `analyze.py` and a renewed literature search.

The implementation closes the relevant analytical constraints:

- De Baere is limited to primary-abstract scope.
- Gu is limited to its complete hardware–chemistry–model stack and a within-study independent test cohort.
- HPLC-UV culture-supernatant transfer and electrochemical/ANN stool transfer remain separate.
- Published validation does not establish another matrix, laboratory, operator, cohort, analyte, clinical use, gout outcome, exposure, or safety.
- Unsupported “underivatized,” July 14 verification, both-sources-full-text, and external-replication interpretations are retracted.
- The YELLOW verdict remains bounded to candidate identification and empirical transfer gates.

The legacy discovery runner, packet, and PubMed snapshot remain historical inputs rather than authority for the corrective claims. The hidden `.gitkeep` contains a legacy placeholder comment but supplies no scientific claim and does not affect interpretation.

## Summary-fidelity audit

The structured verification map, `results.json`, concise summary, README, focused evidence page, computational registry, open-question entry, quantification ladder, and validation protocols agree on:

- no ready-to-adopt Tier 1 or Tier 2 Open Enzyme butyrate method;
- De Baere as an abstract-supported Tier 3 HPLC-UV culture-supernatant transfer candidate;
- Gu as a full-text-supported Tier 2 stool candidate requiring complete-stack reproduction and independent external transfer;
- no categorical electrochemical failure;
- no cross-matrix or clinical inference.

The README uses current tense and accurately describes a completed repair. The computational registry contains no repair, sweep, drift, or maintenance narration. The literature receipt explicitly includes `wiki/quantification-ladder.md` in `canonical_updates`.

Validation §1.31 owns culture-supernatant HPLC-UV qualification against GC-MS. Validation §1.45 separately owns stool electrochemical/ANN reproducibility and transfer. Neither protocol borrows the other method’s evidence.

## Reader-facing ownership audit

The focused page leads with the measurement weakness, separates production, sampled exposure, and mechanism, then presents matrix-specific sourcing, limitations, and falsification gates. It contains no chassis foil, portfolio ranking, personalized treatment instruction, or editorial history.

Cross-track process lessons remain in the operations document. The index and navigation changes are discoverability-only. The computational registry presents the current scientific result without narrating the corpus repair.

## Conjecture preservation audit

No useful conjecture was deleted merely for lacking direct evidence. The repair corrects factual and historical claims while preserving both testable assay paths.

The negative boundaries are narrow:

- the bounded May search did not establish a qualifying SCFA/ELISA comparison;
- breath hydrogen/methane is not a butyrate-specific assay;
- the reviewed generic free-fatty-acid class is unsuitable for this use;
- the two published candidates are not yet qualified for Open Enzyme.

These findings do not rule out another lower-cost assay, another electrochemical design, future matrix transfer, or direct Tier 3 measurement.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `outputs/.gitkeep` | generated_output | Yes | Legacy placeholder only; no scientific claim. |
| `outputs/codex-synthesis-packet.md` | generated_output | Yes | Frozen May discovery packet; abstract-level and not authority for the repair. |
| `outputs/primary-source-verification-2026-07-24.json` | generated_output | Yes | Complete claim-level source/access/disposition map. |
| `outputs/pubmed-snapshot.json` | generated_output | Yes | Frozen 74-record May snapshot; discovery scope only. |
| `outputs/results.json` | generated_output | Yes | Separates May scan, unsupported July addendum, and July 24 verification. |
| `outputs/summary.md` | generated_output | Yes | Concise, source-specific, and matrix-specific YELLOW summary. |
| `index.md` | proposed update | Yes | Adds a neutral discoverability entry. |
| `logs/lit-scans/comp-038-primary-source-verification-2026-07-24.json` | proposed update | Yes | Compact reproducibility receipt; quantification ladder is listed. |
| `mkdocs.yml` | proposed update | Yes | Navigation label only. |
| `operations/agentic-science-adoption.md` | proposed update | Yes | Correctly separates literature search from executable COMPs. |
| `wiki/computational-experiments.md` | proposed update | Yes | Current result without maintenance narration. |
| `wiki/open-questions.md` | proposed update | Yes | Preserves matrix-specific measurement gaps and next gates. |
| `wiki/quantification-ladder.md` | proposed update | Yes | Correct Tier 3/Tier 4 classification and separate stool candidate. |
| `wiki/tier-2-butyrate-assay-audit-computational.md` | proposed update | Yes | Focused evidence home is accurate and self-contained. |
| `wiki/validation-experiments.md` | proposed update | Yes | §1.31 and §1.45 are distinct, prespecified transfer paths. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| De Baere matrix, 210 nm, ether extraction, pH below 2, 0.5–50 mM calibration | Claim map `DB13-*`; summary; §1.31 | Defines culture-transfer candidate | PMID 23542733; DOI; EPA HERO primary-abstract reproduction | Verified at abstract scope |
| De Baere LOD/LOQ 0.13–0.33/0.5–1.0 mM | `DB13-LIMITS` | Bounds analytical expectations | Primary abstract; endpoints not assigned to butyrate | Verified with analyte-spanning limitation |
| “Underivatized” | `DB13-UNDERIVATIZED` | Prevents unsupported protocol shorthand | Not explicit in accessible source | Retracted |
| Gu hardware and electrodes | `GU26-HARDWARE` | Defines non-interchangeable implementation | PMCID PMC13114974 §2.2 | Verified |
| Gu KOH pretreatment and acquisition | `GU26-PRETREATMENT`, `GU26-ACQUISITION` | Defines complete-stack reproduction | Full text §§2.5–2.6 | Verified |
| Gu fecal cohort n=30 versus GC-MS | `GU26-COHORT` | Defines source-study validation scope | Full text §3.3 and Table 2 | Verified; not external replication |
| Gu MAE/RMSE/R² 0.029/0.034 mM/0.998 | `GU26-BUTYRATE-PERFORMANCE` | Performance prior for §1.45 | Figure 5d and Table 3 | Verified |
| Gu bias −0.015 mM; limits −0.065 to 0.035 mM; p-values 0.0027/0.0031 | `GU26-BIAS` | Prevents reliance on R² alone | §3.3, Figure S5, Table S3 | Verified |
| 24/30 within ±5% | `GU26-PERCENT-AGREEMENT` | Supplemental agreement context | Full text §3.3 | Verified |
| July 14 full-text pass of both sources | `JULY14-FULLTEXT-PASS`, `BOTH-FULLTEXT-VERIFIED` | Historical/source-access correction | Git and artifact history | Retracted |
| Published method equals OE qualification | Results decision object and both validation sections | Prevents adoption or efficacy inflation | Explicit design and source boundaries | False |

## Affected wiki pages

- `wiki/tier-2-butyrate-assay-audit-computational.md` — already consistent — owns current evidence and falsification gates.
- `wiki/computational-experiments.md` — already consistent — concise registry entry with no maintenance narration.
- `wiki/open-questions.md` — already consistent — preserves the matrix-specific gap.
- `wiki/quantification-ladder.md` — already consistent — HPLC-UV is Tier 3; stool electrochemical/ANN remains separate.
- `wiki/validation-experiments.md` — already consistent — §1.31 and §1.45 separate culture and stool qualification.
- `index.md` — already consistent — discoverability only.
- `operations/agentic-science-adoption.md` — already consistent — process boundary, not reader-facing scientific evidence.
- `mkdocs.yml` — already consistent — navigation only.

## New connections or implications

The repair exposes an operationally useful division of labor: culture-supernatant HPLC-UV can answer production QC without waiting for a low-cost stool method, while the electrochemical/ANN stack can be evaluated independently for longitudinal fecal monitoring. Neither track needs to block the other, and neither substitutes for target-compartment exposure or mechanistic readouts.

## Required actions

1. None. The synthesis queue item may be deleted.

## Review limits

I did not execute `analyze.py`, rerun the May search, broaden the two-source set, or independently reproduce the Gu model. De Baere verification remains limited to its accessible primary abstract. Gu’s published performance remains a within-study result without external replication or Open Enzyme qualification.
