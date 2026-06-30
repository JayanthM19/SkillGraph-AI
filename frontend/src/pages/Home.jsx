import Navbar from "../components/common/Navbar";
import ResumeUpload from "../components/upload/ResumeUpload";

function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-8">
        <div className="text-center py-24">
          <h1 className="text-7xl font-extrabold">
            Skill<span className="text-blue-500">Graph</span> AI
          </h1>

          <p className="mt-8 text-2xl text-gray-300">
            Know Your Skills. Build Your Future.
          </p>

          <p className="mt-4 text-gray-500 text-lg max-w-3xl mx-auto">
            AI-powered career intelligence platform that analyzes resumes,
            identifies skill gaps, recommends learning paths, visualizes career
            roadmaps, and accelerates professional growth.
          </p>

          <ResumeUpload />
        </div>
      </div>
    </div>
  );
}

export default Home;