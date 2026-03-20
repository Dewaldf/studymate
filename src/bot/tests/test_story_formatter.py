"""
Tests for the story formatter.
Ensures every generated GitHub issue has all required sections.
"""
import pytest
from bot.story_formatter import format_story, format_stories_preview


VALID_STORY = {
    "title": "As a student, I want to log in with email and password so that I can access my study dashboard",
    "bounded_context": "Identity",
    "layer": "API",
    "type": "feature",
    "user_story": "**As a** student,\n**I want** to log in with email and password,\n**So that** I can access my personal study dashboard.",
    "acceptance_criteria": [
        "Student can enter email and password on the login screen",
        "Valid credentials redirect to the dashboard",
        "Invalid credentials show an inline error message",
        "Failed login attempts are rate-limited after 5 attempts",
    ],
    "technical_notes": [
        "Supabase Auth handles credential validation",
        "JWT token stored in httpOnly cookie",
        "Rate limiting via Supabase Auth built-in protection",
    ],
    "test_approach": [
        "Unit test: login command handler returns JWT on valid credentials",
        "Unit test: login command handler throws on invalid credentials",
        "Integration test: POST /auth/login returns 200 with valid body",
        "Integration test: POST /auth/login returns 401 with wrong password",
        "Frontend unit test: login form displays error on 401 response",
    ],
}


class TestFormatStory:

    def test_returns_dict_with_title_body_labels(self):
        result = format_story(VALID_STORY)
        assert "title" in result
        assert "body" in result
        assert "labels" in result

    def test_title_matches_input(self):
        result = format_story(VALID_STORY)
        assert result["title"] == VALID_STORY["title"]

    def test_body_contains_user_story_section(self):
        result = format_story(VALID_STORY)
        assert "## User Story" in result["body"]

    def test_body_contains_as_a_format(self):
        result = format_story(VALID_STORY)
        assert "**As a**" in result["body"]
        assert "**I want**" in result["body"]
        assert "**So that**" in result["body"]

    def test_body_contains_acceptance_criteria_section(self):
        result = format_story(VALID_STORY)
        assert "## Acceptance Criteria" in result["body"]

    def test_acceptance_criteria_are_checkboxes(self):
        result = format_story(VALID_STORY)
        assert "- [ ]" in result["body"]

    def test_all_acceptance_criteria_included(self):
        result = format_story(VALID_STORY)
        for criterion in VALID_STORY["acceptance_criteria"]:
            assert criterion in result["body"]

    def test_body_contains_technical_notes_section(self):
        result = format_story(VALID_STORY)
        assert "## Technical Notes" in result["body"]

    def test_technical_notes_contain_bounded_context(self):
        result = format_story(VALID_STORY)
        assert "Bounded context:" in result["body"]
        assert "Identity" in result["body"]

    def test_technical_notes_contain_layer(self):
        result = format_story(VALID_STORY)
        assert "Layer:" in result["body"]
        assert "API" in result["body"]

    def test_body_contains_test_approach_section(self):
        result = format_story(VALID_STORY)
        assert "## Test Approach" in result["body"]

    def test_test_approach_items_included(self):
        result = format_story(VALID_STORY)
        for test in VALID_STORY["test_approach"]:
            assert test in result["body"]

    def test_labels_always_include_user_story(self):
        result = format_story(VALID_STORY)
        assert "user story" in result["labels"]

    def test_labels_include_bounded_context_as_lowercase(self):
        result = format_story(VALID_STORY)
        assert "identity" in result["labels"]

    def test_labels_include_type(self):
        result = format_story(VALID_STORY)
        assert "feature" in result["labels"]

    @pytest.mark.parametrize("bounded_context", [
        "Learning", "Identity", "Curriculum", "Reporting", "Safeguarding"
    ])
    def test_all_bounded_contexts_produce_correct_label(self, bounded_context):
        story = {**VALID_STORY, "bounded_context": bounded_context}
        result = format_story(story)
        assert bounded_context.lower() in result["labels"]

    @pytest.mark.parametrize("story_type", ["feature", "enhancement", "bug", "scaffolding"])
    def test_all_valid_types_produce_correct_label(self, story_type):
        story = {**VALID_STORY, "type": story_type}
        result = format_story(story)
        assert story_type in result["labels"]


class TestFormatStoriesPreview:

    def test_returns_string(self):
        stories = [VALID_STORY, {**VALID_STORY, "title": "Story 2"}]
        result = format_stories_preview(stories)
        assert isinstance(result, str)

    def test_preview_contains_all_story_titles(self):
        stories = [
            VALID_STORY,
            {**VALID_STORY, "title": "As a parent, I want a weekly digest"},
        ]
        result = format_stories_preview(stories)
        assert VALID_STORY["title"] in result
        assert "As a parent, I want a weekly digest" in result

    def test_preview_shows_story_count(self):
        stories = [VALID_STORY, {**VALID_STORY, "title": "Story 2"}]
        result = format_stories_preview(stories)
        assert "2" in result

    def test_preview_shows_bounded_context(self):
        result = format_stories_preview([VALID_STORY])
        assert "Identity" in result
