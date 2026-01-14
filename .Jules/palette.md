## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Custom Button Disabled States
**Learning:** Custom button classes (like `.btn-action`) often lack default `:disabled` styles, leaving users confused when limits are reached.
**Action:** Explicitly set `opacity: 0.5` (or similar) alongside the `disabled` attribute to ensure visual affordance matches functional state.
