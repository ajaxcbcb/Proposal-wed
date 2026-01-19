## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-05-27 - Disabled States for Interactive Controls
**Learning:** Users can get confused when interactive controls (like counters) reach their limits without visual feedback.
**Action:** When a limit is reached, set the `disabled` attribute and add `opacity-50` class to the button to clearly indicate the boundary.
