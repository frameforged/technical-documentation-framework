# Documentation Principles

## 1. Explain before detailing

Start with the big picture before deep technical details.

Recommended order:

1. What the product is
2. What problem it solves
3. Who uses it
4. Core concepts
5. How it works
6. How to use it
7. How to integrate it
8. How to operate and troubleshoot it
9. What its limits are

## 2. Prefer clarity over cleverness

Documentation is not a marketing page. Avoid exaggerated claims.

Weak:

> This revolutionary system transforms productivity.

Strong:

> This system centralizes agent creation, tool registration, memory configuration, guardrail policies, and runtime traceability.

## 3. Define concepts in context

A term should not only be defined generally. It must also be explained in the product context.

Use this pattern:

```md
### Term

General meaning:
...

Meaning in this product:
...

Example:
...

Common confusion:
...
```

## 4. Show product boundaries

Every technical product has limits. Documentation must make them explicit.

Include sections like:

```md
## Product Boundaries

This product does:
...

This product does not:
...

This product is not suitable when:
...
```

## 5. Avoid unsupported claims

Do not claim performance, security, compliance, scalability, or reliability characteristics unless the input supports them.

Use assumptions when necessary.

## 6. Make the documentation useful after first reading

The reader should be able to return later and use the documentation as a reference.

Include:

- Tables
- Examples
- Decision notes
- Troubleshooting entries
- Glossary references
- Configuration explanations
