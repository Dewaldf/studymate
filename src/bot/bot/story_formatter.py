"""
Formats story data into GitHub issue payloads (title, body, labels).
"""
from typing import Dict, Any, List


def format_story(story: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a story data dict into a GitHub issue payload."""
    body = _build_body(story)
    labels = _build_labels(story)
    return {
        "title": story["title"],
        "body": body,
        "labels": labels,
    }


def format_stories_preview(stories: List[Dict[str, Any]]) -> str:
    """Build a human-readable preview of proposed stories for Telegram."""
    count = len(stories)
    lines = [f"📋 *{count} {'story' if count == 1 else 'stories'} to create:*\n"]
    for i, story in enumerate(stories, 1):
        bounded_context = story.get("bounded_context", "Unknown")
        story_type = story.get("type", "feature")
        lines.append(
            f"*{i}.* {story['title']}\n"
            f"   └ `{bounded_context}` · `{story_type}`"
        )
    return "\n\n".join(lines)


def _build_body(story: Dict[str, Any]) -> str:
    sections = []

    # User Story section
    sections.append("## User Story\n\n" + story["user_story"])

    # Acceptance Criteria section
    criteria_lines = "\n".join(
        f"- [ ] {criterion}" for criterion in story["acceptance_criteria"]
    )
    sections.append(f"## Acceptance Criteria\n\n{criteria_lines}")

    # Technical Notes section
    bounded_context = story.get("bounded_context", "")
    layer = story.get("layer", "")
    tech_lines = [
        f"- Bounded context: {bounded_context}",
        f"- Layer: {layer}",
    ]
    for note in story.get("technical_notes", []):
        tech_lines.append(f"- {note}")
    sections.append("## Technical Notes\n\n" + "\n".join(tech_lines))

    # Test Approach section
    test_lines = "\n".join(f"- {test}" for test in story.get("test_approach", []))
    sections.append(f"## Test Approach (write tests first)\n\n{test_lines}")

    return "\n\n".join(sections)


def _build_labels(story: Dict[str, Any]) -> List[str]:
    labels = ["user story"]

    bounded_context = story.get("bounded_context", "")
    if bounded_context:
        labels.append(bounded_context.lower())

    story_type = story.get("type", "")
    if story_type:
        labels.append(story_type)

    return labels
