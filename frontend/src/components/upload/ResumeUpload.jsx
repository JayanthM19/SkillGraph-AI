import { useState } from "react";
import { uploadResume } from "../../services/api";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("AI Engineer");

  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select a resume.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const result = await uploadResume(file, role);

console.log("Backend Response:");
console.log(result);

if (result.error) {
    setError(result.error);
    setResponse(null);
    return;
}

setResponse(result);

      // Dashboard navigation will be added in the next step
    } catch (err) {
      console.error(err);

      setError("Failed to analyze resume. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
      mt-20
      max-w-2xl
      mx-auto
      bg-slate-900/70
      backdrop-blur-md
      border
      border-slate-700
      rounded-3xl
      p-10
      shadow-2xl
      "
    >
      <div className="text-5xl mb-6">📄</div>

      <h2 className="text-3xl font-bold">
        Upload Resume
      </h2>

      <p className="mt-3 text-gray-400">
        Upload your resume and let SkillGraph AI build your personalized
        career roadmap.
      </p>

      {/* File Input */}

      <input
        id="resume"
        type="file"
        accept=".pdf"
        className="hidden"
        onChange={(e) => {
          if (e.target.files.length > 0) {
            setFile(e.target.files[0]);
          }
        }}
      />

      {/* Upload Button */}

      <label
        htmlFor="resume"
        className="
        mt-8
        block
        cursor-pointer
        rounded-xl
        bg-blue-600
        hover:bg-blue-700
        transition
        py-4
        font-semibold
        text-lg
        text-center
        "
      >
        {file ? file.name : "Choose Resume"}
      </label>

      {/* Target Role */}

      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
        className="
        mt-8
        w-full
        rounded-xl
        bg-slate-800
        border
        border-slate-700
        p-4
        text-white
        "
      >
        <option>AI Engineer</option>
        <option>Data Scientist</option>
        <option>MLOps Engineer</option>
        <option>Backend Engineer</option>
        <option>Frontend Engineer</option>
        <option>DevOps Engineer</option>
        <option>IoT Engineer</option>
      </select>

      {/* Analyze Button */}

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="
        mt-8
        w-full
        rounded-xl
        bg-green-600
        hover:bg-green-700
        disabled:bg-gray-600
        transition
        py-4
        font-bold
        text-lg
        "
      >
        {loading ? "Analyzing Resume..." : "🚀 Analyze Resume"}
      </button>

      {/* Error Message */}

      {error && (
        <div className="mt-6 rounded-xl bg-red-900/40 border border-red-600 p-4 text-red-300">
          {error}
        </div>
      )}

      {/* Success Message */}

      {response && (
        <div className="mt-6 rounded-xl bg-green-900/40 border border-green-600 p-4 text-green-300">
          ✅ Resume analyzed successfully!
        </div>
      )}
    </div>
  );
}

export default ResumeUpload;