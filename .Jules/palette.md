## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-05-23 - Constraint Communication
**Learning:** When buttons hit logic limits (min/max), visual disabling isn't enough. Using the `disabled` attribute prevents focus traps for keyboard users, and the live region acts as the "feedback" that the value has stopped changing.
**Action:** Always pair visual opacity with the `disabled` attribute and ensure live regions confirm the current state even when stuck.
