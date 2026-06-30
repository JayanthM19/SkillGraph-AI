function Navbar() {
  return (
    <nav className="w-full flex justify-between items-center px-10 py-6 border-b border-slate-800">

      <h1 className="text-2xl font-bold text-blue-500">
        SkillGraph AI
      </h1>

      <div className="flex gap-8 text-gray-300">

        <button className="hover:text-blue-400 transition">
          Home
        </button>

        <button className="hover:text-blue-400 transition">
          Features
        </button>

        <button className="hover:text-blue-400 transition">
          About
        </button>

      </div>

    </nav>
  );
}

export default Navbar;