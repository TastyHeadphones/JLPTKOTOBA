const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');

let words = [];
let tokenizer = null;
const rubyCache = new Map();
const translationCache = JSON.parse(localStorage.getItem('zhEnCache') || '{}');
const pendingTranslations = new Set();
const translationQueue = [];
let activeTranslations = 0;
const MAX_TRANSLATIONS = 3;

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

function saveTranslationCache() {
  localStorage.setItem('zhEnCache', JSON.stringify(translationCache));
}

function enqueueTranslation(zh, onDone) {
  if (!zh || pendingTranslations.has(zh)) return;
  pendingTranslations.add(zh);
  translationQueue.push({ zh, onDone });
  processTranslationQueue();
}

function processTranslationQueue() {
  if (activeTranslations >= MAX_TRANSLATIONS || translationQueue.length === 0) return;
  const job = translationQueue.shift();
  activeTranslations += 1;

  const url = `https://api.mymemory.translated.net/get?${new URLSearchParams({ q: job.zh, langpair: 'zh-CN|en' })}`;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      const translated = data?.responseData?.translatedText || '';
      if (translated) {
        translationCache[job.zh] = translated;
        saveTranslationCache();
      }
      job.onDone(translated);
    })
    .catch(() => job.onDone(''))
    .finally(() => {
      pendingTranslations.delete(job.zh);
      activeTranslations -= 1;
      processTranslationQueue();
    });
}

function render() {
  const q = searchInput.value.trim().toLowerCase();
  const source = sourceFilter.value;

  listEl.innerHTML = '';

  const filtered = words.filter((w) => {
    const matchesSource = source === 'all' || w.source === source;
    if (!matchesSource) return false;
    if (!q) return true;
    return (
      w.term.toLowerCase().includes(q) ||
      w.zh.toLowerCase().includes(q) ||
      w.en.toLowerCase().includes(q) ||
      w.example.toLowerCase().includes(q)
    );
  });

  countEl.textContent = filtered.length.toLocaleString();

  const fragment = document.createDocumentFragment();
  filtered.forEach((w) => {
    const node = template.content.cloneNode(true);
    const termBtn = node.querySelector('.speak.term');
    const exampleBtn = node.querySelector('.speak.example');
    const badge = node.querySelector('.badge');
    const zh = node.querySelector('.value.zh');
    const en = node.querySelector('.value.en');

    termBtn.innerHTML = toRuby(w.term);
    termBtn.addEventListener('click', () => speak(w.term));
    exampleBtn.innerHTML = toRuby(w.example);
    exampleBtn.addEventListener('click', () => speak(w.example));
    badge.textContent = w.source.replace('wordlist.pdf', '');
    zh.textContent = w.zh || '—';
    if (w.en) {
      en.textContent = w.en;
    } else if (w.zh && translationCache[w.zh]) {
      w.en = translationCache[w.zh];
      en.textContent = w.en;
    } else if (w.zh) {
      en.textContent = '翻译中...';
      enqueueTranslation(w.zh, (translated) => {
        if (translated) {
          w.en = translated;
          en.textContent = translated;
        } else {
          en.textContent = '—';
        }
      });
    } else {
      en.textContent = '—';
    }

    fragment.appendChild(node);
  });

  listEl.appendChild(fragment);
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

function init() {
  fetch('words.json')
    .then((res) => res.json())
    .then((data) => {
      words = data;
      initSources();
      render();
    });

  if (typeof kuromoji === 'undefined') {
    console.error('kuromoji is not loaded');
    return;
  }

  kuromoji.builder({ dicPath: 'https://cdn.jsdelivr.net/npm/kuromoji@0.1.2/dict/' })
    .build((err, tok) => {
      if (err) {
        console.error(err);
        return;
      }
      tokenizer = tok;
      rubyCache.clear();
      render();
    });
}

searchInput.addEventListener('input', render);
sourceFilter.addEventListener('change', render);
furiganaToggle.addEventListener('change', () => {
  rubyCache.clear();
  render();
});

init();
