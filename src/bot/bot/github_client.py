"""
GitHub REST API client for fetching issues and creating new ones.
"""
import httpx
from typing import List, Dict, Any


class GitHubClient:
    def __init__(self, token: str, repo: str = "Dewaldf/studymate"):
        self.token = token
        self.repo = repo
        self._base_url = "https://api.github.com"
        self._headers = {
            "Authorization": f"token {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json",
        }

    async def get_existing_issues(self) -> List[Dict[str, Any]]:
        """Fetch all open issues from the repo (up to 100)."""
        url = f"{self._base_url}/repos/{self.repo}/issues"
        async with httpx.AsyncClient(verify=False) as http:
            response = await http.get(
                url,
                headers=self._headers,
                params={"state": "open", "per_page": 100},
            )
            response.raise_for_status()
            issues = response.json()
            return [
                {"number": issue["number"], "title": issue["title"]}
                for issue in issues
            ]

    async def create_issue(
        self,
        title: str,
        body: str,
        labels: List[str],
    ) -> Dict[str, Any]:
        """Create a single GitHub issue and return its number and URL."""
        url = f"{self._base_url}/repos/{self.repo}/issues"
        async with httpx.AsyncClient(verify=False) as http:
            response = await http.post(
                url,
                headers=self._headers,
                json={"title": title, "body": body, "labels": labels},
            )
            response.raise_for_status()
            data = response.json()
            return {
                "number": data["number"],
                "url": data["html_url"],
            }

    async def create_issues(
        self, stories: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Create multiple GitHub issues sequentially and return all results."""
        results = []
        for story in stories:
            result = await self.create_issue(
                title=story["title"],
                body=story["body"],
                labels=story["labels"],
            )
            results.append(result)
        return results
