#!/usr/bin/env python3
"""
code_replicates.py — produce a scaffold + ground-truth diff view for coding
each replicate's response against the existing atomic-claim taxonomy.

Reads:
  - outputs/claims/<prompt-id>.json     (original r1 taxonomy + verdicts)
  - responses/<prompt-id>/<vendor>-r<N>.md  (response body)

Writes:
  - outputs/claims/<prompt-id>-r<N>.json   (one per replicate; verdicts blank, ready to fill)

The script does NOT attempt to auto-code. It produces:
  - a per-(prompt, replicate) JSON file with the same claim structure
  - verdicts pre-populated with an "auto_hint" field showing the r1 verdict + value_quoted
    + a "needs_verification" flag so the human coder remembers to actually look at the new
    response before stamping a verdict

Usage:
  python3 code_replicates.py --replicate 2 --init
  # then edit outputs/claims/*-r2.json by hand to set actual verdicts
"""

import argparse
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
RESPONSES_DIR = HERE / "responses"
CLAIMS_DIR = HERE / "outputs" / "claims"

VENDORS = ["deepseek", "gemini", "openai", "anthropic"]


def load_response_body(prompt_id, vendor, replicate):
    p = RESPONSES_DIR / prompt_id / f"{vendor}-r{replicate}.md"
    if not p.exists():
        return None
    txt = p.read_text()
    if txt.startswith("---"):
        m = re.search(r"^---\s*$", txt[3:], re.MULTILINE)
        if m:
            return txt[3:][m.end():].lstrip("\n")
    return txt


def init(replicate):
    for cf in sorted(CLAIMS_DIR.glob("*.json")):
        if cf.stem.endswith(f"-r{replicate}") or cf.stem.endswith(f"-r2") and replicate != 2:
            continue
        prompt_id = cf.stem
        if "-r" in prompt_id and prompt_id.split("-r")[-1].isdigit():
            continue  # already a replicate file
        out = CLAIMS_DIR / f"{prompt_id}-r{replicate}.json"
        if out.exists():
            print(f"  [skip] {out.name} exists")
            continue
        orig = json.loads(cf.read_text())
        new = {
            "prompt_id": prompt_id,
            "replicate": replicate,
            "task_type": orig["task_type"],
            "coding_notes": f"Replicate {replicate}. Verdicts coded against the same atomic-claim taxonomy as the original. Verdict vocabulary: affirm | disagree (with alternative) | ignore | refusal.",
            "ground_truth_notes": orig.get("ground_truth_notes", ""),
            "claims": [],
        }
        for c in orig["claims"]:
            new_c = {
                "id": c["id"],
                "claim_text": c["claim_text"],
                "verdicts": {v: {"verdict": "PENDING"} for v in VENDORS},
            }
            new["claims"].append(new_c)
        out.write_text(json.dumps(new, indent=2))
        print(f"  [init] {out.name}")


def show(prompt_id, replicate):
    """Print a side-by-side view of r1 verdicts + replicate response excerpt
    for human coding."""
    orig_path = CLAIMS_DIR / f"{prompt_id}.json"
    orig = json.loads(orig_path.read_text())

    print(f"\n============================================================")
    print(f"PROMPT: {prompt_id}  task={orig['task_type']}")
    print(f"============================================================")
    for c in orig["claims"]:
        print(f"\n--- {c['id']}: {c['claim_text']}")
        for v in VENDORS:
            r1 = c["verdicts"].get(v, {})
            print(f"  r1 {v:10s}: {r1.get('verdict', '?'):10s}  alt={r1.get('alternative', '')!r}  quoted={r1.get('value_quoted', '')[:100]!r}")

    for v in VENDORS:
        body = load_response_body(prompt_id, v, replicate)
        print(f"\n>>>>>>>>>>> {prompt_id} {v} r{replicate} <<<<<<<<<<<")
        if body is None:
            print("  (no response file)")
        else:
            print(body[:6000])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--replicate", type=int, required=True)
    p.add_argument("--init", action="store_true")
    p.add_argument("--show", default="", help="prompt id to dump for human coding")
    args = p.parse_args()
    if args.init:
        init(args.replicate)
    if args.show:
        show(args.show, args.replicate)


if __name__ == "__main__":
    main()
