## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-02-18 - Disabled State Visuals
**Learning:** Native `disabled` attributes on buttons are insufficient for visual feedback in this design system. Users need clearer cues when limits (min/max) are reached.
**Action:** Always pair `disabled` attribute with `.opacity-50` class for disabled states.
