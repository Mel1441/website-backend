// src/pages/School/Dashboard.jsx
export default function Dashboard() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-indigo-600 mb-4">Welcome to Your Learning Lab</h1>
      <ul className="space-y-4">
        <li className="bg-white p-4 shadow rounded">📄 View Assigned Worksheets</li>
        <li className="bg-white p-4 shadow rounded">📚 Explore Transcript Lessons</li>
        <li className="bg-white p-4 shadow rounded">🧠 Track Your Progress</li>
      </ul>
    </div>
  );
}