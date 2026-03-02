🚀 RepoInsight AI

AI-powered GitHub repository intelligence platform.

RepoInsight analyzes any public GitHub repository and provides:

📂 Language breakdown

🧱 Framework detection

🏗 Architecture detection

📊 Complexity scoring

🤖 AI-generated technical summary

📈 Visual dashboard with charts

🏗 Tech Stack
Backend

FastAPI

Python

OpenAI API

GitHub API

Frontend

React

Tailwind CSS

Chart.js

Axios

📦 Features

Detects programming languages used

Identifies frameworks (Flask, React, Spring, etc.)

Estimates project complexity

Detects architecture style (MVC, Microservices, etc.)

Generates AI-powered project summary

Displays visual language distribution chart

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/pamal29/RepoInsight-AI.git
cd RepoInsight-AI

🖥 Backend Setup
cd backend
python -m venv venv


Activate virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run backend:

uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

🌐 Frontend Setup

Open new terminal:

cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000

🔐 Environment Variables

Create .env file inside backend/:

OPENAI_API_KEY=your_openai_api_key

📊 API Endpoints
POST /analyze

Analyze a GitHub repository.

Example:

POST /analyze?repo_url=https://github.com/user/repo

🎯 Example Output
{
  "total_files": 120,
  "language_info": {
    "Python": 60,
    "JavaScript": 40
  },
  "frameworks": ["Flask", "React"],
  "architecture": "MVC",
  "complexity": {
    "total_files": 120,
    "total_lines": 3500,
    "complexity_score": 87.5
  },
  "ai_summary": "This repository is a full-stack web application..."
}

🚀 Future Improvements

Security vulnerability scanning

Contributor analysis

Repository health score

Dark mode UI

Deployment to cloud (Render / Vercel)
