# info.json Reference

The `info.json` file is the component manifest. It defines metadata that Elements uses to identify and display the component.

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `identifier` | string | Unique ID using reverse DNS format (e.g., `com.company.component`) |
| `author` | string | Developer or company name |
| `title` | string | Display name shown in Elements UI |
| `group` | string | Category for grouping (must be from allowed list) |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `tags` | array | Keywords for searching/filtering |
| `helpURL` | string | URL to online documentation |
| `infoURL` | string | URL to marketing/info page |
| `deploy` | boolean | Include when deploying pack (default: true) |

## Valid Groups

Components must use one of these predefined groups:

| Group | Use For |
|-------|---------|
| **Accessibility** | ARIA labels, contrast checkers |
| **Animation** | Hover effects, animated SVGs |
| **CMS** | Content management system integrations |
| **Content** | Headings, paragraphs, lists, text blocks |
| **Dynamic** | Online databases, Google Sheets |
| **Ecommerce** | Cart integration, products, checkout |
| **Forms** | Text fields, checkboxes, buttons, inputs |
| **Interactive** | Modals, popovers, accordions, carousels |
| **Layout** | Grid, flex, containers, columns |
| **Media** | Images, video, audio, icons, embeds |
| **Navigation** | Menus, navbars, breadcrumbs, tabs |
| **Security** | Password protection, login forms |
| **SEO** | Keywords, meta tags, SEO helpers |
| **Utility** | Cookies, anchors, placeholders, dividers |

## Complete Example

```json
{
  "identifier": "com.elementsplatform.hero.fullwidth",
  "author": "Elements Platform",
  "title": "Full Width Hero",
  "group": "Layout",
  "tags": [
    "hero",
    "banner",
    "header",
    "full-width"
  ],
  "helpURL": "https://docs.example.com/hero",
  "infoURL": "https://example.com/components/hero",
  "deploy": true
}
```

## Identifier Rules

The identifier must:
- Use reverse DNS format: `com.companyname.componentname`
- Contain only lowercase letters and periods
- Be unique across all installed packs
- Match the component folder name

Good examples:
- `com.acme.button`
- `com.acme.navigation.navbar`
- `com.acme.hero.parallax`

Bad examples:
- `my-button` (not reverse DNS)
- `com.acme.My Button` (spaces and capitals)
- `button` (too generic, not unique)
