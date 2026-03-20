"""
Tests for the GitHub API client.
Uses mocked HTTP responses — no real API calls in unit tests.
"""
import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock, patch
from bot.github_client import GitHubClient


MOCK_ISSUE_RESPONSE = {
    "number": 9,
    "title": "As a student, I want to log in",
    "html_url": "https://github.com/Dewaldf/studymate/issues/9",
    "state": "open",
}

MOCK_ISSUES_LIST = [
    {"number": 2, "title": "As a developer, I want a monorepo folder structure", "state": "open"},
    {"number": 3, "title": "As a developer, I want PostgreSQL and Liquibase", "state": "open"},
]


class TestGitHubClientInit:

    def test_client_stores_token_and_repo(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        assert client.token == "test-token"
        assert client.repo == "Dewaldf/studymate"

    def test_default_repo_is_studymate(self):
        client = GitHubClient(token="test-token")
        assert client.repo == "Dewaldf/studymate"


class TestGetExistingIssues:

    @pytest.mark.asyncio
    async def test_returns_list_of_issues(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_ISSUES_LIST
        mock_response.raise_for_status = MagicMock()

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            issues = await client.get_existing_issues()

        assert isinstance(issues, list)
        assert len(issues) == 2

    @pytest.mark.asyncio
    async def test_returns_number_and_title_per_issue(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_ISSUES_LIST
        mock_response.raise_for_status = MagicMock()

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            issues = await client.get_existing_issues()

        assert issues[0]["number"] == 2
        assert "monorepo" in issues[0]["title"]

    @pytest.mark.asyncio
    async def test_empty_repo_returns_empty_list(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            issues = await client.get_existing_issues()

        assert issues == []


class TestCreateIssue:

    @pytest.mark.asyncio
    async def test_returns_issue_number_and_url(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_ISSUE_RESPONSE
        mock_response.raise_for_status = MagicMock()

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.post = AsyncMock(return_value=mock_response)
            result = await client.create_issue(
                title="As a student, I want to log in",
                body="## User Story\n\n...",
                labels=["user story", "identity", "feature"],
            )

        assert result["number"] == 9
        assert result["url"] == "https://github.com/Dewaldf/studymate/issues/9"

    @pytest.mark.asyncio
    async def test_request_includes_authorization_header(self):
        client = GitHubClient(token="my-secret-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_ISSUE_RESPONSE
        mock_response.raise_for_status = MagicMock()
        captured_headers = {}

        async def mock_post(url, headers=None, json=None, **kwargs):
            captured_headers.update(headers or {})
            return mock_response

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.post = mock_post
            await client.create_issue(title="Test", body="Body", labels=[])

        assert "Authorization" in captured_headers
        assert "my-secret-token" in captured_headers["Authorization"]

    @pytest.mark.asyncio
    async def test_request_body_includes_title_body_labels(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_ISSUE_RESPONSE
        mock_response.raise_for_status = MagicMock()
        captured_payload = {}

        async def mock_post(url, headers=None, json=None, **kwargs):
            captured_payload.update(json or {})
            return mock_response

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.post = mock_post
            await client.create_issue(
                title="Story title",
                body="Story body",
                labels=["user story", "feature"],
            )

        assert captured_payload["title"] == "Story title"
        assert captured_payload["body"] == "Story body"
        assert "user story" in captured_payload["labels"]
        assert "feature" in captured_payload["labels"]

    @pytest.mark.asyncio
    async def test_create_multiple_issues_returns_all_urls(self):
        client = GitHubClient(token="test-token", repo="Dewaldf/studymate")
        call_count = 0

        async def mock_post(url, headers=None, json=None, **kwargs):
            nonlocal call_count
            call_count += 1
            mock_response = MagicMock()
            mock_response.json.return_value = {
                "number": call_count,
                "html_url": f"https://github.com/Dewaldf/studymate/issues/{call_count}",
            }
            mock_response.raise_for_status = MagicMock()
            return mock_response

        stories = [
            {"title": "Story 1", "body": "Body 1", "labels": ["user story"]},
            {"title": "Story 2", "body": "Body 2", "labels": ["user story"]},
        ]

        with patch("httpx.AsyncClient") as mock_http:
            mock_http.return_value.__aenter__.return_value.post = mock_post
            results = await client.create_issues(stories)

        assert len(results) == 2
        assert results[0]["number"] == 1
        assert results[1]["number"] == 2
