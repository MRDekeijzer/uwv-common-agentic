---
name: create-pr
description: Create a GitHub Pull Request using the repository's PR template, filled in based on committed changes on the current branch. Use when the user says "create a PR", "open a PR", "make a pull request", "submit PR", or "create pull request". Asks the user about tests before proceeding.
metadata:
  use-case: Open een draft pull request op basis van het PR-sjabloon van de repository, gevuld met de commits op de huidige branch.
  owner: '@MRDekeijzer'
  status: supported
---
# Create PR from Repository Template

## When to use

- The user says "create a PR", "open a PR", "make a pull request", "submit PR",
  "create pull request", "open pull request".
- The branch has commits ahead of the base branch and the work is ready for review.

## When not to use

- The work is not committed yet. This skill reads committed changes only, so commit first.
- The branch has no commits ahead of base. Say so and stop.
- The repo has no PR template. Say so and stop, rather than inventing a format.

## Purpose

Automate PR creation by:

1. Reading the repo's PR template (`.github/pull_request_template.md`).
2. Analyzing committed changes on the current branch (vs the default branch).
3. Filling in the template sections intelligently.
4. Creating the PR on GitHub.

## Workflow

### 1. Discover context

- Detect the current branch name.
- Determine the default/base branch (usually `dev` or `main`).
- Find the PR template: look for `.github/pull_request_template.md`, then `pull_request_template.md` in the repo root. If none exists, inform the user and stop.

### 2. Gather committed changes

Only use committed changes, never uncommitted work. Run (or equivalent):

```
git log --oneline --no-merges origin/<base>..HEAD
git diff origin/<base>...HEAD --stat
git diff origin/<base>...HEAD
```

If the branch has no commits ahead of base, inform the user and stop.

Use commit messages, file stats, and diffs to understand what changed.

### 3. Fill in the template

Work from whatever sections the discovered template actually contains never change the template's structure. For each placeholder, fill it from the commit messages and diff:

- Check the checkbox(es) that match what the diff shows; leave the rest unchecked.
- Fill in the sections, you MUST be confident in the information being correct otherwise ask the user or verify yourself.
- Delete optional sections when the template says to remove them and they don't apply.
- Link the ticket using the template's closing line, taking the ID from the branch name (e.g. `feature/ABU-1234-...` → `Closes ABU-1234`).

Also derive a **Title** following conventional commits (e.g. `feat(scope): description`) from the branch name or commits.

### 4. Ask the user before creating

Before creating the PR, ask:

> I'm ready to create the PR. One quick question:
> **Tests** — Should I run any tests first, or is this ready as-is?

Only proceed after the user responds. If they say it's ready as-is, create the PR directly.

### 5. Create the Draft PR

Use the `github-pull-request_create_pull_request` tool (or `gh pr create --draft` via terminal) with:

- `title`: The derived PR title
- `body`: The filled-in template
- `base`: The default branch
- `head`: The current branch

If `gh` isn't authenticated or no PR-creation tool is available, tell the user and give them the exact `gh pr create --draft` command to run themselves instead of failing silently.
