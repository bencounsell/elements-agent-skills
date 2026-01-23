---
name: shared-assets
description: Share CSS, JavaScript, images, and fonts between multiple components in an Element Pack. Use when setting up shared libraries, global styles, or common resources that multiple components depend on.
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---

# Shared Assets

This skill covers the `shared` folder mechanism for sharing assets across multiple components in an Element Pack.

## When to Use

Use shared assets when:
- Multiple components depend on the same JavaScript library (Alpine.js, GSAP, etc.)
- You need global CSS fixes or styles that apply across components
- Components share common images, fonts, or other media
- You want to inject initialization scripts once per page

## Folder Structure

The `shared` folder lives inside `components/`:

```
MyElementPack.elementsdevpack/
  components/
    shared/
      assets/                 # JS, CSS, images, fonts
        images/               # Subdirectories supported
        fonts/
      templates/              # HTML/PHP injected into pages
        headStart/            # Start of <head>
        headEnd/              # End of <head>
        bodyStart/            # Start of <body>
        bodyEnd/              # End of <body>
    com.example.component1/
    com.example.component2/
```

## Quick Start: Loading a Shared Library

**1. Add the library to `shared/assets/`:**

```
shared/
  assets/
    alpine.js
```

**2. Create a template to load it in `shared/templates/headEnd/`:**

```html
<!-- shared/templates/headEnd/alpine.html -->
<script defer src="{{assetPath}}/alpine.js"></script>
```

**3. Use the library in any component:**

```html
<!-- com.example.dropdown/templates/index.html -->
<div x-data="{ open: false }">
  <button @click="open = !open">Toggle</button>
  <div x-show="open">Dropdown content</div>
</div>
```

The library loads once per page, regardless of how many components use it.

## Injection Points

Templates must be placed in one of four subfolders:

| Folder | Location | Use Cases |
|--------|----------|-----------|
| `headStart/` | Start of `<head>` | Core libraries that must load first, polyfills |
| `headEnd/` | End of `<head>` | Styles, deferred scripts, additional libraries |
| `bodyStart/` | Start of `<body>` | Early initialization, loading indicators |
| `bodyEnd/` | End of `<body>` | Feature scripts, animations, scroll handlers |

### Injection Point Examples

**Load styles in headEnd:**
```html
<!-- shared/templates/headEnd/styles.html -->
<link rel="stylesheet" href="{{assetPath}}/global.css">
```

**Load scripts at bodyEnd:**
```html
<!-- shared/templates/bodyEnd/animations.html -->
<script src="{{assetPath}}/gsap.min.js"></script>
<script src="{{assetPath}}/scroll-trigger.js"></script>
```

## Referencing Assets

### In Shared Templates

Use `{{assetPath}}` in shared templates (`shared/templates/`) to reference files in `shared/assets/`:

```html
<!-- shared/templates/headEnd/load-assets.html -->
<script src="{{assetPath}}/library.js"></script>
<link rel="stylesheet" href="{{assetPath}}/styles.css">
<img src="{{assetPath}}/images/icon.png">
```

### In Component Templates

Use `{{sharedAssetPath}}` in component templates to reference shared assets:

```html
<!-- com.example.mycomponent/templates/index.html -->
<link rel="stylesheet" href="{{sharedAssetPath}}/css/common.css">
<img src="{{sharedAssetPath}}/icons/arrow.svg">
```

To use `{{sharedAssetPath}}` in templates, pass it from hooks.js:

```javascript
// hooks.js
const transformHook = (rw) => {
  const { sharedAssetPath } = rw.component;
  rw.setProps({ sharedAssetPath });
};
exports.transformHook = transformHook;
```

## Single Inclusion Behavior

Shared files are included **once per page** per element pack, regardless of how many components from that pack are on the page. This ensures:
- Libraries are not loaded multiple times
- Initialization code runs once
- No duplicate styles or scripts

## Component Configuration via Portals

Components can configure shared libraries using portals:

```html
<!-- shared/templates/headEnd/snow-library.html -->
<script src="{{assetPath}}/snowstorm.js"></script>
```

```html
<!-- com.example.snow/templates/index.html -->
<div class="snow-demo">Snow effect active</div>

@portal(headEnd)
  <script>
    snowStorm.flakesMaxActive = {{snowAmount}};
    snowStorm.followMouse = {{followMouse}};
  </script>
@endportal
```

The library loads from shared assets; each component instance configures it via portal.

## Asset Path Variables

| Variable | Available In | Points To |
|----------|--------------|-----------|
| `{{assetPath}}` | Shared templates | `shared/assets/` |
| `{{sharedAssetPath}}` | Component templates (via hooks.js) | `shared/assets/` |
| `{{assetPath}}` | Component templates (via hooks.js) | Component's `assets/page/` |

All paths require hooks.js to pass them to templates except `{{assetPath}}` in shared templates.

## Shared vs Component-Level Assets

| Use Shared Assets | Use Component Assets |
|-------------------|---------------------|
| Library used by multiple components | Library used by one component only |
| Global styles or resets | Component-specific styles |
| Common icons or images | Component-specific images |
| Fonts used across the pack | Fonts unique to one component |

### Component-Level Assets

For component-specific assets (not shared), place files in `assets/page/`:

```
com.example.mycomponent/
  assets/
    page/
      gallery.js
      styles.css
```

Pass the path from hooks.js and use in templates:

```javascript
// hooks.js
const transformHook = (rw) => {
  const { assetPath } = rw.component;
  rw.setProps({ assetPath });
};
exports.transformHook = transformHook;
```

```html
<!-- templates/index.html -->
<script src="{{assetPath}}/gallery.js"></script>
```

## Common Patterns

### Alpine.js Setup

```
shared/
  assets/
    alpine.js
  templates/
    headEnd/
      alpine.html
```

```html
<!-- shared/templates/headEnd/alpine.html -->
<script defer src="{{assetPath}}/alpine.js"></script>
```

### GSAP Animation Library

```
shared/
  assets/
    gsap.min.js
    ScrollTrigger.min.js
  templates/
    bodyEnd/
      gsap.html
```

```html
<!-- shared/templates/bodyEnd/gsap.html -->
<script src="{{assetPath}}/gsap.min.js"></script>
<script src="{{assetPath}}/ScrollTrigger.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger);
</script>
```

### Shared CSS Framework

```
shared/
  assets/
    utilities.css
    animations.css
  templates/
    headEnd/
      styles.html
```

```html
<!-- shared/templates/headEnd/styles.html -->
<link rel="stylesheet" href="{{assetPath}}/utilities.css">
<link rel="stylesheet" href="{{assetPath}}/animations.css">
```
