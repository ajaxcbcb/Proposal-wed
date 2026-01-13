## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Canvas Accessibility
**Learning:** HTML5 Canvas elements are invisible to screen readers unless explicitly given a `role="img"` and a descriptive `aria-label` or fallback content.
**Action:** When using Canvas for charts, dynamically inject accessibility attributes that summarize the visual data (e.g., "Scatter plot showing price vs reliability").
