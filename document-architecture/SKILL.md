---
name: document-architecture
description: Designs the documentation package, table of contents, section order, section purpose, examples, diagrams, and cross-reference plan.
---

# Document Architecture Skill

## Purpose

Design the structure before writing.

Good documentation has a navigable architecture. The reader should know where to start, where to find concepts, where to find integration details, and where to troubleshoot.

## Output format

```md
# Documentation Architecture

## Recommended Documentation Package

## Main README Structure

## Detailed Documents

## Section Order

## Section Purpose Table

| Section | Purpose | Target Audience | Required Content | Example Required |
|---|---|---|---|---|

## Diagram Recommendations

## Glossary Placement

## Cross-reference Plan

## Content That Should Not Be Included
```

## Standard package recommendation

Use this as a default:

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

## Rules

- The README should be short and navigational.
- Deep explanations should live in detailed docs.
- The glossary should be referenced from concept-heavy sections.
- Every major section should have a clear purpose.
- Do not create unnecessary files for small products.
