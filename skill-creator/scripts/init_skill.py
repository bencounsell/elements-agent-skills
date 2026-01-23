#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables for Elements development]

## Skill Category

[TODO: Identify which Elements category this skill belongs to:
- **Component Creation** - Building Elements components (scaffolding, structure, metadata)
- **Data Processing** - hooks.js, properties.json, collections
- **Styling & Theming** - CSS class generation, responsive design, theme integration
- **Templating** - Elements template language, control flow, directives

Delete this section when done - it's just for planning.]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. See existing Elements skills for patterns:

**hooks-js/** - Concise SKILL.md with step-by-step instructions and reference files for detailed API docs
**properties-json/** - Schema documentation with separate reference files for UI controls, theme controls
**frontend-styling/** - Multi-topic organization with separate files for CLASS-GENERATION, RESPONSIVE-DESIGN, THEME-INTEGRATION
**template-language/** - Control flow and directive documentation with reference files

Delete this entire section when done - it's just guidance.]

## [TODO: Replace with the first main section]

[TODO: Add content here. For Elements skills, consider including:
- Code samples showing common patterns
- Examples with realistic component scenarios
- References to scripts/references as needed
- Links to related Elements skills]

## Resources

This skill includes example resource directories:

### scripts/
Executable code for validation or automation.

**Examples from Elements skills:**
- `hooks-js/scripts/validate-hooks.js` - Validates hooks.js syntax

**Appropriate for:** Validation scripts, code generators, automation tools.

### references/
Documentation loaded on demand by the agent.

**Examples from Elements skills:**
- `hooks-js/references/RW-OBJECT.md` - Complete rw object API
- `properties-json/references/UI-CONTROLS.md` - Available control types
- `frontend-styling/references/CLASS-GENERATION.md` - CSS class patterns

**Appropriate for:** API documentation, schema references, detailed guides.

### assets/
Files used in output, not loaded into context.

**Examples from Elements skills:**
- `create-component/assets/component-template/` - Component boilerplate files

**Appropriate for:** Templates, boilerplate code, starter files.

---

**Delete any unneeded directories.** Not every skill requires all three types of resources.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Example scripts from Elements skills:
- hooks-js/scripts/validate-hooks.js - Validates hooks.js syntax and patterns
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # For Elements skills, this might be:
    # - Validation of component files
    # - Code generation utilities
    # - Schema checking

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example reference docs from Elements skills:
- hooks-js/references/RW-OBJECT.md - Complete rw object API documentation
- hooks-js/references/COMMON-PATTERNS.md - Recipes and common patterns
- properties-json/references/UI-CONTROLS.md - Available UI control types
- frontend-styling/references/CLASS-GENERATION.md - CSS class patterns

## When Reference Docs Are Useful

Reference docs are ideal for:
- API documentation (like the rw object)
- Schema references (like properties.json controls)
- Detailed pattern guides
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example (like RW-OBJECT.md)
- Available properties (rw.props, rw.collections, etc.)
- Available functions (rw.setProps, rw.resizeResource, etc.)
- Usage examples

### Schema Reference Example (like UI-CONTROLS.md)
- Control types with examples
- Required vs optional fields
- Common configurations
"""

EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, component boilerplate, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output the agent produces.

Example asset files from Elements skills:
- create-component/assets/component-template/ - Component boilerplate with hooks.js, properties.json, templates/

## Common Asset Types for Elements

- Component templates: Boilerplate directories with standard file structure
- Starter hooks.js: Pre-configured transformation hooks
- Starter properties.json: Common control configurations
- Template files: HTML template patterns

Note: This is a text placeholder. Actual assets can be any file type.
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with template SKILL.md.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create resource directories with example files
    try:
        # Create scripts/ directory with example script
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        example_script = scripts_dir / 'example.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/example.py")

        # Create references/ directory with example reference doc
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        example_reference = references_dir / 'api_reference.md'
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/api_reference.md")

        # Create assets/ directory with example asset placeholder
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        example_asset = assets_dir / 'example_asset.txt'
        example_asset.write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Print next steps
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Customize or delete the example files in scripts/, references/, and assets/")
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nSkill name requirements:")
        print("  - Hyphen-case identifier (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 40 characters")
        print("  - Must match directory name exactly")
        print("\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public")
        print("  init_skill.py my-api-helper --path skills/private")
        print("  init_skill.py custom-skill --path /custom/location")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
