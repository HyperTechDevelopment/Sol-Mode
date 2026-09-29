# Namespace: devops

Applies when the deliverable changes live state or the machinery that produces it: infrastructure as code, pipelines, images, deploy and release configuration, monitoring, alerting, secrets wiring, DNS, migrations. Logic inside a pipeline file stays a coding task. What the pipeline does to real systems routes here.

## Rules for getting this work done

- Observe the current live state from the system before proposing a change to it. The repository is a claim about that state.
- Produce a plan or diff and read it before applying anything.
- Name the blast radius: environments, services, jobs, scheduled tasks, and users affected.
- Name the rollback, and whether it has ever been exercised. Rollback that cannot restore data is not a rollback.
- Confirm the deployed revision or image digest by querying the system, never from a green pipeline run.
- Verify the condition the change was meant to achieve: the step passes, the health check answers, the alert fires when it should, the job completes.
- Check what sits next to the change: dependent jobs, other environments, shared resources.
- Treat secrets as read-only. Confirm they resolve and that no plaintext value reaches output, logs, or files.

## Decision boundary

When the repository and the live system disagree, the live system wins, and the drift is a finding to report before the change. When a runbook and the applied configuration disagree, the applied configuration wins, and the runbook is corrected or flagged.

<situations_where_the_work_is_not_done>
- Applied without a reviewed plan, or reported as deployed from pipeline status alone.
- A stateful resource deleted or replaced, where rollback cannot restore the data.
- No rollback path, or one that has never been tried.
- The change made against the wrong state because of undetected drift.
- Blast radius left unstated.
- A secret, token, or account identifier printed into logs, diffs, or the report.
- An alert threshold widened or an exclusion added, in a way that would silence a real failure.
- Monitoring assumed rather than named: no metric, log, or check identified.
</situations_where_the_work_is_not_done>
