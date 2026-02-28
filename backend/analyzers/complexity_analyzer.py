import os 

def calculate_complexity(repo_path):
  total_files = 0
  total_lines = 0

  for root,dir,files in os.walk(repo_path):
    for file in files:
      if file.endswith((".py", ".js" , ".java")):
        total_files += 1

        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
          lines = f.readlines()
          total_lines += len(lines)

  complexity_score = total_files *2 + total_lines +0.01

  return{
    "total_files": total_files,
    "total_lines": total_lines,
    "complexity_score": complexity_score
  }