const listEl = document.getElementById('kanjiList');
const cardTemplate = document.getElementById('kanjiCardTemplate');
const searchInput = document.getElementById('searchInput');
const sortModeSelect = document.getElementById('sortMode');
const sourceFilter = document.getElementById('sourceFilter');
const selectAllSourcesBtn = document.getElementById('selectAllSources');
const clearSourcesBtn = document.getElementById('clearSources');
const countEl = document.getElementById('count');
const totalEl = document.getElementById('total');
const scrollSentinel = document.getElementById('scrollSentinel');

const kanjiModal = document.getElementById('kanjiModal');
const closeModalBtn = document.getElementById('closeModal');
const modalChar = document.getElementById('kanjiModalChar');
const modalRank = document.getElementById('kanjiModalRank');
const modalCounts = document.getElementById('kanjiModalCounts');
const modalReadings = document.getElementById('kanjiModalReadings');
const modalWords = document.getElementById('kanjiModalWords');
const modalExample = document.getElementById('kanjiModalExample');
const modalSources = document.getElementById('kanjiModalSources');

const PAGE_SIZE = 80;
const BATCH_MARK_INTERVAL = 200;
const SEARCH_DEBOUNCE_MS = 250;
const SOURCE_FILTER_STORAGE_KEY = 'kanji_source_filter_selected_ids';
const SORT_MODE_STORAGE_KEY = 'kanji_sort_mode';

const SORT_MODE_KEY_MAP = {
  textbook: 'rank_textbook',
  school: 'rank_school',
  frequency: 'rank_frequency',
};

let meta = null;
let selectedSourceIds = [];
let loadedPages = 0;
let loadedItems = [];
let renderPage = 1;
let observer = null;
let autoLoading = false;
let searchTimer = null;
let loadingAllForSearch = false;
let visibleItemMap = new Map();

function setListMessage(text) {
  listEl.innerHTML = '';
  const marker = document.createElement('div');
  marker.className = 'batch-marker';
  marker.textContent = text;
  listEl.appendChild(marker);
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
  const validIds = (meta?.sources || []).map((s) => s.id);
  selectedSourceIds = validIds.filter((id) => ids.includes(id));
}

function saveSelectedSourceIds() {
  localStorage.setItem(SOURCE_FILTER_STORAGE_KEY, JSON.stringify(selectedSourceIds));
}

function getSortMode() {
  const mode = sortModeSelect?.value || 'textbook';
  return SORT_MODE_KEY_MAP[mode] ? mode : 'textbook';
}

function saveSortMode() {
  localStorage.setItem(SORT_MODE_STORAGE_KEY, getSortMode());
}

function loadSavedSortMode() {
  const raw = localStorage.getItem(SORT_MODE_STORAGE_KEY);
  if (!raw) return null;
  return SORT_MODE_KEY_MAP[raw] ? raw : null;
}

function getRankByMode(item) {
  const key = SORT_MODE_KEY_MAP[getSortMode()] || 'rank_textbook';
  return Number(item?.[key] || 0);
}

function getSortLabel() {
  const mode = getSortMode();
  if (mode === 'school') return '学年顺';
  if (mode === 'frequency') return '频次顺';
  return '教材顺';
}

function formatGrade(grade) {
  if (grade >= 1 && grade <= 6) return `小学${grade}年`;
  if (grade === 8) return '常用';
  if (grade === 9) return '人名';
  if (grade === 10) return '人名扩展';
  return '未分级';
}

function loadSavedSourceIds() {
  const raw = localStorage.getItem(SOURCE_FILTER_STORAGE_KEY);
  if (raw == null) return null;
  try {
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) return null;
    return parsed.filter((id) => typeof id === 'string');
  } catch (err) {
    console.warn('汉字来源筛选记忆读取失败:', err);
    return null;
  }
}

function applySourceSelection(ids) {
  const wanted = new Set(ids);
  getSourceOptionInputs().forEach((input) => {
    input.checked = wanted.has(input.value);
  });
  setSelectedSourceIds(getSelectedSourceIdsFromControl());
}

function selectAllSources() {
  getSourceOptionInputs().forEach((input) => {
    input.checked = true;
  });
  setSelectedSourceIds(getSelectedSourceIdsFromControl());
}

function initSourceFilter() {
  sourceFilter.innerHTML = '';
  (meta?.sources || []).forEach((src) => {
    const option = document.createElement('label');
    option.className = 'source-option';

    const text = document.createElement('span');
    text.className = 'source-option-text';
    text.textContent = `${src.label} (${src.count})`;

    const input = document.createElement('input');
    input.className = 'source-option-input';
    input.type = 'checkbox';
    input.value = src.id;

    option.appendChild(text);
    option.appendChild(input);
    sourceFilter.appendChild(option);
  });
}

async function fetchKanjiChunk(page) {
  const res = await fetch(`data/kanji_p${page}.json`);
  if (!res.ok) {
    throw new Error(`加载汉字分片失败: p${page}`);
  }
  return res.json();
}

async function loadUntil(targetPages) {
  if (!meta) return;
  while (loadedPages < targetPages && loadedPages < meta.pages) {
    const nextPage = loadedPages + 1;
    const chunk = await fetchKanjiChunk(nextPage);
    loadedItems.push(...chunk);
    loadedPages = nextPage;
  }
}

async function loadAllForSearch() {
  if (!meta || loadingAllForSearch || loadedPages >= meta.pages) return;
  loadingAllForSearch = true;
  try {
    await loadUntil(meta.pages);
    render();
  } finally {
    loadingAllForSearch = false;
  }
}

function getFilteredItems() {
  if (!selectedSourceIds.length) return [];

  const selected = new Set(selectedSourceIds);
  let items = loadedItems.filter((item) => (item.sources || []).some((src) => selected.has(src)));

  const q = searchInput.value.trim().toLowerCase();
  if (!q) return items;

  items = items.filter((item) => {
    if ((item.kanji || '').toLowerCase().includes(q)) return true;

    if ((item.readings || []).some((r) => (r || '').toLowerCase().includes(q))) {
      return true;
    }

    if ((item.words || []).some((w) => {
      const text = `${w.term || ''} ${w.zh || ''} ${w.en || ''}`.toLowerCase();
      return text.includes(q);
    })) {
      return true;
    }

    if ((item.examples || []).some((e) => ((e.example || '').toLowerCase().includes(q)))) {
      return true;
    }

    return false;
  });

  items.sort((a, b) => getRankByMode(a) - getRankByMode(b));
  return items;
}

function makeChip(text, cls = '') {
  const span = document.createElement('span');
  span.className = `chip${cls ? ` ${cls}` : ''}`;
  span.textContent = text;
  return span;
}

function render() {
  const filtered = getFilteredItems();
  const total = filtered.length;
  const visibleCount = Math.min(total, renderPage * PAGE_SIZE);
  const visible = filtered.slice(0, visibleCount);

  countEl.textContent = String(visibleCount);
  totalEl.textContent = String(total);

  if (!selectedSourceIds.length) {
    setListMessage('请先选择至少一个文件。');
    scrollSentinel.style.display = 'none';
    return;
  }

  if (!visible.length) {
    setListMessage('没有匹配的汉字。');
    const hasMorePages = !!meta && loadedPages < meta.pages;
    scrollSentinel.style.display = hasMorePages ? 'block' : 'none';
    return;
  }

  listEl.innerHTML = '';
  visibleItemMap = new Map();

  const fragment = document.createDocumentFragment();
  visible.forEach((item, index) => {
    const serial = index + 1;
    if ((serial - 1) % BATCH_MARK_INTERVAL === 0) {
      const marker = document.createElement('div');
      const start = serial;
      const end = Math.min(serial + BATCH_MARK_INTERVAL - 1, total);
      const group = Math.floor((serial - 1) / BATCH_MARK_INTERVAL) + 1;
      marker.className = 'batch-marker';
      marker.textContent = `序号 ${group} · ${start}-${end}`;
      fragment.appendChild(marker);
    }

    visibleItemMap.set(item.kanji, item);

    const node = cardTemplate.content.cloneNode(true);
    const kanjiChar = node.querySelector('.kanji-char');
    const rank = node.querySelector('.rank');
    const freq = node.querySelector('.freq');
    const counts = node.querySelector('.counts');
    const readings = node.querySelector('.readings');
    const sampleWords = node.querySelector('.sample-words');
    const sampleExample = node.querySelector('.sample-example');
    const sources = node.querySelector('.sources');

    kanjiChar.textContent = item.kanji;
    kanjiChar.dataset.kanji = item.kanji;

    rank.textContent = `${getSortLabel()} #${getRankByMode(item)}`;
    freq.textContent = `频次 ${item.frequency}`;
    counts.textContent = `词条 ${item.count_term} · 例句 ${item.count_example} · ${formatGrade(item.grade)}${item.stroke_count ? ` · ${item.stroke_count}画` : ''}`;

    (item.readings || []).forEach((reading) => {
      readings.appendChild(makeChip(reading, 'reading'));
    });

    (item.words || []).slice(0, 4).forEach((w) => {
      const label = w.zh ? `${w.term} · ${w.zh}` : (w.term || '');
      const chip = makeChip(label, 'word');
      if (w.en) {
        chip.title = w.en;
      }
      sampleWords.appendChild(chip);
    });

    const firstExample = (item.examples || [])[0]?.example || '';
    sampleExample.textContent = firstExample || '—';

    const srcList = item.sources || [];
    srcList.slice(0, 4).forEach((src) => {
      sources.appendChild(makeChip(src, 'source'));
    });
    if (srcList.length > 4) {
      sources.appendChild(makeChip(`+${srcList.length - 4}`, 'source'));
    }

    fragment.appendChild(node);
  });

  listEl.appendChild(fragment);

  const hasMoreRendered = visibleCount < total;
  const hasMorePages = !!meta && loadedPages < meta.pages;
  scrollSentinel.style.display = hasMoreRendered || hasMorePages ? 'block' : 'none';
}

function resetAndRender() {
  renderPage = 1;
  render();
}

async function onSourceChange() {
  setSelectedSourceIds(getSelectedSourceIdsFromControl());
  saveSelectedSourceIds();
  resetAndRender();

  if (searchInput.value.trim()) {
    await loadAllForSearch();
  }
}

async function autoLoadNextPage() {
  if (autoLoading || !meta || !selectedSourceIds.length) return;

  const filtered = getFilteredItems();
  const visibleCount = Math.min(filtered.length, renderPage * PAGE_SIZE);
  const hasMoreRendered = visibleCount < filtered.length;
  const hasMorePages = loadedPages < meta.pages;

  if (!hasMoreRendered && !hasMorePages) return;

  autoLoading = true;
  try {
    if (hasMoreRendered) {
      renderPage += 1;
    } else {
      await loadUntil(loadedPages + 1);
      renderPage += 1;
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

function openModal(item) {
  if (!item) return;

  modalChar.textContent = item.kanji || '';
  modalRank.textContent = `${getSortLabel()}排名 #${getRankByMode(item)} · 频次 ${item.frequency}`;
  modalCounts.textContent = `词条出现 ${item.count_term} 次，例句出现 ${item.count_example} 次。${formatGrade(item.grade)}${item.stroke_count ? `，${item.stroke_count}画。` : ''}`;

  modalReadings.innerHTML = '';
  (item.readings || []).forEach((reading) => {
    modalReadings.appendChild(makeChip(reading, 'reading'));
  });

  modalWords.innerHTML = '';
  (item.words || []).forEach((w) => {
    const text = `${w.term || ''}${w.zh ? ` · ${w.zh}` : ''}`;
    const chip = makeChip(text, 'word');
    if (w.en) {
      chip.title = w.en;
    }
    modalWords.appendChild(chip);
  });

  const firstExample = (item.examples || [])[0]?.example || '';
  modalExample.textContent = firstExample || '—';

  modalSources.innerHTML = '';
  (item.sources || []).forEach((src) => {
    modalSources.appendChild(makeChip(src, 'source'));
  });

  kanjiModal.hidden = false;
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  kanjiModal.hidden = true;
  document.body.style.overflow = '';
}

function setupModalEvents() {
  closeModalBtn.addEventListener('click', closeModal);
  kanjiModal.addEventListener('click', (event) => {
    if (event.target === kanjiModal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !kanjiModal.hidden) {
      closeModal();
    }
  });

  listEl.addEventListener('click', (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const btn = target.closest('.kanji-char');
    if (!(btn instanceof HTMLButtonElement)) return;

    const ch = btn.dataset.kanji || '';
    if (!ch) return;

    const item = visibleItemMap.get(ch);
    if (!item) return;

    openModal(item);
  });
}

async function init() {
  const res = await fetch('data/kanji_index.json');
  if (!res.ok) {
    setListMessage('汉字索引加载失败。');
    return;
  }

  meta = await res.json();
  const savedSort = loadSavedSortMode();
  if (savedSort && sortModeSelect) {
    sortModeSelect.value = savedSort;
  } else if (sortModeSelect && meta?.default_sort && SORT_MODE_KEY_MAP[meta.default_sort]) {
    sortModeSelect.value = meta.default_sort;
  }
  saveSortMode();

  initSourceFilter();

  const saved = loadSavedSourceIds();
  if (saved === null) {
    selectAllSources();
  } else {
    applySourceSelection(saved);
  }
  saveSelectedSourceIds();

  await loadUntil(1);
  render();
  setupInfiniteScroll();
  setupModalEvents();
}

searchInput.addEventListener('input', () => {
  resetAndRender();
  if (searchTimer) {
    clearTimeout(searchTimer);
  }
  searchTimer = setTimeout(() => {
    if (searchInput.value.trim()) {
      loadAllForSearch().catch((err) => {
        console.error(err);
      });
    }
  }, SEARCH_DEBOUNCE_MS);
});

sourceFilter.addEventListener('change', () => {
  onSourceChange().catch((err) => {
    console.error(err);
    setListMessage(`筛选失败：${err.message}`);
  });
});

if (selectAllSourcesBtn) {
  selectAllSourcesBtn.addEventListener('click', () => {
    selectAllSources();
    onSourceChange().catch((err) => {
      console.error(err);
      setListMessage(`筛选失败：${err.message}`);
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
      setListMessage(`筛选失败：${err.message}`);
    });
  });
}

init().catch((err) => {
  console.error(err);
  setListMessage(`初始化失败：${err.message}`);
});

if (sortModeSelect) {
  sortModeSelect.addEventListener('change', () => {
    saveSortMode();
    resetAndRender();
  });
}
