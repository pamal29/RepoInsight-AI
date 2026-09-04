from datetime import datetime, timedelta, timezone
from collections import Counter


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