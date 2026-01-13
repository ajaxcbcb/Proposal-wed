## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Interactive Control Limits
**Learning:** Interactive controls with min/max limits should visually disable buttons when limits are reached. This prevents user frustration (clicking "minus" at 0 and nothing happening) and provides clear affordance of the boundary.
**Action:** Programmatically set the `disabled` attribute on buttons when the limit is reached.
