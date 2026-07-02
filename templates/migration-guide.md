# Migration Guide Template

A migration guide serves a reader with a working system on the old version and a limited maintenance window. Its job is to answer three questions in order: do I need to do anything, how much work is it, and what exactly do I run. Everything else is decoration.

```md
# Migrating from <old version> to <new version>

## Do you need to act?

<The triage table comes first. Most readers should be able to stop reading here.>

| You use... | Action needed |
|---|---|
| <feature unaffected> | None — upgrade directly |
| <feature with changed behavior> | Yes — see "<section>" below |
| <removed feature> | Yes, before upgrading — see "<section>" below |

## Before you start

- <Version prerequisites: e.g. "you must be on 2.3 or later; earlier versions migrate to 2.3 first">
- <Backups or state exports to take, with commands>
- <Expected downtime, or a statement that the migration is zero-downtime and why>

## <Change 1: named by the old behavior the reader will search for>

**What changed:** <old behavior → new behavior, one paragraph.>

**Who is affected:** <the concrete condition, ideally with a command or query that checks it.>

**Steps:**

1. <Exact command or code change, with before/after snippets.>
2. ...

**Verification:** <how to confirm this part of the migration worked.>

## <Change 2: ...>

## Rollback

<How to return to the old version if verification fails, and up to which point in the procedure
rollback remains possible. If a step is a point of no return, it was already marked in its section;
repeat the list of such steps here.>

## Known issues

<Migration-specific problems and their workarounds. Remove the section rather than leaving it
empty or speculative.>
```

Name sections after the *old* behavior, because that is what the reader searches for — someone hit by a removed flag searches the flag's name, not the new feature that replaced it.
