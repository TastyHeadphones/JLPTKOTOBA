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
const phoneticGroupsEl = document.getElementById('phoneticGroups');

const PAGE_SIZE = 80;
const BATCH_MARK_INTERVAL = 200;
const SEARCH_DEBOUNCE_MS = 250;

const CLOUD_TTS_API_URL = 'https://texttospeech.googleapis.com/v1/text:synthesize';
const CLOUD_TTS_VOICES_URL = 'https://texttospeech.googleapis.com/v1/voices';
const CLOUD_TTS_KEY_STORAGE_KEY = 'cloud_tts_api_key_persist';
const CLOUD_TTS_FALLBACK_STATUS = '语音：浏览器回退（未配置 Cloud TTS Key）';
const CLOUD_TTS_DEFAULT_VOICE = 'ja-JP-Chirp3-HD-Iapetus';
const MAX_AUDIO_CACHE = 16;

const PHONETIC_GROUPS = [
  {
    title: '五十音（清音）',
    items: [
      { kana: 'あ / ア', romaji: 'a', speak: 'あ' },
      { kana: 'い / イ', romaji: 'i', speak: 'い' },
      { kana: 'う / ウ', romaji: 'u', speak: 'う' },
      { kana: 'え / エ', romaji: 'e', speak: 'え' },
      { kana: 'お / オ', romaji: 'o', speak: 'お' },
      { kana: 'か / カ', romaji: 'ka', speak: 'か' },
      { kana: 'き / キ', romaji: 'ki', speak: 'き' },
      { kana: 'く / ク', romaji: 'ku', speak: 'く' },
      { kana: 'け / ケ', romaji: 'ke', speak: 'け' },
      { kana: 'こ / コ', romaji: 'ko', speak: 'こ' },
      { kana: 'さ / サ', romaji: 'sa', speak: 'さ' },
      { kana: 'し / シ', romaji: 'shi', speak: 'し' },
      { kana: 'す / ス', romaji: 'su', speak: 'す' },
      { kana: 'せ / セ', romaji: 'se', speak: 'せ' },
      { kana: 'そ / ソ', romaji: 'so', speak: 'そ' },
      { kana: 'た / タ', romaji: 'ta', speak: 'た' },
      { kana: 'ち / チ', romaji: 'chi', speak: 'ち' },
      { kana: 'つ / ツ', romaji: 'tsu', speak: 'つ' },
      { kana: 'て / テ', romaji: 'te', speak: 'て' },
      { kana: 'と / ト', romaji: 'to', speak: 'と' },
      { kana: 'な / ナ', romaji: 'na', speak: 'な' },
      { kana: 'に / ニ', romaji: 'ni', speak: 'に' },
      { kana: 'ぬ / ヌ', romaji: 'nu', speak: 'ぬ' },
      { kana: 'ね / ネ', romaji: 'ne', speak: 'ね' },
      { kana: 'の / ノ', romaji: 'no', speak: 'の' },
      { kana: 'は / ハ', romaji: 'ha', speak: 'は' },
      { kana: 'ひ / ヒ', romaji: 'hi', speak: 'ひ' },
      { kana: 'ふ / フ', romaji: 'fu', speak: 'ふ' },
      { kana: 'へ / ヘ', romaji: 'he', speak: 'へ' },
      { kana: 'ほ / ホ', romaji: 'ho', speak: 'ほ' },
      { kana: 'ま / マ', romaji: 'ma', speak: 'ま' },
      { kana: 'み / ミ', romaji: 'mi', speak: 'み' },
      { kana: 'む / ム', romaji: 'mu', speak: 'む' },
      { kana: 'め / メ', romaji: 'me', speak: 'め' },
      { kana: 'も / モ', romaji: 'mo', speak: 'も' },
      { kana: 'や / ヤ', romaji: 'ya', speak: 'や' },
      { kana: 'ゆ / ユ', romaji: 'yu', speak: 'ゆ' },
      { kana: 'よ / ヨ', romaji: 'yo', speak: 'よ' },
      { kana: 'ら / ラ', romaji: 'ra', speak: 'ら' },
      { kana: 'り / リ', romaji: 'ri', speak: 'り' },
      { kana: 'る / ル', romaji: 'ru', speak: 'る' },
      { kana: 'れ / レ', romaji: 're', speak: 'れ' },
      { kana: 'ろ / ロ', romaji: 'ro', speak: 'ろ' },
      { kana: 'わ / ワ', romaji: 'wa', speak: 'わ' },
      { kana: 'を / ヲ', romaji: 'wo', speak: 'を' },
      { kana: 'ん / ン', romaji: 'n', speak: 'ん' },
    ],
  },
  {
    title: '浊音 / 半浊音',
    items: [
      { kana: 'が / ガ', romaji: 'ga', speak: 'が' },
      { kana: 'ぎ / ギ', romaji: 'gi', speak: 'ぎ' },
      { kana: 'ぐ / グ', romaji: 'gu', speak: 'ぐ' },
      { kana: 'げ / ゲ', romaji: 'ge', speak: 'げ' },
      { kana: 'ご / ゴ', romaji: 'go', speak: 'ご' },
      { kana: 'ざ / ザ', romaji: 'za', speak: 'ざ' },
      { kana: 'じ / ジ', romaji: 'ji', speak: 'じ' },
      { kana: 'ず / ズ', romaji: 'zu', speak: 'ず' },
      { kana: 'ぜ / ゼ', romaji: 'ze', speak: 'ぜ' },
      { kana: 'ぞ / ゾ', romaji: 'zo', speak: 'ぞ' },
      { kana: 'だ / ダ', romaji: 'da', speak: 'だ' },
      { kana: 'ぢ / ヂ', romaji: 'ji (di)', speak: 'ぢ' },
      { kana: 'づ / ヅ', romaji: 'zu (du)', speak: 'づ' },
      { kana: 'で / デ', romaji: 'de', speak: 'で' },
      { kana: 'ど / ド', romaji: 'do', speak: 'ど' },
      { kana: 'ば / バ', romaji: 'ba', speak: 'ば' },
      { kana: 'び / ビ', romaji: 'bi', speak: 'び' },
      { kana: 'ぶ / ブ', romaji: 'bu', speak: 'ぶ' },
      { kana: 'べ / ベ', romaji: 'be', speak: 'べ' },
      { kana: 'ぼ / ボ', romaji: 'bo', speak: 'ぼ' },
      { kana: 'ぱ / パ', romaji: 'pa', speak: 'ぱ' },
      { kana: 'ぴ / ピ', romaji: 'pi', speak: 'ぴ' },
      { kana: 'ぷ / プ', romaji: 'pu', speak: 'ぷ' },
      { kana: 'ぺ / ペ', romaji: 'pe', speak: 'ぺ' },
      { kana: 'ぽ / ポ', romaji: 'po', speak: 'ぽ' },
    ],
  },
  {
    title: '拗音（清音）',
    items: [
      { kana: 'きゃ / キャ', romaji: 'kya', speak: 'きゃ' },
      { kana: 'きゅ / キュ', romaji: 'kyu', speak: 'きゅ' },
      { kana: 'きょ / キョ', romaji: 'kyo', speak: 'きょ' },
      { kana: 'しゃ / シャ', romaji: 'sha', speak: 'しゃ' },
      { kana: 'しゅ / シュ', romaji: 'shu', speak: 'しゅ' },
      { kana: 'しょ / ショ', romaji: 'sho', speak: 'しょ' },
      { kana: 'ちゃ / チャ', romaji: 'cha', speak: 'ちゃ' },
      { kana: 'ちゅ / チュ', romaji: 'chu', speak: 'ちゅ' },
      { kana: 'ちょ / チョ', romaji: 'cho', speak: 'ちょ' },
      { kana: 'にゃ / ニャ', romaji: 'nya', speak: 'にゃ' },
      { kana: 'にゅ / ニュ', romaji: 'nyu', speak: 'にゅ' },
      { kana: 'にょ / ニョ', romaji: 'nyo', speak: 'にょ' },
      { kana: 'ひゃ / ヒャ', romaji: 'hya', speak: 'ひゃ' },
      { kana: 'ひゅ / ヒュ', romaji: 'hyu', speak: 'ひゅ' },
      { kana: 'ひょ / ヒョ', romaji: 'hyo', speak: 'ひょ' },
      { kana: 'みゃ / ミャ', romaji: 'mya', speak: 'みゃ' },
      { kana: 'みゅ / ミュ', romaji: 'myu', speak: 'みゅ' },
      { kana: 'みょ / ミョ', romaji: 'myo', speak: 'みょ' },
      { kana: 'りゃ / リャ', romaji: 'rya', speak: 'りゃ' },
      { kana: 'りゅ / リュ', romaji: 'ryu', speak: 'りゅ' },
      { kana: 'りょ / リョ', romaji: 'ryo', speak: 'りょ' },
    ],
  },
  {
    title: '拗音（浊音 / 半浊音）',
    items: [
      { kana: 'ぎゃ / ギャ', romaji: 'gya', speak: 'ぎゃ' },
      { kana: 'ぎゅ / ギュ', romaji: 'gyu', speak: 'ぎゅ' },
      { kana: 'ぎょ / ギョ', romaji: 'gyo', speak: 'ぎょ' },
      { kana: 'じゃ / ジャ', romaji: 'ja', speak: 'じゃ' },
      { kana: 'じゅ / ジュ', romaji: 'ju', speak: 'じゅ' },
      { kana: 'じょ / ジョ', romaji: 'jo', speak: 'じょ' },
      { kana: 'ぢゃ / ヂャ', romaji: 'ja (dya)', speak: 'ぢゃ' },
      { kana: 'ぢゅ / ヂュ', romaji: 'ju (dyu)', speak: 'ぢゅ' },
      { kana: 'ぢょ / ヂョ', romaji: 'jo (dyo)', speak: 'ぢょ' },
      { kana: 'びゃ / ビャ', romaji: 'bya', speak: 'びゃ' },
      { kana: 'びゅ / ビュ', romaji: 'byu', speak: 'びゅ' },
      { kana: 'びょ / ビョ', romaji: 'byo', speak: 'びょ' },
      { kana: 'ぴゃ / ピャ', romaji: 'pya', speak: 'ぴゃ' },
      { kana: 'ぴゅ / ピュ', romaji: 'pyu', speak: 'ぴゅ' },
      { kana: 'ぴょ / ピョ', romaji: 'pyo', speak: 'ぴょ' },
    ],
  },
  {
    title: '外来音（扩展音）',
    items: [
      { kana: 'ファ', romaji: 'fa', speak: 'ファ' },
      { kana: 'フィ', romaji: 'fi', speak: 'フィ' },
      { kana: 'フェ', romaji: 'fe', speak: 'フェ' },
      { kana: 'フォ', romaji: 'fo', speak: 'フォ' },
      { kana: 'フュ', romaji: 'fyu', speak: 'フュ' },
      { kana: 'ティ', romaji: 'ti', speak: 'ティ' },
      { kana: 'トゥ', romaji: 'tu', speak: 'トゥ' },
      { kana: 'ディ', romaji: 'di', speak: 'ディ' },
      { kana: 'ドゥ', romaji: 'du', speak: 'ドゥ' },
      { kana: 'ウィ', romaji: 'wi', speak: 'ウィ' },
      { kana: 'ウェ', romaji: 'we', speak: 'ウェ' },
      { kana: 'ウォ', romaji: 'wo', speak: 'ウォ' },
      { kana: 'ヴァ', romaji: 'va', speak: 'ヴァ' },
      { kana: 'ヴィ', romaji: 'vi', speak: 'ヴィ' },
      { kana: 'ヴ', romaji: 'vu', speak: 'ヴ' },
      { kana: 'ヴェ', romaji: 've', speak: 'ヴェ' },
      { kana: 'ヴォ', romaji: 'vo', speak: 'ヴォ' },
      { kana: 'ヴュ', romaji: 'vyu', speak: 'ヴュ' },
      { kana: 'ツァ', romaji: 'tsa', speak: 'ツァ' },
      { kana: 'ツィ', romaji: 'tsi', speak: 'ツィ' },
      { kana: 'ツェ', romaji: 'tse', speak: 'ツェ' },
      { kana: 'ツォ', romaji: 'tso', speak: 'ツォ' },
      { kana: 'シェ', romaji: 'she', speak: 'シェ' },
      { kana: 'ジェ', romaji: 'je', speak: 'ジェ' },
      { kana: 'チェ', romaji: 'che', speak: 'チェ' },
      { kana: 'スィ', romaji: 'si', speak: 'スィ' },
      { kana: 'ズィ', romaji: 'zi', speak: 'ズィ' },
      { kana: 'イェ', romaji: 'ye', speak: 'イェ' },
      { kana: 'キェ', romaji: 'kye', speak: 'キェ' },
      { kana: 'ギェ', romaji: 'gye', speak: 'ギェ' },
      { kana: 'ニェ', romaji: 'nye', speak: 'ニェ' },
      { kana: 'ヒェ', romaji: 'hye', speak: 'ヒェ' },
      { kana: 'ビェ', romaji: 'bye', speak: 'ビェ' },
      { kana: 'ピェ', romaji: 'pye', speak: 'ピェ' },
      { kana: 'ミェ', romaji: 'mye', speak: 'ミェ' },
      { kana: 'リェ', romaji: 'rye', speak: 'リェ' },
      { kana: 'クァ', romaji: 'kwa', speak: 'クァ' },
      { kana: 'クィ', romaji: 'kwi', speak: 'クィ' },
      { kana: 'クェ', romaji: 'kwe', speak: 'クェ' },
      { kana: 'クォ', romaji: 'kwo', speak: 'クォ' },
      { kana: 'グァ', romaji: 'gwa', speak: 'グァ' },
      { kana: 'グィ', romaji: 'gwi', speak: 'グィ' },
      { kana: 'グェ', romaji: 'gwe', speak: 'グェ' },
      { kana: 'グォ', romaji: 'gwo', speak: 'グォ' },
      { kana: 'テュ', romaji: 'tyu', speak: 'テュ' },
      { kana: 'デュ', romaji: 'dyu', speak: 'デュ' },
    ],
  },
  {
    title: '特殊音 / 长音',
    items: [
      { kana: 'っ / ッ', romaji: 'sokuon (停顿)', speak: 'っ' },
      { kana: 'ー', romaji: 'chouon (长音符)', speak: 'ー' },
      { kana: 'ぁ ぃ ぅ ぇ ぉ', romaji: 'small vowels', speak: 'ぁぃぅぇぉ' },
      { kana: 'ゃ ゅ ょ', romaji: 'small ya yu yo', speak: 'ゃゅょ' },
      { kana: 'ゎ', romaji: 'small wa', speak: 'ゎ' },
      { kana: 'ゐ / ヰ', romaji: 'wi (旧假名)', speak: 'ゐ' },
      { kana: 'ゑ / ヱ', romaji: 'we (旧假名)', speak: 'ゑ' },
      { kana: 'ああ', romaji: 'aa', speak: 'ああ' },
      { kana: 'いい', romaji: 'ii', speak: 'いい' },
      { kana: 'うう', romaji: 'uu', speak: 'うう' },
      { kana: 'えい', romaji: 'ei', speak: 'えい' },
      { kana: 'おう', romaji: 'ou', speak: 'おう' },
      { kana: 'おお', romaji: 'oo', speak: 'おお' },
      { kana: 'カー', romaji: 'kaa', speak: 'カー' },
      { kana: 'キー', romaji: 'kii', speak: 'キー' },
      { kana: 'クー', romaji: 'kuu', speak: 'クー' },
      { kana: 'ケー', romaji: 'kee', speak: 'ケー' },
      { kana: 'コー', romaji: 'koo', speak: 'コー' },
    ],
  },
];

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

function getSelectedSourceIdsFromControl() {
  return Array.from(sourceFilter.selectedOptions).map((opt) => opt.value);
}

function setSelectedSourceIds(ids) {
  selectedSourceIds = sourceMeta
    .map((meta) => meta.id)
    .filter((id) => ids.includes(id));
}

function selectAllSources() {
  Array.from(sourceFilter.options).forEach((opt) => {
    opt.selected = true;
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

function renderPhoneticGroups() {
  if (!phoneticGroupsEl) return;
  phoneticGroupsEl.innerHTML = '';

  const fragment = document.createDocumentFragment();
  PHONETIC_GROUPS.forEach((group) => {
    const card = document.createElement('article');
    card.className = 'phonetic-group';

    const title = document.createElement('h3');
    title.textContent = group.title;
    card.appendChild(title);

    const items = document.createElement('div');
    items.className = 'phonetic-items';

    group.items.forEach((item) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'phonetic-btn';
      btn.dataset.speak = item.speak || item.kana;

      const kana = document.createElement('span');
      kana.className = 'phonetic-kana';
      kana.textContent = item.kana;

      const romaji = document.createElement('span');
      romaji.className = 'phonetic-romaji';
      romaji.textContent = item.romaji;

      btn.appendChild(kana);
      btn.appendChild(romaji);
      items.appendChild(btn);
    });

    card.appendChild(items);
    fragment.appendChild(card);
  });

  phoneticGroupsEl.appendChild(fragment);
}

function setupPhoneticClicks() {
  if (!phoneticGroupsEl) return;
  phoneticGroupsEl.addEventListener('click', (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;
    const btn = target.closest('.phonetic-btn');
    if (!(btn instanceof HTMLButtonElement)) return;
    const text = btn.dataset.speak || '';
    if (!text) return;
    speak(text);
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
  sourceFilter.multiple = true;
  sourceFilter.size = Math.min(8, Math.max(4, sourceMeta.length));
  sourceMeta.forEach((meta) => {
    const opt = document.createElement('option');
    opt.value = meta.id;
    opt.textContent = `${meta.label} (${meta.count})`;
    sourceFilter.appendChild(opt);
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
  renderPhoneticGroups();
  setupPhoneticClicks();

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
    Array.from(sourceFilter.options).forEach((opt) => {
      opt.selected = false;
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
