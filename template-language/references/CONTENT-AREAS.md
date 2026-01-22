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
@richtext("description", title: "Description", default: "<p>Enter your description here...</p>")
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

Rich text outputs standard HTML tags. Style them in your CSS:

```css
/* In your component CSS */
.my-component p {
  margin-bottom: 1em;
}

.my-component ul, .my-component ol {
  margin-left: 1.5em;
}

.my-component a {
  color: var(--link-color);
}

.my-component strong {
  font-weight: bold;
}

.my-component em {
  font-style: italic;
}
```

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

### Dropzone in Loop Items

For repeatable sections, use collections instead of dropzones in loops:

```html
<!-- DON'T do this -->
@each(item in items)
  @dropzone("item-content")  <!-- Won't work as expected -->
@endeach

<!-- DO this instead - use collection data -->
@each(item in items)
  <div class="item">
    {{item.content}}
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

Show helpful messages when content is empty:

```html
<div class="content-area">
  @dropzone("content", title: "Page Content")

  @if(edit)
    <!-- Only visible in edit mode -->
    <div class="edit-hint" style="opacity: 0.5; padding: 2rem; text-align: center;">
      Drop components here to build your page
    </div>
  @endif
</div>
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
