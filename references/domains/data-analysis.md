# Namespace: data

Applies to metrics, queries, datasets, conclusions drawn from data, charts, and dashboards. A chart whose correctness depends on the numbers routes here and to `design-ux.md`. A chart whose layout alone is in question routes to `design-ux.md`.

## Rules for getting this work done

- Open the data before writing a query. Record columns, types, row count, and date range first.
- Reach for the written definition of every metric reported: denominator, population, window, business rule.
- When a metric is defined only in conversation, say that before reporting a number.
- Reach first for the query, notebook, or job that produces these numbers today, and for prior work on the same question.
- Recompute every reported figure a second way when a second path exists.
- Reconcile: say whether the parts sum to the whole, and name every deliberate exclusion.
- Report the base beside every percentage change, and the distribution beside every average.
- Confirm units, currency, and time zone, and whether the period boundary is inclusive.
- State the effect size, not the direction alone. With a small sample, give the range.
- Stamp a recalled rate or benchmark as memory, unverified, or open its source.

## Decision boundary

When the records and a summary disagree, the records win. When a metric definition and a prior report disagree, the definition wins, and the disagreement is itself a finding to report rather than a number to reconcile quietly. When a chart and the table it came from disagree, the table wins.

<situations_where_the_work_is_not_done>
- A window, filter, or segment chosen because the result looks clean.
- A percentage change on a small base, reported without the base.
- An average over a skewed or bimodal distribution, presented as typical.
- A metric definition that changed mid-period and was not noticed.
- A correlation reported as a cause.
- A chart that does not match the table beside it, or an axis starting above zero without a stated reason.
- More decimals than the measurement supports.
- A query that ran successfully and was never checked against anything.
</situations_where_the_work_is_not_done>

## Special cases

- Silent data loss: search nulls, sentinel values, and rows dropped by a join before concluding a trend.
- Survivorship: check what left the dataset during the period, not only what entered it.
