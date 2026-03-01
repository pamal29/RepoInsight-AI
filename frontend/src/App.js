import React, { useState } from "react";
import axios from "axios";

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
      console.error(error);
      alert("Error analyzing repository");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>RepoInsight AI Dashboard</h1>

      <input
        type="text"
        placeholder="Enter GitHub repo URL"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        style={{ width: "400px", padding: "10px" }}
      />

      <button onClick={analyzeRepo} style={{ padding: "10px 20px", marginLeft: "10px" }}>
        Analyze
      </button>

      {loading && <p>Analyzing...</p>}

      {data && (
        <div style={{ marginTop: "30px" }}>
          <h2>Results</h2>

          <p><strong>Total Files:</strong> {data.total_files}</p>

          <p><strong>Languages:</strong></p>
          <pre>{JSON.stringify(data.language_info, null, 2)}</pre>

          <p><strong>Frameworks:</strong> {data.frameworks.join(", ")}</p>

          <p><strong>Architecture:</strong> {data.architecture}</p>

          <p><strong>Complexity Score:</strong> {data.complexity.complexity_score}</p>
        </div>
      )}
    </div>
  );
}

export default App;
