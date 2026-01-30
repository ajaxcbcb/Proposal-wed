## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-23 - Disabled States for Custom Buttons
**Learning:** Custom buttons (like `.btn-action`) may not have built-in `:disabled` styles, confusing users when limits are reached.
**Action:** Always pair the `disabled` attribute with the `opacity-50` utility class to ensure visual feedback.
