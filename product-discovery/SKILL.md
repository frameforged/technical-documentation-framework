---
name: product-discovery
description: Analyzes the product, problem, users, components, integrations, boundaries, assumptions, and missing information before documentation is written.
---

# Product Discovery Skill

## Purpose

Understand the product before writing documentation.

This phase prevents vague documentation by identifying what the product is, why it exists, who uses it, what it connects to, and what is known or unknown.

## Inputs

The user may provide:

- Product name
- Product description
- Repository content
- API specification
- Architecture notes
- Screenshots
- Meeting notes
- Rough ideas
- Existing documentation
- A short domain description

## Output format

```md
# Product Discovery Report

## Product Summary

## Problem Statement

## Target Users

## Main Use Cases

## Core Capabilities

## Core Components

## Integration Points

## Inputs and Outputs

## Runtime or Operating Model

## Product Boundaries

## Assumptions

## Open Questions
```

## Source-driven discovery

The most common real request is "document this repository", with little or no prose description. In that case the codebase is the primary source, and discovery means reading it deliberately rather than asking the user to retype what the code already says. Work through the repository in this order:

1. **Orientation files first**: README, CHANGELOG, existing `docs/`, package manifests (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, ...). The manifest gives the product name, declared dependencies, entry points, and scripts — often the fastest honest summary of what the product is.
2. **Entry points**: the `main`/`bin`/`cmd` files, the HTTP route table, the CLI argument parser, or the exported public API of a library. The entry points define the product surface; everything else is implementation.
3. **Configuration**: config schemas, environment variable reads, example `.env` or YAML files. Every configuration key is a documentation obligation.
4. **The data model**: schema migrations, ORM models, protobuf/OpenAPI definitions. Core entities found here become glossary candidates.
5. **Tests**: integration and end-to-end tests show intended usage more truthfully than comments do, including setup order and expected failure behavior.
6. **Error paths**: raised exceptions, error enums, retry/timeout constants. These feed the troubleshooting and edge-case sections directly.

While reading, keep the boundary between observation and inference visible. "The service retries five times" is a fact if a constant says `MAX_RETRIES = 5`; "the service appears designed for multi-tenant use" is an inference and enters the report as an assumption. Version numbers, limits, and defaults must be quoted from code, not recalled from similar products.

If the repository is too large to read fully, say what was covered and what was not. A discovery report based on three of nine modules must list the other six under open questions, not silently generalize from the three.

## Analysis questions

Answer as many as possible:

- What is the product?
- What problem does it solve?
- Who uses it?
- What does the user do with it?
- What are the main features?
- What are the main components?
- What systems does it integrate with?
- What data enters and leaves the product?
- What happens at runtime?
- What is explicitly out of scope?
- What information is missing?

## Rules

- Do not invent facts.
- Clearly label assumptions.
- If the product is broad, scope the documentation based on the user's request.
- If the user provides only minimal information, create a best-effort discovery report and list open questions.
- Keep the report technical, not promotional.
