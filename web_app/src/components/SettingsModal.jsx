import { useState, useEffect } from 'react';
import { X, Save, Key, Globe } from 'lucide-react';
import clsx from 'clsx'; // Although imported, standard usage or simple string concat works too if logic simple.

export function SettingsModal({ isOpen, onClose }) {
    const [googleKey, setGoogleKey] = useState('');
    const [yahooId, setYahooId] = useState('');

    useEffect(() => {
        if (isOpen) {
            setGoogleKey(window.localStorage.getItem('google_tts_key') || '');
            setYahooId(window.localStorage.getItem('yahoo_client_id') || '');
        }
    }, [isOpen]);

    const handleSave = () => {
        window.localStorage.setItem('google_tts_key', googleKey);
        window.localStorage.setItem('yahoo_client_id', yahooId);
        onClose();
        // Ideally we would trigger a context update or re-render, but for now specific components read from localStorage or passed props
        // We might need to refresh App state if keys change, simplest is window reload or callback
        window.location.reload();
    };

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm transition-opacity">
            <div className="bg-white dark:bg-slate-900 rounded-2xl shadow-2xl w-full max-w-md overflow-hidden border border-slate-200 dark:border-slate-800 animate-in fade-in zoom-in duration-200">

                {/* Header */}
                <div className="px-6 py-4 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-800/50">
                    <h2 className="text-lg font-bold text-slate-800 dark:text-white flex items-center gap-2">
                        <Key className="w-5 h-5 text-indigo-500" />
                        API Configuration
                    </h2>
                    <button
                        onClick={onClose}
                        className="p-1 rounded-full hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors text-slate-500"
                    >
                        <X className="w-5 h-5" />
                    </button>
                </div>

                {/* content */}
                <div className="p-6 space-y-6">
                    <p className="text-sm text-slate-500 dark:text-slate-400">
                        These keys are stored locally in your browser and used to fetch data directly from Yahoo and Google services.
                    </p>

                    {/* Yahoo Input */}
                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300">
                            Yahoo Client ID (Furigana)
                        </label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <Globe className="h-4 w-4 text-slate-400" />
                            </div>
                            <input
                                type="password"
                                value={yahooId}
                                onChange={(e) => setYahooId(e.target.value)}
                                className="block w-full pl-10 pr-3 py-2 border border-slate-300 dark:border-slate-700 rounded-lg bg-white dark:bg-slate-800 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-shadow sm:text-sm"
                                placeholder="Enter Yahoo Client ID"
                            />
                        </div>
                        <p className="text-xs text-slate-400">
                            Required for dynamic Furigana generation.
                        </p>
                    </div>

                    {/* Google Input */}
                    <div className="space-y-2">
                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300">
                            Google Cloud API Key (TTS)
                        </label>
                        <div className="relative">
                            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <Key className="h-4 w-4 text-slate-400" />
                            </div>
                            <input
                                type="password"
                                value={googleKey}
                                onChange={(e) => setGoogleKey(e.target.value)}
                                className="block w-full pl-10 pr-3 py-2 border border-slate-300 dark:border-slate-700 rounded-lg bg-white dark:bg-slate-800 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-shadow sm:text-sm"
                                placeholder="Enter Google API Key"
                            />
                        </div>
                        <p className="text-xs text-slate-400">
                            Required for Text-to-Speech audio.
                        </p>
                    </div>
                </div>

                {/* Footer */}
                <div className="px-6 py-4 bg-slate-50 dark:bg-slate-800/50 flex justify-end gap-3 border-t border-slate-100 dark:border-slate-800">
                    <button
                        onClick={onClose}
                        className="px-4 py-2 text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-slate-800 dark:hover:text-white transition-colors"
                    >
                        Cancel
                    </button>
                    <button
                        onClick={handleSave}
                        className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg shadow-sm hover:shadow transition-all"
                    >
                        <Save className="w-4 h-4" />
                        Save Configuration
                    </button>
                </div>

            </div>
        </div>
    );
}
