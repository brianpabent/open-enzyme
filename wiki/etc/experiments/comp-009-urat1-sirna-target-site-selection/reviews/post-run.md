ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 9172b45ec49760f2286ef53a2d1679ac017a6d98c82cc0da9dd409fbad40a8ef

# Independent comp review — comp-009

## Reviewed snapshot

Reviewer: `/root/comp009_retirement/comp009_gate2_final3`.

The canonical manifest digest is exactly `9172b45ec49760f2286ef53a2d1679ac017a6d98c82cc0da9dd409fbad40a8ef`. I independently recomputed and verified every path, byte count, and SHA-256 for all 14 bound files. No unbound file is needed to interpret the retirement.

I also reconstructed the retired artifact from Git commit `b6ca51a489e4ac321fda5f7a1f2e073d884ae0b7`, verified all 10 historical blobs against `invalidation.json`, and reproduced its canonical tree digest exactly: `5d53e3d4972f61cb043c9b955d1b3316ad46c1f54e32c9bcdfc415b7ed6d08aa`.

## Bottom-line verdict

Clean.

The artifact-summary-corpus contract is internally consistent. COMP-009 is fully retired as a source of guide sequences, counts, ranks, composite scores, GREEN status, target availability, accessibility, specificity, tractability, H03 support, or P2-2 closure. The surviving URAT1-siRNA hypothesis is preserved without relying on those invalid premises, and COMP-048 is now the valid first gate.

## Implementation and constraint closure

The retirement is justified by the historical implementation and closes the relevant defects:

- **Reynolds rules:** The historical code reverse-complemented the target and evaluated positions on the antisense sequence, although the cited criteria concern sense-strand positions and terminal asymmetry. Its “R2” substitute—a no-four-base-run check—did not implement the cited low sense-strand 3′ terminal stability or inverted-repeat constraints. This mismatch is confirmed against [Reynolds et al.](https://pubmed.ncbi.nlm.nih.gov/14758366/).
- **Ui-Tei rules:** The implementation did not enforce the simultaneous four-part rule set. It weakened the first-seven antisense A/U requirement from five to four and omitted the required sense 5′ G/C condition and long-G/C-stretch exclusion. This is confirmed against the [Ui-Tei selection guidelines](https://ui-tei.rnai.jp/assets/files/pdf/Guidelines%20for%20the%20selection.pdf).
- **Accessibility:** Accessibility did not participate in filtering. All eight historical shortlisted sites had extremely low computed unpaired probabilities, ranging from zero to approximately `0.0047`, yet five or more shortlist entries alone produced GREEN.
- **Composite weighting:** The score was an unvalidated weighted sum in which protein conservation could contribute up to 30 points while accessibility contributed at most about 0.12 points among shortlisted candidates. This is neither a calibrated efficacy model nor a faithful RNAxs implementation. The comparison is consistent with [Tafer et al.](https://pubmed.ncbi.nlm.nih.gov/18438400/).
- **Off-target and transcript coverage:** The artifact lacked transcriptome-wide and 3′UTR off-target clearance and operated from a single transcript accession.
- **Cross-species reasoning:** Amino-acid conservation was used as a proxy for nucleotide-level guide reuse, which does not establish guide conservation.
- **Boundary handling:** The historical region classification mislabeled a site crossing the annotated CDS boundary as wholly 5′UTR.
- **Empirical closure:** No uptake, intracellular delivery, knockdown, urate-transport, durability, reversibility, or renal-safety result supported the historical feasibility verdict.
- **Declarative-versus-executed rules:** Most parameters in `design_parameters.json` were not actually consumed by the analysis; the JSON therefore overstated implementation completeness.
- **Model fit:** The computation could not answer the first unresolved question—whether a viable human proximal-tubule delivery handle and compatible architecture exist. Retirement, rather than rerun, is the correct disposition.

The tombstone is deliberately non-runnable and preserves the historical blobs only through immutable Git provenance.

## Summary-fidelity audit

The tombstone and all 12 proposed updates agree on the retirement’s scope:

- No historical or rerun COMP-009 guide is valid.
- No filter funnel, candidate count, rank, composite score, shortlist, GREEN verdict, accessibility claim, specificity claim, cross-species claim, or tractability conclusion survives.
- COMP-009 no longer supports H03 or closes P2-2.
- COMP-048 owns the first executable gate: delivery-handle and architecture selection.
- Guide design is explicitly downstream of a positive delivery result.
- The two historical-report corrections clearly withdraw the unsupported “≤50%” recommendation. They replace it with measured therapeutic-window requirements and state that human genetics supplies a safety boundary, not a universal dose or knockdown ceiling.
- The chassis and H03 pages also avoid unsupported quarterly dosing, cleaner-safety-profile, durability, and dose claims.
- Historical positive output remains available only as invalidated provenance, not as live scientific evidence.

The deleted `synthesis/queue/comp-review-009.md` contained eight action groups. Each is closed: live outputs and stale inputs were retired, reader-facing interpretation was replaced, H03/P2-2 routing was corrected, environment pinning became moot because the artifact is non-runnable, boundary defects are recorded, and future off-target/cross-species requirements now sit downstream of COMP-048. Deleting the queue item in this batch is appropriate.

## Reader-facing ownership audit

Ownership is coherent and economical:

- The COMP-009 experiment page owns the invalidation, provenance, and successor routing.
- The focused interpretive page explains why no COMP-009 scientific output survives.
- The modality page owns current evidence, limitations, and the delivery-first falsification program.
- H03 owns the surviving hypothesis and conjecture.
- `open-questions.md` and `todos.md` own P2-2/COMP-048 sequencing.
- `index.md`, the hypothesis index, and the computational-experiment registry remain concise discovery surfaces.
- The chassis comparison page limits itself to portfolio implications and does not use another track as a rhetorical foil.
- No page presents personalized treatment instructions, editorial-history narration, or an unsupported clinical recommendation.

## Conjecture preservation audit

The URAT1-siRNA Research Conjecture remains intact in H03 using the required structure and compact length:

- Grounded premises retain their evidence levels and provenance.
- The novel leap explicitly states that the complete causal chain lacks direct evidence.
- The potential benefit is stated conditionally.
- The discriminating observation starts with delivery, followed only conditionally by guide work and functional testing.

None of its premises depends on a COMP-009 sequence, score, rank, accessibility estimate, specificity assessment, tractability verdict, GREEN status, or P2-2 closure.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md` | design | Yes | Complete non-runnable tombstone; provenance and successor are explicit. |
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/invalidation.json` | design | Yes | Historical tree, blob hashes, canonical digest, invalidation bases, and successor verified. |
| `index.md` | proposed update | Yes | siRNA-2 correctly starts with COMP-048; guide selection is downstream. |
| `logs/multilingual-east-asian-gout-cohort-scan-2026-05-19.md` | proposed update | Yes | Unsupported ~50% ceiling clearly withdrawn. |
| `operations/global-lit-scan-p0-remediation-2026-05-20/outputs/p0-2-east-asian-gout-genetics-source-read-2026-05-20.md` | proposed update | Yes | Unsupported ≤50% guardrail replaced by empirical-window requirements. |
| `operations/operational-search-template.md` | proposed update | Yes | Partner trigger is delivery-first; no premature guide work. |
| `operations/todos.md` | proposed update | Yes | P2-2 routes to COMP-048; guide work is conditional. |
| `wiki/chassis-pending-interventions.md` | proposed update | Yes | No cleaner-safety or quarterly-dosing inference; COMP-048 is first gate. |
| `wiki/computational-experiments.md` | proposed update | Yes | COMP-009 is retired and all historical conclusions invalidated. |
| `wiki/hypotheses/H03-sirna-urat1-thesis.md` | proposed update | Yes | H03 survives without COMP-009 premises; no dose, interval, or guide claim. |
| `wiki/hypotheses/README.md` | proposed update | Yes | H03 index entry accurately reflects delivery-first status. |
| `wiki/open-questions.md` | proposed update | Yes | P2-2 is COMP-048; P2-2b guide work is deferred. |
| `wiki/sirna-urat1-modality.md` | proposed update | Yes | Evidence, limitations, safety boundary, and falsification sequence are accurate. |
| `wiki/urat1-sirna-target-site-selection-computational.md` | proposed update | Yes | Historical result is fully invalidated without preserving positive residue. |

There are no manifest-bound generated outputs. That is correct for a retirement artifact.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Canonical review digest | `post-run.manifest.json` | Binds 14 review files | Independently recomputed | Verified |
| Retired-tree commit and digest | `invalidation.json` | Binds 10 historical blobs | Git blobs and canonical JSON independently recomputed | Verified |
| Reynolds criteria were misimplemented | Historical `scripts/analyze.py` | Candidate scoring | Checked against primary publication | Supports invalidation |
| Ui-Tei criteria were incomplete/weakened | Historical `scripts/analyze.py` | Candidate scoring/filtering | Checked against primary guideline | Supports invalidation |
| Accessibility did not gate candidates | Historical code and outputs | Ranking/verdict | Direct code/output inspection | Supports invalidation |
| Composite weighting was unvalidated | Historical code | Rank ordering | Direct implementation inspection plus RNAxs primary comparison | Supports invalidation |
| Off-target/transcript/cross-species coverage was inadequate | Historical inputs/code | Specificity and portability claims | Direct implementation inspection | Supports invalidation |
| GREEN and availability were unsupported | Historical summary/output | Feasibility conclusion | No empirical or valid computational closure | Fully retired |
| No universal ≤50% knockdown recommendation | Two corrected historical reports, modality, H03 | Safety framing | Correction preserves human-genetic modality without inventing a percentage | Verified |
| COMP-048 is the successor first gate | Tombstone and active routing pages | Portfolio sequencing | Linked directory and README exist | Verified |

## Affected wiki pages

The active wiki surfaces are mutually consistent:

- `wiki/chassis-pending-interventions.md`
- `wiki/computational-experiments.md`
- `wiki/hypotheses/H03-sirna-urat1-thesis.md`
- `wiki/hypotheses/README.md`
- `wiki/open-questions.md`
- `wiki/sirna-urat1-modality.md`
- `wiki/urat1-sirna-target-site-selection-computational.md`
- the COMP-009 tombstone and invalidation record

Full-corpus searches found no active historical guide sequence, old or rerun candidate list, stale candidate count or score, surviving rank, GREEN verdict, guide-availability claim, accessibility/specificity/tractability claim, invalid H03 support, or false P2-2 closure. Safety, durability, dose, and interval searches found only the new corrective language or unrelated tracks.

COMP-048 resolves at the linked path. The H03 status link routes to the existing `Falsification program` section on the modality page, and the manual anchor check is valid.

## New connections or implications

No new scientific conjecture is introduced by the retirement. The operational implication is appropriately narrower: delivery-handle and architecture feasibility must be established before guide-selection computation can become decision-relevant.

## Required actions

None.

## Review limits

This was a static, context-isolated authoring review. I did not execute the retired model, as required. Primary-source comparison focused on the load-bearing Reynolds, Ui-Tei, and RNAxs method claims rather than conducting a new general siRNA literature scan.

The standing maintenance queue records 61 historical legacy link debts outside this batch. They are not attributable to COMP-009. All changed COMP-009 surfaces and the COMP-048/H03 routes are link-clean; in the current shared worktree, `scripts/check-links.py` also reports zero broken relative links.
