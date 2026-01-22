# Available Data in hooks.js

Complete reference for all data available through the `rw` object.

## rw.props

All property values from `properties.json`. Each property's `id` becomes a key.

**Example properties.json:**
```json
{
  "groups": [{
    "properties": [
      { "id": "heading", "text": { "default": "Hello" } },
      { "id": "showBorder", "switch": { "default": true } },
      { "id": "padding", "slider": { "default": 4 } }
    ]
  }]
}
```

**In hooks.js:**
```javascript
const { heading, showBorder, padding } = rw.props;
// heading = "Hello"
// showBorder = true
// padding = 4
```

### Special Property Types

**Image properties:**
```javascript
const { heroImage } = rw.props;
// heroImage = {
//   resource: { src: "...", width: 1920, height: 1080 },
//   alt: "Description",
//   title: "Image Title"
// }
```

**Link properties:**
```javascript
const { buttonLink } = rw.props;
// buttonLink = {
//   href: "https://...",
//   title: "Link Text",
//   target: "_blank",
//   rel: "noopener"
// }
```

**Theme color properties:**
```javascript
const { bgColor } = rw.props;
// bgColor = "primary" (theme color name)
```

---

## rw.responsiveProps

Property values organized by breakpoint when `"responsive": true` is set.

**Example properties.json:**
```json
{
  "id": "columns",
  "responsive": true,
  "select": { "default": "3", "options": ["1", "2", "3", "4"] }
}
```

**In hooks.js:**
```javascript
const { columns } = rw.responsiveProps;
// columns = {
//   mobile: "1",
//   tablet: "2",
//   desktop: "3"
// }
```

---

## rw.collections

Data from collection JSON files in the `collections/` folder.

**Example collections/slides.json:**
```json
{
  "items": [
    { "title": "Slide 1", "image": {...} },
    { "title": "Slide 2", "image": {...} }
  ]
}
```

**In hooks.js:**
```javascript
const { slides } = rw.collections;
// slides = [
//   { title: "Slide 1", image: {...} },
//   { title: "Slide 2", image: {...} }
// ]
```

---

## rw.project

Project-level information.

| Property | Type | Example | Description |
|----------|------|---------|-------------|
| `title` | string | `"My Website"` | Project name |
| `mode` | string | `"edit"` | Current mode: `"edit"`, `"preview"`, `"publish"` |
| `siteUrl` | string | `"https://example.com"` | Published site URL |
| `basePath` | string | `"/"` | Base path for URLs |

```javascript
const { title, mode, siteUrl } = rw.project;
```

---

## rw.page

Current page information.

| Property | Type | Example | Description |
|----------|------|---------|-------------|
| `id` | string | `"page-abc123"` | Unique page ID |
| `title` | string | `"About Us"` | Page title |
| `filename` | string | `"about.html"` | Output filename |
| `path` | string | `"/about/"` | URL path |
| `isHome` | boolean | `false` | Is home page? |

```javascript
const { id, title, path, isHome } = rw.page;
```

---

## rw.node

Current component instance information.

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique instance ID |
| `title` | string | User-assigned title |
| `parent` | object | Parent node reference |

```javascript
const { id, title } = rw.node;
```

---

## rw.component

Component metadata from `info.json`.

| Property | Type | Description |
|----------|------|-------------|
| `title` | string | Component display name |
| `identifier` | string | Unique component ID |
| `assetPath` | string | Path to component assets |
| `author` | string | Component author |

```javascript
const { title, identifier, assetPath } = rw.component;
```

---

## rw.theme

Theme configuration and design tokens.

```javascript
const {
  colors,      // Color palette
  fonts,       // Font definitions
  spacing,     // Spacing scale
  breakpoints, // Responsive breakpoints
  shadows,     // Shadow definitions
  radii        // Border radius values
} = rw.theme;
```

**Colors example:**
```javascript
const { primary, secondary, background } = rw.theme.colors;
```

**Breakpoints example:**
```javascript
const { mobile, tablet, desktop } = rw.theme.breakpoints;
// mobile = 0, tablet = 768, desktop = 1024
```

---

## rw.pages

Array of all site pages for navigation building.

```javascript
const pages = rw.pages;
// [
//   { id: "...", title: "Home", path: "/", isHome: true, hidden: false },
//   { id: "...", title: "About", path: "/about/", hidden: false },
//   { id: "...", title: "Contact", path: "/contact/", hidden: false }
// ]
```

**Common pattern - build navigation:**
```javascript
const navItems = rw.pages
  .filter(page => !page.hidden)
  .map(page => ({
    title: page.title,
    url: page.path,
    isActive: page.id === rw.page.id
  }));

rw.setProps({ navItems });
```

---

## Data Availability by Mode

| Data | Edit | Preview | Publish |
|------|------|---------|---------|
| `rw.props` | ✅ | ✅ | ✅ |
| `rw.collections` | ✅ | ✅ | ✅ |
| `rw.project.mode` | `"edit"` | `"preview"` | `"publish"` |
| `rw.project.siteUrl` | ⚠️ May be empty | ⚠️ May be empty | ✅ |
| `rw.page` | ✅ | ✅ | ✅ |
| `rw.pages` | ✅ | ✅ | ✅ |
| `rw.theme` | ✅ | ✅ | ✅ |
