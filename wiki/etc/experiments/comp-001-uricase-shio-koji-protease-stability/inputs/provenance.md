# Input Provenance — COMP-001

## Fixed inputs

| File | Source and version | Verification |
|---|---|---|
| `Q00511.fasta` | UniProt REST record Q00511; release 2025_03; fetched 2026-05-05; `https://rest.uniprot.org/uniprotkb/Q00511.fasta` | FASTA header identifies reviewed *A. flavus* uricase, PE=1, sequence version 3. The 302-residue sequence SHA-256 is `cb5dbe78672345fa69aa22b22567f43efc9977817af32cb2cf2c98ec1852f877`. |
| `alphafold_Q00511_plddt.json` | AlphaFold DB model `AF-Q00511-F1-model_v6`; original input fetched 2026-05-05 from `https://alphafold.ebi.ac.uk/files/AF-Q00511-F1-model_v6.pdb` | Rechecked against the same official PDB on 2026-07-23. The downloaded PDB SHA-256 was `39a21b80fa2bbceaa8fe0b9d32a3ef7a6bc77b8635b17af54ffd6a224694585d`. |
| `legacy_preference_filters.json` | Preserved from the original COMP-001 `protease_specificities.json` encoding | **Legacy encoding; claim-level provenance absent.** The earlier file generally attributed the arrays to MEROPS release 12.4 and several author-year citations but did not record a residue-by-residue derivation or evidence that the Boolean arrays were exhaustive specificity rules. The revised COMP treats them only as fixed code filters. |

## AlphaFold PDB-to-JSON transformation

The pLDDT vector was verified by parsing chain A `ATOM` records from the official PDB and selecting one Cα record per residue in PDB order. Three-letter residue names were converted to canonical one-letter codes; residue numbers had to be contiguous from 1 through 302. The Cα B-factor field supplied the per-residue pLDDT value, following the [AlphaFold DB confidence-score specification](https://alphafold.ebi.ac.uk/faq).

The extracted residue sequence matched `Q00511.fasta` position by position, and all 302 extracted pLDDT values matched the committed JSON. The canonical position–residue–pLDDT mapping—one line per residue as `<position>\t<one-letter residue>\t<pLDDT to two decimals>`—has SHA-256 `90abb3e1a8ea932f71231e742c22f00a34ebc7c864bf7680c022b19555662f80`. `analyze.py` validates that mapping before writing outputs, so a shifted same-length confidence vector fails.

## Interpretation boundary

AlphaFold pLDDT is a per-residue estimate of local prediction confidence. It is not solvent accessibility, burial, protease recognition, cleavage probability, or survival. AlphaFold DB describes values above 90 as very high confidence, 70–90 as confident, 50–70 as low confidence, and below 50 as very low confidence; the revised COMP reports those descriptive bins without converting them into biological-risk classes.

The legacy filters are similarly bounded. A nonempty array is used as a Boolean inclusion list and an empty array leaves that side of the adjacent pair unrestricted. Those are reproducible program semantics, not evidence that the filter captures the enzyme’s complete substrate specificity.
