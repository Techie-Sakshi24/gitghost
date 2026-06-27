"""
GitGhost - README generator using Claude AI
"""

import os
import anthropic


SYSTEM_PROMPT = """You are GitGhost, an elite GitHub README writer. You create cinematic, personality-driven GitHub profile READMEs that feel human — not corporate, not cringe, not generic.

Your READMEs:
- Open with a punchy 1-2 line hook that captures the developer's actual vibe from their repos/bio
- Use emojis sparingly (max 8-10 total) — only where they add meaning
- Include a "What I build" section based on actual repo patterns
- Include a stats/skills section using real language data
- Feature top repos in a clean way
- End with something memorable — a quote, a line, anything that doesn't sound like a template
- NEVER use: "passionate developer", "love to code", "always learning", "hard worker", "team player"
- NEVER add fake badges or shields unless asked
- Sound like a real person wrote it at 11pm after shipping something they're proud of

Output ONLY the raw markdown. No explanation, no preamble, no backticks around the whole thing."""


def generate_readme(profile_summary: str, style: str = "cinematic", api_key: str = None) -> str:
    """Generate README using Claude."""
    key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError("ANTHROPIC_API_KEY not set.")

    client = anthropic.Anthropic(api_key=key)

    style_instructions = {
        "cinematic": "Write it with cinematic energy — dramatic but real. Like a movie trailer for a developer.",
        "minimal": "Write it minimal and clean — no fluff, just the essentials. Less is more.",
        "fun": "Write it fun and witty — jokes welcome, personality first, tech second.",
        "professional": "Write it professional but human — could go on a resume but still has a voice.",
    }

    style_note = style_instructions.get(style, style_instructions["cinematic"])

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"{style_note}\n\nHere is the developer's GitHub data:\n\n{profile_summary}\n\nGenerate their GitHub profile README now."
            }
        ]
    )

    return response.content[0].text.strip()