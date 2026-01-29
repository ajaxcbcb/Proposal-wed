## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Limit Indication
**Learning:** When using icon-only incrementers, the "end of range" state can be ambiguous.
**Action:** Use `disabled` attribute combined with `opacity-50` class to clearly signal upper/lower bounds are reached without hiding the controls.
