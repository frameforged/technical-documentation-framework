# Natural Writing Rules

Documentation produced by this framework must read as if a knowledgeable engineer wrote it for a colleague. Readers can tell when a text was machine-generated, and once they suspect it, they stop trusting it. These rules exist to remove the patterns that trigger that suspicion.

The test for every sentence is simple: **would a person who actually knows this product say it this way while explaining it across a desk?** If not, rewrite it.

These rules apply in every output language. The examples below are in English, but the same habits appear in Turkish, German, or any other language, and the same fixes work.

## Patterns to eliminate

### 1. Empty openers and closers

Machine-written sections start with "This section covers X" and end with "In conclusion, X plays a vital role." Neither sentence carries information.

Weak:

> Authentication is a critical aspect of any modern system. This section explores the authentication mechanisms of the platform.

Better:

> Every request to the API carries a signed token. Without one, the gateway rejects the call before it reaches any service.

Start with a fact the reader needs. If the first sentence could open any document about any product, delete it.

### 2. Term stacking

Piling three or four technical terms into one sentence, none of them explained, is the fastest way to lose a reader and the most reliable sign of generated text.

Weak:

> The platform performs schema-driven payload validation, policy-based access resolution, and idempotent event materialization.

Better:

> Before a request touches business logic, the gateway checks it against a schema. A malformed payload never gets further than that. Access rules run next: the caller's role decides which operations are even visible.

Give each new term room. Introduce it, show what it does with one concrete case, then move on.

### 3. Reflexive triads

"Fast, reliable, and scalable." One triad in a document is fine. A triad in every paragraph is a template. Replace abstract adjective triples with one concrete consequence.

Weak:

> The module is flexible, extensible, and easy to maintain.

Better:

> Each connector lives in its own package, so replacing the payment provider does not touch the order pipeline.

### 4. Uniform sentence rhythm

When every sentence runs 20–25 words and follows the same subject–verb–object shape, the text reads like output, not writing. People vary. A short sentence lands a point. A longer one carries the mechanism, the exception, and the reason it matters. Vary length deliberately within each paragraph.

### 5. Filler intensifiers

"Highly", "extremely", "seamlessly", "robust", "cutting-edge", "it is important to note that" — these add bulk, not meaning. Cut them. If a claim needs weight, give it a number or a fact instead of an adverb.

Weak:

> The system delivers extremely high throughput with seamless scaling.

Better:

> A single worker handles about 2,000 events per second; adding workers scales linearly up to the partition count.

### 6. Transition-word chains

"Furthermore", "moreover", "additionally", "on the other hand" at the start of consecutive sentences signal assembly, not thought. If two sentences belong together, their content should connect them. Often the best transition is none.

### 7. Formatting overload

Bolding every noun, turning every paragraph into a bullet list, inserting a table where a sentence would do — this fragments the text and reads as auto-generated. Use bullets only for genuinely parallel, countable items. Use prose for explanation. Use tables for values the reader will look up, not for ideas.

### 8. Hedged non-statements

"This may potentially improve performance in certain scenarios" says nothing. Either state what improves, by how much, and when — or label it honestly as unverified and move it to the assumptions list.

### 9. Punctuation tells: em dashes, semicolons, arrow chains

The em dash ("—") and the semicolon are the two strongest punctuation-level signs of generated text. A human explaining something across a desk writes short sentences; a model glues clauses together with dashes and semicolons. In body prose:

- **No em dashes.** Where a dash would sit, use a comma, a parenthesis, or start a new sentence. "The binding is preserved — the agent does not break silently" becomes "The binding is preserved, so the agent does not break silently."
- **No semicolons.** Two clauses joined by a semicolon are two sentences. Write them as two sentences.
- **No arrow chains in prose.** "null → default" belongs in a table cell or code, not in a sentence. In prose write "if null, the default applies."

These marks stay acceptable where they are notation rather than prose: code, literal values (`ACTIVE→RETIRED` as an enum transition), and compact table-cell shorthand. Everywhere the reader reads full sentences, they go.

This applies in every language. In Turkish the same fixes hold: "değildir; ... türüdür" becomes "değildir, ... türüdür" or two sentences, and "tanımlar — örneğin ..." becomes "tanımlar. Örneğin ...".

## Explain with examples, always

An abstract definition alone is never enough. When introducing a concept, a configuration choice, or a limit, attach one of:

- **A concrete scenario.** "When a webhook fails, the retry queue holds it for up to 24 hours. A subscriber that comes back online Tuesday morning still receives Monday night's events."
- **A comparison that motivates the choice.** "Polling would work here, but at 10,000 devices it means 10,000 requests a minute for data that changes hourly. That is why the SDK pushes instead."
- **A number with its meaning attached.** "The 6 MB payload limit is roughly a 2,000-row CSV export."

## Register

Natural does not mean casual. Technical documentation keeps a professional register:

- Prefer third person and direct instruction ("the scheduler retries", "set the timeout to 30 s") over chatty address ("you'll love how easy this is").
- Analogies are welcome when they genuinely explain, but keep them measured. One good analogy per concept, not a running metaphor.
- Avoid exclamation marks, rhetorical questions in body text, and enthusiasm words ("amazing", "powerful", "effortless").
- Be precise. "Usually", "in most cases", "somehow" are acceptable only when the uncertainty is real — and then say why.

## Self-check pass

After drafting any section, reread it once with these questions. The first draft always needs this pass.

1. Which sentences carry no information? Delete them.
2. Which term appears without an example or definition nearby? Fix or simplify.
3. How many consecutive sentences share the same length and shape? Break the rhythm.
4. Count the intensifiers and hedges. Remove them or replace with facts.
5. Does any paragraph open with "This section..." or close with "In conclusion..."? Rewrite.
6. Are there bullet lists that should be prose, or bold text that earns nothing? Flatten them.
7. Read the hardest paragraph aloud. Where you stumble, the reader will too.
8. Search the text for "—" and ";" in body prose. Rewrite each hit as separate sentences, a comma, or a parenthesis (see pattern 9).

## Non-negotiable balance

None of this permits sacrificing technical accuracy for flow. The goal is not fewer terms; it is terms embedded in an explanation that earns them. An expert reader must still find the full technical content — precise, complete, and verifiable — just written by someone who sounds like they built the thing.
