def detect_framework(files):
    FRAMEWORK_SIGNATURES = {
        "requirements.txt": {
            "fastapi":      "FastAPI",
            "flask":        "Flask",
            "django":       "Django",
            "tornado":      "Tornado",
            "aiohttp":      "aiohttp",
            "tensorflow":   "TensorFlow",
            "torch":        "PyTorch",
            "scikit-learn": "Scikit-learn",
            "langchain":    "LangChain",
            "openai":       "OpenAI SDK",
            "sqlalchemy":   "SQLAlchemy",
            "celery":       "Celery",
            "pytest":       "Pytest",
        },
        "package.json": {
            "react":        "React",
            "next":         "Next.js",
            "vue":          "Vue.js",
            "nuxt":         "Nuxt.js",
            "svelte":       "Svelte",
            "express":      "Express.js",
            "fastify":      "Fastify",
            "nestjs":       "NestJS",
            "gatsby":       "Gatsby",
            "tailwindcss":  "Tailwind CSS",
            "typescript":   "TypeScript",
            "jest":         "Jest",
            "vite":         "Vite",
            "webpack":      "Webpack",
        },
        "pom.xml": {
            "spring-boot":  "Spring Boot",
            "spring":       "Spring",
            "hibernate":    "Hibernate",
            "junit":        "JUnit",
        },
        "build.gradle": {
            "spring-boot":  "Spring Boot",
            "spring":       "Spring",
            "hibernate":    "Hibernate",
        },
        "go.mod": {
            "gin-gonic":    "Gin",
            "echo":         "Echo",
            "fiber":        "Fiber",
        },
        "cargo.toml": {
            "actix":        "Actix",
            "rocket":       "Rocket",
            "axum":         "Axum",
        },
        "gemfile": {
            "rails":        "Ruby on Rails",
            "sinatra":      "Sinatra",
        },
    }
    detected = set()

    for file in files:
      filename = file.get("path", "").split("/")[-1].lower()
      content = file.get("content", "").lower()

      if filename in FRAMEWORK_SIGNATURES and content:
        for keyword,label in FRAMEWORK_SIGNATURES[filename].items():
          if keyword in content:
            detected.add(label)

return sorted(detected)