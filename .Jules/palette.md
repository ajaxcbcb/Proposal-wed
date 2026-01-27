## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-24 - Testing Disabled States with Playwright
**Learning:** Playwright's `click()` automatically waits for elements to be enabled. Verifying that a button *becomes* disabled requires asserting the state (e.g., `expect(loc).to_be_disabled()`) rather than trying to click it again, which causes a timeout.
**Action:** When testing limits, loop exactly N times to reach the limit, then assert the disabled state without clicking.
