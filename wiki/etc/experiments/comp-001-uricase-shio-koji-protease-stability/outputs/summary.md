# COMP-001 — Q00511 Legacy Preference-Filter and pLDDT-Context Audit

**Verdict:** **PROXY ONLY — EMPIRICAL PROTEASE RISK UNRESOLVED**

**Method boundary:** Adjacent-pair matches to unverified legacy preference filters plus AlphaFold pLDDT context only. The filters are not established exhaustive protease specificity rules, and pLDDT is model confidence rather than solvent accessibility. This output does not estimate cleavage, protease-survival risk, retained activity, or fermentation performance.

## Question

Which adjacent residue pairs in *A. flavus* UOX (Q00511) match three fixed legacy preference filters, and what AlphaFold confidence surrounds each match?

## Sequence-confidence snapshot

| Metric | Value |
|---|---:|
| Sequence length | 302 aa |
| Mean pLDDT | 97.14 |
| Minimum pLDDT | 80.50 |
| Residues with pLDDT ≥90 | 293 |
| Residues with pLDDT 70–<90 | 9 |
| Residues with pLDDT 50–<70 | 0 |
| Residues with pLDDT <50 | 0 |

pLDDT reports local prediction confidence. It does not establish burial or protease accessibility.

## Encoded preference-filter inventory

| Legacy filter label | Adjacent-pair matches | Lowest local mean pLDDT |
|---|---:|---:|
| ALP legacy P1 filter | 215 | 84.54 |
| NPr legacy P1' filter | 97 | 84.54 |
| Acid-protease legacy P1/P1' filter | 44 | 93.52 |

The complete pair inventory, exact filter arrays, window bounds, included-residue counts, and unrounded means are in `cleavage_sites.json`. The legacy arrays lack claim-level provenance and are not treated as exhaustive biological specificity rules.

## Decision

COMP-001 supplies an auditable sequence-filter inventory and pLDDT context only. Every possible output leaves protease susceptibility unresolved. The §1.10 shio-koji retained-activity assay remains the feasibility gate.

No inferential sensitivity analysis is warranted for this exact enumeration. A different filter encoding or window width would be a new design requiring fresh review.

## Reproduction

Run `python3 analyze.py` from the COMP directory. The script uses Python standard-library code and fixed committed inputs. Two runs must produce byte-identical outputs.

---

*Generated from the fixed COMP-001 inputs. Source accessions, versions, transformations, and limitations are recorded in `inputs/provenance.md`.*
