# Codex Test Skill

This folder is a minimal test skill for validating Codex skill structure.

It includes:

- `SKILL.md` with required frontmatter and concise operating instructions.
- `agents/openai.yaml` with UI metadata.
- `references/` with optional guidance loaded only when needed.
- `scripts/` with small validation helpers.

Start by reading `SKILL.md`, then run:

```bash
python scripts/validate_yaml.py .
python scripts/count_tokens.py .
```
