## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Live Region Implementation
**Learning:** When adding `aria-live` feedback to existing dense UIs, inserting visible text can break layout.
**Action:** Use the `.visually-hidden` utility class on the live region container to provide screen reader updates without affecting visual design.
