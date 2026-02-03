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

    return (
        <div style={style} className="p-2">
            <div
                className="h-full bg-card-bg rounded-2xl shadow-apple hover:shadow-apple-hover transition-all duration-300 transform hover:-translate-y-1 p-6 flex flex-col justify-between border border-white/50"
            >
                <div className="flex justify-between items-start">
                    <div
                        className="cursor-pointer group"
                        onClick={() => speak(item.word)}
                    >
                        <div className="text-3xl font-bold text-apple-dark font-jp group-hover:text-apple-blue transition-colors">
                            {item.reading && item.reading !== item.word ? (
                                <ruby>
                                    {item.word}
                                    <rt className="text-xs text-gray-400 font-normal opacity-0 group-hover:opacity-100 transition-opacity">{item.reading}</rt>
                                </ruby>
                            ) : (
                                item.word
                            )}
                        </div>
                    </div>
                    <span className="px-2 py-1 bg-apple-gray text-gray-500 text-xs font-semibold rounded-lg uppercase tracking-wide">
                        {item.level}
                    </span>
                </div>

                <div className="mt-4 space-y-1">
                    <p className="text-gray-900 font-medium leading-snug">{item.meaning_cn}</p>
                    <p className="text-gray-500 text-sm leading-snug">{item.meaning_en}</p>
                </div>

                {item.example_sentence && (
                    <div
                        className="mt-4 pt-4 border-t border-gray-100 cursor-pointer group"
                        onClick={() => speak(item.example_sentence!)}
                    >
                        <p className="text-sm text-gray-600 font-jp leading-relaxed group-hover:text-apple-blue transition-colors">
                            {item.example_sentence}
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default WordCard;
