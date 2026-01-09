## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Canvas Accessibility
**Learning:** HTML5 Canvas elements are invisible to screen readers by default. Visual charts must have semantic roles and descriptive labels injected dynamically to be accessible.
**Action:** Add `role="img"` and descriptive `aria-label` attributes to canvas elements via JavaScript when rendering charts.
