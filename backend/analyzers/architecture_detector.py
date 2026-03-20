def detect_architecture(files):
  paths = [file.get("path", "").lower() for file in files]

  folders = set()

  for path in paths:
    parts = path.split("/")
    for part in parts[:-1]:
      folders.add(part)

  filenames = {path.split("/")[-1] for path in paths}
  
if {"controllers", "services", "repositories", "models"}.issubset(folders):
  return{
    "pattern":"clean/ Layered Architecture",
    "confident":"High",
    "description":"Separation of concerns with controllers, services, repositories, and models"
  }

  if{"models","views","controllers"}.issubset(folders):
    return{
      "pattern":"MVC (Model-View-Controller)",
      "confidence":"High",
      "description": "Classic MVC seperation with model, view and controllers"
    }

  if {"components", "pages"}.issubset(folders):
    hooks_or_store = "hooks" in folders or "store" in folders or "context" in folders
    return{
      "pattern": "Frontend SPA",
      "confifence": "High" if hooks_or_store else "Medium",
      "description": "Single Page Application structure with components and pages"
    }