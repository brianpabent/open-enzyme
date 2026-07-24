ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: e324f71b8ca043a121f0b1f66d400abd0036184f97519566d93966fceca0a948

# Independent comp review — comp-022

## Reviewed snapshot

Reviewer: `/root/comp022_retirement_gate2_clean`. The canonical manifest digest
recomputed exactly, and all 11 entries matched their recorded byte counts and
SHA-256 hashes.

## Bottom-line verdict

Clean. COMP-022 is fully retired as ranking or component-selection authority.
All queue actions are closed, and deletion of
`synthesis/queue/comp-review-022.md` is authorized in this commit.

## Implementation and constraint closure

The live artifact is non-runnable. `invalidation.json` binds 26 retired files
at commit `5b0a548445bde2da5395be65fb8042f3b033a350`; every byte count and
SHA-256 matched that snapshot, and the invalidation digest recomputed exactly.

Static inspection confirmed:

- 43,200 is the historical `6 × 12 × 10 × 60` enumeration and is inventory
  only.
- The four historical v1-cluster rows have v2 concordance values 5, 4, 4, and
  4: 4/4 entered ≥4, while 1/4 entered =5.
- `esmfold_pLDDT.csv` came from single-pass ESM2 log probabilities rescaled to
  50–90, not ESMFold pLDDT or fold quality.
- Q00511 is 302 residues, contains `NFS` at 191–193, and terminates in `SKL`.
- No PTS1, N191Q, promoter, signal-peptide, codon, processing-route, terminal,
  propeptide, glycosylation, or exact-construct preference survives.
- Direct secretion, GlaA-KEX2 processing, and the other construct variables
  survive only as matched empirical factors. No successor ranking is proposed.

No retired model or result-bearing code was executed.

## Summary-fidelity audit

All manifest-bound surfaces agree on the retirement. COMP-048 remains limited
to surface-expression/topology follow-up candidates; receptor identity,
internalization, accessibility, ligand binding, and polarity remain
downstream. Operations no longer treats COMP-022 or COMP-032 rankings as
authority. `bio-ai-tools.md` reports the Paperclip arithmetic as approximately
7.5× and contains no personalized treatment prompt.

No active non-review surface retains open-review, strict-tier-confirmation,
rescued-shortlist, or equivalent stale authority language.

## Reader-facing ownership audit

The evidence page owns the invalidation boundary, surviving empirical factors,
and matched experiment. It contains no personalized treatment instructions,
page-placement narration, cross-track ranking residue, or duplicated ranking
exposition.

## Conjecture preservation audit

Retirement kills only the composite ranking, component preferences, and
derived routing claims. It does not reject UOX, *A. oryzae*, direct secretion,
carrier processing, or the wider portfolio. Useful construct variables remain
unranked empirical factors.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| COMP-022 `README.md` | design | Yes | Clean non-runnable tombstone |
| `invalidation.json` | design | Yes | Exact retired scope and hashes verified |
| `index.md` | proposed_update | Yes | COMP-022 and COMP-048 boundaries clean |
| `mkdocs.yml` | proposed_update | Yes | Retired label and target correct |
| `operations/agentic-science-adoption.md` | proposed_update | Yes | COMP-022/032 authority retired |
| Paper draft | proposed_update | Yes | PTS1 history correctly bounded |
| `wiki/computational-experiments.md` | proposed_update | Yes | Registry and planned table agree |
| `wiki/etc/autonomous-screening-methodology.md` | proposed_update | Yes | No rescued composite authority |
| `wiki/etc/bio-ai-tools.md` | proposed_update | Yes | Arithmetic and reader contract corrected |
| COMP-022 evidence page | proposed_update | Yes | Correct boundary and empirical gate |
| `wiki/validation-experiments.md` | proposed_update | Yes | Matched factors; no component ordering |

There are no generated outputs.

## Load-bearing verification table

| Claim | Verification | Verdict |
|---|---|---|
| Manifest digest | Independently recomputed | Verified |
| Retired artifact binding | 26 Git blobs rehashed | Verified |
| 43,200 rows | Historical factorization | Historical inventory only |
| 4/4 ≥4; 1/4 =5 | Historical v2 rows | Verified |
| ESM2, not pLDDT | Historical producer code | Verified |
| Q00511 `NFS` / `SKL` | FASTA and reviewed UniProt | Verified |
| No component preference | Current surfaces | Verified |
| Queue closure | Actions 1–8 reconciled | Authorized |

## Affected wiki pages

All manifest-bound wiki pages and `wiki/koji-endgame-strain.md` are consistent.

## New connections or implications

None found.

## Required actions

None.

## Review limits

Read-only static review. The retired model was not executed. Current Q00511
sequence identity was independently checked; other historical scientific
inputs were inspected only as invalidated provenance.
