# Technical Documentation Framework

A Claude Skill framework for producing clear, structured, example-rich, terminology-controlled technical documentation for any product, platform, service, SDK, API, library, workflow, or technical system — and delivering it in the format you actually need: Markdown, Word (DOCX), PDF, HTML, or slides.

## Why this exists

Asking a model to "write documentation" produces text that describes a product without helping anyone use it: generic sections, undefined jargon, no examples, no boundaries, and a voice that readers immediately recognize as machine-generated.

This framework replaces that single prompt with a ten-phase pipeline. Claude first understands the product, decides who is reading, maps the technical territory, and locks the terminology — and only then writes. Every draft passes a technical review with a scored rubric before it ships, and the final artifact is converted, verified, and delivered in whatever format was requested.

Two standards run through every phase:

- **The output reads human.** A dedicated rule set ([rules/natural-writing-rules.md](rules/natural-writing-rules.md)) eliminates the patterns that make text smell generated — empty section openers, stacked undefined terms, uniform sentence rhythm, filler intensifiers — and the QA rubric fails documentation that violates it, regardless of technical accuracy.
- **The deliverable is what was asked for.** "Give me a Word file with screenshots" produces a `.docx` on disk with embedded images, a real table of contents, native heading styles, and page numbers — checked before delivery.

## What it produces

- Product documentation and developer guides
- Architecture documents and decision records
- API and SDK references
- Integration guides and operational runbooks
- Troubleshooting guides, glossaries, migration guides, release notes

## The pipeline

| Phase | Skill | Output |
|---|---|---|
| 1. Product Discovery | [product-discovery](product-discovery/SKILL.md) | Product summary, use cases, boundaries, open questions |
| 2. Audience Alignment | [audience-alignment](audience-alignment/SKILL.md) | Reader profile, required depth, terminology policy |
| 3. Knowledge Mapping | [knowledge-mapping](knowledge-mapping/SKILL.md) | Concept, component, and flow maps; failure scenarios |
| 4. Glossary Building | [glossary-builder](glossary-builder/SKILL.md) | Controlled vocabulary with definitions and examples |
| 5. Document Architecture | [document-architecture](document-architecture/SKILL.md) | Package layout, section plan, diagram plan |
| 6. Section Writing | [section-writer](section-writer/SKILL.md) | Complete sections in a natural, human voice |
| 7. Examples and Edge Cases | [examples-and-edge-cases](examples-and-edge-cases/SKILL.md) | Realistic, incorrect-usage, and edge-case examples |
| 8. Technical Review | [technical-review](technical-review/SKILL.md) | Scored QA report and readiness decision |
| 9. Publishing | [publishing](publishing/SKILL.md) | Navigable Markdown package with assets |
| 10. Format and Delivery | [output-formats](output-formats/SKILL.md) | Verified DOCX / PDF / HTML / slides / Markdown artifact |

## Output formats

Markdown is the working format; the deliverable is whatever the request names. [scripts/convert.py](scripts/convert.py) wraps pandoc to turn a finished package into a single document:

```bash
python3 scripts/convert.py docs/ --to docx -o product-documentation.docx \
    --title "Product Documentation" --toc
```

DOCX and PDF outputs get a title page, automatic table of contents, native heading styles, and page numbers. HTML output is a single self-contained file. Screenshots and rendered diagrams live in `docs/assets/` and are embedded automatically. [output-formats/SKILL.md](output-formats/SKILL.md) covers capture conventions, per-format quality checks, and what to do when pandoc is unavailable.

## Language behavior

Documentation is written in the language of the conversation unless explicitly overridden: a Turkish request produces Turkish documentation, "bunu İngilizce yaz" produces English. Widely accepted technical terms may stay in English when translating them would hurt clarity — the rules are in [rules/language-rules.md](rules/language-rules.md).

## Getting started

1. Make the framework available to Claude — clone it into your skills directory, or point Claude at the repository in your session.
2. Ask for documentation the way you would ask a technical writer:

```text
Use this framework to create technical documentation for an AI agent
orchestration platform with agent creation, tool registration, memory
management, guardrails, and trace observability.

Audience: developers and platform engineers.
Include a glossary, real-world examples, edge cases, and troubleshooting.
Deliver it as a Word document with a table of contents.
```

A worked input prompt lives in [examples/agent-orchestration-documentation-prompt.md](examples/agent-orchestration-documentation-prompt.md), and [examples/sample-output-signalhop/](examples/sample-output-signalhop/) is a complete reference output — a documentation package for a fictional webhook delivery service, written to this framework's standards. It doubles as the quality bar during review.

The framework also maintains documentation, not just creates it: updates after a product change, release notes, migration guides, deprecation notes, and doc audits against a new version all follow [rules/maintenance-rules.md](rules/maintenance-rules.md).

## Repository structure

```text
technical-documentation-framework/
├── README.md
├── SKILL.md                     # Entry point: pipeline, defaults, quality gates
├── CLAUDE.md                    # Behavioral instructions for Claude
├── rules/                       # Cross-cutting rules applied in every phase
│   ├── documentation-principles.md
│   ├── natural-writing-rules.md # Keeps the output from reading machine-generated
│   ├── writing-style-rules.md
│   ├── language-rules.md
│   ├── terminology-rules.md
│   ├── structure-rules.md
│   ├── example-rules.md
│   ├── technical-depth-rules.md
│   ├── api-documentation-rules.md
│   ├── architecture-documentation-rules.md
│   ├── security-and-compliance-rules.md
│   ├── maintenance-rules.md     # Updates, versioning, deprecations, release notes
│   └── qa-rubric.md
├── product-discovery/           # Phase skills (one directory per phase)
├── audience-alignment/
├── knowledge-mapping/
├── glossary-builder/
├── document-architecture/
├── section-writer/
├── examples-and-edge-cases/
├── technical-review/
├── publishing/
├── output-formats/              # Phase 10: DOCX / PDF / HTML / slides delivery
├── scripts/
│   └── convert.py               # Markdown package → DOCX / PDF / HTML / PPTX
├── templates/                   # Reusable document skeletons
│   ├── documentation-package.md
│   ├── glossary-entry.md
│   ├── api-endpoint.md
│   ├── architecture-decision-record.md
│   ├── troubleshooting-entry.md
│   ├── runbook.md
│   ├── release-notes.md
│   └── migration-guide.md
└── examples/
    ├── agent-orchestration-documentation-prompt.md
    └── sample-output-signalhop/ # Reference output: a complete docs package for a fictional product
```

## Quality gate

Documentation does not ship until it clears the rubric in [rules/qa-rubric.md](rules/qa-rubric.md): correctness, clarity, depth, example quality, terminology consistency, and natural voice, each weighted and scored. Missing glossary, undefined core concepts, invented facts, machine-sounding prose, or an unverified output artifact are all blocking failures.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
