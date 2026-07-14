---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-034
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-034

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-034-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-034-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-034

## Bottom-line verdict

**Action required — root comp-034 verdict is stale and materially superseded by its own later ProteinMPNN and Rosetta/PyRosetta extensions.** The original 2026-05-16 substitute-sampler result is reproducible by inspection as a deterministic pilot, but it does **not** support the current wet-lab recommendation after the 2026-05-19 genuine ProteinMPNN rerun and 2026-05-30 Rosetta/structure-gated cleavage extension. The strongest supported in-silico recommendation is no longer the root README’s `EEEEPAARRAR` proline double-mutant; it is the MPNN-native helix-preserving `NEEEQQQEEEQ` / sibling `NEEEQEEQDQQ` class, with proline arms demoted.

## Implementation and constraint closure

I traced the root `analyze.py`, committed root outputs, later `proteinmpnn_rerun` scoring, and `rosetta_concordance` scripts/results.

Key closure findings:

- **Original question/model fit is only partial.**
  - The stated question is “reduce predicted shio-koji protease cleavage while preserving lobe-lobe geometry and codon compatibility.”
  - Root `analyze.py` does **not** directly model lobe-lobe geometry. It substitutes:
    - a hand-coded local pLDDT penalty model for linker “loop” behavior;
    - a full-protein ESM2 “pseudo-pLDDT” weighted average, not ESM2/ESMFold;
    - top-quintile concordance, not an absolute biophysical threshold.
  - The original “loop flexibility” metric is physically mis-aimed for this target because the WT linker is a high-confidence **helix**, not a flexible loop. The later Rosetta extension correctly reframes the objective as **preserve protective helix while stripping protease-preferred residues**, not “proline-rigidify / make a loop.”

- **Stored-but-unused / hard-coded inputs.**
  - `inputs/linker_residue_range.json` is not loaded by `analyze.py`; linker boundaries, WT sequence, and permitted amino-acid pool are hard-coded.
  - `design_constraints`, `boundary_justification`, `rare_codon_definition`, and several provenance-rich JSON leaves are documentation-only in the root run.
  - This is not fatal because constants match the intended values, but it breaks the apparent input contract: changing `linker_residue_range.json` would not change the computation.

- **Protease scoring closure.**
  - Root cleavage scores call `find_cleavage_sites()` from the shared `protease_stability.py`.
  - That library originally used pLDDT as an accessibility proxy. The current library now carries a caveat from comp-034: high pLDDT ≠ burial. For the lactoferrin linker, real SASA shows exposed helix; root `0.407 → 0.290` scores are therefore sequence/proxy scores, not physical cleavage rates.
  - Later `structure_gated_cleavage.py` and `refold_via_relax.py` substantially improve this by using SASA + DSSP conformation gates. Those later results overturn the proline-arm interpretation.

- **Concordance gate weakness.**
  - Root GREEN = N-of-5 ≥3. WT itself is GREEN despite failing cleavage and loop-pLDDT.
  - Several “GREEN” candidates fail the cleavage metric. Thus GREEN means “passes three metrics,” not “solves cleavage.”
  - The `linker_cleavage_score` top-quintile cutoff is `0.039`; `EEEEPAARRAR` at `0.290` and `EEEEPAAPPAP` at `0.233` fail this metric in root outputs. Their 4/5 status is driven by ESM2 proxy, CAI proxy, loop band, and similarity—not by passing the cleavage top-quintile.

- **CAI metric is mislabeled.**
  - `cai_of_sequence()` always chooses the highest-frequency codon per amino acid, so it is not a conventional CAI over an actual back-translated DNA sequence.
  - It is a geometric mean of best-codon `freq_per1000` values by amino-acid composition. This is a residue-composition codon-favorability proxy, not implemented CAI.

- **ProteinMPNN rerun closure.**
  - The later `proteinmpnn_rerun` artifacts show real MPNN sampling occurred and found constrained-pool STRICT candidates (`NEEEQQQEEEQ`, `NEEEEQQEQEQ`, `NEEEEEQEQEQ` unique sequences).
  - However, candidate counts include duplicates. `shortlist_mpnn.json` reports 5 STRICT records in the constrained pool, but only 3 unique strict linker sequences.
  - The MPNN rerun supersedes the root README claim that 0 candidates pass STRICT, if the experiment is considered as the full committed artifact rather than only root `outputs/`.

- **Rosetta/structure-gated extension closure.**
  - `rosetta_ddg_results_cartesian10.json` and `refold_via_relax_results.json` support the extension’s central claim:
    - `NEEEQQQEEEQ`: ΔΔG_min +0.23 REU, helix 0.818, real-structure gated cleavage 0.388 vs WT 1.143.
    - `NEEEQEEQDQQ`: ΔΔG_min +2.39 REU, helix 0.818, real-structure gated cleavage 0.388.
    - proline arms: ΔΔG_min about +20 to +57 REU and much weaker structure-gated cleavage benefit.
  - This makes the root proline-first recommendation obsolete.
  - Minor metadata mismatch: `rosetta_ddg_results_cartesian10.json` `_meta.method` still says “torsion-space ddG” even though `make_relax()` uses `fr.cartesian(True)` and `ref2015_cart`.

- **Constraint closure.**
  - Reaction substrates/products are not enzyme-catalysis variables here; the relevant “reaction” is protease cleavage of a protein substrate.
  - The root model does not include protease abundance, cleavage kinetics, finite ferment residence time, full shio-koji proteome, glycosylation shielding, secretion processing, iron saturation, or actual wet-lab exposure.
  - Later Rosetta improves localization/access by using actual structure-derived SASA and secondary structure, but it remains in silico and local-relax-on-AF-backbone, not an independent full-protein fold prediction or proteolysis assay.
  - Immunogenicity/neoepitope risk for low-identity MPNN variants is flagged but not modeled.

## Summary-fidelity audit

The artifact-summary contract is not clean.

- **Root `README.md` / `outputs/summary.md` / `outputs/shortlist.json`: stale relative to committed later artifacts.**
  - They still report: 15/60 GREEN, 0 STRICT, primary `EEEEPAARRAR`, secondary `SEEEPAARRAR`, aggressive `EEEEPAAPPAP`.
  - This was superseded by genuine MPNN and Rosetta concordance, which elevate `NEEEQQQEEEQ` / `NEEEQEEQDQQ` and demote proline arms.
  - Root output files were not regenerated or clearly marked as “v1 substitute-sampler only; superseded.”

- **Interpretive page `wiki/lactoferrin-linker-redesign-computational.md`: internally inconsistent.**
  - Top callouts correctly describe the 2026-05-19 MPNN rerun and 2026-05-30 physics inversion.
  - But the retained headline text still says primary wet-lab variant `EEEEPAARRAR`, secondary `SEEEPAARRAR`, aggressive `EEEEPAAPPAP`, and the final “Evidence level” paragraph still recommends “WT control + V357P conservative + DEEDPANPQAH aggressive.”
  - The page therefore contains both the superseding result and the old recommendation.

- **`wiki/computational-experiments.md`: stale.**
  - The comp-034 index entry still reports the original substitute-sampler pilot: `EEEEPAARRAR` primary, 15/60 GREEN, 0 STRICT.
  - It does not propagate the MPNN STRICT candidates or the Rosetta inversion of wet-lab priority.

- **`wiki/validation-experiments.md §1.10`: mostly reconciled but still has local inconsistencies.**
  - The linker-variant arm correctly elevates `NEEEQQQEEEQ` as primary and demotes proline arms.
  - But the subsection says “4-lane gel” and then lists 5 lanes.
  - The section header cost still says `$600–1,100`, while the estimated-cost paragraph says `$2,460–4,460` after adders.
  - These are not scientific reversals, but they are summary-contract errors.

- **`wiki/etc/bio-ai-tools.md`: stale workflow language.**
  - It still says structured-mandatory connectors should use “proline substitution” and “loop flexibility lower is better.”
  - Comp-034’s own physics extension showed this was the wrong lesson for a structured helix. The general pattern should say: classify secondary structure first; for structured helices, prefer protease-preference stripping while preserving secondary structure, and treat proline as risky unless the connector is genuinely flexible/removable.

- **`wiki/etc/autonomous-screening-methodology.md`: already reconciled on the pLDDT-accessibility proxy.**
  - It correctly records the comp-034 lesson that pLDDT is not burial and that real SASA should replace the proxy for load-bearing accessibility.

- **`wiki/lactoferrin.md`: boundary issue already surfaced in comp provenance but still likely needs correction.**
  - It says hLf N-lobe residues 1–333 and C-lobe 345–703 in mature numbering, while UniProt precursor length 710 with signal peptide 1–19 implies mature length 691.
  - The lobe boundary around 333/345 is usable for the linker, but mature C-terminal numbering appears wrong.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| WT linker is UniProt P02788 residues 353–363, `SEEEVAARRAR` | `analyze.py` constants; `inputs/P02788.fasta`; `inputs/linker_residue_range.json`; `inputs/provenance.md` | `assert extracted_wt_linker == WT_LINKER`; full-protein reconstruction slices | FASTA directly inspected; UniProt citation/provenance recorded but primary REST response not in bundle | **Supported by artifact; primary-source verification not independently repeated here** |
| Mature numbering is 334–344 | `analyze.py`, outputs, provenance | Reported as `353-19` to `363-19` | Derived from signal peptide 1–19 / chain 20–710; primary UniProt cited | **Plausible; direct primary not in bundle** |
| WT linker pLDDT mean ≈95.61 | `alphafold_P02788_plddt.json`; `outputs/summary.md` | Used in local pLDDT proxy and ESM2 proxy | Direct JSON values available | **Supported** |
| WT linker is a helix/structured segment, not a flexible loop | `inputs/linker_residue_range.json`; Rosetta DSSP outputs; `refold_via_relax_results.json` | Later Rosetta extension uses helix retention; root model instead penalizes high loop pLDDT | PDB/UniProt cited; Rosetta outputs directly available | **Supported; root metric initially mis-specified** |
| WT ALP-preferred P1 count | `linker_residue_range.json`; README | Used indirectly in sampler proline boost via hard-coded ALP set | JSON says `wt_p1_matches_count: 11` but positions list only 8 and note says only 8/11 are ALP P1-preferred; README wording also contradictory | **Correction required** |
| Root WT cleavage score 0.407; `EEEEPAARRAR` 0.290 | `outputs/candidates.json`; `outputs/shortlist.json`; `analyze.py` | Computed from shared protease library with pLDDT accessibility proxy | Reproducible by code path; protease specificity file not in bundle; proxy later shown flawed | **Internally reproducible but not a physical cleavage rate** |
| CAI / codon compatibility | `a_oryzae_codon_usage.json`; `analyze.py cai_of_sequence()` | Geometric mean of best-codon `freq_per1000` by amino acid | Codon table directly available; primary Kazusa/Nakao/Machida not independently verified | **Metric mislabeled as CAI; implementation is amino-acid codon-favorability proxy** |
| ESM2 pseudo-pLDDT | `analyze.py esm2_pseudo_plddt_proxy()` | Concordance metric | No ESM2 model run in root; surrogate formula only | **Label overstates implementation; acceptable only if clearly called surrogate** |
| Root candidate generation | `analyze.py build_candidate_pool()` | Creates 60 candidates | Deterministic seed 42; not ProteinMPNN | **Reproducible substitute sampler; superseded by later MPNN rerun** |
| ProteinMPNN constrained STRICT candidates | `proteinmpnn_rerun/candidates_mpnn_constrained.json`; `shortlist_mpnn.json`; `summary.md` | Later candidate identity and §1.10 arm selection | Text FASTA and JSON artifacts available; binary npz not inspected | **Supported at sequence/score-summary level; counts should be deduplicated** |
| `NEEEQQQEEEQ` stability-neutral and helix-preserving | `rosetta_ddg_results_cartesian10.json`; `refold_via_relax_results.json`; Rosetta README | Later wet-lab priority inversion | JSON directly available; code not executed; PyRosetta primary runtime not reproduced | **Supported as committed in-silico result; not wet-lab evidence** |
| Structure-gated cleavage −66% for MPNN arms vs WT | `refold_via_relax_results.json`; Rosetta README | Later conclusion that helix-preserving charge/polar arms win | WT 1.143 vs MPNN 0.388 directly in JSON | **Supported directionally; absolute weights heuristic** |
| Proline arms destabilizing | `rosetta_ddg_results_cartesian10.json`; `refold_via_relax_results.json` | Demotion of `SEEEPAARRAR`, `EEEEPAARRAR`, `EEEEPAAPPAP` | ΔΔG_min +20.11/+21.26/+57.48 in JSON | **Supported as Rosetta local-relax result; needs wet-lab Tm/proteolysis validation** |
| Root reproducibility command | `README.md` | `cd experiments/comp-034-lactoferrin-linker-redesign; python3 analyze.py` | Actual tracked path is `wiki/etc/experiments/...`; root command omits `wiki/etc/` | **Correction required** |
| Later reproducibility dependencies | `proteinmpnn_rerun/summary.md`; `rosetta_concordance/README.md` | Required for final recommendation | Requires ProteinMPNN, NumPy, PyRosetta; not covered by root “stdlib only” claim | **Correction required: final result has multi-tool dependencies** |

## Affected wiki pages

- `wiki/lactoferrin-linker-redesign-computational.md` — **change required** — top update notes correctly record MPNN/Rosetta supersession, but the retained headline and final recommendation still promote the old proline/substitute-sampler plate.
- `wiki/computational-experiments.md` — **change required** — comp-034 entry remains at the original 15/60, 0 STRICT, `EEEEPAARRAR` primary verdict; should summarize the superseded-v1 vs MPNN/Rosetta-v2 state.
- `wiki/validation-experiments.md` — **change required** — §1.10 scientific arm is mostly updated to `NEEEQQQEEEQ` primary, but “4-lane gel” lists 5 lanes and the cost line is inconsistent with the updated cost paragraph.
- `wiki/etc/bio-ai-tools.md` — **change required** — the reusable workflow still encodes the stale “proline substitution / loop flexibility” lesson for structured-mandatory connectors; comp-034’s physics result requires the opposite caution for helical connectors.
- `wiki/etc/autonomous-screening-methodology.md` — **already consistent** — correctly records the pLDDT-as-accessibility failure mode and real-SASA replacement lesson.
- `wiki/lactoferrin.md` — **change required** — lobe-boundary section appears to retain mature C-lobe endpoint `703`, inconsistent with UniProt precursor length and comp-034’s provenance note.
- `wiki/lactoferrin-protease-stability-computational.md` — **already consistent / no direct change found** — archived comp-005 stub; comp-034 does not invalidate comp-005’s mature-Lf MODERATE framing, but the pLDDT accessibility caveat should be understood when interpreting old scores.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — **already consistent** — treats lactoferrin as koji-routed and flags pLDDT proxy limitations; no comp-034-driven correction found.
- `wiki/chaperone-orthogonal-stacking.md` — **possible change required outside comp-034 scope** — direct read showed some older lactoferrin disulfide-count language remains internally mixed in the page; not central to comp-034 linker result but should be separately linted.
- `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/README.md` and `outputs/summary.md` — **change required** — root artifact summaries are stale relative to committed rerun/physics extensions or must be explicitly labeled “v1 substitute-sampler only; superseded.”

## New connections or implications

- **The dominant comp-034 lesson is not “proline blocks proteases”; it is “preserve protective secondary structure while removing preferred cleavage residues.”** This matters for any future linker-redesign page and invalidates a generic proline-first design heuristic for helical connectors.
- **The pLDDT accessibility failure affects more than comp-034.** The shared protease-stability library now says comp-001/005/006/012/037 used the same pLDDT-as-burial proxy. For compact proteins this may be conservative enough, but any confident exposed helix/strand region should be rechecked with real SASA if it becomes load-bearing.
- **ProteinMPNN’s constrained and unconstrained behavior separate two different design objectives.** Constrained MPNN strips the linker to polar/charged residues and finds low-cleavage helix-preserving candidates; unconstrained MPNN tends to preserve Ala/Ile/Arg-like helical motifs and often does not reduce cleavage. This is useful mechanistic context for future sequence-design constraints.
- **Wet-lab §1.10 should include stability/Tm, not just proteolysis.** The Rosetta inversion shows a variant can reduce sequence-level cleavage while destabilizing the inter-lobe helix. The validation assay should measure proteolysis plus fold/iron-binding/Tm.
- **Deduplication matters in design screens.** The MPNN constrained pool’s 5 STRICT records are 3 unique sequences. Future comp summaries should report both record count and unique sequence count.

## Required actions

1. **Update root comp-034 README and root `outputs/summary.md` or mark them superseded.**  
   Owner surface: `wiki/etc/experiments/comp-034-lactoferrin-linker-redesign/README.md`, `outputs/summary.md`, `outputs/shortlist.json` if regenerated.  
   Verification criterion: a reader can distinguish v1 substitute-sampler results from the later MPNN/Rosetta-supported recommendation; no root summary states `EEEEPAARRAR` as current primary without a supersession caveat.

2. **Reconcile `wiki/lactoferrin-linker-redesign-computational.md`.**  
   Owner surface: interpretive page.  
   Verification criterion: headline verdict, recommendation paragraph, and evidence-level summary all name `NEEEQQQEEEQ` primary / `NEEEQEEQDQQ` backup and demote proline arms, or explicitly preserve old text only as archived genealogy.

3. **Update `wiki/computational-experiments.md` comp-034 entry.**  
   Owner surface: computational experiment index.  
   Verification criterion: entry reports the current state: v1 15/60 GREEN and 0 STRICT was superseded by genuine MPNN constrained candidates with unique STRICT sequences and Rosetta/structure-gated helix-preservation result.

4. **Fix §1.10 validation text inconsistencies.**  
   Owner surface: `wiki/validation-experiments.md §1.10`.  
   Verification criterion: lane count matches listed lanes; cost header matches the updated cost range or explicitly separates base vs add-on cost.

5. **Correct the reusable workflow in `wiki/etc/bio-ai-tools.md`.**  
   Owner surface: “Protease-vulnerability-to-redesign workflow.”  
   Verification criterion: structured-mandatory connectors are not generically assigned to proline substitution; workflow distinguishes helical/structured connectors from flexible loops and includes Rosetta/SASA/secondary-structure gates before wet-lab promotion.

6. **Fix ALP-preferred residue count inconsistency.**  
   Owner surface: `inputs/linker_residue_range.json`, README prose if retained.  
   Verification criterion: count and position list agree (`S,V,A,R` positions = 8/11 P1-preferred under the coded ALP set; Glu residues are not ALP P1-preferred), or the text explicitly describes neighboring P1′ effects separately.

7. **Clarify metric names in code/output documentation.**  
   Owner surface: README, output summaries, possibly `analyze.py` comments.  
   Verification criterion: “CAI” is described as best-codon frequency/composition proxy unless actual DNA-level CAI is implemented; “ESM2 pseudo-pLDDT” is explicitly surrogate-only.

8. **Make reproduction contract versioned.**  
   Owner surface: root README plus `proteinmpnn_rerun/summary.md` and `rosetta_concordance/README.md`.  
   Verification criterion: commands and dependencies are listed for (a) root stdlib v1, (b) ProteinMPNN rerun, (c) Rosetta/PyRosetta extension; repo-relative paths are correct from repo root.

9. **Correct `wiki/lactoferrin.md` mature C-lobe endpoint / mature-length text.**  
   Owner surface: lactoferrin structural section.  
   Verification criterion: mature numbering is internally consistent with UniProt P02788 signal peptide 1–19 and chain 20–710.

10. **If any wet-lab ordering depends on final candidate identity, require a formal v2 rerun/summary packet.**  
   Owner surface: comp-034 experiment folder and §1.10.  
   Verification criterion: final wet-lab plate is tied to a single committed summary that deduplicates candidates, uses current physics/structure-gated metrics, and states remaining in-silico-only limits.

## Review limits

- I did **not** execute arbitrary code. Reproducibility is assessed by static inspection of scripts and committed outputs.
- Repository `grep_repo` failed because `rg` was unavailable in the tool environment, so affected-surface search was limited to provided explicit pages plus manual reads of selected likely pages.
- Binary `.npz` ProteinMPNN probability/score files and PDB coordinate files were not inspected; I relied on committed text/JSON summaries and FASTA where available.
- The comp-005 protease specificity JSON was referenced by code but not included in the provided text bundle; I did not independently verify protease-specificity tables or primary MEROPS sources.
- UniProt, AlphaFold DB, PDB 1B0L, Kazusa/Nakao/Machida, and literature primary sources were not fetched live; provenance strings and committed input files were inspected, not independently primary-source verified.
- `wiki/lactoferrin.md`, `wiki/chaperone-orthogonal-stacking.md`, and `wiki/validation-experiments.md` are large; only bounded portions were inspected before the tool-result budget was exhausted.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
