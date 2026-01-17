## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-02-18 - Stress Test Accessibility
**Learning:** Adding `aria-live` summary to calculators significantly improves screen reader experience, but verifying disabled button states with Playwright requires handling timeouts or state checks since `click()` waits for enabled state.
**Action:** When testing disabled buttons, check attributes directly or use try/except blocks for timeouts, and combine with visual disabled states for better UX.
