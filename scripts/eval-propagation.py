#!/usr/bin/env python3
"""
eval-propagation.py — Pass 1 propagation eval harness.

Runs a candidate model against a fixed propagation scenario and scores it
against a known-good golden diff. Lets us pick a Pass 1 model empirically
instead of by reputation.

Architecture:
- A scenario pins a `before_sha` (state where a trigger file has landed but
  propagation hasn't run yet) plus the `expected_targets` (files that the
  actual production sweep updated). This is the apples-to-apples test.
- The harness creates a git worktree at `before_sha`, exposes a small tool
  set (read_file / edit_file / write_file / list_files / grep / done) over
  OpenRouter's OpenAI-compatible API, and lets the model run an agentic
  loop until it calls `done` (or hits max_iterations).
- After the loop, we diff the worktree vs `before_sha` and compute recall /
  precision against `expected_targets`. Diff lines and edit-minimality come
  for free. Style discipline (evidence tags, frontmatter, no marketing) is
  recorded but eyeball-graded for v0.

Why a custom harness vs. Aider/Codex CLI: deterministic, no external
dependency, identical contract for every model so the only variable is the
model. Aider can be benchmarked separately later.

Usage:
    python3 scripts/eval-propagation.py \\
        --scenario evals/scenarios/01-chembl-ic50-cross-check.md \\
        --model deepseek/deepseek-v4-pro

To matrix-run across models, wrap this in shell. v1 will add a driver.
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

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

# OpenRouter pricing per Mtok (input, output). Update when adding models.
PRICING_USD_PER_MTOK = {
    "deepseek/deepseek-v4-pro":     (0.435, 0.87),
    "deepseek/deepseek-v4-flash":   (0.14, 0.28),
    "anthropic/claude-sonnet-4-6":  (3.00, 15.00),
    "anthropic/claude-haiku-4-5":   (0.80, 4.00),
    "anthropic/claude-opus-4-7":    (15.00, 75.00),
    "google/gemini-2.5-pro":        (1.25, 5.00),
    "google/gemini-2.5-flash":      (0.30, 2.50),
    "openai/gpt-5":                 (2.50, 10.00),
    "openai/gpt-5-mini":            (0.50, 2.00),
    "meta-llama/llama-4-maverick":  (0.27, 0.85),
    "qwen/qwen3-coder":             (0.30, 1.20),
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the worktree. Returns full file contents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Path relative to worktree root"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Apply a string replacement to an existing file. "
                "Errors if old_string is not found or matches more than once. "
                "Use this for surgical edits — preserve everything else."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_string": {"type": "string"},
                    "new_string": {"type": "string"},
                },
                "required": ["path", "old_string", "new_string"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": (
                "Create a new file or overwrite an existing one. "
                "Use only when creating new pages — prefer edit_file for existing files."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files matching a glob pattern (e.g. 'wiki/*.md'). Relative to worktree root.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string"},
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grep",
            "description": (
                "Search for a regex pattern across files. Returns matching paths and line numbers. "
                "Useful for finding cross-references that need propagation."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string"},
                    "glob": {"type": "string", "description": "Optional file glob to scope search (e.g. 'wiki/*.md')"},
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "done",
            "description": "Signal that propagation is complete. Call this when all needed edits are done.",
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "One-paragraph summary of what changed and why"},
                },
                "required": ["summary"],
            },
        },
    },
]


def parse_scenario(path):
    text = open(path).read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
    if not m:
        sys.exit(f"Scenario {path} missing YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    fm["_body"] = m.group(2).strip()
    for list_field in ("trigger_files", "expected_targets"):
        if list_field in fm:
            fm[list_field] = [p.strip() for p in fm[list_field].split(",") if p.strip()]
    return fm


def make_worktree(before_sha):
    wt_path = tempfile.mkdtemp(prefix="eval-prop-")
    subprocess.run(
        ["git", "worktree", "add", "--detach", wt_path, before_sha],
        check=True, capture_output=True,
    )
    return wt_path


def remove_worktree(wt_path):
    subprocess.run(["git", "worktree", "remove", "--force", wt_path], capture_output=True)


def safe_path(wt, rel):
    """Block path traversal — keep edits inside the worktree."""
    abs_path = os.path.realpath(os.path.join(wt, rel))
    wt_real = os.path.realpath(wt)
    if not abs_path.startswith(wt_real + os.sep) and abs_path != wt_real:
        raise ValueError(f"path {rel!r} escapes worktree")
    return abs_path


def tool_read_file(wt, args):
    try:
        p = safe_path(wt, args["path"])
    except ValueError as e:
        return f"ERROR: {e}"
    if not os.path.exists(p):
        return f"ERROR: file not found: {args['path']}"
    return open(p).read()


def tool_edit_file(wt, args):
    try:
        p = safe_path(wt, args["path"])
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


def tool_write_file(wt, args):
    try:
        p = safe_path(wt, args["path"])
    except ValueError as e:
        return f"ERROR: {e}"
    is_new = not os.path.exists(p)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(args["content"])
    return f"OK: wrote {args['path']} ({'new file' if is_new else 'overwritten'})"


def tool_list_files(wt, args):
    matches = glob.glob(os.path.join(wt, args["pattern"]), recursive=True)
    rels = sorted([os.path.relpath(m, wt) for m in matches])
    return "\n".join(rels) if rels else "(no matches)"


def tool_grep(wt, args):
    cmd = ["grep", "-rn", args["pattern"]]
    if args.get("glob"):
        cmd += ["--include=" + args["glob"]]
    cmd.append(wt)
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    if not out.strip():
        return "(no matches)"
    out = out.replace(wt + "/", "")
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
                [
                    "curl", "-sS", "--fail-with-body",
                    "https://openrouter.ai/api/v1/chat/completions",
                    "-H", f"Authorization: Bearer {api_key}",
                    "-H", "Content-Type: application/json",
                    "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                    "-H", "X-Title: Open Enzyme propagation eval",
                    "-d", f"@{body_path}",
                    "--max-time", "300",
                ],
                capture_output=True, text=True, timeout=320,
            )
            if r.returncode == 0:
                try:
                    return json.loads(r.stdout)
                except json.JSONDecodeError:
                    sys.exit(f"Non-JSON OpenRouter response: {r.stdout[:1500]}")
            transient = ("429" in r.stdout) or ("rate-limit" in r.stdout) or ("temporarily" in r.stdout) or ("502" in r.stdout) or ("503" in r.stdout)
            if not transient or attempt == max_retries - 1:
                print(f"OpenRouter call failed (exit {r.returncode}): {r.stderr.strip()}", file=sys.stderr)
                print(f"stdout: {r.stdout[:1500]}", file=sys.stderr)
                sys.exit(1)
            backoff = 2 ** attempt * 5  # 5s, 10s, 20s
            print(f"  [retry {attempt+1}/{max_retries-1}] transient error, sleeping {backoff}s ...", file=sys.stderr, flush=True)
            import time
            time.sleep(backoff)
    finally:
        os.unlink(body_path)


def run_agentic_loop(wt, api_key, model, system_prompt, user_prompt, max_iterations=30):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    total_in = total_out = 0
    iteration = 0
    done_summary = None
    last_text = None
    error = None

    while iteration < max_iterations:
        iteration += 1
        t0 = datetime.datetime.now()
        print(f"  [iter {iteration}] calling {model} ...", file=sys.stderr, flush=True)
        resp = call_openrouter(api_key, model, messages)
        dt = (datetime.datetime.now() - t0).total_seconds()
        if "choices" not in resp:
            error = f"bad response: {json.dumps(resp)[:500]}"
            print(f"  [iter {iteration}] ERROR: {error}", file=sys.stderr, flush=True)
            break
        msg = resp["choices"][0]["message"]
        usage = resp.get("usage", {})
        in_tok = usage.get("prompt_tokens", 0)
        out_tok = usage.get("completion_tokens", 0)
        total_in += in_tok
        total_out += out_tok
        # Persist assistant turn (incl. any tool_calls)
        assistant_turn = {"role": "assistant", "content": msg.get("content")}
        if msg.get("tool_calls"):
            assistant_turn["tool_calls"] = msg["tool_calls"]
        messages.append(assistant_turn)

        if msg.get("content"):
            last_text = msg["content"]

        tool_calls = msg.get("tool_calls") or []
        tc_summary = ",".join(tc["function"]["name"] for tc in tool_calls) or "(no tools)"
        print(
            f"  [iter {iteration}] {dt:.1f}s in={in_tok} out={out_tok} tools={tc_summary}",
            file=sys.stderr, flush=True,
        )
        if not tool_calls:
            break

        for tc in tool_calls:
            fn = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"] or "{}")
            except json.JSONDecodeError as e:
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": f"ERROR: invalid JSON arguments: {e}",
                })
                continue
            if fn == "done":
                done_summary = args.get("summary", "")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": "OK",
                })
            elif fn in TOOL_IMPLS:
                try:
                    result = TOOL_IMPLS[fn](wt, args)
                except Exception as e:
                    result = f"ERROR: {type(e).__name__}: {e}"
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": result,
                })
            else:
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": f"ERROR: unknown tool {fn}",
                })
        if done_summary is not None:
            break

    return {
        "iterations": iteration,
        "input_tokens": total_in,
        "output_tokens": total_out,
        "done_summary": done_summary,
        "completed": done_summary is not None,
        "last_text": last_text,
        "error": error,
        "hit_iter_cap": iteration >= max_iterations and done_summary is None,
    }


def compute_metrics(wt, scenario):
    before = scenario["before_sha"]
    expected = set(scenario.get("expected_targets", []))

    r = subprocess.run(
        ["git", "-C", wt, "diff", "--name-only", before],
        capture_output=True, text=True,
    )
    actual = set(p.strip() for p in r.stdout.splitlines() if p.strip())

    r2 = subprocess.run(
        ["git", "-C", wt, "ls-files", "--others", "--exclude-standard"],
        capture_output=True, text=True,
    )
    actual.update(p.strip() for p in r2.stdout.splitlines() if p.strip())

    recall = (len(expected & actual) / len(expected)) if expected else None
    precision = (len(expected & actual) / len(actual)) if actual else None

    diff_proc = subprocess.run(
        ["git", "-C", wt, "diff", before],
        capture_output=True, text=True,
    )
    diff_text = diff_proc.stdout

    new_files = {}
    for f in actual:
        check = subprocess.run(
            ["git", "-C", wt, "ls-tree", before, f],
            capture_output=True, text=True,
        )
        if not check.stdout.strip():
            full = os.path.join(wt, f)
            if os.path.exists(full):
                new_files[f] = open(full).read()

    return {
        "files_changed": sorted(actual),
        "expected_targets": sorted(expected),
        "missed": sorted(expected - actual),
        "spurious": sorted(actual - expected),
        "recall": recall,
        "precision": precision,
        "diff_lines": len(diff_text.splitlines()),
        "diff": diff_text,
        "new_files": new_files,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--max-iterations", type=int, default=30)
    parser.add_argument("--output-dir", default="logs/eval-propagation")
    parser.add_argument("--prompt-file", default="scripts/sweep-prompt-1-propagate.md")
    parser.add_argument("--keep-worktree", action="store_true",
                        help="Skip worktree cleanup (for debugging)")
    args = parser.parse_args()

    api_key = read_api_key()
    scenario = parse_scenario(args.scenario)

    print(f"Scenario:    {scenario.get('name', args.scenario)}", file=sys.stderr)
    print(f"Model:       {args.model}", file=sys.stderr)
    print(f"Before SHA:  {scenario['before_sha']}", file=sys.stderr)
    print(f"Expected:    {scenario.get('expected_targets', [])}", file=sys.stderr)

    sweep_brief = open(args.prompt_file).read()
    system_prompt = (
        sweep_brief
        + "\n\n---\n\n"
        + "You are running inside an evaluation harness. The repo is checked out at the "
          "worktree root and you have these tools: read_file, edit_file, write_file, "
          "list_files, grep, done. There is no shell, no git, no commit step — the harness "
          "computes the diff after you finish. Make all surgical edits via edit_file. "
          "Create new pages with write_file. When you are done, call done() with a one-paragraph "
          "summary of what you changed and why.\n\n"
          "Stay in scope: only propagate. Do not author new findings, do not run synthesis, "
          "do not edit wiki/synthesis.md (that is Pass 2's job)."
    )

    trigger_list = "\n".join(f"  - {f}" for f in scenario["trigger_files"])
    user_prompt = (
        f"Trigger files (recently changed):\n{trigger_list}\n\n"
        f"Scenario context:\n{scenario['_body']}\n\n"
        f"Run Pass 1 propagation now. Read the trigger files first, then identify and update "
        f"affected wiki pages. Call done() when finished."
    )

    wt = make_worktree(scenario["before_sha"])
    print(f"Worktree:    {wt}", file=sys.stderr)

    try:
        loop = run_agentic_loop(
            wt, api_key, args.model, system_prompt, user_prompt,
            max_iterations=args.max_iterations,
        )
        metrics = compute_metrics(wt, scenario)
    finally:
        if args.keep_worktree:
            print(f"Worktree retained at {wt}", file=sys.stderr)
        else:
            remove_worktree(wt)

    in_per, out_per = PRICING_USD_PER_MTOK.get(args.model, (None, None))
    if in_per is not None:
        cost = (loop["input_tokens"] * in_per + loop["output_tokens"] * out_per) / 1_000_000
        cost_str = f"{cost:.4f}"
    else:
        cost = None
        cost_str = "unknown"

    date = datetime.date.today().isoformat()
    scen_name = scenario.get("name") or os.path.basename(args.scenario).replace(".md", "")
    model_safe = args.model.replace("/", "-")
    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, f"{date}-{model_safe}-{scen_name}.md")

    log = (
        f"---\n"
        f"date: {date}\n"
        f"scenario: {scen_name}\n"
        f"model: {args.model}\n"
        f"before_sha: {scenario['before_sha']}\n"
        f"iterations: {loop['iterations']}\n"
        f"completed: {loop['completed']}\n"
        f"hit_iter_cap: {loop['hit_iter_cap']}\n"
        f"input_tokens: {loop['input_tokens']}\n"
        f"output_tokens: {loop['output_tokens']}\n"
        f"cost_usd: {cost_str}\n"
        f"recall: {metrics['recall']}\n"
        f"precision: {metrics['precision']}\n"
        f"files_changed: {len(metrics['files_changed'])}\n"
        f"diff_lines: {metrics['diff_lines']}\n"
        f"---\n\n"
        f"# Propagation eval — {args.model} on {scen_name}\n\n"
        f"## Done summary\n\n"
        f"{loop['done_summary'] or '(model did not call done() — see last_text)'}\n\n"
    )
    if not loop["completed"] and loop["last_text"]:
        log += f"## Last assistant text\n\n```\n{loop['last_text']}\n```\n\n"
    if loop["error"]:
        log += f"## Error\n\n```\n{loop['error']}\n```\n\n"

    log += (
        f"## Metrics\n\n"
        f"- Recall: {metrics['recall']}\n"
        f"- Precision: {metrics['precision']}\n"
        f"- Files touched ({len(metrics['files_changed'])}): {metrics['files_changed']}\n"
        f"- Expected but not touched: {metrics['missed']}\n"
        f"- Touched but not expected: {metrics['spurious']}\n\n"
        f"## Diff\n\n```diff\n{metrics['diff']}\n```\n"
    )
    for f, content in metrics["new_files"].items():
        truncated = content[:5000]
        suffix = "" if len(content) <= 5000 else f"\n... [truncated, {len(content) - 5000} chars omitted]"
        log += f"\n## New file: {f}\n\n```\n{truncated}{suffix}\n```\n"

    with open(out_path, "w") as f:
        f.write(log)

    print(f"\nLog: {out_path}", file=sys.stderr)
    print(
        f"  iterations={loop['iterations']} completed={loop['completed']} "
        f"hit_iter_cap={loop['hit_iter_cap']}",
        file=sys.stderr,
    )
    print(
        f"  in={loop['input_tokens']:,} out={loop['output_tokens']:,} cost=${cost_str}",
        file=sys.stderr,
    )
    print(
        f"  recall={metrics['recall']} precision={metrics['precision']} "
        f"files={len(metrics['files_changed'])} diff_lines={metrics['diff_lines']}",
        file=sys.stderr,
    )
    print(out_path)


if __name__ == "__main__":
    main()
