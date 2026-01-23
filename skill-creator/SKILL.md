---
name: skill-creator
description: Guide for creating effective skills. Use when creating a new skill (or updating an existing skill) that extends the agent's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend the agent's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks—they transform a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else the agent needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

**Default assumption: The agent is already very smart.** Only add context the agent doesn't already have. Challenge each piece of information: "Does the agent really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Think of the agent as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md (required)

Every SKILL.md consists of:

- **Frontmatter** (YAML): Contains `name` and `description` fields. These are the fields the agent reads to determine when the skill gets used, thus it is very important to be clear and comprehensive in describing what the skill is, and when it should be used.
- **Body** (Markdown): Instructions and guidance for using the skill. Only loaded AFTER the skill triggers (if at all).

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/validate-hooks.js` for validating hooks.js syntax and patterns
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by the agent for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform the agent's process and thinking.

- **When to include**: For documentation that the agent should reference while working
- **Examples**: `references/UI-CONTROLS.md` for properties.json control types, `references/RW-OBJECT.md` for hooks.js API, `references/CLASS-GENERATION.md` for CSS patterns
- **Use cases**: API documentation, control schemas, theme integration patterns, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when the agent determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output the agent produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/component-template/` for component boilerplate, `assets/starter-hooks.js` for hooks.js starter code
- **Use cases**: Component templates, boilerplate code, starter files that get copied or modified
- **Benefits**: Separates output resources from documentation, enables the agent to use files without loading them into context

#### What to Not Include in a Skill

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- etc.

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxilary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc. Creating additional documentation files just adds clutter and confusion.

## Elements Skill Categories

Skills for RapidWeaver Elements typically fall into these categories:

- **Component Creation** - Skills that help build Elements components, including scaffolding, file structure, and component metadata (see `create-component/`)
- **Data Processing** - Skills for hooks.js, properties.json, and collections that process data before template rendering (see `hooks-js/`, `properties-json/`)
- **Styling & Theming** - Skills for CSS class generation, responsive design, and theme integration (see `frontend-styling/`)
- **Templating** - Skills for the Elements template language, including control flow, directives, and content areas (see `template-language/`)

When creating a new Elements skill, identify which category it belongs to and reference the existing skills in that category for patterns and conventions.

## Reference Implementations

This repository contains example skills demonstrating common patterns:

| Skill | Pattern Demonstrated |
|-------|---------------------|
| `hooks-js/` | Data processing with validation script, concise SKILL.md with reference files |
| `properties-json/` | Schema documentation with detailed reference files for UI controls and theme integration |
| `create-component/` | Asset templates for scaffolding new components |
| `frontend-styling/` | Multi-topic reference organization (CLASS-GENERATION, RESPONSIVE-DESIGN, THEME-INTEGRATION) |
| `template-language/` | Control flow and directive documentation patterns |

Study these implementations when designing new skills to understand effective patterns for Elements development.

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by the agent (Unlimited because scripts can be executed without reading into context window)

#### Progressive Disclosure Patterns

Keep SKILL.md body to the essentials and under 500 lines to minimize context bloat. Split content into separate files when approaching this limit. When splitting out content into other files, it is very important to reference them from SKILL.md and describe clearly when to read them, to ensure the reader of the skill knows they exist and when to use them.

**Key principle:** When a skill supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details (patterns, examples, configuration) into separate reference files.

**Pattern 1: High-level guide with references**

```markdown
# hooks.js Processing

## Quick start

Basic transformation hook:
[code example]

## Advanced features

- **RW Object API**: See [RW-OBJECT.md](references/RW-OBJECT.md) for complete API
- **Common patterns**: See [COMMON-PATTERNS.md](references/COMMON-PATTERNS.md) for recipes
- **Available data**: See [AVAILABLE-DATA.md](references/AVAILABLE-DATA.md) for all data properties
```

The agent loads RW-OBJECT.md, COMMON-PATTERNS.md, or AVAILABLE-DATA.md only when needed.

**Pattern 2: Domain-specific organization**

For Skills with multiple domains, organize content by domain to avoid loading irrelevant context:

```
properties-json/
├── SKILL.md (overview and navigation)
└── references/
    ├── UI-CONTROLS.md (input fields, switches, segmented controls)
    ├── THEME-CONTROLS.md (color pickers, font selectors)
    └── GENERAL-STRUCTURE.md (file structure, groups, conditions)
```

When a user asks about color pickers, the agent only reads THEME-CONTROLS.md.

Similarly, for skills supporting multiple topics, organize by topic:

```
frontend-styling/
├── SKILL.md (overview and navigation)
└── references/
    ├── CLASS-GENERATION.md (CSS class patterns)
    ├── RESPONSIVE-DESIGN.md (breakpoint handling)
    └── THEME-INTEGRATION.md (theme variable usage)
```

When the user asks about responsive design, the agent only reads RESPONSIVE-DESIGN.md.

**Pattern 3: Conditional details**

Show basic content, link to advanced content:

```markdown
# Template Language

## Basic output

Use double braces for variable output: `{{variableName}}`

## Control flow

**For conditionals**: See [CONTROL-FLOW.md](references/CONTROL-FLOW.md)
**For loops and iteration**: See [CONTROL-FLOW.md](references/CONTROL-FLOW.md)
**For directives**: See [DIRECTIVES.md](references/DIRECTIVES.md)
```

The agent reads CONTROL-FLOW.md or DIRECTIVES.md only when the user needs those features.

**Important guidelines:**

- **Avoid deeply nested references** - Keep references one level deep from SKILL.md. All reference files should link directly from SKILL.md.
- **Structure longer reference files** - For files longer than 100 lines, include a table of contents at the top so the agent can see the full scope when previewing.

## Skill Creation Process

Skill creation involves these steps:

1. Understand the skill with concrete examples
2. Plan reusable skill contents (scripts, references, assets)
3. Initialize the skill (run init_skill.py)
4. Edit the skill (implement resources and write SKILL.md)
5. Iterate based on real usage

Follow these steps in order, skipping only if there is a clear reason why they are not applicable.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `hooks-js` skill to handle queries like "Help me process collection data in hooks.js," the analysis shows:

1. Writing hooks.js transformation logic requires understanding the rw object API each time
2. A `references/RW-OBJECT.md` documenting the available properties and methods would be helpful
3. A `scripts/validate-hooks.js` script to check for common errors would be useful

Example: When designing a `create-component` skill for queries like "Create a new accordion component," the analysis shows:

1. Creating a component requires the same boilerplate files each time (hooks.js, properties.json, templates/)
2. An `assets/component-template/` directory containing the boilerplate files would be helpful to store in the skill

Example: When building a `properties-json` skill to handle queries like "Add a color picker to my component," the analysis shows:

1. Writing properties.json requires understanding the control types and their options
2. A `references/UI-CONTROLS.md` file documenting available controls would be helpful
3. A `references/THEME-CONTROLS.md` for theme-aware controls would also be useful

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration or packaging is needed. In this case, continue to the next step.

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

The script:

- Creates the skill directory at the specified path
- Generates a SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, and `assets/`
- Adds example files in each directory that can be customized or deleted

After initialization, customize or remove the generated SKILL.md and example files as needed.

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another agent instance to use. Include information that would be beneficial and non-obvious to the agent. Consider what procedural knowledge, domain-specific details, or reusable assets would help another agent instance execute these tasks more effectively.

#### Learn Proven Design Patterns

Consult these helpful guides based on your skill's needs:

- **Multi-step processes**: See references/workflows.md for sequential workflows and conditional logic
- **Specific output formats or quality standards**: See references/output-patterns.md for template and example patterns

These files contain established best practices for effective skill design.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Added scripts must be tested by actually running them to ensure there are no bugs and that the output matches what is expected. If there are many similar scripts, only a representative sample needs to be tested to ensure confidence that they all work while balancing time to completion.

Any example files and directories not needed for the skill should be deleted. The initialization script creates example files in `scripts/`, `references/`, and `assets/` to demonstrate structure, but most skills won't need all of them.

#### Update SKILL.md

**Writing Guidelines:** Always use imperative/infinitive form.

##### Frontmatter

Write the YAML frontmatter. Required and optional fields per the [Cursor Agent Skills spec](https://cursor.com/docs/context/skills):

**Required fields:**

- `name`: Max 64 chars, lowercase letters/numbers/hyphens only. Must match the skill folder name.
- `description`: The PRIMARY triggering mechanism. Include both WHAT the skill does and WHEN to use it.
  - Include all "when to use" information here - Not in the body. The body is only loaded after triggering, so "When to Use This Skill" sections in the body are not helpful to the agent.
  - Example: "Write and debug hooks.js files for RapidWeaver Elements components. Use when processing data before template rendering, generating CSS classes, working with collections, handling resources, or detecting edit/preview modes."

**Optional fields:**

- `license`: License name or reference to a bundled license file (e.g., "MIT" or "See LICENSE.txt")
- `compatibility`: Environment requirements (system packages, network access, etc.)
- `metadata`: Arbitrary key-value pairs for additional metadata
- `disable-model-invocation`: When `true`, the skill only loads when explicitly invoked via `/skill-name`. Use this for workflow skills with side effects that should not be auto-triggered.

##### Body

Write instructions for using the skill and its bundled resources.

### Step 5: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again
