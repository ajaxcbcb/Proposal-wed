## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Skip Links are Essential
**Learning:** Single-page apps or long landing pages often trap keyboard users in navigation menus. A "Skip to content" link is a low-effort, high-impact a11y win.
**Action:** Always verify `tabindex="-1"` is on the target container (e.g., `<main id="content" tabindex="-1">`) so focus lands correctly.
