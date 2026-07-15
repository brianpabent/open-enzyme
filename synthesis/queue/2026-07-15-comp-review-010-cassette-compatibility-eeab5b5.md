---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-010
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-010

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-010-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-010-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-010

## Reviewed snapshot
Independent API reviewer; daemon snapshot `commit:eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the complete artifact bundle supplied for `wiki/etc/experiments/comp-010-cassette-compatibility`, including script, all inputs, both generated outputs, README, provenance, and `wiki-archive.md`. I also inspected bounded portions of omitted affected wiki pages via repository tools until the tool-result budget was exhausted. The repository grep tool failed because `rg` is unavailable in the environment, so mechanism-wide search coverage is limited.

## Bottom-line verdict
Action required. The sequence-level LOW-risk conclusion is broadly plausible within its stated narrow scope, but the artifact-summary-wiki contract is not clean. Required fixes include a code logic bug in the Huynh comparison branch, inconsistent lactoferrin residue numbering for a proposed KEX2-site mutation, inconsistent glycosylation burden accounting, a stale `17` lactoferrin-disulfide entry in `chaperone-orthogonal-stacking.md`, and a stale generated-summary script path.

## Implementation and constraint closure
The implementation is a deterministic stdlib Python sequence-analysis pipeline over protein FASTA plus JSON rule tables. It performs:

- amino-acid-level codon proxy using hard-coded origin-preferred codons;
- mature-sequence `KR` scanning with P1′ classification from `kex2_site_specs.json`;
- C-terminal ER/PTS scans;
- cysteine/disulfide count using hard-coded known disulfide counts;
- `N-X-S/T` sequon scanning;
- combined burden synthesis and Huynh comparison;
- JSON and Markdown summary generation.

Important closure findings:

- **Question/model fit:** comp-010 answers a narrow sequence/cassette-design question. It does not resolve physiological UOX topology, urate concentration relative to Km, oxygen limitation, peroxide mass balance, solid-state secretion, iron availability, residence time, or clinical efficacy. The README, wiki archive, validation entry, and computational index mostly preserve this boundary.
- **Stored-but-unused / weakly used inputs:**
  - `glucoamylase_carrier.fasta` is included but not loaded or analyzed. That is acceptable only if the scope is payload compatibility rather than carrier-sequence risk; the artifact should not imply carrier-specific closure.
  - `rare_codon_definition.freq_threshold`, `rare_codons_list`, and JSON logic text are not implemented; code uses only `rscu < 0.4`. This does not affect the current zero-rare result because the preferred codons used are not below threshold, but the implementation and input definition are not identical.
  - `alternative_linkers` and detailed KEX2 documentation fields are provenance/design context only, not computation inputs.
- **Code bug:** `analyze_huynh_comparison()` now contains the corrected text “Uricase has 3 cysteine residues (0 annotated disulfides)” inside `if oe_uri_cysteine == 0:`. Since Q00511 has 3 cysteines, the branch is unreachable, so generated JSON and summary omit the intended “no PDI load from uricase” easier-than-Huynh comparison item. The condition should key on `known_disulfide_bonds == 0`, not cysteine count.
- **Residue-numbering bug / ambiguity:** The code reports lactoferrin moderate KR site at mature position 579 and full position 598 (`signal_peptide_end = 19`, so full = mature + 19). `wiki-archive.md` recommends mutating `K597→Q` and describes the full-sequence motif as `K597-R598-K599`. That is off by one relative to the implementation. Because this is a gene-synthesis-time design recommendation, this is load-bearing.
- **Glycosylation burden ambiguity:** Generated JSON/summary count `dual_cassette_nxst_sites = 4` because uricase has one predicted `NFS` sequon plus three lactoferrin sequons. `wiki-archive.md` §5.6 says combined glycosylation is 3 and treats uricase as `~0` because likely unoccupied. Both may be defensible if labeled as “predicted sequons” vs “expected occupied sites,” but the artifact currently mixes those metrics.
- **Reaction/physiology constraints:** No reaction substrates/products/cofactors are modeled except as background context. Uricase requires urate, O₂, and produces H₂O₂/allantoin intermediates, but comp-010 does not compute substrate occupancy, O₂ availability, peroxide burden, or access. This is acceptable for a sequence-level comp only because downstream §1.33/§1.36 gates are explicitly retained.
- **Localization:** C-terminal `SKL` PTS1 risk is correctly surfaced as moderate and empirical. The conclusion “amyB signal peptide should override PTS1” is a mechanistic expectation, not implemented or verified.
- **Secretion/folding:** Disulfide burden is a bulk-count comparator only; it does not model architecture-specific PDI residence, ER capacity, or solid-state secretion. The wiki-archive correction now states “predicted tractable but not demonstrated,” which is appropriate.
- **Reproducibility:** The stated command in README is now correct: `cd wiki/etc/experiments/comp-010-cassette-compatibility && python3 analyze.py`. No external dependencies are required. I did not execute code in daemon mode.

## Summary-fidelity audit
- **README.md:** Mostly faithful to current intended interpretation. It correctly frames comp-010 as sequence-level candidate support, not topology selection. It uses the corrected reproducibility path. It does not expose the code bug in the Huynh comparison branch.
- **outputs/cassette_analysis.json:** Internally consistent with the current code, but inherits the unreachable uricase-cysteine comparison branch and the 4-sequon combined glycosylation metric. It reports lactoferrin KR full position 598.
- **outputs/summary.md:** Faithful to generated JSON, but:
  - stale script path: `experiments/comp-010-cassette-compatibility/analyze.py` instead of `wiki/etc/experiments/comp-010-cassette-compatibility/analyze.py`;
  - omits the intended corrected Huynh comparison item about uricase having 3 cysteines / 0 disulfides due to the code bug;
  - reports combined N-glycosylation as 4 predicted sequons, while wiki archive uses 3 likely occupied sites.
- **wiki-archive.md:** Mostly improved and appropriately caveated versus the earlier over-strong Huynh-capacity wording. However, it contains the lactoferrin KEX2 full-position mismatch (`K597→Q` vs code full position 598) and the 3-vs-4 glycosylation inconsistency.
- **wiki/cassette-compatibility-computational.md:** Stub only; consistent with archive linkage.
- **wiki/computational-experiments.md:** The comp-010 entry is appropriately narrow: LOW cassette-design risk, bulk disulfide comparator only, topology not selected. No action from the index text itself.
- **wiki/validation-experiments.md §1.9:** The supplied section is consistent with comp-010’s limited role and keeps §1.33/§1.36 gates. It repeats the comp-010 design notes in a bounded way.
- **wiki/hypotheses/H01-ward-dual-cassette.md:** The inspected comp-010 subsection is consistent and explicitly says comp-010 is not a killshot.
- **wiki/koji-endgame-strain.md:** Inspected sections are largely consistent with comp-010 and current topology caveats.
- **wiki/chaperone-orthogonal-stacking.md:** Change required. In §5.5.1, the triple-cassette setup table still lists lactoferrin as **17** disulfides while surrounding text uses 16 and total 24. This is a stale load-bearing number in a page that uses the comp-010/Notari correction.
- **wiki/aspergillus-oryzae.md:** The comp-010 update text is consistent on 16 disulfides and caveats equal-count vs equal-burden. The broader page still contains strong peroxide-safety language elsewhere, but that is primarily governed by comp-044/045/§1.33 rather than comp-010.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-010-cassette-compatibility/README.md` | tracked summary / committed update | yes | Corrected reproduction path; interpretation mostly faithful; narrow scope preserved. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/analyze.py` | executable analysis | yes | Deterministic stdlib script; has unreachable corrected uricase-cysteine comparison branch; stale generated script path in summary writer; some inputs unused/documentation-only. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/P02788.fasta` | input FASTA | yes | Used for Lf sequence scans; residue-numbering conventions need reconciliation against code/provenance/wiki text. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/Q00511.fasta` | input FASTA | yes | Used for uricase sequence scans; length 302 and 3 cysteines reflected in outputs. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/a_oryzae_codon_usage.json` | input JSON | yes | Used for RSCU lookup; `freq_threshold`, `rare_codons_list`, and AND-logic note are not implemented. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/glucoamylase_carrier.fasta` | input FASTA / provenance context | yes | Not used by code; acceptable only if analysis is explicitly payload-only, not carrier-risk closure. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/kex2_site_specs.json` | input JSON | yes | P1′ preference lists used; alternate linker and documentation leaves unused as expected context. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md` | provenance | yes | Corrects Q00511 length to 302; primary-source citations not directly verified here. Lf feature numbering needs clarification. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/outputs/cassette_analysis.json` | generated output | yes | Reproducible from current code by inspection; includes 4 predicted NXST sites combined; omits intended uricase easier-than-Huynh cysteine/disulfide note. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md` | generated output | yes | Faithful to JSON but has stale script path, misses corrected uricase comparison note, and participates in 4-vs-3 glycosylation inconsistency. |
| `wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md` | archived proposed/interpretive wiki content | yes | Mostly well caveated; needs KEX2 full-position correction and glycosylation metric clarification. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 uricase length = 302 aa | `Q00511.fasta`, `provenance.md`, README, JSON | `len(uricase_seq)` | Direct FASTA available; UniProt not independently fetched | Verified within artifact |
| Q00511 has 3 cysteines, 0 annotated disulfides | FASTA, `URICASE_DISULFIDES = 0`, JSON | Cys counted from sequence; disulfides hard-coded | Cys count verifiable in FASTA; disulfide annotation only citation/provenance | Count verified; disulfide annotation not primary-verified |
| Q00511 internal KR site at mature/full 128, P1′=N | JSON, summary, wiki-archive | Computed by `analyze_kex2_sites()` | Directly derivable from FASTA | Plausible and internally reproducible |
| Q00511 C-terminal `SKL` PTS1-like motif | FASTA, JSON, summary | Computed by routing scan | Directly visible in FASTA | Verified motif; functional routing unverified |
| P02788 length = 710 aa, signal peptide end = 19, mature length = 691 | FASTA, provenance, code constants, JSON | Used for mature scans and positions | FASTA available; UniProt signal peptide not independently fetched | Internally consistent for length; signal boundary citation not primary-verified |
| Lactoferrin internal KR sites: mature 38 P1′=D and mature 579 P1′=K | JSON, summary, wiki-archive | Computed by `analyze_kex2_sites()` | Directly derivable from FASTA if numbering convention accepted | Mature positions plausible; full positions inconsistent in wiki text |
| Lactoferrin moderate-site mutation recommendation `K597→Q` | `wiki-archive.md` §5.2/§6 | Documentation recommendation; not generated from code | Conflicts with code full position 598 | Action required before gene synthesis |
| Lactoferrin disulfides = 16 | code constant `LF_DISULFIDES = 16`, JSON, summaries | Hard-coded folding-load input | Provenance cites Notari 2023; primary not included | Plausible but not independently primary-verified |
| Lactoferrin cysteine count = 32 mature | code passes `lf_seq[19:]` to disulfide analyzer; JSON | Counted from mature sequence | Direct FASTA available | Internally verified by code logic; not manually source-verified |
| Huynh baseline = 16 disulfides and 39.7 mg/L | code constants, JSON, summary/wiki | Comparator for load index and titer gap | Citation string only; primary not in artifact | Not primary-verified; comparator appropriately caveated |
| Lf target = 500 mg/L; UOX target = 100 mg/L | `analyze_combined_burden()` | Titer-gap summary | Comes from corpus/validation design, not primary data | Design target, not evidence |
| Ward 1995 Lf >2 g/L | README/wiki/archive/summary | Contextual benchmark only | Citation string; primary not in artifact | Not primary-verified; appropriately separated from proof |
| Codon usage “LOW” for both payloads | JSON/summary | Computed from hard-coded preferred-codon maps and RSCU table | Codon table manually transcribed; preferred codon maps not directly sourced in artifact | Mechanistic proxy only; not sufficient for CDS design |
| Combined disulfide load = 16, all from Lf | JSON/summary/wiki | Sum of hard-coded disulfide counts | Depends on hard-coded LF and UOX annotations | Arithmetic valid; source verification incomplete |
| Combined glycosylation burden = 4 predicted sequons vs 3 likely occupied sites | JSON/summary vs wiki-archive | JSON sums predicted NXST; wiki interprets expected occupied sites | Uricase occupancy unverified | Action required to label metric consistently |
| Overall cassette-design risk = LOW | README, JSON, summary, wiki-archive/index | Synthesis rule in `analyze_combined_burden()` | Depends on narrow sequence-level model | Plausible only as “no blocking sequence-level issue”; not physiological proof |

## Affected wiki pages
- `wiki/cassette-compatibility-computational.md` — already consistent / no content change required beyond archive fixes — stub points to archive and experiment folder.
- `wiki/computational-experiments.md` — already consistent — comp-010 entry preserves narrow sequence-level LOW verdict and topology caveat.
- `wiki/validation-experiments.md` — already consistent — §1.9 keeps §1.33 upstream, staged Lf/UOX/dual design, and comp-010 as computational prior only.
- `wiki/hypotheses/H01-ward-dual-cassette.md` — already consistent — comp-010 is described as design support, not a survived killshot or evidence-tier upgrade.
- `wiki/koji-endgame-strain.md` — mostly consistent — inspected sections carry the corrected 16-disulfide count and topology caveat; no comp-010-specific action except ensuring any KEX2 full-position mutation text is reconciled if present elsewhere.
- `wiki/chaperone-orthogonal-stacking.md` — change required — §5.5.1 still lists lactoferrin as 17 disulfides in a table while the corrected model uses 16; this is a stale load-bearing number.
- `wiki/aspergillus-oryzae.md` — already consistent for comp-010’s disulfide/cassette-compatibility text — broader peroxide-safety language remains a separate comp-044/045/§1.33 issue.
- `wiki/lactoferrin.md` — unresolved / likely needs spot check — tool budget prevented full review; residue/feature numbering conventions for mature vs full P02788 should be checked because comp-010 currently has a mutation-position mismatch.
- `wiki/uricase-variant-selection.md` — unresolved — tool budget prevented inspection; likely affected only if it repeats Q00511 length/cysteine/PTS1 claims.

## New connections or implications
- The most actionable cross-corpus implication is not a new biological conclusion but a **numbering-discipline issue**: comp-010 mixes mature and full P02788 positions in a way that could cause a wrong gene-synthesis mutation. This should be standardized before any wet-lab ordering.
- The **glycosylation-burden distinction** should become a general reporting convention: “predicted sequons” and “expected occupied ER glycosylation sites” are different metrics. Uricase’s `NFS` is especially ambiguous because native intracellular non-occupancy does not prove non-occupancy after forced secretion through the ER.
- The Huynh comparison should be reframed in generated output as “uricase contributes no disulfide/PDI load despite 3 free cysteines,” not “uricase has no cysteines.” The current code fix attempted this but did not close the branch condition.

## Required actions
1. Fix `analyze_huynh_comparison()` so the “uricase has 3 cysteine residues, 0 annotated disulfides” easier-than-Huynh note is appended when `known_disulfide_bonds == 0`, not when cysteine count is zero; regenerate `outputs/cassette_analysis.json` and `outputs/summary.md`.
2. Reconcile lactoferrin residue numbering across code, JSON, summary, provenance, and `wiki-archive.md`. Verify whether the moderate KEX2-site P1 lysine is full-position 598 or 597, then update the mutation recommendation accordingly before gene synthesis.
3. Clarify glycosylation accounting: report both “predicted NXST sequons = 4” and “expected occupied sites = 3 if uricase N191 is unoccupied,” or choose one metric consistently for combined ER burden. Update JSON/summary/wiki-archive/README wording as needed.
4. Fix the generated summary’s stale script path from `experiments/comp-010-cassette-compatibility/analyze.py` to `wiki/etc/experiments/comp-010-cassette-compatibility/analyze.py`, then regenerate.
5. Update `wiki/chaperone-orthogonal-stacking.md` §5.5.1 to remove the stale lactoferrin “17 disulfides” table entry and ensure all comp-010/Notari-derived counts are 16.
6. Mark load-bearing literature values as citation-only unless primary source text was actually verified, or add primary-source verification artifacts for LF disulfide count, Huynh titer/disulfide baseline, Ward titer, KEX2 P1′ rules, and codon-table provenance.

## Review limits
- I did not execute `analyze.py` in daemon mode; reproducibility was assessed by inspection.
- Primary sources were not fetched or independently verified. Citation strings and provenance were inspected, but primary-source verification should not be inferred.
- Repository grep failed because the environment lacks `rg`; therefore mechanism-wide affected-page discovery is incomplete.
- Tool-result budget was exhausted while reading omitted pages. I inspected key relevant sections of H01, chaperone-orthogonal-stacking, koji-endgame-strain, lactoferrin, and aspergillus pages as available, but not every omitted page was fully read.
- The bundle’s `validation-experiments.md` was truncated after the comp-010-relevant sections; later unrelated sections were not inspected.
