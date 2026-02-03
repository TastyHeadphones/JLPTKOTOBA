import React from 'react';
import type { VocabularyItem } from '../types';

interface WordCardProps {
    item: VocabularyItem;
}

const WordCard: React.FC<WordCardProps> = ({ item }) => {
    const speak = (text: string) => {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ja-JP';
        window.speechSynthesis.speak(utterance);
    };

    return (
        <div className="bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow p-6 border border-gray-100 flex flex-col items-start gap-4">
            <div className="flex justify-between w-full items-start">
                <div
                    className="cursor-pointer group"
                    onClick={() => speak(item.word)}
                >
                    {/* Main Word Display */}
                    <div className="text-3xl font-bold text-gray-800 font-jp mb-1 group-hover:text-indigo-600 transition-colors">
                        {/* Simple Ruby logic if reading is available and different from word */}
                        {item.reading && item.reading !== item.word ? (
                            <ruby>
                                {item.word}
                                <rt className="text-sm text-gray-500 font-normal">{item.reading}</rt>
                            </ruby>
                        ) : (
                            item.word
                        )}
                    </div>
                </div>

                <span className="px-3 py-1 bg-sakura text-pink-600 text-xs font-bold rounded-full">
                    {item.level}
                </span>
            </div>

            <div className="flex flex-col gap-1 w-full">
                <div className="text-gray-700 font-medium">{item.meaning_cn}</div>
                <div className="text-gray-500 text-sm">{item.meaning_en}</div>
            </div>

            {/* Example Sentence Section - Render only if available */}
            {(item.example_sentence) && (
                <div
                    className="mt-4 p-4 bg-gray-50 rounded-lg w-full cursor-pointer hover:bg-gray-100 transition-colors border-l-4 border-bamboo"
                    onClick={() => speak(item.example_sentence!)}
                >
                    <div className="font-jp text-lg text-gray-800 mb-2">
                        {item.example_reading ? (
                            // If we have full HTML string with ruby tags for the sentence, we'd sanitize/parse it.
                            // For now, let's assume raw text or simple ruby if we parse it later.
                            // If the enrichment script provides HTML, we would use dangerouslySetInnerHTML safely.
                            // Or if it provides separate reading.
                            // Let's assume for now it's just text, and we might implement detailed ruby later.
                            item.example_sentence
                        ) : item.example_sentence}
                    </div>
                    <div className="text-sm text-gray-600">
                        {item.example_meaning_cn}
                    </div>
                </div>
            )}

            {!item.example_sentence && (
                <div className="mt-2 text-xs text-gray-400 italic">
                    No example sentence yet.
                </div>
            )}
        </div>
    );
};

export default WordCard;
