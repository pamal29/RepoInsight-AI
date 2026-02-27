from fastapi import FastAPI
from backend.github.fetcher import get_repo_contents
from backend.utils.file_filter import filter_files
from backend.analyzers.language_detector import detect_language

app = FastAPI()

@app.get("/")
def root():
  return {"message": "RepoInsight AI is running"}

@app.post("/analyze")
def analyze_repo(repo_url: str):
  files = get_repo_contents(repo_url)
  filtered_files = filter_files(files)
  language_info = detect_language(filtered_files)

  return{
    "total_files": len(filtered_files),
    "language_info": language_info
  }


# uvicorn main:app --reload


