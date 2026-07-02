---
name: publishing
description: Converts the final documentation into a publishable Markdown package with a README, detailed docs, glossary, troubleshooting, examples, and FAQ when applicable.
---

# Publishing Skill

## Purpose

Prepare the final documentation as a clean, navigable Markdown package. Markdown is the working format; if the user asked for a different deliverable (DOCX, PDF, HTML, slides), this package is the input to `output-formats/SKILL.md`, which handles the conversion and verification.

## Default output package

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
├── faq.md
└── assets/            # screenshots and rendered diagrams, referenced with relative paths
```

Include `assets/` only when the documentation contains images. Name files `NN-short-description.png` in document order so converted formats keep figures in sequence.

Not every product needs every file, and some need more: `sdk-guide.md`, `integration-guide.md`, `migration-guide.md`, or `runbooks/` join the package when the product and the request call for them (`rules/structure-rules.md` lists the extended set). Small products shrink to as little as README, getting-started, and troubleshooting.

## File naming rules

- Use lowercase file names.
- Use hyphens instead of spaces.
- Keep names descriptive.
- Avoid unnecessary abbreviations.

## README requirements

The README should include:

```md
# Product Name

Short description.

## What It Does

## Who It Is For

## Quick Start

## Core Concepts

## Documentation Map

| Document | Description |
|---|---|

## Example Usage

## Support or Troubleshooting
```

## Publishing checklist

- Headings are consistent.
- Links are valid or clearly marked as placeholders.
- The glossary is included.
- The README links to detailed docs.
- Assumptions are visible.
- The documentation language is consistent.
- Code blocks are properly fenced.
- Tables are readable.
- No placeholder text remains unless intentionally marked.
- Images referenced in the text exist in `assets/` and every image is referenced from the text.
- If the user requested a non-Markdown format, hand off to `output-formats/SKILL.md` — publishing is not finished until the requested artifact exists and has been verified.
