#!/usr/bin/env python3
"""
Claude Code Plugin: Prompt Improver
Automatically provides grammar corrections and refined versions of user prompts.
"""

import sys
import json

# Configuration
MIN_PROMPT_LENGTH = 10
SKIP_PREFIXES = ("/", "!", "?")
SKIP_EXACT = {"y", "n", "yes", "no", "ok", "okay", "sure", "thanks", "thank you"}


def should_skip(prompt: str) -> bool:
    """Determine if prompt should be skipped."""
    if len(prompt) < MIN_PROMPT_LENGTH:
        return True
    if prompt.startswith(SKIP_PREFIXES):
        return True
    if prompt.lower().strip() in SKIP_EXACT:
        return True
    return False


def escape_prompt(prompt: str) -> str:
    """Escape special characters in prompt for safe embedding."""
    return prompt.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def create_instruction(prompt: str) -> str:
    """Generate the instruction for Claude as plain text context."""
    safe_prompt = escape_prompt(prompt)
    return f"""[PROMPT IMPROVEMENT REQUEST]
Before responding, provide grammar correction and refined version:

Original: "{safe_prompt}"

Format your response starting with:
> **1. Grammar**: [corrected version]
> **2. Refined**: [eloquent, professional version]

Then proceed with your actual response."""


def main():
    """Main entry point."""
    try:
        input_data = sys.stdin.read()
        if not input_data.strip():
            sys.exit(0)
        data = json.loads(input_data)
        prompt = data.get("prompt", "")
    except Exception:
        sys.exit(0)

    if not prompt or should_skip(prompt):
        sys.exit(0)

    print(create_instruction(prompt))
    sys.exit(0)


if __name__ == "__main__":
    main()
