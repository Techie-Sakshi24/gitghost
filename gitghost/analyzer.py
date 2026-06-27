"""
GitGhost - GitHub profile analyzer
"""

import os
import requests
from datetime import datetime


def get_github_data(username: str, token: str = None) -> dict:
    """Fetch GitHub profile + repos data."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    base = "https://api.github.com"

    # User profile
    user_res = requests.get(f"{base}/users/{username}", headers=headers)
    if user_res.status_code == 404:
        raise ValueError(f"GitHub user '{username}' not found.")
    if user_res.status_code == 401:
        raise ValueError("Invalid GitHub token.")
    user = user_res.json()

    # Repos
    repos_res = requests.get(
        f"{base}/users/{username}/repos",
        headers=headers,
        params={"per_page": 100, "sort": "updated"}
    )
    repos = repos_res.json()

    # Filter out forks, get top by stars
    own_repos = [r for r in repos if not r.get("fork")]
    top_repos = sorted(own_repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:6]

    # Language stats
    lang_counts = {}
    for repo in own_repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    top_langs = sorted(lang_counts.items(), key=lambda x: -x[1])[:5]

    # Stats
    total_stars = sum(r.get("stargazers_count", 0) for r in own_repos)
    total_forks = sum(r.get("forks_count", 0) for r in own_repos)

    # Account age
    created = datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    years = (datetime.now() - created).days // 365

    return {
        "username": username,
        "name": user.get("name") or username,
        "bio": user.get("bio") or "",
        "location": user.get("location") or "",
        "blog": user.get("blog") or "",
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "public_repos": user.get("public_repos", 0),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "account_years": years,
        "top_languages": top_langs,
        "top_repos": [
            {
                "name": r["name"],
                "description": r.get("description") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "language": r.get("language") or "",
                "url": r["html_url"],
                "topics": r.get("topics", []),
            }
            for r in top_repos
        ],
    }


def build_profile_summary(data: dict) -> str:
    """Build a text summary to send to Claude."""
    langs = ", ".join(f"{l} ({c} repos)" for l, c in data["top_languages"])
    repos_text = ""
    for r in data["top_repos"]:
        repos_text += f"\n- {r['name']}: {r['description']} | ⭐{r['stars']} | {r['language']}"
        if r["topics"]:
            repos_text += f" | topics: {', '.join(r['topics'][:4])}"

    return f"""GitHub Profile Data:
Name: {data['name']}
Username: {data['username']}
Bio: {data['bio']}
Location: {data['location']}
Followers: {data['followers']} | Following: {data['following']}
Public Repos: {data['public_repos']} | Total Stars: {data['total_stars']} | Total Forks: {data['total_forks']}
Account Age: {data['account_years']} years
Top Languages: {langs}

Top Repositories:{repos_text}"""