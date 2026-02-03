import { useState, useEffect } from 'react';
import { useInView } from 'react-intersection-observer';
import { Volume2, Loader2, BookOpen } from 'lucide-react';
import clsx from 'clsx';

export function SmartWordCard({ data, googleKey, yahooId, index }) {
    const { word, meaning_cn, meaning_en, level, example, ruby_html, examples } = data;
    const [ref, inView] = useInView({
        triggerOnce: true,
        threshold: 0.1,
    });

    const [displayHtml, setDisplayHtml] = useState(ruby_html || word);
    const [isLoadingFurigana, setIsLoadingFurigana] = useState(false);

    // Determine effective example
    const displayExample = example || (examples && examples.length > 0 ? examples[0].text : null);

    // Play Audio (Google TTS)
    const playAudio = async (textToPlay) => {
        if (!googleKey) {
            alert('Please set your Google Cloud API Key in settings.');
            return;
        }
        if (!textToPlay) return;

        // Basic cache for audio URLs using display text as partial key (careful with memory)
        // For now, direct fetch.
        const url = `https://texttospeech.googleapis.com/v1/text:synthesize?key=${googleKey}`;
        const payload = {
            input: { text: textToPlay },
            voice: { languageCode: 'ja-JP', ssmlGender: 'NEUTRAL' },
            audioConfig: { audioEncoding: 'MP3' }
        };

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const result = await response.json();
            if (result.audioContent) {
                const audio = new Audio("data:audio/mp3;base64," + result.audioContent);
                audio.play();
            } else {
                console.error(result);
                alert('TTS Error: ' + (result.error ? result.error.message : 'Unknown error'));
            }
        } catch (e) {
            console.error(e);
            alert('Network Error: ' + e.message);
        }
    };

    // Fetch Furigana (Yahoo API)
    useEffect(() => {
        // If we already have ruby_html from JSON, we don't need to fetch
        if (ruby_html) return;

        // If not in view or no API key, skip
        if (!inView || !yahooId) return;

        // Check Cache
        const cacheKey = `furigana_v2_${word}`;
        const cached = localStorage.getItem(cacheKey);
        if (cached) {
            setDisplayHtml(cached);
            return;
        }

        const fetchFurigana = async () => {
            setIsLoadingFurigana(true);
            try {
                // Yahoo Japan Furigana Service V2
                // Note: This often requires a proxy due to CORS. 
                // We will try a CORS proxy if direct fails, or assume user has a solution.
                // Using a public CORS proxy is not secure for secrets, but for ClientID it's "okayish" for a personal tool.
                // For this implementation, we try direct. If it fails, user sees it in console.
                const url = `https://jlp.yahooapis.jp/FuriganaService/V2/furigana`;

                // Yahoo API expects a POST request
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'User-Agent': `Yahoo AppID: ${yahooId}`,
                    },
                    body: JSON.stringify({
                        id: '1234-1', // Request ID
                        jsonrpc: '2.0',
                        method: 'jlp.furiganaservice.furigana',
                        params: {
                            q: word,
                            grade: 1, // 1=elementary school level (more furigana)
                        }
                    })
                });

                if (!response.ok) throw new Error('Yahoo API Error');

                const data = await response.json();
                if (data.result && data.result.word) {
                    // Construct Ruby HTML from result
                    // Result is list of { surface, furigana, roman, ... }
                    const html = data.result.word.map(w => {
                        if (w.furigana) {
                            return `<ruby>${w.surface}<rt>${w.furigana}</rt></ruby>`;
                        }
                        return w.surface;
                    }).join('');

                    setDisplayHtml(html);
                    localStorage.setItem(cacheKey, html);
                }

            } catch (error) {
                console.error('Furigana Fetch Error:', error);
                // Fallback: just keep displaying the word
            } finally {
                setIsLoadingFurigana(false);
            }
        };

        fetchFurigana();
    }, [inView, yahooId, word, ruby_html]);

    // Styling
    const levelColors = {
        N1: "bg-red-50 text-red-600 border-red-100 dark:bg-red-900/20 dark:text-red-300 dark:border-red-900/50",
        N2: "bg-orange-50 text-orange-600 border-orange-100 dark:bg-orange-900/20 dark:text-orange-300 dark:border-orange-900/50",
        N3: "bg-yellow-50 text-yellow-600 border-yellow-100 dark:bg-yellow-900/20 dark:text-yellow-300 dark:border-yellow-900/50",
        N4: "bg-green-50 text-green-600 border-green-100 dark:bg-green-900/20 dark:text-green-300 dark:border-green-900/50",
        N5: "bg-blue-50 text-blue-600 border-blue-100 dark:bg-blue-900/20 dark:text-blue-300 dark:border-blue-900/50",
    };

    return (
        <div ref={ref} className="group relative break-inside-avoid">
            <div className="relative overflow-hidden bg-white/70 dark:bg-slate-900/70 backdrop-blur-xl rounded-2xl p-6 border border-white/20 dark:border-slate-700 shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-1">

                {/* Gradient Glow Effect on Hover */}
                <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/0 via-purple-500/0 to-pink-500/0 opacity-0 group-hover:opacity-10 transition-opacity duration-500 pointer-events-none" />

                {/* Header Badge */}
                <div className="flex justify-between items-start mb-6">
                    <span className="text-xs font-mono text-slate-400 dark:text-slate-500/50">#{index}</span>
                    <span className={clsx("px-2.5 py-1 rounded-full text-[10px] font-bold tracking-wide uppercase border", levelColors[level])}>
                        {level}
                    </span>
                </div>

                {/* Main Word Section */}
                <div className="text-center relative mb-8">
                    {/* Word */}
                    <div className="relative inline-block">
                        <h2
                            className="text-4xl md:text-5xl font-black text-slate-800 dark:text-slate-100 tracking-tight"
                            dangerouslySetInnerHTML={{ __html: displayHtml }}
                        />
                        {isLoadingFurigana && (
                            <div className="absolute -right-6 top-0 text-slate-300 animate-spin">
                                <Loader2 className="w-4 h-4" />
                            </div>
                        )}
                    </div>

                    {/* Action Buttons */}
                    <div className="mt-4 flex justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 transform translate-y-2 group-hover:translate-y-0">
                        <button
                            onClick={() => playAudio(word)}
                            className="p-2 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-500 hover:text-indigo-600 hover:bg-indigo-50 dark:hover:bg-slate-700 transition-colors tooltip"
                            title="Play Pronunciation"
                        >
                            <Volume2 className="w-5 h-5" />
                        </button>
                    </div>
                </div>

                {/* Divider */}
                <div className="w-16 h-1 mx-auto bg-gradient-to-r from-transparent via-slate-200 dark:via-slate-700 to-transparent rounded-full mb-6"></div>

                {/* Meanings */}
                <div className="space-y-4 mb-6">
                    <div className="text-center">
                        <p className="text-lg font-bold text-slate-800 dark:text-slate-100 leading-snug">
                            {meaning_cn}
                        </p>
                        {meaning_en && meaning_en.length > 0 && (
                            <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 font-medium">
                                {meaning_en.slice(0, 3).join(", ")}
                            </p>
                        )}
                    </div>
                </div>

                {/* Example Section */}
                {displayExample && (
                    <div className="mt-auto bg-slate-50/50 dark:bg-slate-800/50 rounded-xl p-4 border border-slate-100 dark:border-slate-800/50">
                        <div className="flex items-start gap-3">
                            <BookOpen className="w-4 h-4 text-slate-400 mt-1 flex-shrink-0" />
                            <div className="flex-1">
                                <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed font-serif">
                                    {displayExample}
                                </p>
                            </div>
                            <button
                                onClick={() => playAudio(displayExample)}
                                className="text-slate-400 hover:text-indigo-500 transition-colors"
                            >
                                <Volume2 className="w-4 h-4" />
                            </button>
                        </div>
                    </div>
                )}

            </div>
        </div>
    );
}
