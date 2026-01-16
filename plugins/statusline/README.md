# Statusline

Enhanced Claude Code status line with comprehensive information display.

## Features

- **Model Display**: Shows current model name (e.g., "Claude Opus 4.5")
- **Directory**: Current working directory name
- **Git Status**:
  - Current branch name
  - Uncommitted file count (shows filename if only 1 file)
  - Sync status with upstream (ahead/behind/synced)
  - Last fetch time
- **Context Usage**: Visual progress bar with percentage and token count
- **Last Message**: Shows your last prompt for context

## Screenshot

```
Claude Opus 4.5 | my-project | 🔀main (2 files uncommitted, synced 5m ago) | ██▄░░░░░░░ 25% of 200k tokens
💬 I want my current claude status line installable as a plugin...
```

## Installation

### Quick Setup (Recommended)

```bash
claude plugin install statusline@methuz-claude-marketplace && ~/.claude/plugins/cache/methuz-claude-marketplace/statusline/*/setup.sh
```

Then restart Claude Code.

### Manual Setup

1. Install the plugin:
   ```bash
   claude plugin install statusline@methuz-claude-marketplace
   ```

2. Run the setup script:
   ```bash
   ~/.claude/plugins/cache/methuz-claude-marketplace/statusline/*/setup.sh
   ```

3. Restart Claude Code

## Color Themes

Edit `statusline.sh` and change the `COLOR` variable to customize:

- `blue` (default)
- `orange`
- `teal`
- `green`
- `lavender`
- `rose`
- `gold`
- `slate`
- `cyan`
- `gray`

## Requirements

- `jq` - JSON processor (usually pre-installed or install via `brew install jq`)
- `git` - For git status features

## License

MIT
