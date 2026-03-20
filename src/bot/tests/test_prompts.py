"""
Tests for the system prompt builder.
All tests must pass before implementation begins.
"""
import pytest
from bot.prompts import build_system_prompt


REQUIRED_PRODUCT_KEYWORDS = [
    "StudyMate",
    "GCSE",
    "Matric",
    "check-in",
    "quiz",
    "badge",
    "streak",
    "parent",
]

REQUIRED_BOUNDED_CONTEXTS = [
    "Learning",
    "Identity",
    "Curriculum",
    "Reporting",
    "Safeguarding",
]

REQUIRED_TECH_STACK_KEYWORDS = [
    "Next.js",
    "ASP.NET Core",
    "MediatR",
    "PostgreSQL",
    "Liquibase",
    "EF Core",
    "Supabase",
    "Hangfire",
    "SendGrid",
    "Stripe",
    "Azure",
]

REQUIRED_STORY_FORMAT_SECTIONS = [
    "## User Story",
    "## Acceptance Criteria",
    "## Technical Notes",
    "## Test Approach",
    "Bounded context",
]

REQUIRED_BEHAVIOUR_INSTRUCTIONS = [
    "one clarifying question",
    "summarise",
    "breakdown",
    "create stories",
]


class TestBuildSystemPrompt:

    def test_returns_non_empty_string(self):
        prompt = build_system_prompt(existing_issues=[])
        assert isinstance(prompt, str)
        assert len(prompt) > 500

    @pytest.mark.parametrize("keyword", REQUIRED_PRODUCT_KEYWORDS)
    def test_contains_product_context(self, keyword):
        prompt = build_system_prompt(existing_issues=[])
        assert keyword in prompt, f"System prompt missing product keyword: '{keyword}'"

    @pytest.mark.parametrize("context", REQUIRED_BOUNDED_CONTEXTS)
    def test_contains_all_bounded_contexts(self, context):
        prompt = build_system_prompt(existing_issues=[])
        assert context in prompt, f"System prompt missing bounded context: '{context}'"

    @pytest.mark.parametrize("tech", REQUIRED_TECH_STACK_KEYWORDS)
    def test_contains_tech_stack(self, tech):
        prompt = build_system_prompt(existing_issues=[])
        assert tech in prompt, f"System prompt missing tech stack keyword: '{tech}'"

    @pytest.mark.parametrize("section", REQUIRED_STORY_FORMAT_SECTIONS)
    def test_contains_story_format_template(self, section):
        prompt = build_system_prompt(existing_issues=[])
        assert section in prompt, f"System prompt missing story format section: '{section}'"

    @pytest.mark.parametrize("instruction", REQUIRED_BEHAVIOUR_INSTRUCTIONS)
    def test_contains_behaviour_instructions(self, instruction):
        prompt = build_system_prompt(existing_issues=[])
        assert instruction in prompt, f"System prompt missing behaviour instruction: '{instruction}'"

    def test_includes_existing_issues_when_provided(self):
        existing = [
            {"number": 2, "title": "As a developer, I want a monorepo folder structure"},
            {"number": 3, "title": "As a developer, I want PostgreSQL and Liquibase"},
        ]
        prompt = build_system_prompt(existing_issues=existing)
        assert "#2" in prompt
        assert "monorepo folder structure" in prompt

    def test_empty_existing_issues_does_not_error(self):
        prompt = build_system_prompt(existing_issues=[])
        assert "existing" in prompt.lower() or "no current" in prompt.lower()

    def test_mentions_edtech_expertise(self):
        prompt = build_system_prompt(existing_issues=[])
        assert "EdTech" in prompt or "edtech" in prompt.lower()
