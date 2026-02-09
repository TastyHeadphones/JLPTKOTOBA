const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const selectAllSourcesBtn = document.getElementById('selectAllSources');
const clearSourcesBtn = document.getElementById('clearSources');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const scrollSentinel = document.getElementById('scrollSentinel');
const furiganaStatus = document.getElementById('furiganaStatus');
const ttsStatus = document.getElementById('ttsStatus');
const cloudTtsKeyInput = document.getElementById('cloudTtsKeyInput');
const voiceSelect = document.getElementById('voiceSelect');

const PAGE_SIZE = 80;
const BATCH_MARK_INTERVAL = 200;
const SEARCH_DEBOUNCE_MS = 250;

const CLOUD_TTS_API_URL = 'https://texttospeech.googleapis.com/v1/text:synthesize';
const CLOUD_TTS_VOICES_URL = 'https://texttospeech.googleapis.com/v1/voices';
const CLOUD_TTS_KEY_STORAGE_KEY = 'cloud_tts_api_key_persist';
const CLOUD_TTS_FALLBACK_STATUS = '语音：浏览器回退（未配置 Cloud TTS Key）';
const CLOUD_TTS_DEFAULT_VOICE = 'ja-JP-Chirp3-HD-Iapetus';
const MAX_AUDIO_CACHE = 16;

let sourceMeta = [];
let selectedSourceIds = [];
let renderPage = 1;
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
      loading: false,
      loadAllRequested: false,
    });
  }
  return sourceState.get(sourceId);
}

function getSourceOptionInputs() {
  return Array.from(sourceFilter.querySelectorAll('.source-option-input'));
}

function getSelectedSourceIdsFromControl() {
  return getSourceOptionInputs()
    .filter((input) => input.checked)
    .map((input) => input.value);
}

function setSelectedSourceIds(ids) {
  selectedSourceIds = sourceMeta
    .map((meta) => meta.id)
    .filter((id) => ids.includes(id));
}

function selectAllSources() {
  getSourceOptionInputs().forEach((input) => {
    input.checked = true;
  });
  setSelectedSourceIds(getSelectedSourceIdsFromControl());
}

function getSelectedMetas() {
  return sourceMeta.filter((meta) => selectedSourceIds.includes(meta.id));
}

function getCombinedItems() {
  const items = [];
  getSelectedMetas().forEach((meta) => {
    const state = getState(meta.id);
    items.push(...state.items);
  });
  return items;
}

function hasAnyMoreSourcePages() {
  return getSelectedMetas().some((meta) => {
    const state = getState(meta.id);
    return state.loadedPages < meta.pages;
  });
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
}

async function loadSelectedUntil(targetPages = 1) {
  for (const sourceId of selectedSourceIds) {
    const state = getState(sourceId);
    if (state.loadedPages >= targetPages) continue;
    await loadUntil(sourceId, targetPages);
  }
}

async function loadAllForSearchSelected() {
  for (const sourceId of selectedSourceIds) {
    await loadAllForSearch(sourceId);
  }
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

function getCloudTtsKey() {
  return cloudTtsKeyInput.value.trim();
}

function saveCloudTtsKey() {
  const key = getCloudTtsKey();
  if (key) {
    localStorage.setItem(CLOUD_TTS_KEY_STORAGE_KEY, key);
  } else {
    localStorage.removeItem(CLOUD_TTS_KEY_STORAGE_KEY);
  }
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

function scoreCloudVoiceName(name) {
  let score = 0;
  if (name.includes('Chirp3-HD')) score += 400;
  else if (name.includes('Neural2')) score += 300;
  else if (name.includes('Wavenet')) score += 200;
  else if (name.includes('Standard')) score += 100;

  if (name.endsWith('Iapetus')) score += 40;
  if (name.endsWith('Kore')) score += 30;
  if (name.endsWith('Schedar')) score += 20;

  return score;
}

function makeCloudVoiceLabel(name) {
  if (name.includes('Chirp3-HD-')) {
    return `${name.replace('ja-JP-Chirp3-HD-', '')} (Chirp3-HD)`;
  }
  if (name.includes('Neural2-')) {
    return `${name.replace('ja-JP-', '')} (Neural2)`;
  }
  if (name.includes('Wavenet-')) {
    return `${name.replace('ja-JP-', '')} (Wavenet)`;
  }
  if (name.includes('Standard-')) {
    return `${name.replace('ja-JP-', '')} (Standard)`;
  }
  return name;
}

function populateVoiceSelect(voiceNames, preserveValue = '') {
  const uniqueNames = [...new Set(voiceNames)].filter(Boolean);
  if (!uniqueNames.length) return;

  const preferred =
    (preserveValue && uniqueNames.includes(preserveValue) && preserveValue) ||
    (uniqueNames.includes(CLOUD_TTS_DEFAULT_VOICE) && CLOUD_TTS_DEFAULT_VOICE) ||
    uniqueNames[0];

  voiceSelect.innerHTML = '';
  uniqueNames.forEach((name) => {
    const option = document.createElement('option');
    option.value = name;
    option.textContent = makeCloudVoiceLabel(name);
    voiceSelect.appendChild(option);
  });

  voiceSelect.value = preferred;
}

async function fetchCloudVoiceNames(apiKey) {
  const url = `${CLOUD_TTS_VOICES_URL}?languageCode=ja-JP&key=${encodeURIComponent(apiKey)}`;
  const res = await fetch(url);
  if (!res.ok) {
    let errMessage = `Cloud TTS voice 列表失败 (${res.status})`;
    try {
      const payload = await res.json();
      if (payload?.error?.message) {
        errMessage = payload.error.message;
      }
    } catch (err) {
      // ignore parse errors
    }
    throw new Error(errMessage);
  }

  const payload = await res.json();
  const names = (payload.voices || [])
    .map((v) => v.name)
    .filter((name) => typeof name === 'string' && name.startsWith('ja-JP-'))
    .sort((a, b) => scoreCloudVoiceName(b) - scoreCloudVoiceName(a));

  return names;
}

async function refreshCloudVoiceOptions(apiKey) {
  const current = voiceSelect.value;
  const names = await fetchCloudVoiceNames(apiKey);
  if (!names.length) return;
  populateVoiceSelect(names, current);
}

async function requestCloudSynthesis(apiKey, text, voiceName) {
  const body = {
    input: { text },
    voice: { languageCode: 'ja-JP' },
    audioConfig: {
      audioEncoding: 'MP3',
      speakingRate: 0.95,
      pitch: 0,
    },
  };

  if (voiceName) {
    body.voice.name = voiceName;
  }

  const res = await fetch(`${CLOUD_TTS_API_URL}?key=${encodeURIComponent(apiKey)}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
    signal: ttsRequestController.signal,
  });

  if (!res.ok) {
    let errMessage = `Cloud TTS 失败 (${res.status})`;
    try {
      const payload = await res.json();
      if (payload?.error?.message) {
        errMessage = payload.error.message;
      }
    } catch (err) {
      // ignore parse errors
    }
    const error = new Error(errMessage);
    error.status = res.status;
    throw error;
  }

  const payload = await res.json();
  if (!payload.audioContent) {
    throw new Error('Cloud TTS 未返回音频数据');
  }

  const bytes = base64ToBytes(payload.audioContent);
  return new Blob([bytes], { type: 'audio/mpeg' });
}

async function speakWithCloudTts(text, apiKey) {
  const selectedVoice = voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE;
  const cacheKey = `${selectedVoice}::${text}`;

  if (audioCache.has(cacheKey)) {
    await playAudioUrl(audioCache.get(cacheKey));
    setTtsStatus(`语音：Cloud TTS ${selectedVoice}（缓存）`);
    return;
  }

  if (ttsRequestController) {
    ttsRequestController.abort();
  }
  ttsRequestController = new AbortController();

  setTtsStatus('语音：Cloud TTS 生成中...');

  let audioBlob;
  let usedVoice = selectedVoice;
  try {
    audioBlob = await requestCloudSynthesis(apiKey, text, selectedVoice);
  } catch (err) {
    if (err.status === 400 && selectedVoice) {
      audioBlob = await requestCloudSynthesis(apiKey, text, '');
      usedVoice = 'ja-JP (auto)';
    } else {
      throw err;
    }
  }

  const url = URL.createObjectURL(audioBlob);
  putAudioCache(cacheKey, url);

  await playAudioUrl(url);
  setTtsStatus(`语音：Cloud TTS ${usedVoice}`);
}

function speakWithBrowser(text, reason = CLOUD_TTS_FALLBACK_STATUS) {
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

  const apiKey = getCloudTtsKey();
  if (!apiKey) {
    speakWithBrowser(text, CLOUD_TTS_FALLBACK_STATUS);
    return;
  }

  try {
    await speakWithCloudTts(text, apiKey);
  } catch (err) {
    if (err.name === 'AbortError') {
      return;
    }
    console.error(err);
    speakWithBrowser(text, `语音：Cloud TTS失败，已回退 (${err.message})`);
  }
}

function render() {
  if (!selectedSourceIds.length) {
    countEl.textContent = '0/0';
    listEl.innerHTML = '';
    const placeholder = document.createElement('div');
    placeholder.className = 'batch-marker';
    placeholder.textContent = '请先选择至少一个文件。';
    listEl.appendChild(placeholder);
    scrollSentinel.style.display = 'none';
    return;
  }

  const filtered = getFilteredWords(getCombinedItems());
  const visibleCount = Math.min(filtered.length, renderPage * PAGE_SIZE);
  const visible = filtered.slice(0, visibleCount);

  countEl.textContent = `${visibleCount}/${filtered.length}`;
  listEl.innerHTML = '';

  const fragment = document.createDocumentFragment();
  visible.forEach((w, index) => {
    const serial = index + 1;
    if ((serial - 1) % BATCH_MARK_INTERVAL === 0) {
      const marker = document.createElement('div');
      const start = serial;
      const end = Math.min(serial + BATCH_MARK_INTERVAL - 1, filtered.length);
      const group = Math.floor((serial - 1) / BATCH_MARK_INTERVAL) + 1;
      marker.className = 'batch-marker';
      marker.textContent = `序号 ${group} · ${start}-${end}`;
      fragment.appendChild(marker);
    }

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
  const hasMoreSourcePages = hasAnyMoreSourcePages();
  scrollSentinel.style.display = hasMoreRendered || hasMoreSourcePages ? 'block' : 'none';
}

function resetAndRender() {
  renderPage = 1;
  render();
}

async function onSourceChange() {
  setSelectedSourceIds(getSelectedSourceIdsFromControl());
  renderPage = 1;

  if (selectedSourceIds.length) {
    await loadSelectedUntil(1);
  }
  render();

  if (searchInput.value.trim()) {
    await loadAllForSearchSelected();
  }
}

async function autoLoadNextPage() {
  if (autoLoading || !selectedSourceIds.length) return;

  const filtered = getFilteredWords(getCombinedItems());
  const visibleCount = Math.min(filtered.length, renderPage * PAGE_SIZE);
  const hasMoreRendered = visibleCount < filtered.length;
  const hasMoreSourcePages = hasAnyMoreSourcePages();
  if (!hasMoreRendered && !hasMoreSourcePages) return;

  autoLoading = true;
  try {
    if (hasMoreRendered) {
      renderPage += 1;
    } else {
      const nextMeta = getSelectedMetas().find((meta) => {
        const state = getState(meta.id);
        return state.loadedPages < meta.pages;
      });
      if (nextMeta) {
        const nextState = getState(nextMeta.id);
        await loadUntil(nextMeta.id, nextState.loadedPages + 1);
        renderPage += 1;
      }
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
    const option = document.createElement('label');
    option.className = 'source-option';

    const text = document.createElement('span');
    text.className = 'source-option-text';
    text.textContent = `${meta.label} (${meta.count})`;

    const input = document.createElement('input');
    input.className = 'source-option-input';
    input.type = 'checkbox';
    input.value = meta.id;

    const mark = document.createElement('span');
    mark.className = 'source-option-mark';
    mark.textContent = '✓';
    mark.setAttribute('aria-hidden', 'true');

    option.appendChild(text);
    option.appendChild(input);
    option.appendChild(mark);
    sourceFilter.appendChild(option);
  });
}

function initKeyAndVoice() {
  if (!voiceSelect.value) {
    voiceSelect.value = CLOUD_TTS_DEFAULT_VOICE;
  }

  const savedKey = localStorage.getItem(CLOUD_TTS_KEY_STORAGE_KEY) || '';
  if (savedKey) {
    cloudTtsKeyInput.value = savedKey;
  }

  cloudTtsKeyInput.addEventListener('input', () => {
    saveCloudTtsKey();
    if (getCloudTtsKey()) {
      setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    } else {
      setTtsStatus(CLOUD_TTS_FALLBACK_STATUS);
    }
  });

  cloudTtsKeyInput.addEventListener('change', async () => {
    const apiKey = getCloudTtsKey();
    saveCloudTtsKey();
    if (!apiKey) {
      setTtsStatus(CLOUD_TTS_FALLBACK_STATUS);
      return;
    }

    setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    try {
      await refreshCloudVoiceOptions(apiKey);
      setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    } catch (err) {
      console.warn(err.message);
    }
  });

  voiceSelect.addEventListener('change', () => {
    if (getCloudTtsKey()) {
      setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    }
  });
}

async function init() {
  furiganaStatus.textContent = '假名模式：预生成（稳定）';
  setTtsStatus(CLOUD_TTS_FALLBACK_STATUS);

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
  selectAllSources();
  renderPage = 1;
  await loadSelectedUntil(1);
  render();
  setupInfiniteScroll();
  initKeyAndVoice();
  refreshBestBrowserVoice();

  if ('speechSynthesis' in window && 'onvoiceschanged' in window.speechSynthesis) {
    window.speechSynthesis.onvoiceschanged = () => {
      refreshBestBrowserVoice();
    };
  }

  const apiKey = getCloudTtsKey();
  if (apiKey) {
    setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    try {
      await refreshCloudVoiceOptions(apiKey);
      setTtsStatus(`语音：Cloud TTS ${voiceSelect.value || CLOUD_TTS_DEFAULT_VOICE}`);
    } catch (err) {
      console.warn(err.message);
    }
  }
}

searchInput.addEventListener('input', () => {
  resetAndRender();
  if (searchTimer) {
    clearTimeout(searchTimer);
  }
  searchTimer = setTimeout(() => {
    if (searchInput.value.trim()) {
      loadAllForSearchSelected().catch((err) => {
        console.error(err);
      });
    }
  }, SEARCH_DEBOUNCE_MS);
});

sourceFilter.addEventListener('change', () => {
  onSourceChange().catch((err) => {
    console.error(err);
    furiganaStatus.textContent = `切换来源失败：${err.message}`;
  });
});

if (selectAllSourcesBtn) {
  selectAllSourcesBtn.addEventListener('click', () => {
    selectAllSources();
    onSourceChange().catch((err) => {
      console.error(err);
      furiganaStatus.textContent = `切换来源失败：${err.message}`;
    });
  });
}

if (clearSourcesBtn) {
  clearSourcesBtn.addEventListener('click', () => {
    getSourceOptionInputs().forEach((input) => {
      input.checked = false;
    });
    onSourceChange().catch((err) => {
      console.error(err);
      furiganaStatus.textContent = `切换来源失败：${err.message}`;
    });
  });
}

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
