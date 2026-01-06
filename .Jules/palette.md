## 2024-05-23 - Interactive Calculator Accessibility
**Learning:** Interactive calculators often update visual numbers without announcing changes to screen readers. This leaves keyboard/SR users blindly clicking buttons without feedback.
**Action:** Use `aria-live="polite"` regions with summary sentences (e.g., "Net profit: RM 1,000") to confirm updates.

## 2024-05-23 - Accessibility: Skip Links & Bootstrap
**Learning:** Bootstrap 5's `visually-hidden-focusable` class is the standard way to implement accessible skip links that remain hidden until focused. It eliminates the need for custom CSS for off-screen positioning.
**Action:** When implementing keyboard navigation aids in Bootstrap-based projects, prioritize `visually-hidden-focusable` over custom CSS implementations. Ensure the target container (e.g., `<main>`) has `tabindex="-1"` to receive focus programmatically.
