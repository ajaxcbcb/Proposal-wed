## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Canvas Accessibility
**Learning:** HTML5 Canvas elements are invisible to screen readers by default, leaving users missing context for critical data visualizations.
**Action:** Dynamically inject `role="img"` and descriptive `aria-label` attributes (using data from the drawing function) to make charts accessible.
