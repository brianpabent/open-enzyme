#!/usr/bin/env python3
"""
run_experiment.py — fire all 8 prompts at all 4 vendor models via OpenRouter.

Reads OPENROUTER_API_KEY from env or repo root .env.
Writes one response file per (prompt, vendor) pair into responses/<prompt-id>/<vendor>.md,
each with YAML frontmatter recording the OpenRouter response model, usage, cost.

Also writes responses/_cost_log.jsonl — one line per call — for the provenance audit.

Idempotent: if a response file already exists with a non-empty body, skip.
Use --force to re-run.
"""

import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # Open Enzyme repo root
PROMPTS_DIR = HERE / "prompts"
RESPONSES_DIR = HERE / "responses"
COST_LOG = RESPONSES_DIR / "_cost_log.jsonl"

# Vendor models — names from scripts/synthesize.py + OpenRouter slug catalog.
# Anthropic Opus 4.7 OpenRouter slug per CLAUDE.md context is "anthropic/claude-opus-4-7".
# OpenAI GPT-5.5 is used by Pass 3; the parent brief asked for GPT-5 or 5.5 — we use 5.5
# since Pass 3 uses it and it's the operational reviewer in the daemon.
VENDORS = {
    "deepseek":  "deepseek/deepseek-v4-pro",
    "gemini":    "google/gemini-2.5-pro",
    "openai":    "openai/gpt-5.5",
    "anthropic": "anthropic/claude-opus-4-7",
}

PRICING_USD_PER_MTOK = {
    "google/gemini-2.5-pro":      (1.25, 5.00),
    "deepseek/deepseek-v4-pro":   (0.435, 0.87),
    "anthropic/claude-opus-4-7":  (15.00, 75.00),
    # OpenRouter sometimes returns "anthropic/claude-4.7-opus" as the served
    # slug for the same model — both map to the same pricing tier.
    "anthropic/claude-4.7-opus":  (15.00, 75.00),
    "openai/gpt-5.5":             (3.00, 12.00),
    "openai/gpt-5":               (2.50, 10.00),
}

# Per-vendor max_tokens. DeepSeek V4-Pro and OpenAI GPT-5.5 are reasoning
# models that consume substantial tokens internally before emitting visible
# content — empirically ~3.5K-5K reasoning tokens for these prompts. We
# cap them at 8K. Gemini and Anthropic do not behave this way and produce
# tighter outputs; capping them at 2K keeps Opus cost bounded.
MAX_TOKENS_BY_VENDOR = {
    "deepseek":  8000,
    "openai":    8000,
    "gemini":    8000,  # bumped from 5000 after Gemini still truncated on prompts 6 + 8
    "anthropic": 6000,  # bumped from 4000 after Anthropic still truncated on prompt 8
}
TEMPERATURE = 0.7  # match daemon Pass 2

DATE_VERSION_SUFFIX_RE = re.compile(r"-\d{8}$")


def canonical_model_slug(slug: str) -> str:
    base = slug.split(":", 1)[0]
    return DATE_VERSION_SUFFIX_RE.sub("", base)


def read_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("OPENROUTER_API_KEY not in env or .env")


def load_prompt_text(prompt_file: pathlib.Path) -> str:
    """Strip the YAML frontmatter; return everything after the closing '---'."""
    text = prompt_file.read_text()
    if text.startswith("---"):
        # find second '---' on its own line
        m = re.search(r"^---\s*$", text[3:], re.MULTILINE)
        if m:
            return text[3:][m.end():].lstrip("\n")
    return text


def call_openrouter(api_key: str, model_slug: str, prompt: str, max_tokens: int, max_retries: int = 4):
    """Single OpenRouter chat-completion call with retry on transient errors."""
    body = {
        "model": model_slug,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": TEMPERATURE,
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
        json.dump(body, tf)
        body_path = tf.name

    last_err = None
    try:
        for attempt in range(max_retries):
            result = subprocess.run(
                [
                    "curl", "-sS", "--fail-with-body",
                    "https://openrouter.ai/api/v1/chat/completions",
                    "-H", f"Authorization: Bearer {api_key}",
                    "-H", "Content-Type: application/json",
                    "-H", "HTTP-Referer: https://github.com/brianpabent/open-enzyme",
                    "-H", "X-Title: Open Enzyme empirical-vendor-comparison",
                    "-d", f"@{body_path}",
                    "--max-time", "300",
                ],
                capture_output=True, text=True, timeout=320,
            )
            if result.returncode == 0:
                try:
                    return json.loads(result.stdout), None
                except json.JSONDecodeError as e:
                    last_err = f"non-json: {result.stdout[:500]} ({e})"
                    return None, last_err
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
                last_err = (
                    f"curl exit {result.returncode}\n"
                    f"stderr: {result.stderr.strip()[:500]}\n"
                    f"stdout: {result.stdout[:1000]}"
                )
                return None, last_err
            backoff = [10, 30, 60][attempt] if attempt < 3 else 60
            print(f"  [retry {attempt+1}] transient, sleeping {backoff}s", file=sys.stderr, flush=True)
            time.sleep(backoff)
    finally:
        os.unlink(body_path)
    return None, last_err


def cost_of(model_slug: str, in_tok: int, out_tok: int) -> float:
    canon = canonical_model_slug(model_slug)
    p = PRICING_USD_PER_MTOK.get(canon)
    if not p:
        return 0.0
    return in_tok * p[0] / 1_000_000 + out_tok * p[1] / 1_000_000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="re-run prompts even if response file exists")
    parser.add_argument("--only-prompt", default="", help="if set, only run prompts whose stem contains this substring")
    parser.add_argument("--only-vendor", default="", help="if set, only run this vendor key (deepseek/gemini/openai/anthropic)")
    parser.add_argument("--dry-run", action="store_true", help="show what would be called, don't call")
    parser.add_argument("--replicate", type=int, default=1, help="replicate number; writes to <vendor>-r<N>.md. Default 1.")
    args = parser.parse_args()
    replicate_suffix = f"-r{args.replicate}"

    api_key = read_api_key()
    RESPONSES_DIR.mkdir(exist_ok=True)

    prompts = sorted(PROMPTS_DIR.glob("*.md"))
    if args.only_prompt:
        prompts = [p for p in prompts if args.only_prompt in p.stem]
    if not prompts:
        sys.exit("no prompts matched")

    vendors = VENDORS if not args.only_vendor else {args.only_vendor: VENDORS[args.only_vendor]}

    total_cost = 0.0
    calls = 0
    skipped = 0
    errors = []

    for prompt_path in prompts:
        prompt_id = prompt_path.stem
        prompt_text = load_prompt_text(prompt_path)
        prompt_hash = hashlib.sha256(prompt_text.encode()).hexdigest()[:12]
        per_prompt_dir = RESPONSES_DIR / prompt_id
        per_prompt_dir.mkdir(exist_ok=True)

        print(f"\n=== {prompt_id}  (sha256:{prompt_hash}) ===", file=sys.stderr)
        for vendor_key, model_slug in vendors.items():
            out_path = per_prompt_dir / f"{vendor_key}{replicate_suffix}.md"
            if out_path.exists() and out_path.stat().st_size > 200 and not args.force:
                print(f"  [skip] {vendor_key} already has a response", file=sys.stderr)
                skipped += 1
                continue

            if args.dry_run:
                print(f"  [dry] would call {model_slug}", file=sys.stderr)
                continue

            max_tok = MAX_TOKENS_BY_VENDOR.get(vendor_key, 4000)
            print(f"  [call] {vendor_key} ({model_slug}, max_tokens={max_tok}) ...", file=sys.stderr, flush=True)
            t0 = time.time()
            resp, err = call_openrouter(api_key, model_slug, prompt_text, max_tok)
            dt = time.time() - t0

            ts = datetime.datetime.utcnow().isoformat() + "Z"
            if err is not None or resp is None:
                print(f"  [ERR ] {vendor_key}: {err[:300] if err else 'unknown'}", file=sys.stderr)
                errors.append((prompt_id, vendor_key, err))
                # Persist the error so the audit trail is complete.
                out_path.write_text(
                    f"---\nprompt_id: {prompt_id}\nvendor: {vendor_key}\nmodel_requested: {model_slug}\n"
                    f"call_timestamp_utc: {ts}\nstatus: ERROR\nerror: |\n  {(err or '').replace(chr(10), chr(10)+'  ')}\n---\n\n"
                    f"(no response — see error)\n"
                )
                _log_call(prompt_id, vendor_key, model_slug, None, None, None, dt, ts, "error", err, args.replicate)
                continue

            choice = resp["choices"][0]
            content = choice.get("message", {}).get("content") or ""
            finish_reason = choice.get("finish_reason", "?")
            served_raw = resp.get("model", model_slug)
            served = canonical_model_slug(served_raw)
            usage = resp.get("usage", {})
            in_tok = usage.get("prompt_tokens", 0)
            out_tok = usage.get("completion_tokens", 0)
            call_cost = cost_of(served, in_tok, out_tok)
            total_cost += call_cost
            calls += 1

            if not content.strip():
                err_msg = f"empty content; finish_reason={finish_reason!r}; choice={json.dumps(choice)[:500]}"
                print(f"  [ERR ] {vendor_key}: empty content (finish_reason={finish_reason})", file=sys.stderr)
                errors.append((prompt_id, vendor_key, err_msg))
                out_path.write_text(
                    f"---\nprompt_id: {prompt_id}\nvendor: {vendor_key}\nmodel_requested: {model_slug}\n"
                    f"model_served: {served}\nmodel_served_raw: {served_raw}\nfinish_reason: {finish_reason}\n"
                    f"call_timestamp_utc: {ts}\nstatus: EMPTY\n---\n\n(empty content)\n"
                )
                _log_call(prompt_id, vendor_key, model_slug, served, in_tok, out_tok, dt, ts, "empty", err_msg, args.replicate)
                continue

            response_hash = hashlib.sha256(content.encode()).hexdigest()[:12]
            header = (
                f"---\n"
                f"prompt_id: {prompt_id}\n"
                f"prompt_sha256_12: {prompt_hash}\n"
                f"vendor: {vendor_key}\n"
                f"replicate: {args.replicate}\n"
                f"model_requested: {model_slug}\n"
                f"model_served: {served}\n"
                f"model_served_raw: {served_raw}\n"
                f"call_timestamp_utc: {ts}\n"
                f"latency_seconds: {dt:.2f}\n"
                f"input_tokens: {in_tok}\n"
                f"output_tokens: {out_tok}\n"
                f"cost_usd: {call_cost:.4f}\n"
                f"finish_reason: {finish_reason}\n"
                f"response_sha256_12: {response_hash}\n"
                f"status: ok\n"
                f"---\n\n"
            )
            out_path.write_text(header + content + "\n")
            print(f"  [done] {vendor_key} r{args.replicate} cost=${call_cost:.4f} ({in_tok} in / {out_tok} out, {dt:.1f}s)", file=sys.stderr)
            _log_call(prompt_id, vendor_key, model_slug, served, in_tok, out_tok, dt, ts, "ok", None, args.replicate)

    print(f"\n--- summary ---", file=sys.stderr)
    print(f"calls made:      {calls}", file=sys.stderr)
    print(f"skipped (cached): {skipped}", file=sys.stderr)
    print(f"errors:          {len(errors)}", file=sys.stderr)
    print(f"total cost USD:  ${total_cost:.4f}", file=sys.stderr)
    if errors:
        print("\nerrors detail:", file=sys.stderr)
        for prompt_id, vendor, err in errors:
            print(f"  - {prompt_id} / {vendor}: {(err or '')[:200]}", file=sys.stderr)


def _log_call(prompt_id, vendor, model_req, model_served, in_tok, out_tok, dt, ts, status, err, replicate=1):
    rec = {
        "timestamp_utc": ts,
        "prompt_id": prompt_id,
        "vendor": vendor,
        "replicate": replicate,
        "model_requested": model_req,
        "model_served": model_served,
        "input_tokens": in_tok,
        "output_tokens": out_tok,
        "latency_seconds": round(dt, 2),
        "status": status,
        "error": (err[:500] if err else None),
    }
    with COST_LOG.open("a") as f:
        f.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    main()
