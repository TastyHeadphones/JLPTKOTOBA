const listEl = document.getElementById('list');
const template = document.getElementById('cardTemplate');
const searchInput = document.getElementById('searchInput');
const sourceFilter = document.getElementById('sourceFilter');
const countEl = document.getElementById('count');
const furiganaToggle = document.getElementById('furiganaToggle');
const loadMoreBtn = document.getElementById('loadMoreBtn');
const furiganaStatus = document.getElementById('furiganaStatus');

const PAGE_SIZE = 80;
const SEARCH_DEBOUNCE_MS = 250;

let sourceMeta = [];
let currentSourceId = '';
const sourceState = new Map();
let searchTimer = null;

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

function setJapaneseContent(el, plain, rubyHtml) {
  if (furiganaToggle.checked && rubyHtml) {
    el.innerHTML = rubyHtml;
  } else {
    el.textContent = plain || '';
  }
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
    termBtn.addEventListener('click', () => speak(w.term || ''));

    setJapaneseContent(exampleBtn, w.example || '', w.example_ruby || '');
    exampleBtn.addEventListener('click', () => speak(w.example || ''));

    badge.textContent = (w.source || '').replace('wordlist.pdf', '');
    zh.textContent = w.zh || '—';
    en.textContent = w.en || '—';

    fragment.appendChild(node);
  });

  listEl.appendChild(fragment);

  const hasMoreRendered = visibleCount < filtered.length;
  const hasMoreSourcePages = !!meta && state.loadedPages < meta.pages;
  loadMoreBtn.hidden = !hasMoreRendered && !hasMoreSourcePages;
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

async function onLoadMore() {
  const meta = getMeta(currentSourceId);
  const state = getState(currentSourceId);
  if (!meta) return;

  state.renderPage += 1;
  const needVisible = state.renderPage * PAGE_SIZE;
  const filteredCount = getFilteredWords(state.items).length;
  if (filteredCount < needVisible && state.loadedPages < meta.pages) {
    await loadUntil(currentSourceId, state.loadedPages + 1);
  }
  render();
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

async function init() {
  furiganaStatus.textContent = '假名模式：预生成（稳定）';

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
}

searchInput.addEventListener('input', () => {
  resetAndRender();
  if (searchTimer) {
    clearTimeout(searchTimer);
  }
  searchTimer = setTimeout(() => {
    loadAllForSearch(currentSourceId);
  }, SEARCH_DEBOUNCE_MS);
});

sourceFilter.addEventListener('change', () => {
  onSourceChange();
});

furiganaToggle.addEventListener('change', render);
loadMoreBtn.addEventListener('click', () => {
  onLoadMore();
});

init().catch((err) => {
  console.error(err);
  furiganaStatus.textContent = `初始化失败：${err.message}`;
});
