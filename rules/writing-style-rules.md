# Writing Style Rules

These rules define the baseline register. For the deeper rules that keep the text from reading machine-generated — sentence rhythm, term stacking, filler removal, the self-check pass — read and apply `rules/natural-writing-rules.md`. Both files apply to every document.

## Voice

Write like an engineer explaining the system to a colleague: clear, calm, specific, and confident where the facts allow it. Third person or direct instruction; professional throughout.

## Avoid

- Marketing exaggeration and enthusiasm words ("powerful", "seamless", "effortless")
- Vague claims that a number or example could replace
- Buzzwords without explanation
- Unexplained acronyms
- Very long paragraphs
- Inconsistent terminology
- Unsupported performance or security claims
- Section openers that carry no information ("This section covers...")

## Prefer

- A concrete fact in the first sentence of every section
- Short paragraphs, with sentence length varied inside them
- Tables for values the reader will look up; prose for explanation
- Step-by-step flows for procedures
- Concrete examples over abstract description
- Explicit assumptions
- Clear boundaries
- Definitions before usage

## Technical terms

When a technical term appears for the first time:

1. Use the preferred term from the glossary.
2. Explain it immediately — a short gloss, an example, or both. Never let three new terms land in one sentence.
3. Add the term to the glossary when it matters beyond this paragraph.

Example:

> A guardrail is a control rule that limits what the agent can accept, execute, or return. If a guardrail blocks a tool call, the agent receives the rejection reason instead of the tool result.

## Numbers and claims

A claim without support is a liability. "Low latency" tells the reader nothing; "p95 under 120 ms at 1,000 requests per second" tells them everything. When no number exists, describe the mechanism that justifies the claim, or drop the claim.
