# Component Folder Structure

A component is a self-contained, reusable building block in Elements. Each component lives in its own folder within an Element Pack.

## Directory Structure

```
com.companyname.componentname/
├── info.json                 # Required: Component metadata
├── properties.json           # Required: UI controls definition
├── properties.config.json    # Optional: Build tools config
├── hooks.js                  # Optional: Data processing logic
├── hooks.source.js           # Optional: Source for build tools
├── icon.pdf                  # Optional: Main icon
├── icon-dark.pdf             # Optional: Dark mode icon
├── paletteIcon.pdf           # Optional: Palette icon
├── paletteIcon-dark.pdf      # Optional: Dark mode palette icon
├── collections/              # Optional: Collection definitions
│   └── *.json
├── templates/
│   ├── index.html            # Required: Main template entry point
│   ├── *.html                # Additional HTML templates
│   ├── *.css                 # Styles (processed & concatenated)
│   ├── *.js                  # Scripts (processed & concatenated)
│   ├── includes/             # Reusable template partials
│   ├── headStart/            # Injected at start of <head>
│   ├── headEnd/              # Injected at end of </head>
│   ├── bodyStart/            # Injected after <body>
│   ├── bodyEnd/              # Injected before </body>
│   ├── pageStart/            # Injected at document start
│   ├── pageEnd/              # Injected at document end
│   └── backend/              # Server-side files (PHP, etc.)
└── assets/                   # Static files (not processed)
    ├── images/
    ├── fonts/
    └── *.js, *.css
```

## File Descriptions

### Required Files

| File | Purpose |
|------|---------|
| `info.json` | Defines component metadata: identifier, title, author, group |
| `properties.json` | Defines UI controls shown in the inspector |
| `templates/index.html` | Main HTML template entry point |

### Optional Files

| File | Purpose |
|------|---------|
| `hooks.js` | JavaScript logic for data processing before rendering |
| `hooks.source.js` | Source file when using Build Tools |
| `properties.config.json` | Simplified property definitions with Build Tools |
| `icon.pdf` / `icon-dark.pdf` | Component icons for light/dark mode |
| `paletteIcon.pdf` | Icon shown in the component palette |

### Template Directories

| Directory | When Rendered |
|-----------|---------------|
| `headStart/` | Beginning of `<head>` tag |
| `headEnd/` | End of `<head>` tag (before `</head>`) |
| `bodyStart/` | Right after `<body>` tag |
| `bodyEnd/` | Right before `</body>` tag |
| `pageStart/` | Very beginning of document |
| `pageEnd/` | Very end of document |
| `backend/` | Files deployed to server, not included in page |

## Naming Conventions

### Component Identifier

Use reverse domain name format:
- `com.yourcompany.componentname`
- `com.yourcompany.category.componentname`

Examples:
- `com.acme.hero`
- `com.acme.navigation.navbar`
- `com.acme.forms.contact`

### Property IDs

Use camelCase, be descriptive:
- Good: `heroTitle`, `backgroundColor`, `showButton`
- Bad: `title1`, `bg`, `btn`

## Minimal Component Example

The simplest valid component:

**com.example.minimal/info.json:**
```json
{
  "identifier": "com.example.minimal",
  "author": "Your Name",
  "title": "Minimal Component",
  "group": "Utility"
}
```

**com.example.minimal/properties.json:**
```json
{
  "groups": []
}
```

**com.example.minimal/templates/index.html:**
```html
<div>Hello from minimal component!</div>
```
