---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-011
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-011


ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-011

## Reviewed snapshot

Independent API reviewer; daemon-mode review of commit `eeab5b53054b93544c428a476dad06a8f8fe2621`.

Snapshot basis: supplied complete tracked-file inventory for `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility`, full artifact bundle content, and repo reads of several affected wiki pages. I did not execute `analyze.py`. Repository fixed-string search failed because `rg` is unavailable in the tool environment, so corpus-wide affected-surface discovery is incomplete and is itself a review limit.

## Bottom-line verdict

**Action required.** The new ALLN-346 mutant implementation is directionally plausible and the key I132R result is internally consistent, but the artifact-summary-wiki contract is not clean:

- `wiki-archive.md` and several earlier sections of `outputs/summary.md`/JSON still describe the *C. utilis* fusion contingency as “both 130 and 138 HIGH / mutate both,” while the new mutant analysis says I132R changes position 130 from HIGH to MODERATE.
- The new mutant is analyzed only as a side branch; the main `combined_burden` and `comparison` objects still use WT P78609 and do not clearly separate “WT P78609 result” from “recommended P78609+ALLN-346 construct.”
- `README.md` does not surface the added second analyzed sequence and remains WT-oriented.
- Top-level propagation is partial: `uricase-variant-selection.md` reflects the mutant refinement, but `computational-experiments.md` still only says I132R is “adjacent” to the position-130 KR rather than the more load-bearing fact that it is the P1′ residue and reduces the site classification.

The qualitative MODERATE cassette-risk verdict is not invalidated, but the update is not fully reconciled.

## Implementation and constraint closure

I traced the load-bearing flow as follows:

- `main()` loads:
  - `inputs/P78609.fasta` as WT *C. utilis* / *Cyberlindnera jadinii* uricase.
  - `inputs/P02788.fasta` as human lactoferrin.
  - `inputs/a_oryzae_codon_usage.json`.
  - `inputs/kex2_site_specs.json`.
- WT uricase is analyzed for codon proxy, KEX2 sites, routing, cysteine/disulfide load, and N-X-S/T sequons.
- Lactoferrin is analyzed similarly, with signal peptide end hard-coded as 19 aa and mature-chain disulfides hard-coded as 16.
- The new block defines `ALLN346_MUTATIONS`, applies them with WT residue assertions, analyzes the mutant sequence, and writes:
  - `uricase_alln346_mutant`
  - `uricase_alln346_kex2_delta_vs_wt`
  - `mutant_analysis_added`

Key implementation findings:

- **Mutation-position logic is plausible.** Manual inspection of the supplied P78609 sequence confirms:
  - position 51 = E,
  - position 87 = A,
  - position 132 = I,
  - position 165 = Y,
  - position 180 = I,
  - position 190 = V,
  - position 244 = Q.
  The position-130 WT KR site is `KRI`; I132R changes it to `KRR`, making P1′ = R.
- **KEX2 delta logic is plausible.** The code classifies P1′ R as `MODERATE` because `R` is in `reduced_efficiency`; P1′ S at position 138 remains `HIGH`.
- **No new KR site is introduced by I132R.** The mutant local sequence becomes `KRR`, which still contains only the original K-R at positions 130–131; positions 131–132 are R-R, not K-R.
- **The mutant is not used in the main combined verdict.** `combined = analyze_combined_burden(uricase_results, lactoferrin_results, ...)` still uses WT `uricase_results`, not `mutant_results`. This is defensible for direct-secretion overall risk if codon/free-Cys/routing are unchanged and uricase KEX2 is non-load-bearing, but it must be labeled clearly because the recommendations invoke the ALLN-346 construct.
- **Hard-coded topology assumption remains load-bearing.** `uricase_kex2_is_load_bearing = False` makes uricase KEX2 risk informational only. The computation therefore answers an asymmetric candidate architecture with direct-secreted uricase, not a general Ward glucoamylase-KEX2 uricase-fusion architecture. The summary mostly acknowledges this, but older wording still overstates “Ward architecture” as though it is uniformly applicable.
- **Input JSON unused-leaf heuristic:**
  - `rare_codon_definition.freq_threshold`, `rare_codons_list`, and the text `logic` are not used; the code uses only `rscu_threshold`.
  - This creates a documentation/code mismatch: JSON says rare if `rscu < 0.4 AND freq_per1000 < 10`, but code says rare if `rscu < 0.4`.
  - Not load-bearing for the headline because *C. utilis* HEAVY burden is driven by CAI proxy <0.90, not rare-codon count.
  - `internal_kr_site_risk`, `alternative_linkers`, and Huynh linker fields are documentation/specification inputs rather than directly used scoring inputs; KEX2 scoring uses `cleavage_rule.p1_prime_preferences`.
- **Disulfide/cysteine logic is internally consistent.**
  - Uricase: 4 cysteines, 0 known disulfides → 4 free cysteines.
  - Lactoferrin: code passes mature sequence only and hard-codes 16 disulfides → 32 mature cysteines, 0 free cysteines.
- **Mass balance / physiologic-rate closure is intentionally out of scope.** This comp is a sequence/cassette compatibility analysis, not a physiological urate-consumption model. It should not be used as evidence of luminal efficacy, dose sufficiency, oxygen closure, or serum-urate reduction.
- **Safety/handling closure is partial but appropriately caveated for this comp.**
  - Free-Cys aggregation risk is flagged.
  - H₂O₂/oxygen/exposure/residence-time are not modeled here and are deferred to §1.33/§1.36.
  - KEX2 structural accessibility is not modeled; output labels KEX2 scoring as conservative sequence-level extrapolation.

## Summary-fidelity audit

### Clean or mostly consistent

- `outputs/cassette_analysis.json` and `outputs/summary.md` agree on the newly added mutant KEX2 result:
  - WT: 2 KR sites, overall HIGH.
  - Mutant: 2 KR sites, overall HIGH.
  - Site change: position 130 P1′ I / HIGH → R / MODERATE.
- The corrected total disulfide count in `outputs/summary.md` is now 16, not 17.
- The README reproduction path was corrected to `cd wiki/etc/experiments/...`.
- `uricase-variant-selection.md` already includes the key 2026-07-14 mutant refinement and is broadly consistent with the new output.

### Mismatches / stale or overstrong wording

- **`wiki-archive.md` is stale.** It is the archived full interpretive page pointed to by the top-level stub, but it still says:
  - 2 internal KR sites, positions 130 and 138, both HIGH.
  - If moved to fusion, double KR→KQ mutation at positions 130 and 138 is required.
  - Add ALLN-346 mutations as recommendation, without the newly added second-sequence analysis.
  This is now incomplete for the recommended P78609+ALLN-346 construct.
- **`outputs/summary.md` has internal tension.**
  - Section 3.2 says if §1.33 selects fusion architecture, KR→KQ mutations at BOTH positions 130 and 138 are required.
  - Section 3.8 later says I132R changes the position-130 site from HIGH to MODERATE and the WT plan shifts.
  - The correct reconciled language should be: for the ALLN-346 mutant, position 138 remains HIGH; position 130 is reduced but not abolished, so it may still need mutation or empirical monitoring if a KEX2-fusion topology is selected.
- **`outputs/cassette_analysis.json` main comparison objects remain WT-only without clear labeling.**
  - `comparison.cutilis_harder_than_aflavus` says positions 130 and 138 are both HIGH.
  - `combined_burden.c_utilis_vs_aflavus_material_differences` says positions 130 HIGH + 138 HIGH.
  - Separate mutant fields correct this, but downstream readers of the primary comparison object may miss the refinement.
- **`README.md` is stale relative to the new artifact.**
  - It lists seven analyses, not the added second sequence.
  - It states positions 130 and 138 are both HIGH without noting that the recommended ALLN-346 construct changes 130 to MODERATE.
- **`computational-experiments.md` partially reflects the result but under-specifies it.**
  - It says “ALLN-346 mutation I132R adjacent to position 130 KR.”
  - The load-bearing point is stronger and more specific: I132R is the P1′ residue of the position-130 KR site and reduces the sequence-level risk classification from HIGH to MODERATE.
- **Top-level corpus propagation could not be fully searched.** The repo search tool failed due to missing `rg`; therefore pages not explicitly included in the bundle may still contain stale “both KR sites HIGH / double KR mutation” language.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/README.md` | Tracked artifact / summary-facing README | Yes | Reproduction path fixed. Stale with respect to added ALLN-346 second-sequence analysis; still WT-oriented and says both KR sites HIGH. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/analyze.py` | Executable analysis code | Yes, by supplied artifact | New mutant block is plausible; code not executed. Main combined/comparison results still use WT P78609. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/P02788.fasta` | Input sequence | Yes | Human lactoferrin sequence present; signal peptide handled in code. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/P78609.fasta` | Input sequence | Yes | P78609 sequence supports the asserted ALLN mutations and I132R/P1′ geometry. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/a_oryzae_codon_usage.json` | Input JSON | Yes | Used for CAI/RSCU. Rare-codon documentation and code logic are not identical; not headline-load-bearing. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/glucoamylase_carrier.fasta` | Input sequence | Yes | Present but not used by `analyze.py` in the displayed implementation; documentation/supporting carrier input. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/kex2_site_specs.json` | Input JSON | Yes | P1′ preferences used for KEX2 scoring; other linker/risk fields are documentation/specification. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/provenance.md` | Input provenance | Yes | Provides source/citation strings and limitations. Primary sources/patent not independently verified in this review. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/cassette_analysis.json` | Generated output | Yes | Contains correct mutant delta, but primary combined/comparison objects remain WT-centered and can propagate stale “130 HIGH” wording. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/summary.md` | Generated human summary | Yes | Contains new §3.8 mutant analysis but earlier sections still overstate “mutate both 130 and 138” for fusion without reconciling the ALLN-346 case. |
| `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/wiki-archive.md` | Archived interpretive wiki / proposed summary surface | Yes | Stale; does not include the second-sequence mutant analysis and still states both sites HIGH / double mutation required. Requires update or explicit frozen-obsolete note. |
| `wiki/computational-experiments.md` | Explicit referencing wiki page | Partially, relevant comp-011 section inspected | Entry is broadly consistent but should update “I132R adjacent” to “I132R is P1′ and reduces 130 HIGH→MODERATE.” |
| `wiki/uricase-variant-selection.md` | Affected wiki page read via tool | Yes, relevant sections | Already contains the mutant refinement and is mostly consistent. |
| `wiki/validation-experiments.md` | Affected wiki page read via tool | Partially, relevant §1.9 region inspected | Correctly stages §1.33 before §1.9 and treats UOX topology as unresolved. No direct mutant-specific mismatch found in inspected region. |
| `wiki/hypotheses/H01-ward-dual-cassette.md` | Affected hypothesis page read via tool | Partially, relevant framing inspected | Correctly stages H01 downstream of §1.33. No direct comp-011 mutant mismatch found in inspected region. |
| `wiki/koji-endgame-strain.md` | Affected wiki page read via tool | Partially before tool budget exhaustion | General platform page reflects §1.33 staging. Full mutant-specific scan not completed due tool budget. |
| `wiki/chaperone-orthogonal-stacking.md` | Affected wiki page | No | Tool-result budget exhausted before content returned; wiki-archive claims a mirrored C. utilis free-Cys/PDI note exists, but I could not verify it. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| P78609 is 303 aa *C. utilis* / *Cyberlindnera jadinii* uricase | `inputs/P78609.fasta`, `provenance.md` | Sequence used for WT and mutant analyses | UniProt citation string present; not independently fetched | Plausible; primary-source verification not performed here |
| ALLN-346 mutations are E51K, A87G, I132R, Y165F, I180V, V190G, Q244K | `analyze.py`, `outputs/cassette_analysis.json`, `provenance.md` | Applied to P78609 via `apply_mutations()` | Patent citation string present; exact Allena parent sequence disclosed as uncertain | Mutation positions match P78609; exact parent-sequence uncertainty remains |
| I132R changes position-130 KEX2 site from KRI to KRR | `analyze.py`, `outputs/cassette_analysis.json`, `outputs/summary.md` | Mutant KEX2 analysis | Verified against supplied P78609 sequence | Correct by inspection |
| WT position 130 KEX2 site = HIGH, P1′ I | `outputs/cassette_analysis.json`, `outputs/summary.md` | KEX2 risk scoring | Rule source is citation string to Kex2 literature | Internally correct under implemented rule |
| Mutant position 130 KEX2 site = MODERATE, P1′ R | `outputs/cassette_analysis.json`, §3.8 summary | KEX2 delta result | Rule source is citation string to Kex2 literature | Internally correct under implemented rule |
| Position 138 remains HIGH, P1′ S | `outputs/cassette_analysis.json` | KEX2 risk scoring | Rule source citation string | Correct under implemented rule |
| Overall mutant KEX2 risk remains HIGH | `outputs/cassette_analysis.json`, `outputs/summary.md` | Mutant result | Derived from at least one HIGH site | Correct |
| Uricase KEX2 sites are non-load-bearing under direct secretion | `analyze.py`, `outputs/summary.md` | `uricase_kex2_is_load_bearing = False` | Design assumption; not empirically verified | Acceptable as candidate-specific assumption, but not a general Ward-fusion answer |
| If fusion topology selected, WT double mutation 130 + 138 would be needed | `outputs/summary.md`, `wiki-archive.md` | Recommendation language | Derived from WT KEX2 scoring | Correct for WT; stale/overstrong for ALLN-346 mutant |
| If fusion topology selected for ALLN-346 mutant, position 130 is “handled” by I132R | §3.8 interpretation and `uricase-variant-selection.md` | Recommendation refinement | Derived from sequence-level KEX2 scoring only | Needs softer wording: reduced, not abolished; may still require mutation/monitoring |
| C. utilis codon burden HEAVY, CAI proxy ~0.65 | `analyze.py`, JSON, summary | CAI proxy from amino-acid preferred-codon table | Codon table/provenance citation strings; no primary verification | Mechanistic proxy; conclusion plausible but not CDS analysis |
| Lactoferrin codon burden LOW by proxy but full optimization recommended in practice | JSON, summary | CAI proxy says LOW | Practical recommendation not derived from code | Needs clear distinction; not a comp-011 headline blocker |
| C. utilis uricase has 4 cysteines and 0 annotated disulfides | `analyze.py`, JSON, summary, provenance | Free-Cys risk flag | UniProt annotation cited; not independently verified | Internally correct for supplied sequence; annotation not primary-verified here |
| Lactoferrin has 16 mature disulfides | `analyze.py`, JSON, summary, provenance | Dual disulfide load = 16 | Notari 2023 citation string; not independently verified | Internally consistent |
| Dual disulfide load = 16, all on Lf | JSON, summary | Huynh comparator | Derived from hard-coded disulfides | Correct under hard-coded inputs |
| H₂O₂, oxygen, residence time, physiologic urate access are not resolved here | Summary limitations; validation §1.33/§1.36 | Out-of-scope constraints | Corpus staging partially inspected | Correct; comp-011 must not be cited as physiological efficacy evidence |
| README reproduction command | `README.md` | `python3 analyze.py` from experiment dir | Not executed | Plausible stdlib-only path; determinism not independently reproduced |

## Affected wiki pages

- `wiki/c-utilis-uricase-cassette-compatibility-computational.md` — **change required** — top-level stub points to `wiki-archive.md`; the archive is now stale relative to the new mutant analysis.
- `wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/wiki-archive.md` — **change required** — full archived analysis still says both KR sites HIGH and double mutation required, with no ALLN-346 second-sequence section.
- `wiki/computational-experiments.md` — **change required** — comp-011 entry should state I132R is the P1′ residue of the position-130 KR site and reduces HIGH→MODERATE, not merely “adjacent.”
- `wiki/uricase-variant-selection.md` — **already consistent / mostly reconciled** — contains the 2026-07-14 mutant analysis and correct HIGH→MODERATE refinement. Minor wording should avoid implying position 130 is fully solved under fusion.
- `wiki/validation-experiments.md` — **already consistent in inspected sections** — §1.9 correctly defers UOX topology to §1.33. No mutant-specific correction found in inspected region.
- `wiki/hypotheses/H01-ward-dual-cassette.md` — **already consistent in inspected sections** — correctly stages H01 downstream of §1.33; no mutant-specific stale claim found in inspected region.
- `wiki/koji-endgame-strain.md` — **not fully verified** — partial inspection confirms current §1.33 staging; full mutant-specific search could not be completed due tool budget.
- `wiki/chaperone-orthogonal-stacking.md` — **unverified** — bundle omitted page and tool budget exhausted. `wiki-archive.md` claims a mirrored C. utilis variant note exists; this needs verification in a follow-up propagation pass.
- Potential additional pages containing `ALLN-346`, `C. utilis`, `P78609`, `130 + 138`, or “both HIGH” — **unverified / change may be required** — fixed-string search failed because `rg` is missing in the tool environment.

## New connections or implications

- The ALLN-346 mutation set has a **cassette-topology implication**, not just a gut-protease/stability implication. I132R sits exactly at the P1′ residue of the position-130 KEX2 site, so a future glucoamylase-KEX2 fusion design for P78609+ALLN-346 is not the same as WT P78609.
- The mutant result does **not** make KEX2 risk disappear. It converts one site from HIGH to MODERATE while position 138 remains HIGH. Therefore, a fusion topology still needs explicit KEX2 mitigation/monitoring; the mitigation burden is reduced, not eliminated.
- The experiment reinforces the importance of keeping **sequence candidate** and **topology candidate** separate: WT P78609, P78609+ALLN-346, direct secretion, and fusion secretion are four different design states. Several artifact sections still collapse them into one “C. utilis” statement.

## Required actions

1. **Reconcile `wiki-archive.md` with the new mutant analysis.**  
   Verification criterion: archive contains an ALLN-346 second-sequence section or an explicit note that the archive is frozen/obsolete relative to `outputs/summary.md`; no unqualified “both 130 and 138 HIGH / mutate both” language remains for the recommended P78609+ALLN-346 construct.

2. **Update `README.md` to mention the added ALLN-346 mutant analysis.**  
   Verification criterion: README key results distinguish WT P78609 KEX2 scoring from P78609+ALLN-346 scoring and point readers to the mutant JSON/summary section.

3. **Reconcile `outputs/summary.md` internal wording.**  
   Verification criterion: earlier KEX2 recommendation section says WT requires attention at 130+138, while ALLN-346 reduces position 130 to MODERATE but does not abolish it; position 138 remains HIGH. Avoid implying I132R fully solves position 130 under a fusion topology.

4. **Clarify JSON summary fields or add labels separating WT comparison from mutant comparison.**  
   Verification criterion: primary `combined_burden`/`comparison` fields are clearly labeled as WT P78609, or corresponding mutant-adjusted comparison fields are added for the recommended P78609+ALLN-346 construct.

5. **Update `wiki/computational-experiments.md` comp-011 entry.**  
   Verification criterion: entry states that I132R is the P1′ residue of the position-130 KR site and reduces the KEX2 classification from HIGH to MODERATE; it should not only say “adjacent.”

6. **Run a corpus-wide propagation audit using a working search tool.**  
   Verification criterion: pages containing `ALLN-346`, `P78609`, `C. utilis`, `130 + 138`, `both HIGH`, `double KR`, or `KRI` are checked and reconciled, especially omitted pages such as `chaperone-orthogonal-stacking.md` and `koji-endgame-strain.md`.

7. **Preserve the primary-source verification boundary.**  
   Verification criterion: summaries continue to say that US10815461B2 discloses the mutation set but exact ALLN-346 parent sequence is not available; avoid wording that implies the exact clinical ALLN-346 full sequence was primary-verified.

## Review limits

- I did not execute `python3 analyze.py`; reproducibility is assessed by inspection only.
- Primary sources were not independently fetched or verified. UniProt, patent, Ward/Huynh/Rockwell/Brenner/Notari claims are reviewed as artifact-provided provenance/citation strings.
- Repository `grep_repo` failed because `rg` is not installed, so mechanism-wide corpus search was incomplete.
- Tool-result budget was exhausted before I could fully inspect `chaperone-orthogonal-stacking.md` and all omitted reference pages.
- Large affected pages were inspected only in relevant sections where tool output allowed.
- No medical or clinical inference is made; this remains Phase 0 in silico cassette-design review.
