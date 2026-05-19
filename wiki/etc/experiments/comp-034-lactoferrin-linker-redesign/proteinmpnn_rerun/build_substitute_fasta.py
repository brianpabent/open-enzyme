"""
Build a FASTA file of full-length lactoferrin reconstructions for each unique
linker sequence in the substitute sampler's candidate pool, so we can use
ProteinMPNN's --score_only mode to compute its per-sequence log-likelihood.

This lets us answer: when MPNN is shown the substitute's candidates, what
score does it assign relative to its own preferred samples?

Output: substitute_candidates_full.fasta
"""
from __future__ import annotations
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
EXP_DIR = SCRIPT_DIR.parent

LINKER_START = 353
LINKER_END = 363

# WT from canonical inputs
fasta_path = EXP_DIR / "inputs/P02788.fasta"
seq = ""
with open(fasta_path) as f:
    for line in f:
        if not line.startswith(">"):
            seq += line.strip()
assert len(seq) == 710

# Load substitute results
sub_path = EXP_DIR / "outputs/candidates.json"
sub = json.loads(sub_path.read_text())
candidates = sub["candidates"]

# Also include MPNN STRICT / top GREEN for cross-comparison
mpnn_short = json.loads((SCRIPT_DIR / "shortlist_mpnn.json").read_text())
extras = []
for c in mpnn_short["constrained_pool"]["strict"]:
    extras.append(("MPNN_constrained_STRICT", c["linker_sequence"]))
for c in mpnn_short["constrained_pool"]["green"][:10]:
    extras.append(("MPNN_constrained_GREEN", c["linker_sequence"]))
for c in mpnn_short["unconstrained_pool"]["green"][:10]:
    extras.append(("MPNN_unconstrained_GREEN", c["linker_sequence"]))

# Build full-length sequences for unique linkers
unique = {}
for c in candidates:
    linker = c["linker_sequence"]
    if linker not in unique:
        unique[linker] = ("substitute", c["candidate_id"], c.get("tier"), c.get("n_pass"))

# Add WT explicitly
unique.setdefault("SEEEVAARRAR", ("WT", 0, "WT", None))

# Add extras
for label, linker in extras:
    if linker not in unique:
        unique[linker] = (label, None, None, None)

# Write fasta
out_path = SCRIPT_DIR / "substitute_candidates_full.fasta"
with open(out_path, "w") as f:
    for linker, (source, cid, tier, npass) in unique.items():
        reconstructed = seq[: LINKER_START - 1] + linker + seq[LINKER_END:]
        assert len(reconstructed) == 710
        header = f">{source}|linker={linker}|cid={cid}|tier={tier}|n_pass={npass}"
        f.write(header + "\n")
        # Wrap fasta at 60 chars
        for i in range(0, len(reconstructed), 60):
            f.write(reconstructed[i:i+60] + "\n")

print(f"wrote {out_path.name}: {len(unique)} unique full-length sequences")
print(f"  substitute pool: {sum(1 for v in unique.values() if v[0]=='substitute')}")
print(f"  WT: {sum(1 for v in unique.values() if v[0]=='WT')}")
print(f"  MPNN strict: {sum(1 for v in unique.values() if v[0]=='MPNN_constrained_STRICT')}")
print(f"  MPNN constrained green: {sum(1 for v in unique.values() if v[0]=='MPNN_constrained_GREEN')}")
print(f"  MPNN unconstrained green: {sum(1 for v in unique.values() if v[0]=='MPNN_unconstrained_GREEN')}")
