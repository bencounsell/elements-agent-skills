# Class Generation Reference

Patterns for building dynamic Tailwind class strings in hooks.js.

## The Core Pattern

The standard pattern for generating class strings uses an array, filter, and join:

```javascript
const classes = [
  'base-class',
  'another-class',
  condition && 'conditional-class',
  anotherCondition && 'another-conditional-class'
]
  .filter(Boolean)
  .join(' ');
```

### How It Works

1. **Array** - Start with an array of class strings and conditional expressions
2. **Conditional inclusion** - `condition && 'class'` returns the class string if true, `false` if not
3. **Filter** - `.filter(Boolean)` removes all falsy values (`false`, `null`, `undefined`, `''`, `0`)
4. **Join** - `.join(' ')` combines the remaining classes into a space-separated string

## Basic Examples

### Static Classes

```javascript
const transformHook = (rw) => {
  const classes = [
    'flex',
    'items-center',
    'gap-4',
    'p-4'
  ].join(' ');

  rw.setProps({ classes });
};
```

Output: `flex items-center gap-4 p-4`

### Boolean Conditions

```javascript
const transformHook = (rw) => {
  const { isActive, isDisabled, showBorder } = rw.props;

  const classes = [
    'btn',
    isActive && 'btn-active',
    isDisabled && 'btn-disabled opacity-50 cursor-not-allowed',
    showBorder && 'border border-surface-300'
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

### Value-Based Conditions

```javascript
const transformHook = (rw) => {
  const { variant, size } = rw.props;

  const classes = [
    'btn',
    // Variant
    variant === 'primary' && 'bg-brand-500 text-white',
    variant === 'secondary' && 'bg-surface-100 text-surface-900',
    variant === 'outline' && 'border-2 border-brand-500 text-brand-500',
    variant === 'ghost' && 'text-brand-500 hover:bg-brand-50',
    // Size
    size === 'sm' && 'px-3 py-1 text-sm',
    size === 'md' && 'px-4 py-2 text-base',
    size === 'lg' && 'px-6 py-3 text-lg'
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

## Object Mapping

Map property values to class sets using objects:

```javascript
const transformHook = (rw) => {
  const { variant } = rw.props;

  const variantClasses = {
    primary: 'bg-brand-500 text-white hover:bg-brand-600',
    secondary: 'bg-surface-100 text-surface-900 hover:bg-surface-200',
    outline: 'border-2 border-brand-500 text-brand-500 hover:bg-brand-50',
    ghost: 'text-brand-500 hover:bg-brand-50'
  };

  const classes = [
    'btn',
    'px-4 py-2',
    'rounded-md',
    'transition-colors',
    variantClasses[variant]
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

### Multiple Object Maps

```javascript
const transformHook = (rw) => {
  const { variant, size, rounded } = rw.props;

  const variantClasses = {
    primary: 'bg-brand-500 text-white',
    secondary: 'bg-surface-100 text-surface-900'
  };

  const sizeClasses = {
    sm: 'px-3 py-1 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  const roundedClasses = {
    none: 'rounded-none',
    sm: 'rounded-sm',
    md: 'rounded-md',
    lg: 'rounded-lg',
    full: 'rounded-full'
  };

  const classes = [
    'btn',
    variantClasses[variant],
    sizeClasses[size],
    roundedClasses[rounded]
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

## Combining Multiple Class Sources

### From Properties and Computed Values

```javascript
const transformHook = (rw) => {
  const { bgColor, padding, textColor, customClasses } = rw.props;

  const classes = [
    // From theme controls (already formatted)
    bgColor,
    padding,
    textColor,
    // Computed classes
    'relative',
    'overflow-hidden',
    // User's custom classes
    customClasses
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

### Merging Base and Override Classes

```javascript
const transformHook = (rw) => {
  const { variant, customClasses } = rw.props;

  // Base classes that always apply
  const baseClasses = 'inline-flex items-center justify-center transition-colors';

  // Variant-specific classes
  const variantClasses = variant === 'primary'
    ? 'bg-brand-500 text-white'
    : 'bg-surface-100 text-surface-900';

  // Combine all sources
  const classes = [baseClasses, variantClasses, customClasses]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

## Responsive Class Generation

### Building Responsive Classes Manually

```javascript
const transformHook = (rw) => {
  const { columns } = rw.responsiveProps;

  // columns = { base: "1", md: "2", lg: "3" }

  const gridClasses = Object.entries(columns)
    .map(([breakpoint, value]) => {
      const prefix = breakpoint === 'base' ? '' : `${breakpoint}:`;
      return `${prefix}grid-cols-${value}`;
    })
    .join(' ');

  rw.setProps({ gridClasses });
};
```

Output: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

### Helper Function for Responsive Values

```javascript
const buildResponsiveClasses = (values, classTemplate) => {
  return Object.entries(values)
    .map(([breakpoint, value]) => {
      const prefix = breakpoint === 'base' ? '' : `${breakpoint}:`;
      return `${prefix}${classTemplate.replace('{{value}}', value)}`;
    })
    .join(' ');
};

const transformHook = (rw) => {
  const { padding, fontSize } = rw.responsiveProps;

  const paddingClasses = buildResponsiveClasses(padding, 'p-{{value}}');
  const fontClasses = buildResponsiveClasses(fontSize, 'text-{{value}}');

  rw.setProps({ paddingClasses, fontClasses });
};
```

## Conditional Class Groups

### Grouped Conditions

```javascript
const transformHook = (rw) => {
  const { hasOverlay, overlayColor, overlayOpacity } = rw.props;

  // Group related classes
  const overlayClasses = hasOverlay
    ? [overlayColor, overlayOpacity, 'absolute inset-0'].filter(Boolean).join(' ')
    : '';

  rw.setProps({ overlayClasses });
};
```

### Nested Conditionals

```javascript
const transformHook = (rw) => {
  const { buttonStyle, showIcon, iconPosition } = rw.props;

  const classes = [
    'btn',
    buttonStyle,
    // Icon-related classes only when showing icon
    showIcon && 'inline-flex items-center gap-2',
    showIcon && iconPosition === 'right' && 'flex-row-reverse'
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ classes });
};
```

## State-Based Classes

### Hover State Classes

```javascript
const transformHook = (rw) => {
  const { bgColor, bgColorHover } = rw.props;

  // bgColor = "bg-brand-500"
  // bgColorHover = "hover:bg-brand-600"

  const classes = [bgColor, bgColorHover].filter(Boolean).join(' ');

  rw.setProps({ classes });
};
```

### Multiple States

```javascript
const transformHook = (rw) => {
  const { isInteractive } = rw.props;

  const stateClasses = isInteractive
    ? 'hover:shadow-lg focus:ring-2 focus:ring-brand-500 active:scale-95 transition-all'
    : '';

  rw.setProps({ stateClasses });
};
```

## Collection Item Classes

### Classes Based on Position

```javascript
const transformHook = (rw) => {
  const items = rw.collections.items || [];

  const processedItems = items.map((item, index) => {
    const isFirst = index === 0;
    const isLast = index === items.length - 1;

    const itemClasses = [
      'p-4',
      isFirst && 'rounded-t-lg',
      isLast && 'rounded-b-lg',
      !isLast && 'border-b border-surface-200'
    ]
      .filter(Boolean)
      .join(' ');

    return {
      ...item,
      itemClasses
    };
  });

  rw.setProps({ items: processedItems });
};
```

### Alternating Classes

```javascript
const transformHook = (rw) => {
  const items = rw.collections.items || [];

  const processedItems = items.map((item, index) => {
    const isEven = index % 2 === 0;

    const rowClasses = [
      'p-4',
      isEven ? 'bg-surface-50' : 'bg-white'
    ].join(' ');

    return {
      ...item,
      rowClasses
    };
  });

  rw.setProps({ items: processedItems });
};
```

## Utility Functions

### Class Name Builder Helper

```javascript
// Reusable helper function
const cx = (...classes) => classes.filter(Boolean).join(' ');

const transformHook = (rw) => {
  const { variant, size, isDisabled } = rw.props;

  const buttonClasses = cx(
    'btn',
    variant === 'primary' && 'bg-brand-500 text-white',
    variant === 'secondary' && 'bg-surface-100',
    size === 'lg' && 'px-6 py-3',
    isDisabled && 'opacity-50 cursor-not-allowed'
  );

  rw.setProps({ buttonClasses });
};

exports.transformHook = transformHook;
```

### Conditional Class Object

```javascript
const transformHook = (rw) => {
  const { isVisible, isAnimated, position } = rw.props;

  // Object where keys are classes and values are conditions
  const classConditions = {
    'opacity-100': isVisible,
    'opacity-0': !isVisible,
    'transition-opacity duration-300': isAnimated,
    'absolute': position === 'absolute',
    'fixed': position === 'fixed',
    'relative': position === 'relative'
  };

  const classes = Object.entries(classConditions)
    .filter(([_, condition]) => condition)
    .map(([className]) => className)
    .join(' ');

  rw.setProps({ classes });
};
```

## Common Mistakes

### Don't Forget filter(Boolean)

```javascript
// Wrong - will include "false" as a string
const classes = [
  'base',
  false && 'conditional'
].join(' '); // "base false"

// Correct
const classes = [
  'base',
  false && 'conditional'
].filter(Boolean).join(' '); // "base"
```

### Don't Mutate rw.props

```javascript
// Wrong
rw.props.classes = 'new-class';

// Correct
rw.setProps({ classes: 'new-class' });
```

### Handle Undefined Values

```javascript
// Could output "p-undefined"
const classes = `p-${rw.props.padding}`;

// Better - provide default
const padding = rw.props.padding || 4;
const classes = `p-${padding}`;

// Or check before using
const classes = [
  rw.props.padding && `p-${rw.props.padding}`
].filter(Boolean).join(' ');
```

## Complete Example

```javascript
const transformHook = (rw) => {
  const {
    variant,
    size,
    isFullWidth,
    isDisabled,
    bgColor,
    bgColorHover,
    textColor,
    padding,
    borderRadius,
    shadow,
    customClasses
  } = rw.props;

  // Variant classes
  const variantClasses = {
    solid: '',
    outline: 'border-2 bg-transparent',
    ghost: 'bg-transparent'
  };

  // Size classes (only if not using theme spacing)
  const sizeClasses = {
    sm: 'text-sm',
    md: 'text-base',
    lg: 'text-lg'
  };

  // Build the final class string
  const buttonClasses = [
    // Base styles
    'inline-flex items-center justify-center',
    'font-medium',
    'transition-colors duration-200',
    // Theme control outputs
    bgColor,
    bgColorHover,
    textColor,
    padding,
    borderRadius,
    shadow,
    // Variant
    variantClasses[variant],
    // Size
    sizeClasses[size],
    // Conditional modifiers
    isFullWidth && 'w-full',
    isDisabled && 'opacity-50 cursor-not-allowed pointer-events-none',
    // User custom classes
    customClasses
  ]
    .filter(Boolean)
    .join(' ');

  rw.setProps({ buttonClasses });
};

exports.transformHook = transformHook;
```
