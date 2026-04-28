#!/usr/bin/env python3
"""
sweep-3-review.py — Pass 3 reviewer driver via OpenRouter.

Replaces `claude --dangerously-skip-permissions -p ...` for Pass 3. Routes
through OpenRouter (default: anthropic/claude-sonnet-4-6) so we are not
bound by the Anthropic-direct 30K ITPM cap, which kills Pass 3 on the full
wiki corpus the same way it killed Pass 1.

This is a one-shot synthesis call (not agentic): we inline the Pass 2
synthesis log + the wiki corpus + the Pass 3 review brief, and the model
writes review blockquotes separated by `<<<NEXT>>>` markers to stdout.
The downstream synthesis-merge.py script does the deterministic
substitution into wiki/synthesis.md.

Why one-shot rather than agentic: Pass 3 is critique, not exploration.
Sending the whole corpus inline lets the model spot-check any cited file
in zero extra round trips. Simpler than wiring a custom agentic harness.

Usage in CI:
    python3 scripts/sweep-3-review.py \\
        --synthesis-log logs/v4-synthesis-<date>-<sha>.md \\
        --commit-sha "$GITHUB_SHA" \\
        --diff-base "<sha>" \\
        --trigger-files "wiki/foo.md\\nwiki/bar.md" \\
        --marker-count 12 \\
      > reviews.txt
"""

import argparse
import datetime
import glob
import json
import os
import subprocess
import sys
import tempfile
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

DEFAULT_MODEL = "anthropic/claude-sonnet-4-6"
DEFAULT_PROMPT = "scripts/sweep-prompt-3-review.md"

# Pass 3 sees the synthesis log + the trigger files (recent changes the
# synthesis is grounded in). NOT the full wiki corpus — that exceeds
# Sonnet's 200K context. The synthesis log already inlines its citations,
# and Pass 3 is critique, not exhaustive primary-source verification.

PRICING_USD_PER_MTOK = {
    "anthropic/claude-sonnet-4-6":  (3.00, 15.00),
    "anthropic/claude-haiku-4-5":   (0.80, 4.00),
    "anthropic/claude-opus-4-7":    (15.00, 75.00),
    "google/gemini-2.5-pro":        (1.25, 5.00),
}


def read_api_key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k
    env_path = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_path):
        for line in open(env_path):
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("OPENROUTER_API_KEY not set in env or .env")


def build_trigger_context(trigger_files):
    """Inline the trigger files (the recent changes Pass 2 synthesized from)."""
    parts = []
    included = []
    for p in trigger_files:
        if not os.path.exists(p):
            continue
        with open(p) as f:
            parts.append(f"\n\n=== {p} ===\n\n{f.read()}")
            included.append(p)
    return "".join(parts), included


def call_openrouter(api_key, model, messages, max_tokens=8000, max_retries=4):
    body = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.5,
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        json.dump(body, tf)
        body_path = tf.name
    try:
        for attempt in range(max_retries):
            r = subprocess.run(
                ["curl", "-sS", "--fail-with-body",
                 "https://openrouter.ai/api/v1/chat/completions",
                 "-H", f"Authorization: Bearer {api_key}",
                 "-H", "Content-Type: application/json",
                 "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                 "-H", "X-Title: Open Enzyme sweep Pass 3",
                 "-d", f"@{body_path}",
                 "--max-time", "600"],
                capture_output=True, text=True, timeout=620,
            )
            if r.returncode == 0:
                try:
                    return json.loads(r.stdout)
                except json.JSONDecodeError:
                    sys.exit(f"Non-JSON response: {r.stdout[:1500]}")
            # Transient detection across BOTH stdout and stderr. See
            # sweep-1-propagate.py for the rationale (curl --fail-with-body
            # writes HTTP status to stderr; checking only stdout missed real
            # 503s in run 25049501442, 2026-04-28).
            combined = (r.stdout or "") + "\n" + (r.stderr or "")
            transient = (
                r.returncode == 22
                or any(s in combined for s in (
                    "429", "rate-limit", "rate limit", "temporarily",
                    "502", "503", "504",
                    "Connection reset", "Connection refused",
                    "timed out", "timeout",
                ))
            )
            if not transient or attempt == max_retries - 1:
                print(f"OpenRouter call failed (exit {r.returncode}): {r.stderr.strip()}", file=sys.stderr)
                print(f"stdout: {r.stdout[:1500]}", file=sys.stderr)
                sys.exit(1)
            backoff = [10, 30, 60, 120][attempt] if attempt < 4 else 120
            print(f"  [retry {attempt+1}/{max_retries-1}] transient error, sleeping {backoff}s ...", file=sys.stderr, flush=True)
            time.sleep(backoff)
    finally:
        os.unlink(body_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--synthesis-log", required=True,
                        help="Path to the Pass 2 synthesis log")
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--diff-base", default="")
    parser.add_argument("--trigger-files", required=True)
    parser.add_argument("--marker-count", type=int, required=True)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--max-tokens", type=int, default=8000)
    args = parser.parse_args()

    api_key = read_api_key()

    if not os.path.exists(args.synthesis_log):
        sys.exit(f"Synthesis log not found: {args.synthesis_log}")
    synthesis_text = open(args.synthesis_log).read()

    sweep_brief = open(args.prompt_file).read()

    raw_triggers = args.trigger_files.replace(",", "\n")
    trigger_files = [p.strip() for p in raw_triggers.splitlines() if p.strip()]
    trigger_context, included_triggers = build_trigger_context(trigger_files)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    trigger_list = "\n".join(f"  - {f}" for f in trigger_files)

    prompt = (
        sweep_brief
        + "\n\n---\n\n"
        + f"TRIGGER: Pass 3 review at {timestamp}.\n"
        + f"  synthesis_log:    {args.synthesis_log}\n"
        + f"  marker_count:     {args.marker_count}\n"
        + f"  diff_base:        {args.diff_base or 'unknown'}\n"
        + f"  commit_sha:       {args.commit_sha}\n"
        + f"  trigger files:\n{trigger_list}\n"
        + "ci=github-actions-sweep-3-review\n\n"
        + "=== PASS 2 SYNTHESIS LOG ===\n\n"
        + synthesis_text
        + "\n\n=== TRIGGER FILES (the recent changes Pass 2 synthesized from) ===\n"
        + trigger_context
    )

    prompt_chars = len(prompt)
    prompt_tok_est = prompt_chars // 4
    print(f"Pass 3 prompt: synthesis log + {len(included_triggers)} trigger files, "
          f"~{prompt_tok_est:,} tokens (est.)", file=sys.stderr)
    if prompt_tok_est > 180_000:
        print(f"WARNING: estimate {prompt_tok_est:,} tokens — close to Sonnet's 200K cap.",
              file=sys.stderr)

    resp = call_openrouter(
        api_key, args.model,
        [{"role": "user", "content": prompt}],
        max_tokens=args.max_tokens,
    )

    if "choices" not in resp:
        print(f"Unexpected response: {json.dumps(resp, indent=2)[:1500]}", file=sys.stderr)
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
        sys.exit(1)

    usage = resp.get("usage", {})
    in_tok = usage.get("prompt_tokens", 0)
    out_tok = usage.get("completion_tokens", 0)
    in_per, out_per = PRICING_USD_PER_MTOK.get(args.model, (None, None))
    if in_per is not None:
        cost = (in_tok * in_per + out_tok * out_per) / 1_000_000
        cost_str = f"${cost:.4f}"
    else:
        cost_str = "(unknown)"

    print(f"Tokens: in={in_tok:,} out={out_tok:,} cost={cost_str}", file=sys.stderr)

    # Reviews go to stdout — workflow captures to REVIEWS_FILE
    sys.stdout.write(content)
    if not content.endswith("\n"):
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
