# Theme Controls Reference

Theme-integrated controls that connect to the RapidWeaver Elements Theme Studio. These ensure components adapt to theme changes and maintain design consistency.

## themeColor

Color picker using the theme's color palette.

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

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `name` | string | Color name from theme (brand, surface, accent, etc.) |
| `brightness` | number | Brightness level (50-950) |
| `darkName` | string | Color name for dark mode |
| `darkBrightness` | number | Brightness for dark mode |

### Light and Dark Mode Colors

```json
{
  "title": "Surface Color",
  "id": "surfaceColor",
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

### Common Color Patterns

**Background color:**

```json
{
  "title": "Background",
  "id": "bgColor",
  "format": "bg-{{value}}",
  "themeColor": {
    "default": { "name": "brand", "brightness": 500 }
  }
}
```

**Text color:**

```json
{
  "title": "Text Color",
  "id": "textColor",
  "format": "text-{{value}}",
  "themeColor": {
    "default": { "name": "surface", "brightness": 900 }
  }
}
```

**Border color:**

```json
{
  "title": "Border Color",
  "id": "borderColor",
  "format": "border-{{value}}",
  "themeColor": {
    "default": { "name": "surface", "brightness": 300 }
  }
}
```

**Hover color:**

```json
{
  "title": "Hover Color",
  "id": "hoverBgColor",
  "format": "hover:bg-{{value}}",
  "themeColor": {
    "default": { "name": "brand", "brightness": 600 }
  }
}
```

## themeSpacing

Spacing control using the theme's spacing scale. Supports multiple modes for different CSS properties.

**Available modes:** `padding`, `margin`, `gap`, `position`, `single`

### Padding Mode

```json
{
  "title": "Card Padding",
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
  "title": "Section Margin",
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
  "title": "Grid Gap",
  "id": "gridGap",
  "themeSpacing": {
    "mode": "gap",
    "default": {
      "base": {
        "x": "md",
        "y": "md"
      }
    }
  }
}
```

Output: `gap-x-md gap-y-md`

### Single Mode

For single spacing values (useful for positioning, offsets):

```json
{
  "title": "Badge Offset",
  "id": "badgeOffset",
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

Output: `top-2`

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

### Linked Values

Link horizontal/vertical values to change together:

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

## themeFont

Font family picker using theme fonts.

```json
{
  "title": "Headline Font",
  "id": "headlineFont",
  "themeFont": {
    "default": {
      "base": "heading"
    }
  }
}
```

Output: `font-heading`

### Responsive Font

```json
{
  "title": "Font Family",
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

```json
{
  "title": "Heading Size",
  "id": "headingSize",
  "themeTextStyle": {
    "default": {
      "base": { "name": "2xl" }
    }
  }
}
```

Output: `text-2xl`

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

Typography preset picker (article styles, prose settings).

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

## themeBorderWidth

Border width control with individual sides.

```json
{
  "title": "Border Width",
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

### Linked Border Width

```json
{
  "title": "Card Border",
  "id": "cardBorderWidth",
  "themeBorderWidth": {
    "default": {
      "base": {
        "top": "0",
        "right": "0",
        "bottom": "0",
        "left": "0",
        "linkHorizontal": true,
        "linkVertical": true
      }
    }
  }
}
```

## themeBorderRadius

Border radius control with individual corners.

```json
{
  "title": "Card Radius",
  "id": "cardRadius",
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

### Default Theme Radius

Use "Default" to inherit from theme:

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

## themeShadow

Box shadow picker using theme's shadow scale.

```json
{
  "title": "Card Shadow",
  "id": "cardShadow",
  "themeShadow": {
    "default": {
      "name": "md"
    }
  }
}
```

Output: `shadow-md`

### Shadow Modes

**Box shadow (default):**

```json
{
  "title": "Box Shadow",
  "id": "boxShadow",
  "themeShadow": {
    "default": {
      "name": "lg"
    }
  }
}
```

**Drop shadow (for filters):**

```json
{
  "title": "Drop Shadow",
  "id": "dropShadow",
  "themeShadow": {
    "mode": "drop",
    "default": {
      "name": "md"
    }
  }
}
```

**Text shadow:**

```json
{
  "title": "Text Shadow",
  "id": "textShadow",
  "themeShadow": {
    "mode": "text",
    "default": {
      "name": "sm"
    }
  }
}
```

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

## Complete Example

```json
{
  "groups": [
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
          "title": "Size",
          "id": "headingSize",
          "themeTextStyle": {
            "default": {
              "base": { "name": "2xl" },
              "md": { "name": "4xl" }
            }
          }
        },
        {
          "title": "Color",
          "id": "headingColor",
          "format": "text-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 900,
              "darkName": "surface",
              "darkBrightness": 50
            }
          }
        }
      ]
    },
    {
      "title": "Background",
      "icon": "paintbrush.fill",
      "properties": [
        {
          "title": "Color",
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
          "title": "Color",
          "id": "borderColor",
          "format": "border-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 200
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
          "id": "boxShadow",
          "themeShadow": {
            "default": {
              "base": { "name": "sm" },
              "md": { "name": "md" }
            }
          }
        }
      ]
    }
  ]
}
```
