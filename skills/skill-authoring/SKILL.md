---
name: skill-authoring
description: Use when writing, reviewing, or splitting a skill for the uwv-common-agentic registry, or when someone asks "should this be a skill", "write a SKILL.md", "add this to the registry", or why a skill is not triggering. Covers the frontmatter contract, writing descriptions that actually fire, and the duplicate check.
metadata:
  use-case: Schrijf een SKILL.md die aan het registry-contract voldoet, en bepaal of een nieuwe skill überhaupt nodig is.
  projects: [uwv-common-agentic, any-claude-code-project, agent-tooling]
  owner: '@FrisoHarlaar'
  status: experimental
---

# Skill authoring

## When to use

- Someone wants to add a skill to this registry.
- A skill exists but never triggers, or triggers when it shouldn't.
- Deciding whether a piece of knowledge should be a skill, a line in `CLAUDE.md`, or nothing.

## When not to use

- The knowledge is specific to one repository — put it in that repo's `CLAUDE.md`. A skill
  that only ever applies to one codebase is a `CLAUDE.md` section with extra steps.
- It's a one-off instruction for the current task. Just say it.
- You want to *find* an existing skill — use `npx skills find <keyword>` instead.

## Does this need to be a skill?

Three questions. A "no" to any of them means stop.

1. Would at least two different projects load this?
2. Does it encode something an agent gets wrong without it — a convention, a gotcha, an
   order of operations? Knowledge the model already has is not a skill.
3. Does a skill already do it? Run `npx skills add MRDekeijzer/uwv-common-agentic --list`
   and `npx skills find <keyword>`. If one is close, extend it rather than adding a sibling.

## Write the description first

The `description` is the only text an agent sees when choosing whether to load the skill.
Everything else in the file is invisible until that choice is made, so a vague description
means the skill never runs.

Write it as a trigger, not a summary. Include the literal words a user would type.

- Weak: `Helps with database migrations.`
- Strong: `Use when adding or reviewing an Alembic migration, or when someone says "migration failed", "downgrade", or "the schema drifted". Covers reversible migrations and backfills on large tables.`

Then check the body: `## When to use` lists triggering situations, `## When not to use`
draws the boundary. The second section is the one that keeps the registry usable as it grows —
write it properly and it doubles as the duplicate check for the next contributor.

## Structure

```
skills/<name>/
  SKILL.md        # frontmatter + When to use / When not to use / How it works
  <anything else> # scripts, templates, reference docs - installed alongside
```

Keep `SKILL.md` short enough to read in one sitting. Long reference material goes in a
sibling file the skill links to, so it is loaded only when actually needed.

## Before opening the PR

```bash
python3 tools/validate_skills.py --fix   # regenerate the README catalog
python3 tools/validate_skills.py         # must exit 0
```

Full contribution rules, including the four merge gates, are in
[CONTRIBUTING.md](../../CONTRIBUTING.md).
