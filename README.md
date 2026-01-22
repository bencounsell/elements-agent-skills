# Elements Agent Skills

A collection of [Agent Skills](https://agentskills.io) for building, modifying, and debugging [RapidWeaver Elements](https://www.realmacsoftware.com/elements/) components.

These skills teach AI agents how to work with the Elements component system, following the [Agent Skills specification](https://agentskills.io/specification).

## Skills

| Skill | Description |
|-------|-------------|
| [create-component](./create-component/) | Scaffold new Elements components with proper folder structure |
| [hooks-js](./hooks-js/) | Write and debug hooks.js files for data processing |
| [template-language](./template-language/) | Work with Elements template directives (@if, @each, @text, etc.) |

## Installation

### Manual Installation

Clone or download this repository and point your agent to the skill directories.

```bash
git clone https://github.com/your-org/elements-agent-skills.git
```

### Using with Claude

Copy the skill folder(s) you need into your project or reference them in your agent configuration.

## Skill Structure

Each skill follows the [Agent Skills specification](https://agentskills.io/specification):

```
skill-name/
├── SKILL.md          # Main instructions (required)
├── references/       # Additional documentation
├── scripts/          # Executable code (optional)
└── assets/           # Templates and static files (optional)
```

## Creating New Skills

Use the existing skills as templates. Each `SKILL.md` requires:

```yaml
---
name: skill-name
description: What the skill does and when to use it
license: MIT
metadata:
  author: Elements Platform
  version: "1.0"
---
```

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Elements Documentation](https://docs.realmacsoftware.com/elements-docs)
- [RWElementsCorePack (GitHub)](https://github.com/realmacsoftware/RWElementsCorePack)
- [RWElementDevPacks Examples (GitHub)](https://github.com/realmacsoftware/RWElementDevPacks)

## License

MIT License - See [LICENSE](./LICENSE) for details.
