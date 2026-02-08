const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const scrollSentinel = document.getElementById('scrollSentinel');
const furiganaStatus = document.getElementById('furiganaStatus');
const ttsStatus = document.getElementById('ttsStatus');
const geminiKeyInput = document.getElementById('geminiKeyInput');
const voiceSelect = document.getElementById('voiceSelect');

const PAGE_SIZE = 80;
const SEARCH_DEBOUNCE_MS = 250;

const GEMINI_MODEL = 'gemini-2.5-flash-preview-tts';
const GEMINI_API_URL = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent`;
const GEMINI_KEY_STORAGE_KEY = 'gemini_api_key_persist';
const GEMINI_FALLBACK_STATUS = '语音：浏览器回退（未配置 Gemini Key）';
const GEMINI_DEFAULT_VOICE = 'Iapetus';
const MAX_AUDIO_CACHE = 16;

let sourceMeta = [];
let currentSourceId = '';
let searchTimer = null;
let observer = null;
let autoLoading = false;
let ttsRequestController = null;
let activeAudio = null;
let bestBrowserVoice = null;

const sourceState = new Map();
const audioCache = new Map();

function scoreBrowserVoice(v) {
  const name = (v?.name || '').toLowerCase();
  const lang = (v?.lang || '').toLowerCase();
  let score = 0;

  if (lang.startsWith('ja')) score += 50;
  if (/siri/.test(name)) score += 120;
  if (/natural/.test(name)) score += 90;
  if (/kyoko|nanami|otoya|ja-jp/.test(name)) score += 80;
  if (/enhanced|premium|high quality/.test(name)) score += 60;
  if (v?.default) score += 15;

  return score;
}

function refreshBestBrowserVoice() {
  if (!('speechSynthesis' in window)) {
    bestBrowserVoice = null;
    return;
  }
  const voices = window.speechSynthesis.getVoices() || [];
  if (!voices.length) {
    bestBrowserVoice = null;
    return;
  }
  bestBrowserVoice = [...voices].sort((a, b) => scoreBrowserVoice(b) - scoreBrowserVoice(a))[0] || null;
}

function getMeta(sourceId) {
  return sourceMeta.find((s) => s.id === sourceId) || null;
}

function getState(sourceId) {
  if (!sourceState.has(sourceId)) {
    sourceState.set(sourceId, {
      items: [],
      loadedPages: 0,
      renderPage: 1,
      loading: false,
      loadAllRequested: false,
    });
  }
  return sourceState.get(sourceId);
}

async function fetchChunk(sourceId, page) {
  const res = await fetch(`data/${sourceId}_p${page}.json`);
  if (!res.ok) {
    throw new Error(`加载分片失败: ${sourceId} p${page}`);
  }
  return res.json();
}

async function loadUntil(sourceId, targetPages) {
  const meta = getMeta(sourceId);
  if (!meta) return;

  const state = getState(sourceId);
  if (state.loading) return;

  state.loading = true;
  try {
    while (state.loadedPages < targetPages && state.loadedPages < meta.pages) {
      const nextPage = state.loadedPages + 1;
      const chunk = await fetchChunk(sourceId, nextPage);
      state.items.push(...chunk);
      state.loadedPages = nextPage;
    }
  } finally {
    state.loading = false;
  }
}

async function loadAllForSearch(sourceId) {
  const meta = getMeta(sourceId);
  const state = getState(sourceId);
  if (!meta || state.loadAllRequested || state.loadedPages >= meta.pages) return;

  state.loadAllRequested = true;
  await loadUntil(sourceId, meta.pages);
  render();
}

function getFilteredWords(items) {
  const q = searchInput.value.trim().toLowerCase();
  if (!q) return items;

  return items.filter((w) => {
    const term = (w.term || '').toLowerCase();
    const zh = (w.zh || '').toLowerCase();
    const en = (w.en || '').toLowerCase();
    const example = (w.example || '').toLowerCase();
    return term.includes(q) || zh.includes(q) || en.includes(q) || example.includes(q);
  });
}

function setJapaneseContent(el, plain, rubyHtml) {
  if (furiganaToggle.checked && rubyHtml) {
    el.innerHTML = rubyHtml;
  } else {
    el.textContent = plain || '';
  }
}

function stopAllSpeech() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  if (activeAudio) {
    activeAudio.pause();
    activeAudio.currentTime = 0;
    activeAudio = null;
  }
}

async function playAudioUrl(url) {
  stopAllSpeech();
  activeAudio = new Audio(url);
  await activeAudio.play();
  activeAudio.onended = () => {
    activeAudio = null;
  };
}

function setTtsStatus(text) {
  ttsStatus.textContent = text;
}

function putAudioCache(cacheKey, url) {
  if (audioCache.has(cacheKey)) return;
  audioCache.set(cacheKey, url);

  if (audioCache.size > MAX_AUDIO_CACHE) {
    const oldest = audioCache.keys().next().value;
    const oldUrl = audioCache.get(oldest);
    audioCache.delete(oldest);
    if (oldUrl) {
      URL.revokeObjectURL(oldUrl);
    }
  }
}

function getGeminiKey() {
  return geminiKeyInput.value.trim();
}

function saveGeminiKey() {
  const key = getGeminiKey();
  if (key) {
    localStorage.setItem(GEMINI_KEY_STORAGE_KEY, key);
  } else {
    localStorage.removeItem(GEMINI_KEY_STORAGE_KEY);
  }
}

function parseSampleRate(mimeType) {
  const match = /rate=(\d+)/i.exec(mimeType || '');
  if (!match) return 24000;
  const value = Number(match[1]);
  return Number.isFinite(value) && value > 0 ? value : 24000;
}

function base64ToBytes(input) {
  const normalized = input.replace(/-/g, '+').replace(/_/g, '/');
  const padded = normalized + '='.repeat((4 - normalized.length % 4) % 4);
  const binary = atob(padded);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) {
    bytes[i] = binary.charCodeAt(i);
  }
  return bytes;
}

function pcm16ToWavBlob(pcmBytes, sampleRate) {
  const numChannels = 1;
  const bitsPerSample = 16;
  const blockAlign = (numChannels * bitsPerSample) / 8;
  const byteRate = sampleRate * blockAlign;
  const dataSize = pcmBytes.byteLength;
  const buffer = new ArrayBuffer(44 + dataSize);
  const view = new DataView(buffer);

  function writeAscii(offset, text) {
    for (let i = 0; i < text.length; i += 1) {
      view.setUint8(offset + i, text.charCodeAt(i));
    }
  }

  writeAscii(0, 'RIFF');
  view.setUint32(4, 36 + dataSize, true);
  writeAscii(8, 'WAVE');
  writeAscii(12, 'fmt ');
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, numChannels, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, byteRate, true);
  view.setUint16(32, blockAlign, true);
  view.setUint16(34, bitsPerSample, true);
  writeAscii(36, 'data');
  view.setUint32(40, dataSize, true);

  new Uint8Array(buffer, 44).set(pcmBytes);
  return new Blob([buffer], { type: 'audio/wav' });
}

function buildPlayableAudioBlob(base64Data, mimeType) {
  const bytes = base64ToBytes(base64Data);
  const lowerMime = (mimeType || '').toLowerCase();

  if (
    lowerMime.includes('audio/wav') ||
    lowerMime.includes('audio/mpeg') ||
    lowerMime.includes('audio/mp3') ||
    lowerMime.includes('audio/ogg') ||
    lowerMime.includes('audio/webm') ||
    lowerMime.includes('audio/aac')
  ) {
    const type = lowerMime.split(';')[0] || 'audio/mpeg';
    return new Blob([bytes], { type });
  }

  const sampleRate = parseSampleRate(mimeType);
  return pcm16ToWavBlob(bytes, sampleRate);
}

async function speakWithGemini(text, apiKey) {
  const voiceName = voiceSelect.value || GEMINI_DEFAULT_VOICE;
  const cacheKey = `${voiceName}::${text}`;

  if (audioCache.has(cacheKey)) {
    await playAudioUrl(audioCache.get(cacheKey));
    setTtsStatus(`语音：Gemini ${voiceName}（缓存）`);
    return;
  }

  if (ttsRequestController) {
    ttsRequestController.abort();
  }
  ttsRequestController = new AbortController();

  setTtsStatus('语音：Gemini 生成中...');

  const response = await fetch(GEMINI_API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-goog-api-key': apiKey,
    },
    body: JSON.stringify({
      systemInstruction: {
        parts: [{ text: 'Read the user text in natural Japanese (ja-JP). Keep wording unchanged.' }],
      },
      contents: [
        {
          parts: [{ text }],
        },
      ],
      generationConfig: {
        responseModalities: ['AUDIO'],
        speechConfig: {
          voiceConfig: {
            prebuiltVoiceConfig: {
              voiceName,
            },
          },
        },
      },
    }),
    signal: ttsRequestController.signal,
  });

  if (!response.ok) {
    let errMessage = `Gemini TTS 失败 (${response.status})`;
    try {
      const payload = await response.json();
      if (payload?.error?.message) {
        errMessage = payload.error.message;
      }
    } catch (err) {
      // ignore parsing failure
    }
    throw new Error(errMessage);
  }

  const payload = await response.json();
  const part = payload?.candidates?.[0]?.content?.parts?.find((p) => p?.inlineData?.data);
  const base64Data = part?.inlineData?.data;
  const mimeType = part?.inlineData?.mimeType || 'audio/L16;rate=24000';

  if (!base64Data) {
    throw new Error('Gemini 未返回音频数据');
  }

  const audioBlob = buildPlayableAudioBlob(base64Data, mimeType);
  const url = URL.createObjectURL(audioBlob);
  putAudioCache(cacheKey, url);

  await playAudioUrl(url);
  setTtsStatus(`语音：Gemini ${voiceName}`);
}

function speakWithBrowser(text, reason = GEMINI_FALLBACK_STATUS) {
  stopAllSpeech();
  if (!('speechSynthesis' in window)) {
    alert('浏览器不支持 TTS');
    return;
  }
  refreshBestBrowserVoice();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'ja-JP';
  if (bestBrowserVoice) {
    utter.voice = bestBrowserVoice;
  }
  utter.rate = 0.95;
  utter.pitch = 1.0;
  window.speechSynthesis.speak(utter);
  if (bestBrowserVoice) {
    setTtsStatus(`${reason} (${bestBrowserVoice.name})`);
  } else {
    setTtsStatus(reason);
  }
}

async function speak(text) {
  if (!text) return;

  const apiKey = getGeminiKey();
  if (!apiKey) {
    speakWithBrowser(text, GEMINI_FALLBACK_STATUS);
    return;
  }

  try {
    await speakWithGemini(text, apiKey);
  } catch (err) {
    if (err.name === 'AbortError') {
      return;
    }
    console.error(err);
    speakWithBrowser(text, `语音：Gemini失败，已回退 (${err.message})`);
  }
}

function render() {
  const meta = getMeta(currentSourceId);
  const state = getState(currentSourceId);
  const filtered = getFilteredWords(state.items);
  const visibleCount = Math.min(filtered.length, state.renderPage * PAGE_SIZE);
  const visible = filtered.slice(0, visibleCount);

  countEl.textContent = `${visibleCount}/${filtered.length}`;
  listEl.innerHTML = '';

  const fragment = document.createDocumentFragment();
  visible.forEach((w) => {
    const node = template.content.cloneNode(true);
    const termBtn = node.querySelector('.speak.term');
    const exampleBtn = node.querySelector('.speak.example');
    const badge = node.querySelector('.badge');
    const zh = node.querySelector('.value.zh');
    const en = node.querySelector('.value.en');

    setJapaneseContent(termBtn, w.term || '', w.term_ruby || '');
    termBtn.addEventListener('click', () => {
      speak(w.term || '');
    });

    setJapaneseContent(exampleBtn, w.example || '', w.example_ruby || '');
    exampleBtn.addEventListener('click', () => {
      speak(w.example || '');
    });

    badge.textContent = (w.source || '').replace('wordlist.pdf', '');
    zh.textContent = w.zh || '—';
    en.textContent = w.en || '—';

    fragment.appendChild(node);
  });

  listEl.appendChild(fragment);

  const hasMoreRendered = visibleCount < filtered.length;
  const hasMoreSourcePages = !!meta && state.loadedPages < meta.pages;
  scrollSentinel.style.display = hasMoreRendered || hasMoreSourcePages ? 'block' : 'none';
}

function resetAndRender() {
  const state = getState(currentSourceId);
  state.renderPage = 1;
  render();
}

async function onSourceChange() {
  currentSourceId = sourceFilter.value;
  const state = getState(currentSourceId);

  if (state.loadedPages === 0) {
    await loadUntil(currentSourceId, 1);
  }

  state.renderPage = 1;
  render();

  if (searchInput.value.trim()) {
    loadAllForSearch(currentSourceId);
  }
}

async function autoLoadNextPage() {
  const meta = getMeta(currentSourceId);
  const state = getState(currentSourceId);
  if (!meta || autoLoading) return;

  const filtered = getFilteredWords(state.items);
  const visibleCount = Math.min(filtered.length, state.renderPage * PAGE_SIZE);
  const hasMoreRendered = visibleCount < filtered.length;
  const hasMoreSourcePages = state.loadedPages < meta.pages;
  if (!hasMoreRendered && !hasMoreSourcePages) return;

  autoLoading = true;
  try {
    if (hasMoreRendered) {
      state.renderPage += 1;
    } else {
      await loadUntil(currentSourceId, state.loadedPages + 1);
      state.renderPage += 1;
    }
    render();
  } finally {
    autoLoading = false;
  }
}

function setupInfiniteScroll() {
  if (!('IntersectionObserver' in window)) return;

  observer = new IntersectionObserver((entries) => {
    const entry = entries[0];
    if (!entry || !entry.isIntersecting) return;
    autoLoadNextPage();
  }, {
    root: null,
    rootMargin: '600px 0px 600px 0px',
    threshold: 0,
  });

  observer.observe(scrollSentinel);
}

function initSourceFilter() {
  sourceFilter.innerHTML = '';
  sourceMeta.forEach((meta) => {
    const opt = document.createElement('option');
    opt.value = meta.id;
    opt.textContent = `${meta.label} (${meta.count})`;
    sourceFilter.appendChild(opt);
  });
}

function initKeyAndVoice() {
  if (!voiceSelect.value) {
    voiceSelect.value = GEMINI_DEFAULT_VOICE;
  }

  const savedKey = localStorage.getItem(GEMINI_KEY_STORAGE_KEY) || '';
  if (savedKey) {
    geminiKeyInput.value = savedKey;
  }

  function syncGeminiKeyStatus() {
    saveGeminiKey();
    if (getGeminiKey()) {
      setTtsStatus(`语音：Gemini ${voiceSelect.value || GEMINI_DEFAULT_VOICE}`);
    } else {
      setTtsStatus(GEMINI_FALLBACK_STATUS);
    }
  }

  geminiKeyInput.addEventListener('input', syncGeminiKeyStatus);
  geminiKeyInput.addEventListener('change', syncGeminiKeyStatus);

  voiceSelect.addEventListener('change', () => {
    if (getGeminiKey()) {
      setTtsStatus(`语音：Gemini ${voiceSelect.value || GEMINI_DEFAULT_VOICE}`);
    }
  });
}

async function init() {
  furiganaStatus.textContent = '假名模式：预生成（稳定）';
  setTtsStatus(GEMINI_FALLBACK_STATUS);

  const res = await fetch('data/index.json');
  if (!res.ok) {
    furiganaStatus.textContent = '数据索引加载失败';
    return;
  }

  const index = await res.json();
  sourceMeta = index.sources || [];
  if (!sourceMeta.length) {
    furiganaStatus.textContent = '没有可用词条数据';
    return;
  }

  initSourceFilter();
  currentSourceId = sourceMeta[0].id;
  sourceFilter.value = currentSourceId;

  await loadUntil(currentSourceId, 1);
  render();
  setupInfiniteScroll();
  initKeyAndVoice();
  refreshBestBrowserVoice();
  if ('speechSynthesis' in window && 'onvoiceschanged' in window.speechSynthesis) {
    window.speechSynthesis.onvoiceschanged = () => {
      refreshBestBrowserVoice();
    };
  }

  if (getGeminiKey()) {
    setTtsStatus(`语音：Gemini ${voiceSelect.value || GEMINI_DEFAULT_VOICE}`);
  }
}

searchInput.addEventListener('input', () => {
  resetAndRender();
  if (searchTimer) {
    clearTimeout(searchTimer);
  }
  searchTimer = setTimeout(() => {
    if (searchInput.value.trim()) {
      loadAllForSearch(currentSourceId);
    }
  }, SEARCH_DEBOUNCE_MS);
});

sourceFilter.addEventListener('change', () => {
  onSourceChange().catch((err) => {
    console.error(err);
    furiganaStatus.textContent = `切换来源失败：${err.message}`;
  });
});

furiganaToggle.addEventListener('change', render);

window.addEventListener('beforeunload', () => {
  for (const url of audioCache.values()) {
    URL.revokeObjectURL(url);
  }
});

init().catch((err) => {
  console.error(err);
  furiganaStatus.textContent = `初始化失败：${err.message}`;
});
