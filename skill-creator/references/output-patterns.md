# Output Patterns

Use these patterns when skills need to produce consistent, high-quality output.

## Template Pattern

Provide templates for output format. Match the level of strictness to your needs.

**For strict requirements (like properties.json structure):**

```markdown
## properties.json control structure

ALWAYS use this exact structure for UI controls:

{
  "title": "[Human-readable label]",
  "id": "[camelCase identifier]",
  "[controlType]": {
    "default": [default value],
    [control-specific options]
  }
}
```

**For flexible guidance (like hooks.js patterns):**

```markdown
## hooks.js structure

Here is a sensible default pattern, but adapt as needed:

const transformHook = (rw) => {
  // Destructure needed properties
  const { prop1, prop2 } = rw.props;

  // Transform data
  const result = /* transformation logic */;

  // Pass to template
  rw.setProps({ result });
};

exports.transformHook = transformHook;
```

## Examples Pattern

For skills where output quality depends on seeing examples, provide input/output pairs:

```markdown
## CSS class generation

Generate class strings following these examples:

**Example 1:**
Input: User wants responsive columns (1 on mobile, 2 on tablet, 3 on desktop)
Output:
```javascript
const gridClasses = [
  `grid-cols-${columns.mobile}`,
  `md:grid-cols-${columns.tablet}`,
  `lg:grid-cols-${columns.desktop}`
].join(' ');
```

**Example 2:**
Input: User wants conditional visibility class
Output:
```javascript
const classes = [
  baseClass,
  isVisible && 'block',
  !isVisible && 'hidden'
].filter(Boolean).join(' ');
```

Follow this style: build arrays, filter falsy values, join with spaces.
```

Examples help the agent understand the desired style and level of detail more clearly than descriptions alone.

## Elements-Specific Patterns

### properties.json Examples

Show common control configurations:

```markdown
**Switch control:**
{
  "title": "Show Border",
  "id": "showBorder",
  "switch": { "default": false }
}

**Segmented control:**
{
  "title": "Alignment",
  "id": "alignment",
  "segmented": {
    "default": "center",
    "options": [
      { "title": "Left", "value": "left" },
      { "title": "Center", "value": "center" },
      { "title": "Right", "value": "right" }
    ]
  }
}
```

### hooks.js Examples

Show common transformation patterns:

```markdown
**Conditional classes:**
const classes = [
  isFullWidth ? 'w-full' : 'max-w-4xl mx-auto',
  `text-${alignment}`
].join(' ');

**Collection processing:**
const items = rw.collections.items.map((item, index) => ({
  ...item,
  isFirst: index === 0,
  isLast: index === items.length - 1
}));
```

