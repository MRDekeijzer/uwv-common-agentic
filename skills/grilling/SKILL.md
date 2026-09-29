---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea, one question at a time. Use when the user wants to stress-test their thinking, pressure-test a design, find the holes in a plan before building, or uses any 'grill' trigger phrase.
metadata:
  use-case: Bevraag een plan of ontwerp kritisch voordat het gebouwd wordt, met één vraag per keer.
  owner: '@FrisoHarlaar'
  status: supported
---

# Grilling

## When to use

- Before building something whose shape is still being argued about.
- A plan, design, spec or architectural decision that has not been pressure-tested.
- The user says "grill me", "stress-test this", "poke holes in this", "interview me".

## When not to use

- The work is already decided and the user wants it built — grilling then just stalls.
- A single factual question with one right answer. Look it up instead.
- You are the one who needs to decide. This skill surfaces the user's decisions; it does
  not hand its own judgement back as a question.

## How it works

Interview me relentlessly about every aspect of this until we reach a shared understanding.
Walk down each branch of the decision tree, resolving dependencies between decisions
one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.
Asking multiple questions at once is bewildering.

If a *fact* can be found by exploring the environment (filesystem, tools, etc.), look it up
rather than asking me. The *decisions*, though, are mine — put each one to me and wait for
my answer.

Do not act on it until I confirm we have reached a shared understanding.
