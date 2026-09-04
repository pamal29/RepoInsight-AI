import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from fastapi.middleware.cors import CORSMiddleware
from github_api.fetcher import g

from github_api.fetcher import get_repo_contents , get_commit_activity
from utils.file_filter import filter_files
from analyzers.language_detector import detect_language
from analyzers.framework_detector import detect_framework
from analyzers.complexity_analyzer import calculate_complexity
from analyzers.architecture_detector import detect_architecture
from analyzers.readme_scorer import score_readme

import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("repoinsight")

app = FastAPI(
    title="RepoInsight AI",
    description="Analyze your GitHub repositories with AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_REPO_PATTERN = re.compile(
    r"^https?://github\.com/[\w.-]+/[\w.-]+/?$"
)


class AnalyzeRequest(BaseModel):
    repo_url: str

    @field_validator("repo_url")
    @classmethod
    def validate_repo_url(cls, v: str) -> str:
        if not GITHUB_REPO_PATTERN.match(v.strip()):
            raise ValueError(
                "repo_url must look like https://github.com/<owner>/<repo>"
            )
        return v.strip()


class AnalyzeResponse(BaseModel):
    repo_url: str
    total_files: int
    language_info: dict
    frameworks: dict
    complexity: dict
    architecture: dict
    readme_score: dict
    commit_activity: dict   


@app.get("/")
def root():
    return {"message": "RepoInsight AI is running"}


@app.post("/analyze", response_model=AnalyzeResponse)   
def analyze_repo(request: AnalyzeRequest):
    try:
        files = get_repo_contents(request.repo_url)
    except Exception as e:
        logger.exception("Failed to fetch repo contents for %s", request.repo_url)
        raise HTTPException(
            status_code=400, detail=f"Error fetching repository contents: {e}"
        )

    if not files:
        raise HTTPException(status_code=400, detail="No files to analyze")

    filtered_files = filter_files(files)
    if not filtered_files:
        raise HTTPException(
            status_code=400, detail="No analyzable files found after filtering"
        )

    language_info = detect_language(filtered_files)
    frameworks = detect_framework(filtered_files)
    complexity = calculate_complexity(filtered_files)
    architecture = detect_architecture(filtered_files)
    readme_score = score_readme(filtered_files)

    try:
        commit_activity = get_commit_activity(request.repo_url)
    except Exception as e:
        logger.exception("Failed to fetch commit activity for %s", request.repo_url)
        commit_activity = {"total_commits": 0, "contributors": {}, "error": str(e)}

    return {
        "repo_url": request.repo_url,
        "total_files": len(filtered_files),
        "language_info": language_info,
        "frameworks": frameworks,
        "complexity": complexity,
        "architecture": architecture,
        "readme_score": readme_score,
        "commit_activity": commit_activity,
    }


# uvicorn main:app --reload