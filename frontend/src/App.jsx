import { useState } from "react";

const API_BASE = "http://127.0.0.1:8080";

export default function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  async function handleAnalyze() {
    if (!repoUrl.trim()) return;
    setLoading(true);
    setError(null);
    setData(null);

    try {
      const res = await fetch(`${API_BASE}/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ repo_url: repoUrl, include_ai_summary: false }),
      });
      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || "Something went wrong");
      }
      setData(await res.json());
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h1>RepoInsight AI</h1>

      <input
        type="text"
        placeholder="https://github.com/owner/repo"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleAnalyze()}
      />
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <div>
          <h2>Results</h2>
          <p>Total Files: {data.total_files}</p>
          <p>Primary Language: {data.language_info?.primary_language}</p>
          <p>Frameworks: {data.frameworks?.join(", ") || "None"}</p>
          <p>Architecture: {data.architecture?.pattern}</p>
          <p>Complexity: {data.complexity?.complexity_level}</p>
          <p>Total Lines: {data.complexity?.total_lines}</p>

          <h3>README</h3>
          <p>Score: {data.readme_score?.score}/100</p>
          <p>Grade: {data.readme_score?.grade}</p>
          {data.readme_score?.improvements?.map((item, i) => (
            <p key={i}>✗ {item}</p>
          ))}

          <h3>Security</h3>
          <p>Risk Level: {data.security?.risk_level}</p>
          <p>Issues: {data.security?.total_issues}</p>

          <h3>Commits</h3>
          <p>Total: {data.commit_history?.total_commits_fetched}</p>
          <p>Last 30 days: {data.commit_history?.commits_last_30_days}</p>
          <p>Longest Streak: {data.commit_history?.longest_streak} days</p>
        </div>
      )}
    </div>
  );
}