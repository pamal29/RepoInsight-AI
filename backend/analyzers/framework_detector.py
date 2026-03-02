import os

def detect_framework(file_path):
  framework = []

  for root, dirs, files in os.walk(file_path):
    for file in files:
      file_path = os.path.join(root, file)

      if file == "requirements.txt":
        with open(file_path, "r", encoding="utf-8") as f:
          content = f.read().lower()
          if "flask" in content:
            framework.append("Flask")

      if file == "package.json":
        with open(file_path, "r", encoding="utf-8") as f:
          content = f.read().lower()
          if "react" in content:
            framework.append("React")

      if file == "pom.xml":
        with open(file_path, "r", encoding="utf-8") as f:
          content = f.read().lower()
          if "spring" in content:
            framework.append("Spring")

    
  return list(set(framework))