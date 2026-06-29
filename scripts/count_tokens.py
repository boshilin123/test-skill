#!/usr/bin/env python3
"""Estimate readable content size for this test skill."""

from __future__ import annotations

import sys
from pathlib import Path


INCLUDED_SUFFIXES = {".md", ".yaml", ".yml", ".py", ""}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in INCLUDED_SUFFIXES:
            yield path


def estimate_tokens(text: str) -> int:
    words = len(text.split())
    chars = len(text)
    return max(words, chars // 4)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    total_chars = 0
    total_tokens = 0
    for path in iter_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        chars = len(text)
        tokens = estimate_tokens(text)
        total_chars += chars
        total_tokens += tokens
        print(f"{path.relative_to(root)}\tchars={chars}\test_tokens={tokens}")
    print(f"TOTAL\tchars={total_chars}\test_tokens={total_tokens}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
