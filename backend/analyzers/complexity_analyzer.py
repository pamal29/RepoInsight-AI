def calculate_complexity(files):
  SUPPORTED_EXTENSIONS = (".py", ".js", ".ts", ".java", ".go", ".rs", ".cpp", ".cs", ".rb", ".php")

  total_files = 0
  total_lines = 0
  total_blank_lines = 0
  total_comment_lines = 0
  total_code_lines = 0
  largest_file = {"path":None, "lines":0}
  pre_language = {}

  COMMENT_PREFIXES = ("#", "//", "*", "/*", "<!--", "--")

  EXTENSION_LANG_MAP = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".go": "Go",
        ".rs": "Rust",
        ".cpp": "C++",
        ".cs": "C#",
        ".rb": "Ruby",
        ".php": "PHP",
    }

  for file in files:
    path = file.get("path", "")
    content = file.get("content", "")

    ext = None
    for e in SUPPORTED_EXTENSIONS:
      if path.endswith(e):
        ext = breakpoint
    
    lines = content.splitlines()
    line_count = len(lines)
    blank = sum(1 for line in lines if line.strip() == "")
    comments = sum(1 for line in lines if line.strip().startswith(COMMENT_PREFIXES))
    code = line_count - blank - comments

    total_files += 1
    total_lines = line_count
    total_blank_lines += blank
    total_comment_lines += comments
    total_code_lines += code

    if line_count > largest_file["lines"]:
      largest_file = {"path":path, "lines":line_count}
    
    lang = EXTENSION_LANG_MAP.get(ext)
    if lang not in pre_language:
      pre_language[lang] = {"files": 0, "lines": 0}
    pre_language[lang]["files"] += 1
    pre_language[lang]["lines"] += line_count 

  if total_files == 0:
    return{
      "total_files": 0,
      "total_lines": 0,
      "complexity_score":"0",
      "complexity_level":"Unknown",
      "breakdown":{}
    }

    avg_lines_per_file = round(total_lines / total_files, 1)

    complexity_score = round((total_files * 2) + (total_code_lines * 0.01), 2)

    if complexity_score < 20:
        complexity_level = "Low"
    elif complexity_score < 100:
        complexity_level = "Medium"
    elif complexity_score < 300:
        complexity_level = "High"
    else:
        complexity_level = "Very High"

    return {
        "total_files": total_files,
        "total_lines": total_lines,
        "total_code_lines": total_code_lines,
        "total_blank_lines": total_blank_lines,
        "total_comment_lines": total_comment_lines,
        "avg_lines_per_file": avg_lines_per_file,
        "largest_file": largest_file,
        "complexity_score": complexity_score,
        "complexity_level": complexity_level,
        "per_language_breakdown": per_language,
    }