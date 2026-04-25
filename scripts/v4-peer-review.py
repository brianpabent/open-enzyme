#!/usr/bin/env python3
"""
v4-peer-review.py — one-off DeepSeek V4-Pro peer-review pass on the Open Enzyme wiki.

Demonstrates the multi-agent peer-review pattern: V4 reads the same corpus Claude
just swept (commit 4a40f74), produces its own Pass 2 synthesis, and adds a
differential-analysis section comparing what V4 surfaces vs. what Claude found.

Reads OPENROUTER_API_KEY from .env. Saves output to logs/v4-peer-review-<date>.md.
Reports token usage and cost.

Run from the repo root:
    python3 scripts/v4-peer-review.py
"""

import os
import sys
import json
import glob
import datetime
import subprocess
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

# --- Read API key from .env (no logging the value) -----------------------------
API_KEY = None
with open(".env") as f:
    for line in f:
        if line.startswith("OPENROUTER_API_KEY="):
            API_KEY = line.split("=", 1)[1].strip()
            break
if not API_KEY:
    sys.exit("OPENROUTER_API_KEY not found in .env")

# --- Build the corpus ----------------------------------------------------------
# All wiki/*.md including synthesis.md (V4 needs to see Claude's existing
# Pass 2 to do a differential). Concatenate with === filename === separators.
#
# OpenRouter caps deepseek/deepseek-v4-pro at 512K tokens (platform policy,
# even though the model itself supports 1M). Excluding three low-synthesis-
# value files to fit:
#   - GRAPH.md: Mermaid diagram, hard for non-vision models to use
#   - references.md: bibliography only
#   - ai-bio-tools-playbook.md: tooling reference, not biology mechanism
EXCLUDE = {
    "wiki/GRAPH.md",
    "wiki/references.md",
    "wiki/ai-bio-tools-playbook.md",
}
wiki_files = [p for p in sorted(
    glob.glob("wiki/*.md") + glob.glob("wiki/hypotheses/*.md")
) if p not in EXCLUDE]
corpus_parts = []
for path in wiki_files:
    with open(path) as f:
        corpus_parts.append(f"\n\n=== {path} ===\n\n{f.read()}")
corpus = "".join(corpus_parts)
corpus_chars = len(corpus)
corpus_token_estimate = corpus_chars // 4  # rough English-prose ratio

# --- Peer-review prompt --------------------------------------------------------
prompt = f"""You are running a peer-review pass on the Open Enzyme research wiki.

Yesterday (commit 4a40f74), Claude Opus 4.7 ran a Pass 2 synthesis on this corpus. The result is the most-recent block at the top of `wiki/synthesis.md` ("New this sweep — 2026-04-24 (local session, 25-file v1.2 batch)"). It surfaced 7 new connections, 2 contradictions, 6 proposed experiments, 6 open questions, 3 priority actions.

Your task: do an independent Pass 2 synthesis on the same corpus, then compare.

1. Read the entire corpus below (files concatenated under `=== filename ===` markers).
2. Read the existing 2026-04-24 synthesis block at the top of `wiki/synthesis.md` carefully — that is what Claude found.
3. Generate your own Pass 2 synthesis. New connections you would surface, contradictions you spot, experiments you would propose, open questions you would flag.
4. Then add a final **Differential Analysis** section: which of Claude's 7 connections do you confirm, partially-confirm, push back on, or reject? What did Claude miss that you found? What did Claude find that you did not? Be specific — cite document names and PMIDs where applicable.

Output format: the same Pass 2 structure as Claude used.

```
## V4 peer-review pass — 2026-04-25

**Reviewer**: DeepSeek V4-Pro (via OpenRouter)
**Substrate**: Open Enzyme wiki at commit 4a40f74

### New Connections

(numbered, each with Documents Connected / Why It Matters / Suggested Action / Supported-or-Speculative tag)

### Contradictions Found

### Proposed Experiments (ranked by insight per cost)

### Open Questions

### Differential Analysis vs. Claude 4a40f74

Confirmed: ...
Partially confirmed: ...
Push-back: ...
Rejected: ...
Missed by Claude (newly surfaced by V4): ...
Missed by V4 (Claude caught): ...
```

Discipline:
- Tag every substantive claim with evidence level: **Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation**.
- Mark each Connection as **Supported** (multiple sources align) or **Speculative** (reasonable but unvalidated).
- Cite specific document names and PMIDs where applicable.
- Do NOT propose file edits. Do NOT generate commit messages. Synthesis text only — this is a peer-review pass, not a sweep.
- Honest framing: PhD audience. No marketing language. Distinguish proven from speculative.

[CORPUS BELOW]

{corpus}
"""

prompt_chars = len(prompt)
prompt_token_estimate = prompt_chars // 4
print(f"Corpus: {len(wiki_files)} files, {corpus_chars:,} chars, ~{corpus_token_estimate:,} tokens (estimate)")
print(f"Total prompt: {prompt_chars:,} chars, ~{prompt_token_estimate:,} tokens (estimate)")

# Sanity check — V4-Pro context is 1,048,576 tokens
if prompt_token_estimate > 900_000:
    sys.exit(f"Prompt estimate {prompt_token_estimate:,} tokens — too close to 1M ceiling. Trim corpus.")

# --- Call OpenRouter via curl (avoids Python's macOS SSL cert quirk) -----------
print("\nCalling deepseek/deepseek-v4-pro via OpenRouter ...")

request_body = {
    "model": "deepseek/deepseek-v4-pro",
    "messages": [{"role": "user", "content": prompt}],
    # 6K is plenty for synthesis output (Claude's pass-2 was ~3K). Smaller
    # output budget = more headroom for input under OpenRouter's 512K cap.
    "max_tokens": 6_000,
    "temperature": 0.7,
}

# Write the request body to a temp file — too large for command-line argument
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
    json.dump(request_body, tf)
    body_path = tf.name

try:
    result = subprocess.run(
        [
            "curl", "-sS", "--fail-with-body",
            "https://openrouter.ai/api/v1/chat/completions",
            "-H", f"Authorization: Bearer {API_KEY}",
            "-H", "Content-Type: application/json",
            "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
            "-H", "X-Title: Open Enzyme V4 peer-review",
            "-d", f"@{body_path}",
            "--max-time", "600",
        ],
        capture_output=True,
        text=True,
        timeout=620,
    )
finally:
    os.unlink(body_path)

if result.returncode != 0:
    print(f"curl failed (exit {result.returncode})")
    print(f"stderr: {result.stderr.strip()}")
    print(f"stdout (first 2000 chars): {result.stdout[:2000]}")
    sys.exit(1)

try:
    body = json.loads(result.stdout)
except json.JSONDecodeError:
    print("Non-JSON response:")
    print(result.stdout[:2000])
    sys.exit(1)

if "choices" not in body:
    print("Unexpected response:")
    print(json.dumps(body, indent=2)[:2000])
    sys.exit(1)

content = body["choices"][0]["message"]["content"]
usage = body.get("usage", {})
prompt_tokens = usage.get("prompt_tokens", 0)
completion_tokens = usage.get("completion_tokens", 0)

# OpenRouter pricing (2026-04-25): input $0.435/Mtok, output $0.87/Mtok
input_cost = prompt_tokens * 0.435 / 1_000_000
output_cost = completion_tokens * 0.87 / 1_000_000
total_cost = input_cost + output_cost

print(f"\nResponse received.")
print(f"  Input tokens:  {prompt_tokens:,} (estimated {prompt_token_estimate:,})")
print(f"  Output tokens: {completion_tokens:,}")
print(f"  Cost:          ${total_cost:.4f}  (in: ${input_cost:.4f}, out: ${output_cost:.4f})")

# --- Save output ---------------------------------------------------------------
date_str = datetime.date.today().isoformat()
output_path = f"logs/v4-peer-review-{date_str}.md"
os.makedirs("logs", exist_ok=True)

header = f"""---
title: "V4-Pro peer-review pass — {date_str}"
date: {date_str}
reviewer: DeepSeek V4-Pro (via OpenRouter)
substrate_commit: 4a40f74
substrate_label: "Claude Opus 4.7 local-session sweep, 2026-04-24"
input_tokens: {prompt_tokens}
output_tokens: {completion_tokens}
cost_usd: {total_cost:.4f}
---

# V4-Pro peer-review pass — {date_str}

This is the first concrete instance of the multi-agent peer-review pattern named in
[`open-enzyme-vision.md`](../wiki/open-enzyme-vision.md) §3. DeepSeek V4-Pro was given
the same wiki corpus Claude swept yesterday (commit `4a40f74`) and asked to produce an
independent Pass 2 synthesis plus a differential analysis. Output below is verbatim
model output, unedited.

The discipline that makes this trustworthy is the same on both sides: evidence-level
tags, inline provenance, distinguishable Supported vs. Speculative claims. The wiki is
the shared substrate; V4 and Claude are the two reviewers.

---

"""

with open(output_path, "w") as f:
    f.write(header + content + "\n")

print(f"\nSaved: {output_path}")
print(f"\nNext: read {output_path} and compare against the 2026-04-24 block at the top of wiki/synthesis.md.")
