## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-23 - Skip Link Implementation in Static/Bootstrap Context
**Learning:** For static sites using Bootstrap 5, the most robust "Skip to content" pattern combines Bootstrap's `.visually-hidden-focusable` class on the link with `tabindex="-1"` on the target container (e.g., `<main>`). This ensures focus is reliably transferred and the link only appears when needed.
**Action:** Always check target container focusability when implementing skip links.
