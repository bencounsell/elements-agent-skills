---
name: create-component
description: Scaffold new RapidWeaver Elements components with proper folder structure, info.json, properties.json, templates, and hooks.js. Use when creating a new component from scratch or setting up the boilerplate for an Element Dev Pack component.
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---

# Create Elements Component

This skill helps you scaffold new RapidWeaver Elements components with the correct folder structure and required files.

## When to Use

- Creating a new component from scratch
- Setting up boilerplate for an Element Dev Pack
- Adding a new component to an existing pack
- User mentions "new component", "create component", or "scaffold component"

## Component Folder Structure

Every component must follow this structure:

```
com.company.componentname/
├── info.json           # Required: Component metadata
├── properties.json     # Required: UI controls definition
├── hooks.js            # Optional: Data processing logic
├── icon.pdf            # Optional: Component icon
├── templates/
│   ├── index.html      # Required: Main template
│   └── includes/       # Optional: Reusable template partials
└── assets/             # Optional: Static files (images, CSS, JS)
```

## Step-by-Step Instructions

### 1. Create the Component Folder

Use reverse domain naming: `com.companyname.componentname`

```bash
mkdir -p com.example.mycomponent/templates/includes
mkdir -p com.example.mycomponent/assets
```

### 2. Create info.json

Required fields: `identifier`, `author`, `title`, `group`

```json
{
  "identifier": "com.example.mycomponent",
  "author": "Your Name",
  "title": "My Component",
  "group": "Content",
  "tags": ["example", "starter"]
}
```

**Valid groups:** Accessibility, Animation, CMS, Content, Dynamic, Ecommerce, Forms, Interactive, Layout, Media, Navigation, Security, SEO, Utility

### 3. Create properties.json

Define UI controls users will see in the inspector:

```json
{
  "groups": [{
    "title": "Settings",
    "icon": "gearshape",
    "properties": [{
      "title": "Heading",
      "id": "heading",
      "text": {
        "default": "Hello World"
      }
    }]
  }]
}
```

### 4. Create templates/index.html

The main template using Elements Language:

```html
<div class="my-component">
  <h2>{{heading}}</h2>
  @dropzone("content", title: "Add Content")
</div>
```

### 5. Create hooks.js (Optional)

For data processing before template rendering:

```javascript
const transformHook = (rw) => {
  const { heading } = rw.props;

  rw.setProps({
    processedHeading: heading.toUpperCase()
  });
};

exports.transformHook = transformHook;
```

## Examples

### Simple Text Component

**Request:** "Create a simple heading component"

**info.json:**
```json
{
  "identifier": "com.example.heading",
  "author": "Elements Platform",
  "title": "Simple Heading",
  "group": "Content"
}
```

**properties.json:**
```json
{
  "groups": [{
    "title": "Content",
    "properties": [{
      "title": "Heading Text",
      "id": "headingText",
      "text": { "default": "Enter heading" }
    }, {
      "title": "Heading Level",
      "id": "headingLevel",
      "select": {
        "default": "h2",
        "options": ["h1", "h2", "h3", "h4", "h5", "h6"]
      }
    }]
  }]
}
```

**templates/index.html:**
```html
@if(headingLevel == "h1")
  <h1>{{headingText}}</h1>
@elseif(headingLevel == "h2")
  <h2>{{headingText}}</h2>
@elseif(headingLevel == "h3")
  <h3>{{headingText}}</h3>
@else
  <h4>{{headingText}}</h4>
@endif
```

### Container with Dropzone

**Request:** "Create a container component with customizable background"

**properties.json:**
```json
{
  "groups": [{
    "title": "Container",
    "properties": [{
      "title": "Background Color",
      "id": "bgColor",
      "themeColor": { "default": "background" }
    }, {
      "title": "Padding",
      "id": "padding",
      "slider": {
        "default": 4,
        "min": 0,
        "max": 12,
        "round": true
      }
    }]
  }]
}
```

**templates/index.html:**
```html
<div class="container bg-{{bgColor}} p-{{padding}}">
  @dropzone("content", title: "Container Content")
</div>
```

## Guidelines

1. **Always use reverse domain naming** for the identifier (e.g., `com.yourcompany.componentname`)
2. **Choose the correct group** from the allowed categories - this affects where the component appears in the UI
3. **Keep properties.json organized** - group related controls together
4. **Use meaningful property IDs** - they become template variables (e.g., `heroTitle` not `title1`)
5. **Start simple** - add complexity incrementally; a minimal component is better than a broken one
6. **Test in Elements** - verify the component loads and controls work before adding more features

## Reference Documentation

For detailed information, see:
- [COMPONENT-STRUCTURE.md](references/COMPONENT-STRUCTURE.md) - Full folder structure details
- [INFO-JSON.md](references/INFO-JSON.md) - All info.json fields and valid groups
- [PROPERTIES-JSON.md](references/PROPERTIES-JSON.md) - UI control types and options
