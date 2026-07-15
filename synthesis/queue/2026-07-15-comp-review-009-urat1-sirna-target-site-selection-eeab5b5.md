---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-009
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-009

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-009-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-009-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-009

## Reviewed snapshot
Independent review of daemon snapshot `eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the supplied artifact files, generated outputs, executable script, key inputs, README, archive, and the explicit referencing wiki pages. Repository `grep_repo` was unavailable because the tool backend lacked `rg`; I therefore used the bundle plus targeted `read_file` for omitted pages (`modality-chokepoint-matrix.md`, `chassis-pending-interventions.md`, `validation-experiments.md`, index/vision pages). Snapshot-to-files appeared coherent for the rerun outputs, but the documentation/wiki contract is not clean.

## Bottom-line verdict
Action required. The rerun computation appears to have corrected the original fatal substitution from artificial back-translated CDS to real NM_144585.4 mRNA, but the artifact and corpus still contain stale original-run claims, old guide sequences, old funnel counts, and over-strong “viable/accessible” wording. The computation supports only “filter-passing real-transcript candidate sites exist”; it does **not** establish accessible, off-target-cleared, cross-species-reusable, or wet-lab-ready siRNA guides.

## Implementation and constraint closure
I traced the current `scripts/analyze.py` through the committed inputs and outputs:

- **Question/model fit:** The rerun answers a narrower question than the original headline: whether any 21-nt windows on NM_144585.4 pass simple siRNA design filters. It does not resolve knockdown efficacy, transcriptome specificity, chemical-modification behavior, kidney-proximal-tubule delivery, isoform coverage, or actual RISC accessibility in cells.
- **Corrected substitution:** The new code uses `inputs/NM_144585.4_mrna.fasta` rather than back-translating protein sequence. That fixes the prior nucleotide-specificity invalidation.
- **Main hidden substitution remains:** “Target-site availability” is treated as “mechanistically viable” despite RNAplfold probabilities for the shortlisted 21-mers being extremely low (`0.0–0.0047`). The interpretive page handles this caveat better than `outputs/summary.md` and much better than README, but the output summary still calls the sites “viable.”
- **Inputs into code:**
  - `NM_144585.4_mrna.fasta` is used.
  - `urat1_orthologs.fasta` is used for amino-acid conservation hints.
  - `design_parameters.json` is read only for `output_shortlist_size`; most thresholds and motif lists are hard-coded.
  - `human_codon_usage.json` and `orthologs.json` are stale/unused by the rerun, yet README and metadata still describe old uses.
- **Stored-but-unused / stale parameters:** The heuristic unused-input list is mostly real for this rerun: `codons`, `structural_accessibility`, most Reynolds/Ui-Tei/off-target/conservation JSON entries are not dynamically consumed. Some are documentation-only, but documentation is stale and contradicts the rerun.
- **Scoring implementation:** Reynolds/Ui-Tei/immunogenicity filters are plausible as simple sequence-rule filters. However, off-target logic described in `design_parameters.json` (“known miRNA seed” approximation) is not implemented; no transcriptome seed matching occurs.
- **RNAplfold implementation:** The code uses ViennaRNA `probs_window` with `u=21`, `W=80`, `L=40`, using probability that the 21-nt stretch ending at `end1` is unpaired. I did not execute the code. ViennaRNA version is not pinned.
- **Region classification issue:** `region_of()` classifies by midpoint. The rank-8 “5'UTR” candidate at mRNA position 326 spans positions 326–346, crossing the CDS start at 338 and containing the start codon. Calling it a pure `5'UTR` target is misleading; it should be labeled boundary-spanning or excluded/handled explicitly.
- **Conservation closure:** Conservation is amino-acid window identity only. It is correctly labeled in rerun outputs as a hint, but stale pages still imply nucleotide/cross-species guide reuse.
- **Biological constraints not closed:** No transcript isoform scan beyond NM_144585.4; no human transcriptome off-target clearance; no seed-family burden; no SNP/variant analysis; no chemical modification or innate immune mitigation modeling beyond motif avoidance; no intracellular accessibility or expression context; no delivery/localization modeling.

## Summary-fidelity audit
Major mismatches remain.

- `outputs/summary.md`: Mostly matches the current JSON/CSV counts and shortlist, but overstates “viable real-transcript target sites” given P(unpaired) ≈ 0 for most hits. It should say “filter-passing candidate sites” and explicitly foreground low accessibility in the verdict, not only limitations.
- `outputs/shortlist.csv`: Matches the JSON shortlist.
- `outputs/target_sites.json`: Internally coherent with the rerun and carries `off_target_cleared: false`, but omits `filtered_out_by_homopolymer` while README/old summaries still discuss it.
- `README.md`: Not reconciled. The top-line verdict, pipeline, methodology summary, file index, top-line shortlist, and limitations are still the invalidated original back-translation run. Only the “How to reproduce” section was updated. This is the most serious artifact-level summary failure.
- `wiki/urat1-sirna-target-site-selection-computational.md`: Mixed state. The opening warning and verdict are updated for the rerun, but the funnel table, “Top 5 wet-lab handoff candidates,” limitations, and “What this informs” still reproduce the invalidated 2026-05-16 artificial-CDS counts/sequences and claims.
- `wiki/computational-experiments.md`: The comp-009 planned-analysis row is materially consistent: completed rerun on real transcript; 8 sites; low accessibility and off-target uncleared.
- `wiki/hypotheses/H03-sirna-urat1-thesis.md`: Consistent and appropriately caveated: target-site availability supported, exposure/off-target not closed, original invalidated.
- `wiki/sirna-urat1-modality.md`: Still lists P2-2 as queued and describes comp-009 as a future RNAfold/accessibility analysis. It should be updated to “completed rerun; availability only; low accessibility/off-target open.”
- `wiki/chassis-pending-interventions.md`: Still says the cheapest first move is comp-009 queued. It should be updated to reflect completion and the remaining next moves.
- `wiki-archive.md`: It is explicitly an archive, but it contains invalidated guide sequences and cross-species reuse claims. It must remain clearly frozen and should not be linked as current evidence.
- `wiki/validation-experiments.md`: No direct comp-009 update was required in the inspected section; siRNA validation remains mostly tracked on the modality/H03/chassis-pending surfaces.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/target_sites.json` | generated output | yes | Rerun output is internally coherent; supports 8 diverse shortlisted candidates from 31 passing windows, but only as off-target-uncleared, low-accessibility candidates. |
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/shortlist.csv` | generated output | yes | Matches JSON shortlist; no off-target-cleared or wet-lab-ready implication should be inferred. |
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/summary.md` | generated output | yes | Numerically matches rerun, but “viable”/“GREEN” wording is too strong without an accessibility threshold and with P(unpaired) near zero. |
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md` | artifact summary/proposed update | yes | Severely stale above the reproduction section: original back-translation counts, original guides, stdlib claim, and old limitations remain. |
| `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/wiki-archive.md` | archive | yes | Old invalidated artifact snapshot; acceptable only if never cited as current. |
| `wiki/urat1-sirna-target-site-selection-computational.md` | interpretive wiki page | yes | Partially updated but still contains invalidated funnel, top candidates, and old limitations. |
| `wiki/computational-experiments.md` | index/wiki surface | inspected relevant sections | Consistent with rerun and caveats. |
| `wiki/hypotheses/H03-sirna-urat1-thesis.md` | hypothesis/wiki surface | yes | Consistent and appropriately limited. |
| `wiki/sirna-urat1-modality.md` | scope/wiki surface | yes | Stale P2-2 queued status and no rerun result propagation. |
| `wiki/chassis-pending-interventions.md` | affected wiki surface | inspected relevant comp-009 section | Stale: still names comp-009 as cheapest first move rather than completed with residual gates. |
| `wiki/modality-chokepoint-matrix.md` | affected wiki surface | inspected relevant siRNA row | No direct numeric mismatch found; could optionally link comp-009 but not load-bearing. |
| `wiki/validation-experiments.md` | affected wiki surface | inspected dashboard/relevant framing | No direct comp-009 mismatch found in inspected sections. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Real transcript is `NM_144585.4`, length 2792 nt | FASTA, JSON metadata, summary | Used as sequence scanned by `analyze.py` | FASTA included; NCBI primary record not independently verified in artifact | Plausible but primary-source verification unresolved. |
| CDS coordinates 338–1999 | `analyze.py`, JSON metadata, summary | Hard-coded; used for region/conservation mapping | Claimed “per RefSeq annotation”; GBFF/NCBI annotation not included | Needs source verification or included annotation snapshot. |
| 2711 windows scored | JSON metadata, summary | From `range(30, len(mrna)-21-30)` | Reconstructable from code and transcript length | Plausible; note edge-trim means not literally every full-mRNA 21-mer. |
| 222 GC pass / 120 immuno pass / 76 homopolymer pass / 31 design pass / 8 shortlist | JSON/summary/CSV | Derived in code | Not independently executed; internally consistent across outputs | Plausible by inspection, not reproduced. |
| “8 viable real-transcript target sites” | output summary/README/wiki | Derived from shortlist count | No accessibility threshold, off-target search, or knockdown model | Overstated; should be “8 filter-passing candidate sites.” |
| RNAplfold P(unpaired) values 0.0–0.0047 | JSON/CSV/summary | Composite score component | ViennaRNA version not pinned; code not executed | Values undermine “accessible” claim; rerun reproduction needed for exact numbers. |
| Off-target cleared | JSON metadata says false; summary limitation says no | Not implemented | No transcriptome database included | Correctly not cleared; any wet-lab handoff must not proceed on current guides alone. |
| Conservation 95.2%, 90.5%, etc. | JSON/CSV/summary | Computed from protein FASTA positional windows | Ortholog FASTA included; UniProt primary records not verified; no MSA; no nucleotide alignment | Accept only as amino-acid regional hint. |
| Top candidate mRNA 1029 sense `CCUUGGUGAUGACCUUGAACU` | CSV/JSON/summary | Shortlist rank 1 | Maps plausibly to included FASTA; no external transcript verification | Candidate sequence plausible, not off-target-cleared. |
| Rank-8 `5'UTR` candidate at mRNA 326 | CSV/JSON | Region by midpoint | Code shows midpoint rule; window overlaps CDS start | Region label misleading; needs correction. |
| Design parameters from Reynolds/Ui-Tei/Judge/Hornung/Tafer | `design_parameters.json`, README | Mostly hard-coded, not read from JSON | Citation strings only; primary papers not included | Parameters plausible but provenance not verified; JSON stale. |
| Repro command with ViennaRNA | README | Required to reproduce outputs | No lockfile/version; top README still says stdlib/run `python3` | Reproducibility contract inconsistent and incomplete. |

## Affected wiki pages
- `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md` — change required — stale original-run top-line, methodology, file index, shortlist, and limitations contradict rerun outputs.
- `wiki/urat1-sirna-target-site-selection-computational.md` — change required — opening caveat is updated, but funnel, top candidates, limitations, and old guide sequences remain invalidated.
- `wiki/sirna-urat1-modality.md` — change required — P2-2 still marked queued; should record comp-009 rerun completion and residual accessibility/off-target gates.
- `wiki/chassis-pending-interventions.md` — change required — “cheapest first move: comp-009” is stale; next move should be off-target clearance / accessibility thresholding / delivery chemistry scan.
- `wiki/hypotheses/H03-sirna-urat1-thesis.md` — already consistent — correctly states availability supported but exposure/off-target open and original invalidated.
- `wiki/computational-experiments.md` — already consistent — comp-009 row correctly notes real transcript rerun, 8 sites, low accessibility, off-target uncleared.
- `wiki/modality-chokepoint-matrix.md` — already broadly consistent / optional change — siRNA row remains generic; no stale comp-009 numbers found in inspected section.
- `wiki/validation-experiments.md` — already consistent / no direct change required from inspected sections — siRNA-specific experimental next steps are not housed there yet.

## New connections or implications
- The rerun turns the H03 killshot into a split decision: **target-site existence survives, but target-site exposure is now the dominant sequence-side uncertainty** because all shortlisted RNAplfold 21-mer unpaired probabilities are near zero.
- The rank-8 start-codon-overlapping candidate highlights that UTR/CDS boundary sites need explicit handling in siRNA design; midpoint region labels are too coarse for handoff.
- The artifact demonstrates a recurring corpus hygiene issue: rerunning a comp corrected the machine outputs but did not fully propagate into the long-form artifact README or interpretive page. For future reruns, stale top-line tables should be treated as release blockers.

## Required actions
1. Update `README.md` to fully reflect the rerun: real NM_144585.4 input, ViennaRNA dependency, 2711/222/120/76/31/8 funnel, new shortlist, no back-translation, no stdlib-only claim, no original guide table.
2. Update `wiki/urat1-sirna-target-site-selection-computational.md`: replace old funnel/top-5/limitations with rerun values and remove all invalidated original guide sequences except in an explicitly historical warning.
3. Update `wiki/sirna-urat1-modality.md` and `wiki/chassis-pending-interventions.md` so comp-009 P2-2 is no longer queued; state “completed rerun, availability only; low accessibility and off-target clearance remain open.”
4. Reword `outputs/summary.md` and any wiki verdicts from “viable/accessibile sites” to “filter-passing candidate sites,” unless an explicit accessibility threshold is defined and met.
5. Pin the reproducibility environment: ViennaRNA version, Python version, install command, and ideally a lockfile or recorded package version; remove contradictory stdlib-only language.
6. Clean or retire stale inputs/docs (`human_codon_usage.json`, old `structural_accessibility` and cross-species-reuse claims in `design_parameters.json` / `orthologs.json`) or clearly label them retained only for historical provenance.
7. Fix region annotation for boundary-spanning windows, especially mRNA position 326, or explicitly exclude/report UTR/CDS-overlap targets.
8. Before any wet-lab handoff, run transcriptome seed/off-target clearance against relevant human transcript/3'UTR databases and, if cross-species reuse matters, repeat against real ortholog mRNAs.

## Review limits
I did not execute `analyze.py`; exact ViennaRNA outputs were not independently reproduced. Primary sources for RefSeq NM_144585.4, UniProt orthologs, Reynolds/Ui-Tei/Judge/Hornung/Tafer parameters were not directly verified; only artifact-provided sequences and citation strings were inspected. Repository-wide fixed-string search failed because `grep_repo` could not find `rg`, so affected-surface search was limited to the bundle plus targeted page reads. The bundle was truncated for `open-questions.md`; no load-bearing comp-009 claim was identified there before truncation, but a full corpus search should still be run after tool repair.
