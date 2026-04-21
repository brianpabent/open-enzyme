#!/usr/bin/env python3
"""
Mermaid Obsidian Compatibility Linter
=====================================

Scans all .md files for Mermaid code blocks and flags syntax that
Obsidian's built-in Mermaid renderer can't handle.

Usage:
    python3 scripts/lint-mermaid.py              # scan all .md files
    python3 scripts/lint-mermaid.py docs/foo.md   # scan specific file(s)
    python3 scripts/lint-mermaid.py --fix         # auto-fix what we can

Exit codes:
    0  — no issues found
    1  — issues found (or --fix applied changes)
"""

import argparse
import glob
import re
import sys
from pathlib import Path

# ── Rules ────────────────────────────────────────────────────────────────────
# Each rule is (pattern_in_mermaid_block, description, auto_fix_func_or_None).

def _fix_br_tags(line: str) -> str:
    """Replace <br/>, <br>, <br /> with ' — ' or just remove them."""
    return re.sub(r'<br\s*/?>', ' ', line)

def _fix_html_bold(line: str) -> str:
    """Replace <b>...</b> and <strong>...</strong> with plain text."""
    line = re.sub(r'</?b>', '', line)
    line = re.sub(r'</?strong>', '', line)
    return line

RULES = [
    {
        "id": "BR_TAG",
        "pattern": re.compile(r'<br\s*/?>'),
        "description": "<br/> tags in node labels — Obsidian renders these as 'Unsupported markdown: list'",
        "fix": _fix_br_tags,
    },
    {
        "id": "HTML_BOLD",
        "pattern": re.compile(r'</?(?:b|strong)>'),
        "description": "<b>/<strong> tags — Obsidian Mermaid ignores inline HTML styling",
        "fix": _fix_html_bold,
    },
    {
        "id": "HTML_ITALIC",
        "pattern": re.compile(r'</?(?:i|em)>'),
        "description": "<i>/<em> tags — use plain text instead",
        "fix": lambda line: re.sub(r'</?(?:i|em)>', '', line),
    },
    {
        "id": "HTML_ENTITY",
        "pattern": re.compile(r'&(?:nbsp|amp|lt|gt|quot);'),
        "description": "HTML entities — Obsidian Mermaid may not decode these",
        "fix": None,  # too context-dependent to auto-fix
    },
    {
        "id": "FONT_TAG",
        "pattern": re.compile(r'</?font[^>]*>'),
        "description": "<font> tags — not supported in Obsidian Mermaid",
        "fix": lambda line: re.sub(r'</?font[^>]*>', '', line),
    },
    {
        "id": "UNQUOTED_LIST",
        "pattern": re.compile(r'\[(?!")[^\]]*\d+\.[^\]]*\]'),
        "description": "Unquoted node label containing 'N.' — Obsidian parses this as a markdown list. Wrap in double quotes: [\"...\"]",
        "fix": lambda line: re.sub(
            r'\[(?!")((?:[^\]]*\d+\.)[^\]]*)\]',
            lambda m: '["' + m.group(1) + '"]',
            line,
        ),
    },
]


# ── Core logic ───────────────────────────────────────────────────────────────

def extract_mermaid_blocks(content: str):
    """Yield (start_line, end_line, block_text) for each ```mermaid block."""
    lines = content.split('\n')
    in_block = False
    block_start = 0
    block_lines = []

    for i, line in enumerate(lines, start=1):
        if line.strip() == '```mermaid':
            in_block = True
            block_start = i
            block_lines = []
        elif in_block and line.strip() == '```':
            yield block_start, i, '\n'.join(block_lines)
            in_block = False
        elif in_block:
            block_lines.append(line)


def lint_file(filepath: str, fix: bool = False) -> list[dict]:
    """Lint a single file. Returns list of issues found."""
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')
    issues = []
    fixed_content = content

    for block_start, block_end, block_text in extract_mermaid_blocks(content):
        block_lines = block_text.split('\n')

        for line_offset, line in enumerate(block_lines):
            file_line = block_start + line_offset + 1  # +1 because block_start is the ```mermaid line

            for rule in RULES:
                if rule["pattern"].search(line):
                    issues.append({
                        "file": str(path),
                        "line": file_line,
                        "rule": rule["id"],
                        "description": rule["description"],
                        "text": line.strip(),
                    })

                    if fix and rule["fix"]:
                        fixed_line = rule["fix"](line)
                        fixed_content = fixed_content.replace(line, fixed_line, 1)

    if fix and fixed_content != content:
        path.write_text(fixed_content, encoding='utf-8')

    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Lint Mermaid blocks in markdown files for Obsidian compatibility."
    )
    parser.add_argument(
        "files", nargs="*",
        help="Specific .md files to lint. If omitted, scans docs/ and wiki/."
    )
    parser.add_argument(
        "--fix", action="store_true",
        help="Auto-fix issues where possible."
    )
    args = parser.parse_args()

    # Resolve project root (script lives in scripts/)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    if args.files:
        files = args.files
    else:
        files = sorted(
            glob.glob(str(project_root / "docs" / "*.md"))
            + glob.glob(str(project_root / "wiki" / "*.md"))
        )

    all_issues = []
    for f in files:
        issues = lint_file(f, fix=args.fix)
        all_issues.extend(issues)

    if not all_issues:
        print("✓ No Mermaid compatibility issues found.")
        return 0

    # Print report
    if args.fix:
        print(f"Fixed {len(all_issues)} issue(s):\n")
    else:
        print(f"Found {len(all_issues)} issue(s):\n")

    for issue in all_issues:
        rel_path = Path(issue["file"]).relative_to(project_root) if project_root in Path(issue["file"]).parents else issue["file"]
        prefix = "FIXED" if args.fix else "WARN"
        print(f"  [{prefix}] {rel_path}:{issue['line']}  [{issue['rule']}]")
        print(f"         {issue['description']}")
        print(f"         → {issue['text']}")
        print()

    return 1


if __name__ == "__main__":
    sys.exit(main())
