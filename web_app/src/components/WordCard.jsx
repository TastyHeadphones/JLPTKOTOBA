export function WordCard({ data, apiKey, index }) {
    const { word, reading, meaning_cn, meaning_en, level, example, ruby_html, examples } = data;

    // Backward compatibility for example
    const displayExample = example || (examples && examples.length > 0 ? examples[0].text : null);

    // Audio Playback
    const playAudio = async (textToPlay) => {
        if (!apiKey) {
            alert('Please enter your Google Cloud API Key at the top of the page.');
            return;
        }
        if (!textToPlay) return;

        const url = `https://texttospeech.googleapis.com/v1/text:synthesize?key=${apiKey}`;
        const payload = {
            input: { text: textToPlay },
            voice: { languageCode: 'ja-JP', ssmlGender: 'NEUTRAL' },
            audioConfig: { audioEncoding: 'MP3' }
        };

        try {
            const response = await fetch(url, {
                method: 'POST',
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
            alert('Network Error: ' + e.message);
        }
    };

    // Level Badge Colors
    const levelColors = {
        N1: "bg-red-100 text-red-700 border-red-200 dark:bg-red-900/30 dark:text-red-300 dark:border-red-800",
        N2: "bg-orange-100 text-orange-700 border-orange-200 dark:bg-orange-900/30 dark:text-orange-300 dark:border-orange-800",
        N3: "bg-yellow-100 text-yellow-700 border-yellow-200 dark:bg-yellow-900/30 dark:text-yellow-300 dark:border-yellow-800",
        N4: "bg-green-100 text-green-700 border-green-200 dark:bg-green-900/30 dark:text-green-300 dark:border-green-800",
        N5: "bg-blue-100 text-blue-700 border-blue-200 dark:bg-blue-900/30 dark:text-blue-300 dark:border-blue-800",
    };

    return (
        <div className="group relative bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-100 dark:border-slate-700 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">

            {/* Index Badge */}
            <div className="absolute top-4 left-4 text-xs font-mono text-slate-300 dark:text-slate-600">
                #{index}
            </div>

            {/* Top Row: Level & Reading */}
            <div className="flex justify-end items-start mb-2">
                <span className={`px-2 py-0.5 rounded-md text-xs font-bold border ${levelColors[level] || "bg-gray-100"}`}>
                    {level}
                </span>
            </div>
            <div className="text-center -mt-2 mb-1">
                <span className="text-sm text-slate-500 font-mono tracking-wide">{reading}</span>
            </div>

            {/* Main Word */}
            <div className="mb-4 text-center flex items-center justify-center gap-2">
                <button
                    onClick={() => playAudio(word)}
                    className="text-slate-300 hover:text-indigo-500 transition-colors p-1"
                    title="Play Word"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M19.114 5.636a9 9 0 0 1 0 12.728M16.463 8.288a5.25 5.25 0 0 1 0 7.424M6.75 8.25l4.72-4.72a.75.75 0 0 1 1.28.53v15.88a.75.75 0 0 1-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.009 9.009 0 0 1 2.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75Z" />
                    </svg>
                </button>
                <h2 className="text-4xl font-bold bg-clip-text text-slate-800 dark:text-slate-100 py-1"
                    dangerouslySetInnerHTML={{ __html: ruby_html || word }}
                />
            </div>

            {/* Divider */}
            <div className="h-px bg-slate-100 dark:bg-slate-700 mb-4 w-full"></div>

            {/* Meanings */}
            <div className="space-y-2">
                <div>
                    <p className="text-lg font-bold text-slate-800 dark:text-slate-100 leading-snug">
                        {meaning_cn}
                    </p>
                </div>
                {meaning_en && meaning_en.length > 0 && (
                    <div>
                        <p className="text-sm text-slate-500 dark:text-slate-400 italic">
                            {meaning_en.slice(0, 3).join(", ")}
                        </p>
                    </div>
                )}
            </div>

            {/* Examples (Optional) */}
            {displayExample && (
                <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-700">
                    <div className="flex items-center gap-2 mb-1">
                        <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Example</span>
                        <button onClick={() => playAudio(displayExample)} className="text-slate-400 hover:text-indigo-500 transition-colors" title="Play Example">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M19.114 5.636a9 9 0 0 1 0 12.728M16.463 8.288a5.25 5.25 0 0 1 0 7.424M6.75 8.25l4.72-4.72a.75.75 0 0 1 1.28.53v15.88a.75.75 0 0 1-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.009 9.009 0 0 1 2.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75Z" />
                            </svg>
                        </button>
                    </div>
                    <div className="text-sm text-slate-600 dark:text-slate-300 text-xs bg-slate-50 dark:bg-slate-700/50 p-2 rounded">
                        <p>{displayExample}</p>
                    </div>
                </div>
            )}
        </div>
    );
}
