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

  service_folders = [f for f in folders if "service" in f]
  has_docker_compose = "docker-compose.yml" in filenames or "docker-compose.yaml" in filenames

  if len(service_folders) >= 2 or (has_docker_compose and "services" in folders):
    return{
      "pattern": "Microservices",
      "confidence": "Medium",
      "description": "Multiple indipendent sevice modules detected"
    }

  if {"functions", "handlers", "lambdas"}.intersection(folders):
    return{
      "pattern": "Serverless / Function",
      "confidence": "Medium",
      "description": "Function-based structure typical of serverless deployments"
    }

  if {"notebooks", "data", "models"}.issubset(folders) or any(p.endswith(".ipynb") for p in paths):
        return {
            "pattern": "Data Science / ML Project",
            "confidence": "Medium",
            "description": "Notebook and data-centric structure typical of ML projects."
        }
 
  has_subdirs= any("/" in path for path in paths)
  if not has_subdirs:
    return{
      "pattern": "Flat / Script-based",
      "confidence": "High",
      "description": "No subdirectory structure — likely a simple script or utility project."
    }

  return{
    "pattern": "Monolithic",
    "confidence": "Low",
    "description": "Could not detect a specific pattern. Likely a monolithic or custom structure."
  }