#!/usr/bin/env python3
"""
sweep-3-review.py — Pass 3 reviewer driver via OpenRouter.

Routes through OpenRouter (default: anthropic/claude-opus-4-7) so we are
not bound by the Anthropic-direct 30K ITPM cap.

Execution model — agentic with bounded iterations:

  1. Inline the Pass 2 synthesis log + the trigger files (the recent
     changes Pass 2 synthesized from) + the cited_files (every wiki/*.md
     Pass 2 referenced in any finding). This is the "warm cache" — the
     reviewer has direct access to the most likely sources without a
     tool round-trip.
  2. Provide read-only research tools (read_file, list_files, grep) so
     the reviewer can investigate any file the inlined cache missed.
     Pass 3 verifies claims, so the ability to look at primary sources
     on-demand matters more than the round-trip overhead.
  3. The reviewer signals completion by returning content (no tool
     calls). That content is the final review output: review blockquotes
     separated by `<<<NEXT>>>` markers. The downstream synthesis-merge.py
     script does deterministic substitution into wiki/synthesis.md.

Why agentic now (was one-shot pre-2026-04-28): Pass 3 is critique, but
critique without source-material access is just internal-consistency
checking, not real review. The previous one-shot design made the
reviewer say "I can't confirm because I don't have the trigger file"
when a cited file wasn't pre-loaded — observed in the 2026-04-27 cycle.
Adding bounded read-only tool access lets the reviewer fetch what the
inlined warm cache missed without giving it write or edit power.

Strict scope preserved: tools are read-only, max iterations capped, and
the final output is still ONLY the review blockquotes separated by
`<<<NEXT>>>`. The synthesis-merge script counts separators and bails on
mismatch, so any verbose preamble from the model would fail-fast.

Usage in CI:
    python3 scripts/sweep-3-review.py \\
        --synthesis-log logs/v4-synthesis-<date>-<sha>.md \\
        --commit-sha "$GITHUB_SHA" \\
        --diff-base "<sha>" \\
        --trigger-files "wiki/foo.md\\nwiki/bar.md" \\
        --cited-files "wiki/abcg2-modulators.md\\nwiki/lactoferrin.md" \\
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

DEFAULT_MODEL = "anthropic/claude-opus-4-7"
DEFAULT_PROMPT = "scripts/sweep-prompt-3-review.md"
MAX_TOOL_ITERATIONS = 8  # bound research depth; final response counts as "done"

PRICING_USD_PER_MTOK = {
    "anthropic/claude-sonnet-4-6":  (3.00, 15.00),
    "anthropic/claude-haiku-4-5":   (0.80, 4.00),
    "anthropic/claude-opus-4-7":    (15.00, 75.00),
    "google/gemini-2.5-pro":        (1.25, 5.00),
}

# Read-only research tools for Pass 3. NO edit, NO write — Pass 3 is
# critique, not propagation. Tools are bounded by MAX_TOOL_ITERATIONS.
TOOLS = [
    {"type": "function", "function": {
        "name": "read_file",
        "description": (
            "Read a file in the repository. Use to verify claims in the Pass 2 "
            "synthesis against primary wiki content, especially when a cited "
            "file isn't in the inlined warm cache."),
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string", "description": "repo-relative path, e.g. wiki/abcg2-modulators.md"},
        }, "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "list_files",
        "description": "List files matching a glob (e.g. 'wiki/*.md').",
        "parameters": {"type": "object", "properties": {
            "pattern": {"type": "string"},
        }, "required": ["pattern"]}}},
    {"type": "function", "function": {
        "name": "grep",
        "description": (
            "Search a regex across files. Returns paths and line numbers. "
            "Use to find where a claim is grounded in the wiki, or to check "
            "whether a cited mechanism appears as the synthesizer described."),
        "parameters": {"type": "object", "properties": {
            "pattern": {"type": "string"},
            "glob":    {"type": "string", "description": "e.g. 'wiki/*.md'"},
        }, "required": ["pattern"]}}},
]


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


def safe_path(rel):
    abs_path = os.path.realpath(os.path.join(REPO_ROOT, rel))
    if not abs_path.startswith(REPO_ROOT + os.sep) and abs_path != REPO_ROOT:
        raise ValueError(f"path {rel!r} escapes repo root")
    return abs_path


def tool_read_file(args):
    try:
        p = safe_path(args["path"])
    except ValueError as e:
        return f"ERROR: {e}"
    if not os.path.exists(p):
        return f"ERROR: file not found: {args['path']}"
    return open(p).read()


def tool_list_files(args):
    matches = glob.glob(os.path.join(REPO_ROOT, args["pattern"]), recursive=True)
    rels = sorted([os.path.relpath(m, REPO_ROOT) for m in matches])
    return "\n".join(rels) if rels else "(no matches)"


def tool_grep(args):
    cmd = ["grep", "-rn", args["pattern"]]
    if args.get("glob"):
        cmd += ["--include=" + args["glob"]]
    cmd.append(REPO_ROOT)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return "ERROR: grep timed out"
    if r.returncode == 1:
        return "(no matches)"
    if r.returncode != 0:
        return f"ERROR: grep failed: {r.stderr.strip()}"
    # Strip the absolute repo prefix for readability
    out = r.stdout.replace(REPO_ROOT + "/", "")
    # Cap output to keep tool responses small
    if len(out) > 8000:
        out = out[:8000] + "\n... (truncated)"
    return out


TOOL_HANDLERS = {
    "read_file":  tool_read_file,
    "list_files": tool_list_files,
    "grep":       tool_grep,
}


def build_evidence_context(trigger_files, cited_files):
    """Inline trigger + cited files. Trigger files are the cause of the
    sweep; cited_files are everything Pass 2 referenced in its synthesis.
    Both go into the warm cache so the reviewer doesn't need a tool
    round-trip for the most likely sources."""
    seen = set()
    parts = []
    included = []
    for label, paths in (("trigger", trigger_files), ("cited", cited_files)):
        for p in paths:
            if p in seen or not os.path.exists(p):
                continue
            seen.add(p)
            with open(p) as f:
                parts.append(f"\n\n=== {p} ({label}) ===\n\n{f.read()}")
                included.append((p, label))
    return "".join(parts), included


def run_agentic_review(api_key, model, initial_prompt, max_iterations, max_tokens):
    """Drive the bounded agentic loop: tool calls until the model returns
    a final response (no tool calls), then return that final content.
    Returns (content, total_in_tokens, total_out_tokens). Raises SystemExit
    on hard failures."""
    messages = [{"role": "user", "content": initial_prompt}]
    total_in = 0
    total_out = 0

    for iteration in range(max_iterations + 1):
        body = {
            "model": model,
            "messages": messages,
            "tools": TOOLS,
            "max_tokens": max_tokens,
            "temperature": 0.5,
        }
        # Force a final response on the last allowed iteration — no more tool
        # calls accepted.
        if iteration == max_iterations:
            body["tool_choice"] = "none"

        resp = call_openrouter_raw(api_key, body)
        if "choices" not in resp:
            print(f"Unexpected response shape: {json.dumps(resp, indent=2)[:1500]}",
                  file=sys.stderr)
            sys.exit(1)
        choice = resp["choices"][0]
        msg = choice.get("message", {}) or {}
        usage = resp.get("usage", {}) or {}
        total_in += usage.get("prompt_tokens", 0)
        total_out += usage.get("completion_tokens", 0)

        tool_calls = msg.get("tool_calls") or []
        content = msg.get("content")

        # Terminal: model returned content with no tool calls. That's our
        # final review output.
        if content and not tool_calls:
            return content, total_in, total_out

        # If there are tool calls, execute each and append the results.
        if tool_calls:
            messages.append({
                "role": "assistant",
                "content": content or "",
                "tool_calls": tool_calls,
            })
            for tc in tool_calls:
                fn = (tc.get("function") or {})
                name = fn.get("name")
                raw_args = fn.get("arguments") or "{}"
                try:
                    parsed = json.loads(raw_args)
                except json.JSONDecodeError:
                    result = f"ERROR: tool args not JSON: {raw_args[:200]}"
                else:
                    handler = TOOL_HANDLERS.get(name)
                    if not handler:
                        result = f"ERROR: unknown tool {name!r}"
                    else:
                        try:
                            result = handler(parsed)
                        except Exception as e:
                            result = f"ERROR: {type(e).__name__}: {e}"
                # Cap each tool result to keep the loop bounded
                if len(result) > 30_000:
                    result = result[:30_000] + "\n... (truncated, use grep to narrow)"
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.get("id", ""),
                    "name": name or "",
                    "content": result,
                })
            print(f"  [iter {iteration+1}/{max_iterations}] {len(tool_calls)} tool call(s) processed",
                  file=sys.stderr)
            continue

        # No content, no tool calls — pathological. Bail.
        print(
            f"OpenRouter returned no content and no tool calls "
            f"(finish_reason={choice.get('finish_reason', '?')!r}). "
            f"Full message: {json.dumps(msg, indent=2)[:1500]}",
            file=sys.stderr,
        )
        sys.exit(1)

    # If we somehow exit the loop without returning, that's a bug
    print(f"Pass 3 agentic loop exhausted {max_iterations} iterations without final content",
          file=sys.stderr)
    sys.exit(1)


def call_openrouter_raw(api_key, body):
    """Lower-level OpenRouter call — handles retries and returns parsed JSON."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        json.dump(body, tf)
        body_path = tf.name
    try:
        max_retries = 4
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
                print(f"OpenRouter call failed (exit {r.returncode}): {r.stderr.strip()}",
                      file=sys.stderr)
                print(f"stdout: {r.stdout[:1500]}", file=sys.stderr)
                sys.exit(1)
            backoff = [10, 30, 60, 120][attempt] if attempt < 4 else 120
            print(f"  [retry {attempt+1}/{max_retries-1}] transient error, sleeping {backoff}s ...",
                  file=sys.stderr, flush=True)
            time.sleep(backoff)
    finally:
        os.unlink(body_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--synthesis-log", required=True,
                        help="Path to the Pass 2 synthesis log")
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--diff-base", default="")
    parser.add_argument("--trigger-files", required=True,
                        help="Comma- or newline-separated list of trigger files")
    parser.add_argument("--cited-files", default="",
                        help=("Comma- or newline-separated list of files Pass 2 "
                              "cited in any synthesis finding. Inlined into the "
                              "warm cache so the reviewer can verify cited "
                              "content without a tool round-trip."))
    parser.add_argument("--marker-count", type=int, required=True)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--max-tokens", type=int, default=8000)
    parser.add_argument("--max-iterations", type=int, default=MAX_TOOL_ITERATIONS,
                        help=f"Tool-use iteration cap (default {MAX_TOOL_ITERATIONS})")
    args = parser.parse_args()

    api_key = read_api_key()

    if not os.path.exists(args.synthesis_log):
        sys.exit(f"Synthesis log not found: {args.synthesis_log}")
    synthesis_text = open(args.synthesis_log).read()

    sweep_brief = open(args.prompt_file).read()

    def _split(s):
        return [p.strip() for p in s.replace(",", "\n").splitlines() if p.strip()]

    trigger_files = _split(args.trigger_files)
    cited_files = _split(args.cited_files)
    evidence_context, included = build_evidence_context(trigger_files, cited_files)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    trigger_list = "\n".join(f"  - {f}" for f in trigger_files) or "  (none specified)"
    cited_list = "\n".join(f"  - {f}" for f in cited_files) or "  (none parsed from synthesis)"

    prompt = (
        sweep_brief
        + "\n\n---\n\n"
        + f"TRIGGER: Pass 3 review at {timestamp}.\n"
        + f"  synthesis_log:    {args.synthesis_log}\n"
        + f"  marker_count:     {args.marker_count}\n"
        + f"  diff_base:        {args.diff_base or 'unknown'}\n"
        + f"  commit_sha:       {args.commit_sha}\n"
        + f"  trigger files (caused this sweep):\n{trigger_list}\n"
        + f"  cited files (Pass 2 referenced these):\n{cited_list}\n"
        + f"  max_tool_iterations: {args.max_iterations}\n"
        + "ci=github-actions-sweep-3-review\n\n"
        + "Tools available: read_file, list_files, grep (read-only). Use them\n"
        + "to verify any claim against primary sources. The inlined evidence\n"
        + "below is the warm cache; if you need a file not in there, fetch it.\n"
        + "When done researching, return your review blockquotes — that signals\n"
        + "completion (no more tool calls).\n\n"
        + "=== PASS 2 SYNTHESIS LOG ===\n\n"
        + synthesis_text
        + "\n\n=== INLINED EVIDENCE (trigger + cited files) ===\n"
        + evidence_context
    )

    prompt_chars = len(prompt)
    prompt_tok_est = prompt_chars // 4
    n_trig = sum(1 for _, lab in included if lab == "trigger")
    n_cited = sum(1 for _, lab in included if lab == "cited")
    print(f"Pass 3 prompt: synthesis log + {n_trig} trigger + {n_cited} cited files inlined "
          f"(~{prompt_tok_est:,} tokens est.); tool iters cap {args.max_iterations}",
          file=sys.stderr)
    if prompt_tok_est > 180_000:
        print(f"WARNING: estimate {prompt_tok_est:,} tokens — close to Opus's 200K cap.",
              file=sys.stderr)

    content, in_tok, out_tok = run_agentic_review(
        api_key, args.model, prompt,
        max_iterations=args.max_iterations,
        max_tokens=args.max_tokens,
    )

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
