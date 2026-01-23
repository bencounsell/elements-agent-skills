# Theme Integration Reference

Theme controls connect your component's styling to the Elements Theme Studio, ensuring components adapt when the theme changes.

## Overview

Theme controls output Tailwind CSS classes based on theme values. They support:
- Theme color palettes
- Theme spacing scales
- Theme typography
- Responsive values per breakpoint
- Dark mode variants

## themeColor

Color picker using the theme's color palette.

### Basic Usage

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

### Options

| Option | Type | Description |
|--------|------|-------------|
| `name` | string | Color name from theme palette |
| `brightness` | number | Brightness level (50-950) |
| `darkName` | string | Color name for dark mode |
| `darkBrightness` | number | Brightness for dark mode |

### Available Color Names

| Name | Use Case |
|------|----------|
| `brand` | Primary brand color |
| `accent` | Secondary/accent color |
| `surface` | Backgrounds, cards, borders |
| `text` | Text colors |

### Light and Dark Mode

```json
{
  "title": "Background",
  "id": "bgColor",
  "format": "bg-{{value}}",
  "themeColor": {
    "default": {
      "name": "surface",
      "brightness": 50,
      "darkName": "surface",
      "darkBrightness": 900
    }
  }
}
```

Output: `bg-surface-50 dark:bg-surface-900`

### Common Patterns

**Background color:**
```json
{
  "format": "bg-{{value}}",
  "themeColor": { "default": { "name": "surface", "brightness": 100 } }
}
```

**Text color:**
```json
{
  "format": "text-{{value}}",
  "themeColor": { "default": { "name": "surface", "brightness": 900 } }
}
```

**Border color:**
```json
{
  "format": "border-{{value}}",
  "themeColor": { "default": { "name": "surface", "brightness": 300 } }
}
```

**Hover color:**
```json
{
  "format": "hover:bg-{{value}}",
  "themeColor": { "default": { "name": "brand", "brightness": 600 } }
}
```

**Focus ring:**
```json
{
  "format": "focus:ring-{{value}}",
  "themeColor": { "default": { "name": "brand", "brightness": 500 } }
}
```

### Brightness Scale

| Brightness | Typical Use |
|------------|-------------|
| `50` | Very light backgrounds |
| `100` | Light backgrounds |
| `200` | Light borders, dividers |
| `300` | Borders, disabled states |
| `400` | Muted text, placeholders |
| `500` | Primary/default |
| `600` | Hover states |
| `700` | Active/pressed states |
| `800` | Dark text |
| `900` | Very dark backgrounds/text |
| `950` | Near black |

## themeSpacing

Spacing control using the theme's spacing scale. Supports different modes for padding, margin, gap, and positioning.

### Modes

| Mode | Output Classes | Sides |
|------|---------------|-------|
| `padding` | `pt-`, `pr-`, `pb-`, `pl-` | top, right, bottom, left |
| `margin` | `mt-`, `mr-`, `mb-`, `ml-` | top, right, bottom, left |
| `gap` | `gap-x-`, `gap-y-` | x, y |
| `position` | `top-`, `right-`, `bottom-`, `left-` | top, right, bottom, left |
| `single` | Custom via format | value |

### Padding Mode

```json
{
  "title": "Padding",
  "id": "cardPadding",
  "themeSpacing": {
    "mode": "padding",
    "default": {
      "base": {
        "top": "md",
        "right": "md",
        "bottom": "md",
        "left": "md"
      }
    }
  }
}
```

Output: `pt-md pr-md pb-md pl-md`

### Margin Mode

```json
{
  "title": "Margin",
  "id": "sectionMargin",
  "themeSpacing": {
    "mode": "margin",
    "default": {
      "base": {
        "top": "0",
        "right": "auto",
        "bottom": "0",
        "left": "auto"
      }
    }
  }
}
```

Output: `mt-0 mr-auto mb-0 ml-auto`

### Gap Mode

```json
{
  "title": "Gap",
  "id": "gridGap",
  "themeSpacing": {
    "mode": "gap",
    "default": {
      "base": {
        "top": "md",
        "left": "md"
      }
    }
  }
}
```

Output: `gap-x-md gap-y-md`

### Position Mode

```json
{
  "title": "Position",
  "id": "badgePosition",
  "themeSpacing": {
    "mode": "position",
    "default": {
      "base": {
        "top": "2",
        "right": "2",
        "bottom": "auto",
        "left": "auto"
      }
    }
  }
}
```

Output: `top-2 right-2`

### Single Mode

For single spacing values with custom format:

```json
{
  "title": "Offset",
  "id": "offset",
  "format": "translate-x-{{value}}",
  "themeSpacing": {
    "mode": "single",
    "default": {
      "base": {
        "value": "4"
      }
    }
  }
}
```

Output: `translate-x-4`

### Linked Values

Link horizontal and/or vertical values to change together:

```json
{
  "title": "Button Padding",
  "id": "buttonPadding",
  "themeSpacing": {
    "mode": "padding",
    "default": {
      "base": {
        "top": "2",
        "right": "4",
        "bottom": "2",
        "left": "4",
        "linkHorizontal": true,
        "linkVertical": true
      }
    }
  }
}
```

When linked, changing one side changes the linked side automatically.

### Responsive Spacing

```json
{
  "title": "Section Padding",
  "id": "sectionPadding",
  "themeSpacing": {
    "mode": "padding",
    "default": {
      "base": {
        "top": "md",
        "right": "sm",
        "bottom": "md",
        "left": "sm"
      },
      "md": {
        "top": "xl",
        "right": "lg",
        "bottom": "xl",
        "left": "lg"
      }
    }
  }
}
```

## themeBorderRadius

Border radius control with individual corners.

### Basic Usage

```json
{
  "title": "Border Radius",
  "id": "borderRadius",
  "themeBorderRadius": {
    "default": {
      "base": {
        "topLeft": "lg",
        "topRight": "lg",
        "bottomLeft": "lg",
        "bottomRight": "lg"
      }
    }
  }
}
```

Output: `rounded-tl-lg rounded-tr-lg rounded-bl-lg rounded-br-lg`

### Default Theme Value

Use "Default" to inherit from theme settings:

```json
{
  "title": "Border Radius",
  "id": "borderRadius",
  "themeBorderRadius": {
    "default": {
      "base": {
        "topLeft": "Default",
        "topRight": "Default",
        "bottomLeft": "Default",
        "bottomRight": "Default"
      }
    }
  }
}
```

### Available Values

| Value | Result |
|-------|--------|
| `none` | `rounded-*-none` |
| `sm` | `rounded-*-sm` |
| `md` | `rounded-*-md` |
| `lg` | `rounded-*-lg` |
| `xl` | `rounded-*-xl` |
| `2xl` | `rounded-*-2xl` |
| `3xl` | `rounded-*-3xl` |
| `full` | `rounded-*-full` |
| `Default` | Theme default |

### Partial Rounding

```json
{
  "title": "Top Corners Only",
  "id": "topRadius",
  "themeBorderRadius": {
    "default": {
      "base": {
        "topLeft": "lg",
        "topRight": "lg",
        "bottomLeft": "none",
        "bottomRight": "none"
      }
    }
  }
}
```

## themeBorderWidth

Border width control with individual sides.

### Basic Usage

```json
{
  "title": "Border",
  "id": "borderWidth",
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

Output: `border-t border-r border-b border-l`

### Linked Border Width

```json
{
  "title": "Border",
  "id": "borderWidth",
  "themeBorderWidth": {
    "default": {
      "base": {
        "top": "0",
        "right": "0",
        "bottom": "2",
        "left": "0",
        "linkHorizontal": true,
        "linkVertical": true
      }
    }
  }
}
```

### Available Values

| Value | Class |
|-------|-------|
| `Default` | `border-*` |
| `0` | `border-*-0` |
| `1` | `border-*-1` |
| `2` | `border-*-2` |
| `4` | `border-*-4` |
| `8` | `border-*-8` |

## themeShadow

Box shadow, drop shadow, or text shadow using theme's shadow scale.

### Box Shadow (Default)

```json
{
  "title": "Shadow",
  "id": "cardShadow",
  "themeShadow": {
    "default": {
      "name": "md"
    }
  }
}
```

Output: `shadow-md`

### Drop Shadow

For filter-based shadows (better for non-rectangular elements):

```json
{
  "title": "Drop Shadow",
  "id": "imageShadow",
  "themeShadow": {
    "mode": "drop",
    "default": {
      "name": "lg"
    }
  }
}
```

Output: `drop-shadow-lg`

### Text Shadow

```json
{
  "title": "Text Shadow",
  "id": "headingShadow",
  "themeShadow": {
    "mode": "text",
    "default": {
      "name": "sm"
    }
  }
}
```

### Available Values

| Name | Description |
|------|-------------|
| `Default` | Default shadow |
| `none` | No shadow |
| `sm` | Small shadow |
| `md` | Medium shadow |
| `lg` | Large shadow |
| `xl` | Extra large shadow |
| `2xl` | 2X large shadow |
| `inner` | Inner shadow (box only) |

### Responsive Shadow

```json
{
  "title": "Shadow",
  "id": "shadow",
  "themeShadow": {
    "default": {
      "base": { "name": "sm" },
      "md": { "name": "lg" }
    }
  }
}
```

Output: `shadow-sm md:shadow-lg`

## themeFont

Font family picker using theme fonts.

### Basic Usage

```json
{
  "title": "Font",
  "id": "headingFont",
  "themeFont": {
    "default": {
      "base": "heading"
    }
  }
}
```

Output: `font-heading`

### Available Fonts

| Value | Description |
|-------|-------------|
| `heading` | Theme heading font |
| `body` | Theme body font |
| `mono` | Monospace font |

### Responsive Font

```json
{
  "title": "Font",
  "id": "fontFamily",
  "themeFont": {
    "default": {
      "base": { "name": "body" },
      "md": { "name": "heading" }
    }
  }
}
```

Output: `font-body md:font-heading`

## themeTextStyle

Text size picker using theme's type scale.

### Basic Usage

```json
{
  "title": "Text Size",
  "id": "headingSize",
  "themeTextStyle": {
    "default": {
      "base": { "name": "2xl" }
    }
  }
}
```

Output: `text-2xl`

### Available Sizes

| Name | Size |
|------|------|
| `xs` | 0.75rem |
| `sm` | 0.875rem |
| `base` | 1rem |
| `lg` | 1.125rem |
| `xl` | 1.25rem |
| `2xl` | 1.5rem |
| `3xl` | 1.875rem |
| `4xl` | 2.25rem |
| `5xl` | 3rem |
| `6xl` | 3.75rem |
| `7xl` | 4.5rem |
| `8xl` | 6rem |
| `9xl` | 8rem |

### Responsive Text Size

```json
{
  "title": "Headline Size",
  "id": "headlineSize",
  "themeTextStyle": {
    "default": {
      "base": { "name": "xl" },
      "md": { "name": "3xl" },
      "lg": { "name": "5xl" }
    }
  }
}
```

Output: `text-xl md:text-3xl lg:text-5xl`

## themeTypography

Typography preset picker for article/prose styling.

### Basic Usage

```json
{
  "title": "Article Style",
  "id": "articleStyle",
  "themeTypography": {
    "default": {
      "base": { "name": "article" }
    }
  }
}
```

### Responsive Typography

```json
{
  "title": "Prose Style",
  "id": "proseStyle",
  "themeTypography": {
    "default": {
      "base": { "name": "article" },
      "md": { "name": "article-lg" }
    }
  }
}
```

## Format Strings

Format strings transform theme control values into Tailwind classes.

### How Format Works

The `{{value}}` placeholder is replaced with the control's output:

```json
{
  "format": "bg-{{value}}",
  "themeColor": { "default": { "name": "brand", "brightness": 500 } }
}
```

`{{value}}` becomes `brand-500`, final output: `bg-brand-500`

### Common Format Patterns

| Format | Use Case | Example Output |
|--------|----------|----------------|
| `bg-{{value}}` | Background color | `bg-brand-500` |
| `text-{{value}}` | Text color | `text-surface-900` |
| `border-{{value}}` | Border color | `border-surface-300` |
| `hover:bg-{{value}}` | Hover background | `hover:bg-brand-600` |
| `focus:ring-{{value}}` | Focus ring | `focus:ring-brand-500` |
| `p-{{value}}` | Padding | `p-4` |
| `gap-{{value}}` | Gap | `gap-6` |
| `rounded-{{value}}` | Border radius | `rounded-lg` |

### Multiple Formats

For hover states, use separate properties:

```json
{
  "title": "Background",
  "id": "bgColor",
  "visible": "state == 'normal'",
  "format": "bg-{{value}}",
  "themeColor": { "default": { "name": "brand", "brightness": 500 } }
},
{
  "title": "Background",
  "id": "bgColorHover",
  "visible": "state == 'hover'",
  "format": "hover:bg-{{value}}",
  "themeColor": { "default": { "name": "brand", "brightness": 600 } }
}
```

## Complete Example

A fully styled card with all theme controls:

```json
{
  "groups": [
    {
      "title": "Colors",
      "icon": "paintbrush.fill",
      "properties": [
        {
          "title": "Background",
          "id": "cardBg",
          "format": "bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 50,
              "darkName": "surface",
              "darkBrightness": 800
            }
          }
        },
        {
          "title": "Text Color",
          "id": "textColor",
          "format": "text-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 900,
              "darkName": "surface",
              "darkBrightness": 100
            }
          }
        },
        {
          "title": "Border Color",
          "id": "borderColor",
          "format": "border-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 200,
              "darkName": "surface",
              "darkBrightness": 700
            }
          }
        }
      ]
    },
    {
      "title": "Spacing",
      "icon": "squareshape.squareshape.dotted",
      "properties": [
        {
          "title": "Padding",
          "id": "cardPadding",
          "themeSpacing": {
            "mode": "padding",
            "default": {
              "base": {
                "top": "md",
                "right": "md",
                "bottom": "md",
                "left": "md",
                "linkHorizontal": true,
                "linkVertical": true
              },
              "md": {
                "top": "lg",
                "right": "lg",
                "bottom": "lg",
                "left": "lg"
              }
            }
          }
        }
      ]
    },
    {
      "title": "Border",
      "icon": "square.dashed",
      "properties": [
        {
          "title": "Width",
          "id": "borderWidth",
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
        },
        {
          "title": "Radius",
          "id": "borderRadius",
          "themeBorderRadius": {
            "default": {
              "base": {
                "topLeft": "lg",
                "topRight": "lg",
                "bottomLeft": "lg",
                "bottomRight": "lg"
              }
            }
          }
        }
      ]
    },
    {
      "title": "Effects",
      "icon": "sparkles",
      "properties": [
        {
          "title": "Shadow",
          "id": "cardShadow",
          "themeShadow": {
            "default": {
              "base": { "name": "sm" },
              "md": { "name": "md" }
            }
          }
        }
      ]
    },
    {
      "title": "Typography",
      "icon": "textformat.size",
      "properties": [
        {
          "title": "Font",
          "id": "headingFont",
          "themeFont": {
            "default": {
              "base": "heading"
            }
          }
        },
        {
          "title": "Heading Size",
          "id": "headingSize",
          "themeTextStyle": {
            "default": {
              "base": { "name": "xl" },
              "md": { "name": "2xl" }
            }
          }
        }
      ]
    }
  ]
}
```

Template usage:

```html
<div class="{{cardBg}} {{textColor}} {{borderColor}} {{cardPadding}} {{borderWidth}} {{borderRadius}} {{cardShadow}}">
  <h3 class="{{headingFont}} {{headingSize}}">{{title}}</h3>
  <p>{{description}}</p>
</div>
```
