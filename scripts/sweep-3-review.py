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
MAX_TOOL_ITERATIONS = 16  # bound research depth; final response counts as "done"

PRICING_USD_PER_MTOK = {
    "anthropic/claude-sonnet-4-6":  (3.00, 15.00),
    "anthropic/claude-haiku-4-5":   (0.80, 4.00),
    "anthropic/claude-opus-4-7":    (15.00, 75.00),
    "google/gemini-2.5-pro":        (1.25, 5.00),
}

# Anthropic prompt-cache read pricing per Mtok. Cache reads bill at 10% of
# base input; cache writes bill at 1.25× base. Same caveat as Pass 1
# (sweep-1-propagate.py): OpenRouter's OAI-compat usage shim only exposes
# read tokens via prompt_tokens_details, so reported cost treats writes at
# 1× and slightly under-reports vs. the OpenRouter dashboard. Direction
# (cached < non-cached) is correct; magnitude is optimistic.
CACHE_READ_USD_PER_MTOK = {
    "anthropic/claude-sonnet-4-6":  0.30,
    "anthropic/claude-haiku-4-5":   0.08,
    "anthropic/claude-opus-4-7":    1.50,
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


def build_evidence_context(trigger_files, cited_files, char_budget=1_400_000):
    """Inline trigger + cited files. Trigger files are the cause of the
    sweep; cited_files are everything Pass 2 referenced in its synthesis.
    Both go into the warm cache so the reviewer doesn't need a tool
    round-trip for the most likely sources.

    char_budget: hard cap on total inlined characters. Default 1.4M chars
    ≈ 350K tokens. Pass 3 is agentic — the model can run up to 16 tool
    round-trips, each shipping the entire accumulated message history
    back to the model. A single round-trip with one wiki-file read +
    intermediate reasoning consumes ~50-100K tokens. The cumulative-size
    guard in run_agentic_review (CUMULATIVE_CHAR_BUDGET = 900K tokens)
    force-finishes before Opus's 1M cap, so in practice the effective max
    iters is bounded by cumulative cost: 350K initial + ~75K per round
    ≈ 7-10 rounds before the guard fires. The 16-iter ceiling is a
    safety net against runaway loops, not the binding constraint —
    cumulative budget is. Bumped 8 → 16 (2026-05-07) after the
    abc8de9 run hit the 8-iter cap before producing final output.
    Trigger files always inline (skipping a triggering file breaks the
    review's premise); cited files inline until budget, then are skipped
    with a notice (the model can still tool-fetch them).

    Returns (concatenated_text, included_list, skipped_list).
    `included_list`: [(path, label)] for files actually inlined.
    `skipped_list`: [(path, label, reason)] for files skipped — these
    appear in the final prompt as a "not inlined; tool-fetch if needed"
    section so the reviewer knows the file exists and why it wasn't pre-loaded.
    """
    seen = set()
    parts = []
    included = []
    skipped = []
    used_chars = 0
    # Trigger files always inline — skipping a trigger breaks the premise
    # of the review (you're reviewing changes triggered by these files).
    # Cited files are best-effort: inline until budget, then skip.
    for label, paths, force in (
        ("trigger", trigger_files, True),
        ("cited", cited_files, False),
    ):
        for p in paths:
            if p in seen or not os.path.exists(p):
                continue
            seen.add(p)
            with open(p) as f:
                content = f.read()
            entry = f"\n\n=== {p} ({label}) ===\n\n{content}"
            entry_chars = len(entry)
            if not force and used_chars + entry_chars > char_budget:
                skipped.append((p, label, f"budget ({used_chars:,} + {entry_chars:,} chars > {char_budget:,} cap)"))
                continue
            parts.append(entry)
            included.append((p, label))
            used_chars += entry_chars
    return "".join(parts), included, skipped


def _inject_cache_breakpoints(messages, model):
    """Return a copy of `messages` with `cache_control` markers on the
    initial user prompt and the most recent tool message.

    Pass 3's structure differs from Pass 1: there's no system role.
    Message 0 is the user prompt with the synthesis log + trigger files +
    cited files inlined (~250–400K tokens on a typical sweep). That's the
    breakpoint that matters most — without it, every iteration re-pays
    full input price on a quarter-million-token prefix that hasn't
    changed. Cache-write on the latest tool message gives a rolling
    checkpoint: each iter writes, the next iter reads.

    Anthropic models honor the markers via OpenRouter's pass-through
    (10% cache-read pricing); DeepSeek/OpenAI cache automatically and
    ignore the markers; the array-of-blocks content shape is valid
    OpenAI-compat for every provider, so the transform is safe to apply
    unconditionally. See sweep-1-propagate.py for the validation history
    and per-provider notes.
    """
    if not messages:
        return messages
    last_tool_idx = -1
    for i, m in enumerate(messages):
        if m.get("role") == "tool":
            last_tool_idx = i
    out = []
    for i, m in enumerate(messages):
        m2 = dict(m)
        # Cache the initial user prompt (huge inlined evidence block)
        if i == 0 and m2.get("role") == "user" and isinstance(m2.get("content"), str):
            m2["content"] = [{
                "type": "text",
                "text": m2["content"],
                "cache_control": {"type": "ephemeral"},
            }]
        # Rolling cache write on the latest tool message
        elif i == last_tool_idx and isinstance(m2.get("content"), str):
            m2["content"] = [{
                "type": "text",
                "text": m2["content"],
                "cache_control": {"type": "ephemeral"},
            }]
        out.append(m2)
    return out


def run_agentic_review(api_key, model, initial_prompt, max_iterations, max_tokens):
    """Drive the bounded agentic loop: tool calls until the model returns
    a final response (no tool calls), then return that final content.
    Returns (content, total_in_tokens, total_out_tokens). Raises SystemExit
    on hard failures.

    Cumulative-size guard: before each API call, estimate the total prompt
    size (sum of message contents). If approaching the model's context cap
    (Opus = 1M tokens ≈ 4M chars), force the next call to be the final
    one (tool_choice=none) so we don't ship an over-cap request that
    OpenRouter will 400 on. This is the post-mortem fix for the 21:17Z
    failure where 4 tool round-trips pushed cumulative input to 1.023M
    tokens > 1M cap."""
    # Conservative cap: 3.6M chars ≈ 900K tokens. Leave 100K headroom
    # for the model's response + finishing reasoning. Opus's true cap
    # is 1M tokens so we want to force-finish well before that.
    CUMULATIVE_CHAR_BUDGET = 3_600_000

    messages = [{"role": "user", "content": initial_prompt}]
    total_in = 0
    total_out = 0
    total_cached = 0

    for iteration in range(max_iterations + 1):
        # Estimate cumulative request size in chars; force-finish if approaching cap
        cumulative_chars = sum(
            len(m.get("content") or "") for m in messages
        )
        approaching_cap = cumulative_chars > CUMULATIVE_CHAR_BUDGET
        if approaching_cap:
            print(f"  [iter {iteration+1}/{max_iterations}] cumulative request {cumulative_chars:,} chars "
                  f"approaches budget {CUMULATIVE_CHAR_BUDGET:,}; forcing final response (no more tool calls)",
                  file=sys.stderr)

        body = {
            "model": model,
            "messages": _inject_cache_breakpoints(messages, model),
            "tools": TOOLS,
            "max_tokens": max_tokens,
            "temperature": 0.5,
        }
        # Force a final response on the last allowed iteration OR when
        # approaching the cumulative-size cap — no more tool calls accepted.
        if iteration == max_iterations or approaching_cap:
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
        total_cached += (usage.get("prompt_tokens_details") or {}).get("cached_tokens", 0)

        tool_calls = msg.get("tool_calls") or []
        content = msg.get("content")

        # Terminal: model returned content with no tool calls. That's our
        # final review output.
        if content and not tool_calls:
            return content, total_in, total_out, total_cached

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
    evidence_context, included, skipped = build_evidence_context(trigger_files, cited_files)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    trigger_list = "\n".join(f"  - {f}" for f in trigger_files) or "  (none specified)"
    cited_list = "\n".join(f"  - {f}" for f in cited_files) or "  (none parsed from synthesis)"
    if skipped:
        skipped_list = "\n".join(f"  - {f} ({label}) — {reason}" for f, label, reason in skipped)
        skipped_block = (
            f"  cited files SKIPPED from inlining (budget cap; tool-fetch if needed):\n"
            f"{skipped_list}\n"
        )
    else:
        skipped_block = ""

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
        + skipped_block
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
    # Opus's actual context cap is 1M tokens. Warn at 80% (800K) — well
    # below the cumulative-loop budget (900K) so warnings fire before the
    # agentic loop's force-finish guard would.
    if prompt_tok_est > 800_000:
        print(f"WARNING: estimate {prompt_tok_est:,} tokens — close to Opus's 1M cap. "
              f"build_evidence_context's char_budget may need to be lowered.",
              file=sys.stderr)

    content, in_tok, out_tok, cached_tok = run_agentic_review(
        api_key, args.model, prompt,
        max_iterations=args.max_iterations,
        max_tokens=args.max_tokens,
    )

    in_per, out_per = PRICING_USD_PER_MTOK.get(args.model, (None, None))
    cache_read_per = CACHE_READ_USD_PER_MTOK.get(args.model)
    non_cached = max(0, in_tok - cached_tok)
    if in_per is not None:
        if cache_read_per is not None and cached_tok > 0:
            cost = (
                non_cached * in_per
                + cached_tok * cache_read_per
                + out_tok * out_per
            ) / 1_000_000
        else:
            cost = (in_tok * in_per + out_tok * out_per) / 1_000_000
        cost_str = f"${cost:.4f}"
    else:
        cost_str = "(unknown)"

    cache_pct = (cached_tok / in_tok * 100) if in_tok else 0
    cache_note = f" (cached={cached_tok:,}, {cache_pct:.0f}%)" if cached_tok else ""
    print(f"Tokens: in={in_tok:,}{cache_note} out={out_tok:,} cost={cost_str}",
          file=sys.stderr)

    # Reviews go to stdout — workflow captures to REVIEWS_FILE
    sys.stdout.write(content)
    if not content.endswith("\n"):
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
