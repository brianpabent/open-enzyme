---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-009
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-009

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-009-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-009-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-009

## Bottom-line verdict
**Quantitative verdict invalid.** The computation ranks siRNA candidates on a **seeded, randomly back-translated artificial CDS**, not on the actual human SLC22A12 / URAT1 mRNA or RefSeq CDS. Because siRNA targeting is nucleotide-sequence-specific, the reported guide sequences, scores, conservation/reuse claims, and “H03 killshot does not fire” conclusion do **not** resolve the stated question. At most, the artifact shows that a URAT1-length protein sequence can be synonymously encoded to contain some windows satisfying generic siRNA design heuristics.

## Implementation and constraint closure
I traced the main inputs through `scripts/analyze.py`, `outputs/summary.md`, `outputs/shortlist.csv`, and `outputs/target_sites.json`.

Key closure findings:

- **Wrong biological object.** The stated question is “Which 21-nt target sites on SLC22A12 mRNA are viable?” The implementation never loads actual SLC22A12 mRNA (`NM_144585.3`) or any transcript variant. It back-translates the UniProt protein using human-average codon usage and a random seed. This substitutes “possible synonymous CDS sequence” for “the expressed mRNA target.”
- **Target-site sequences are not valid oligo-design outputs.** The top antisense guides are reverse complements of the artificial CDS, so they should not be used as wet-lab handoff candidates or evidence that the actual mRNA contains those sites.
- **Accessibility is not mRNA accessibility.** The “local structural accessibility” score is calculated on the isolated 21-mer using a crude self-stem heuristic. It does not fold the actual full mRNA, local transcript region, UTRs, isoforms, or cellular RNA context. Thus the “accessible” part of the verdict is unclosed.
- **Off-target filtering is absent.** `design_parameters.json` describes seed-region transcriptome filtering and known-miRNA seed cautions, but the code performs no BLAST/transcriptome search and no known-miRNA seed exclusion.
- **Most design parameters are stored but unused.** `design_parameters.json` is loaded only to read `output_shortlist_size`. Thresholds and rules for guide length, duplex length, GC range, Ui-Tei, Reynolds positional preferences, TLR motifs, GU-rich threshold, structural accessibility, seed region, and off-target filters are hardcoded or not implemented.
- **`orthologs.json` is not read.** RefSeq IDs, UniProt provenance, and species metadata are documentation only. Conservation comes only from `urat1_orthologs.fasta`.
- **Conservation is AA-level, positional, and not siRNA-level.** The code computes amino-acid identity over direct positional windows, not nucleotide conservation of the actual human/chimp/mouse/rat mRNAs. The claim that the “same guide should work in rodent preclinical PK/PD AND human therapeutic” is unsupported.
- **AA-window labels are approximate for non-codon-aligned siRNA windows.** The code slides every nucleotide, but maps conservation by `aa_pos = i // 3` and `aa_len = 7`. For non-frame-aligned windows, the reported AA window does not exactly correspond to the 21 nt target.
- **Pipeline count has a boundary/presentation issue.** Code uses `range(75, len(human_cds) - window - 75)`, yielding 1-based starts 76–1563, not a clean “CDS positions 76 to 1584” start range as written. This is minor relative to the surrogate-sequence problem.
- **Output contract is overstated.** The script docstring says `target_sites.json` contains “all 21-mer windows with per-filter scores,” but the committed output contains metadata, shortlist, and top 50 passing candidates only. It does not preserve all 1,488 scored windows.
- **Safety and operating-regime closure incomplete.** The artifact checks a few unmodified RNA immunogenic motifs and GU-rich windows, but does not address chemical modifications, dose, kidney delivery, proximal-tubule access, endosomal escape, RISC loading, transcript abundance, transcript variants, knockdown-depth ceiling, hypouricemia risk, uricosuria/stone risk, or off-target transcriptome effects. Those are outside this computation but must not be implied closed.
- **Sensitivity analysis absent.** The dominant uncertainties are actual mRNA sequence, transcript isoforms/UTRs, RNA structure, off-target burden, delivery chemistry, and nucleotide conservation. The run varies none of them; random seed is fixed rather than sensitivity-tested.

## Summary-fidelity audit
The artifact documentation is internally mixed: the limitations sections acknowledge the biggest caveat, but the verdict language and propagated wiki claims are stronger than the implementation supports.

- **README.md:** Correctly admits CDS-only, back-translation surrogate, no ViennaRNA, no BLAST, AA-not-nucleotide conservation. However, it still states **“GREEN,” “URAT1 mRNA is amenable,” “10 ranked target-site candidates,”** and **“H03 killshot does not fire.”** That overstates what a random back-translation can establish.
- **outputs/summary.md:** Same issue. It says “target-site shortlist is viable” and “URAT1 mRNA has multiple regions amenable to standard siRNA design rules,” but the exact nucleotide target sites are artificial.
- **interpretive page `wiki/urat1-sirna-target-site-selection-computational.md`:** Requires correction. It claims URAT1 mRNA has accessible target sites and that the same top guide should work in rodents and humans. The limitations paragraph softens the sequence issue, but not enough to undo the headline conclusion.
- **`wiki/computational-experiments.md`:** The page still lists comp-009 under **Planned Analyses**, not as a completed analysis. If comp-009 is promoted, it must be promoted with a downgraded/invalid verdict; otherwise the planned item should be reframed as “rerun required with actual RefSeq mRNA.”
- **`wiki/hypotheses/H03-sirna-urat1-thesis.md`:** Assumption 1 says URAT1 mRNA accessible sites are “verified by comp-009.” That is not supported. H03 should remain unclosed on this assumption.
- **`wiki/sirna-urat1-modality.md`:** P2-2 remains queued in the page, while the comp artifact claims it is closed. The page should be reconciled: comp-009 attempted a proxy analysis but did not close P2-2.
- **`wiki/chassis-pending-interventions.md`:** Still describes comp-009 as the cheapest queued first move. This is acceptable only if updated to say the first attempted run did not close the mRNA target-site question.
- **`wiki/modality-chokepoint-matrix.md`:** Still treats comp-009 as a queued follow-up via the siRNA scope page. It should not inherit the GREEN verdict unless rerun on real mRNA.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Actual URAT1 mRNA target sites identified | README, summary, interpretive page | Not implemented; actual mRNA absent | RefSeq ID named in `orthologs.json`, sequence not present | **Invalid** |
| Human URAT1 protein Q96S37, 553 aa | FASTA, README | Used as source for back-translation | FASTA committed; primary UniProt not independently verified | Plausible but not primary-verified |
| Back-translated CDS, 1659 nt, GC 56.5%, seed 42 | `human_codon_usage.json`, `analyze.py`, outputs | Used as the actual scanned sequence | Codon frequencies cited to Kazusa; no primary file/snapshot | Reproducible surrogate, not biological target |
| `NM_144585.3` canonical mRNA | `orthologs.json`, README limitations | Not used | Citation string only; sequence absent | **Unresolved / unused** |
| 1,488 windows scanned | `analyze.py`, outputs | Generated from artificial CDS | Inspectable from code | Internally plausible, but on wrong sequence |
| Window range “CDS positions 76 to 1584” | README, summary | Code starts windows 1-based 76–1563 | Derived from code, wording imprecise | Minor mismatch |
| GC filter 30–52% | `design_parameters.json`, code | Hardcoded in `reynolds_score` and filter | Source named “Reynolds 2004”; primary not included | Implemented but not source-verified |
| Reynolds positional rules | `design_parameters.json`, code | Hardcoded partial scoring | Citation string only | Implemented as heuristic, not verified |
| Ui-Tei AU ≥4/7 | `design_parameters.json`, code | Hardcoded via `ui_tei_au_count` filter | Citation string only | Implemented, not source-verified |
| TLR7/8 motifs | `design_parameters.json`, code | Hardcoded `TLR_MOTIFS` | Citation strings only | Implemented but not data-driven from JSON |
| GU-rich threshold ≥7/9 | `design_parameters.json`, code | Hardcoded default in function | Citation string only | Implemented but not parameter-bound |
| Homopolymer exclusion | `design_parameters.json`, code | Implemented by checking `R2_no4runs` | Source not primary-verified | Implemented |
| Structural accessibility | README, design params, code | Isolated 21-mer self-stem heuristic | Tafer/Tinoco references named only; no primary verification | **Does not establish mRNA accessibility** |
| ViennaRNA/RNAplfold absence | README, summary | Not used | Limitation explicitly stated | Correct limitation, but verdict overstates |
| No BLAST/off-target transcriptome | README, summary | Not implemented | Limitation stated | Critical unresolved design gate |
| Seed-region off-target filter | `design_parameters.json` | Not implemented | Documentation only | **Stored but unused** |
| Known miRNA seed approximation | `design_parameters.json` | Not implemented; no list present | Documentation only | **Missing implementation** |
| Cross-mammalian conservation | FASTA, code, outputs | AA-level direct positional identity | FASTA committed; no MSA; mRNAs absent | Supports only rough AA conservation, not guide reuse |
| “Same guide works in rodents and humans” | README, interpretive page | Not implemented at nucleotide level | Ortholog mRNAs absent | **Unsupported / should remove** |
| Top guide `UAUAGUAUCUGGCAAAGGUAG` | outputs | Derived from artificial CDS | No actual mRNA verification | **Not a valid synthesis candidate** |
| Composite score 81.1/100 | code, outputs | Weighted sum of heuristic components | Weights not primary-sourced; no sensitivity | Internally computed but biologically non-actionable |
| `orthologs.json` provenance | input file | Not read | Documentation only | Unused input |
| `design_parameters.json` thresholds | input file | Mostly not read; only shortlist size used | Documentation only for most fields | **Parameter-file contract broken** |
| `target_sites.json` “all windows” | script docstring, README | Output caps passing candidates at top 50 | Inspectable | **Output contract mismatch** |
| Repro command `cd experiments/...` | README | Script path itself is runnable; cd path likely wrong relative to repo | Not executed | Needs correction to `wiki/etc/experiments/...` or documented working directory |

## Affected wiki pages
- `wiki/urat1-sirna-target-site-selection-computational.md` — **change required** — downgrade/remove GREEN mRNA-accessibility verdict; remove rodent/human same-guide claim; label current run as artificial-CDS proxy only.
- `wiki/computational-experiments.md` — **change required** — comp-009 remains in Planned Analyses despite artifact existence; if added to Analyses, verdict must be “invalid/proxy; rerun required with actual mRNA,” not GREEN.
- `wiki/hypotheses/H03-sirna-urat1-thesis.md` — **change required** — Assumption 1 is not verified by this artifact; H03 should not be unblocked on target-site accessibility.
- `wiki/sirna-urat1-modality.md` — **change required** — P2-2 is still queued; reconcile by stating comp-009 did not close it and that a RefSeq/RNAfold/off-target rerun remains required.
- `wiki/chassis-pending-interventions.md` — **change required** — cheapest-first-move text should note comp-009 attempted a surrogate analysis but did not close the mRNA target-selection gate.
- `wiki/modality-chokepoint-matrix.md` — **change required** — siRNA follow-up language should not inherit the GREEN comp-009 interpretation; keep target-site selection open pending real mRNA analysis.
- `wiki/open-questions.md` — **change required / optional depending on editorial policy** — should add or update an explicit open question: actual SLC22A12 transcript/isoform siRNA target-site selection with off-target and RNA accessibility closure remains unresolved.
- `wiki/validation-experiments.md` — **already consistent** — no direct comp-009 target-site claim found in inspected portion; siRNA track is mostly chassis-pending rather than wet-lab-indexed here.
- `wiki/index.md` — **already consistent** — broad platform statement only; no comp-009-specific propagation found.

## New connections or implications
- The artifact exposes a broader **siRNA-design standard** needed for the corpus: nucleotide-specific RNA therapeutics cannot be validated from protein back-translation. Future RNA/ASO comps should require committed transcript FASTA, isoform selection, UTR policy, target-region mapping, off-target seed scan, and real RNA accessibility prediction before any GREEN verdict.
- The H03 card’s delivery-chemistry caveats are downstream; comp-009 does **not** yet clear the upstream “does the target mRNA contain usable sites?” killshot. The siRNA track remains gated before kidney-tropic delivery is even considered.
- AA conservation may still be useful as a **region-selection hint** after a real mRNA rerun, but not as a same-guide cross-species claim. A corrected workflow could prioritize conserved protein regions, then require nucleotide-level human/rodent mRNA alignment before preclinical guide reuse is asserted.

## Required actions
1. **Rerun comp-009 on actual transcript sequences.** Owner surface: `wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/`. Verification criterion: input includes actual human SLC22A12 RefSeq transcript/CDS sequence(s), explicit isoform choice, UTR inclusion/exclusion rationale, and committed transcript FASTA.
2. **Replace artificial guide shortlist.** Owner surface: `outputs/summary.md`, `outputs/shortlist.csv`, `outputs/target_sites.json`, interpretive page. Verification criterion: no guide sequence is reported unless it maps exactly to the actual selected SLC22A12 transcript.
3. **Implement or remove parameter-file claims.** Owner surface: `scripts/analyze.py` and `inputs/design_parameters.json`. Verification criterion: thresholds/motifs/lengths/seed filters are read from JSON or clearly documented as hardcoded; unused documentation-only fields are labeled as such.
4. **Add real off-target closure.** Owner surface: comp-009 rerun. Verification criterion: seed-region and near-perfect-match search against a human transcriptome/3′UTR database is performed, or the verdict remains explicitly “target-site proxy only; no off-target clearance.”
5. **Replace accessibility surrogate with real RNA folding/accessibility.** Owner surface: comp-009 rerun. Verification criterion: RNAplfold/ViennaRNA or equivalent local accessibility over the actual mRNA context is used; isolated-21-mer self-folding is not called “mRNA accessibility.”
6. **Correct conservation claim.** Owner surface: README, summary, interpretive page. Verification criterion: cross-species reuse claims require nucleotide-level alignment of human/mouse/rat/chimp ortholog mRNAs at the guide site; AA-only conservation may be reported only as a region-level hint.
7. **Fix output contract.** Owner surface: `target_sites.json` and script docstring/README. Verification criterion: either all scored windows are output, or docs say only top 50 passing candidates are retained.
8. **Reconcile wiki propagation.** Owner surface: affected pages above. Verification criterion: no page states H03 target-site assumption is confirmed or P2-2 is closed until a real-mRNA rerun passes.

## Review limits
- I did **not** execute `scripts/analyze.py`; reproducibility was assessed by code/output inspection only.
- Primary sources for Reynolds, Ui-Tei, Judge/Hornung/Forsbach, Tafer, Kazusa codon usage, and UniProt/RefSeq were not directly verified; only artifact citation strings and committed FASTA/JSON were inspected.
- Repository `grep_repo` failed because its underlying `rg` executable was unavailable, so corpus search was limited to the explicit bundle plus selected `read_file` inspections of omitted pages.
- I inspected the beginning/large relevant portions of omitted pages via `read_file`, but not every byte of `validation-experiments.md` due file size.
- No arbitrary code was run and no external network access was used.
