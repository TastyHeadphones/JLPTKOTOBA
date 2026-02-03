import { useState, useMemo, useEffect } from 'react'
import vocabData from './data/vocab.json'
import { WordCard } from './components/WordCard'
import { FilterBar } from './components/FilterBar'

function App() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedLevel, setSelectedLevel] = useState('All')
  const [displayedCount, setDisplayedCount] = useState(50)

  // Filter Data
  const filteredData = useMemo(() => {
    return vocabData.filter(item => {
      const matchLevel = selectedLevel === 'All' || item.level === selectedLevel
      const matchSearch = item.word.includes(searchTerm) ||
        (item.reading && item.reading.includes(searchTerm)) ||
        item.meaning_cn.includes(searchTerm) ||
        (item.meaning_en && item.meaning_en.some(m => m.toLowerCase().includes(searchTerm.toLowerCase())))
      return matchLevel && matchSearch
    })
  }, [searchTerm, selectedLevel])

  const displayedData = filteredData.slice(0, displayedCount)

  const handleLoadMore = () => {
    setDisplayedCount(prev => prev + 50)
  }

  // Reset display count when filter changes
  useEffect(() => {
    setDisplayedCount(50)
  }, [searchTerm, selectedLevel])

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 font-sans transition-colors duration-300">

      {/* Header */}
      <header className="sticky top-0 z-50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 shadow-sm">
        <div className="max-w-5xl mx-auto px-4 py-4">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <h1 className="text-2xl font-bold bg-gradient-to-r from-indigo-500 to-purple-600 bg-clip-text text-transparent">
              日本語語彙 Master
            </h1>
            <div className="flex items-center gap-2">
              <input
                type="password"
                placeholder="Google Cloud API Key"
                className="px-3 py-1 text-sm border rounded-md dark:bg-slate-800 dark:text-white"
                value={window.localStorage.getItem('google_tts_key') || ''}
                onChange={(e) => {
                  const val = e.target.value;
                  window.localStorage.setItem('google_tts_key', val);
                  // Force re-render or state update could use context, but valid for now if we lift state
                  // simple reload for this demo or just use text input
                  window.location.reload();
                }}
              />
            </div>
            <FilterBar
              searchTerm={searchTerm}
              setSearchTerm={setSearchTerm}
              selectedLevel={selectedLevel}
              setSelectedLevel={setSelectedLevel}
            />
          </div>
          <div className="mt-2 text-sm text-slate-500 dark:text-slate-400">
            Found {filteredData.length} words
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-5xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {displayedData.map((item, index) => (
            <WordCard
              key={item.id}
              data={item}
              index={index + 1}
              apiKey={window.localStorage.getItem('google_tts_key')}
            />
          ))}
        </div>

        {/* Empty State */}
        {displayedData.length === 0 && (
          <div className="text-center py-20 text-slate-500">
            No words found matching your criteria.
          </div>
        )}

        {/* Load More */}
        {displayedData.length < filteredData.length && (
          <div className="text-center mt-12">
            <button
              onClick={handleLoadMore}
              className="px-8 py-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-full shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-300 font-medium text-indigo-600 dark:text-indigo-400"
            >
              Load More ({filteredData.length - displayedData.length} remaining)
            </button>
          </div>
        )}
      </main>

      <footer className="text-center py-8 text-slate-400 text-sm">
        Generated from JLPT PDFs
      </footer>
    </div>
  )
}

export default App
