import { useState, useMemo } from 'react';
import vocabData from './data/vocab.json';
import { VocabularyItem } from './types';
import WordCard from './components/WordCard';

// Cast imported JSON to typed array
const allVocabulary = vocabData as VocabularyItem[];

function App() {
  const [selectedLevel, setSelectedLevel] = useState<string>('All');
  const [searchTerm, setSearchTerm] = useState('');

  const levels = ['All', 'N5', 'N4', 'N3', 'N2', 'N1'];

  const filteredVocabulary = useMemo(() => {
    return allVocabulary.filter(item => {
      const matchLevel = selectedLevel === 'All' || item.level === selectedLevel;
      const matchSearch = item.word.includes(searchTerm) ||
        item.meaning_cn.includes(searchTerm) ||
        item.reading.includes(searchTerm);
      return matchLevel && matchSearch;
    });
  }, [selectedLevel, searchTerm]);

  return (
    <div className="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8 font-jp">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-indigo-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            JLPT Kotoba
          </h1>
          <p className="mt-4 max-w-2xl mx-auto text-xl text-gray-500">
            Master Japanese Vocabulary with Native Audio & Examples
          </p>
        </div>

        {/* Controls */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-10 sticky top-4 z-10 bg-white/80 backdrop-blur-md p-4 rounded-2xl shadow-lg border border-white/20">
          <div className="flex gap-2 bg-gray-100 p-1 rounded-lg">
            {levels.map(level => (
              <button
                key={level}
                onClick={() => setSelectedLevel(level)}
                className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${selectedLevel === level
                    ? 'bg-white text-indigo-600 shadow-sm transform scale-105'
                    : 'text-gray-500 hover:text-gray-700'
                  }`}
              >
                {level}
              </button>
            ))}
          </div>

          <input
            type="text"
            placeholder="Search keywords..."
            className="w-full sm:w-64 px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Grid */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {filteredVocabulary.slice(0, 100).map((item) => (
            /* Limit to 100 for performance until we add virtualization or pagination */
            <WordCard key={item.id} item={item} />
          ))}
        </div>

        {filteredVocabulary.length > 100 && (
          <div className="mt-8 text-center text-gray-400">
            Showing first 100 of {filteredVocabulary.length} words. Filter to see more.
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
