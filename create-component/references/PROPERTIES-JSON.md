# properties.json Reference

The `properties.json` file defines the UI controls users see in the Elements inspector when editing a component.

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

## Property Structure

Each property (control) has:

```json
{
  "title": "Display Label",
  "id": "propertyId",
  "controlType": {
    // control-specific options
  }
}
```

The `id` becomes the variable name in templates: `{{propertyId}}`

## Common UI Controls

### Text Input

```json
{
  "title": "Heading",
  "id": "heading",
  "text": {
    "default": "Enter text here"
  }
}
```

### Text Area

```json
{
  "title": "Description",
  "id": "description",
  "textArea": {
    "default": "Enter description..."
  }
}
```

### Input

A compact single-line input for short technical values (numbers, comma-separated lists, code-like strings).

```json
{
  "title": "Cubic Bezier",
  "id": "timingFunction",
  "format": "ease-[cubic-bezier({{value}})]",
  "input": {
    "default": "0.95,0.05,0.795,0.035",
    "subtitle": "x1, y1, x2, y2"
  }
}
```

### Number

```json
{
  "title": "Count",
  "id": "itemCount",
  "number": {
    "default": 3,
    "min": 1,
    "max": 10
  }
}
```

### Slider

```json
{
  "title": "Opacity",
  "id": "opacity",
  "slider": {
    "default": 100,
    "min": 0,
    "max": 100,
    "units": "%",
    "round": true
  }
}
```

### Switch (Toggle)

```json
{
  "title": "Show Border",
  "id": "showBorder",
  "switch": {
    "default": false
  }
}
```

### Select (Dropdown)

```json
{
  "title": "Size",
  "id": "size",
  "select": {
    "default": "medium",
    "items": [
      { "title": "Small", "value": "small" },
      { "title": "Medium", "value": "medium" },
      { "title": "Large", "value": "large" }
    ]
  }
}
```

### Segmented Control

```json
{
  "title": "Alignment",
  "id": "alignment",
  "segmented": {
    "default": "center",
    "items": [
      { "title": "Left", "value": "left" },
      { "title": "Center", "value": "center" },
      { "title": "Right", "value": "right" }
    ]
  }
}
```

Segmented items can use an SF Symbol `icon` instead of a `title`.

### Resource (Image/File Picker)

There is no `image` control — use `resource` for images and all other file types. Restrict accepted types with `accepts` (string) or `types` (array), e.g. `"resource": { "accepts": "svg" }`.

```json
{
  "title": "Hero Image",
  "id": "heroImage",
  "resource": {}
}
```

### Link

```json
{
  "title": "Button Link",
  "id": "buttonLink",
  "link": {}
}
```

### Collection

Binds a repeating set of items (e.g. tabs, slides, table columns). Note it uses `property` instead of `id`, and the item fields are defined in a nested `collections/<identifier>/properties.json` file using the same schema.

```json
{
  "title": "Tabs",
  "property": "tabs",
  "collection": {
    "identifier": "tabs"
  }
}
```

### Theme Color

Uses the theme's color palette. Specify color name and brightness level.

```json
{
  "title": "Button Color",
  "id": "buttonColor",
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

**With light and dark mode colors:**

```json
{
  "title": "Surface Color",
  "id": "surfaceColor",
  "themeColor": {
    "default": {
      "name": "surface",
      "brightness": 800,
      "darkName": "surface",
      "darkBrightness": 50
    }
  }
}
```

### Theme Font

Uses the theme's font families. Supports responsive breakpoints.

```json
{
  "title": "Headline Font",
  "id": "headlineFont",
  "themeFont": {
    "default": {
      "base": { "name": "heading" },
      "md": { "name": "display" }
    }
  }
}
```

Output: `font-heading md:font-display`

### Theme Text Style

Uses the theme's text size scale.

```json
{
  "title": "Heading Size",
  "id": "headingTextStyle",
  "themeTextStyle": {
    "default": {
      "base": { "name": "3xl" },
      "md": { "name": "5xl" }
    }
  }
}
```

### Theme Typography

Uses the theme's typography presets (e.g., article styles).

```json
{
  "title": "Article Style",
  "id": "articleStyle",
  "themeTypography": {
    "default": {
      "base": { "name": "article" },
      "md": { "name": "article-lg" }
    }
  }
}
```

### Theme Border Width

```json
{
  "title": "Card Border",
  "id": "cardBorderWidth",
  "themeBorderWidth": {
    "default": {
      "base": {
        "top": "1",
        "right": "1",
        "bottom": "1",
        "left": "1"
      }
    }
  }
}
```

### Theme Border Radius

Uses the theme's border radius scale.

```json
{
  "title": "Card Radius",
  "id": "cardRadius",
  "themeBorderRadius": {
    "default": {
      "base": {
        "topRight": "lg",
        "topLeft": "lg",
        "bottomRight": "lg",
        "bottomLeft": "lg"
      }
    }
  }
}
```

### Theme Shadow

Uses the theme's shadow scale.

```json
{
  "title": "Card Shadow",
  "id": "cardShadow",
  "themeShadow": {
    "default": {
      "name": "sm"
    }
  }
}
```

### Theme Spacing

For padding, margin, gap, and positioning. Uses the theme's spacing scale for consistency.

**Available modes:** `padding`, `margin`, `gap`, `transition`, `position`, `single`

```json
{
  "title": "Card Padding",
  "id": "cardPadding",
  "themeSpacing": {
    "mode": "padding",
    "default": {
      "base": {
        "left": "sm",
        "right": "sm",
        "top": "sm",
        "bottom": "sm"
      },
      "md": {
        "left": "lg",
        "right": "lg",
        "top": "lg",
        "bottom": "lg"
      }
    }
  }
}
```

**Single mode** - for a single spacing value:

```json
{
  "title": "Badge Offset",
  "id": "badgeOffsetTop",
  "format": "top-{{value}}",
  "themeSpacing": {
    "mode": "single",
    "default": {
      "base": {
        "value": "2"
      }
    }
  }
}
```

## Format Strings

Use `format` to transform values into CSS classes or other output:

```json
{
  "title": "Padding",
  "id": "padding",
  "format": "p-{{value}}",
  "slider": {
    "default": 4,
    "min": 0,
    "max": 12
  }
}
```

Output in template: `p-4`

## Grouping Properties

Display controls take an empty object `{}` — the text comes from the sibling `title` key, and no `id` is needed.

### UI Dividers

```json
{
  "divider": {}
}
```

### Headings

```json
{
  "title": "Advanced Options",
  "heading": {}
}
```

### Information Text

```json
{
  "title": "This setting affects all breakpoints.",
  "information": {}
}
```

## Conditional Visibility

Show/hide properties based on other values:

```json
{
  "title": "Custom Width",
  "id": "customWidth",
  "visible": "useCustomSize == true",
  "slider": {
    "default": 100
  }
}
```

## Responsive Properties

Enable per-breakpoint values:

```json
{
  "title": "Columns",
  "id": "columns",
  "responsive": true,
  "select": {
    "default": "3",
    "items": [
      { "title": "1", "value": "1" },
      { "title": "2", "value": "2" },
      { "title": "3", "value": "3" },
      { "title": "4", "value": "4" }
    ]
  }
}
```

## Complete Example

```json
{
  "groups": [
    {
      "title": "Content",
      "icon": "text.alignleft",
      "properties": [
        {
          "title": "Heading",
          "id": "heading",
          "text": { "default": "Welcome" }
        },
        {
          "title": "Subheading",
          "id": "subheading",
          "textArea": { "default": "Enter your message" }
        },
        { "divider": {} },
        {
          "title": "Show Button",
          "id": "showButton",
          "switch": { "default": true }
        },
        {
          "title": "Button Text",
          "id": "buttonText",
          "visible": "showButton == true",
          "text": { "default": "Learn More" }
        }
      ]
    },
    {
      "title": "Style",
      "icon": "paintbrush",
      "properties": [
        {
          "title": "Background",
          "id": "bgColor",
          "format": "bg-{{value}}",
          "themeColor": {
            "default": { "name": "brand", "brightness": 500 }
          }
        },
        {
          "title": "Text Color",
          "id": "textColor",
          "format": "text-{{value}}",
          "themeColor": {
            "default": { "name": "brand", "brightness": 50 }
          }
        }
      ]
    }
  ]
}
```
