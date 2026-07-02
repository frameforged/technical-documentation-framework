---
name: audience-alignment
description: Determines the target audience, technical depth, prior knowledge, tone, terminology policy, and example level for the documentation.
---

# Audience Alignment Skill

## Purpose

Documentation must be written for a specific reader.

A developer guide, an executive overview, an API reference, and an operations runbook require different depth, structure, and terminology.

## Audience types

Consider one or more of the following:

- End user
- Developer
- Platform engineer
- DevOps engineer
- SRE
- Solution architect
- Technical architect
- Product manager
- Security engineer
- Compliance team
- Operations team
- New team member
- Executive or decision-maker

## Output format

```md
# Audience Alignment Report

## Primary Audience

## Secondary Audience

## Technical Level

Use a 1-5 scale.

## Expected Prior Knowledge

## Concepts That Must Be Explained

## Concepts That Can Be Assumed

## Tone

## Jargon Policy

## Documentation Depth

## Example Level

## Sections That Need Extra Detail
```

## Rules

- Do not write for everyone equally. Prioritize the primary audience.
- If multiple audiences exist, separate beginner explanation from reference-level detail.
- If the reader is less technical, explain concepts earlier and with examples.
- If the reader is highly technical, still include a glossary but avoid overexplaining common concepts.
- Preserve technical terms that are product-specific or industry-standard.
