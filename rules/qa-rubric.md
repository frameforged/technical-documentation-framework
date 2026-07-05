# Documentation QA Rubric

Score documentation on a 5-point scale.

## 1. Correctness — 25%

Check:

- Are technical statements supported by input or labeled as assumptions?
- Are product boundaries clear?
- Are unsupported claims avoided?
- Are API, SDK, configuration, or architecture details accurate?

## 2. Clarity — 15%

Check:

- Can the target reader understand the product?
- Are concepts defined before deep usage?
- Are paragraphs readable?
- Is jargon explained?

## 3. Depth — 20%

Check:

- Is the architecture or operating model explained?
- Are flows described?
- Are edge cases included?
- Are troubleshooting or failure scenarios included when relevant?

## 4. Example Quality — 15%

Check:

- Are examples realistic?
- Is there at least one simple example?
- Is there at least one incorrect usage example when relevant?
- Are edge cases practical?

## 5. Terminology Consistency — 15%

Check:

- Is there a glossary?
- Are terms used consistently?
- Are similar concepts distinguished?
- Are product-specific terms preserved?

## 6. Natural Voice — 10%

Check against `natural-writing-rules.md`:

- Do sections open with information rather than "This section describes..."?
- Are new terms explained on first use instead of stacked?
- Does sentence rhythm vary, or does every sentence share the same length and shape?
- Are filler intensifiers ("highly", "seamlessly", "robust") absent, with claims backed by numbers or mechanisms?
- Is formatting proportionate — bullets for parallel items only, prose for explanation?

## Decision table

| Score | Decision |
|---:|---|
| 4.50 - 5.00 | Ready to publish |
| 4.00 - 4.49 | Minor revision required |
| 3.00 - 3.99 | Major revision required |
| 0.00 - 2.99 | Rewrite required |

## Blocking issues

Documentation cannot be marked ready if any of these are true:

- No glossary exists.
- Core concepts are not explained.
- Product boundaries are missing.
- Examples are missing.
- Unknown facts are presented as facts.
- The same concept is named inconsistently.
- Usage or integration steps are ambiguous.
- The documentation is not written in the required language.
- The text fails the natural-writing self-check — it reads machine-generated (template openers, term stacking, uniform rhythm, filler intensifiers).
- The user requested a specific output format and the artifact was not produced or not verified.
- A formatted deliverable (DOCX/PDF) ships with default styling or fails the design self-check in `document-design-rules.md` — no brand-sourced palette, missing cover/TOC/header/footer, figures out of reading order, or an unexplained content loss against the source document.
