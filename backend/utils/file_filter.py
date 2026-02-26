ALLOWED_EXTENSIONS = (
    ".py", ".js", ".ts", ".java",
    ".md", ".json", ".xml", ".yml"
)

EXCLUDED_FOLDERS = (
    "node_modules",
    ".git",
    "__pycache__",
    "dist",
    "build"
)

def filter_files(files):
  filtered = []

  for file in files:
    if any(folder in file["path"] for folder in EXCLUDED_FOLDERS):
      continue

    if file["path"].endswith(ALLOWED_EXTENSIONS):
      filtered.append(file)

  return filtered