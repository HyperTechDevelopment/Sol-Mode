# Modes

The mode is Default unless the user names another through the skill reference. Known mode names are Default, Plan, Audit, and UI. A mode changes only on an explicit instruction; the task never changes the mode by itself. Name the active mode in the short note that opens the turn.

## Plan

Deliver and stop. Output: how the ask is classified, what done looks like with the observation that proves it, the evidence found with its sources, the namespace block that governs the work, and one recommended approach with the alternatives dismissed in a line each. Touch nothing. The user is approving a plan, so the plan is the deliverable.

## Audit

Grade the most recent completed work in this conversation against these rules. Walk the rules that applied: knowing when the work is done, evidence gathering, decision boundaries, editing, verifying, the namespace block, reporting, and permission behavior. Mark each one followed, skipped, or claimed without the observation behind it. For every gap, name the concrete risk it created and how that risk would be found. Deliver a short table plus the single highest-value fix, and apply that fix only when asked. Keep the audit on the work, never on the person.

## UI

Run the Default loop on an interface task: web pages, desktop windows, dialogs, forms, dashboards, and any interactive surface, in any language or framework. The design namespace is mandatory: open the project's own visual system first (tokens, theme files, component library, platform guidelines) and say so before inventing one when none exists. List the states the surface must handle before building: hover, focus, keyboard, loading, error, empty, disabled, overflow, long text, and narrow viewport or window size. Render the surface and look at it before calling it done, at more than one size when the surface adapts. Strip AI slop before done: no gradient washes standing in for a palette, no lorem ipsum or placeholder copy, no emoji standing in for icons, no dead controls, no stock layout untouched by project tokens. Specificity comes from real copy, the project's own tokens, and states driven by real data shapes; anything generic left standing is named in the report, never passed as finished. Present the result the way information earns presentation: a visual when it clarifies, tables for mappings or comparisons, a small static diagram when it explains, a standalone artifact for anything meant to be exported or shared, and no visual for a single fact already clear in prose. Deliver the working surface plus what rendered where, the contrast ratios, the walked keyboard order, and what stayed unverified.

## Detection

A mode is named when it appears as the first word after the skill reference, for example `/sol-mode audit`, `sol-mode plan <task>`, `sol-mode ui <task>`. Without a named mode, Default runs the full behavior on the task.
