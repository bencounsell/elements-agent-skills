# Content Areas Reference

Detailed guide for @text, @richtext, @markdown, and @dropzone directives.

## @text - Plain Text

Editable plain text content without formatting.

### Basic Usage

```html
@text("heading")
```

### With Default Value

```html
@text("heading", default: "Welcome to Our Site")
```

### With Title (Editor Label)

```html
@text("tagline", title: "Tagline", default: "Your tagline here")
```

### Multiple Text Areas

```html
<div class="hero">
  @text("heroTitle", title: "Title", default: "Main Heading")
  @text("heroSubtitle", title: "Subtitle", default: "Supporting text")
</div>
```

### In Different Contexts

```html
<!-- As heading -->
<h1>@text("pageTitle", default: "Page Title")</h1>

<!-- As paragraph -->
<p>@text("intro", default: "Introduction text...")</p>

<!-- As button text -->
<button>@text("buttonLabel", default: "Click Here")</button>

<!-- As attribute (use property instead) -->
<img alt="{{imageAlt}}" />
```

**Note:** For attributes, use properties from properties.json rather than @text.

---

## @richtext - Formatted Text

Editable rich text with formatting options (bold, italic, links, lists).

### Basic Usage

```html
@richtext("content")
```

### With Title

```html
@richtext("bodyContent", title: "Body Content")
```

### With Default

```html
@richtext("description", title: "Description", default: "Enter your description here...")
```

### Common Patterns

```html
<!-- Article body -->
<article>
  <h1>@text("title", default: "Article Title")</h1>
  @richtext("articleBody", title: "Article Content")
</article>

<!-- Card description -->
<div class="card">
  @text("cardTitle", default: "Card Title")
  @richtext("cardContent", title: "Card Content")
</div>

<!-- Sidebar content -->
<aside>
  @richtext("sidebarContent", title: "Sidebar")
</aside>
```

### Styling Rich Text

Rich text outputs standard HTML tags. Style them using Tailwind's typography plugin.

**Note:** Always use Tailwind classes for styling—never custom CSS.

```html
<!-- Use the prose class for automatic rich text styling -->
<div class="prose prose-lg">
  @richtext("content", title: "Content")
</div>

<!-- Customize prose styles -->
<div class="prose prose-blue prose-lg max-w-none">
  @richtext("articleBody", title: "Article")
</div>

<!-- Or target specific elements with arbitrary variants -->
<div class="[&_p]:mb-4 [&_ul]:ml-6 [&_ol]:ml-6 [&_a]:text-blue-600 [&_a]:underline">
  @richtext("content", title: "Content")
</div>
```

### Using Theme Typography

For user-configurable typography styles, use the `themeTypography` control in properties.json. This displays a typography picker that lets users select from styles defined in Theme Studio.

**In properties.json:**

```json
{
  "title": "Article Style",
  "id": "articleStyle",
  "themeTypography": {
    "default": {
      "base": {
        "name": "article"
      },
      "md": {
        "name": "article-lg"
      }
    }
  }
}
```

**In template:**

```html
<div class="{{articleStyle}}">
  @richtext("content", title: "Content")
</div>
```

The `themeTypography` control outputs Tailwind prose classes based on the theme's typography configuration, making it ideal for rich text and markdown content areas.

---

## @markdown - Markdown Content

Editable Markdown that renders to HTML.

### Basic Usage

```html
@markdown("article")
```

### With Title and Default

```html
@markdown("readme", title: "README", default: "# Getting Started\n\nWrite your content here...")
```

### Use Cases

```html
<!-- Documentation -->
<div class="docs">
  @markdown("documentation", title: "Documentation")
</div>

<!-- Blog post -->
<article class="blog-post">
  @markdown("postContent", title: "Post Content", default: "# Post Title\n\nYour content here...")
</article>

<!-- Technical content -->
<div class="code-docs">
  @markdown("technicalDocs", title: "Technical Documentation")
</div>
```

### Supported Markdown Features

- Headings (`# ## ###`)
- Bold (`**text**`)
- Italic (`*text*`)
- Links (`[text](url)`)
- Lists (ordered and unordered)
- Code blocks
- Blockquotes
- Horizontal rules

---

## @dropzone - Child Components

Container that accepts child components dropped by users.

### Basic Usage

```html
@dropzone("content")
```

### With Title

```html
@dropzone("content", title: "Add Content Here")
```

### Named Dropzone

```html
@dropzone(name: "sidebar", title: "Sidebar Content")
```

### Horizontal Layout

For side-by-side children (like columns):

```html
@dropzone(name: "columns", title: "Columns", horizontal: true)
```

### Multiple Dropzones

```html
<div class="layout">
  <header>
    @dropzone("header", title: "Header Content")
  </header>

  <main>
    @dropzone("main", title: "Main Content")
  </main>

  <aside>
    @dropzone("sidebar", title: "Sidebar")
  </aside>

  <footer>
    @dropzone("footer", title: "Footer Content")
  </footer>
</div>
```

### Grid with Dropzone

```html
<div class="grid grid-cols-{{columns}}">
  @dropzone(name: "gridItems", title: "Grid Items", horizontal: true)
</div>
```

### Conditional Dropzone

```html
@if(showSidebar)
  <aside class="sidebar">
    @dropzone("sidebar", title: "Sidebar")
  </aside>
@endif
```

### Dropzones Inside Loops

Dropzones can be placed inside `@each` loops to create dynamic, repeating content areas. This is useful for components like tab panels, accordion sections, or multi-column layouts where each iteration needs its own dropzone.

The dropzone name and title must be static text—you cannot use dynamic values like `{{index}}` or template variables inside the dropzone declaration. Elements automatically handles creating unique dropzones for each loop iteration.

```html
<!-- Tab panels with per-tab dropzones -->
@each(tab in tabs)
  <div class="tab-panel">
    @dropzone("panel", title: "Panel")
  </div>
@endeach

<!-- Accordion with content dropzones -->
@each(section in sections)
  <div class="accordion-item">
    <button class="accordion-header">
      {{section.title}}
    </button>
    <div class="accordion-body">
      @dropzone("content", title: "Section Content")
    </div>
  </div>
@endeach
```

---

## Best Practices

### Naming Conventions

Use descriptive, unique IDs:

```html
<!-- Good -->
@text("heroTitle")
@text("heroSubtitle")
@richtext("heroDescription")
@dropzone("heroContent")

<!-- Bad -->
@text("title")      <!-- Too generic -->
@text("text1")      <!-- Not descriptive -->
@text("t")          <!-- Too short -->
```

### Providing Defaults

Always provide helpful defaults:

```html
<!-- Good - guides the user -->
@text("heading", default: "Enter your heading here")
@richtext("content", default: "<p>Add your content...</p>")

<!-- Bad - no guidance -->
@text("heading")
@richtext("content")
```

### Grouping Related Content

```html
<section class="testimonial">
  @text("quote", title: "Quote", default: "Customer testimonial...")
  @text("author", title: "Author Name", default: "John Doe")
  @text("role", title: "Author Role", default: "CEO, Company")
</section>
```

### Edit Mode Placeholders

Show helpful messages when the a property or properties are empty:

```html
@if(!hasImages)
  <div rwResourceDropZone="images">
      <!-- Only visible in edit mode when dropzone is empty -->
      <div class="opacity-50 p-8 text-center">
        Drop folder here to add images
      </div>
  </div>
@endif
```

### Accessibility

```html
<!-- Provide context -->
<section aria-labelledby="section-heading">
  <h2 id="section-heading">
    @text("sectionTitle", default: "Section Title")
  </h2>
  @richtext("sectionContent")
</section>
```
