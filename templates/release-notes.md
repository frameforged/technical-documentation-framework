# Release Notes Template

Order by reader impact: breaking changes first, new capabilities second, fixes last. Every entry says what the user gets or must do — not what the team did internally. `rules/maintenance-rules.md` has the voice guidance.

```md
# <Product Name> <version> — <date>

<One or two sentences on the theme of the release, only if it has one. Skip the paragraph
entirely for routine releases; do not manufacture a narrative.>

## Breaking changes

### <Change title, phrased as the behavior difference>

<What changed, who is affected, and how to tell if you are.>

**Migration:** <the concrete step, with a command or code snippet. Every breaking change has
one, even a one-liner.>

## New

### <Capability, phrased as what the user can now do>

<What it does, the smallest example that shows it, and a link to the full documentation section.>

## Changed

- <Behavior or default changes that are compatible but observable. Include old → new values:
  "default publish timeout raised from 5 s to 10 s".>

## Fixed

- <Symptom-first: "Webhook deliveries no longer duplicate when the endpoint responds during
  a deploy restart" — not "fixed race condition in scheduler".>

## Deprecated

- <Feature, since-when, removal target, replacement. Mirrors the deprecation note placed in
  the feature's own documentation.>
```

After writing the notes, apply the documentation updates they imply — a release note announcing a changed default while the configuration page still shows the old one is a consistency failure the QA rubric catches.
