#!/usr/bin/env python3
"""
synthesize.py — Pass 2 of the hybrid sweep architecture.

Reads the full wiki corpus, calls a synthesis-capable model via OpenRouter
(default: DeepSeek V4-Pro), saves output to logs/v4-synthesis-<date>-<sha>.md.
Designed to be invoked by .github/workflows/wiki-sweep.yml after Pass 1
(Claude propagation) completes.

The "v4-synthesis-" log filename prefix is a fixed convention regardless of
the model used; the actual model is recorded in the log file's YAML frontmatter
under `reviewer_model:`. This means future logs are still discoverable by the
established naming pattern even when the default model changes.

Differs from scripts/peer-review.py: that script does *peer review* against
an existing Claude synthesis. This script does *fresh synthesis* with no
comparison baseline — Pass 3 (Claude review via scripts/synthesis-merge.py) is
what produces the differential.

Reads OPENROUTER_API_KEY from env first, falls back to .env (for local runs).
Reads scripts/sweep-prompt-2-synthesize.md for the model brief.

Usage in CI:
    python3 scripts/synthesize.py \\
        --commit-sha <full-sha> \\
        --trigger-files "wiki/file1.md,wiki/file2.md"

Usage locally:
    OPENROUTER_API_KEY=... python3 scripts/synthesize.py --commit-sha HEAD

The output filename is logs/v4-synthesis-<YYYY-MM-DD>-<sha7>.md and is printed
to stdout on success — the GitHub Actions step parses that to know which file
to commit and pass to Pass 3.
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

# OpenRouter caps deepseek/deepseek-v4-pro at 512K input tokens (platform
# policy, even though the model itself supports 1M). Excluding three low-
# synthesis-value files keeps us under that ceiling.
EXCLUDE = {
    "wiki/GRAPH.md",                  # Mermaid diagram — hard for non-vision models
    "wiki/references.md",             # bibliography
    "wiki/ai-bio-tools-playbook.md",  # tooling reference, not biology
}

# Default model. Override with --model.
# TODO(model-flexibility): when new long-context models land (Gemini Deep
# Research, Claude Opus with 1M, GPT-5 Pro, etc.), add them as --model
# options and benchmark against V4-Pro on the same corpus + prompt.
DEFAULT_MODEL = "deepseek/deepseek-v4-pro"


def read_api_key():
    """OPENROUTER_API_KEY from env first, fall back to .env file."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    env_path = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("OPENROUTER_API_KEY="):
                    return line.split("=", 1)[1].strip()
    sys.exit("OPENROUTER_API_KEY not in env or .env")


def build_corpus():
    """Concat all wiki/*.md and wiki/hypotheses/*.md, minus EXCLUDE."""
    paths = sorted(
        glob.glob("wiki/*.md") + glob.glob("wiki/hypotheses/*.md")
    )
    paths = [p for p in paths if p not in EXCLUDE]
    parts = []
    for p in paths:
        with open(p) as f:
            parts.append(f"\n\n=== {p} ===\n\n{f.read()}")
    return "".join(parts), paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True,
                        help="Full commit SHA (typically $GITHUB_SHA in CI)")
    parser.add_argument("--trigger-files", default="",
                        help="Comma-separated list of trigger files for the TRIGGER block")
    parser.add_argument("--diff-base", default="",
                        help="SHA of the last sweep commit (for the TRIGGER block)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"OpenRouter model slug (default: {DEFAULT_MODEL})")
    parser.add_argument("--prompt-file", default="scripts/sweep-prompt-2-synthesize.md",
                        help="Path to the synthesis prompt template")
    parser.add_argument("--max-tokens", type=int, default=8000,
                        help="Output token budget (default 8K)")
    args = parser.parse_args()

    api_key = read_api_key()

    # Build the prompt: model brief + corpus + TRIGGER block
    with open(args.prompt_file) as f:
        prompt_template = f.read()

    corpus, included_paths = build_corpus()
    sha_short = args.commit_sha[:7]
    date_str = datetime.date.today().isoformat()
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    output_path = f"logs/v4-synthesis-{date_str}-{sha_short}.md"

    trigger_block = (
        "\n\n---\n\n"
        f"TRIGGER: Sweep at {timestamp}, commit {args.commit_sha}.\n"
        f"  date_str: {date_str}\n"
        f"  sha_short: {sha_short}\n"
        f"  diff_base: {args.diff_base or 'unknown'}\n"
        f"  trigger files: {args.trigger_files or '(none specified)'}\n"
        f"  output_path: {output_path}\n"
        f"  reviewer_model: {args.model}\n"
        f"commit=yes\n"
        f"ci=github-actions-sweep-2-synthesize\n"
    )

    full_prompt = prompt_template + trigger_block + "\n\n=== CORPUS ===\n" + corpus
    prompt_chars = len(full_prompt)
    prompt_token_estimate = prompt_chars // 4
    print(f"Corpus: {len(included_paths)} files, ~{prompt_token_estimate:,} tokens (est.)",
          file=sys.stderr)

    # Sanity check
    if prompt_token_estimate > 480_000:
        print(f"WARNING: estimate {prompt_token_estimate:,} tokens — close to 512K cap. May need EXCLUDE expansion.",
              file=sys.stderr)

    # Build request body
    body = {
        "model": args.model,
        "messages": [{"role": "user", "content": full_prompt}],
        "max_tokens": args.max_tokens,
        "temperature": 0.7,
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        json.dump(body, tf)
        body_path = tf.name

    # Retry on transient upstream rate limits — V4-Pro routes through
    # Together / SiliconFlow / DeepInfra and these provider-side throttles
    # come and go. Backoff: 10s, 30s, 60s, 120s.
    import time as _time
    max_retries = 5
    result = None
    try:
        for attempt in range(max_retries):
            result = subprocess.run(
                [
                    "curl", "-sS", "--fail-with-body",
                    "https://openrouter.ai/api/v1/chat/completions",
                    "-H", f"Authorization: Bearer {api_key}",
                    "-H", "Content-Type: application/json",
                    "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                    "-H", "X-Title: Open Enzyme synthesis sweep",
                    "-d", f"@{body_path}",
                    "--max-time", "600",
                ],
                capture_output=True, text=True, timeout=620,
            )
            if result.returncode == 0:
                break
            transient = any(s in result.stdout for s in ("429", "rate-limit", "temporarily", "502", "503"))
            if not transient or attempt == max_retries - 1:
                break
            backoff = [10, 30, 60, 120][attempt] if attempt < 4 else 120
            print(f"  [retry {attempt+1}/{max_retries-1}] transient error, sleeping {backoff}s ...", file=sys.stderr, flush=True)
            _time.sleep(backoff)
    finally:
        os.unlink(body_path)

    if result.returncode != 0:
        print(f"curl failed (exit {result.returncode})", file=sys.stderr)
        print(f"stderr: {result.stderr.strip()}", file=sys.stderr)
        print(f"stdout: {result.stdout[:2000]}", file=sys.stderr)
        sys.exit(1)

    try:
        resp = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"Non-JSON response: {result.stdout[:2000]}", file=sys.stderr)
        sys.exit(1)

    if "choices" not in resp:
        print(f"Unexpected response: {json.dumps(resp, indent=2)[:2000]}", file=sys.stderr)
        sys.exit(1)

    choice = resp["choices"][0]
    content = choice.get("message", {}).get("content")
    finish_reason = choice.get("finish_reason", "?")
    if not content:
        print(
            f"OpenRouter returned empty content (finish_reason={finish_reason!r}). "
            f"Full choice: {json.dumps(choice, indent=2)[:1500]}",
            file=sys.stderr,
        )
        # Common causes: provider streamed an error, content filter, truncation
        # before any tokens. Exit non-zero so the workflow marks Pass 2 failed
        # and Pass 3 is correctly skipped — better than writing garbage.
        sys.exit(1)
    usage = resp.get("usage", {})
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)

    # OpenRouter pricing for deepseek-v4-pro: $0.435/Mtok in, $0.87/Mtok out
    cost_in = in_tok * 0.435 / 1_000_000
    cost_out = out_tok * 0.87 / 1_000_000
    cost_total = cost_in + cost_out

    print(f"Tokens: in={in_tok:,} out={out_tok:,}  cost=${cost_total:.4f}",
          file=sys.stderr)

    # Save with frontmatter
    os.makedirs("logs", exist_ok=True)
    header = (
        f"---\n"
        f"title: \"Synthesis — {date_str} (commit {sha_short})\"\n"
        f"date: {date_str}\n"
        f"commit: {args.commit_sha}\n"
        f"diff_base: {args.diff_base or 'unknown'}\n"
        f"trigger_files: {args.trigger_files or '(none)'}\n"
        f"reviewer_model: {args.model}\n"
        f"input_tokens: {in_tok}\n"
        f"output_tokens: {out_tok}\n"
        f"cost_usd: {cost_total:.4f}\n"
        f"corpus_files: {len(included_paths)}\n"
        f"---\n\n"
    )

    with open(output_path, "w") as f:
        f.write(header + content + "\n")

    # Pass-3 reviewer reads stdout to find the path
    print(output_path)


if __name__ == "__main__":
    main()
