# Maintenance Rules

Most documentation work is not writing new documents; it is keeping existing ones true after the product changed. These rules govern updates, versioning, deprecations, and release notes. They apply whenever the request is "update the docs", "the product changed", "document version X", or "write the release notes".

## Updating is not rewriting

When asked to update existing documentation, change what the product change invalidated and leave the rest alone. A wholesale rewrite destroys the reader's landmarks, the team's review history, and any links pointing into the document. Work diff-driven:

1. Identify what actually changed in the product — from the changelog, the code diff, or the user's description. List the changes explicitly before touching any document.
2. For each change, find every place the documentation states the old behavior: the section that describes it, the examples that exercise it, the configuration tables, the glossary entry, the troubleshooting entries built on it, and the FAQ. A limit raised from 100 to 500 typically appears in three to five places; fixing one of them creates a self-contradicting document, which is worse than a uniformly outdated one.
3. Update those places, matching the surrounding voice and depth. A patched paragraph that suddenly reads differently from its neighbors flags itself.
4. Re-run the technical review scoped to the touched documents, plus a cross-document consistency check on the changed facts.

If the existing documentation is genuinely poor, say so and propose a rewrite as its own piece of work — do not smuggle one into an update.

## Reviewing docs against a release

Given a new product version, audit before editing. Walk the changelog or diff and classify every entry:

| Change type | Documentation obligation |
|---|---|
| New feature | New section or document; glossary entries for new terms; example |
| Changed behavior or default | Update every statement of the old behavior; add a migration note if users must act |
| Deprecation | Mark the feature (see below); keep the docs until removal |
| Removal | Remove or archive the sections; add a migration path; check for dangling cross-references |
| Bug fix | Update only if the docs documented the buggy behavior as intended, or a troubleshooting entry taught a workaround that is now unnecessary |

The output of the audit is a list of documents and sections to touch, presented before the edits are made.

## Deprecation notes

A deprecated feature stays documented until it is removed — readers still run it in production. Mark it at the top of its section, not in a footnote:

```md
> **Deprecated since 2.4, removal planned for 3.0.** Use [batch publishing](api-reference.md#publish-a-batch)
> instead; it covers the same cases and lifts the 100-event limit. Existing integrations keep working
> until 3.0 but receive a `Deprecation` response header.
```

Every deprecation note answers three questions: since when, until when, and what replaces it. A note that cannot answer the replacement question is a signal to push back on the deprecation itself.

## Versioning documentation

When the product ships incompatible versions side by side, pin the docs:

- State the covered product version near the top of the package README ("This documentation covers version 2.x").
- Keep per-version documentation sets only when versions differ enough that inline notes ("in 1.x this defaults to `false`") would litter every page — maintaining parallel doc trees is expensive and drifts.
- Never describe two versions' behavior in one sentence. Split into marked blocks or separate sections.

## Release notes and changelogs

Release notes are documentation with the same quality bar — natural voice, concrete facts — plus one extra rule: lead with what the *user* must do or gets, not with what the team did.

Weak:

> Refactored the delivery scheduler for improved performance.

Strong:

> Deliveries to slow endpoints no longer delay other subscriptions on the same topic. If you saw bursts of late webhooks after one subscriber went down, that is fixed.

Order entries by reader impact: breaking changes first, then new capabilities, then fixes. Every breaking change carries a migration step, even a one-liner. Use `templates/release-notes.md` for the structure.
