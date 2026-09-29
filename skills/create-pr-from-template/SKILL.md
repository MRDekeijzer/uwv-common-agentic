---
name: create-pr-from-template
description: Create a GitHub Pull Request using the repository's PR template, filled in based on committed changes on the current branch. Use when the user says "create a PR", "open a PR", "make a pull request", "submit PR", or "create pull request". Asks the user about tests and changelog before proceeding.
metadata:
  use-case: Open een pull request die het PR-sjabloon van de repo zelf gebruikt, gevuld vanuit de commits op je branch.
  projects: [elk-github-project, repos-met-pr-sjabloon, uwv-common-agentic]
  owner: '@FrisoHarlaar'
  status: supported
---

# Create PR from Repository Template

## When to use

- The user says "create a PR", "open a PR", "make a pull request", "submit PR",
  "create pull request", "open pull request".
- The branch has commits ahead of the base branch and the work is ready for review.

## When not to use

- The work is not committed yet. This skill reads committed changes only — commit first.
- The branch has no commits ahead of base. Say so and stop.
- The repo has no PR template and the user wants a specific custom format. Ask them for it
  instead of inventing one.

## Purpose

Automate PR creation by:
1. Reading the repo's PR template.
2. Analyzing committed changes on the current branch (vs the default branch).
3. Filling in the template sections intelligently.
4. Creating the PR on GitHub.

## Workflow

### 1. Discover context

- Detect the current branch name.
- Determine the default/base branch (usually `main`, sometimes `dev`).
- Find the PR template. GitHub accepts several names and either casing, so check all of:
  `.github/PULL_REQUEST_TEMPLATE.md`, `.github/pull_request_template.md`,
  `PULL_REQUEST_TEMPLATE.md` and `pull_request_template.md` in the repo root, and any file
  under `.github/PULL_REQUEST_TEMPLATE/`.

### 2. Gather committed changes

Run (or equivalent):
```
git log --oneline --no-merges origin/<base>..HEAD
git diff origin/<base>...HEAD --stat
git diff origin/<base>...HEAD
```

Use commit messages, file stats, and diffs to understand what changed.

### 3. Fill in the PR template

- **Title**: Derive from branch name or commit messages, in Conventional Commits form
  (e.g. `feat(scope): description`). In a squash-merge repo this title becomes the commit
  line on the base branch, so it has to stand on its own.
- **Description**: Summarize the changes based on the diff — what was added/changed and why.
- **Tests section**: Check the appropriate box based on what you observe (test files changed,
  infra-only change, etc.).
- **Changelog section**: Leave unchecked by default.
- **Documentation section**: Check "No documentation updates required" for infra/config
  changes unless docs were touched.
- **Closes**: Extract the ticket ID from the branch name (e.g. `feature/ABU-1234-...` →
  `Closes ABU-1234`).

### 4. Ask the user BEFORE creating

Before creating the PR, ask the user:

> I'm ready to create the PR. Two quick questions:
> 1. **Tests** — Should I run any tests first, or is this ready as-is?
> 2. **Changelog** — Should I add an entry to `CHANGELOG.md` before opening the PR?

Only proceed after the user responds. If they say no to both, create the PR directly.
If they want changelog updates, make the edit, commit, and push before creating the PR.

### 5. Create the PR

Use the `github-pull-request_create_pull_request` tool, or `gh pr create` in the terminal, with:
- `title`: The derived PR title
- `body`: The filled-in template
- `base`: The default branch
- `head`: The current branch

## Rules

- **Always** base the PR body on the repo's actual template — do not invent a custom format.
- **Always** derive content from committed changes, not uncommitted work.
- **Never** create the PR without first asking about tests and changelog.
- **Never** modify the template structure — only fill in the placeholder sections.
- If no PR template is found in the repo, fall back to a simple summary format.
- If the branch has no commits ahead of base, inform the user and stop.
