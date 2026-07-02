---
name: section-writer
description: Writes publishable Markdown documentation sections using the planned architecture, glossary, examples, assumptions, and technical depth rules.
---

# Section Writer Skill

## Purpose

Write the documentation sections in publishable Markdown.

## Required style

Apply `rules/writing-style-rules.md` and `rules/natural-writing-rules.md` while drafting — not as a cleanup step afterwards.

- Clear headings
- Short paragraphs, with sentence length varied inside them
- Concrete explanations; every section opens with a fact, never with "This section describes..."
- Consistent terminology; new terms explained on first use
- Practical examples
- Explicit assumptions
- Tables where helpful
- No unsupported claims
- No marketing exaggeration or filler intensifiers

## Generic section template

```md
## Section Title

This section explains ...

### What it is

### Why it matters

### How it works

### Example

### Important details

### Common mistakes
```

## Required sections for broad product documentation

Use these unless the product type suggests a better structure:

- Overview
- Problem Statement
- Target Audience
- What This Product Is
- What This Product Is Not
- Core Concepts
- Architecture or Operating Model
- Core Components
- Runtime Flow
- Getting Started
- Configuration
- Usage Scenarios
- API, SDK, or Integration Reference
- Examples
- Edge Cases
- Security and Authorization
- Observability
- Troubleshooting
- Product Boundaries
- FAQ
- Glossary

## Writing rules

- Define important terms before using them heavily.
- Use the glossary's preferred term consistently.
- Mention assumptions where information is missing.
- Make boundaries explicit.
- Separate conceptual explanation from operational steps.
- Use examples that match the user's product domain.
