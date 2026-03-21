def score_readme(files: list) -> dict:
  readme_file = None

  for file in files:
    path = file.get("path", "").lower()
    if path in ("readme.md", "readme.txt", "readme.rst","readme"):
      readme_file = file
      break

  if not readme_file:
    return{
      "score": 0,
      "grade": "F",
      "found": False,
      "feedback": ["No README file found. Every project need one"],
      "checks": {}
    }

  content = readme_file.get("content", "")
  content_lower = content.lower()
  lines = content.splitlines()
  word_count = len(content.split())

  