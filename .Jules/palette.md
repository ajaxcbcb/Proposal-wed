## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2025-02-05 - Boundary Feedback on Interactive Controls
**Learning:** Users clicking repeatedly (e.g., trying to go below 0 bookings) need immediate feedback that they've hit a limit. Visual dimming (`opacity-50`) plus semantic `disabled` attribute prevents frustration.
**Action:** Always pair functional limits with `disabled` attribute and visual degradation (opacity) on control buttons.
