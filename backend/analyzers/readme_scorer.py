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

  checks = {
    "has_title":{
      "passed": any(line.startswith("#")for line in lines),
      "weight": 10,
      "feedback_fail":"Missing top level Title."
    },

    "has_description":{
      "passed": word_count > 50,
      "weight": 15,
      "feedback_fail":f"Description is too short({word_count} words). Aim for at least 50 words."
    },

    "has_installation":{
      "passed": any(kw in content_lower for kw in ["install", "setup", "getting started", "quick start"]),
      "weight": 15,
      "feedback_fail":"No installation or setup instructions."
    },

    "has_usage":{
      "passed": any(kw in content_lower for kw in ["usage", "example", "how to use","run"]),
      "weight": 15,
      "feedback_fail":"No usage examples or documentation."
    },

    "has_code_blocks": {
        "passed": "```" in content,
        "weight": 10,
        "feedback_fail": "No code blocks found. Add examples with ``` code blocks."
    },
    "has_badges": {
        "passed": "![" in content and (
            "badge" in content_lower or
            "shield" in content_lower or
            "img.shields.io" in content_lower or
            "travis" in content_lower
        ),
        "weight": 5,
        "feedback_fail": "No badges found (build status, license, version, etc.)."
    },
    "has_license": {
        "passed": any(kw in content_lower for kw in ["license", "mit", "apache", "gpl"]),
        "weight": 10,
        "feedback_fail": "No license information mentioned."
    },
    "has_contributing": {
        "passed": any(kw in content_lower for kw in ["contribut", "pull request", "pr welcome"]),
        "weight": 5,
        "feedback_fail": "No contributing guidelines mentioned."
    },
    "has_screenshots_or_demo": {
        "passed": any(kw in content_lower for kw in ["screenshot", "demo", "preview", "gif", ".png", ".jpg"]),
        "weight": 10,
        "feedback_fail": "No screenshots or demo links found. Visuals make a big difference!"
    },
    "has_tech_stack": {
        "passed": any(kw in content_lower for kw in ["built with", "tech stack", "technologies", "stack", "powered by"]),
        "weight": 5,
        "feedback_fail": "No tech stack section found."
    },
  }