---
name: create-pr
description: Create a GitHub Pull Request using the repository's PR template, filled in based on committed changes on the current branch. Use when the user says "create a PR", "open a PR", "make a pull request", "submit PR", or "create pull request". Asks the user about tests before proceeding.
license: MIT
compatibility: Requires git and either the GitHub CLI (gh) or the VS Code GitHub Pull Requests extension.
metadata:
  use-case: Open een draft pull request op basis van het PR-template van de repository, gevuld met de commits op de huidige branch.
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

## Workflow

### 1. Discover context

- Detect the current branch name.
- Determine the base branch: `gh repo view --json defaultBranchRef -q .defaultBranchRef.name`. If `gh` is unavailable, use `git symbolic-ref --short refs/remotes/origin/HEAD`. Never guess.
- Find the PR template. GitHub matches the filename case-insensitively, so do the same (e.g. `git ls-files | grep -i pull_request_template`). Look in `.github/`, the repo root and `docs/`, in that order.
- If the template is a directory (`.github/PULL_REQUEST_TEMPLATE/*.md`), list the templates and ask the user which one to use.
- If no template exists, inform the user and stop.

### 2. Gather committed changes

Only use committed changes, never uncommitted work. Fetch first so the comparison is not against a stale base:

```
git fetch origin <base>
git log --oneline --no-merges origin/<base>..HEAD
git diff origin/<base>...HEAD --stat
git diff origin/<base>...HEAD
```

If the branch has no commits ahead of base, inform the user and stop.

Use commit messages, file stats, and diffs to understand what changed.

### 3. Fill in the template

Work from whatever sections the discovered template actually contains; never change the template's structure. For each placeholder, fill it from the commit messages and diff:

- Check the checkbox(es) that match what the diff shows; leave the rest unchecked.
- Fill in the sections. You MUST be confident the information is correct; otherwise ask the user or verify it yourself.
- Delete optional sections when the template says to remove them and they don't apply.
- If the template has a closing line for a ticket and the branch name contains a ticket key (e.g. `feat/ABC-123-...`), fill it in (`Closes ABC-123`). Otherwise leave the line for the user and mention it.

Also derive a **Title** following conventional commits (e.g. `feat(scope): description`) from the branch name or commits.

### 4. Ask the user before creating

Before creating the PR, ask:

> I'm ready to create the PR. One quick question:
> **Tests** — Should I run any tests first, or is this ready as-is?

Only proceed after the user responds. If they say it's ready as-is, create the PR directly.

### 5. Push and create the Draft PR

A pull request needs the branch on the remote. If `git status -sb` shows no upstream or unpushed commits, run `git push -u origin HEAD` first.

Use the `github-pull-request_create_pull_request` tool (or `gh pr create --draft` via terminal) with:

- `title`: The derived PR title
- `body`: The filled-in template
- `base`: The base branch from step 1
- `head`: The current branch

If `gh` isn't authenticated or no PR-creation tool is available, tell the user and give them the exact `git push` and `gh pr create --draft` commands to run themselves instead of failing silently.
