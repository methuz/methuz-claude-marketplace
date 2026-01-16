#!/bin/bash
# Setup script for methuz statusline plugin
# Run after: claude plugin install statusline@methuz-claude-marketplace

set -e

SETTINGS_FILE="$HOME/.claude/settings.json"
PLUGIN_PATH=$(find "$HOME/.claude/plugins/cache/methuz-claude-marketplace/statusline" -name "statusline.sh" 2>/dev/null | head -1)

if [[ -z "$PLUGIN_PATH" ]]; then
    echo "Error: Plugin not found. Please install first:"
    echo "  claude plugin install statusline@methuz-claude-marketplace"
    exit 1
fi

echo "Found statusline at: $PLUGIN_PATH"

# Create settings.json if it doesn't exist
if [[ ! -f "$SETTINGS_FILE" ]]; then
    echo "{}" > "$SETTINGS_FILE"
fi

# Backup existing settings
cp "$SETTINGS_FILE" "$SETTINGS_FILE.backup"

# Update settings with jq
if command -v jq &> /dev/null; then
    jq --arg path "$PLUGIN_PATH" '.statusLine = {
        "type": "command",
        "command": $path,
        "padding": 0
    }' "$SETTINGS_FILE" > "$SETTINGS_FILE.tmp" && mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
    echo "✅ Status line configured successfully!"
    echo "   Restart Claude Code to see the new status line."
else
    echo "Error: jq is required. Install with: brew install jq"
    exit 1
fi
