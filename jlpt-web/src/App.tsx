import { useState, useMemo } from 'react';
import { Virtuoso } from 'react-virtuoso';
import vocabData from './data/vocab.json';
import type { VocabularyItem } from './types';
import WordCard from './components/WordCard';

const allVocabulary = vocabData as VocabularyItem[];

function App() {
  const [selectedLevel, setSelectedLevel] = useState<string>('All');

  const levels = ['All', 'N5', 'N4', 'N3', 'N2', 'N1'];

  const filteredVocabulary = useMemo(() => {
    return allVocabulary.filter(item => {
      const matchLevel = selectedLevel === 'All' || item.level === selectedLevel;
      return matchLevel;
    });
  }, [selectedLevel]);

  return (
    <div className="h-screen flex flex-col bg-apple-gray font-sans overflow-hidden">
      {/* Sticky Glass Header */}
      <header className="glass z-50 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4 shrink-0 transition-all duration-300">
        <h1 className="text-2xl font-bold text-apple-dark tracking-tight">
          JLPT Kotoba
        </h1>

        <div className="flex bg-gray-200/50 p-1 rounded-xl">
          {levels.map(level => (
            <button
              key={level}
              onClick={() => setSelectedLevel(level)}
              className={`px-4 py-1.5 rounded-lg text-sm font-medium transition-all duration-200 ${selectedLevel === level
                  ? 'bg-white text-apple-blue shadow-sm'
                  : 'text-gray-500 hover:text-gray-700'
                }`}
            >
              {level}
            </button>
          ))}
        </div>
      </header>

      {/* Main Content Area with Virtualized Grid */}
      <main className="flex-1 w-full max-w-[700px] mx-auto px-4 pb-4 pt-6">
        <Virtuoso
          style={{ height: '100%' }}
          totalCount={filteredVocabulary.length}
          overscan={200}
          itemContent={(index) => {
            const item = filteredVocabulary[index];
            return (
              <div className="pb-4 flex justify-center">
                <div className="w-full">
                  <WordCard item={item} />
                </div>
              </div>
            );
          }}
        />
      </main>

      {/* Footer Info */}
      <div className="text-center py-2 text-xs text-gray-400">
        {filteredVocabulary.length} words
      </div>
    </div>
  );
}

export default App;
