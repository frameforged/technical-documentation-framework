# Example Rules

## Purpose

Examples turn abstract documentation into usable documentation.

## Templates versus prose

The labeled formats below (**Scenario:**, **Goal:**, ...) are for reference-style entries — example catalogs, edge-case lists, troubleshooting collections — where readers scan for a matching case. Inside narrative sections, weave examples into the prose instead: a code block introduced by a sentence beats a five-label form. Applying the labeled format everywhere produces exactly the mechanical texture that `natural-writing-rules.md` forbids.

## Required example types

Where relevant, include these three levels:

1. Simple example
2. Realistic example
3. Incorrect usage example

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

## Example for an API product

```md
### Incorrect Usage: Verifying the signature against re-serialized JSON

**Incorrect approach:**
The webhook handler parses the request body, re-serializes it with `json.dumps`, and computes the HMAC over the result.

**Why this is a problem:**
Serializers do not preserve key order or whitespace. The recomputed digest differs from the one the provider computed over the original bytes, so every genuine request fails verification with a 401 — intermittently, depending on payload shape, which makes it look like a provider-side bug.

**Correct approach:**
Compute the HMAC over the raw request bytes (`request.get_data()`, `express.raw()`), before any parsing middleware touches them.
```

A complete non-AI example set — narrative examples, edge cases, and symptom-first troubleshooting entries — is in `examples/sample-output-signalhop/`.

## Example for an AI agent orchestration product

```md
### Example: Customer request processing agent

**Scenario:**  
A user sends the message: "I want to increase my credit card limit."

**Goal:**  
The agent should classify the request, check whether authentication is required, call the appropriate tool only if allowed, and produce a safe response.

**Input:**  
"I want to increase my credit card limit."

**Process:**  
1. The agent identifies the request as a card limit increase request.
2. The guardrail checks whether sensitive financial action rules apply.
3. The agent verifies whether the user is authenticated.
4. If authentication is missing, the agent does not call the banking tool.
5. The agent returns a safe next-step response.

**Output:**  
"I can help with that, but you need to complete authentication before I can continue with a credit limit request."

**Important note:**  
The agent should not execute financial actions before authentication and policy checks are completed.
```
