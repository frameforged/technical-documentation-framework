# Language Rules

## Purpose

This rule ensures that generated documentation follows the language of the user's current conversation.

## Primary rule

Write the documentation in the language used by the user in the current conversation unless the user explicitly requests a different language.

## Priority order

When deciding the documentation language, use this priority order:

1. Explicit language instruction from the user.
2. Language used in the latest user request.
3. Dominant language of the current conversation.
4. If still unclear, ask a concise clarification question or state the assumption.

## Examples

### Turkish conversation

User:

> Bu ürünün teknik dokümantasyonunu yaz.

Output language:

> Turkish

### English override

User:

> Bu ürünün dokümantasyonunu İngilizce yaz.

Output language:

> English

### Mixed conversation

User:

> Write this documentation in Turkish, but keep technical terms like Agent and Tool in English.

Output language:

> Turkish, with selected technical terms preserved in English.

## Terminology translation

Do not force translation of widely accepted technical terms if translation would reduce clarity.

Acceptable examples:

- Agent
- Tool
- Skill
- Runtime
- Guardrail
- Memory
- Trace
- Workflow
- Connector
- Adapter

When a technical term is kept in English, explain it in the documentation language.

Example:

> Agent, belirli bir hedefe ulaşmak için model, tool, memory ve policy gibi bileşenleri kullanan karar verici yazılım birimidir.

## Consistency

Once the documentation language is selected, use it consistently across all files.

Exceptions:

- Code examples
- API names
- Configuration keys
- Product-specific identifiers
- Standard protocol names
- Technical terms intentionally preserved in English
