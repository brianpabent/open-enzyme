#!/usr/bin/env python3
"""
fresh-synthesis.py — manual full-corpus synthesis with the model of your choice.

Local CLI tool (NOT the daemon path — see .github/workflows/wiki-sweep.yml
for the CI sweep). The daemon is a 3-pass pipeline (Pass 1 Propagate →
Pass 2 Synthesize → Pass 3 Review). This script is the manual sibling:
point it at any OpenRouter-served model and ask "what does THIS model find
across our corpus?"

Two main use cases:

1. **Model bench.** When a new long-context model ships (next Claude Opus,
   next Gemini, next GPT, next DeepSeek), run it across the corpus and
   compare its synthesis against what the daemon's Pass 2 has been
   surfacing. The architecture is intentionally model-agnostic — only the
   OpenRouter slug changes.

2. **Second-opinion synthesis.** When you want fresh eyes on the corpus
   between daemon sweeps — a different vendor, a different prompt, a
   different time horizon — run this manually. It reads the full wiki
   INCLUDING synthesis/queue/, so it sees what the daemon has already
   surfaced and can produce a differential.

Reads OPENROUTER_API_KEY from env first, falls back to .env. Saves output
to logs/fresh-synth-<model-slug>-<date>.md. Reports token usage and cost.

Run from the repo root:
    python3 scripts/fresh-synthesis.py
    python3 scripts/fresh-synthesis.py --model anthropic/claude-opus-4-7
    python3 scripts/fresh-synthesis.py --model google/gemini-2.5-pro
    python3 scripts/fresh-synthesis.py --model openai/gpt-5.5

Future work (out of scope for v0): a scripts/benchmark-models.py that runs
the same prompt against multiple models and produces a side-by-side
comparison artifact in evals/.
"""

import os
import sys
import json
import glob
import datetime
import argparse
import subprocess
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

# Default model. Override with --model.
DEFAULT_MODEL = "deepseek/deepseek-v4-pro"

# OpenRouter pricing per Mtok (input, output) — used for cost reporting.
# Update when new model slugs are added or pricing changes. If a model
# isn't in this map, cost reporting falls back to "unknown".
PRICING_USD_PER_MTOK = {
    "deepseek/deepseek-v4-pro":   (0.435, 0.87),
    "deepseek/deepseek-v4-flash": (0.14, 0.28),
    "anthropic/claude-3.5-sonnet": (3.00, 15.00),
    "anthropic/claude-3-opus":    (15.00, 75.00),
    "google/gemini-2.5-pro":      (1.25, 5.00),
    "openai/gpt-5":               (2.50, 10.00),
}

# --- Argparse -------------------------------------------------------------------
parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
parser.add_argument("--model", default=DEFAULT_MODEL,
                    help=f"OpenRouter model slug (default: {DEFAULT_MODEL})")
parser.add_argument("--max-tokens", type=int, default=6000,
                    help="Output token budget (default 6K)")
args = parser.parse_args()

# --- Read API key from env first, fall back to .env (no logging the value) -----
API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not API_KEY:
    env_path = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("OPENROUTER_API_KEY="):
                    API_KEY = line.split("=", 1)[1].strip()
                    break
if not API_KEY:
    sys.exit("OPENROUTER_API_KEY not in env or .env")

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

# --- Fresh-synthesis prompt ----------------------------------------------------
# The substrate is the entire wiki corpus PLUS synthesis/queue/, so the model
# can see what the daemon's Pass 2 has been surfacing and produce a differential.
# The prompt is intentionally model-agnostic — only the corpus and the model slug
# vary between runs.
substrate_commit = subprocess.run(
    ["git", "rev-parse", "--short", "HEAD"],
    capture_output=True, text=True, check=False,
).stdout.strip() or "unknown"

prompt = f"""You are running an independent full-corpus synthesis on the Open Enzyme research wiki.

This wiki is normally maintained by a 3-pass daemon (Pass 1 Propagate → Pass 2 Synthesize → Pass 3 Review) that fires on each push. The most recent daemon-produced synthesis is at the top of `synthesis/queue/`. The wiki corpus below is the substrate; `synthesis/queue/` is included so you can see what the daemon has already surfaced.

Your task: do an independent Pass-2-style synthesis on the same corpus, then compare against what the daemon has been finding.

1. Read the entire corpus below (files concatenated under `=== filename ===` markers).
2. Read the most recent block at the top of `synthesis/queue/` carefully — that's what the daemon's Pass 2 surfaced (with Pass 3 review verdicts inline).
3. Generate your own synthesis: new connections you would surface, contradictions you spot, experiments you would propose, open questions you would flag.
4. Add a final **Differential Analysis** section: which of the daemon's findings do you confirm, partially-confirm, push back on, or reject? What did the daemon miss that you found? What did the daemon find that you did not? Be specific — cite document names and PMIDs where applicable.

Output format:

```
## Fresh synthesis — {{date}}

**Model**: {args.model} (via OpenRouter)
**Substrate**: Open Enzyme wiki at commit {substrate_commit}

### New Connections

(numbered, each with Documents Connected / Why It Matters / Suggested Action / Supported-or-Speculative tag)

### Contradictions Found

### Proposed Experiments (ranked by insight per cost)

### Open Questions

### Differential Analysis vs. the daemon's most recent synthesis

Confirmed: ...
Partially confirmed: ...
Push-back: ...
Rejected: ...
Missed by the daemon (newly surfaced here): ...
Missed here (daemon caught): ...
```

Discipline:
- Tag every substantive claim with evidence level: **Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation**.
- Mark each Connection as **Supported** (multiple sources align) or **Speculative** (reasonable but unvalidated).
- Cite specific document names and PMIDs where applicable.
- Do NOT propose file edits. Do NOT generate commit messages. Synthesis text only.
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
print(f"\nCalling {args.model} via OpenRouter ...")

request_body = {
    "model": args.model,
    "messages": [{"role": "user", "content": prompt}],
    # Smaller output budget = more headroom for input under OpenRouter's 512K cap.
    "max_tokens": args.max_tokens,
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
            "-H", "X-Title: Open Enzyme fresh-synthesis",
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

# Look up pricing for the chosen model. Falls back to V4-Pro pricing if
# unknown — adjust PRICING_USD_PER_MTOK at top of file when adding models.
in_per_mtok, out_per_mtok = PRICING_USD_PER_MTOK.get(
    args.model, PRICING_USD_PER_MTOK[DEFAULT_MODEL]
)
input_cost = prompt_tokens * in_per_mtok / 1_000_000
output_cost = completion_tokens * out_per_mtok / 1_000_000
total_cost = input_cost + output_cost

print(f"\nResponse received.")
print(f"  Input tokens:  {prompt_tokens:,} (estimated {prompt_token_estimate:,})")
print(f"  Output tokens: {completion_tokens:,}")
print(f"  Cost:          ${total_cost:.4f}  (in: ${input_cost:.4f}, out: ${output_cost:.4f})")

# --- Save output ---------------------------------------------------------------
date_str = datetime.date.today().isoformat()
# Model-tagged filename so head-to-head runs on the same date don't overwrite.
model_tag = args.model.split("/")[-1].replace("-pro", "").replace("-", "")
output_path = f"logs/fresh-synth-{model_tag}-{date_str}.md"
os.makedirs("logs", exist_ok=True)

header = f"""---
title: "Fresh synthesis ({args.model}) — {date_str}"
date: {date_str}
model: {args.model} (via OpenRouter)
substrate_commit: {substrate_commit}
input_tokens: {prompt_tokens}
output_tokens: {completion_tokens}
cost_usd: {total_cost:.4f}
---

# Fresh synthesis — {args.model} — {date_str}

Independent full-corpus synthesis run via `scripts/fresh-synthesis.py`. The model
read the entire wiki corpus (including `synthesis/queue/`, so it could see what
the daemon's Pass 2 has been surfacing) and produced its own findings plus a
differential analysis. Output below is verbatim model output, unedited.

This is the manual sibling of the daemon's Pass 2 — same substrate, different
model, run on demand rather than on push. Useful for benchmarking new long-context
models against the corpus and for surfacing what the daemon's vendor mix has been
missing.

---

"""

with open(output_path, "w") as f:
    f.write(header + content + "\n")

print(f"\nSaved: {output_path}")
print(f"\nNext: read {output_path} and compare its Differential Analysis section against the most recent sweep block at the top of synthesis/queue/.")
