from fastapi import FastAPI
from github_api.fetcher import get_repo_contents
from utils.file_filter import filter_files
from analyzers.language_detector import detect_language
from analyzers.framework_detector import detect_framework
from analyzers.complexity_analyzer import calculate_complexity
from analyzers.architecture_detector import detect_architecture
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
  title="RepoInsight AI",
  description = "Analyze your GitHub repositories with AI",
  version="1.0.0"
)
  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
  repo_url:str

@app.get("/")
def root():
  return {"message": "RepoInsight AI is running"}

@app.post("/analyze")
def analyze_repo(request : AnalyzeRequest):
  try:

    files = get_repo_contents(request.repo_url)
  except Exception as e:
    raise HTTPException(status_code=400, detail="Error fetching repository contents")

  if not files:
    raise HTTPException(status_code=400, detail="No files to analyze")

  filtered_files = filter_files(files)

  if not filtered_files:
    raise HTTPException(status_code=400, detail="No analyzable files found after filtering")

  language_info = detect_language(filtered_files)
  frameworks = detect_framework(filtered_files)
  complexity = calculate_complexity(filtered_files)
  architecture = detect_architecture(filtered_files)


  return {
       "repo_url": request.repo_url,
        "total_files": len(filtered_files),
        "language_info": language_info,
        "frameworks": frameworks,
        "complexity": complexity,
        "architecture": architecture,
  }


# uvicorn main:app --reload


