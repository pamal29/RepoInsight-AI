import { useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

const SECTIONS = {
  language: { color: "#4d9fff", bg: "rgba(77,159,255,0.1)", label: "Language" },
  frameworks: { color: "#a78bfa", bg: "rgba(167,139,250,0.1)", label: "Frameworks" },
  architecture: { color: "#a78bfa", bg: "rgba(167,139,250,0.1)", label: "Architecture" },
  complexity: { color: "#4d9fff", bg: "rgba(77,159,255,0.1)", label: "Complexity" },
  readme: { color: "#4ade80", bg: "rgba(74,222,128,0.1)", label: "README" },
  security: { color: "#ff6b6b", bg: "rgba(255,107,107,0.1)", label: "Security" },
  commits: { color: "#fbbf24", bg: "rgba(251,191,36,0.1)", label: "Commits" },
};

function StatCard({ tone, label, value, sub }) {
  const s = SECTIONS[tone];
  return (
    <div
      style={{
        background: "#171a23",
        border: "1px solid #262b38",
        borderLeft: `3px solid ${s.color}`,
        borderRadius: 10,
        padding: "16px 18px",
        minWidth: 150,
        flex: "1 1 150px",
      }}
    >
      <p style={{ margin: 0, fontSize: 12, letterSpacing: 0.3, color: "#8b8fa3" }}>{label}</p>
      <p style={{ margin: "6px 0 0", fontSize: 22, fontWeight: 600, color: "#e4e6eb", fontFamily: "'JetBrains Mono', ui-monospace, monospace" }}>
        {value}
      </p>
      {sub && <p style={{ margin: "4px 0 0", fontSize: 12, color: s.color }}>{sub}</p>}
    </div>
  );
}

function SectionHeading({ tone, children }) {
  const s = SECTIONS[tone];
  return (
    <h3
      style={{
        display: "flex",
        alignItems: "center",
        gap: 8,
        margin: "28px 0 12px",
        fontSize: 13,
        fontWeight: 600,
        color: s.color,
        textTransform: "uppercase",
        letterSpacing: 0.8,
      }}
    >
      <span style={{ width: 8, height: 8, borderRadius: 2, background: s.color, display: "inline-block" }} />
      {children}
    </h3>
  );
}

function Pill({ tone, children }) {
  const s = SECTIONS[tone];
  return (
    <span
      style={{
        display: "inline-block",
        padding: "4px 10px",
        borderRadius: 999,
        fontSize: 12,
        fontWeight: 500,
        background: s.bg,
        color: s.color,
        marginRight: 6,
        marginBottom: 6,
      }}
    >
      {children}
    </span>
  );
}

function ScoreRing({ score = 0, color }) {
  const size = 72;
  const stroke = 6;
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const pct = Math.max(0, Math.min(100, score));
  return (
    <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
      <circle cx={size / 2} cy={size / 2} r={r} stroke="#262b38" strokeWidth={stroke} fill="none" />
      <circle
        cx={size / 2}
        cy={size / 2}
        r={r}
        stroke={color}
        strokeWidth={stroke}
        fill="none"
        strokeDasharray={c}
        strokeDashoffset={c - (pct / 100) * c}
        strokeLinecap="round"
      />
      <text
        x={size / 2}
        y={size / 2}
        fill="#e4e6eb"
        fontSize="18"
        fontWeight="600"
        textAnchor="middle"
        dominantBaseline="central"
        transform={`rotate(90 ${size / 2} ${size / 2})`}
        fontFamily="'JetBrains Mono', ui-monospace, monospace"
      >
        {pct}
      </text>
    </svg>
  );
}

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
    <div
      style={{
        minHeight: "100vh",
        background: "#0f1117",
        color: "#e4e6eb",
        fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif",
        padding: "48px 20px 80px",
      }}
    >
      <div style={{ maxWidth: 760, margin: "0 auto" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 6 }}>
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: 3,
              background: "linear-gradient(135deg,#4d9fff,#a78bfa)",
            }}
          />
          <span style={{ fontSize: 13, color: "#8b8fa3", letterSpacing: 0.5 }}>repo analysis</span>
        </div>
        <h1 style={{ fontSize: 34, fontWeight: 600, margin: "0 0 28px", letterSpacing: -0.5 }}>
          RepoInsight <span style={{ color: "#4d9fff" }}>AI</span>
        </h1>

        <div style={{ display: "flex", gap: 10, marginBottom: 8 }}>
          <input
            type="text"
            placeholder="https://github.com/owner/repo"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAnalyze()}
            style={{
              flex: 1,
              background: "#171a23",
              border: "1px solid #262b38",
              borderRadius: 8,
              padding: "12px 14px",
              color: "#e4e6eb",
              fontSize: 14,
              fontFamily: "'JetBrains Mono', ui-monospace, monospace",
              outline: "none",
            }}
            onFocus={(e) => (e.target.style.borderColor = "#4d9fff")}
            onBlur={(e) => (e.target.style.borderColor = "#262b38")}
          />
          <button
            onClick={handleAnalyze}
            disabled={loading}
            style={{
              background: loading ? "#262b38" : "linear-gradient(135deg,#4d9fff,#a78bfa)",
              color: loading ? "#8b8fa3" : "#0f1117",
              border: "none",
              borderRadius: 8,
              padding: "0 22px",
              fontSize: 14,
              fontWeight: 600,
              cursor: loading ? "default" : "pointer",
              whiteSpace: "nowrap",
            }}
          >
            {loading ? "Analyzing…" : "Analyze"}
          </button>
        </div>

        {error && (
          <p style={{ color: "#ff6b6b", fontSize: 13, marginTop: 8 }}>{error}</p>
        )}

        {data && (
          <div style={{ marginTop: 12 }}>
            {/* Overview */}
            <div style={{ display: "flex", flexWrap: "wrap", gap: 12, marginTop: 24 }}>
              <StatCard tone="language" label="Total files" value={data.total_files ?? "—"} />
              <StatCard
                tone="language"
                label="Primary language"
                value={data.language_info?.primary_language ?? "—"}
              />
              <StatCard
                tone="architecture"
                label="Architecture"
                value={data.architecture?.pattern ?? "—"}
              />
              <StatCard
                tone="complexity"
                label="Complexity"
                value={data.complexity?.complexity_level ?? "—"}
                sub={data.complexity?.total_lines ? `${data.complexity.total_lines.toLocaleString()} lines` : undefined}
              />
            </div>

            {data.frameworks?.length > 0 && (
              <>
                <SectionHeading tone="frameworks">Frameworks</SectionHeading>
                <div>
                  {data.frameworks.map((f, i) => (
                    <Pill tone="frameworks" key={i}>{f}</Pill>
                  ))}
                </div>
              </>
            )}

            {/* README */}
            <SectionHeading tone="readme">README health</SectionHeading>
            <div
              style={{
                background: "#171a23",
                border: "1px solid #262b38",
                borderLeft: "3px solid #4ade80",
                borderRadius: 10,
                padding: 18,
                display: "flex",
                alignItems: "center",
                gap: 20,
              }}
            >
              <ScoreRing score={data.readme_score?.score ?? 0} color="#4ade80" />
              <div>
                <p style={{ margin: 0, fontSize: 15, fontWeight: 600 }}>
                  Grade: {data.readme_score?.grade ?? "—"}
                </p>
                <div style={{ marginTop: 8 }}>
                  {data.readme_score?.improvements?.map((item, i) => (
                    <p key={i} style={{ margin: "3px 0", fontSize: 13, color: "#8b8fa3" }}>
                      <span style={{ color: "#ff6b6b" }}>✗</span> {item}
                    </p>
                  ))}
                </div>
              </div>
            </div>

            {/* Security */}
            <SectionHeading tone="security">Security</SectionHeading>
            <div style={{ display: "flex", gap: 12 }}>
              <StatCard tone="security" label="Risk level" value={data.security?.risk_level ?? "—"} />
              <StatCard tone="security" label="Issues found" value={data.security?.total_issues ?? 0} />
            </div>

            {/* Commits */}
            <SectionHeading tone="commits">Commit activity</SectionHeading>
            <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
              <StatCard tone="commits" label="Total commits" value={data.commit_history?.total_commits_fetched ?? 0} />
              <StatCard tone="commits" label="Last 30 days" value={data.commit_history?.commits_last_30_days ?? 0} />
              <StatCard
                tone="commits"
                label="Longest streak"
                value={data.commit_history?.longest_streak ?? 0}
                sub="days"
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}