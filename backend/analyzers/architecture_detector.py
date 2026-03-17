def detect_architecture(files):
  paths = [file.get("path", "").lower() for file in files]

  folders = set()

  for path in paths:
    parts = path.split("/")
    for part in parts[:-1]:
      folders.add(part)

  filenames = {path.split("/")[-1] for path in paths}
  
