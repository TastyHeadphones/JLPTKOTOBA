import { useState, useMemo, useEffect } from 'react'
import { Virtuoso } from 'react-virtuoso'
import { Search, Settings, Filter, Languages } from 'lucide-react'
import vocabData from './data/vocab.json'
import { SmartWordCard } from './components/SmartWordCard'
import { FilterBar } from './components/FilterBar'
import { SettingsModal } from './components/SettingsModal'

function App() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedLevel, setSelectedLevel] = useState('All')
  const [isSettingsOpen, setIsSettingsOpen] = useState(false)
  const [windowWidth, setWindowWidth] = useState(typeof window !== 'undefined' ? window.innerWidth : 1200)

  // API Keys (read from localStorage on mount/update)
  // We can let components read them directly or pass them down. 
  // Passing them guarantees updates if we force a re-render or state update.
  const [keys, setKeys] = useState({
    google: window.localStorage.getItem('google_tts_key') || '',
    yahoo: window.localStorage.getItem('yahoo_client_id') || ''
  })

  // Listen for storage events or manual updates (SettingsModal reloads page currently, which is fine)
  useEffect(() => {
    const handleResize = () => setWindowWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

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

  // Virtualization Grid Logic
  // Calculate columns based on width
  // sm: 1, md: 2 (768px), lg: 3 (1024px)
  const columns = windowWidth < 768 ? 1 : windowWidth < 1024 ? 2 : 3;

  // Chunk data for rows
  const rows = useMemo(() => {
    const chunks = [];
    for (let i = 0; i < filteredData.length; i += columns) {
      chunks.push(filteredData.slice(i, i + columns));
    }
    return chunks;
  }, [filteredData, columns]);

  return (
    <div className="h-screen flex flex-col bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 font-sans transition-colors duration-300 overflow-hidden">

      {/* Settings Modal */}
      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => {
          setIsSettingsOpen(false);
          // Update keys state to reflect changes without reload if possible, 
          // though modal reload approach is robust for now.
          setKeys({
            google: window.localStorage.getItem('google_tts_key') || '',
            yahoo: window.localStorage.getItem('yahoo_client_id') || ''
          });
        }}
      />

      {/* Header */}
      <header className="flex-none z-50 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">

            {/* Title & Settings */}
            <div className="flex items-center justify-between md:justify-start gap-4">
              <div className="flex items-center gap-2">
                <div className="bg-indigo-600 p-2 rounded-lg text-white">
                  <Languages size={24} />
                </div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-violet-600 bg-clip-text text-transparent">
                  JLPT Master
                </h1>
              </div>
              <button
                onClick={() => setIsSettingsOpen(true)}
                className="p-2 rounded-full hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500 transition-colors"
                title="API Settings"
              >
                <Settings className="w-6 h-6" />
              </button>
            </div>

            {/* Filter Bar */}
            <div className="flex-1 max-w-2xl">
              <FilterBar
                searchTerm={searchTerm}
                setSearchTerm={setSearchTerm}
                selectedLevel={selectedLevel}
                setSelectedLevel={setSelectedLevel}
              />
            </div>

            <div className="hidden md:block text-sm font-medium text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-3 py-1 rounded-full">
              {filteredData.length} Words
            </div>
          </div>
        </div>
      </header>

      {/* Main Content (Virtualized List) */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 py-6">
        {filteredData.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-slate-400">
            <Search className="w-16 h-16 mb-4 opacity-20" />
            <p className="text-lg">No words found trying searching for something else.</p>
          </div>
        ) : (
          <Virtuoso
            className="no-scrollbar"
            style={{ height: '100%' }}
            data={rows}
            itemContent={(index, rowItems) => (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">
                {rowItems.map((item) => (
                  <SmartWordCard
                    key={item.id}
                    data={item}
                    index={item.id + 1} // Use original ID for consistent numbering
                    googleKey={keys.google}
                    yahooId={keys.yahoo}
                  />
                ))}
              </div>
            )}
          />
        )}
      </main>
    </div>
  )
}

export default App
