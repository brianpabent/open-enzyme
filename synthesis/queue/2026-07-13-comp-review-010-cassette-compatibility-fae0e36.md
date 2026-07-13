---
type: comp-review
sweep_date: 2026-07-13
sweep_sha: fae0e36
comp: comp-010
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-010

Canonical review log: [`logs/comp-reviews/2026-07-13-comp-010-fae0e36.md`](../../logs/comp-reviews/2026-07-13-comp-010-fae0e36.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-010

## Bottom-line verdict
Action required — the **narrow sequence-level LOW verdict is mostly supported for the stated asymmetric candidate** (direct-secreted *A. flavus* UOX + glucoamylase-KEX2 hLf), but the artifact-summary contract is not clean. Several committed surfaces remain stale or internally inconsistent, the reproducibility links/paths are partly broken, and the implementation leaves important design choices as hard-coded substitutions rather than analyzed conclusions.

This comp should be read as: **“No obvious sequence-level blockers for one candidate architecture.”** It does **not** resolve UOX topology, physiological urate/O₂/H₂O₂ feasibility, solid-state secretion, ER capacity for lactoferrin, or dual-strain therapeutic sufficiency.

## Implementation and constraint closure

I traced the supplied `analyze.py`, inputs, JSON output, summary, README, provenance, interpretive archive, and key referenced wiki pages available in the bundle. I also inspected omitted high-impact pages (`H01`, `chaperone-orthogonal-stacking`, `koji-endgame-strain`, `lactoferrin` partially, `uricase-variant-selection` attempted but tool budget ended). Repository grep failed because the backend `rg` binary was unavailable, so corpus-wide search coverage is incomplete.

**What the code actually does**
- Loads:
  - `Q00511.fasta`
  - `P02788.fasta`
  - `a_oryzae_codon_usage.json`
  - `kex2_site_specs.json`
- Does **not** load or analyze `glucoamylase_carrier.fasta`, despite the experiment question invoking Ward 1995 glucoamylase-KEX2 architecture. The carrier is present as an input/provenance object but not part of the executable model.
- Hard-codes:
  - `URICASE_SP_END = 0`
  - `LF_SP_END = 19`
  - `URICASE_DISULFIDES = 0`
  - `LF_DISULFIDES = 16`
  - Huynh baseline = 16 disulfides and 39.7 mg/L
  - OE targets = 500 mg/L Lf and 100 mg/L uricase
  - `uricase_kex2_is_load_bearing = False`
- Computes:
  - amino-acid-level codon proxy, not CDS-level codon adaptation;
  - mature-sequence KR sites and P1′ risk;
  - simple routing motif scan;
  - disulfide-load index;
  - N-X-S/T sequons;
  - deterministic combined burden and Huynh comparison.

**Stored-but-unused / implementation-closure findings**
- `glucoamylase_carrier.fasta` is unused. This is acceptable only if comp-010 is explicitly framed as a **payload sequence screen**, not as an analysis of the full Ward fusion cassette.
- In `kex2_site_specs.json`, the code uses `cleavage_rule.p1_prime_preferences` but not:
  - `canonical_sequence`
  - `cleavage_occurs_after`
  - `huynh_2020_validated_linker`
  - `internal_kr_site_risk`
  - `alternative_linkers`
  These appear documentation-only or design-context fields, not executable inputs.
- In `a_oryzae_codon_usage.json`, the code uses `rare_codon_definition.rscu_threshold` only. It ignores `freq_threshold`, `rare_codons_list`, and the JSON text saying rare codons require both RSCU and frequency logic. Because the codon analysis is already a weak amino-acid proxy, this does not overturn the cassette verdict, but it is an implementation/provenance mismatch that should be reconciled.
- The codon module reports lactoferrin burden `LOW`, then the summary correctly says this is a methodological artifact and full *A. oryzae* optimization remains required. The implementation therefore should not be used as independent evidence that native human LTF CDS is compatible.
- Uricase KEX2 risk is suppressed by a hard-coded architecture assumption (`uricase_kex2_is_load_bearing = False`). This is valid only within the direct-secretion candidate and becomes invalid if §1.33 selects a fusion topology.
- Routing risk (`uricase` C-terminal `SKL`) is reported but not included as a combined-risk driver. That is acceptable for “sequence-level candidate generator,” but not for declaring the platform topology safe.
- Lactoferrin mature cysteine counting is corrected in the code (`lf_seq[LF_SP_END:]` → 32 Cys, 16 disulfides), but some documentation surfaces remain stale.
- `analyze.py` comment still says “Uricase Q00511: no Cys,” while the sequence/output correctly show 3 cysteines and 0 disulfides. This is a non-output code-comment error but should be fixed.

**Constraint closure**
- Uricase reaction substrates/products are **not modeled**: urate + O₂ + H₂O → allantoin/CO₂ + H₂O₂. No finite substrate pool, Km, oxygen availability, peroxide scavenging, product formation, exposure window, residence time, or host viability is represented here.
- Physiological substrate concentration and UOX operating regime are explicitly outside this comp and delegated to §1.33 / comp-044 / comp-045. This is now mostly reflected in validation/H01/koji pages.
- Lactoferrin folding constraints are only represented by bulk disulfide count and glycosylation sequons. Iron, bicarbonate, apo/holo state, actual ER residence time, and architecture-specific folding kinetics are not modeled in the code.
- The Huynh comparison is a **bulk-count comparator**, not a quantitative ER-capacity proof. The broader corpus’s chaperone page correctly introduces architecture coefficients in many places, but it still contains stale 17-disulfide language in the triple-cassette section.
- Localization/transport:
  - Uricase `SKL` PTS1 is detected, but whether amyB signal peptide overrides it is a wet-lab question.
  - Lactoferrin fusion cleavage and internal KR site accessibility are not structurally modeled.
- Safety/off-targets:
  - H₂O₂ burden, local peaks, antioxidant loss, redox burden, and host viability are not modeled.
  - Fungal glycan immunogenicity/allergenicity claims are literature-derived context, not computed.
- Sensitivity ranges:
  - There is no sensitivity sweep. Dominant uncertainties — UOX topology, O₂, peroxide, substrate concentration, solid-state secretion, PDI/ERO1 capacity, KEX2 accessibility — are not explored by this code.

## Summary-fidelity audit

**Internally consistent surfaces**
- `outputs/cassette_analysis.json` appears consistent with the current code and trigger diff:
  - Lf mature cysteines = 32
  - Lf disulfides = 16
  - dual disulfide load = 16
  - load index = 1.0
  - UOX KR128 marked informational only within direct secretion
- `outputs/summary.md` mostly matches the JSON and current intended interpretation.
- `README.md` largely reflects the reframed candidate-generator stance.
- `wiki/computational-experiments.md` entry is materially reconciled: LOW sequence-level risk, 16 disulfides, topology not selected.
- `wiki/validation-experiments.md` §1.9 is materially reconciled: §1.33 first, Lf-only → selected UOX-only → dual-cassette, saturating UOX activity not a physiological pass.
- `wiki/hypotheses/H01-ward-dual-cassette.md` is materially reconciled: comp-010 is design support, not a killshot; topology and physiological gate remain upstream.
- `wiki/koji-endgame-strain.md` is mostly reconciled: §1.33 upstream, 16 Lf disulfides, architecture-adjusted PDI burden acknowledged.
- `wiki/aspergillus-oryzae.md` is mostly reconciled: 16 disulfides and “bulk count not capacity proof” are stated.

**Mismatches / stale or broken surfaces**
- `outputs/summary.md` cross-reference links are broken relative to the actual file location. From `wiki/etc/experiments/comp-010-cassette-compatibility/outputs/`, links like `../../wiki/hypotheses/H01...` do not resolve to `wiki/hypotheses/...`. The previous/README-style relative paths are also not uniformly correct from the `outputs/` subdirectory. The generator should be fixed.
- `README.md` reproduction command says:
  - `cd experiments/comp-010-cassette-compatibility`
  but the tracked path is:
  - `wiki/etc/experiments/comp-010-cassette-compatibility`
- `inputs/provenance.md` says Q00511 length is **301 aa**, while the FASTA and output show **302 aa**. The output position logic uses the 302-aa sequence; provenance is stale.
- `wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md` still contains stale/stronger statements:
  - Lf cysteine count table shows **33** and combined cysteines **36**, inconsistent with mature-count output (32 Lf, 35 combined with UOX cysteines).
  - It says Lf’s 16 disulfides “fall within the demonstrated capacity” of NSlD-ΔP10 ER folding machinery, which is stronger than the corrected interpretation. The corrected stance is “bulk-count comparator; architecture-specific capacity remains empirical.”
  - It also includes older design recommendations that read more like direct-secretion UOX is selected, though later passages soften this.
- `wiki/chaperone-orthogonal-stacking.md` still contains stale `17 disulfides` language in the triple-cassette setup section and internal arithmetic inconsistency around “0 + 16 + 8 = 24.” This page must be corrected because it is the main architecture-adjusted PDI framework and is repeatedly cited as the reason bulk equality is insufficient.
- `wiki/cassette-compatibility-computational.md` is a stub and is fine as a pointer, but because it points to `wiki-archive.md`, the archive’s stale content matters.
- Some wording in the artifact still risks over-reading:
  - “Overall dual-cassette secretion burden: LOW” can be misread as physiological/ER-capacity closure unless always paired with “sequence-level candidate architecture only.”
  - The code’s `overall_dual_cassette_risk = LOW` ignores the moderate UOX routing risk by design. That is acceptable only under the current limited question.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 uricase sequence = 302 aa | `inputs/Q00511.fasta`; `outputs` sequence_length 302 | Directly loaded for all UOX analyses | Provenance says 301 aa, conflicting with FASTA/output | **Change required** — fix provenance |
| P02788 lactoferrin sequence = 710 aa with signal peptide 1–19 | `inputs/P02788.fasta`; `LF_SP_END = 19` | Used for mature KEX2/glycan scan and mature disulfide count | Provenance names UniProt; primary not directly verified here | Plausible; primary-source verification unresolved |
| Lf mature cysteine count = 32 | `analyze.py` passes `lf_seq[19:]`; JSON disulfide section | Used in disulfide/free-Cys calculation | Provenance cites Notari 2023 and signal-peptide cysteine correction | Supported by artifact logic; archive stale |
| Lf disulfide bonds = 16 | `LF_DISULFIDES = 16`; JSON/summary | Load-bearing for Huynh ratio | Citation string to Notari 2023; primary not directly verified in this review | Plausible but primary-source verification unresolved |
| Uricase disulfides = 0 | `URICASE_DISULFIDES = 0`; JSON | Sets UOX PDI load to zero | Provenance says UniProt; code comment wrongly says “no Cys” though sequence has 3 Cys | Output likely correct; comment/provenance wording should be fixed |
| Huynh baseline = 16 disulfides | `huynh_baseline_disulfides = 16`; JSON | Denominator for folding load index | Citation string to Huynh 2020; primary not directly verified here | Plausible; only bulk comparator |
| Huynh titer = 39.7 mg/L | `analyze_combined_burden`; JSON | Titer gap calculation | Citation string to Huynh 2020 | Plausible; primary verification unresolved |
| Lf target = 500 mg/L | `analyze_combined_burden`; JSON/summary | Titer-gap numerator | Comes from H01/OE validation design, not computed | Design target, not evidence |
| Uricase target = 100 mg/L | `analyze_combined_burden`; JSON | Context only | Design target | Not physiologically validated by comp-010 |
| Ward 1995 Lf >2 g/L | summary/wiki text | Used to argue Huynh is not Lf ceiling | Citation string only | Primary verification unresolved; should remain “protein-specific precedent,” not capacity proof |
| Uricase KR128, P1′=N, HIGH if fusion | `analyze_kex2_sites`; JSON | Load-bearing only if fusion topology selected | Derived from FASTA + KEX2 rules | Supported by implementation; topology-dependent |
| Lf KR sites: mature 38 P1′=D low; mature 579 P1′=K moderate | `analyze_kex2_sites`; JSON/summary | Supports Lf KEX2 moderate risk | Derived from FASTA + KEX2 rules | Supported by implementation; accessibility unmodeled |
| KEX2 P1′ rules | `kex2_site_specs.json`; code uses preferences | Drives HIGH/MODERATE/LOW KR classification | Sources named: Bathurst, Rockwell, Brenner, Huynh, Ward | Secondary/citation-level only in artifact; *A. oryzae* kexB specificity unresolved |
| Uricase C-terminal `SKL` PTS1 | `analyze_secretion_targeting`; JSON | Produces MODERATE routing note | Sequence-derived; motif consensus not externally verified | Supported as motif flag; functional relevance untested |
| Uricase NFS sequon at 191 | `predict_nxst_sites`; JSON | Counts one UOX NXST site | Sequence-derived; occupancy not verified | Supported as upper-bound sequon, not glycosylation evidence |
| Lf N-glycan sites | `predict_nxst_sites`; JSON maps full 156/497/642 to mature 137/478/623 | Supports 3-site glycan burden | Provenance calls them N137/N478/N623; numbering ambiguous | Implementation plausible, but labels should clarify full vs mature numbering |
| Codon burden LOW | `analyze_codon_usage`; JSON | Included in combined LOW risk | Uses amino-acid preferred-codon proxy; not CDS | Weak proxy only; should not support native-CDS compatibility |
| Rare-codon threshold | `a_oryzae_codon_usage.json` vs code | Code uses RSCU only | JSON includes freq threshold/list/logic not used | **Change required** — align code and provenance or document |
| Direct-secretion UOX topology | hard-coded `uricase_kex2_is_load_bearing = False` | Suppresses UOX KR128 from combined risk | Candidate assumption, not selected by comp-010 | Valid only as candidate; must not propagate as selected topology |
| Glucoamylase carrier sequence | `inputs/glucoamylase_carrier.fasta` | Not used | Provenance provided | Stored-but-unused; either document as context or analyze if claiming full cassette compatibility |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — comp-010 entry reflects 16 disulfides, topology not selected, §1.33/§1.9 split.
- `wiki/validation-experiments.md` — already consistent — §1.9 is staged after §1.33; comp-010 prior is framed as sequence-level only.
- `wiki/hypotheses/H01-ward-dual-cassette.md` — already consistent — comp-010 is design support, not a killshot; topology and physiological UOX system remain open.
- `wiki/koji-endgame-strain.md` — already consistent overall — it incorporates the 16-disulfide correction and the architecture-adjusted PDI caveat.
- `wiki/aspergillus-oryzae.md` — already consistent overall — it states 16 bulk disulfides and warns count equality is not ER-capacity proof.
- `wiki/cassette-compatibility-computational.md` — change required indirectly — stub is okay, but it points to `wiki-archive.md`, whose content is stale.
- `wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md` — change required — stale cysteine counts and stronger ER-capacity language remain.
- `wiki/chaperone-orthogonal-stacking.md` — change required — stale `17 disulfides` language remains in the triple-cassette section and should be reconciled with the 16-disulfide Notari correction.
- `wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md` — change required — generated cross-reference links are broken relative to the output file path.
- `wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md` — change required — Q00511 length conflicts with FASTA/output.
- `wiki/etc/experiments/comp-010-cassette-compatibility/README.md` — change required — reproduction command path omits `wiki/etc/`.

## New connections or implications
- **KR128 is now a topology discriminator.** comp-010’s UOX KR128 site is harmless only in direct secretion. If §1.33 selects any glucoamylase-KEX2/fusion UOX topology, comp-010 flips from “informational” to “actionable redesign” for UOX.
- **Lf-alone §1.9A is the real ER-capacity calibration point.** The corrected 16-disulfide bulk equality to Huynh does not settle capacity; the chaperone-orthogonal framework’s transferrin-lobe α coefficient makes Lf’s effective PDI load potentially higher than IgG despite equal count.
- **comp-022 refinements complement comp-010 but do not supersede §1.33.** PTS1-blocking tag and N191Q are sensible gene-synthesis refinements if a secreted koji UOX topology survives, but neither proves secreted UOX is physiologically viable.
- **Codon analysis should become a post-vendor-CDS QC, not a biological conclusion.** The current protein-level CAI proxy is too weak to support actual gene-design decisions beyond “do full *A. oryzae* optimization for hLf.”

## Required actions
1. Fix generated cross-reference links in `outputs/summary.md` / `write_summary()` and correct the README reproduction path. Verification: links resolve from the committed file locations in a fresh clone.
2. Correct `inputs/provenance.md` for Q00511 length and fix the stale `analyze.py` comment saying uricase has no cysteines. Verification: provenance, FASTA length, and JSON output agree.
3. Reconcile `wiki-archive.md` with current outputs: Lf mature cysteines = 32, combined cysteines = 35, Lf disulfides = 16, no “demonstrated capacity” wording beyond bulk-count contextual precedent. Verification: archive matches `cassette_analysis.json` and uses the same limited verdict language.
4. Reconcile `wiki/chaperone-orthogonal-stacking.md` stale 17-disulfide references and all dependent arithmetic. Verification: all Lf disulfide counts on that page are 16 unless explicitly discussing historical errors.
5. Decide and document the codon rare-codon rule. Either implement the JSON-stated RSCU+frequency/list logic or simplify the JSON/provenance to the code’s RSCU-only rule, then rerun outputs if any output changes. Verification: no unused contradictory rare-codon definition remains.
6. Clarify the role of `glucoamylase_carrier.fasta`: either mark it explicitly as provenance/context-only or add an analysis of carrier/fusion context if the experiment continues to ask whether the full Ward architecture works “out of the box.” Verification: README question, input list, and code scope agree.
7. Before future propagation, primary-source-check the load-bearing literature numbers used as evidence anchors: Notari 2023 Lf 16 disulfides, Huynh 2020 39.7 mg/L and 16-disulfide comparator, Ward 1995 >2 g/L Lf, and KEX2 P1′ rules. Verification: artifact provenance distinguishes “primary verified” from “citation string only.”

## Review limits
- I did not execute `analyze.py`; reproducibility was assessed by inspection.
- Repository grep failed because the tool backend could not find `rg`; affected-page search is therefore incomplete.
- I inspected several omitted high-impact pages with `read_file`, but tool-result budget truncated `chaperone-orthogonal-stacking.md` and `lactoferrin.md`, and prevented further file inspection.
- I did not verify primary papers externally; literature values are treated as citation/provenance claims unless directly present in the artifact.
- No clinical or therapeutic efficacy conclusion is drawn. This remains Phase 0 in silico sequence/cassette design support.
