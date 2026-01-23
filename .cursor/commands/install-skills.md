# Install Skills

Symlink all skill folders from this repository to `~/.cursor/skills/`.

## Instructions

1. **Find skill folders**: List all directories in this repository's root that contain a `SKILL.md` file. These are the skill folders to install.

2. **Ensure target exists**: Create `~/.cursor/skills/` if it doesn't exist.

3. **For each skill folder**, run these shell commands:
   - Remove any existing symlink, file, or directory at `~/.cursor/skills/<skill-name>`
   - Create a symlink: `ln -s <full-path-to-skill-folder> ~/.cursor/skills/<skill-name>`

4. **Report results**: List which skills were successfully linked.

## Example Commands

```bash
# Remove existing (if any)
rm -rf ~/.cursor/skills/create-component

# Create symlink
ln -s /Users/ben/Developer/elements-agent-skills/create-component ~/.cursor/skills/create-component
```

## Notes

- Use the repository's absolute path when creating symlinks
- A skill folder is any directory containing a `SKILL.md` file
- Expected skills: `create-component`, `frontend-styling`, `hooks-js`, `properties-json`, `template-language`, `skill-creator`
