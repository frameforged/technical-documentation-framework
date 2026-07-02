# Technical Depth Rules

## Purpose

Prevent shallow documentation.

## Required questions for technical sections

For each important component or feature, answer:

- What is it?
- Why does it exist?
- Which problem does it solve?
- What inputs does it receive?
- What outputs does it produce?
- Which components does it depend on?
- How does it communicate with other components?
- What happens when it fails?
- How is it configured?
- How is it observed?
- How is it secured?
- What are its limits?

## Weak vs strong explanation

Weak:

> The runtime executes agents.

Strong:

> The runtime receives an agent execution request, builds the execution context, resolves the agent configuration, applies guardrail checks, determines available tools, executes allowed tool calls, records trace events, and returns the final response.

## Required "Important Details" section

Every major document should include an "Important Details" or equivalent section.

Example:

```md
## Important Details

- Tool access does not automatically mean the agent is authorized to use the tool. Tool execution should pass permission and policy checks.
- Long-term memory should not store temporary, sensitive, or unverified information.
- Guardrails may apply to input, planning, tool execution, and final output stages.
- Trace data should be designed for debugging and auditability, but it should not expose sensitive data unnecessarily.
```
