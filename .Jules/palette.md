## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Canvas Data Accessibility
**Learning:** HTML5 Canvas elements are invisible to screen readers. Complex visualizations (charts, diagrams) must provide alternative text descriptions that convey the *insight*, not just "Chart".
**Action:** Add `role="img"` and dynamic `aria-label` attributes to canvas elements, summarizing the data trend or key takeaway (e.g., "Competitive map showing us in the top-right quadrant...").
