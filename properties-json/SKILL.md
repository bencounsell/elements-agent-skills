---
name: properties-json
description: Define UI controls for RapidWeaver Elements components using properties.json. Use when creating inspector panels with text inputs, sliders, switches, dropdowns, theme colors, spacing controls, and conditional visibility.
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---

# Elements properties.json

This skill helps you write `properties.json` files that define the UI controls users see in the Elements inspector when editing a component.

## When to Use

- Creating UI controls for component settings
- Building inspector panels with grouped controls
- Adding conditional visibility between controls
- Integrating with theme colors, fonts, and spacing
- Outputting Tailwind CSS classes from control values
- Enabling responsive (per-breakpoint) settings

## Component Lifecycle

```
properties.json → hooks.js → templates
```

1. **Properties** define UI controls and capture user input
2. **Hooks** process and transform those values
3. **Templates** render the final HTML output

## Basic Structure

```json
{
  "groups": [
    {
      "title": "Group Name",
      "icon": "sf-symbol-name",
      "properties": [
        // UI controls go here
      ]
    }
  ]
}
```

## Common Properties

Every control supports these properties:

| Property | Description |
|----------|-------------|
| `title` | Human-friendly label in the inspector |
| `id` | Unique key for templates and conditional logic |
| `format` | Transform value before output (e.g., `"p-{{value}}"`) |
| `visible` | Conditional show/hide expression |
| `enabled` | Conditional enable/disable expression |
| `responsive` | Per-breakpoint values (default: `true`) |

## Step-by-Step Instructions

### 1. Create Groups

Organize controls into logical groups with icons:

```json
{
  "groups": [
    {
      "title": "Content",
      "icon": "textformat",
      "properties": []
    },
    {
      "title": "Style",
      "icon": "paintbrush",
      "properties": []
    }
  ]
}
```

> **Note:** Icons use SF Symbols. See the [SF Symbols app](https://developer.apple.com/sf-symbols/) for available icons.

### 2. Add Basic Controls

```json
{
  "title": "Headline",
  "id": "headline",
  "text": {
    "default": "Welcome"
  }
}
```

**UI Controls:**

| Control | Use Case |
|---------|----------|
| `text` | Single-line text input |
| `textarea` | Multi-line text input |
| `number` | Numeric input with optional min/max |
| `slider` | Range selection with visual slider |
| `switch` | Boolean toggle |
| `select` | Dropdown menu |
| `segmented` | Button group for options |
| `resource` | Resource picker (images, videos, PDFs) |
| `link` | URL/page link picker |

**Theme Controls:**

| Control | Use Case |
|---------|----------|
| `themeColor` | Color picker from theme palette |
| `themeSpacing` | Padding, margin, or gap from theme scale |
| `themeFont` | Font family from theme fonts |
| `themeTextStyle` | Text size from theme type scale |
| `themeTypography` | Typography preset (article styles) |
| `themeBorderWidth` | Border width with individual sides |
| `themeBorderRadius` | Border radius with individual corners |
| `themeShadow` | Box/drop/text shadow from theme |

### 3. Use Format Strings

Transform values into Tailwind classes:

```json
{
  "title": "Padding",
  "id": "padding",
  "format": "p-{{value}}",
  "slider": {
    "default": 4,
    "min": 0,
    "max": 12,
    "round": true
  }
}
```

Output in template: `{{padding}}` → `p-4`

For arbitrary values:

```json
{
  "title": "Opacity",
  "id": "overlayOpacity",
  "format": "opacity-[{{value}}%]",
  "slider": {
    "default": 70,
    "min": 0,
    "max": 100
  }
}
```

Output: `opacity-[70%]`

### 4. Add Conditional Visibility

Show controls based on other values:

```json
{
  "title": "Show Overlay",
  "id": "showOverlay",
  "switch": {
    "default": false
  }
},
{
  "title": "Overlay Color",
  "id": "overlayColor",
  "visible": "showOverlay == true",
  "themeColor": {
    "default": { "name": "surface", "brightness": 900 }
  }
}
```

Supported operators: `==`, `!=`, `>`, `<`, `>=`, `<=`, `&&`, `||`, `matches` (regex)

### 5. Use Theme Controls

Integrate with the theme's design system:

```json
{
  "title": "Background",
  "id": "bgColor",
  "format": "bg-{{value}}",
  "themeColor": {
    "default": {
      "name": "brand",
      "brightness": 500
    }
  }
}
```

Output: `bg-brand-500`

### 6. Enable Responsive Values

By default, all controls are responsive. Users can set different values per breakpoint:

```json
{
  "title": "Columns",
  "id": "columns",
  "select": {
    "default": "3",
    "items": [
      { "title": "1 Column", "value": "1" },
      { "title": "2 Columns", "value": "2" },
      { "title": "3 Columns", "value": "3" }
    ]
  }
}
```

Output when customized: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

Disable with `"responsive": false` for non-visual settings.

## Examples

For complete component examples, see [EXAMPLES.md](references/EXAMPLES.md). Examples include:

- **Card Component** - Content, media, and styling with conditional button
- **Hero Section** - Background style toggle with overlay controls
- **Button with Hover States** - State toggle pattern for hover styles
- **Pricing Table** - Multiple conditional sections with information elements

## UI Elements

Non-interactive elements for organizing the inspector.

### divider

Visual separator line between controls:

```json
{ "divider": {} }
```

### heading

Section heading within a group to label related controls:

```json
{ "heading": "Advanced Settings" }
```

Or with object syntax:

```json
{ "heading": {}, "title": "Advanced Settings" }
```

### information

Help text or instructions for users:

```json
{
  "information": {},
  "title": "This setting affects all breakpoints."
}
```

Can be combined with visibility for contextual help:

```json
{
  "information": {},
  "title": "Enter a valid coupon code (e.g., SAVE10)",
  "visible": "couponCode matches /^SAVE[0-9]{2}$/"
}
```

## Guidelines

1. **Group logically** - Organize related controls together (Content, Style, Layout)
2. **Use meaningful IDs** - `heroHeadline` not `text1`; IDs become template variables
3. **Provide defaults** - Always set sensible default values
4. **Use visibility wisely** - Hide advanced options behind toggles
5. **Leverage theme controls** - Use `themeColor`, `themeSpacing`, etc. for consistency
6. **Disable responsive when needed** - Use `"responsive": false` for IDs, CSS classes, and non-visual settings
7. **Add helpful labels** - Use `information` to explain complex settings

## Reference Documentation

For detailed information, see:
- [GENERAL-STRUCTURE.md](references/GENERAL-STRUCTURE.md) - Common properties for all controls
- [UI-CONTROLS.md](references/UI-CONTROLS.md) - Standard input controls
- [THEME-CONTROLS.md](references/THEME-CONTROLS.md) - Theme integration controls
- [EXAMPLES.md](references/EXAMPLES.md) - Complete component examples
