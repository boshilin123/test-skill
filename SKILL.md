---
name: codex-test-skill
description: Create and validate a minimal Codex skill scaffold for testing skill loading, frontmatter parsing, reference routing, and helper script execution. Use when the user wants a lightweight test skill, a sample skill folder, or a quick structural check for Codex skill conventions.
---

# Codex Test Skill

## Purpose

Use this skill as a small, low-risk fixture for checking whether Codex can discover a skill, read its instructions, load optional references, and run bundled helper scripts.

## Workflow

1. Confirm the requested skill folder or file path.
2. Read `SKILL.md` first and keep the active context small.
3. Load `references/style_guide.md` only when writing or reviewing skill prose.
4. Load `references/common_pitfalls.md` only when debugging a failed validation or inconsistent skill behavior.
5. Run `scripts/validate_yaml.py` before reporting the skill as structurally ready.
6. Run `scripts/count_tokens.py` when checking whether the skill is too verbose for a test fixture.

## Expected Structure

```text
codex-test-skill/
|-- SKILL.md
|-- README.md
|-- LICENSE
|-- .gitignore
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- style_guide.md
|   `-- common_pitfalls.md
`-- scripts/
    |-- validate_yaml.py
    `-- count_tokens.py
```

## Validation

Run the local validator from the skill root:

```bash
python scripts/validate_yaml.py .
python scripts/count_tokens.py .
```

Treat this skill as a sample, not as production policy. Keep changes simple, deterministic, and easy to inspect.
