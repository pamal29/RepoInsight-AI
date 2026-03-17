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

    
