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

Compute boolean values in hooks.js, then use them in templates:

```javascript
// hooks.js
function processProperties(rw) {
  rw.isActive = rw.status === "active";
  rw.isPending = rw.status === "pending";
  rw.isInactive = rw.status === "inactive";
}
```

```html
@if(isActive)
  <span class="badge-active">Active</span>
@elseif(isPending)
  <span class="badge-pending">Pending</span>
@elseif(isInactive)
  <span class="badge-inactive">Inactive</span>
@else
  <span class="badge-unknown">Unknown</span>
@endif
```

### Complex Conditions

Comparison operators (`==`, `!=`, `>`, `<`) and logical operators (`&&`, `||`) are **not supported** in templates. Compute these in hooks.js instead:

```javascript
// hooks.js
function processProperties(rw) {
  // Comparisons
  rw.hasNoItems = rw.count === 0;
  rw.hasItems = rw.items.length > 0;
  rw.isComplete = rw.progress >= 100;
  rw.isVisible = rw.type !== "hidden";

  // Logical combinations
  rw.showArticle = rw.isPublished && rw.isVisible;
  rw.hasAdminAccess = rw.isAdmin || rw.isModerator;
  rw.canEdit = (rw.isLoggedIn && rw.hasPermission) || rw.isAdmin;
}
```

```html
@if(hasNoItems)
  <p>No items</p>
@endif

@if(hasItems)
  <p>{{itemCount}} items found</p>
@endif

@if(isComplete)
  <span>Complete!</span>
@endif

@if(showArticle)
  <article>{{content}}</article>
@endif

@if(hasAdminAccess)
  <div class="admin-tools">...</div>
@endif

@if(canEdit)
  <button>Edit</button>
@endif
```

### Negation

The `!` operator **is supported** in templates:

```html
@if(!isEmpty)
  <ul>...</ul>
@endif

@if(!edit)
  <!-- Only in preview/published mode -->
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
    @if(slide::isLast)last@endif"
    data-index="{{slide::index}}">
    {{slide.content}}
  </div>
@endeach
```

### Empty State

Use a boolean computed in hooks.js to check for empty collections:

```html
@if(hasNoItems)
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
  <a href="{{viewAllLink}}">View all {{itemCount}} items</a>
@endif
```

---

## Combined Patterns

### Responsive Grid

```javascript
// hooks.js - compute isEmpty boolean
const transformHook = (rw) => {
  const { items } = rw.collections;
  rw.setProps({
    items,
    hasNoItems: items.length === 0
  });
};
exports.transformHook = transformHook;
```

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

@if(hasNoItems)
  @if(edit)
    <div class="placeholder">Add items to populate the grid</div>
  @endif
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
