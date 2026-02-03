import { useState, useMemo } from 'react';
// @ts-ignore
import { Grid } from 'react-window';
import { AutoSizer } from 'react-virtualized-auto-sizer';

// @ts-ignore
const GridComponent: any = Grid;
// @ts-ignore
const AutoSizerComponent: any = AutoSizer;

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

  // Card Dimensions
  const CARD_HEIGHT = 280;
  const MIN_COLUMN_WIDTH = 300;

  const Cell = ({ columnIndex, rowIndex, style, data }: any) => {
    const { items, columnCount } = data;
    const index = rowIndex * columnCount + columnIndex;

    if (index >= items.length) {
      return null;
    }

    const item = items[index];

    return (
      <WordCard item={item} style={style} />
    );
  };

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
      <main className="flex-1 w-full max-w-[1600px] mx-auto px-4 pb-4 pt-6">
        <div className="w-full h-full">
          {/* @ts-ignore */}
          <AutoSizer>
            {({ height, width }: { height: number; width: number }) => {
              const columnCount = Math.floor(width / MIN_COLUMN_WIDTH) || 1;
              const columnWidth = width / columnCount;
              const rowCount = Math.ceil(filteredVocabulary.length / columnCount);

              return (
                <GridComponent
                  columnCount={columnCount}
                  columnWidth={columnWidth}
                  height={height}
                  rowCount={rowCount}
                  rowHeight={CARD_HEIGHT}
                  width={width}
                  itemData={{ items: filteredVocabulary, columnCount }}
                  className="no-scrollbar"
                >
                  {Cell}
                </GridComponent>
              );
            }}
          </AutoSizer>
        </div>
      </main>

      {/* Footer Info */}
      <div className="text-center py-2 text-xs text-gray-400">
        {filteredVocabulary.length} words
      </div>
    </div>
  );
}

export default App;
