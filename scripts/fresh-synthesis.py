#!/usr/bin/env python3
"""
fresh-synthesis.py — manual full-corpus synthesis with the model of your choice.

Local CLI tool (NOT the daemon path — see .github/workflows/wiki-sweep.yml
for the CI sweep). The daemon is a 3-pass pipeline (Pass 1 Propagate →
Pass 2 Synthesize → Pass 3 Review). This script is the manual sibling:
point it at a verified OpenRouter model and ask "what does THIS model find
across our corpus?"

Two main use cases:

1. **Model bench.** When a new long-context model ships (next Claude Opus,
   next Gemini, next GPT, next DeepSeek), run it across the corpus and
   compare its synthesis against what the daemon's Pass 2 has been
   surfacing. The architecture is intentionally model-agnostic — only the
   OpenRouter slug changes after its settings are verified in the registry.

2. **Second-opinion synthesis.** When you want fresh eyes on the corpus
   between daemon sweeps — a different vendor, a different prompt, a
   different time horizon — run this manually. It reads the full wiki
   INCLUDING synthesis/queue/, so it sees what the daemon has already
   surfaced and can produce a differential.

Reads OPENROUTER_API_KEY from env first, falls back to .env. Saves the raw
output under the system temporary directory for short-lived review. Apply any
accepted finding to its canonical wiki owner, then discard the raw file; Git
and the current corpus are the durable record. Reports token usage and cost.

Run from the repo root:
    python3 scripts/fresh-synthesis.py
    python3 scripts/fresh-synthesis.py --model anthropic/claude-opus-4.7
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

try:
    import model_settings
except ModuleNotFoundError:
    from scripts import model_settings

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

ROLE = model_settings.role("manual_fresh_synthesis")
DEFAULT_MODEL = ROLE["model"]

# --- Argparse -------------------------------------------------------------------
parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
parser.add_argument("--model", default=DEFAULT_MODEL,
                    help=f"OpenRouter model slug (default: {DEFAULT_MODEL})")
parser.add_argument("--max-tokens", type=int, default=ROLE["output_tokens"],
                    help="Output token budget (default from the versioned role)")
parser.add_argument("--prepare-only", action="store_true",
                    help="Validate settings and report projected cost without reading credentials or calling a model")
args = parser.parse_args()
try:
    model_settings.validate_context(args.model, 0, args.max_tokens)
except model_settings.ModelSettingsError as exc:
    sys.exit(str(exc))

# --- Build the corpus ----------------------------------------------------------
# All wiki/*.md only. Post-2026-05-08 migration `synthesis/` is sibling to
# wiki/, not under it; excluded from this corpus by scope. Concatenate with
# === filename === separators.
#
# Retain the existing corpus exclusions; route-specific context limits are
# checked against the selected model's versioned registry entry below.
#   - GRAPH.md: Mermaid diagram, hard for non-vision models to use
#   - references.md: bibliography only
#   - ai-bio-tools-playbook.md: tooling reference, not biology mechanism
EXCLUDE = {
    "wiki/GRAPH.md",
    "wiki/references.md",
    "wiki/ai-bio-tools-playbook.md",
}
# Includes synthesis/queue/*.md so the prompt's "queue is included" claim is
# truthful and the model can do a real differential vs the daemon's last output.
# (Codex round-2 #2: the prompt claimed queue inclusion the code didn't deliver.)
wiki_files = [p for p in sorted(
    glob.glob("wiki/*.md") + glob.glob("wiki/hypotheses/*.md") + glob.glob("synthesis/queue/*.md")
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
3. Run a grounding pass: identify the source-backed premises, evidence boundaries, contradictions, and constraints that can support or block cross-domain reasoning.
4. Run a deliberately creative connection pass. Be conservative about what you claim and aggressive about what you imagine. Seek high-upside connections between seemingly separate details. Direct evidence for the connecting leap is not required when the premises are grounded; label that output **Research Conjecture**, isolate the unsupported leap, and name a discriminating observation.
5. Run a boundary pass: reject only candidates with a failed premise, a disguised factual claim, a restatement, no discriminating observation, or too little upside. A negative result kills only the scope actually tested.
6. Add a final **Differential Analysis** section: which of the daemon's findings do you confirm, partially-confirm, push back on, or reject? What did the daemon miss that you found? What did the daemon find that you did not? Be specific — cite document names and PMIDs where applicable.

Output format:

```
## Fresh synthesis — {{date}}

**Model**: {args.model} (via OpenRouter)
**Substrate**: Open Enzyme wiki at commit {substrate_commit}

### New Connections

(numbered; use either a source-backed finding or this compact structure:
Epistemic status: Research Conjecture / Grounded Premises with evidence tags and sources /
Novel Leap with explicit absence of direct evidence / Why It Matters /
Discriminating Observation / Canonical Owner)

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
- **Research Conjecture is not an evidence level.** Its premises retain evidence tags; its leap is explicitly unsupported.
- Cite specific document names and PMIDs where applicable.
- Do NOT propose file edits. Do NOT generate commit messages. Synthesis text only.
- Honest framing: PhD audience. No marketing language. Distinguish proven from speculative.

[CORPUS BELOW]

{corpus}
"""

prompt_chars = len(prompt)
prompt_token_estimate = prompt_chars // 4
request_body = {
    "model": args.model,
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": args.max_tokens,
    "temperature": ROLE["temperature"],
}
try:
    request_body = model_settings.chat_body(request_body, margin=ROLE["context_margin_tokens"])
except model_settings.ModelSettingsError as exc:
    sys.exit(str(exc))
request_input_estimate = len(json.dumps(request_body, ensure_ascii=False)) / 4
if args.prepare_only:
    print(json.dumps({
        "model": args.model,
        "model_settings_sha256": model_settings.registry_sha256(),
        "corpus_files": len(wiki_files),
        "input_token_estimate": request_input_estimate,
        "max_output_tokens": args.max_tokens,
        "projected_cost_usd": model_settings.estimate_cost(args.model, request_input_estimate, args.max_tokens),
        "max_cost_usd": ROLE["max_cost_usd"],
    }, sort_keys=True))
    sys.exit(0)

# --- Read API key only after settings/context preflight ---------------------
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

print(f"Corpus: {len(wiki_files)} files, {corpus_chars:,} chars, ~{corpus_token_estimate:,} tokens (estimate)")
print(f"Total prompt: {prompt_chars:,} chars, ~{prompt_token_estimate:,} tokens (estimate)")
# --- Call OpenRouter via curl (avoids Python's macOS SSL cert quirk) -----------
print(f"\nCalling {args.model} via OpenRouter ...")

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

total_cost, cost_is_estimated = model_settings.usage_cost(args.model, usage)

print(f"\nResponse received.")
print(f"  Input tokens:  {prompt_tokens:,} (estimated {prompt_token_estimate:,})")
print(f"  Output tokens: {completion_tokens:,}")
print(f"  Cost:          ${total_cost:.4f}" + (" (estimated)" if cost_is_estimated else " (provider receipt)"))

# --- Save output ---------------------------------------------------------------
date_str = datetime.date.today().isoformat()
# Model-tagged filename so head-to-head runs on the same date don't overwrite.
model_tag = args.model.split("/")[-1].replace("-pro", "").replace("-", "")
output_dir = os.path.join(tempfile.gettempdir(), "open-enzyme-fresh-synthesis")
output_path = os.path.join(output_dir, f"fresh-synth-{model_tag}-{date_str}.md")
os.makedirs(output_dir, exist_ok=True)

header = f"""---
title: "Fresh synthesis ({args.model}) — {date_str}"
date: {date_str}
model: {args.model} (via OpenRouter)
substrate_commit: {substrate_commit}
input_tokens: {prompt_tokens}
output_tokens: {completion_tokens}
cost_usd: {total_cost:.4f}
cost_is_estimated: {str(cost_is_estimated).lower()}
model_settings_sha256: {model_settings.registry_sha256()}
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
print(f"\nNext: review {output_path}, route accepted findings to their canonical wiki owners, and delete the temporary file.")
