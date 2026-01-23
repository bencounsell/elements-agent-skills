# General Structure Reference

All properties in `properties.json` share a common structure with these universal keys.

## Property Structure

```json
{
  "title": "Display Label",
  "id": "propertyId",
  "format": "prefix-{{value}}",
  "visible": "otherProperty == true",
  "enabled": "anotherProperty != 'disabled'",
  "responsive": true,
  "controlType": {
    // control-specific options
  }
}
```

## Common Properties

### title

The human-friendly label shown in the Elements inspector. Use short, descriptive labels.

```json
{
  "title": "Headline",
  "id": "heroHeadline",
  "text": {
    "default": "Welcome"
  }
}
```

### id

The unique identifier for the control. This becomes the variable name in templates and is used in conditional expressions.

```json
{
  "title": "Button Label",
  "id": "buttonLabel",
  "text": {
    "default": "Click Me"
  }
}
```

Template usage:

```html
<button>{{buttonLabel}}</button>
```

**Best practices:**
- Use camelCase: `heroHeadline`, `cardBgColor`
- Be descriptive: `heroHeadline` not `title1`
- Keep IDs unique within the component

### format

Transforms the control's value before passing it to templates. Supports Tailwind classes, CSS properties, and CSS custom properties.

#### Tailwind Classes

```json
{
  "title": "Padding",
  "id": "cardPadding",
  "format": "p-{{value}}",
  "slider": {
    "default": 4,
    "min": 0,
    "max": 12
  }
}
```

Output: `p-4`

#### Arbitrary Values

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

#### CSS Properties

```json
{
  "title": "Badge Offset",
  "id": "badgeOffsetX",
  "format": "transform: translateX({{value}}px);",
  "number": {
    "default": 12
  }
}
```

Output: `transform: translateX(12px);`

#### CSS Custom Properties

```json
{
  "title": "Badge Offset",
  "id": "badgeOffsetX",
  "format": "--badge-offset-x: {{value}}px;",
  "number": {
    "default": 12
  }
}
```

Output: `--badge-offset-x: 12px;`

Usage in template:

```html
<div class="badge" style="{{badgeOffsetX}}">New</div>
```

### visible

Controls whether the property is shown in the inspector based on a logical expression.

#### Basic Comparison

```json
{
  "title": "Overlay Color",
  "id": "overlayColor",
  "visible": "showOverlay == true",
  "themeColor": {}
}
```

#### Multiple Conditions

```json
{
  "title": "Image Settings",
  "id": "imageSettings",
  "visible": "(bgStyle == 'image' || bgStyle == 'video') && showAdvanced == true"
}
```

#### Numeric Comparisons

```json
{
  "title": "Fine Tuning",
  "id": "fineTuning",
  "visible": "blurAmount > 0 && blurAmount <= 20"
}
```

#### Negation

```json
{
  "title": "Default Colors",
  "id": "defaultColors",
  "visible": "useCustomColors != true"
}
```

#### Regex Matching

```json
{
  "title": "Valid Format",
  "information": {},
  "visible": "couponCode matches /^SAVE[0-9]{2}$/"
}
```

**Supported operators:**
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `&&`, `||`
- Regex: `matches /pattern/`

### enabled

Controls whether the property is enabled (interactive) vs disabled (grayed out). Uses the same expression syntax as `visible`.

```json
{
  "title": "Shadow Blur",
  "id": "shadowBlur",
  "enabled": "showShadow == true && shadowStyle != 'none'",
  "slider": {
    "default": 10,
    "min": 0,
    "max": 50
  }
}
```

**Difference from visible:**
- `visible: false` - Control is completely hidden
- `enabled: false` - Control is visible but grayed out and non-interactive

### responsive

Controls whether users can set different values per breakpoint. Default is `true`.

#### Default Behavior (responsive: true)

```json
{
  "title": "Columns",
  "id": "gridColumns",
  "select": {
    "default": "3",
    "items": [
      { "title": "1", "value": "1" },
      { "title": "2", "value": "2" },
      { "title": "3", "value": "3" }
    ]
  }
}
```

When users customize per-breakpoint, output becomes:

```
grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3
```

Elements automatically applies Tailwind's responsive modifiers.

#### Multi-Value Responsive

Works with controls that output multiple classes:

```json
{
  "title": "Position",
  "id": "badgePosition",
  "select": {
    "default": "bottom-0 left-0",
    "items": [
      { "title": "Top Right", "value": "top-0 right-0" },
      { "title": "Bottom Left", "value": "bottom-0 left-0" }
    ]
  }
}
```

Output: `bottom-0 left-0 md:top-0 md:right-0`

#### Disabling Responsive

Use `"responsive": false` for:
- HTML IDs
- CSS class names
- Non-visual settings
- State toggles

```json
{
  "title": "Element ID",
  "id": "elementId",
  "responsive": false,
  "text": {
    "default": ""
  }
}
```

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

## Complete Example

```json
{
  "title": "Overlay Opacity",
  "id": "overlayOpacity",
  "format": "bg-opacity-[{{value}}%]",
  "visible": "showOverlay == true",
  "enabled": "overlayStyle != 'none'",
  "responsive": false,
  "slider": {
    "default": 60,
    "min": 0,
    "max": 100,
    "round": true,
    "units": "%"
  }
}
```

This control:
- Shows a slider labeled "Overlay Opacity"
- Only appears when `showOverlay` is true
- Is disabled when `overlayStyle` is 'none'
- Outputs `bg-opacity-[60%]` (not responsive)
- Has a range of 0-100 with whole numbers
