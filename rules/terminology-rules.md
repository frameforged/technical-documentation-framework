# Terminology Rules

## Purpose

Ensure that all important technical terms are defined, used consistently, and explained in the product context.

## Mandatory glossary entry format

Every important term must follow this format:

```md
### Term Name

**Short definition:**  
A one-sentence definition.

**Detailed explanation:**  
A deeper explanation of the concept.

**Meaning in this product:**  
How this product specifically uses the term.

**Example:**  
A realistic example.

**Common confusion:**  
Concepts that are similar but not the same.

**Related terms:**  
Linked concepts.
```

## Term selection rules

- Use one preferred term for each concept.
- Preserve product-specific names exactly.
- Preserve common technical terms when translation would reduce clarity.
- Explain preserved English terms in the documentation language.
- Do not use synonyms randomly.

## Domain profiles

The lists below are starting points per product domain, not a universal checklist. Extract the real glossary from the product itself — its code, API surface, and configuration; a payment API and an agent platform share almost no vocabulary. If the product fits none of these profiles, build the candidate list from the sources in `glossary-builder/SKILL.md` alone.

### Profile: APIs, SaaS, and integration products

- API Key
- Access Token
- Tenant / Organization
- Environment (test, staging, production)
- Endpoint
- Webhook
- Event
- Subscription
- Idempotency / Idempotency Key
- Rate Limit
- Pagination / Cursor
- Retry / Backoff
- Timeout
- Dead-letter Queue
- Delivery Guarantee (at-least-once, at-most-once, exactly-once)
- Payload
- Schema / Versioning
- Deprecation
- SLA / SLO
- Audit Log

For a worked glossary in this domain, see `examples/sample-output-signalhop/glossary.md`.

### Profile: AI and agentic products

When documenting an AI agent, orchestration platform, LLM platform, assistant framework, or automation platform, consider these terms:

- Agent
- Tool
- Skill
- Brain
- Model
- LLM
- Prompt
- System Prompt
- Instruction
- Policy
- Guardrail
- Memory
- Short-term Memory
- Long-term Memory
- Context
- Session
- State
- Workflow
- Orchestration
- Runtime
- Connector
- Adapter
- Function Calling
- Tool Calling
- Trace
- Observability
- Evaluation
- Human-in-the-loop
- Role-based Access Control
- Authorization
- Authentication
- Audit Log
- Sandbox
- Rate Limit
- Retry
- Timeout
- Fallback

## Example glossary entries

### Agent

**Short definition:**  
An agent is a software unit that uses a model, tools, memory, and policies to complete a task or make a decision.

**Detailed explanation:**  
An agent is more than a language model. It can interpret an objective, plan steps, call tools, use context, apply rules, and produce a controlled output.

**Meaning in this product:**  
In an agent orchestration platform, an agent is a managed entity with a name, purpose, available tools, memory configuration, guardrail policies, and runtime behavior.

**Example:**  
A customer-support agent classifies a user request, calls a CRM tool, checks policy rules, and drafts a response.

**Common confusion:**  
An agent is not the same as an LLM. The LLM may be one component used by the agent.

**Related terms:**  
Tool, Memory, Guardrail, Runtime, Orchestration.

### Tool

**Short definition:**  
A tool is a callable capability that allows an agent or system to perform an action outside pure text generation.

**Detailed explanation:**  
A tool can call an API, query a database, send an email, read a file, trigger a workflow, or interact with another system.

**Meaning in this product:**  
A tool is a registered executable integration with an input schema, output schema, permission model, and runtime execution behavior.

**Example:**  
`getCustomerInfo` receives a customer ID and returns customer profile data from a CRM system.

**Common confusion:**  
A tool is not a skill. A tool executes an action. A skill teaches or guides behavior.

**Related terms:**  
Skill, Connector, Adapter, Function Calling, Tool Calling.

### Skill

**Short definition:**  
A skill is a reusable instruction, rule, template, and example package that teaches a model or agent how to perform a specific task.

**Detailed explanation:**  
A skill shapes behavior. It may include a `SKILL.md`, rules, templates, examples, scripts, and domain-specific guidance.

**Meaning in this product:**  
In this framework, each skill is a specialized documentation phase such as product discovery, glossary building, section writing, or technical review.

**Example:**  
The `glossary-builder` skill extracts technical terms and converts them into standardized glossary entries.

**Common confusion:**  
A skill is not necessarily executable. A tool usually is executable.

**Related terms:**  
Tool, Instruction, Rule, Template.
