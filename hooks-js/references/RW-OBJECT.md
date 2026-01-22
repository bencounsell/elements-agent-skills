# The rw Object Reference

The `rw` object is passed to your transform hook and provides access to all component data and helper functions.

## Available Data Properties

### rw.props

UI control values from `properties.json`. Each property `id` becomes a key.

```javascript
const { heading, showButton, padding } = rw.props;
```

### rw.responsiveProps

Responsive property values organized by breakpoint.

```javascript
const { columns } = rw.responsiveProps;
// columns = { mobile: "1", tablet: "2", desktop: "3" }
```

### rw.collections

Collection data defined in the component's `collections/` folder.

```javascript
const { slides, items } = rw.collections;
// slides = [{ title: "...", image: {...} }, ...]
```

### rw.project

Project-level data:

| Property | Type | Description |
|----------|------|-------------|
| `title` | string | Project/site title |
| `mode` | string | `"edit"`, `"preview"`, or `"publish"` |
| `siteUrl` | string | Published site URL |
| `basePath` | string | Base path for the site |

```javascript
const { mode, siteUrl } = rw.project;
```

### rw.page

Current page data:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique page identifier |
| `title` | string | Page title |
| `filename` | string | Output filename |
| `path` | string | Page path/URL |
| `isHome` | boolean | Is this the home page? |

```javascript
const { title, filename, isHome } = rw.page;
```

### rw.node

Component instance (node) data:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique node identifier |
| `title` | string | User-set node title |
| `parent` | object | Parent node reference |

```javascript
const { id, title } = rw.node;
```

### rw.component

Component metadata:

| Property | Type | Description |
|----------|------|-------------|
| `title` | string | Component title from info.json |
| `identifier` | string | Component identifier |
| `assetPath` | string | Path to component assets |

```javascript
const { assetPath } = rw.component;
```

### rw.theme

Theme data including design tokens:

| Property | Type | Description |
|----------|------|-------------|
| `colors` | object | Theme color definitions |
| `fonts` | object | Theme font definitions |
| `spacing` | object | Theme spacing scale |
| `breakpoints` | object | Responsive breakpoints |

```javascript
const { colors, breakpoints } = rw.theme;
```

### rw.pages

Site navigation tree - array of all pages for building navigation.

```javascript
const navPages = rw.pages.filter(p => !p.hidden);
```

## Available Functions

### rw.setProps(object)

Pass data to templates. Merges with existing props.

```javascript
rw.setProps({
  computedValue: 42,
  classes: 'my-class another-class',
  items: processedItems
});
```

### rw.setRootElement(config)

Configure the component's root HTML element:

```javascript
rw.setRootElement({
  tag: 'section',           // HTML tag (default: 'div')
  classes: 'my-component',  // CSS classes
  attributes: {             // HTML attributes
    'data-id': rw.node.id,
    'aria-label': 'My Component'
  }
});
```

### rw.addAnchor(id, title)

Register an anchor point for the link picker:

```javascript
rw.addAnchor('my-section', 'My Section');
// Creates anchor: #my-section
```

### rw.resizeResource(resource, options)

Resize an image resource:

```javascript
const resized = rw.resizeResource(imageResource, {
  width: 800,
  height: 600,
  mode: 'fill'    // 'fill', 'fit', or 'stretch'
});
// Returns: { src: "path/to/resized.jpg", width: 800, height: 600 }
```

**Options:**

| Option | Type | Description |
|--------|------|-------------|
| `width` | number | Target width in pixels |
| `height` | number | Target height in pixels |
| `mode` | string | `"fill"` (crop), `"fit"` (contain), `"stretch"` |
| `quality` | number | JPEG quality (0-100) |

### rw.getBreakpoints()

Get theme breakpoint configuration:

```javascript
const breakpoints = rw.getBreakpoints();
// Returns: { mobile: 0, tablet: 768, desktop: 1024 }
```

## Usage Patterns

### Accessing Nested Properties

```javascript
const { heroImage } = rw.props;

if (heroImage && heroImage.resource) {
  const src = heroImage.resource.src;
  const alt = heroImage.alt || '';
}
```

### Checking Project Mode

```javascript
const { mode } = rw.project;

const isEditing = mode === 'edit';
const isPreviewing = mode === 'preview';
const isPublishing = mode === 'publish';
```

### Working with Theme Data

```javascript
const { colors } = rw.theme;

// Access specific color
const primaryColor = colors.primary;
```
