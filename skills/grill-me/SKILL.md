---
name: grill-me
description: A relentless interview to sharpen a plan or design. Invoked by the user as /grill-me; it starts a grilling session and is never triggered by the model on its own.
disable-model-invocation: true
metadata:
  use-case: Start op eigen initiatief een grilling-sessie met /grill-me; het model stelt dit nooit zelf voor.
  owner: '@FrisoHarlaar'
  status: supported
---

# Grill me

## When to use

- The user types `/grill-me`. That is the only trigger.

## When not to use

- Never on the model's own initiative — `disable-model-invocation: true` enforces this.
  If a plan looks like it needs pressure-testing, say so and let the user ask.
- To do the grilling itself. That lives in [`grilling`](../grilling/SKILL.md); this skill
  only starts it.

## How it works

Run a `/grilling` session.
