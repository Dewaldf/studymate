"""
Claude API interaction layer.
Handles conversational responses and structured story JSON generation.
"""
import json
import re
import anthropic
from typing import List, Dict, Any

from bot.conversation import Conversation
from bot.prompts import build_system_prompt


def _get_client(api_key: str) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=api_key)


async def get_conversational_response(
    conversation: Conversation,
    api_key: str,
    existing_issues: List[Dict[str, Any]],
) -> str:
    """Send the full conversation history to Claude and return its next response."""
    client = _get_client(api_key)
    system_prompt = build_system_prompt(existing_issues)

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        thinking={"type": "adaptive"},
        system=system_prompt,
        messages=conversation.messages,
    )

    for block in response.content:
        if block.type == "text":
            return block.text

    return "I'm sorry, I couldn't generate a response. Please try again."


async def generate_stories_json(
    conversation: Conversation,
    api_key: str,
    existing_issues: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Ask Claude to output the agreed stories as a JSON array.
    Appends a trigger message to the existing conversation so Claude
    has full context when generating the structured output.
    """
    client = _get_client(api_key)
    system_prompt = build_system_prompt(existing_issues)

    messages = list(conversation.messages) + [
        {
            "role": "user",
            "content": (
                "create stories\n\n"
                "Output ONLY a valid JSON array of story objects. "
                "No explanation, no markdown code fences, just the raw JSON array."
            ),
        }
    ]

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8096,
        thinking={"type": "adaptive"},
        system=system_prompt,
        messages=messages,
    )

    raw = ""
    for block in response.content:
        if block.type == "text":
            raw = block.text.strip()
            break

    # Strip markdown code fences if Claude included them
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    return json.loads(raw)
