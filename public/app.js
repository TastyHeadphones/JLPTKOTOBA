const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const loadMoreBtn = document.getElementById('loadMoreBtn');
const furiganaStatus = document.getElementById('furiganaStatus');

const PAGE_SIZE = 80;

let words = [];
let currentPage = 1;

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

function setJapaneseContent(el, plain, rubyHtml) {
  if (furiganaToggle.checked && rubyHtml) {
    el.innerHTML = rubyHtml;
  } else {
    el.textContent = plain || '';
  }
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

    setJapaneseContent(termBtn, w.term || '', w.term_ruby || '');
    termBtn.addEventListener('click', () => speak(w.term || ''));

    setJapaneseContent(exampleBtn, w.example || '', w.example_ruby || '');
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

function init() {
  furiganaStatus.textContent = '假名模式：使用预生成数据（稳定）';

  fetch('words.json')
    .then((res) => res.json())
    .then((data) => {
      words = data;
      initSources();
      render();
    })
    .catch((err) => {
      furiganaStatus.textContent = `数据加载失败：${err.message}`;
    });
}

searchInput.addEventListener('input', resetAndRender);
sourceFilter.addEventListener('change', resetAndRender);
furiganaToggle.addEventListener('change', render);
loadMoreBtn.addEventListener('click', () => {
  currentPage += 1;
  render();
});

init();
