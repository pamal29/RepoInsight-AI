from github import Github
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from collections import Counter

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

g = Github(GITHUB_TOKEN)


def get_repo_contents(repo_url: str):
    repo_name = repo_url.removeprefix("https://github.com/")
    repo = g.get_repo(repo_name)
    contents = repo.get_contents("")

    all_files = []

    while contents:
        file_content = contents.pop(0)

        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))

        elif file_content.type == "file":
            try:
                if file_content.encoding == "base64":
                    decoded = file_content.decoded_content.decode(
                        "utf-8", errors="ignore"
                    )
                    all_files.append({
                        "path": file_content.path,
                        "content": decoded
                    })
            except Exception:
                continue

    return all_files


def get_commit_activity(repo_url: str, days: int = 90):
    """
    Returns recent commit frequency and top contributors for a repo.
    """
    repo_name = repo_url.removeprefix("https://github.com/").rstrip("/")
    repo = g.get_repo(repo_name)

    since = datetime.now(timezone.utc) - timedelta(days=days)

    try:
        commits = repo.get_commits(since=since)
    except Exception as e:
        return {
            "total_commits": 0,
            "contributors": {},
            "error": str(e),
        }

    contributor_counts = Counter()
    total = 0

    for commit in commits:
        total += 1
        author = commit.author.login if commit.author else (
            commit.commit.author.name if commit.commit.author else "unknown"
        )
        contributor_counts[author] += 1

    return {
        "total_commits": total,
        "contributors": dict(contributor_counts.most_common(10)),
        "period_days": days,
    }