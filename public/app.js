const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const scrollSentinel = document.getElementById('scrollSentinel');
const furiganaStatus = document.getElementById('furiganaStatus');
const ttsStatus = document.getElementById('ttsStatus');
const openaiKeyInput = document.getElementById('openaiKeyInput');
const voiceSelect = document.getElementById('voiceSelect');

const PAGE_SIZE = 80;
const SEARCH_DEBOUNCE_MS = 250;
const OPENAI_MODEL = 'gpt-4o-mini-tts';
const OPENAI_TTS_INSTRUCTIONS = 'Speak in natural conversational Japanese with clear pronunciation and moderate pace.';
const OPENAI_API_URL = 'https://api.openai.com/v1/audio/speech';
const OPENAI_KEY_STORAGE_KEY = 'openai_api_key_session';
const MAX_AUDIO_CACHE = 24;

let sourceMeta = [];
let currentSourceId = '';
let searchTimer = null;
let observer = null;
let autoLoading = false;
let openaiRequestController = null;
let activeAudio = null;

const sourceState = new Map();
const audioCache = new Map();

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
    if (oldUrl) URL.revokeObjectURL(oldUrl);
  }
}

function getOpenAIKey() {
  return openaiKeyInput.value.trim();
}

function saveOpenAIKey() {
  const key = getOpenAIKey();
  if (key) {
    sessionStorage.setItem(OPENAI_KEY_STORAGE_KEY, key);
  } else {
    sessionStorage.removeItem(OPENAI_KEY_STORAGE_KEY);
  }
}

async function speakWithOpenAI(text, apiKey) {
  const voice = voiceSelect.value || 'coral';
  const cacheKey = `${voice}::${text}`;

  if (audioCache.has(cacheKey)) {
    await playAudioUrl(audioCache.get(cacheKey));
    setTtsStatus(`语音：OpenAI ${voice}（缓存）`);
    return;
  }

  if (openaiRequestController) {
    openaiRequestController.abort();
  }
  openaiRequestController = new AbortController();

  setTtsStatus('语音：OpenAI 生成中...');

  const response = await fetch(OPENAI_API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model: OPENAI_MODEL,
      voice,
      input: text,
      response_format: 'mp3',
      instructions: OPENAI_TTS_INSTRUCTIONS,
    }),
    signal: openaiRequestController.signal,
  });

  if (!response.ok) {
    let errMessage = `OpenAI TTS 失败 (${response.status})`;
    try {
      const payload = await response.json();
      if (payload?.error?.message) {
        errMessage = payload.error.message;
      }
    } catch (err) {
      // keep fallback message
    }
    throw new Error(errMessage);
  }

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  putAudioCache(cacheKey, url);
  await playAudioUrl(url);
  setTtsStatus(`语音：OpenAI ${voice}`);
}

function speakWithBrowser(text) {
  stopAllSpeech();
  if (!('speechSynthesis' in window)) {
    alert('浏览器不支持 TTS');
    return;
  }
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'ja-JP';
  window.speechSynthesis.speak(utter);
  setTtsStatus('语音：浏览器回退（未配置 OpenAI Key）');
}

async function speak(text) {
  if (!text) return;

  const apiKey = getOpenAIKey();
  if (!apiKey) {
    speakWithBrowser(text);
    return;
  }

  try {
    await speakWithOpenAI(text, apiKey);
  } catch (err) {
    if (err.name === 'AbortError') {
      return;
    }
    console.error(err);
    setTtsStatus(`语音：OpenAI失败，已回退 (${err.message})`);
    speakWithBrowser(text);
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
  const savedKey = sessionStorage.getItem(OPENAI_KEY_STORAGE_KEY) || '';
  if (savedKey) {
    openaiKeyInput.value = savedKey;
  }

  openaiKeyInput.addEventListener('change', () => {
    saveOpenAIKey();
    if (getOpenAIKey()) {
      setTtsStatus(`语音：OpenAI ${voiceSelect.value}`);
    } else {
      setTtsStatus('语音：浏览器回退（未配置 OpenAI Key）');
    }
  });

  voiceSelect.addEventListener('change', () => {
    if (getOpenAIKey()) {
      setTtsStatus(`语音：OpenAI ${voiceSelect.value}`);
    }
  });
}

async function init() {
  furiganaStatus.textContent = '假名模式：预生成（稳定）';
  setTtsStatus('语音：浏览器回退（未配置 OpenAI Key）');

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

  if (getOpenAIKey()) {
    setTtsStatus(`语音：OpenAI ${voiceSelect.value}`);
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
