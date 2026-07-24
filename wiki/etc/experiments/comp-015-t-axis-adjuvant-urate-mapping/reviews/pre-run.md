PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 579361004668254795602fca0dfd20914470cf72ea8ee5fd308a6ef234673ae7

# Independent Gate 1 review — COMP-015 retirement

**Reviewer:** `/root/comp044_pre_review_v20`  
**Reviewed snapshot:** `579361004668254795602fca0dfd20914470cf72ea8ee5fd308a6ef234673ae7`

The exact two-file retirement snapshot passed integrity and scope review. The
tombstone README and invalidation ledger match the manifest. All ten retired
non-review files match their recorded sizes and SHA-256 hashes at commit
`b6ca51a489e4ac321fda5f7a1f2e073d884ae0b7`, and the retirement-set digest
recomputes to
`949f3d93a6b1a57fc677939bfe9a9b33080409dd0e1b93cee7096ff432bb06d1`.

The retirement boundary is appropriately narrow and non-runnable. It
invalidates the code, inputs, outputs, matrix-derived verdicts and rankings,
evidence counts, heuristic exposure calculations, false COMP-007 threshold
attribution, material substitutions, and predictive use while retaining Git
provenance.

The source-specific survivors match the primary records:

- Purified cordycepin at 15, 30, and 60 mg/kg supports an unranked
  **Animal Model** URAT1/urate lead, not human exposure, efficacy, or a dual
  androgen benefit (PMID 29422889).
- The 2019 study distinguishes a 70% ethanol *Eurycoma longifolia* stem
  extract, eurycomanol-type compounds 4–7 with hURAT1 activity at 50 µM, and
  comparatively low-activity pure eurycomanone as compound 3. The extract or
  compounds 4–7 result cannot be transferred to pure eurycomanone
  (PMID 31920654; PMC6914847).
- Purified eurycomanol at 5–20 mg/kg orally supports a source-specific
  **Animal Model** urate-clearance, PRPS-expression, and transporter lead, not
  human efficacy or a Physta mechanism (PMID 34785103).
- Physta's urate measurements appear in a safety laboratory table. Week-12
  comparisons versus placebo were null at both doses (`p=0.88`, `p=0.52`);
  the study supplies neither urate efficacy nor a mechanistic bridge to
  eurycomanone or eurycomanol (PMC8254464).

The surviving Research Conjecture is explicitly untested, requires
exact-material identity and measured exposure, and makes no comparative
ranking or decision claim. The named correction cascade captures the active
reader-facing and decision-bearing uses found by the repository-wide search.
COMP-017 retains its own lifecycle gate, followed by a repository readback,
exact Gate 2 review, and same-commit queue deletion.

No required pre-authoring correction remains.
