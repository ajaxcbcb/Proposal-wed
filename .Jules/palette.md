## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2026-01-15 - Disabled States for Limits
**Learning:** Preventing value changes at limits (min/max) without disabling the control confuses users, who may think the click didn't register.
**Action:** Always programmatically set `disabled` and reduce opacity (e.g., `0.3`) on buttons when their limit is reached.
