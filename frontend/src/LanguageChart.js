import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function LanguageChart({ languageData }) {
  if (!languageData) return null;

  const chartData = {
    labels: Object.keys(languageData),
    datasets: [
      {
        data: Object.values(languageData),
        backgroundColor: [
          "#3B82F6",
          "#10B981",
          "#F59E0B",
          "#EF4444",
          "#8B5CF6",
        ],
      },
    ],
  };

  return (
    <div className="bg-gray-50 p-4 rounded-lg shadow">
      <h2 className="font-semibold text-xl mb-4">Language Distribution</h2>
      <Pie data={chartData} />
    </div>
  );
}

export default LanguageChart;
