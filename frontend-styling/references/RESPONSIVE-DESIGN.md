# Responsive Design Reference

Patterns for building responsive Elements components that adapt across screen sizes.

## Breakpoint System

Elements uses a mobile-first responsive design approach with these breakpoints:

| Prefix | Min Width | Typical Devices |
|--------|-----------|-----------------|
| (none) | 0px | Mobile phones (base/default) |
| `sm:` | 640px | Large phones, small tablets |
| `md:` | 768px | Tablets |
| `lg:` | 1024px | Laptops, desktops |
| `xl:` | 1280px | Large desktops |
| `2xl:` | 1536px | Extra large screens |

### How It Works

1. **Base styles** - No prefix, applies to all screen sizes.
2. **Breakpoint prefix** - Applies only at that breakpoint and above (e.g., `md:text-3xl`).
3. **Cascade up** - Larger breakpoints override smaller ones.

```html
<!-- padding: 4 on mobile, 6 on tablet, 8 on desktop -->
<div class="p-4 md:p-6 lg:p-8">
  <h1 class="text-xl md:text-3xl lg:text-5xl">Responsive Heading</h1>
</div>
```

## Responsive Properties

### Default Behavior (responsive: true)

All properties, with the exception of `themeColor`, in `properties.json` are responsive by default. When users customize per-breakpoint, Elements automatically generates the responsive class string.

```json
{
  "title": "Columns",
  "id": "columns",
  "format": "grid-cols-{{value}}",
  "select": {
    "default": "1",
    "items": [
      { "title": "1", "value": "1" },
      { "title": "2", "value": "2" },
      { "title": "3", "value": "3" }
    ]
  }
}
```

**Output:** `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

### Disabling Responsive

Disable with `"responsive": false` for properties that shouldn't change per breakpoint, such as HTML IDs, attributes, or non-visual strings.

```json
{
  "title": "Element ID",
  "id": "elementId",
  "responsive": false,
  "text": { "default": "" }
}
```

### Multi-Value Responsive

Properties with multiple classes (e.g., position) correctly prefix every class in the value:

```json
{
  "id": "position",
  "select": {
    "default": "top-0 left-0",
    "items": [
      {
        "title": "Top Left",
        "value": "top-0 left-0"
      },
      {
        "title": "Center",
        "value": "top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
      }
    ]
  }
}
```

**Output (with Center selected at md):** `top-0 left-0 md:top-1/2 md:left-1/2 md:-translate-x-1/2 md:-translate-y-1/2`

## Using rw.responsiveProps

Use `rw.responsiveProps` in `hooks.js` for **Custom CSS** (media queries, CSS variables) or **Non-class responsive data**. For Tailwind classes, use `format` in `properties.json` instead.

### Structure

```javascript
rw.responsiveProps = {
  cardWidth: {
    base: "280",
    md: "350",
    lg: "400"
  }
};
```

### Custom CSS Example (Media Queries)

```javascript
const transformHook = (rw) => {
  const breakpoints = rw.getBreakpoints();
  const { cardWidth } = rw.responsiveProps;
  const uniqueId = rw.props.uniqueId;

  const cssRules = Object.entries(cardWidth)
    .map(([bp, width]) => {
      const breakpoint = breakpoints.find(b => b.name === bp);
      const rule = `#card-${uniqueId} { width: ${width}px; }`;

      return bp === 'base'
        ? rule
        : `@media (min-width: ${breakpoint.minWidth}px) { ${rule} }`;
    })
    .join('\n');

  rw.setProps({ customStyles: `<style>${cssRules}</style>` });
};
```

### CSS Variables Example

```javascript
const transformHook = (rw) => {
  const breakpoints = rw.getBreakpoints();
  const { columnGap } = rw.responsiveProps;
  const uniqueId = rw.props.uniqueId;

  const cssRules = breakpoints
    .filter(bp => columnGap[bp.name])
    .map(bp => {
      const rule = `#grid-${uniqueId} { --column-gap: ${columnGap[bp.name]}px; }`;
      return bp.name === 'base' ? rule : `@media (min-width: ${bp.minWidth}px) { ${rule} }`;
    })
    .join('\n');

  rw.setProps({ gridStyles: `<style>${cssRules}</style>` });
};
```

## Using rw.getBreakpoints()

Returns the theme's breakpoint configuration:

```javascript
const transformHook = (rw) => {
  const breakpoints = rw.getBreakpoints();
  // [{ name: "base", minWidth: 0 }, { name: "sm", minWidth: 640 }, ...]

  rw.setProps({ breakpoints });
};
```

## Common Responsive Patterns

### Theme Controls

Theme controls automatically handle responsive output.

```json
{
  "themeTextStyle": {
    "default": { "base": { "name": "lg" }, "md": { "name": "xl" } }
  },
  "themeSpacing": {
    "mode": "padding",
    "default": { "base": { "top": "md" }, "md": { "top": "xl" } }
  },
  "themeShadow": {
    "default": { "base": { "name": "sm" }, "lg": { "name": "lg" } }
  },
  "themeBorderRadius": {
    "default": {
      "base": {
        "topLeft": "Default",
        "topRight": "Default",
        "bottomLeft": "Default",
        "bottomRight": "Default",
      },
      "lg": {
        "topLeft": "md",
        "topRight": "md",
        "bottomLeft": "md",
        "bottomRight": "md",
      }
    }
  }
}
```

### Responsive Layout & Visibility

```json
{
  "id": "layout",
  "select": {
    "default": "flex-col",
    "items": [
      { "title": "Stacked", "value": "flex-col" },
      { "title": "Side by Side", "value": "flex-row" }
    ]
  }
}
```

**Typical use:** `flex-col md:flex-row` (stacked on mobile, side-by-side on tablet).

```html
<!-- Hidden on mobile, visible on medium+ -->
<div class="hidden md:block">Desktop only</div>

<!-- Visible on mobile, hidden on medium+ -->
<div class="block md:hidden">Mobile only</div>
```

## Best Practices

1.  **Mobile-First**: Design for the base (mobile) breakpoint first, then add overrides for larger screens.
2.  **Logical Progression**: Values should generally increase or decrease logically across breakpoints (e.g., `text-sm md:text-base lg:text-lg`).
3.  **Don't Over-Customize**: Only set values for breakpoints where the design actually needs to change.
4.  **Handle Edge Cases**: When using `rw.responsiveProps` for custom CSS, always provide a fallback for missing breakpoints.

```javascript
// Graceful fallback for missing breakpoints
const baseValue = scrollSpeed.base || '100';
const value = scrollSpeed[bp.name] || baseValue;
```

5.  **Test Thoroughly**: Verify the component at each major breakpoint (320px, 640px, 768px, 1024px, 1280px).
