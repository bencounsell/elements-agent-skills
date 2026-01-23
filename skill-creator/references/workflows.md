# Workflow Patterns

## Sequential Workflows

For complex tasks, break operations into clear, sequential steps. It is often helpful to give the agent an overview of the process towards the beginning of SKILL.md:

```markdown
Creating a new Elements component involves these steps:

1. Copy the component template (from assets/component-template/)
2. Update info.json with component metadata
3. Define properties in properties.json
4. Implement data transformations in hooks.js
5. Create the HTML template in templates/index.html
6. Test the component in RapidWeaver
```

## Conditional Workflows

For tasks with branching logic, guide the agent through decision points:

```markdown
1. Determine the component type:
   **Static content?** → Skip hooks.js, use template only
   **Dynamic data processing?** → Follow "hooks.js workflow" below
   **User-configurable?** → Follow "properties.json workflow" below

2. hooks.js workflow:
   - Access properties via rw.props
   - Transform data as needed
   - Pass to template via rw.setProps()

3. properties.json workflow:
   - Define UI controls for each configurable option
   - Group related controls together
   - Add theme controls for colors/fonts if needed
```

## Elements Component Lifecycle

For skills that work with the full component lifecycle:

```markdown
Component data flows through these stages:

properties.json → hooks.js → templates

1. **properties.json**: Defines UI controls and their default values
2. **hooks.js**: Processes and transforms property values
3. **templates**: Renders the final HTML output

When debugging, trace data through each stage to find issues.
```
