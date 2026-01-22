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
  "textarea": {
    "default": "Enter description..."
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
    "options": ["small", "medium", "large"]
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
    "options": [
      { "title": "Left", "value": "left" },
      { "title": "Center", "value": "center" },
      { "title": "Right", "value": "right" }
    ]
  }
}
```

### Image

```json
{
  "title": "Hero Image",
  "id": "heroImage",
  "image": {}
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

### Theme Color

```json
{
  "title": "Background",
  "id": "bgColor",
  "themeColor": {
    "default": "background"
  }
}
```

### Theme Font

```json
{
  "title": "Heading Font",
  "id": "headingFont",
  "themeFont": {
    "default": "heading"
  }
}
```

### Theme Spacing

```json
{
  "title": "Padding",
  "id": "padding",
  "themeSpacing": {
    "default": "md"
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

### UI Dividers

```json
{
  "divider": true
}
```

### Headings

```json
{
  "heading": "Advanced Options"
}
```

### Information Text

```json
{
  "information": "This setting affects all breakpoints."
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
    "options": ["1", "2", "3", "4"]
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
          "textarea": { "default": "Enter your message" }
        },
        { "divider": true },
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
          "themeColor": { "default": "primary" }
        },
        {
          "title": "Text Color",
          "id": "textColor",
          "themeColor": { "default": "on-primary" }
        }
      ]
    }
  ]
}
```
