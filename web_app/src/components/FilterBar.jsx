export function FilterBar({ searchTerm, setSearchTerm, selectedLevel, setSelectedLevel }) {
    const levels = ["All", "N1", "N2", "N3", "N4", "N5"]

    return (
        <div className="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
            {/* Search Input */}
            <div className="relative group">
                <input
                    type="text"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    placeholder="Search word, reading, meaning..."
                    className="w-full sm:w-64 pl-10 pr-4 py-2 bg-slate-100 dark:bg-slate-800 border-none rounded-xl focus:ring-2 focus:ring-indigo-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all outline-none"
                />
                <svg className="w-5 h-5 text-slate-400 absolute left-3 top-2.5 group-focus-within:text-indigo-500 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
            </div>

            {/* Level Selector */}
            <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-xl">
                {levels.map(lvl => (
                    <button
                        key={lvl}
                        onClick={() => setSelectedLevel(lvl)}
                        className={`flex-1 sm:flex-none px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${selectedLevel === lvl
                                ? "bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm"
                                : "text-slate-500 hover:text-slate-700 dark:hover:text-slate-300"
                            }`}
                    >
                        {lvl}
                    </button>
                ))}
            </div>
        </div>
    )
}
