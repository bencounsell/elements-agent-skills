---
name: frontend-styling
description: Style RapidWeaver Elements components using Tailwind CSS 3 and the theme system. Use when applying colors, spacing, typography, borders, shadows, responsive layouts, or generating dynamic class strings.
license: MIT
metadata:
  author: Elements Platform
  version: "1.2"
---

# Elements Frontend Styling

This skill covers styling Elements components using **Tailwind CSS 3** utilities and the integrated theme system.

## Core Styling Concepts

### Utility Composition
Elements uses Tailwind CSS 3. Style components by composing utility classes in your templates:

```html
<div class="bg-brand-500 text-white p-4 rounded-lg shadow-md">
  Content
</div>
```

### Property-to-Class Mapping
In `properties.json`, use `format` to transform user-selected values into Tailwind classes:

```json
{
  "id": "padding",
  "format": "p-{{value}}",
  "slider": { "default": 4, "min": 0, "max": 12 }
}
```

### Theme Integration
Theme controls connect to the Elements Theme Studio. They automatically handle color names, spacing scales, and responsive output.

| Control | Purpose | Example Output |
|---------|---------|----------------|
| `themeColor` | Palette colors | `bg-brand-500 dark:bg-brand-400` |
| `themeSpacing` | Padding/Margin/Gap/Postition/Translate | `pt-md pr-lg pb-md pl-lg` |
| `themeTextStyle` | Font size/line height | `text-2xl` |
| `themeFont` | Font family | `font-heading` |
| `themeShadow` | Box shadows | `shadow-md` |
| `themeBorderRadius` | Corner radius | `rounded-lg` |
| `themeBorderWidth` | Border with | `border-tl-2 border-tr-2 border-bl-2 border-br-2` |
| `themeTypography` | Typography | `prose` |

## Responsive Design

### Mobile-First Breakpoints
Elements uses a mobile-first approach. Styles without a prefix apply to all screens; prefixed styles override them at specific widths.

| Prefix | Min Width |
|--------|-----------|
| (none) | 0px |
| `sm:` | 640px |
| `md:` | 768px |
| `lg:` | 1024px |
| `xl:` | 1280px |

### Responsive Properties
All properties (except `themeColor`) are responsive by default. Users can set different values per breakpoint, and Elements generates the combined class string:

**Input (at md):** `grid-cols-1 md:grid-cols-2`

## Dynamic Classes in hooks.js

Use `hooks.js` to build complex class strings from multiple properties.

### The Array Pattern
Always use the array-filter-join pattern for clean, conditional class strings:

```javascript
const transformHook = (rw) => {
  const { size, isActive, variant } = rw.props;

  const classes = [
    'base-component',
    `size-${size}`,
    isActive && 'is-active',
    variant === 'primary' ? 'bg-brand-500' : 'bg-surface-100'
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

### Responsive Logic in Hooks
Use `rw.responsiveProps` when you need to access the per-breakpoint values for non-Tailwind logic (e.g., custom CSS or JS calculations).

```javascript
const { columns } = rw.responsiveProps;
// columns = { base: "1", md: "2" }
```

## Guidelines

1. **Prefer Theme Controls**: Use `themeColor`, `themeSpacing`, etc., instead of hardcoded Tailwind values to ensure the component respects user theme choices.
2. **Use Format Strings**: Let `properties.json` handle simple class generation via `format`.
3. **Array Pattern**: Always use `.filter(Boolean).join(' ')` in hooks to avoid extra spaces or "false" strings in HTML.
4. **Responsive Defaults**: Keep `responsive: true` (default) for visual styles; set `responsive: false` for IDs, attributes, or state toggles.
5. **Dark Mode**: `themeColor` automatically generates `dark:` variants based on the theme configuration.

## Reference Documentation
- [CLASS-GENERATION.md](references/CLASS-GENERATION.md) - Advanced hook patterns
- [THEME-INTEGRATION.md](references/THEME-INTEGRATION.md) - Full theme control reference
- [RESPONSIVE-DESIGN.md](references/RESPONSIVE-DESIGN.md) - Deep dive into responsive logic
