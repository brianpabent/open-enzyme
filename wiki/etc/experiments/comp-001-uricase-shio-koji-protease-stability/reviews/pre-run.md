PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: dce2c4d10993623429e03b9a0f3f6e3f50e4aa97dd16c1d1dc0002d974eff5bd

# Adversarial pre-run review — comp-001

## Reviewed snapshot

Reviewer: `/root/comp001_pre_review_v6`, fresh context-isolated Gate 1 reviewer. I inspected all 6 manifest-bound design files and both prior-output baseline files. I independently canonicalized the manifest payload and reproduced SHA-256 `dce2c4d10993623429e03b9a0f3f6e3f50e4aa97dd16c1d1dc0002d974eff5bd`. Every recorded file exists and matches its manifest byte count and SHA-256; no design file is omitted.

Relative to the last approved/post-run design snapshot, `analyze.py`, `Q00511.fasta`, `alphafold_Q00511_plddt.json`, `legacy_preference_filters.json`, and `inputs/provenance.md` are byte-identical. Only `README.md` differs. Its current §1.10 links use the corrected double-hyphen Markdown anchor for the `Uricase + Lactoferrin` heading. No code, input, model, parameter, rule, sensitivity plan, output schema, or verdict mapping changed.

## Bottom-line verdict

This exact snapshot may run. It implements a narrow, deterministic inventory of all Q00511 adjacent peptide bonds that match three explicitly unverified legacy Boolean filters and attaches the prespecified local AlphaFold pLDDT-window context. It cannot emit a protease-risk class or use pLDDT as accessibility, cleavage likelihood, folding quality, secretion capacity, survival, retained activity, fermentation performance, or biological risk.

Every possible descriptive result is constrained to:

`PROXY ONLY — EMPIRICAL PROTEASE RISK UNRESOLVED`

The empirical §1.10 retained-activity assay remains the feasibility gate.

## Question and model fit

The registered computation and implementation agree:

1. Validate the fixed UniProt Q00511 sequence.
2. Validate an exact position–residue–pLDDT mapping.
3. Traverse every one of the 301 adjacent peptide bonds.
4. Apply three fixed Boolean inclusion filters with explicit empty-list semantics.
5. Report every matching pair and its prespecified terminal-safe pLDDT window.
6. Preserve empirical protease susceptibility as unresolved.

There is no hidden substitution of pLDDT for solvent accessibility, cleavage, folding quality, secretion capacity, survival, or biological risk. There is also no substitution of the legacy arrays for exhaustive protease specificity. Protease identity, concentration, kinetics, compartmental access, exposure time, salt/pH effects, quaternary structure, retained activity, and fermentation survival remain outside the computation. Those constraints would be essential to a biological protease-risk model, but this COMP does not claim to provide one.

## Constraint and implementation audit

The script is self-contained, deterministic, and limited to the Python standard library and three committed machine-readable inputs.

- `load_sequence()` accepts only canonical amino acids and requires the exact reviewed Q00511 sequence SHA-256.
- The official UniProt Q00511 record independently reproduced the committed header and sequence SHA-256 `cb5dbe78672345fa69aa22b22567f43efc9977817af32cb2cf2c98ec1852f877`.
- `load_plddt()` requires positions exactly `1..302`, finite values within `[0,100]`, and the exact reviewed position–residue–pLDDT mapping hash.
- The official AlphaFold `AF-Q00511-F1-model_v6` PDB independently reproduced SHA-256 `39a21b80fa2bbceaa8fe0b9d32a3ef7a6bc77b8635b17af54ffd6a224694585d`. Independent chain-A Cα extraction found 302 contiguous residues from 1 through 302 and reproduced mapping SHA-256 `90abb3e1a8ea932f71231e742c22f00a34ebc7c864bf7680c022b19555662f80`.
- Filter loading requires schema version 1, the explicit `legacy_encoding_not_claim_level_verified` status, unique nonempty rule IDs, canonical nonduplicated residue lists, and at least one constrained side.
- A nonempty filter is an inclusion list; an empty filter is unrestricted. These are program semantics, not biological-specificity claims.
- `range(len(sequence) - 1)` visits P1 positions 1 through 301 and therefore every Q00511 peptide bond, including K301/L302.
- Windows use inclusive bounds `max(1, P1−3)` through `min(length, P1+1+3)`. Static inspection confirms the first window is residues 1–5, an internal full window has eight residues, and the terminal K301/L302 window is residues 298–302.
- Each match retains exact positions, residue identities, inclusive bounds, residue count, and the unrounded calculated mean. The complete match inventory remains in JSON; the summary rounds only presentation values.
- Execution reads only the three committed inputs and overwrites only `outputs/cleavage_sites.json` and `outputs/summary.md`. It uses no random state, network service, environment-derived parameter, clock value, or third-party dependency.
- The two prior-output baselines are valid schema-v2 proxy-only artifacts matching their recorded hashes. They pose no schema or overwrite incompatibility.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Fixed Q00511 sequence, 302 residues | `inputs/Q00511.fasta`; `inputs/provenance.md`; sequence-hash constant | Coordinate system and enumeration of 301 peptide bonds | Official UniProt record, release/access date, and exact sequence hash; independently reproduced | Pass |
| AlphaFold model `AF-Q00511-F1-model_v6` | `inputs/provenance.md`; pLDDT JSON | Descriptive confidence context only | Official AlphaFold PDB URL/version and exact PDB hash; independently reproduced | Pass |
| Exact position–residue–pLDDT alignment | Mapping-hash constant; pLDDT loader | Prevent shifted or mismatched confidence vectors | Documented chain-A Cα transformation; 302-position hash independently reproduced | Pass |
| Three legacy residue arrays | `inputs/legacy_preference_filters.json` | Fixed Boolean match filters | Claim-level provenance explicitly absent; never promoted to exhaustive specificity | Pass within proxy-only scope |
| Empty array means unrestricted | Filter input; README; `matches_filter()` | Deterministic filter semantics | Explicit code convention, not a biological claim | Pass |
| Three flanking residues per side | `FLANK_RESIDUES`; README | Prespecified descriptive window | Design choice, not a biological threshold | Pass |
| Inclusive terminal-safe bounds | `motif_window_bounds()`; `local_plddt()`; self-checks | Preserve P1/P1′ and residue 302 | Directly inspectable implementation | Pass |
| Unrounded local means and complete matches | JSON output construction | Audit each reported match | Deterministically derived from fixed values | Pass |
| Fixed proxy-only verdict | README; JSON verdict and decision boundary; summary template | Prevent descriptive results from becoming risk claims | Precommitted for every possible result | Pass |
| §1.10 retained-activity assay remains the gate | README; JSON decision boundary; summary template | Preserve empirical decision authority | Correctly outside computational scope | Pass |

## Falsification, sensitivity, and output contract

The result/verdict map is complete. Zero, sparse, or numerous filter matches and any pLDDT distribution all retain the same proxy-only verdict. Input-integrity or schema violations stop execution instead of yielding a biological interpretation.

No inferential sensitivity analysis is warranted for exact enumeration of fixed inputs. The design correctly requires any alternative filter encoding or pLDDT window width to undergo a new pre-run review.

The schema-v2 JSON exposes the scope, caveat, input hashes, window definition, sequence statistics, exact filter arrays, explicit legacy-provenance status, empty-filter semantics, match counts, complete matching-pair inventory, positions, residues, bounds, residue counts, unrounded means, supported and unsupported interpretations, empirical gate, sensitivity rationale, and fixed verdict. The Markdown summary repeats the proxy boundary and directs readers to the complete machine-readable inventory.

Neither the schema nor the summary can legitimately support accessibility, cleavage, folding quality, secretion capacity, survival, retained activity, fermentation performance, or a LOW/MODERATE/HIGH biological-risk classification.

## Downstream authoring contract

The planned interpretive evidence home is `wiki/uricase-protease-stability-computational.md`. Named dependents are `wiki/computational-experiments.md`, empirical gate `wiki/validation-experiments.md` §1.10, and direct UOX dependent `wiki/uricase-shio-koji-thermal-stability-computational.md`.

The claim boundary is narrow:

- The run may establish only which fixed Q00511 adjacent pairs match the encoded legacy arrays and their prespecified pLDDT context.
- It may not establish biological recognition, exhaustive specificity, solvent access, cleavage, folding quality, secretion capacity, retained activity, survival, fermentation performance, or biological risk.
- Direct UOX pages that used COMP-001 for accessibility, burial, LOW risk, survival, or “confirmation experiment” claims must be corrected.
- Shared-proxy conclusions for other payloads remain separately reviewable and cannot use COMP-001 as a validated benchmark.
- Empirical §1.10 retained-activity testing remains the feasibility gate.
- No cross-track ranking, personalized treatment instruction, editorial history, duplicated exposition, or deletion of neighboring untested hypotheses is authorized.

## Required actions before execution

None.

## Review limits

I did not execute, import, compile, or otherwise invoke `analyze.py`; I did not generate or alter outputs; and I did not test two-run byte identity. Code, inputs, prior outputs, file effects, and planned interpretation were reviewed statically. Official UniProt and AlphaFold records were retrieved only to verify the bound provenance and hashes. The legacy filter arrays remain intentionally unverified at claim level and are approved only as fixed historical code filters, never as exhaustive biological specificity rules.
