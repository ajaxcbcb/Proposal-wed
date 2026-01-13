## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-23 - Canvas Accessibility
**Learning:** Dynamic canvas charts need JS-injected ARIA labels because their content is rendered from external JSON data, making static HTML attributes insufficient.
**Action:** Always inject `role="img"` and `aria-label` inside the rendering function using the same data source as the visual chart.
