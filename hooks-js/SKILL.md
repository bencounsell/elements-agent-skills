---
name: hooks-js
description: Write and debug hooks.js files for RapidWeaver Elements components. Use when processing data before template rendering, generating CSS classes, working with collections, handling resources, or detecting edit/preview modes.
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---

# Elements hooks.js

This skill helps you write `hooks.js` files that process and transform data before it reaches your component templates.

## When to Use

- Processing or transforming property values before rendering
- Generating dynamic CSS class strings
- Working with collection data
- Handling image resources and resizing
- Detecting edit vs preview mode
- Computing derived values from multiple properties

## Component Lifecycle

```
properties.json → hooks.js → templates
```

1. **Properties** define UI controls and their values
2. **Hooks** process and transform those values
3. **Templates** render the final HTML output

## Basic Structure

```javascript
const transformHook = (rw) => {
  // Access properties from UI controls
  const { title, isVisible } = rw.props;

  // Transform and pass data to templates
  rw.setProps({
    message: `Hello, ${title}!`,
    displayClass: isVisible ? 'block' : 'hidden'
  });
};

exports.transformHook = transformHook;
```

## The `rw` Object

### Available Data

| Property | Description |
|----------|-------------|
| `rw.props` | UI control values from properties.json |
| `rw.responsiveProps` | Responsive property values by breakpoint |
| `rw.collections` | Component collections data |
| `rw.project` | Project data (title, mode, siteUrl) |
| `rw.page` | Current page data (id, title, filename) |
| `rw.node` | Component node data (id, title, parent) |
| `rw.component` | Component metadata (title, assetPath) |
| `rw.theme` | Theme data including breakpoints |
| `rw.pages` | Site navigation page tree |

### Available Functions

| Function | Description |
|----------|-------------|
| `rw.setProps(obj)` | Pass data to templates |
| `rw.setRootElement(config)` | Configure root HTML element |
| `rw.addAnchor(id, title)` | Register anchor for link picker |
| `rw.resizeResource(resource, options)` | Resize image resources |
| `rw.getBreakpoints()` | Get theme breakpoint data |

## Step-by-Step Instructions

### 1. Access Property Values

```javascript
const transformHook = (rw) => {
  // Destructure the properties you need
  const { heading, showButton, buttonText } = rw.props;
};
```

### 2. Transform Values

```javascript
const transformHook = (rw) => {
  const { padding } = rw.props;

  // Double the padding value
  const doubledPadding = padding * 2;

  rw.setProps({
    computedPadding: doubledPadding
  });
};
```

### 3. Generate CSS Classes

```javascript
const transformHook = (rw) => {
  const { size, alignment, isFullWidth } = rw.props;

  const classes = [
    `size-${size}`,
    `text-${alignment}`,
    isFullWidth && 'w-full'
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

### 4. Detect Edit/Preview Mode

```javascript
const transformHook = (rw) => {
  const { mode } = rw.project;

  rw.setProps({
    isEditMode: mode === 'edit',
    isPreviewMode: mode === 'preview',
    isPublished: mode === 'publish'
  });
};
```

## Examples

### Conditional Class Generation

**properties.json:**
```json
{
  "title": "Full Width",
  "id": "isFullWidth",
  "switch": { "default": false }
},
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

**hooks.js:**
```javascript
const transformHook = (rw) => {
  const { isFullWidth, alignment } = rw.props;

  const containerClasses = [
    isFullWidth ? 'w-full' : 'max-w-4xl mx-auto',
    `text-${alignment}`
  ].join(' ');

  rw.setProps({ containerClasses });
};

exports.transformHook = transformHook;
```

**template.html:**
```html
<div class="{{containerClasses}}">
  {{content}}
</div>
```

### Working with Collections

**hooks.js:**
```javascript
const transformHook = (rw) => {
  const { slides } = rw.collections;

  // Process collection items
  const processedSlides = slides.map((slide, index) => ({
    ...slide,
    isFirst: index === 0,
    isLast: index === slides.length - 1,
    number: index + 1
  }));

  rw.setProps({
    slides: processedSlides,
    totalSlides: slides.length,
    hasMultipleSlides: slides.length > 1
  });
};

exports.transformHook = transformHook;
```

### Image Resource Processing

**hooks.js:**
```javascript
const transformHook = (rw) => {
  const { heroImage } = rw.props;

  if (heroImage && heroImage.resource) {
    // Create resized versions
    const thumbnail = rw.resizeResource(heroImage.resource, {
      width: 400,
      height: 300,
      mode: 'fill'
    });

    const fullSize = rw.resizeResource(heroImage.resource, {
      width: 1920,
      height: 1080,
      mode: 'fit'
    });

    rw.setProps({
      thumbnailSrc: thumbnail.src,
      fullSizeSrc: fullSize.src,
      imageAlt: heroImage.alt || ''
    });
  }
};

exports.transformHook = transformHook;
```

### Building Navigation from Pages

**hooks.js:**
```javascript
const transformHook = (rw) => {
  const { pages } = rw;

  // Filter to only published pages
  const navItems = pages
    .filter(page => !page.hidden)
    .map(page => ({
      title: page.title,
      url: page.url,
      isCurrentPage: page.id === rw.page.id
    }));

  rw.setProps({ navItems });
};

exports.transformHook = transformHook;
```

### Responsive Values

**hooks.js:**
```javascript
const transformHook = (rw) => {
  const { columns } = rw.responsiveProps;

  // columns = { mobile: "1", tablet: "2", desktop: "3" }

  const gridClasses = [
    `grid-cols-${columns.mobile}`,
    `md:grid-cols-${columns.tablet}`,
    `lg:grid-cols-${columns.desktop}`
  ].join(' ');

  rw.setProps({ gridClasses });
};

exports.transformHook = transformHook;
```

## Guidelines

1. **Keep hooks focused** - Do data processing only; leave HTML to templates
2. **Use destructuring** - Extract only the properties you need from `rw.props`
3. **Filter Boolean** - Use `.filter(Boolean)` to remove falsy values from class arrays
4. **Handle missing data** - Check if resources/collections exist before processing
5. **Don't mutate** - Create new objects/arrays instead of modifying `rw.props` directly
6. **Export correctly** - Always include `exports.transformHook = transformHook;`

## Common Patterns

### Combine Multiple Properties into Classes

```javascript
const classes = [
  sizeClass,
  colorClass,
  isActive && 'active',
  isDisabled && 'disabled'
].filter(Boolean).join(' ');
```

### Provide Defaults

```javascript
const title = rw.props.title || 'Default Title';
const items = rw.collections.items || [];
```

### Conditional Properties

```javascript
rw.setProps({
  ...(showHeader && { headerContent: processedHeader }),
  ...(hasItems && { itemCount: items.length })
});
```

## Reference Documentation

For detailed information, see:
- [RW-OBJECT.md](references/RW-OBJECT.md) - Complete rw object API
- [COMMON-PATTERNS.md](references/COMMON-PATTERNS.md) - Recipes and patterns
- [AVAILABLE-DATA.md](references/AVAILABLE-DATA.md) - All available data properties
