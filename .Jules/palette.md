## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-05-24 - Interactive Controls Limits
**Learning:** Users need clear signals when they hit a min/max limit. Just stopping the counter isn't enough.
**Action:** Visually disable the button (opacity/pointer-events) AND use the `disabled` attribute to communicate the state programmatically.
