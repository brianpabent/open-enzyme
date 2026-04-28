#!/usr/bin/env python3
"""
sweep-1-propagate.py — Pass 1 propagation driver via OpenRouter.

Replaces `claude --dangerously-skip-permissions -p ...` for Pass 1. Routes
through OpenRouter (default: anthropic/claude-sonnet-4-6) so we are not
bound by the Anthropic-direct 30K ITPM org limit, which kills Pass 1 on
medium-sized propagation jobs.

The agentic loop is the same shape as scripts/eval-propagation.py: model
gets read_file / edit_file / write_file / list_files / grep / done over
OpenRouter's OpenAI-compatible API, runs until done() or iter cap, then
this script stages, commits, and pushes whatever changed.

Read-only paths are enforced as a safety net regardless of what the prompt
says, so a confused model can't trash CLAUDE.md or scripts/.

Usage in CI:
    python3 scripts/sweep-1-propagate.py \\
        --commit-sha "$GITHUB_SHA" \\
        --trigger-files "wiki/foo.md\\nwiki/bar.md" \\
        --diff-base "<last-sweep-sha>"

Local manual run (operates on current checkout):
    OPENROUTER_API_KEY=... python3 scripts/sweep-1-propagate.py \\
        --commit-sha HEAD \\
        --trigger-files "wiki/koji-home-fermentation.md"
"""

import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

DEFAULT_MODEL = "anthropic/claude-sonnet-4-6"
DEFAULT_PROMPT = "scripts/sweep-prompt-1-propagate.md"

# Paths the model is forbidden to write to. Mirrors sweep-prompt-1-propagate.md
# but enforced here so a misbehaving model can't cause damage.
READ_ONLY_GLOBS = [
    "wiki/synthesis.md",
    "reference/**",
    "*.html",
    "CLAUDE.md",
    "README.md",
    "scripts/**",
    ".claude/**",
    ".obsidian/**",
    ".git/**",
]

# OpenRouter pricing per Mtok (input, output) — for cost reporting.
PRICING_USD_PER_MTOK = {
    "anthropic/claude-sonnet-4-6":  (3.00, 15.00),
    "anthropic/claude-haiku-4-5":   (0.80, 4.00),
    "anthropic/claude-opus-4-7":    (15.00, 75.00),
    "deepseek/deepseek-v4-pro":     (0.435, 0.87),
}

TOOLS = [
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read a file. Returns full contents.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}}, "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "edit_file",
        "description": (
            "Apply a unique-string replacement to an existing file. Errors "
            "if old_string is missing or matches more than once. Use for "
            "surgical edits — preserve everything else."),
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"},
            "old_string": {"type": "string"},
            "new_string": {"type": "string"}},
            "required": ["path", "old_string", "new_string"]}}},
    {"type": "function", "function": {
        "name": "write_file",
        "description": (
            "Create a new file or overwrite an existing one. Use only when "
            "creating new pages — prefer edit_file otherwise."),
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"},
            "content": {"type": "string"}},
            "required": ["path", "content"]}}},
    {"type": "function", "function": {
        "name": "list_files",
        "description": "List files matching a glob (e.g. 'wiki/*.md').",
        "parameters": {"type": "object", "properties": {
            "pattern": {"type": "string"}}, "required": ["pattern"]}}},
    {"type": "function", "function": {
        "name": "grep",
        "description": (
            "Search a regex across files. Returns paths and line numbers. "
            "Use to find cross-references that need propagation."),
        "parameters": {"type": "object", "properties": {
            "pattern": {"type": "string"},
            "glob": {"type": "string"}},
            "required": ["pattern"]}}},
    {"type": "function", "function": {
        "name": "done",
        "description": "Signal propagation complete. Call when all needed edits are done.",
        "parameters": {"type": "object", "properties": {
            "summary": {"type": "string"}}, "required": ["summary"]}}},
]


def is_read_only(rel_path):
    """True if rel_path matches any read-only glob."""
    from fnmatch import fnmatch
    norm = rel_path.replace(os.sep, "/")
    for pat in READ_ONLY_GLOBS:
        # fnmatch doesn't support '**' across separators; expand by splitting
        if pat.endswith("/**"):
            prefix = pat[:-3]
            if norm == prefix or norm.startswith(prefix + "/"):
                return True
        elif fnmatch(norm, pat):
            return True
    return False


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


def tool_edit_file(args):
    if is_read_only(args["path"]):
        return f"ERROR: {args['path']} is read-only in Pass 1"
    try:
        p = safe_path(args["path"])
    except ValueError as e:
        return f"ERROR: {e}"
    if not os.path.exists(p):
        return f"ERROR: file not found: {args['path']}"
    text = open(p).read()
    count = text.count(args["old_string"])
    if count == 0:
        return f"ERROR: old_string not found in {args['path']}"
    if count > 1:
        return f"ERROR: old_string matches {count} times in {args['path']} — make it more specific"
    new_text = text.replace(args["old_string"], args["new_string"])
    with open(p, "w") as f:
        f.write(new_text)
    return f"OK: edited {args['path']} (1 replacement)"


def tool_write_file(args):
    if is_read_only(args["path"]):
        return f"ERROR: {args['path']} is read-only in Pass 1"
    try:
        p = safe_path(args["path"])
    except ValueError as e:
        return f"ERROR: {e}"
    is_new = not os.path.exists(p)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(args["content"])
    return f"OK: wrote {args['path']} ({'new file' if is_new else 'overwritten'})"


def tool_list_files(args):
    matches = glob.glob(os.path.join(REPO_ROOT, args["pattern"]), recursive=True)
    rels = sorted([os.path.relpath(m, REPO_ROOT) for m in matches])
    return "\n".join(rels) if rels else "(no matches)"


def tool_grep(args):
    cmd = ["grep", "-rn", args["pattern"]]
    if args.get("glob"):
        cmd += ["--include=" + args["glob"]]
    cmd.append(REPO_ROOT)
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout.replace(REPO_ROOT + "/", "")
    if not out.strip():
        return "(no matches)"
    if len(out) > 8000:
        out = out[:8000] + f"\n... [truncated, {len(out) - 8000} chars omitted]"
    return out


TOOL_IMPLS = {
    "read_file": tool_read_file,
    "edit_file": tool_edit_file,
    "write_file": tool_write_file,
    "list_files": tool_list_files,
    "grep": tool_grep,
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


def call_openrouter(api_key, model, messages, max_tokens=4000, max_retries=4):
    body = {
        "model": model,
        "messages": messages,
        "tools": TOOLS,
        "max_tokens": max_tokens,
        "temperature": 0.3,
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
                 "-H", "X-Title: Open Enzyme sweep Pass 1",
                 "-d", f"@{body_path}",
                 "--max-time", "300"],
                capture_output=True, text=True, timeout=320,
            )
            if r.returncode == 0:
                try:
                    return json.loads(r.stdout)
                except json.JSONDecodeError:
                    sys.exit(f"Non-JSON OpenRouter response: {r.stdout[:1500]}")
            # Transient detection: check BOTH stdout and stderr. Curl with
            # --fail-with-body returns exit 22 on HTTP errors and writes the
            # status code to stderr (e.g. "curl: (22) The requested URL
            # returned error: 503"); the response body in stdout may be HTML
            # or empty. Run 25049501442 (2026-04-28) failed because the prior
            # check only looked at stdout. Also treat curl exit 22 (HTTP
            # error) as transient by default — most non-transient HTTP
            # errors here are 4xx auth/quota issues that don't recover with
            # retry, but the cost of retrying once is low.
            combined = (r.stdout or "") + "\n" + (r.stderr or "")
            transient = (
                r.returncode == 22  # HTTP error per --fail-with-body
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
            backoff = 2 ** attempt * 5
            print(f"  [retry {attempt+1}/{max_retries-1}] transient error, sleeping {backoff}s ...", file=sys.stderr, flush=True)
            time.sleep(backoff)
    finally:
        os.unlink(body_path)


def run_agentic_loop(api_key, model, system_prompt, user_prompt, max_iterations=40):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    total_in = total_out = 0
    iteration = 0
    done_summary = None
    last_text = None

    while iteration < max_iterations:
        iteration += 1
        t0 = datetime.datetime.now()
        print(f"  [iter {iteration}] calling {model} ...", file=sys.stderr, flush=True)
        resp = call_openrouter(api_key, model, messages)
        dt = (datetime.datetime.now() - t0).total_seconds()
        msg = resp["choices"][0]["message"]
        usage = resp.get("usage", {})
        in_tok = usage.get("prompt_tokens", 0)
        out_tok = usage.get("completion_tokens", 0)
        total_in += in_tok
        total_out += out_tok

        assistant_turn = {"role": "assistant", "content": msg.get("content")}
        if msg.get("tool_calls"):
            assistant_turn["tool_calls"] = msg["tool_calls"]
        messages.append(assistant_turn)
        if msg.get("content"):
            last_text = msg["content"]

        tool_calls = msg.get("tool_calls") or []
        tc_summary = ",".join(tc["function"]["name"] for tc in tool_calls) or "(no tools)"
        print(f"  [iter {iteration}] {dt:.1f}s in={in_tok} out={out_tok} tools={tc_summary}", file=sys.stderr, flush=True)
        if not tool_calls:
            break

        for tc in tool_calls:
            fn = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"] or "{}")
            except json.JSONDecodeError as e:
                messages.append({"role": "tool", "tool_call_id": tc["id"],
                                 "content": f"ERROR: invalid JSON arguments: {e}"})
                continue
            if fn == "done":
                done_summary = args.get("summary", "")
                messages.append({"role": "tool", "tool_call_id": tc["id"], "content": "OK"})
            elif fn in TOOL_IMPLS:
                try:
                    result = TOOL_IMPLS[fn](args)
                except Exception as e:
                    result = f"ERROR: {type(e).__name__}: {e}"
                messages.append({"role": "tool", "tool_call_id": tc["id"], "content": result})
            else:
                messages.append({"role": "tool", "tool_call_id": tc["id"],
                                 "content": f"ERROR: unknown tool {fn}"})
        if done_summary is not None:
            break

    return {
        "iterations": iteration,
        "input_tokens": total_in,
        "output_tokens": total_out,
        "done_summary": done_summary,
        "completed": done_summary is not None,
        "last_text": last_text,
        "hit_iter_cap": iteration >= max_iterations and done_summary is None,
    }


def stage_and_commit(trigger_files, diff_base, model, summary, dry_run):
    """Stage non-readonly changes, build a commit message, commit.

    Returns:
        (committed: bool, changed_paths: list[str])
        — `changed_paths` is every path Pass 1 modified or created, regardless
        of whether the commit went through. Pass 2 needs this list to know
        which downstream files Pass 1 propagated to (i.e. the files where new
        connections may now live, distinct from the original trigger files).
    """
    # Get all changed paths (modified, added, untracked)
    r1 = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
    changed = []
    for line in r1.stdout.splitlines():
        if not line.strip():
            continue
        # porcelain v1: "XY path" or "XY orig -> path"
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if is_read_only(path):
            print(f"  refusing to stage read-only path: {path}", file=sys.stderr)
            continue
        changed.append(path)

    if not changed:
        print("Pass 1 produced no changes — no commit", file=sys.stderr)
        return False, []

    print(f"Staging {len(changed)} paths:", file=sys.stderr)
    for p in changed:
        print(f"  {p}", file=sys.stderr)

    if dry_run:
        print("(dry-run: skipping git add/commit)", file=sys.stderr)
        return False, changed

    subprocess.run(["git", "add", "--"] + changed, check=True)

    # Build commit message
    basenames = ", ".join(os.path.basename(t).replace(".md", "") for t in trigger_files[:3])
    if len(trigger_files) > 3:
        basenames += f", +{len(trigger_files) - 3} more"
    n = len(changed)
    title = f"sweep-1-propagate: {basenames} → {n} files updated [skip-wiki-sweep]"

    body_lines = [
        title, "",
        f"Pass 1 propagation via {model} (OpenRouter).",
        "",
        f"Trigger files (since {diff_base or 'unknown'}):",
    ]
    for t in trigger_files:
        body_lines.append(f"  - {t}")
    body_lines += ["", "Model summary:", "", summary or "(no done() summary — hit iteration cap)"]
    msg = "\n".join(body_lines)

    subprocess.run(["git", "commit", "-m", msg], check=True)
    return True, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--commit-sha", required=True,
                        help="Trigger commit SHA (typically $GITHUB_SHA in CI)")
    parser.add_argument("--trigger-files", required=True,
                        help="Newline- or comma-separated trigger file paths")
    parser.add_argument("--diff-base", default="",
                        help="SHA of last sweep commit (for the prompt header)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"OpenRouter model slug (default: {DEFAULT_MODEL})")
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--max-iterations", type=int, default=40)
    parser.add_argument("--dry-run", action="store_true",
                        help="Run the agentic loop and report changes, but skip git commit")
    args = parser.parse_args()

    api_key = read_api_key()

    # Normalize trigger files (accept both newline and comma separated)
    raw = args.trigger_files.replace(",", "\n")
    trigger_files = [p.strip() for p in raw.splitlines() if p.strip()]
    if not trigger_files:
        sys.exit("No trigger files provided")

    print(f"Model:         {args.model}", file=sys.stderr)
    print(f"Commit SHA:    {args.commit_sha}", file=sys.stderr)
    print(f"Diff base:     {args.diff_base or '(none)'}", file=sys.stderr)
    print(f"Trigger files: {trigger_files}", file=sys.stderr)

    sweep_brief = open(args.prompt_file).read()
    system_prompt = (
        sweep_brief
        + "\n\n---\n\n"
        + "You are running inside the Open Enzyme sweep CI. Tools available: "
          "read_file, edit_file, write_file, list_files, grep, done. "
          "There is no git or shell — the harness will stage and commit your "
          "changes after you call done(). Do NOT attempt git operations.\n\n"
          "Read-only paths (the harness will reject writes to these): "
          "wiki/synthesis.md, reference/, *.html, CLAUDE.md, README.md, "
          "scripts/, .claude/, .obsidian/, .git/.\n\n"
          "Pass 1 scope: propagate the trigger findings to affected wiki "
          "pages with surgical edits. Do NOT synthesize, do NOT propose "
          "experiments, do NOT touch wiki/synthesis.md (that is Pass 2's "
          "job). When all needed edits are done, call done() with a "
          "one-paragraph summary."
    )

    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    trigger_list = "\n".join(f"  - {f}" for f in trigger_files)
    user_prompt = (
        f"TRIGGER: Files changed since last sweep ({args.diff_base or 'unknown'}) at {timestamp}:\n"
        f"{trigger_list}\n\n"
        f"commit_sha: {args.commit_sha}\n"
        f"ci=github-actions-sweep-1-propagate\n\n"
        f"Run Pass 1 propagation now. Read the trigger files first, then "
        f"identify and update affected wiki pages. Call done() when finished."
    )

    loop = run_agentic_loop(
        api_key, args.model, system_prompt, user_prompt,
        max_iterations=args.max_iterations,
    )

    in_per, out_per = PRICING_USD_PER_MTOK.get(args.model, (None, None))
    if in_per is not None:
        cost = (loop["input_tokens"] * in_per + loop["output_tokens"] * out_per) / 1_000_000
        cost_str = f"${cost:.4f}"
    else:
        cost_str = "(unknown)"

    print(
        f"\nLoop finished: iters={loop['iterations']} completed={loop['completed']} "
        f"hit_iter_cap={loop['hit_iter_cap']}",
        file=sys.stderr,
    )
    print(f"Tokens: in={loop['input_tokens']:,} out={loop['output_tokens']:,} cost={cost_str}",
          file=sys.stderr)

    summary = loop["done_summary"] or loop["last_text"] or ""
    committed, changed_paths = stage_and_commit(
        trigger_files, args.diff_base, args.model, summary, args.dry_run,
    )
    if committed:
        print("Pass 1 commit created", file=sys.stderr)
    else:
        print("Pass 1 made no commit", file=sys.stderr)

    # Write the propagated_files list to GITHUB_OUTPUT so Pass 2 can
    # reference it. propagated_files = files Pass 1 modified that weren't
    # already in the trigger set. Pass 2's synthesizer needs to weight
    # attention on these because that's where new connections live after
    # propagation. Trigger files are the *cause* of the sweep; propagated
    # files are where the *new content* now lives.
    trigger_set = {os.path.normpath(t) for t in trigger_files}
    propagated_files = sorted({
        os.path.normpath(p) for p in changed_paths
        if p.startswith("wiki/") and p.endswith(".md")
        and os.path.normpath(p) not in trigger_set
        and os.path.normpath(p) != "wiki/synthesis.md"
    })

    print(f"\nPropagated to {len(propagated_files)} files (excluding trigger set):", file=sys.stderr)
    for p in propagated_files:
        print(f"  {p}", file=sys.stderr)

    gha_output = os.environ.get("GITHUB_OUTPUT")
    if gha_output:
        with open(gha_output, "a") as f:
            f.write("propagated_files<<PROPAGATED_EOF\n")
            f.write("\n".join(propagated_files))
            f.write("\nPROPAGATED_EOF\n")


if __name__ == "__main__":
    main()
