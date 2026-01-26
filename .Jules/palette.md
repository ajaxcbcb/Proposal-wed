## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-10-26 - Button Limits & Feedback
**Learning:** Interactive counters with min/max limits need both visual (opacity) and programmatic (disabled attribute) feedback. Without this, users keep clicking with no effect, wondering if the UI is broken.
**Action:** Always toggle `disabled` attribute AND visual classes (like `opacity-50`) when limits are reached.
