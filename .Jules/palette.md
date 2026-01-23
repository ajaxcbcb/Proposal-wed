# Palette's Journal

## 2025-05-20 - Interactive Calculator Accessibility
**Learning:** For calculator inputs with limits (min/max), merely clamping the value in JS is insufficient UX. Users need visual disablement (opacity/cursor) AND screen readers need `aria-live` feedback to understand why values stop changing.
**Action:** Always pair `Math.min/max` logic with `button.disabled` states and explicit `aria-live` announcements for the resulting state.
