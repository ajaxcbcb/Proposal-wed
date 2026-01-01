## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-23 - Dynamic Canvas Accessibility
**Learning:** Data-driven canvas charts are invisible to screen readers. For dynamic charts, static HTML fallbacks aren't enough.
**Action:** Inject `role="img"` and data-aware `aria-label` strings (e.g., "Bar chart showing X is lower than Y") during the JS render phase.
