## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Visual Feedback for Limits
**Learning:** Disabled buttons in minimal UI often lack sufficient contrast shift to be obvious to low-vision users.
**Action:** Pair `disabled` attribute with `opacity-50` class to reinforce the state visually while the attribute handles functionality.
