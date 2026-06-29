# Common Pitfalls

Use this reference when debugging a failed test skill check.

## Frontmatter

- `SKILL.md` must start with `---`.
- The frontmatter must contain `name` and `description`.
- The skill name should use lowercase letters, digits, and hyphens only.
- The frontmatter should close with a second `---` before the Markdown body.

## Metadata

- `agents/openai.yaml` should quote string values.
- `interface.default_prompt` should mention `$codex-test-skill`.
- Keep UI descriptions short enough for skill lists and chips.

## Resources

- Load references only when needed.
- Keep scripts deterministic and safe to run repeatedly.
- Do not place cache files, secrets, or generated logs in the skill folder.
