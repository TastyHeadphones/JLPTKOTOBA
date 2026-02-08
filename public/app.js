const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const loadMoreBtn = document.getElementById('loadMoreBtn');
const furiganaStatus = document.getElementById('furiganaStatus');

const PAGE_SIZE = 120;
const KUROMOJI_SCRIPT_URLS = [
  'https://cdn.jsdelivr.net/npm/kuromoji@0.1.2/build/kuromoji.js',
  'https://unpkg.com/kuromoji@0.1.2/build/kuromoji.js'
];
const KUROMOJI_DICT_PATHS = [
  'https://cdn.jsdelivr.net/npm/kuromoji@0.1.2/dict/',
  'https://unpkg.com/kuromoji@0.1.2/dict/'
];

let words = [];
let tokenizer = null;
let currentPage = 1;
const rubyCache = new Map();

function hasKanji(text) {
  return /[\u4e00-\u9faf]/.test(text);
}

function kataToHira(str) {
  return str.replace(/[\u30a1-\u30f6]/g, (ch) => String.fromCharCode(ch.charCodeAt(0) - 0x60));
}

function toRuby(text) {
  if (!tokenizer || !furiganaToggle.checked) return text;
  const cacheKey = `${text}::${furiganaToggle.checked}`;
  if (rubyCache.has(cacheKey)) return rubyCache.get(cacheKey);

  const tokens = tokenizer.tokenize(text);
  const html = tokens.map((tok) => {
    if (!tok.reading || !hasKanji(tok.surface_form)) {
      return tok.surface_form;
    }
    const reading = kataToHira(tok.reading);
    return `<ruby>${tok.surface_form}<rt>${reading}</rt></ruby>`;
  }).join('');

  rubyCache.set(cacheKey, html);
  return html;
}

function speak(text) {
  if (!('speechSynthesis' in window)) {
    alert('浏览器不支持 TTS');
    return;
  }
  window.speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'ja-JP';
  window.speechSynthesis.speak(utter);
}

function getFilteredWords() {
  const q = searchInput.value.trim().toLowerCase();
  const source = sourceFilter.value;

  return words.filter((w) => {
    const matchesSource = source === 'all' || w.source === source;
    if (!matchesSource) return false;
    if (!q) return true;

    const term = (w.term || '').toLowerCase();
    const zh = (w.zh || '').toLowerCase();
    const en = (w.en || '').toLowerCase();
    const example = (w.example || '').toLowerCase();
    return term.includes(q) || zh.includes(q) || en.includes(q) || example.includes(q);
  });
}

function render() {
  const filtered = getFilteredWords();
  const visibleCount = Math.min(filtered.length, currentPage * PAGE_SIZE);
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

    termBtn.innerHTML = toRuby(w.term || '');
    termBtn.addEventListener('click', () => speak(w.term || ''));

    exampleBtn.innerHTML = toRuby(w.example || '');
    exampleBtn.addEventListener('click', () => speak(w.example || ''));

    badge.textContent = (w.source || '').replace('wordlist.pdf', '');
    zh.textContent = w.zh || '—';
    en.textContent = w.en || '—';

    fragment.appendChild(node);
  });

  listEl.appendChild(fragment);
  loadMoreBtn.hidden = visibleCount >= filtered.length;
}

function initSources() {
  const sources = Array.from(new Set(words.map((w) => w.source))).sort();
  sources.forEach((src) => {
    const opt = document.createElement('option');
    opt.value = src;
    opt.textContent = src.replace('wordlist.pdf', '');
    sourceFilter.appendChild(opt);
  });
}

function resetAndRender() {
  currentPage = 1;
  render();
}

function loadScript(url) {
  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = url;
    script.async = true;
    script.onload = () => resolve(url);
    script.onerror = () => reject(new Error(`script load failed: ${url}`));
    document.head.appendChild(script);
  });
}

async function ensureKuromojiLoaded() {
  if (typeof kuromoji !== 'undefined') return true;

  for (const url of KUROMOJI_SCRIPT_URLS) {
    try {
      await loadScript(url);
      if (typeof kuromoji !== 'undefined') return true;
    } catch (err) {
      console.warn(err.message);
    }
  }
  return false;
}

function buildTokenizer(dicPath) {
  return new Promise((resolve, reject) => {
    kuromoji.builder({ dicPath }).build((err, tok) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(tok);
    });
  });
}

async function initFurigana() {
  furiganaStatus.textContent = '假名加载中...';

  const loaded = await ensureKuromojiLoaded();
  if (!loaded) {
    furiganaStatus.textContent = '假名加载失败：库文件不可用';
    return;
  }

  for (const dicPath of KUROMOJI_DICT_PATHS) {
    try {
      tokenizer = await buildTokenizer(dicPath);
      rubyCache.clear();
      furiganaStatus.textContent = '假名已启用';
      render();
      return;
    } catch (err) {
      console.warn(`dict failed: ${dicPath}`, err);
    }
  }

  furiganaStatus.textContent = '假名加载失败：词典不可用';
}

function init() {
  fetch('words.json')
    .then((res) => res.json())
    .then((data) => {
      words = data;
      initSources();
      render();
    });

  initFurigana();
}

searchInput.addEventListener('input', resetAndRender);
sourceFilter.addEventListener('change', resetAndRender);
furiganaToggle.addEventListener('change', () => {
  rubyCache.clear();
  render();
});
loadMoreBtn.addEventListener('click', () => {
  currentPage += 1;
  render();
});

init();
