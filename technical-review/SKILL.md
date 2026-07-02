---
name: technical-review
description: Reviews generated documentation for correctness, clarity, depth, example quality, terminology consistency, assumptions, completeness, and publishing readiness.
---

# Technical Review Skill

## Purpose

Evaluate whether the documentation is ready to publish.

## Output format

```md
# Technical Documentation QA Report

## Overall Score

/5

## Correctness

## Clarity

## Depth

## Example Quality

## Terminology Consistency

## Natural Voice

## Language Compliance

## Missing Sections

## Inconsistent Terms

## Shallow Areas

## Risky Assumptions

## Recommended Revisions

## Final Decision
```

## Scoring

Use this weighting:

| Category | Weight |
|---|---:|
| Correctness | 25% |
| Clarity | 15% |
| Depth | 15% |
| Example quality | 15% |
| Terminology consistency | 15% |
| Natural voice | 10% |
| Language compliance | 5% |

Score natural voice against the self-check list in `rules/natural-writing-rules.md`. Read the two or three densest sections aloud in your head: template openers, stacked terms, uniform sentence rhythm, and filler intensifiers each cost points.

## Blocking issues

The documentation is not ready if:

- No glossary exists.
- Core terms are undefined.
- Product boundaries are missing.
- Examples are missing.
- Unknown facts are presented as confirmed facts.
- The same concept is used with inconsistent names.
- The documentation language does not follow the user's instruction or conversation language.
- The structure does not match the requested documentation type.
- The text reads machine-generated: template section openers, unexplained term stacking, uniform sentence rhythm, or filler intensifiers throughout.

## Final decision values

Use one of:

- Ready to publish
- Minor revision required
- Major revision required
- Rewrite required
