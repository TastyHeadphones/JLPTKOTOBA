import React from 'react';
import type { VocabularyItem } from '../types';

interface WordCardProps {
    item: VocabularyItem;
    style?: React.CSSProperties; // For virtualization
}

const WordCard: React.FC<WordCardProps> = ({ item, style }) => {
    const speak = (text: string) => {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ja-JP';
        window.speechSynthesis.speak(utterance);
    };

    const renderWord = () => {
        if (!item.kanji_reading) return item.word;

        // Simple logic: Find the first non-kana character(s) and apply ruby
        // This works for simple cases like 会います (あ) -> 会(あ)います
        // and 間 (あいだ) -> 間(あいだ)

        const kanjiRegex = /[一-龠々]+/g;
        const matches = [...item.word.matchAll(kanjiRegex)];

        if (matches.length === 0) return item.word;

        // If there's only one kanji block and one reading, assume they match
        // This is a common pattern in the provided data
        if (matches.length === 1 && item.kanji_reading) {
            const kanji = matches[0][0];
            const parts = item.word.split(kanji);
            return (
                <>
                    {parts[0]}
                    <ruby className="ruby-base">
                        {kanji}
                        <rt className="ruby-text text-apple-blue font-medium">{item.kanji_reading}</rt>
                    </ruby>
                    {parts[1]}
                </>
            );
        }

        return item.word;
    };

    return (
        <div style={style} className="p-2">
            <div
                className="h-full bg-card-bg rounded-2xl shadow-apple hover:shadow-apple-hover transition-all duration-300 p-6 flex flex-col items-center text-center border border-white/50"
            >
                <div className="w-full flex justify-between items-start mb-4">
                    <span className="px-2 py-1 bg-apple-gray text-gray-500 text-[10px] font-bold rounded-md uppercase tracking-wider">
                        {item.level}
                    </span>
                    <button
                        onClick={() => speak(item.word)}
                        className="p-2 rounded-full hover:bg-apple-gray transition-colors text-apple-blue"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                        </svg>
                    </button>
                </div>

                <div className="flex flex-col items-center">
                    <div className="text-4xl font-bold text-apple-dark font-jp mb-4 leading-relaxed tracking-tight">
                        {renderWord()}
                    </div>

                    <div className="mt-2 space-y-1">
                        <p className="text-xl font-semibold text-gray-800 leading-tight">{item.meaning_cn}</p>
                        <p className="text-xs text-gray-400 font-bold tracking-widest uppercase">{item.meaning_en}</p>
                    </div>
                </div>

                {item.example_sentence && (
                    <div
                        className="mt-8 w-full pt-6 border-t border-gray-100 flex flex-col items-center group cursor-pointer"
                        onClick={() => speak(item.example_sentence!)}
                    >
                        <div className="text-apple-blue mb-2 opacity-0 group-hover:opacity-100 transition-opacity">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                            </svg>
                        </div>
                        <p className="text-[15px] text-gray-700 font-jp leading-relaxed max-w-[80%] text-center group-hover:text-apple-blue transition-colors">
                            {item.example_sentence}
                        </p>
                        <div className="mt-3 space-y-0.5 opacity-80 group-hover:opacity-100 transition-opacity">
                            <p className="text-sm text-gray-500 font-medium">{item.example_meaning_cn}</p>
                            <p className="text-[11px] text-gray-400 italic">{item.example_meaning_en}</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default WordCard;
