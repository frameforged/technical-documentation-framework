---
name: examples-and-edge-cases
description: Adds simple examples, realistic examples, incorrect usage examples, edge cases, common mistakes, and when-not-to-use guidance.
---

# Examples and Edge Cases Skill

## Purpose

Make documentation practical.

A reader should be able to understand not only the happy path, but also mistakes, limits, and unusual situations.

## Required additions

Where relevant, add:

- Simple example
- Realistic example
- Incorrect usage example
- Edge case
- Common mistake
- Decision note
- When not to use this feature or product

## Example format

```md
### Example: Scenario Name

**Scenario:**  
...

**Goal:**  
...

**Input:**  
...

**Process:**  
...

**Output:**  
...

**Important note:**  
...
```

## Edge-case format

```md
### Edge Case: Case Name

**What happens:**  
...

**Why it matters:**  
...

**Recommended handling:**  
...
```

## Incorrect usage format

```md
### Incorrect Usage: Mistake Name

**Incorrect approach:**  
...

**Why this is a problem:**  
...

**Correct approach:**  
...
```

## Placement rule

Use the labeled formats above in reference-style catalogs where readers scan for their case. Inside narrative sections, integrate examples into the prose — `rules/example-rules.md` explains the split, and `examples/sample-output-signalhop/` shows both styles in a finished package.

## Domain edge-case examples

Edge cases come from the product's own failure modes; the sets below illustrate the expected depth in two domains.

### API and integration products

- **Success response lost after processing.** The consumer handles the request, but the acknowledgment never reaches the producer, which retries. Without idempotent consumption the same action executes twice. Documentation must state the delivery guarantee and show the deduplication pattern.
- **The limit is hit only under production load.** A rate limit or timeout that manual testing never reaches (one caller, idle server) fails constantly at real concurrency. Document limits next to realistic load numbers, not only in a reference table.
- **Implicit creation hides typos.** When resources are created on first use (topics, buckets, queues), a misspelled name fails silently — nothing errors, nothing arrives. Document the observable signal that distinguishes "empty" from "misrouted".

### AI-agent products

- **Tool succeeds but the final answer is wrong.** A tool may return correct data that the agent interprets incorrectly. Tool output and final response should be traced separately so the failure can be located.
- **Long-term memory stores temporary information.** A passing user preference should not automatically become long-term memory. Memory writes should be deliberate and policy-controlled.
- **Guardrail only runs on final output.** If guardrails check only the final answer, the agent may still make unsafe tool calls during intermediate steps. Guardrails may be needed at input, planning, tool execution, and output stages.
