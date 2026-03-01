import React, { useState } from "react";
import axios from "axios";
import LanguageChart from "./LanguageChart";

function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeRepo = async () => {
    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        null,
        {
          params: { repo_url: repoUrl },
        }
      );

      setData(response.data);
    } catch (error) {
      alert("Error analyzing repository");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-lg p-8">
        <h1 className="text-3xl font-bold mb-6 text-center">
          🚀 RepoInsight AI Dashboard
        </h1>

        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Enter GitHub repo URL"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            className="flex-1 p-3 border rounded-lg"
          />
          <button
            onClick={analyzeRepo}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition"
          >
            Analyze
          </button>
        </div>

        {loading && <p className="mt-4 text-blue-500">Analyzing...</p>}

        {data && (
          <div className="mt-8 space-y-6">
            <div className="bg-gray-50 p-4 rounded-lg shadow">
              <h2 className="font-semibold text-xl mb-2">Project Overview</h2>
              <p><strong>Total Files:</strong> {data.total_files}</p>
              <p><strong>Architecture:</strong> {data.architecture}</p>
              <p><strong>Frameworks:</strong> {data.frameworks.join(", ")}</p>
              <p><strong>Complexity Score:</strong> {data.complexity.complexity_score}</p>
            </div>

            <LanguageChart languageData={data.language_info} />

            <div className="bg-gray-50 p-4 rounded-lg shadow">
              <h2 className="font-semibold text-xl mb-2">AI Summary</h2>
              <p>{data.ai_summary}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
