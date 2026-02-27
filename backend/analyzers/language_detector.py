def detect_language(files):
  language_count ={
    "Python": 0,
    "Javascript": 0,
    "Java": 0,
    "TypeScript": 0
  }

  for file in files:
    path = file["path"]

    if path.endswith(".py"):
        language_count["Python"] += 1
    elif path.endswith(".js"):
        language_count["JavaScript"] += 1
    elif path.endswith(".ts"):
        language_count["TypeScript"] += 1
    elif path.endswith(".java"):
        language_count["Java"] += 1

    primary_language = max(language_count, key=language_count.get)

    return{
      "primary_language": primary_language,
      "distribution": language_count
    }
