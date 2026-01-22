# Control Flow Patterns

Patterns and recipes for @if and @each directives.

## Conditional Rendering (@if)

### Basic Conditionals

```html
@if(showElement)
  <div>Visible content</div>
@endif
```

### If/Else

```html
@if(isLoggedIn)
  <span>Welcome, {{username}}</span>
@else
  <a href="/login">Sign In</a>
@endif
```

### Multiple Conditions

```html
@if(status == "active")
  <span class="badge-active">Active</span>
@elseif(status == "pending")
  <span class="badge-pending">Pending</span>
@elseif(status == "inactive")
  <span class="badge-inactive">Inactive</span>
@else
  <span class="badge-unknown">Unknown</span>
@endif
```

### Comparison Operators

```html
<!-- Equality -->
@if(count == 0)
  <p>No items</p>
@endif

@if(type != "hidden")
  <div>{{content}}</div>
@endif

<!-- Numeric comparisons -->
@if(items > 0)
  <p>{{items}} items found</p>
@endif

@if(progress >= 100)
  <span>Complete!</span>
@endif
```

### Logical Operators

```html
<!-- AND -->
@if(isPublished && isVisible)
  <article>{{content}}</article>
@endif

<!-- OR -->
@if(isAdmin || isModerator)
  <div class="admin-tools">...</div>
@endif

<!-- NOT -->
@if(!isEmpty)
  <ul>...</ul>
@endif

<!-- Combined -->
@if((isLoggedIn && hasPermission) || isAdmin)
  <button>Edit</button>
@endif
```

### Checking for Values

```html
<!-- Truthy check -->
@if(title)
  <h1>{{title}}</h1>
@endif

<!-- Check nested property -->
@if(image.resource)
  <img src="{{image.resource.src}}" />
@endif

<!-- Check link exists -->
@if(buttonLink.href)
  <a href="{{buttonLink.href}}">{{buttonLink.title}}</a>
@endif
```

### Mode-Specific Content

```html
@if(edit)
  <div class="edit-placeholder">
    Click to edit this component
  </div>
@endif

@if(preview)
  <div class="preview-notice">Preview Mode</div>
@endif

@if(!edit)
  <!-- Only show when not editing -->
  <script>initComponent();</script>
@endif
```

### Inline Conditionals

For CSS classes:
```html
<div class="item @if(isActive)active@endif @if(isHighlighted)highlighted@endif">
  {{content}}
</div>
```

For attributes:
```html
<button @if(isDisabled)disabled@endif>{{label}}</button>

<a href="{{url}}" @if(openInNewTab)target="_blank" rel="noopener"@endif>
  {{linkText}}
</a>
```

---

## Looping (@each)

### Basic Loop

```html
<ul>
  @each(item in items)
    <li>{{item.title}}</li>
  @endeach
</ul>
```

### With Properties

```html
@each(product in products)
  <div class="product">
    <img src="{{product.image.src}}" alt="{{product.image.alt}}" />
    <h3>{{product.name}}</h3>
    <p class="price">{{product.price}}</p>
    <p>{{product.description}}</p>
  </div>
@endeach
```

### Using Loop Helpers

```html
@each(slide in slides)
  <div class="slide
    @if(slide::isFirst)first active@endif
    @if(slide::isLast)last@endif
    @if(slide::isEven)even@endif
    @if(slide::isOdd)odd@endif"
    data-index="{{slide::index}}">

    <span class="counter">{{slide::number}} / {{slides::count}}</span>
    {{slide.content}}
  </div>
@endeach
```

### Empty State

```html
@if(items::isEmpty)
  <div class="empty-state">
    <p>No items to display</p>
    @if(edit)
      <p>Add items using the collection editor</p>
    @endif
  </div>
@else
  <div class="items-grid">
    @each(item in items)
      <div class="item">{{item.title}}</div>
    @endeach
  </div>
@endif
```

### Conditional Content in Loops

```html
@each(item in items)
  <div class="item">
    <h3>{{item.title}}</h3>

    @if(item.image)
      <img src="{{item.image.src}}" alt="{{item.image.alt}}" />
    @endif

    @if(item.description)
      <p>{{item.description}}</p>
    @endif

    @if(item.link)
      <a href="{{item.link.href}}">Learn More</a>
    @endif
  </div>
@endeach
```

### Nested Loops

```html
@each(category in categories)
  <section class="category">
    <h2>{{category.name}}</h2>

    <ul>
      @each(item in category.items)
        <li>{{item.title}}</li>
      @endeach
    </ul>
  </section>
@endeach
```

### First/Last Item Styling

```html
@each(item in items)
  @if(item::isFirst)
    <div class="item featured">
      <h2>{{item.title}}</h2>
      <p>{{item.fullDescription}}</p>
    </div>
  @else
    <div class="item">
      <h3>{{item.title}}</h3>
      <p>{{item.shortDescription}}</p>
    </div>
  @endif
@endeach
```

### Separator Pattern

```html
@each(tag in tags)
  <span class="tag">{{tag.name}}</span>
  @if(!tag::isLast)
    <span class="separator">, </span>
  @endif
@endeach
```

### Limited Display

Use hooks.js to limit items:
```javascript
// In hooks.js
const limitedItems = items.slice(0, 3);
rw.setProps({ limitedItems, hasMore: items.length > 3 });
```

```html
@each(item in limitedItems)
  <div>{{item.title}}</div>
@endeach

@if(hasMore)
  <a href="{{viewAllLink}}">View all {{items::count}} items</a>
@endif
```

---

## Combined Patterns

### Responsive Grid

```html
<div class="grid {{gridClasses}}">
  @each(item in items)
    <div class="grid-item">
      @if(item.image)
        <img src="{{item.image.src}}" alt="" />
      @endif
      <h3>{{item.title}}</h3>
    </div>
  @endeach
</div>

@if(items::isEmpty && edit)
  <div class="placeholder">Add items to populate the grid</div>
@endif
```

### Navigation with Active State

```html
<nav>
  <ul>
    @each(page in navItems)
      <li class="@if(page.isActive)active@endif">
        <a href="{{page.url}}"
           @if(page.isActive)aria-current="page"@endif>
          {{page.title}}
        </a>

        @if(page.children)
          <ul class="submenu">
            @each(child in page.children)
              <li>
                <a href="{{child.url}}">{{child.title}}</a>
              </li>
            @endeach
          </ul>
        @endif
      </li>
    @endeach
  </ul>
</nav>
```

### Accordion

```html
<div class="accordion">
  @each(item in accordionItems)
    <div class="accordion-item" data-index="{{item::index}}">
      <button class="accordion-header @if(item::isFirst)active@endif"
              aria-expanded="@if(item::isFirst)true@else false@endif">
        {{item.title}}
      </button>
      <div class="accordion-content @if(item::isFirst)open@endif">
        {{item.content}}
      </div>
    </div>
  @endeach
</div>
```
