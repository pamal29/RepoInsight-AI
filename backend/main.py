from fastapi import FastAPI
from backend.github.fetcher import get_repo_contents
from backend.utils.file_filter import filter_files
from backend.analyzers.language_detector import detect_language
from backend.analyzers.framework_detector import detect_frameworks
from backend.analyzers.complexity_analyzer import calculate_complexity
from backend.analyzers.architecture_detector import detect_architecture
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "RepoInsight AI is running"}

@app.post("/analyze")
def analyze_repo(repo_url: str):

  files = get_repo_contents(repo_url)

  filtered_files = filter_files(files)
  
  language_info = detect_language(filtered_files)
    
  frameworks = detect_frameworks(filtered_files)
  complexity = calculate_complexity(filtered_files)
  architecture = detect_architecture(filtered_files)

  return {
      "total_files": len(filtered_files),
      "language_info": language_info,
      "frameworks": frameworks,
      "complexity": complexity,
      "architecture": architecture
  }


# uvicorn main:app --reload


