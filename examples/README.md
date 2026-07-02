# Examples

Two kinds of material live here: an input example (a prompt you could give the framework) and an output example (what the framework should hand back).

## [agent-orchestration-documentation-prompt.md](agent-orchestration-documentation-prompt.md)

A worked input: a realistic request for documenting an AI agent orchestration platform, including audience, requirements, and optional delivery-format variations.

## [sample-output-signalhop/](sample-output-signalhop/)

A reference output package for **Signalhop**, a fictional webhook delivery service. Every fact in it was invented for the example; nothing describes a real product.

It exists as the quality bar. When reviewing generated documentation, compare against it:

- Sections open with information, never with "This section describes...".
- Every concept gets a concrete number, scenario, or code sample within a few sentences of its introduction.
- Boundaries are explicit ("Signalhop is deliberately not a message queue"), and the docs say when *not* to use the product.
- The troubleshooting guide is organized by observable symptom, not by component.
- The glossary entries distinguish confusable terms (event vs delivery, API key vs signing secret) instead of only defining them.
- Cross-references point to the exact section that continues the thought.

The package deliberately covers a non-AI product. The framework documents any technical system; if your generated output only reads well for agent platforms, it is overfitting to the examples in the rules files.
