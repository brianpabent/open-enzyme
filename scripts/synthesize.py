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

Sibling script: scripts/fresh-synthesis.py runs a manual, model-agnostic
full-corpus synthesis (no daemon, no markers, model chosen via --model). Use
it for benchmarking new long-context models against the corpus or for
on-demand second-opinion synthesis between sweeps. This script (the daemon's
Pass 2) emits {{PEER-REVIEW}} markers for Pass 3 to substitute reviews into;
fresh-synthesis.py does not.

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
import re
import sys
import json
import glob
import datetime
import argparse
import subprocess
import tempfile
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

# Tool-use iteration cap. Pass 2 is single-shot synthesis with optional
# detail-fetch via read_file / list_directory. 20 reaches is generous; the
# discipline in the prompt is "reach when needed," not "fetch everything."
# On the last allowed iteration the loop force-finishes (tool_choice=none)
# so the model emits its synthesis log even if it hadn't decided to stop.
MAX_TOOL_ITERATIONS = 20

# Files excluded from the corpus regardless of model.
#
# As of 2026-05-15, the convention is to keep reference / methodology /
# tooling pages in `wiki/etc/` rather than maintaining a per-file EXCLUDE
# list. Pages in wiki/etc/ remain in the wiki (humans browsing find them
# via cross-reference and via the etc/README.md index) but the synthesis
# corpus skips the directory entirely.
#
# The build_corpus() loader already skips wiki/etc/* via its glob pattern
# (it globs wiki/*.md, not wiki/**/*.md, so wiki/etc/foo.md is naturally
# excluded). This set is kept empty for forward compatibility but should
# not need entries in normal operation — anything that doesn't belong in
# the synthesis corpus belongs in wiki/etc/.
EXCLUDE = set()

# Default Pass 2 synthesizer.
#
# Timeline:
#   2026-04-24: launched on deepseek/deepseek-v4-pro (~$0.20/sweep).
#   2026-04-25: switched to google/gemini-2.5-pro after V4-Pro through
#     OpenRouter exhibited two unreliable failure modes (sustained 429
#     throttling on Together / SiliconFlow, plus null-content responses
#     with finish_reason=null). Gemini 2.5 Pro produced the same three
#     top-tier connections V4-Pro found on 2026-04-24 (androgen ceiling,
#     fructose challenge, carnosine counter-agent) when run on the same
#     wiki corpus, plus extra contradiction-resolution and pushback work,
#     at ~3.3x the unit cost (~$0.65/sweep vs. ~$0.20).
#   2026-05-05 (attempt 1, REVERTED — see commit d023cbe / a412109):
#     compounding errors. First mistake: shipped DeepSeek V4-Pro as primary
#     without verifying its context cap. Second mistake: panicked, assumed
#     DeepSeek was 128K (V3 era, wrong) and swapped to Gemini Flash as
#     "the smart cheap option." Brian corrected both: DeepSeek V4-Pro is
#     1M context, AND Flash is too shallow for this multi-level-synthesis
#     task. Both mistakes caught before any sweep ran with either bad
#     config.
#   2026-05-05 (attempt 3, current): re-routed to deepseek/deepseek-v4-pro
#     AS PRIMARY with google/gemini-2.5-pro AS AUTOMATIC FALLBACK via
#     OpenRouter's `models` array. Verified corpus size (611K tokens) fits
#     comfortably under DeepSeek's 1M context cap with ~388K headroom.
#     Expected cost: ~$0.20/sweep on V4-Pro success path, ~$0.65/sweep on
#     fallback days. Savings: ~$0.45/sweep × ~10 sweeps/month = ~$4.50/month.
#     Provider-side throttling that motivated the 2026-04-25 switch has
#     since stabilized; if V4-Pro flakes again, OpenRouter's fallback
#     array means Gemini Pro auto-takes-over without code intervention.
#
# Always verify a model's context window against the current corpus size
# before swapping primaries. See CONTEXT_WINDOW_TOKENS below for the
# explicit guard table.
DEFAULT_MODEL = "deepseek/deepseek-v4-pro"
FALLBACK_MODELS = ["google/gemini-2.5-pro"]

# Context window per model (tokens). Used by the size-fit guard at startup
# so we never silently swap to a model that can't accept the corpus.
# Update when adding model options or when providers expand context windows.
CONTEXT_WINDOW_TOKENS = {
    "google/gemini-2.5-pro":      2_000_000,
    "google/gemini-2.5-flash":    2_000_000,
    "deepseek/deepseek-v4-pro":   1_000_000,
    "deepseek/deepseek-v4-flash":   200_000,
    "anthropic/claude-opus-4-7":  1_000_000,
    "openai/gpt-5":                 400_000,
}

# OpenRouter pricing per Mtok (input, output) — used for cost reporting.
# Update when adding model options.
PRICING_USD_PER_MTOK = {
    "google/gemini-2.5-pro":      (1.25, 5.00),
    "google/gemini-2.5-flash":    (0.30, 2.50),
    "deepseek/deepseek-v4-pro":   (0.435, 0.87),
    "deepseek/deepseek-v4-flash": (0.14, 0.28),
    "anthropic/claude-opus-4-7":  (15.00, 75.00),
    "openai/gpt-5":               (2.50, 10.00),
}


# Read-only research tools for Pass 2. Pass 2 is synthesis-only — it must
# never edit any file. The tool surface exists so the synthesizer can fetch
# detail from `wiki/etc/experiments/comp-NNN-*/` (per-comp wiki-archive +
# outputs/ JSON), `wiki/etc/bio-ai-tools.md`, and other files outside the
# pre-loaded corpus when synthesis genuinely needs the detail.
TOOLS = [
    {"type": "function", "function": {
        "name": "read_file",
        "description": (
            "Read a file in the repository. Path is repo-relative. Use to "
            "fetch detail behind a link in the loaded corpus when synthesis "
            "needs it (e.g., per-comp experiment outputs, methodology files, "
            "tool-stack caveats). Especially useful for "
            "`wiki/etc/experiments/comp-NNN-*/wiki-archive.md` and "
            "`wiki/etc/experiments/comp-NNN-*/outputs/*.json`."),
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string",
                     "description": "repo-relative path, e.g. wiki/etc/experiments/comp-029-combined-cp0-systems-model/wiki-archive.md"},
        }, "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "list_directory",
        "description": (
            "List files and subdirectories in a directory (repo-relative "
            "path). Use to explore experiment-output folders before "
            "reaching for a specific file."),
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string", "description": "repo-relative directory path"},
        }, "required": ["path"]}}},
]


def safe_path(rel):
    """Resolve a repo-relative path; reject escapes and null bytes."""
    if "\0" in rel:
        raise ValueError(f"path {rel!r} contains null byte")
    abs_path = os.path.realpath(os.path.join(REPO_ROOT, rel))
    if not abs_path.startswith(REPO_ROOT + os.sep) and abs_path != REPO_ROOT:
        raise ValueError(f"path {rel!r} escapes repo root")
    return abs_path


# Pre-move ↔ post-move path remapping for the experiments/ → wiki/etc/experiments/
# reorg. Tool callers should use the POST-MOVE path per the prompt brief.
# During the transition window where some comp folders still live at the
# pre-move path, fall through to that path automatically. When the move
# completes the fallback becomes dead code; safe to leave.
_PATH_FALLBACK_PREFIXES = [
    ("wiki/etc/experiments/", "experiments/"),
]


def _resolve_with_fallback(rel):
    """Yield (abs_path, was_fallback) candidates for a repo-relative path.

    Handles both `wiki/etc/experiments/comp-NNN-*/foo.md` (with subpath) and
    `wiki/etc/experiments` (directory itself) — the latter strips the
    trailing slash off the prefix when matching.
    """
    yield safe_path(rel), False
    for post, pre in _PATH_FALLBACK_PREFIXES:
        post_trimmed = post.rstrip("/")
        pre_trimmed = pre.rstrip("/")
        if rel.startswith(post):
            fallback_rel = pre + rel[len(post):]
        elif rel == post_trimmed:
            fallback_rel = pre_trimmed
        else:
            continue
        try:
            yield safe_path(fallback_rel), True
        except ValueError:
            pass


def tool_read_file(args):
    rel = args["path"]
    try:
        for candidate, was_fallback in _resolve_with_fallback(rel):
            if os.path.isfile(candidate):
                size = os.path.getsize(candidate)
                if was_fallback:
                    print(f"  [read_file] {rel} → fallback to pre-move path ({size} bytes)",
                          file=sys.stderr)
                else:
                    print(f"  [read_file] {rel} ({size} bytes)", file=sys.stderr)
                return open(candidate).read()
    except ValueError as e:
        print(f"  [read_file] {rel} → ERROR: {e}", file=sys.stderr)
        return f"ERROR: {e}"
    print(f"  [read_file] {rel} → ERROR: file not found", file=sys.stderr)
    return f"ERROR: file not found: {rel}"


def tool_list_directory(args):
    rel = args["path"]
    try:
        for candidate, was_fallback in _resolve_with_fallback(rel):
            if os.path.isdir(candidate):
                entries = sorted(os.listdir(candidate))
                rendered = []
                for e in entries:
                    full = os.path.join(candidate, e)
                    rendered.append(e + ("/" if os.path.isdir(full) else ""))
                if was_fallback:
                    print(f"  [list_directory] {rel} → fallback to pre-move path "
                          f"({len(rendered)} entries)", file=sys.stderr)
                else:
                    print(f"  [list_directory] {rel} ({len(rendered)} entries)",
                          file=sys.stderr)
                return "\n".join(rendered) if rendered else "(empty directory)"
    except ValueError as e:
        print(f"  [list_directory] {rel} → ERROR: {e}", file=sys.stderr)
        return f"ERROR: {e}"
    print(f"  [list_directory] {rel} → ERROR: directory not found", file=sys.stderr)
    return f"ERROR: directory not found: {rel}"


TOOL_HANDLERS = {
    "read_file":      tool_read_file,
    "list_directory": tool_list_directory,
}


# OpenRouter returns the served model with cosmetic suffixes that don't
# indicate a fallback:
#   - Provider-routing variant: ':nitro', ':floor', ':online' (after colon)
#   - Date-version: '-20260423' (8-digit YYYYMMDD at end of last path component)
# Both are routing-tier decisions on the SAME model, not the fallback array
# kicking in. Strip both before fallback detection and pricing lookup.
# Catch 31 (papers/cross-vendor-heterogeneity-guard/revisions.md) caught the
# original `served_model != args.model` test as 100% false-positive across
# five spot-checked sweeps because OpenRouter was returning the versioned slug.
_DATE_VERSION_SUFFIX_RE = re.compile(r"-\d{8}$")


def canonical_model_slug(slug: str) -> str:
    """Normalize an OpenRouter slug for fallback comparison + pricing lookup.

    Strips both alias variants OpenRouter appends to served-model strings:
    ':nitro' / ':floor' / ':online' provider-routing tags, and the
    '-YYYYMMDD' date-version suffix that triggered Catch 31's false-positive
    fallback flag.
    """
    base = slug.split(":", 1)[0]
    return _DATE_VERSION_SUFFIX_RE.sub("", base)


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


def call_openrouter_raw(api_key, body):
    """One OpenRouter chat-completions request with retries.

    Returns the parsed-JSON response dict on success, exits non-zero on
    hard failure. Mirrors the retry policy from the previous single-shot
    path (originally inlined): transient curl-level errors retry with
    10/30/60/120s backoff, and HTTP 200 with non-JSON or empty content
    also retries (the OpenRouter `models` fallback array only kicks in
    on a NEW request, not by re-trying the streamed-empty response in
    place — see the comment trail above MAX_TOOL_ITERATIONS).
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        json.dump(body, tf)
        body_path = tf.name

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

            # Branch (a): curl-level failure. Existing transient-string check.
            if result.returncode != 0:
                combined = (result.stdout or "") + "\n" + (result.stderr or "")
                transient = (
                    result.returncode == 22
                    or any(s in combined for s in (
                        "429", "rate-limit", "rate limit", "temporarily",
                        "502", "503", "504",
                        "Connection reset", "Connection refused",
                        "timed out", "timeout",
                    ))
                )
                if not transient or attempt == max_retries - 1:
                    print(f"curl failed (exit {result.returncode})", file=sys.stderr)
                    print(f"stderr: {result.stderr.strip()}", file=sys.stderr)
                    print(f"stdout: {result.stdout[:2000]}", file=sys.stderr)
                    sys.exit(1)
                backoff = [10, 30, 60, 120][attempt] if attempt < 4 else 120
                print(f"  [retry {attempt+1}/{max_retries-1}] transient curl error, sleeping {backoff}s ...",
                      file=sys.stderr, flush=True)
                time.sleep(backoff)
                continue

            # Branch (b): curl succeeded (returncode 0). Validate body.
            stdout = result.stdout or ""
            try:
                candidate = json.loads(stdout) if stdout.strip() else None
            except json.JSONDecodeError:
                candidate = None

            # For tool-use loops, "content" can legitimately be empty when
            # the response is a tool_calls turn. Validate the response shape
            # rather than the content string here.
            shape_ok = (
                candidate is not None
                and "choices" in candidate
                and candidate["choices"]
                and isinstance(candidate["choices"][0].get("message"), dict)
            )
            if shape_ok:
                msg = candidate["choices"][0]["message"]
                has_content = bool(msg.get("content"))
                has_tool_calls = bool(msg.get("tool_calls"))
                if has_content or has_tool_calls:
                    return candidate

            # Empty / malformed / no-content-and-no-tool-calls → retry.
            if attempt == max_retries - 1:
                if candidate is None:
                    print(f"Non-JSON / empty response after {max_retries} attempts: {stdout[:2000]}",
                          file=sys.stderr)
                elif "choices" not in candidate:
                    print(f"Unexpected response (no 'choices') after {max_retries} attempts: "
                          f"{json.dumps(candidate, indent=2)[:2000]}", file=sys.stderr)
                else:
                    fr = candidate["choices"][0].get("finish_reason", "?")
                    print(f"OpenRouter returned empty content+tool_calls after {max_retries} "
                          f"attempts (finish_reason={fr!r}). "
                          f"Full choice: {json.dumps(candidate['choices'][0], indent=2)[:1500]}",
                          file=sys.stderr)
                sys.exit(1)
            backoff = [10, 30, 60, 120][attempt] if attempt < 4 else 120
            reason = "non-JSON/empty body" if candidate is None else "empty content+tool_calls"
            print(f"  [retry {attempt+1}/{max_retries-1}] HTTP 200 with {reason}, sleeping {backoff}s ...",
                  file=sys.stderr, flush=True)
            time.sleep(backoff)
    finally:
        os.unlink(body_path)


def run_agentic_synthesis(api_key, model, initial_prompt, fallback_models,
                          max_iterations, max_tokens):
    """Drive Pass 2 as a bounded tool-use loop.

    Pass 2 emits a single synthesis log. The loop runs until the model
    returns content with no tool_calls (terminal); each intermediate turn
    can call read_file / list_directory to fetch detail from outside the
    pre-loaded corpus. On the last allowed iteration, tool_choice=none
    forces the model to produce its synthesis log.

    Returns (content, total_in_tokens, total_out_tokens, last_response).
    `last_response` is used by the caller for the served-model and
    canonical-slug logic that runs after this returns.

    Backwards-compatibility: if the model never calls a tool (common case
    when the inlined corpus is sufficient), this loop makes one API call
    and returns identical results to the previous single-shot path.
    """
    messages = [{"role": "user", "content": initial_prompt}]
    total_in = 0
    total_out = 0
    last_response = None
    tool_calls_made = 0

    for iteration in range(max_iterations + 1):
        # On the last allowed iteration force a final answer (no more tools).
        forcing_final = iteration == max_iterations

        body = {
            "model": model,
            "messages": messages,
            "tools": TOOLS,
            "max_tokens": max_tokens,
            "temperature": 0.7,
        }
        if fallback_models:
            body["models"] = fallback_models
        if forcing_final:
            body["tool_choice"] = "none"
            print(f"  [iter {iteration+1}/{max_iterations+1}] iteration cap reached; "
                  f"forcing final synthesis (no more tool calls)", file=sys.stderr)

        resp = call_openrouter_raw(api_key, body)
        last_response = resp
        choice = resp["choices"][0]
        msg = choice.get("message", {}) or {}
        usage = resp.get("usage", {}) or {}
        total_in += usage.get("prompt_tokens", 0)
        total_out += usage.get("completion_tokens", 0)

        tool_calls = msg.get("tool_calls") or []
        content = msg.get("content")

        # Terminal: content with no tool_calls = final synthesis log.
        if content and not tool_calls:
            return content, total_in, total_out, resp

        # Tool calls: execute each and append results, then continue.
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
                # Cap each tool result to keep the loop bounded.
                if len(result) > 30_000:
                    result = result[:30_000] + "\n... (truncated)"
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.get("id", ""),
                    "name": name or "",
                    "content": result,
                })
                tool_calls_made += 1
            print(f"  [iter {iteration+1}/{max_iterations+1}] {len(tool_calls)} tool call(s) processed "
                  f"({tool_calls_made} cumulative)", file=sys.stderr)
            continue

        # Pathological: no content, no tool calls. Bail.
        print(
            f"OpenRouter returned no content and no tool calls "
            f"(finish_reason={choice.get('finish_reason', '?')!r}). "
            f"Full message: {json.dumps(msg, indent=2)[:1500]}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Loop exhausted without returning — shouldn't happen (forcing_final
    # on the last iteration guarantees content). Defensive.
    print(f"Pass 2 tool loop exhausted {max_iterations} iterations without final content",
          file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True,
                        help="Full commit SHA (typically $GITHUB_SHA in CI)")
    parser.add_argument("--trigger-files", default="",
                        help="Comma-separated list of trigger files for the TRIGGER block")
    parser.add_argument("--propagated-files", default="",
                        help=("Comma- or newline-separated list of files Pass 1 modified "
                              "during propagation (excluding original triggers). Pass 2's "
                              "synthesizer should weight attention on these — they're where "
                              "new content lives after Pass 1's propagation pass."))
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

    # Normalize the propagated_files input — Pass 1 emits one path per line
    # via $GITHUB_OUTPUT heredoc; the workflow may pass it through as
    # newline-separated or comma-separated depending on how the env-var
    # interpolation works. Accept both.
    propagated_raw = (args.propagated_files or "").replace(",", "\n")
    propagated_list = [p.strip() for p in propagated_raw.splitlines() if p.strip()]
    propagated_str = ", ".join(propagated_list) if propagated_list else "(none — Pass 1 only edited trigger files in place)"

    trigger_block = (
        "\n\n---\n\n"
        f"TRIGGER: Sweep at {timestamp}, commit {args.commit_sha}.\n"
        f"  date_str: {date_str}\n"
        f"  sha_short: {sha_short}\n"
        f"  diff_base: {args.diff_base or 'unknown'}\n"
        f"  trigger files (changed since last sweep): {args.trigger_files or '(none specified)'}\n"
        f"  propagated files (Pass 1 wrote new content here): {propagated_str}\n"
        f"  output_path: {output_path}\n"
        f"  reviewer_model: {args.model}\n"
        f"commit=yes\n"
        f"ci=github-actions-sweep-2-synthesize\n"
        f"\n"
        f"NOTE: trigger_files are the *cause* of this sweep (recent edits).\n"
        f"propagated_files are where new content now lives after Pass 1's\n"
        f"propagation. New cross-document connections are most likely to\n"
        f"emerge from the union of the two sets — weight your attention\n"
        f"there.\n"
        f"\n"
        f"OUTPUT REQUIREMENT: at the end of your synthesis log, include a\n"
        f"manifest of every wiki/*.md file you cited in any finding,\n"
        f"contradiction, experiment, or open question. Format:\n"
        f"\n"
        f"    Sources cited:\n"
        f"    - wiki/<path>.md\n"
        f"    - wiki/<path>.md\n"
        f"    ...\n"
        f"\n"
        f"Pass 3 (the reviewer) is non-agentic and inlines these files\n"
        f"into its prompt — without the manifest, Pass 3 cannot verify\n"
        f"your claims.\n"
    )

    full_prompt = prompt_template + trigger_block + "\n\n=== CORPUS ===\n" + corpus
    prompt_chars = len(full_prompt)
    prompt_token_estimate = prompt_chars // 4
    print(f"Corpus: {len(included_paths)} files, ~{prompt_token_estimate:,} tokens (est.)",
          file=sys.stderr)

    # Size-fit guard: refuse to send a prompt that overflows the model's
    # context window. Hard fail rather than silently truncate or 400 from
    # the provider. Check against the PRIMARY model; OpenRouter's `models`
    # fallback array means a smaller-context primary failure can fall back
    # to a larger-context model, so the warning threshold uses the SMALLEST
    # context window across [primary] + fallbacks.
    candidate_models = [args.model] + (FALLBACK_MODELS if args.model == DEFAULT_MODEL else [])
    candidate_caps = [CONTEXT_WINDOW_TOKENS.get(m, 200_000) for m in candidate_models]
    primary_cap = candidate_caps[0]
    largest_cap = max(candidate_caps)
    # 90% of primary cap = warn (fallback path may still work)
    # 90% of largest cap = hard refuse (no model can accept this)
    if prompt_token_estimate > int(0.90 * largest_cap):
        print(f"FATAL: estimate {prompt_token_estimate:,} tokens exceeds 90% of the largest available context "
              f"({largest_cap:,} tokens across models {candidate_models}). Trim corpus via EXCLUDE or split sweep.",
              file=sys.stderr)
        sys.exit(2)
    if prompt_token_estimate > int(0.90 * primary_cap):
        print(f"WARNING: estimate {prompt_token_estimate:,} tokens approaches primary {args.model}'s {primary_cap:,} cap. "
              f"Likely fallback to {FALLBACK_MODELS[0] if FALLBACK_MODELS else '(no fallback)'}.",
              file=sys.stderr)

    # Build request body. OpenRouter's `models` array provides automatic
    # provider-side fallback: if the primary model fails (429 throttle, null
    # content, upstream provider down), OpenRouter tries the next model in
    # the array without code intervention. The python-side retry loop in
    # call_openrouter_raw still handles transient curl-level errors. When
    # --model is overridden via CLI, no fallback is used (caller is
    # explicit about which model to test).
    fallback_array = (
        [args.model] + FALLBACK_MODELS if args.model == DEFAULT_MODEL else None
    )

    # Tool-use loop: Pass 2 is single-shot synthesis with optional detail
    # fetch via read_file / list_directory. The model may call zero, one,
    # or many tools before emitting its synthesis log. The loop terminates
    # when the model returns content with no tool_calls. On the last
    # allowed iteration, tool_choice=none forces a content response.
    #
    # Behavior preservation note: a run where the model never calls a tool
    # is functionally equivalent to the previous single-shot path — same
    # request body, same response handling, same downstream emission. The
    # tools surface is purely additive.
    content, in_tok, out_tok, resp_meta = run_agentic_synthesis(
        api_key=api_key,
        model=args.model,
        initial_prompt=full_prompt,
        fallback_models=fallback_array,
        max_iterations=MAX_TOOL_ITERATIONS,
        max_tokens=args.max_tokens,
    )

    # served_model_raw originates from the LAST response in the loop. The
    # fallback-detection / pricing / frontmatter logic that follows is
    # unchanged from the single-shot path.
    served_model_raw = resp_meta.get("model", args.model)
    served_model = canonical_model_slug(served_model_raw)
    args_model_canonical = canonical_model_slug(args.model)
    fallback_used = served_model != args_model_canonical

    in_per, out_per = PRICING_USD_PER_MTOK.get(served_model, (None, None))
    if in_per is None:
        cost_in = cost_out = cost_total = 0.0
    else:
        cost_in = in_tok * in_per / 1_000_000
        cost_out = out_tok * out_per / 1_000_000
        cost_total = cost_in + cost_out

    fallback_note = f" (FALLBACK from {args.model})" if fallback_used else ""
    alias_note = f" (alias: {served_model_raw})" if served_model_raw != served_model else ""
    print(f"Tokens: in={in_tok:,} out={out_tok:,}  cost=${cost_total:.4f}  model={served_model}{alias_note}{fallback_note}",
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
        f"reviewer_model: {served_model}\n"
        f"reviewer_model_served_raw: {served_model_raw}\n"
        f"reviewer_model_requested: {args.model}\n"
        f"reviewer_fallback_used: {fallback_used}\n"
        f"input_tokens: {in_tok}\n"
        f"output_tokens: {out_tok}\n"
        f"cost_usd: {cost_total:.4f}\n"
        f"corpus_files: {len(included_paths)}\n"
        f"---\n\n"
    )

    with open(output_path, "w") as f:
        f.write(header + content + "\n")

    # Extract cited_files for Pass 3. Two strategies, in order:
    #
    # 1. Look for an explicit `Sources cited:` block at the end of the
    #    synthesis (the prompt asks the model to emit one). Parse the
    #    bullet list under that heading.
    # 2. Fallback: regex-scan the entire synthesis for `wiki/<name>.md`
    #    mentions and dedupe. Catches everything cited even if the model
    #    forgot the manifest.
    #
    # Pass 3 is non-agentic — its driver inlines the full text of every
    # path in cited_files into the reviewer's prompt. Without this list,
    # Pass 3 has no way to verify claims about non-trigger files (this
    # is the "I can't confirm because I don't have the trigger file"
    # failure mode Brian observed in the 2026-04-27 / 2026-04-28 cycle).
    import re as _re
    cited_set = set()

    # Strategy 1: explicit manifest
    manifest_match = _re.search(
        r"^[#\s]*Sources cited:\s*$(.*?)(?=^#|\Z)",
        content, _re.MULTILINE | _re.DOTALL,
    )
    if manifest_match:
        for m in _re.finditer(r"wiki/[A-Za-z0-9_\-./]+\.md", manifest_match.group(1)):
            cited_set.add(m.group(0))

    # Strategy 2: scan everything as a fallback (always run, in case the
    # manifest missed any). De-duplicates against the explicit list.
    for m in _re.finditer(r"wiki/[A-Za-z0-9_\-./]+\.md", content):
        path = m.group(0)
        cited_set.add(path)

    cited_files = sorted(cited_set)
    print(f"Pass 2 cited {len(cited_files)} wiki files (will be inlined for Pass 3):",
          file=sys.stderr)
    for p in cited_files:
        print(f"  {p}", file=sys.stderr)

    gha_output = os.environ.get("GITHUB_OUTPUT")
    if gha_output:
        with open(gha_output, "a") as f:
            f.write("cited_files<<CITED_EOF\n")
            f.write("\n".join(cited_files))
            f.write("\nCITED_EOF\n")

    # Pass-3 reviewer reads stdout to find the path
    print(output_path)


if __name__ == "__main__":
    main()
