---
name: technical-documentation-framework
description: A Claude Skill framework for generating clear, structured, example-rich, terminology-controlled technical documentation for any product, platform, service, SDK, API, workflow, or technical system — delivered as Markdown, Word (DOCX), PDF, HTML, or slides.
---

# Technical Documentation Framework

This skill produces high-quality technical documentation for any product or technical system.

It must not behave like a simple writing prompt. It must operate as a documentation pipeline: understand the product, identify the audience, map the knowledge, define terminology, design the document structure, write the sections, add examples and edge cases, review the result, prepare the final documentation package, and deliver it in the format the user asked for.

Two standards are non-negotiable across every phase:

1. The output must read as if a knowledgeable engineer wrote it. Apply `rules/natural-writing-rules.md` while writing, not as an afterthought.
2. The deliverable is what the user asked for. If they asked for a Word file with screenshots, the deliverable is a `.docx` on disk with the screenshots embedded — not Markdown plus an apology.

## Activation criteria

Use this skill when the user asks for any of the following:

- Write technical documentation.
- Create product documentation.
- Document this platform, service, API, SDK, library, agent, workflow, or system.
- Create a README.
- Create a developer guide.
- Create an architecture document.
- Create an API reference.
- Create a glossary.
- Turn rough product notes into documentation.
- Create a Claude Skill for documentation generation.
- Export or convert documentation to Word, PDF, HTML, or slides.
- Produce a document that includes screenshots of a product or UI.
- Update existing documentation after a product change.
- Write release notes, a migration guide, or a runbook.

## Default behavior

Unless the user specifies otherwise:

| Parameter | Default |
|---|---|
| Documentation language | Same language as the user's current conversation |
| Tone | Clear, explanatory, technically accurate |
| Audience | Developers, technical product teams, and architects |
| Depth | Medium to advanced |
| Output format | Whatever the user requests (DOCX, PDF, HTML, slides, ...); Markdown when unspecified |
| Writing voice | Natural, human, per `rules/natural-writing-rules.md` |
| Glossary | Required |
| Examples | Required |
| Edge cases | Required |
| Technical review | Required |
| Assumption handling | Explicitly label assumptions |

## Critical language rule

Before writing any documentation, detect the language of the user's current request and conversation.

The documentation must be written in that language unless the user explicitly requests another language.

Examples:

- User speaks Turkish → write the documentation in Turkish.
- User speaks English → write the documentation in English.
- User speaks Turkish but says "write it in English" → write the documentation in English.
- User switches language and gives a clear instruction → follow the latest explicit instruction.

Read and apply: `rules/language-rules.md`.

## Mandatory pipeline

The following steps must be followed in order.

### Phase 1 — Product Discovery

Read: `product-discovery/SKILL.md`

Goal:
Understand the product, the problem it solves, its users, components, integrations, inputs, outputs, assumptions, and boundaries.

Expected output:

- Product summary
- Problem statement
- Target users
- Main use cases
- Core components
- Integration points
- Product boundaries
- Assumptions
- Open questions

### Phase 2 — Audience Alignment

Read: `audience-alignment/SKILL.md`

Goal:
Identify who the documentation is for and how deep the explanation should be.

Expected output:

- Primary audience
- Secondary audience
- Technical level
- Required prior knowledge
- Concepts that must be explained
- Tone and terminology policy

### Phase 3 — Knowledge Mapping

Read: `knowledge-mapping/SKILL.md`

Goal:
Create a structured technical map of the product.

Expected output:

- Concept map
- Component map
- Data flows
- Runtime flows
- API or SDK surfaces
- Configuration areas
- Security concerns
- Operational concerns
- Observability points
- Failure scenarios

### Phase 4 — Glossary Building

Read: `glossary-builder/SKILL.md`

Goal:
Extract and define every important term used in the documentation.

Expected output:

- Term
- Short definition
- Detailed explanation
- Product-specific meaning
- Example
- Common confusion
- Related terms

The glossary is mandatory. Documentation is incomplete without it.

### Phase 5 — Document Architecture

Read: `document-architecture/SKILL.md`

Goal:
Design the final documentation package.

Expected output:

- Recommended document package
- Table of contents
- Section order
- Purpose of each section
- Required examples per section
- Diagram recommendations
- Cross-reference plan

### Phase 6 — Section Writing

Read: `section-writer/SKILL.md` and `rules/natural-writing-rules.md`

Goal:
Write the full documentation in clean, publishable Markdown, in a voice that reads human.

Expected output:

- Complete sections
- Clear headings
- Concept explanations
- Usage flows
- Configuration guidance
- Integration guidance
- API or SDK explanations when relevant

### Phase 7 — Examples and Edge Cases

Read: `examples-and-edge-cases/SKILL.md`

Goal:
Make the documentation practical and realistic.

Expected output:

- Simple example
- Realistic example
- Incorrect usage example
- Edge-case example
- Decision notes
- Common mistakes
- When not to use this product or feature

### Phase 8 — Technical Review

Read: `technical-review/SKILL.md`

Goal:
Review documentation for correctness, clarity, depth, example quality, and terminology consistency.

Expected output:

- QA score
- Missing sections
- Inconsistent terms
- Shallow areas
- Risky assumptions
- Recommended revisions
- Final readiness decision

### Phase 9 — Publishing

Read: `publishing/SKILL.md`

Goal:
Prepare the final documentation package.

Expected output:

```text
docs/
├── README.md
├── overview.md
├── getting-started.md
├── concepts.md
├── architecture.md
├── configuration.md
├── api-reference.md
├── examples.md
├── troubleshooting.md
├── glossary.md
└── faq.md
```

### Phase 10 — Format and Delivery

Read: `output-formats/SKILL.md`

Goal:
Deliver the reviewed documentation in the format the user requested.

Expected output:

- The final artifact in the requested format (DOCX, PDF, HTML, slides, or Markdown), written to disk and verified
- Screenshots or rendered diagrams embedded where the content calls for them
- The source Markdown package alongside the converted artifact, unless the user declines it

Skip the conversion step only when Markdown itself is the requested deliverable. Never skip the verification step: an artifact that was not opened and checked is not delivered.

## Updating existing documentation

When the request is to update documentation rather than create it, do not rerun the full pipeline blindly. Read and apply `rules/maintenance-rules.md`: work diff-driven from what actually changed in the product, touch every place the old behavior is stated, match the surrounding voice, and re-run technical review scoped to the changed documents. Release notes, migration guides, and deprecation notes follow the same rules and have templates in `templates/`.

## Reference output

`examples/sample-output-signalhop/` is a complete documentation package for a fictional product, written to this framework's standards. Use it as the quality bar during section writing and technical review — especially for voice, example density, boundary statements, and glossary depth.

## Mandatory quality rules

1. Every important technical term must be explained either on first use or in the glossary.
2. Every main section must include at least one example or scenario when applicable.
3. Product boundaries must be explicit.
4. A "What this product is not" or equivalent section must exist.
5. The reader must understand not only what the product does, but why it exists and how it behaves.
6. The tone must be technical and explanatory, not promotional.
7. Unknown information must not be invented. It must be labeled as an assumption or open question.
8. The glossary must guide terminology across the whole documentation.
9. Terminology inconsistency is a QA failure.
10. The final output must be publishable in the requested format; the working format is clean Markdown.
11. Documentation must be written in the language of the user's conversation unless explicitly overridden.
12. The text must pass the natural-writing self-check in `rules/natural-writing-rules.md`. Documentation that reads machine-generated is a QA failure regardless of technical accuracy.

## Final response behavior

When delivering the final documentation, provide:

1. A short summary of what was produced.
2. The documentation package structure.
3. The final artifact in the requested format, plus the source Markdown package.
4. Any assumptions made.
5. QA result, including the natural-writing check.
