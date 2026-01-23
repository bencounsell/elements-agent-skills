# UI Controls Reference

Standard input controls for `properties.json` files. These create interactive UI elements in the Elements inspector.

## Text Controls

### text

Single-line text input.

```json
{
  "title": "Headline",
  "id": "headline",
  "text": {
    "default": "Welcome to our site"
  }
}
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | string | Initial value |
| `subtitle` | string | Help text below the input |

With subtitle:

```json
{
  "title": "Custom Class",
  "id": "customClass",
  "text": {
    "default": "",
    "subtitle": "Add custom Tailwind classes"
  }
}
```

### textarea

Multi-line text input.

```json
{
  "title": "Description",
  "id": "description",
  "textarea": {
    "default": "Enter a description..."
  }
}
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | string | Initial value |

## Numeric Controls

### number

Numeric input with optional constraints.

```json
{
  "title": "Item Count",
  "id": "itemCount",
  "number": {
    "default": 3,
    "min": 1,
    "max": 10
  }
}
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | number | Initial value |
| `min` | number | Minimum allowed value |
| `max` | number | Maximum allowed value |
| `subtitle` | string | Help text (e.g., "In pixels") |

With subtitle:

```json
{
  "title": "Border Width",
  "id": "borderWidth",
  "format": "border-[{{value}}px]",
  "number": {
    "default": 1,
    "min": 0,
    "max": 10,
    "subtitle": "In pixels"
  }
}
```

### slider

Visual range slider.

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

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | number | Initial value |
| `min` | number | Minimum value |
| `max` | number | Maximum value |
| `units` | string | Display unit (e.g., "%", "px", "vh") |
| `round` | boolean | Round to whole numbers |
| `snap` | boolean | Snap to discrete values |
| `items` | array | Discrete value options (see below) |

#### Slider with Discrete Values

Use `items` for named steps instead of a continuous range:

```json
{
  "title": "Font Weight",
  "id": "fontWeight",
  "format": "font-[{{value}}]",
  "slider": {
    "default": "400",
    "items": [
      { "value": "100", "title": "Thin" },
      { "value": "200", "title": "Extra Light" },
      { "value": "300", "title": "Light" },
      { "value": "400", "title": "Normal" },
      { "value": "500", "title": "Medium" },
      { "value": "600", "title": "Semi Bold" },
      { "value": "700", "title": "Bold" },
      { "value": "800", "title": "Extra Bold" },
      { "value": "900", "title": "Black" }
    ]
  }
}
```

```json
{
  "title": "Letter Spacing",
  "id": "letterSpacing",
  "format": "tracking-{{value}}",
  "slider": {
    "default": "normal",
    "items": [
      { "value": "tighter", "title": "Tighter" },
      { "value": "tight", "title": "Tight" },
      { "value": "normal", "title": "Normal" },
      { "value": "wide", "title": "Wide" },
      { "value": "wider", "title": "Wider" },
      { "value": "widest", "title": "Widest" }
    ]
  }
}
```

## Toggle Controls

### switch

Boolean toggle (on/off).

```json
{
  "title": "Show Border",
  "id": "showBorder",
  "switch": {
    "default": false
  }
}
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | boolean | Initial state |
| `trueValue` | string | Output when on |
| `falseValue` | string | Output when off |

#### Switch with Custom Values

Output specific strings instead of true/false:

```json
{
  "title": "Italic",
  "id": "isItalic",
  "switch": {
    "default": false,
    "trueValue": "italic",
    "falseValue": ""
  }
}
```

When on: `{{isItalic}}` outputs `italic`
When off: `{{isItalic}}` outputs empty string

```json
{
  "title": "Full Width",
  "id": "isFullWidth",
  "switch": {
    "default": false,
    "trueValue": "w-full",
    "falseValue": "w-auto"
  }
}
```

## Selection Controls

### select

Dropdown menu.

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

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | string | Initially selected value |
| `options` | array | Simple string array |
| `items` | array | Objects with title/value |

#### Select with Title/Value Items

```json
{
  "title": "Text Transform",
  "id": "textTransform",
  "select": {
    "default": "normal-case",
    "items": [
      { "title": "None", "value": "normal-case" },
      { "title": "Uppercase", "value": "uppercase" },
      { "title": "Lowercase", "value": "lowercase" },
      { "title": "Capitalize", "value": "capitalize" }
    ]
  }
}
```

#### Select with Multi-Class Values

```json
{
  "title": "Position",
  "id": "position",
  "select": {
    "default": "top-0 left-0",
    "items": [
      { "title": "Top Left", "value": "top-0 left-0" },
      { "title": "Top Right", "value": "top-0 right-0" },
      { "title": "Bottom Left", "value": "bottom-0 left-0" },
      { "title": "Bottom Right", "value": "bottom-0 right-0" },
      { "title": "Center", "value": "top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" }
    ]
  }
}
```

### segmented

Button group for selecting from a small set of options.

```json
{
  "title": "Alignment",
  "id": "alignment",
  "segmented": {
    "default": "center",
    "items": [
      { "value": "left", "icon": "text.alignleft" },
      { "value": "center", "icon": "text.aligncenter" },
      { "value": "right", "icon": "text.alignright" }
    ]
  }
}
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `default` | string | Initially selected value |
| `items` | array | Options with value and icon/title |

#### Segmented with Icons

```json
{
  "title": "Button Style",
  "id": "buttonStyle",
  "segmented": {
    "default": "solid",
    "items": [
      { "value": "solid", "icon": "rectangle.fill" },
      { "value": "outline", "icon": "rectangle" },
      { "value": "ghost", "icon": "square.dashed" }
    ]
  }
}
```

#### Segmented with Text

```json
{
  "title": "State",
  "id": "hoverState",
  "responsive": false,
  "segmented": {
    "default": "normal",
    "items": [
      { "title": "Normal", "value": "normal" },
      { "title": "Hover", "value": "hover" }
    ]
  }
}
```

#### Segmented with Default in Items

```json
{
  "title": "Layout",
  "id": "layout",
  "segmented": {
    "items": [
      { "title": "Grid", "value": "grid" },
      { "title": "Flex", "value": "flex", "default": true },
      { "title": "Block", "value": "block" }
    ]
  }
}
```

## Media Controls

### link

URL or page link picker.

```json
{
  "title": "Button Link",
  "id": "buttonLink",
  "link": {}
}
```

Access in templates:

```html
<a href="{{buttonLink.href}}" target="{{buttonLink.target}}">
  {{buttonLink.title}}
</a>
```

**Available properties:**

| Property | Description |
|----------|-------------|
| `buttonLink.href` | The URL |
| `buttonLink.title` | Link text |
| `buttonLink.target` | Target attribute (e.g., `_blank`) |

### resource

Resource picker for images, videos, PDFs, and other files.

```json
{
  "title": "Hero Image",
  "id": "heroImage",
  "resource": {}
}
```

Access in templates:

```html
<img src="{{heroImage.src}}" alt="Hero image" />
```

**Available properties:**

| Property | Description |
|----------|-------------|
| `heroImage.src` | Resource URL |
| `heroImage.width` | Original width (images/videos) |
| `heroImage.height` | Original height (images/videos) |
| `heroImage.filename` | Original filename |
| `heroImage.extension` | File extension |

#### Image Resource

```json
{
  "title": "Card Image",
  "id": "cardImage",
  "resource": {}
}
```

Template usage:

```html
<img src="{{cardImage.src}}" width="{{cardImage.width}}" height="{{cardImage.height}}" />
```

#### Background Image Resource

```json
{
  "title": "Background Image",
  "id": "bgImage",
  "resource": {}
}
```

Template usage:

```html
<div style="background-image: url('{{bgImage.src}}')"></div>
```

#### Video Resource

```json
{
  "title": "Video File",
  "id": "videoFile",
  "resource": {}
}
```

Template usage:

```html
<video src="{{videoFile.src}}" width="{{videoFile.width}}" height="{{videoFile.height}}"></video>
```

#### PDF Resource

```json
{
  "title": "PDF Document",
  "id": "pdfFile",
  "resource": {}
}
```

Template usage:

```html
<a href="{{pdfFile.src}}" download>Download {{pdfFile.filename}}</a>
```

## UI Elements

Non-interactive elements for organizing the inspector.

### divider

Visual separator line.

```json
{ "divider": {} }
```

### heading

Section heading within a group.

```json
{ "heading": "Advanced Settings" }
```

Or with object syntax:

```json
{ "heading": {}, "title": "Advanced Settings" }
```

### information

Help text or instructions.

```json
{
  "information": {},
  "title": "This setting affects all breakpoints."
}
```

Can be combined with visibility:

```json
{
  "information": {},
  "title": "Enter a valid coupon code (e.g., SAVE10)",
  "visible": "couponCode matches /^SAVE[0-9]{2}$/"
}
```

## Complete Example

```json
{
  "groups": [
    {
      "title": "Content",
      "icon": "textformat",
      "properties": [
        {
          "title": "Headline",
          "id": "headline",
          "text": {
            "default": "Welcome"
          }
        },
        {
          "title": "Description",
          "id": "description",
          "textarea": {
            "default": "A short description"
          }
        },
        { "divider": {} },
        { "heading": "Button" },
        {
          "title": "Show Button",
          "id": "showButton",
          "switch": {
            "default": true
          }
        },
        {
          "title": "Button Text",
          "id": "buttonText",
          "visible": "showButton == true",
          "text": {
            "default": "Learn More"
          }
        },
        {
          "title": "Button Link",
          "id": "buttonLink",
          "visible": "showButton == true",
          "link": {}
        }
      ]
    },
    {
      "title": "Layout",
      "icon": "square.split.bottomrightquarter",
      "properties": [
        {
          "title": "Alignment",
          "id": "alignment",
          "segmented": {
            "default": "center",
            "items": [
              { "value": "start", "icon": "text.alignleft" },
              { "value": "center", "icon": "text.aligncenter" },
              { "value": "end", "icon": "text.alignright" }
            ]
          }
        },
        {
          "title": "Columns",
          "id": "columns",
          "select": {
            "default": "3",
            "items": [
              { "title": "1 Column", "value": "1" },
              { "title": "2 Columns", "value": "2" },
              { "title": "3 Columns", "value": "3" },
              { "title": "4 Columns", "value": "4" }
            ]
          }
        },
        {
          "title": "Gap",
          "id": "gap",
          "format": "gap-{{value}}",
          "slider": {
            "default": 4,
            "min": 0,
            "max": 12,
            "round": true
          }
        }
      ]
    },
    {
      "title": "Media",
      "icon": "photo",
      "properties": [
        {
          "title": "Image",
          "id": "cardImage",
          "resource": {}
        },
        {
          "information": {},
          "title": "Recommended size: 800x600px"
        }
      ]
    }
  ]
}
```
