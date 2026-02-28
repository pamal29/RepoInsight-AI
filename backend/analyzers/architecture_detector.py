import os 

def detect_architecture(repo_path):
  folders = set()

  for root, dirs , files in os.walk(repo_path):
    for dir_name in dirs:
      folders.add(dir_name.lower())

  if {"models", "views", "controllers"}.issubset(folders):
    return "MVC"

  if "services" in folders:
    return "Microservices"

  return "Monolithic or Unknown"