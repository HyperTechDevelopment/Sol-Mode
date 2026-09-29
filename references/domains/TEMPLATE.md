# Namespace template

Every file in this folder is a namespace block for one domain, written in the same shape as the tool namespaces the source prompt uses. A namespace block changes the nouns, never the loop: it says what work belongs here, which rules govern it, where the boundary of correct work sits, and which situations mean the work is not done.

## Namespace index

- `design-ux.md` - visual and interactive surfaces
- `data-analysis.md` - metrics, queries, datasets, charts
- `devops.md` - infrastructure, pipelines, deploys, monitoring
- `finance.md` - statements, budgets, forecasts, reconciliation
- `legal-compliance.md` - regulation, policy, contracts, privacy
- `marketing.md` - campaigns, copy, positioning, brand
- `business-ops.md` - processes, procedures, operations, vendors
- `research.md` - literature, market, due diligence, investigations

Coding is the default and has no namespace block. Medical and clinical work has none on purpose: it needs qualified human review, so say that instead of applying rules from here.

## Required shape

1. Title as `# Namespace: <name>`.
2. A short paragraph naming the deliverables that route here, in the imperative.
3. `## Rules for getting this work done` - the rules that govern the work, as one-line directives. These are the load-bearing part.
4. `## Decision boundary` - which source wins when sources disagree, stated in the source's cadence: when X and Y disagree, X wins.
5. A `<situations_where_the_work_is_not_done>` block listing the conditions that mean the work cannot be reported as finished.
6. `## Special cases` - optional, for the exceptions and the conflicts that override the rest.

## Writing rules

- One line per rule. A rule that needs two sentences usually hides two rules.
- Use MUST and Do not for the hard lines, the way the source does.
- Name a concrete artifact: a file, a schema, a report, a command, a registry.
- Avoid second person, em dashes, and tables. Keep each block under about 350 words.
