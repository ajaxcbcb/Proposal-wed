## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-05-24 - Counter Limits UX
**Learning:** Users often click counter buttons repeatedly at limits if there's no visual feedback.
**Action:** Always pair the `disabled` attribute with a visual style (like `opacity-50`) to clearly indicate min/max boundaries have been reached.
