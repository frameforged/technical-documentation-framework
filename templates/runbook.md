# Runbook Template

A runbook is read at 3 a.m. by someone who did not build the system. Optimize for that reader: commands they can paste, decision points with explicit criteria, and no background theory that is not needed to act. Link to the architecture document for the why; the runbook is the what-now.

```md
# Runbook: <Procedure or Incident Name>

**Use this when:** <the observable trigger — the alert name, the symptom, the scheduled task>
**Do not use this when:** <adjacent situations that need a different runbook>
**Expected duration:** <how long the procedure takes end to end>
**Risk level:** <what can go wrong if a step is done incorrectly, and whether steps are reversible>

## Preconditions

- Access required: <systems, roles, credentials — verified before starting, not at step 7>
- State required: <what must be true before proceeding, and the command that checks it>

## Steps

1. <One action per step, with the exact command and the expected output.>

   ```bash
   <command>
   ```

   Expected: <what success looks like — a string in the output, a status code, a metric value>
   If not: <the branch — retry, skip to step N, or escalate>

2. ...

## Verification

<How to confirm the system is healthy after the procedure — specific checks, not "verify everything works".>

## Rollback

<How to undo the procedure if verification fails. If a step is irreversible, say so at that step, not here.>

## Escalation

<Who to contact when the runbook does not resolve the situation, and what information to bring: relevant IDs, log excerpts, which steps were completed.>
```

Two quality checks before publishing a runbook: every command was actually run once against a real or staging system, and someone who did not write it can follow it without asking questions. An untested runbook is a liability with a table of contents.
