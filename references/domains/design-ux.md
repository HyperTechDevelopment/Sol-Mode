# Namespace: design

Applies when the deliverable is seen or interacted with: components, pages, layouts, forms, dashboards, charts, decks, and formatted terminal output. These rules are MUST rules for those deliverables, and they do not change the loop.

## Rules for getting this work done

- Open the project's own visual system first (tokens, theme files, global styles, brand documentation), then the neighboring surfaces, so the new work belongs to the same family. When no system exists, say so before inventing one.
- List the states the surface must handle before building: hover, focus, keyboard, loading, error, empty, disabled, overflow, long text, narrow viewport.
- Render the surface and look at it before calling it done, at more than one width when responsive. Unrendered visual work is unverified work.
- Search the touched files for raw hex values, raw pixel values, and hardcoded font stacks sitting beside a token system.
- Compute contrast for every new foreground and background pair, and report each ratio beside the pair it belongs to.
- Walk the keyboard path: visible focus, sane tab order, labeled controls, and report the walked order.
- Exercise the real API path when the surface calls one, or state that only the visual layer was verified.
- Strip generic AI markers before done: gradient washes, lorem ipsum, emoji-as-icon, dead controls. Specificity comes from real copy, project tokens, and states driven by real data shapes.
- Name what was rendered, at which widths, the contrast ratios, the walked keyboard order, and what was not rendered.

## Decision boundary

An explicit instruction beats the token system for the surface, with the conflict surfaced. Tokens beat a referenced design file. A call for modern or bold never overrides tokens silently. When the harness cannot render the surface, say so and mark the result unverified instead of implying it was seen.

<situations_where_the_work_is_not_done>
- A surface reported as done that has never been rendered.
- Hardcoded colors, spacing, radii, or fonts beside an existing token system.
- Accessibility reported without computed contrast, labeled controls, and a walked keyboard path.
- Only the happy path delivered, with the missing states unmentioned.
- A surface that visibly does not belong to its neighbors, left unflagged.
- Placeholders, dummy assets, dead links, or missing requested assets left in finished work.
- Generic AI markers left standing: gradient washes, placeholder copy, emoji icons, dead controls, or a stock layout untouched by project tokens.
- A visual detail reported as verified when it was inferred from the code.
</situations_where_the_work_is_not_done>

## Special cases

- Charts: correct data first, then layout. The chart namespace for correctness is `data-analysis.md`.
- Decks and documents: the rendered artifact is what gets verified, not the source file.
- Auth surfaces: enumerate the non-happy outcomes beyond invalid input, such as locked, unconfirmed, or offline, and name which ones the work covers.
