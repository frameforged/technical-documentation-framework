---
name: knowledge-mapping
description: Maps concepts, components, flows, APIs, SDKs, configuration areas, security controls, operations, observability points, and failure scenarios.
---

# Knowledge Mapping Skill

## Purpose

Turn product information into structured technical knowledge that can be used to write documentation.

## Output format

```md
# Knowledge Map

## Core Concepts

## Component Map

| Component | Responsibility | Inputs | Outputs | Dependencies | Notes |
|---|---|---|---|---|---|

## Main User Flows

## Runtime Flows

## Data Flows

## API Surface

## SDK Surface

## Configuration Areas

## Integration Points

## Security Controls

## Operational Concerns

## Observability Points

## Failure Scenarios

## Known Unknowns
```

## Required thinking

For every major component, identify:

- Its responsibility
- Its input
- Its output
- Its dependencies
- Its configuration
- Its failure modes
- Its observability signals

## Rules

- Keep this phase structured.
- Prefer tables for component and configuration mapping.
- Mark uncertainty clearly.
- Do not introduce architecture that the user did not provide unless explicitly creating a proposed design.
