---
name: glossary-builder
description: Extracts technical terms and creates a consistent glossary with definitions, product-specific meanings, examples, common confusions, and related terms.
---

# Glossary Builder Skill

## Purpose

Create a controlled vocabulary for the documentation.

Technical documentation becomes confusing when the same concept is described with multiple names or when important concepts are used without definition.

## Term sources

Extract terms from:

- User-provided product description
- Existing product names
- Feature names
- Component names
- API names
- SDK classes or methods
- Configuration keys
- Error messages
- Domain concepts
- Architecture notes
- Security controls
- Operational processes

## Output format

```md
# Glossary

### Term

**Short definition:**  
...

**Detailed explanation:**  
...

**Meaning in this product:**  
...

**Example:**  
...

**Common confusion:**  
...

**Related terms:**  
...
```

## Required behavior

- Identify all important terms.
- Choose one preferred name for each concept.
- List aliases only inside the glossary.
- Explain terms in the selected documentation language.
- Keep product-specific technical names unchanged.
- Distinguish similar terms carefully.

## Domain starting points

Term candidates come from the product first; domain lists only prime the search. `rules/terminology-rules.md` carries two profiles — one for APIs/SaaS/integration products, one for AI-agent products — and a worked non-AI glossary lives in `examples/sample-output-signalhop/glossary.md`.

For AI-agent products specifically, these recur:

- Agent
- Tool
- Skill
- Brain
- Memory
- Short-term Memory
- Long-term Memory
- Guardrail
- Orchestration
- Runtime
- Workflow
- Connector
- Adapter
- Trace
- Evaluation
- Human-in-the-loop
- Policy
- Context
- State

## Quality rule

If the final documentation uses a technical term that is not commonly understood by the target audience, it must appear in the glossary.
