#!/usr/bin/env python3
"""Validate the minimal frontmatter and UI metadata for this test skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")


def read_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter '---'.")
    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter must close with a second '---'.") from exc

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def validate_skill(root: Path) -> list[str]:
    errors: list[str] = []
    skill_md = root / "SKILL.md"
    openai_yaml = root / "agents" / "openai.yaml"

    if not skill_md.exists():
        return ["Missing SKILL.md."]

    try:
        data = read_frontmatter(skill_md)
    except ValueError as exc:
        return [str(exc)]

    name = data.get("name", "")
    description = data.get("description", "")
    if not name:
        errors.append("Missing frontmatter field: name.")
    elif not NAME_RE.match(name):
        errors.append("Skill name must use lowercase letters, digits, and hyphens only.")
    if not description:
        errors.append("Missing frontmatter field: description.")
    elif len(description) < 40:
        errors.append("Description should explain what the skill does and when to use it.")

    if not openai_yaml.exists():
        errors.append("Missing agents/openai.yaml.")
    else:
        text = openai_yaml.read_text(encoding="utf-8")
        if "display_name:" not in text:
            errors.append("agents/openai.yaml missing interface.display_name.")
        if "$codex-test-skill" not in text:
            errors.append("default_prompt should mention $codex-test-skill.")

    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = validate_skill(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {root} looks like a valid test skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
