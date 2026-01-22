# Elements Template Directives Reference

Complete syntax reference for all Elements template directives.

## Property Insertion

### Basic Syntax

```html
{{propertyName}}
```

### Dot Notation

```html
{{object.property}}
{{image.resource.src}}
{{link.href}}
```

### With Default (in hooks.js)

Properties should have defaults set in properties.json or hooks.js, not in templates.

---

## @text

Editable plain text area.

**Syntax:**
```html
@text("id")
@text("id", default: "Default text")
@text("id", title: "Display Title", default: "Default")
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `id` | Yes | Unique identifier (first positional arg) |
| `default` | No | Default text content |
| `title` | No | Label shown in editor |

**Examples:**
```html
@text("heading")
@text("heading", default: "Welcome")
@text("tagline", title: "Tagline", default: "Your tagline here")
```

---

## @richtext

Editable rich text with formatting options.

**Syntax:**
```html
@richtext("id")
@richtext("id", title: "Label")
@richtext("id", title: "Label", default: "Default content")
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `id` | Yes | Unique identifier |
| `title` | No | Label shown in editor |
| `default` | No | Default content |

**Examples:**
```html
@richtext("content")
@richtext("body", title: "Body Content")
@richtext("description", title: "Description", default: "<p>Enter description...</p>")
```

---

## @markdown

Editable Markdown text area.

**Syntax:**
```html
@markdown("id")
@markdown("id", title: "Label", default: "# Heading")
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `id` | Yes | Unique identifier |
| `title` | No | Label shown in editor |
| `default` | No | Default Markdown content |

**Examples:**
```html
@markdown("article")
@markdown("readme", title: "README", default: "# Project Title\n\nDescription here...")
```

---

## @dropzone

Container for child components.

**Syntax:**
```html
@dropzone("name")
@dropzone("name", title: "Label")
@dropzone(name: "id", title: "Label", horizontal: true)
```

**Parameters:**
| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Unique identifier |
| `title` | No | Label shown in editor |
| `horizontal` | No | Horizontal layout (default: false) |

**Examples:**
```html
@dropzone("content")
@dropzone("main", title: "Main Content")
@dropzone(name: "items", title: "Grid Items", horizontal: true)
```

---

## @if / @elseif / @else

Conditional rendering.

**Syntax:**
```html
@if(condition)
  <!-- content -->
@endif

@if(condition)
  <!-- if true -->
@else
  <!-- if false -->
@endif

@if(condition1)
  <!-- condition1 true -->
@elseif(condition2)
  <!-- condition2 true -->
@else
  <!-- all false -->
@endif
```

**Supported in templates:**
- Boolean property checks: `@if(showHeader)`
- Negation with `!`: `@if(!edit)`
- Built-in mode variables: `edit`, `preview`
- Loop helpers: `item::isFirst`, `item::isLast`, `item::index`

**NOT supported in templates:**
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators (`&&`, `||`)
- String comparisons

For complex logic, compute boolean values in hooks.js and pass them to the template.

**Examples:**
```html
<!-- Simple boolean check -->
@if(showHeader)
  <header>{{headerText}}</header>
@endif

<!-- Negation -->
@if(!edit)
  <p>Visible when published</p>
@endif

<!-- Edit/preview mode detection -->
@if(edit)
  <p>Edit mode content</p>
@elseif(preview)
  <p>Preview mode content</p>
@else
  <p>Published content</p>
@endif

<!-- Using computed booleans from hooks.js -->
@if(isPrimary)
  <button class="btn-primary">{{text}}</button>
@elseif(isSecondary)
  <button class="btn-secondary">{{text}}</button>
@else
  <button class="btn-default">{{text}}</button>
@endif
```

**In hooks.js** (for complex conditions):
```javascript
function processProperties(rw) {
  // Compute boolean values for template use
  rw.isPrimary = rw.variant === "primary";
  rw.isSecondary = rw.variant === "secondary";
  rw.showAdminPanel = rw.isLoggedIn && rw.hasPermission;
  rw.hasMultipleItems = rw.items.length > 1;
}
```

---

## @each

Loop over collections.

**Syntax:**
```html
@each(item in collection)
  <!-- use {{item.property}} -->
@endeach
```

**Loop Helpers:**
| Helper | Type | Description |
|--------|------|-------------|
| `item::index` | Number | Zero-based index of the current item |
| `item::isFirst` | Boolean | True if this is the first item |
| `item::isLast` | Boolean | True if this is the last item |

**Examples:**
```html
<ul>
  @each(item in items)
    <li>{{item.title}}</li>
  @endeach
</ul>

@each(slide in slides)
  <div class="slide @if(slide::isFirst)active@endif" data-index="{{slide::index}}">
    {{slide.content}}
  </div>
@endeach
```

---

## @include

Include external template file.

**Syntax:**
```html
@include("templateName")
@include("templateName", param1: value1, param2: value2)
```

**Notes:**
- Template files live in `templates/include/` folder
- File extension is optional (`.html` assumed)
- Parameters become available as variables in the included template

**Examples:**
```html
@include("button")
@include("button", label: "Click Me", variant: "primary")
@include("card", title: item.title, image: item.image)
```

---

## @includeIf

Conditional include.

**Syntax:**
```html
@includeIf(condition, template: "templateName")
@includeIf(condition, template: "templateName", param: value)
```

**Examples:**
```html
@includeIf(showLightbox, template: "lightbox")
@includeIf(hasImage, template: "image-block", src: image.src)
```

---

## @template

Define inline reusable template.

> **Note:** `@template` directives must be defined at the top of your template file, before any HTML output.

**Syntax:**
```html
@template("name")
  <!-- template content -->
@endtemplate
```

**Examples:**
```html
@template("badge")
  <span class="badge badge-{{color}}">{{text}}</span>
@endtemplate

@include("badge", color: "primary", text: "New")
@include("badge", color: "success", text: "Active")
```

---

## @portal

Inject content to specific page locations.

**Syntax:**
```html
@portal(location)
  <!-- content -->
@endportal

@portal(location, id: "unique-id", includeOnce: true)
  <!-- content -->
@endportal
```

**Locations:**
| Location | Description |
|----------|-------------|
| `headStart` | Beginning of `<head>` |
| `headEnd` | End of `<head>` |
| `bodyStart` | After `<body>` |
| `bodyEnd` | Before `</body>` |
| `pageStart` | Document start |
| `pageEnd` | Document end |

**Parameters:**
| Parameter | Description |
|-----------|-------------|
| `id` | Unique identifier for deduplication |
| `includeOnce` | Only include once per page |

**Examples:**
```html
@portal(headEnd, id: "my-styles", includeOnce: true)
  <link rel="stylesheet" href="styles.css" />
@endportal

@portal(bodyEnd, id: "my-script", includeOnce: true)
  <script src="script.js"></script>
@endportal
```

---

## @anchor

Create linkable anchor point.

**Syntax:**
```html
@anchor("id")
```

**Examples:**
```html
<section id="@anchor("features")">
  <h2>Features</h2>
</section>

<section id="@anchor("pricing")">
  <h2>Pricing</h2>
</section>
```

---

## @raw

Disable template processing (for CMS placeholders).

**Syntax:**
```html
@raw()
  <!-- content not processed -->
@endraw
```

**Examples:**
```html
@raw()
  <div>{{cms.field}}</div>
  <p>{{handlebars.variable}}</p>
@endraw
```
