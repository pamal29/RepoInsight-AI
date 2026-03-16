def detect_language(files):
  language_count ={
    "Python": 0,
    "JavaScript": 0,
    "TypeScript": 0,
    "Java": 0,
    "C++": 0,
    "C#": 0,
    "Go": 0,
    "Rust": 0,
    "Ruby": 0,
    "PHP": 0,
    "Swift": 0,
    "Kotlin": 0,
  }

  EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".php": "PHP",
    ".swift": "Swift",
    ".kt": "Kotlin",
  }

  for file in files:
    path = file.get("path", "")
    for ext, lang in EXTENSION_MAP.items():
      if path.endswith(ext):
        language_count[lang] += 1
        break

  active_languages = {lang: count for lang, count in language_count.items() if count > 0}

  if not active_languages:
    return{
      "primary_language": "Unknown",
      "distribution": {}
    }

  primary_language = max(active_languages, key=active_languages.get)

  total = sum (active_languages.values())
  
  percentage_breakdown = {
    lang: round((count/total)*100,1)
    for lang, count in active_languages.items()
  }

  return{
    "primary_language": primary_language,
    "distribution": active_languages,
    "percentage_breakdown": percentage_breakdown,
  }