from github import Github
import os
from dotenv import load_dotenv

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
                # ✅ Only decode if encoding is base64
                if file_content.encoding == "base64":
                    decoded = file_content.decoded_content.decode(
                        "utf-8", errors="ignore"
                    )

                    all_files.append({
                        "path": file_content.path,
                        "content": decoded
                    })

            except Exception:
                # Skip problematic files
                continue

    return all_files
