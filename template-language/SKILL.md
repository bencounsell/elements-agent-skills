---
name: template-language
description: Work with the Elements template language for RapidWeaver components. Use when writing HTML templates with property insertion, conditionals (@if), loops (@each), editable content areas (@text, @richtext), dropzones, includes, and portals.
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---

# Elements Template Language

This skill helps you write templates using the Elements template language - a lightweight system using `{{...}}` syntax for property insertion and `@` directives for dynamic content.

## When to Use

- Writing component HTML templates
- Adding conditional rendering with @if/@else
- Looping over collections with @each
- Creating editable text areas
- Setting up dropzones for child components
- Including reusable template partials
- Injecting scripts/styles with portals

## Property Insertion

Use double curly braces to insert values:

```html
<h2>{{title}}</h2>
<p>{{description}}</p>
<a href="{{link.href}}">{{link.title}}</a>
```

### Dot Notation

Access nested properties:

```html
<span>{{author.name}}</span>
<img src="{{image.resource.src}}" alt="{{image.alt}}" />
```

## Directive Reference

### Content Areas

| Directive | Purpose |
|-----------|---------|
| `@text` | Editable plain text |
| `@richtext` | Editable styled text with formatting |
| `@markdown` | Editable Markdown content |
| `@dropzone` | Container for child components |

### Control Flow

| Directive | Purpose |
|-----------|---------|
| `@if` / `@elseif` / `@else` | Conditional rendering |
| `@each` | Loop over collections |

### Code Organization

| Directive | Purpose |
|-----------|---------|
| `@include` | Include external template file |
| `@includeIf` | Conditional include |
| `@template` | Define inline reusable template |

### Page Integration

| Directive | Purpose |
|-----------|---------|
| `@portal` | Inject content to page regions |
| `@anchor` | Create linkable anchor points |
| `@raw` | Disable template processing |

## Step-by-Step Instructions

### 1. Basic Template Structure

```html
<div class="my-component">
  <h2>{{heading}}</h2>
  <p>{{description}}</p>
</div>
```

### 2. Add Conditional Rendering

```html
@if(showHeader)
  <header>{{headerText}}</header>
@endif

@if(variantPrimary)
  <div class="btn-primary">{{buttonText}}</div>
@elseif(variantSecondary)
  <div class="btn-secondary">{{buttonText}}</div>
@else
  <div class="btn-default">{{buttonText}}</div>
@endif
```

> **Note:** Comparisons like `variant == "primary"` cannot be done in templates. Compute boolean values in hooks.js first:
> ```javascript
> const variantPrimary = rw.props.variant === "primary";
> const variantSecondary = rw.props.variant === "secondary";
> ```

### 3. Loop Over Collections

```html
<ul>
  @each(item in items)
    <li>{{item.title}}</li>
  @endeach
</ul>
```

### 4. Add Editable Content

```html
@text("heading", default: "Enter heading")

@richtext("content", title: "Body Content")

@markdown("article", title: "Article", default: "Write here...")
```

### 5. Create Dropzones

```html
@dropzone("content", title: "Add Content Here")

@dropzone(name: "sidebar", title: "Sidebar", horizontal: false)
```

### 6. Include Partials

```html
@include("button", label: "Click Me", style: "primary")

@includeIf(showLightbox, template: "lightbox")
```

### 7. Use Portals for Scripts

```html
@portal(bodyEnd, id: "my-script", includeOnce: true)
  <script src="{{component.assetPath}}/script.js"></script>
@endportal
```

## Examples

### Card Component

```html
<div class="card {{cardClasses}}">
  @if(showImage)
    <img src="{{image.resource.src}}" alt="{{image.alt}}" class="card-image" />
  @endif

  <div class="card-body">
    @text("title", default: "Card Title")

    @richtext("content", title: "Card Content")

    @if(showButton)
      <a href="{{buttonLink.href}}" class="btn">
        {{buttonText}}
      </a>
    @endif
  </div>
</div>
```

### Grid with Collection Items

```html
<div class="grid {{gridClasses}}">
  @each(item in items)
    <div class="grid-item">
      @if(item::isFirst)
        <span class="badge">Featured</span>
      @endif

      <h3>{{item.title}}</h3>
      <p>{{item.description}}</p>

      @if(item.link)
        <a href="{{item.link.href}}">Learn More</a>
      @endif
    </div>
  @endeach
</div>

@if(hasNoItems)
  <p class="empty-message">No items to display.</p>
@endif
```

### Navigation with Current Page

```html
<nav class="main-nav">
  <ul>
    @each(page in navItems)
      <li class="@if(page.isActive)active@endif">
        <a href="{{page.url}}">{{page.title}}</a>
      </li>
    @endeach
  </ul>
</nav>
```

### Container with Dropzone

```html
<section class="container bg-{{bgColor}} p-{{padding}}">
  <div class="container-inner max-w-{{maxWidth}}">
    @if(showHeading)
      @text("heading", default: "Section Heading")
    @endif

    @dropzone("content", title: "Section Content")
  </div>
</section>
```

### Inline Template Reuse

> **Note:** `@template` directives must be defined at the top of your template file, before any HTML output.

```html
@template("social-icon")
  <a href="{{url}}" class="social-icon" aria-label="{{label}}">
    <svg><!-- icon --></svg>
  </a>
@endtemplate

<div class="social-links">
  @if(facebookUrl)
    @include("social-icon", url: facebookUrl, label: "Facebook")
  @endif
  @if(twitterUrl)
    @include("social-icon", url: twitterUrl, label: "Twitter")
  @endif
  @if(instagramUrl)
    @include("social-icon", url: instagramUrl, label: "Instagram")
  @endif
</div>
```

## Loop Helpers

Inside `@each` loops, use `::` to access loop metadata:

| Helper | Type | Description |
|--------|------|-------------|
| `item::index` | Number | Zero-based index of the current item |
| `item::isFirst` | Boolean | True if this is the first item |
| `item::isLast` | Boolean | True if this is the last item |

```html
@each(slide in slides)
  <div class="slide @if(slide::isFirst)active@endif" data-index="{{slide::index}}">
    {{slide.content}}
  </div>
@endeach
```

## Portal Locations

| Location | Where Content Appears |
|----------|----------------------|
| `headStart` | Beginning of `<head>` |
| `headEnd` | End of `<head>` |
| `bodyStart` | After `<body>` |
| `bodyEnd` | Before `</body>` |
| `pageStart` | Document start |
| `pageEnd` | Document end |

```html
@portal(headEnd, id: "component-styles", includeOnce: true)
  <link rel="stylesheet" href="{{component.assetPath}}/styles.css" />
@endportal

@portal(bodyEnd, id: "component-script", includeOnce: true)
  <script src="{{component.assetPath}}/script.js"></script>
@endportal
```

## Guidelines

1. **Use hooks for logic** - Keep templates focused on HTML; complex processing belongs in hooks.js
2. **Meaningful names** - Use descriptive property names: `heroTitle` not `title1`
3. **Extract patterns** - Use `@include` or `@template` for repeated markup
4. **Use includeOnce** - Prevent duplicate script/style injection with portals
5. **Mode awareness** - Use `edit` and `preview` variables for mode-specific content
6. **Accessible markup** - Include proper ARIA attributes and semantic HTML

## Reference Documentation

For detailed information, see:
- [DIRECTIVES.md](references/DIRECTIVES.md) - Complete directive syntax
- [CONTROL-FLOW.md](references/CONTROL-FLOW.md) - @if and @each patterns
- [CONTENT-AREAS.md](references/CONTENT-AREAS.md) - @text, @richtext, @dropzone
