## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-10-24 - Counter Button Constraints
**Learning:** Users often click limits repeatedly without realizing they've hit the max/min.
**Action:** Visually dim buttons (`opacity-50`) and set the `disabled` attribute when limits are reached to provide clear constraints.
