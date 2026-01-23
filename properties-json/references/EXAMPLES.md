# Component Examples

Complete `properties.json` examples demonstrating common patterns.

## Card Component

A basic card with content, media, and styling controls.

```json
{
  "groups": [
    {
      "title": "Content",
      "icon": "textformat",
      "properties": [
        {
          "title": "Title",
          "id": "cardTitle",
          "text": {
            "default": "Card Title"
          }
        },
        {
          "title": "Description",
          "id": "cardDescription",
          "textarea": {
            "default": "A short description of this card."
          }
        },
        { "divider": {} },
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
      "title": "Media",
      "icon": "photo",
      "properties": [
        {
          "title": "Image",
          "id": "cardImage",
          "resource": {}
        }
      ]
    },
    {
      "title": "Style",
      "icon": "paintbrush",
      "properties": [
        {
          "title": "Background",
          "id": "cardBgColor",
          "format": "bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 50
            }
          }
        },
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
        },
        {
          "title": "Border Radius",
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
        },
        {
          "title": "Shadow",
          "id": "cardShadow",
          "themeShadow": {
            "default": {
              "name": "md"
            }
          }
        }
      ]
    }
  ]
}
```

**Key patterns:**
- Content group with conditional button controls
- Divider to separate related sections
- Theme controls for consistent styling

## Hero Section with Overlay

A hero section with background style toggle and overlay controls.

```json
{
  "groups": [
    {
      "title": "Hero Content",
      "icon": "textformat.size",
      "properties": [
        {
          "title": "Headline",
          "id": "heroHeadline",
          "text": {
            "default": "Build faster with Elements"
          }
        },
        {
          "title": "Subheading",
          "id": "heroSubheading",
          "textarea": {
            "default": "Create beautiful, responsive components without writing code."
          }
        }
      ]
    },
    {
      "title": "Background",
      "icon": "photo.fill",
      "properties": [
        {
          "title": "Style",
          "id": "bgStyle",
          "segmented": {
            "default": "color",
            "items": [
              { "title": "Color", "value": "color" },
              { "title": "Image", "value": "image" }
            ]
          }
        },
        {
          "title": "Background Color",
          "id": "heroBgColor",
          "visible": "bgStyle == 'color'",
          "format": "bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "brand",
              "brightness": 500
            }
          }
        },
        {
          "title": "Background Image",
          "id": "heroBgImage",
          "visible": "bgStyle == 'image'",
          "resource": {}
        },
        { "divider": {} },
        { "heading": "Overlay" },
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
          "format": "bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "surface",
              "brightness": 900
            }
          }
        },
        {
          "title": "Overlay Opacity",
          "id": "overlayOpacity",
          "visible": "showOverlay == true",
          "format": "bg-opacity-[{{value}}%]",
          "slider": {
            "default": 50,
            "min": 0,
            "max": 100,
            "units": "%",
            "round": true
          }
        }
      ]
    },
    {
      "title": "Layout",
      "icon": "square.split.bottomrightquarter",
      "properties": [
        {
          "title": "Min Height",
          "id": "heroMinHeight",
          "format": "min-h-[{{value}}vh]",
          "slider": {
            "default": 60,
            "min": 20,
            "max": 100,
            "units": "vh",
            "round": true
          }
        },
        {
          "title": "Content Alignment",
          "id": "heroAlign",
          "segmented": {
            "default": "center",
            "items": [
              { "value": "start", "icon": "text.alignleft" },
              { "value": "center", "icon": "text.aligncenter" },
              { "value": "end", "icon": "text.alignright" }
            ]
          }
        }
      ]
    }
  ]
}
```

**Key patterns:**
- Segmented control to toggle between modes
- Conditional visibility based on selection
- Heading element to label a section
- Arbitrary value format for viewport units

## Button with Hover States

A button with normal/hover state toggle pattern.

```json
{
  "groups": [
    {
      "title": "Link",
      "icon": "link",
      "properties": [
        {
          "title": "Link",
          "id": "buttonLink",
          "link": {}
        }
      ]
    },
    {
      "title": "Text",
      "icon": "textformat",
      "properties": [
        {
          "title": "Label",
          "id": "buttonLabel",
          "text": {
            "default": "Get Started"
          }
        },
        {
          "title": "Font",
          "id": "buttonFont",
          "themeFont": {
            "default": {
              "base": "body"
            }
          }
        },
        {
          "title": "Size",
          "id": "buttonTextSize",
          "themeTextStyle": {
            "default": {
              "base": { "name": "base" }
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
          "title": "State",
          "id": "bgState",
          "responsive": false,
          "segmented": {
            "default": "normal",
            "items": [
              { "title": "Normal", "value": "normal" },
              { "title": "Hover", "value": "hover" }
            ]
          }
        },
        {
          "title": "Color",
          "id": "buttonBgColor",
          "visible": "bgState == 'normal'",
          "format": "bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "brand",
              "brightness": 500
            }
          }
        },
        {
          "title": "Color",
          "id": "buttonBgColorHover",
          "visible": "bgState == 'hover'",
          "format": "hover:bg-{{value}}",
          "themeColor": {
            "default": {
              "name": "brand",
              "brightness": 600
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
      ]
    },
    {
      "title": "Advanced",
      "icon": "gearshape",
      "properties": [
        {
          "title": "CSS Classes",
          "id": "cssClasses",
          "textarea": {
            "default": ""
          }
        },
        {
          "title": "ID",
          "id": "buttonId",
          "responsive": false,
          "text": {
            "default": ""
          }
        }
      ]
    }
  ]
}
```

**Key patterns:**
- State toggle with `responsive: false` (not a visual setting)
- Same title for different controls shown conditionally
- Hover state using `hover:` prefix in format
- Advanced group for CSS overrides and HTML ID
- Linked padding values for horizontal/vertical sync

## Pricing Table

A more complex example with multiple conditional sections.

```json
{
  "groups": [
    {
      "title": "Plan",
      "icon": "tag",
      "properties": [
        {
          "title": "Plan Name",
          "id": "planName",
          "text": {
            "default": "Pro Plan"
          }
        },
        {
          "title": "Price",
          "id": "planPrice",
          "text": {
            "default": "$29"
          }
        },
        {
          "title": "Billing Period",
          "id": "billingPeriod",
          "select": {
            "default": "/month",
            "items": [
              { "title": "Monthly", "value": "/month" },
              { "title": "Yearly", "value": "/year" },
              { "title": "One-time", "value": "" }
            ]
          }
        },
        { "divider": {} },
        {
          "title": "Show Badge",
          "id": "showBadge",
          "switch": {
            "default": false
          }
        },
        {
          "title": "Badge Text",
          "id": "badgeText",
          "visible": "showBadge == true",
          "text": {
            "default": "Most Popular"
          }
        }
      ]
    },
    {
      "title": "Features",
      "icon": "checklist",
      "properties": [
        {
          "title": "Feature 1",
          "id": "feature1",
          "text": {
            "default": "Unlimited projects"
          }
        },
        {
          "title": "Feature 2",
          "id": "feature2",
          "text": {
            "default": "Priority support"
          }
        },
        {
          "title": "Feature 3",
          "id": "feature3",
          "text": {
            "default": "Custom domain"
          }
        },
        {
          "information": {},
          "title": "Add more features by editing the template directly."
        }
      ]
    },
    {
      "title": "CTA Button",
      "icon": "hand.tap",
      "properties": [
        {
          "title": "Button Text",
          "id": "ctaText",
          "text": {
            "default": "Get Started"
          }
        },
        {
          "title": "Button Link",
          "id": "ctaLink",
          "link": {}
        }
      ]
    },
    {
      "title": "Style",
      "icon": "paintbrush",
      "properties": [
        {
          "title": "Highlight Card",
          "id": "isHighlighted",
          "switch": {
            "default": false
          }
        },
        {
          "title": "Border Color",
          "id": "borderColor",
          "visible": "isHighlighted == true",
          "format": "border-{{value}}",
          "themeColor": {
            "default": {
              "name": "brand",
              "brightness": 500
            }
          }
        },
        {
          "title": "Border Width",
          "id": "borderWidth",
          "visible": "isHighlighted == true",
          "themeBorderWidth": {
            "default": {
              "base": {
                "top": "2",
                "right": "2",
                "bottom": "2",
                "left": "2"
              }
            }
          }
        }
      ]
    }
  ]
}
```

**Key patterns:**
- Information element to provide user guidance
- Multiple conditional controls tied to a single switch
- Select with different display titles vs values
