const gojuonSection = document.getElementById('gojuonSection');
const dakuonSection = document.getElementById('dakuonSection');
const yoonSection = document.getElementById('yoonSection');
const yoonLongSection = document.getElementById('yoonLongSection');
const foreignSection = document.getElementById('foreignSection');
const specialSection = document.getElementById('specialSection');

const ttsStatus = document.getElementById('ttsStatus');
const cloudTtsKeyInput = document.getElementById('cloudTtsKeyInput');
const voiceSelect = document.getElementById('voiceSelect');

const FIVE_VOWELS = ['a', 'i', 'u', 'e', 'o'];
const YOON_VOWELS = ['ya', 'yu', 'yo'];

const CLOUD_TTS_API_URL = 'https://texttospeech.googleapis.com/v1/text:synthesize';
const CLOUD_TTS_VOICES_URL = 'https://texttospeech.googleapis.com/v1/voices';
const CLOUD_TTS_KEY_STORAGE_KEY = 'cloud_tts_api_key_persist';
const CLOUD_TTS_FALLBACK_STATUS = '语音：浏览器回退（未配置 Cloud TTS Key）';
const CLOUD_TTS_DEFAULT_VOICE = 'ja-JP-Chirp3-HD-Iapetus';
const MAX_AUDIO_CACHE = 24;

let bestBrowserVoice = null;
let activeAudio = null;
let ttsRequestController = null;

const audioCache = new Map();

function sound(hiragana, katakana, romaji, speak) {
  return {
    hiragana,
    katakana,
    romaji,
    speak: speak || hiragana,
  };
}

const GOJUON_ROWS = [
  {
    line: 'あ行',
    cells: [
      sound('あ', 'ア', 'a'),
      sound('い', 'イ', 'i'),
      sound('う', 'ウ', 'u'),
      sound('え', 'エ', 'e'),
      sound('お', 'オ', 'o'),
    ],
  },
  {
    line: 'か行',
    cells: [
      sound('か', 'カ', 'ka'),
      sound('き', 'キ', 'ki'),
      sound('く', 'ク', 'ku'),
      sound('け', 'ケ', 'ke'),
      sound('こ', 'コ', 'ko'),
    ],
  },
  {
    line: 'さ行',
    cells: [
      sound('さ', 'サ', 'sa'),
      sound('し', 'シ', 'shi'),
      sound('す', 'ス', 'su'),
      sound('せ', 'セ', 'se'),
      sound('そ', 'ソ', 'so'),
    ],
  },
  {
    line: 'た行',
    cells: [
      sound('た', 'タ', 'ta'),
      sound('ち', 'チ', 'chi'),
      sound('つ', 'ツ', 'tsu'),
      sound('て', 'テ', 'te'),
      sound('と', 'ト', 'to'),
    ],
  },
  {
    line: 'な行',
    cells: [
      sound('な', 'ナ', 'na'),
      sound('に', 'ニ', 'ni'),
      sound('ぬ', 'ヌ', 'nu'),
      sound('ね', 'ネ', 'ne'),
      sound('の', 'ノ', 'no'),
    ],
  },
  {
    line: 'は行',
    cells: [
      sound('は', 'ハ', 'ha'),
      sound('ひ', 'ヒ', 'hi'),
      sound('ふ', 'フ', 'fu'),
      sound('へ', 'ヘ', 'he'),
      sound('ほ', 'ホ', 'ho'),
    ],
  },
  {
    line: 'ま行',
    cells: [
      sound('ま', 'マ', 'ma'),
      sound('み', 'ミ', 'mi'),
      sound('む', 'ム', 'mu'),
      sound('め', 'メ', 'me'),
      sound('も', 'モ', 'mo'),
    ],
  },
  {
    line: 'や行',
    cells: [
      sound('や', 'ヤ', 'ya'),
      null,
      sound('ゆ', 'ユ', 'yu'),
      null,
      sound('よ', 'ヨ', 'yo'),
    ],
  },
  {
    line: 'ら行',
    cells: [
      sound('ら', 'ラ', 'ra'),
      sound('り', 'リ', 'ri'),
      sound('る', 'ル', 'ru'),
      sound('れ', 'レ', 're'),
      sound('ろ', 'ロ', 'ro'),
    ],
  },
  {
    line: 'わ行',
    cells: [
      sound('わ', 'ワ', 'wa'),
      null,
      null,
      null,
      sound('を', 'ヲ', 'wo'),
    ],
  },
];

const DAKUON_ROWS = [
  {
    line: 'が行（浊音）',
    cells: [
      sound('が', 'ガ', 'ga'),
      sound('ぎ', 'ギ', 'gi'),
      sound('ぐ', 'グ', 'gu'),
      sound('げ', 'ゲ', 'ge'),
      sound('ご', 'ゴ', 'go'),
    ],
  },
  {
    line: 'ざ行（浊音）',
    cells: [
      sound('ざ', 'ザ', 'za'),
      sound('じ', 'ジ', 'ji'),
      sound('ず', 'ズ', 'zu'),
      sound('ぜ', 'ゼ', 'ze'),
      sound('ぞ', 'ゾ', 'zo'),
    ],
  },
  {
    line: 'だ行（浊音）',
    cells: [
      sound('だ', 'ダ', 'da'),
      sound('ぢ', 'ヂ', 'ji / di'),
      sound('づ', 'ヅ', 'zu / du'),
      sound('で', 'デ', 'de'),
      sound('ど', 'ド', 'do'),
    ],
  },
  {
    line: 'ば行（浊音）',
    cells: [
      sound('ば', 'バ', 'ba'),
      sound('び', 'ビ', 'bi'),
      sound('ぶ', 'ブ', 'bu'),
      sound('べ', 'ベ', 'be'),
      sound('ぼ', 'ボ', 'bo'),
    ],
  },
  {
    line: 'ぱ行（半浊音）',
    cells: [
      sound('ぱ', 'パ', 'pa'),
      sound('ぴ', 'ピ', 'pi'),
      sound('ぷ', 'プ', 'pu'),
      sound('ぺ', 'ペ', 'pe'),
      sound('ぽ', 'ポ', 'po'),
    ],
  },
];

const YOON_ROWS = [
  { line: 'k系', cells: [sound('きゃ', 'キャ', 'kya'), sound('きゅ', 'キュ', 'kyu'), sound('きょ', 'キョ', 'kyo')] },
  { line: 'g系', cells: [sound('ぎゃ', 'ギャ', 'gya'), sound('ぎゅ', 'ギュ', 'gyu'), sound('ぎょ', 'ギョ', 'gyo')] },
  { line: 's系', cells: [sound('しゃ', 'シャ', 'sha'), sound('しゅ', 'シュ', 'shu'), sound('しょ', 'ショ', 'sho')] },
  { line: 'z系', cells: [sound('じゃ', 'ジャ', 'ja'), sound('じゅ', 'ジュ', 'ju'), sound('じょ', 'ジョ', 'jo')] },
  { line: 't系', cells: [sound('ちゃ', 'チャ', 'cha'), sound('ちゅ', 'チュ', 'chu'), sound('ちょ', 'チョ', 'cho')] },
  { line: 'd系（少见）', cells: [sound('ぢゃ', 'ヂャ', 'dya'), sound('ぢゅ', 'ヂュ', 'dyu'), sound('ぢょ', 'ヂョ', 'dyo')] },
  { line: 'n系', cells: [sound('にゃ', 'ニャ', 'nya'), sound('にゅ', 'ニュ', 'nyu'), sound('にょ', 'ニョ', 'nyo')] },
  { line: 'h系', cells: [sound('ひゃ', 'ヒャ', 'hya'), sound('ひゅ', 'ヒュ', 'hyu'), sound('ひょ', 'ヒョ', 'hyo')] },
  { line: 'b系', cells: [sound('びゃ', 'ビャ', 'bya'), sound('びゅ', 'ビュ', 'byu'), sound('びょ', 'ビョ', 'byo')] },
  { line: 'p系', cells: [sound('ぴゃ', 'ピャ', 'pya'), sound('ぴゅ', 'ピュ', 'pyu'), sound('ぴょ', 'ピョ', 'pyo')] },
  { line: 'm系', cells: [sound('みゃ', 'ミャ', 'mya'), sound('みゅ', 'ミュ', 'myu'), sound('みょ', 'ミョ', 'myo')] },
  { line: 'r系', cells: [sound('りゃ', 'リャ', 'rya'), sound('りゅ', 'リュ', 'ryu'), sound('りょ', 'リョ', 'ryo')] },
];

const YOON_LONG_ROWS = [
  { line: 'k系', cells: [sound('きゃあ', 'キャー', 'kyaa'), sound('きゅう', 'キュー', 'kyuu'), sound('きょう', 'キョー', 'kyou')] },
  { line: 'g系', cells: [sound('ぎゃあ', 'ギャー', 'gyaa'), sound('ぎゅう', 'ギュー', 'gyuu'), sound('ぎょう', 'ギョー', 'gyou')] },
  { line: 's系', cells: [sound('しゃあ', 'シャー', 'shaa'), sound('しゅう', 'シュー', 'shuu'), sound('しょう', 'ショー', 'shou')] },
  { line: 'z系', cells: [sound('じゃあ', 'ジャー', 'jaa'), sound('じゅう', 'ジュー', 'juu'), sound('じょう', 'ジョー', 'jou')] },
  { line: 't系', cells: [sound('ちゃあ', 'チャー', 'chaa'), sound('ちゅう', 'チュー', 'chuu'), sound('ちょう', 'チョー', 'chou')] },
  { line: 'd系（少见）', cells: [sound('ぢゃあ', 'ヂャー', 'dyaa'), sound('ぢゅう', 'ヂュー', 'dyuu'), sound('ぢょう', 'ヂョー', 'dyou')] },
  { line: 'n系', cells: [sound('にゃあ', 'ニャー', 'nyaa'), sound('にゅう', 'ニュー', 'nyuu'), sound('にょう', 'ニョー', 'nyou')] },
  { line: 'h系', cells: [sound('ひゃあ', 'ヒャー', 'hyaa'), sound('ひゅう', 'ヒュー', 'hyuu'), sound('ひょう', 'ヒョー', 'hyou')] },
  { line: 'b系', cells: [sound('びゃあ', 'ビャー', 'byaa'), sound('びゅう', 'ビュー', 'byuu'), sound('びょう', 'ビョー', 'byou')] },
  { line: 'p系', cells: [sound('ぴゃあ', 'ピャー', 'pyaa'), sound('ぴゅう', 'ピュー', 'pyuu'), sound('ぴょう', 'ピョー', 'pyou')] },
  { line: 'm系', cells: [sound('みゃあ', 'ミャー', 'myaa'), sound('みゅう', 'ミュー', 'myuu'), sound('みょう', 'ミョー', 'myou')] },
  { line: 'r系', cells: [sound('りゃあ', 'リャー', 'ryaa'), sound('りゅう', 'リュー', 'ryuu'), sound('りょう', 'リョー', 'ryou')] },
];

const FOREIGN_VOWEL_ROWS = [
  {
    line: 'f系',
    cells: [
      sound('ふぁ', 'ファ', 'fa'),
      sound('ふぃ', 'フィ', 'fi'),
      sound('ふ', 'フ', 'fu'),
      sound('ふぇ', 'フェ', 'fe'),
      sound('ふぉ', 'フォ', 'fo'),
    ],
  },
  {
    line: 'v系',
    cells: [
      sound('ゔぁ', 'ヴァ', 'va'),
      sound('ゔぃ', 'ヴィ', 'vi'),
      sound('ゔ', 'ヴ', 'vu'),
      sound('ゔぇ', 'ヴェ', 've'),
      sound('ゔぉ', 'ヴォ', 'vo'),
    ],
  },
  {
    line: 'w扩展',
    cells: [
      sound('うぁ', 'ウァ', 'wa'),
      sound('うぃ', 'ウィ', 'wi'),
      sound('うぅ', 'ウゥ', 'wu'),
      sound('うぇ', 'ウェ', 'we'),
      sound('うぉ', 'ウォ', 'wo'),
    ],
  },
  {
    line: 'kw系（少见）',
    cells: [
      sound('くぁ', 'クァ', 'kwa'),
      sound('くぃ', 'クィ', 'kwi'),
      sound('くぅ', 'クゥ', 'kwu'),
      sound('くぇ', 'クェ', 'kwe'),
      sound('くぉ', 'クォ', 'kwo'),
    ],
  },
  {
    line: 'gw系（少见）',
    cells: [
      sound('ぐぁ', 'グァ', 'gwa'),
      sound('ぐぃ', 'グィ', 'gwi'),
      sound('ぐぅ', 'グゥ', 'gwu'),
      sound('ぐぇ', 'グェ', 'gwe'),
      sound('ぐぉ', 'グォ', 'gwo'),
    ],
  },
  {
    line: 'ts扩展',
    cells: [
      sound('つぁ', 'ツァ', 'tsa'),
      sound('つぃ', 'ツィ', 'tsi'),
      sound('つぅ', 'ツゥ', 'tsu'),
      sound('つぇ', 'ツェ', 'tse'),
      sound('つぉ', 'ツォ', 'tso'),
    ],
  },
];

const FOREIGN_COMBOS = [
  sound('てぃ', 'ティ', 'ti'),
  sound('でぃ', 'ディ', 'di'),
  sound('とぅ', 'トゥ', 'tu'),
  sound('どぅ', 'ドゥ', 'du'),
  sound('ちぇ', 'チェ', 'che'),
  sound('しぇ', 'シェ', 'she'),
  sound('じぇ', 'ジェ', 'je'),
  sound('すぃ', 'スィ', 'si'),
  sound('ずぃ', 'ズィ', 'zi'),
  sound('ふゅ', 'フュ', 'fyu'),
  sound('ゔゅ', 'ヴュ', 'vyu'),
  sound('てゅ', 'テュ', 'tyu'),
  sound('でゅ', 'デュ', 'dyu'),
  sound('いぇ', 'イェ', 'ye'),
  sound('きぇ', 'キェ', 'kye'),
  sound('ぎぇ', 'ギェ', 'gye'),
  sound('にぇ', 'ニェ', 'nye'),
  sound('ひぇ', 'ヒェ', 'hye'),
  sound('びぇ', 'ビェ', 'bye'),
  sound('ぴぇ', 'ピェ', 'pye'),
  sound('みぇ', 'ミェ', 'mye'),
  sound('りぇ', 'リェ', 'rye'),
];

const SPECIAL_ITEMS = [
  {
    title: '撥音（ん）',
    desc: 'ん在词尾和辅音前读鼻音，实际口型会随下一个音变化。',
    samples: [
      { label: 'ほん', speak: 'ほん' },
      { label: 'しんぶん', speak: 'しんぶん' },
      { label: 'かんじ', speak: 'かんじ' },
    ],
  },
  {
    title: '促音（っ）',
    desc: 'っ表示停顿一拍，后面的清辅音要“加重”。',
    samples: [
      { label: 'きって', speak: 'きって' },
      { label: 'がっこう', speak: 'がっこう' },
      { label: 'いっしょ', speak: 'いっしょ' },
    ],
  },
  {
    title: '长音符号（ー）',
    desc: '片假名外来语常用“ー”延长前一拍元音。',
    samples: [
      { label: 'コーヒー', speak: 'コーヒー' },
      { label: 'メール', speak: 'メール' },
      { label: 'スーパー', speak: 'スーパー' },
    ],
  },
  {
    title: '平假名长音（母音延长）',
    desc: '常见写法：あ段=ああ，い段=いい，う段=うう，え段=えい/ええ，お段=おう/おお。',
    samples: [
      { label: 'おかあさん', speak: 'おかあさん' },
      { label: 'おにいさん', speak: 'おにいさん' },
      { label: 'すうがく', speak: 'すうがく' },
      { label: 'せんせい', speak: 'せんせい' },
      { label: 'とうきょう', speak: 'とうきょう' },
      { label: 'おおきい', speak: 'おおきい' },
    ],
  },
  {
    title: '小假名（ぁぃぅぇぉゃゅょ）',
    desc: '小假名常用于拗音、外来音和细化发音。',
    samples: [
      { label: 'ティ', speak: 'ティ' },
      { label: 'ファ', speak: 'ファ' },
      { label: 'キャ', speak: 'キャ' },
      { label: 'ヴァ', speak: 'ヴァ' },
    ],
  },
];

function createSectionHeader(title, note) {
  const wrapper = document.createElement('div');

  const h2 = document.createElement('h2');
  h2.className = 'section-title';
  h2.textContent = title;
  wrapper.appendChild(h2);

  if (note) {
    const p = document.createElement('p');
    p.className = 'section-note';
    p.textContent = note;
    wrapper.appendChild(p);
  }

  return wrapper;
}

function createSoundButton(item, className = 'sound-btn') {
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = className;
  btn.dataset.speak = item.speak || item.hiragana || item.katakana;

  const kana = document.createElement('span');
  kana.className = 'kana';
  kana.textContent = item.hiragana || '';
  btn.appendChild(kana);

  const katakana = document.createElement('span');
  katakana.className = 'katakana';
  katakana.textContent = item.katakana || '';
  btn.appendChild(katakana);

  const romaji = document.createElement('span');
  romaji.className = 'romaji';
  romaji.textContent = item.romaji || '';
  btn.appendChild(romaji);

  return btn;
}

function appendSoundCell(tr, item) {
  const td = document.createElement('td');
  if (!item) {
    td.className = 'empty';
    td.textContent = '—';
  } else {
    td.appendChild(createSoundButton(item));
  }
  tr.appendChild(td);
}

function renderFiveVowelTable(sectionEl, title, note, rows) {
  sectionEl.innerHTML = '';
  sectionEl.appendChild(createSectionHeader(title, note));

  const wrap = document.createElement('div');
  wrap.className = 'table-wrap';

  const table = document.createElement('table');
  const thead = document.createElement('thead');
  const headRow = document.createElement('tr');

  const first = document.createElement('th');
  first.className = 'row-label';
  first.textContent = '行';
  headRow.appendChild(first);

  FIVE_VOWELS.forEach((vowel) => {
    const th = document.createElement('th');
    th.textContent = vowel;
    headRow.appendChild(th);
  });

  thead.appendChild(headRow);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  rows.forEach((row) => {
    const tr = document.createElement('tr');

    const rowLabel = document.createElement('th');
    rowLabel.className = 'line-label';
    rowLabel.textContent = row.line;
    tr.appendChild(rowLabel);

    row.cells.forEach((item) => {
      appendSoundCell(tr, item);
    });

    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  wrap.appendChild(table);
  sectionEl.appendChild(wrap);
}

function renderYoonTable(sectionEl, title, note, rows) {
  sectionEl.innerHTML = '';
  sectionEl.appendChild(createSectionHeader(title, note));

  const wrap = document.createElement('div');
  wrap.className = 'table-wrap';

  const table = document.createElement('table');
  const thead = document.createElement('thead');
  const headRow = document.createElement('tr');

  const first = document.createElement('th');
  first.className = 'row-label';
  first.textContent = '组';
  headRow.appendChild(first);

  YOON_VOWELS.forEach((vowel) => {
    const th = document.createElement('th');
    th.textContent = vowel;
    headRow.appendChild(th);
  });

  thead.appendChild(headRow);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  rows.forEach((row) => {
    const tr = document.createElement('tr');

    const rowLabel = document.createElement('th');
    rowLabel.className = 'line-label';
    rowLabel.textContent = row.line;
    tr.appendChild(rowLabel);

    row.cells.forEach((item) => {
      appendSoundCell(tr, item);
    });

    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  wrap.appendChild(table);
  sectionEl.appendChild(wrap);
}

function renderGojuon() {
  renderFiveVowelTable(
    gojuonSection,
    '清音五十音图（标准排列）',
    '按あ・か・さ・た・な・は・ま・や・ら・わ排列，空位保留。',
    GOJUON_ROWS
  );

  const nWrap = document.createElement('div');
  nWrap.className = 'chips';
  nWrap.appendChild(createSoundButton(sound('ん', 'ン', 'n')));
  gojuonSection.appendChild(nWrap);
}

function renderDakuon() {
  renderFiveVowelTable(
    dakuonSection,
    '浊音与半浊音',
    '在清音上加浊点（゛）或半浊点（゜）形成。',
    DAKUON_ROWS
  );
}

function renderYoon() {
  renderYoonTable(
    yoonSection,
    '拗音（ゃ・ゅ・ょ）',
    '由い段 + 小ゃ/ゅ/ょ组合而成。',
    YOON_ROWS
  );
}

function renderYoonLong() {
  renderYoonTable(
    yoonLongSection,
    '拗音长音（含ゃ/ゅ/ょ的长拍）',
    '常见写法：ゃ系多接あ，ゅ系多接う，ょ系多写成おう。',
    YOON_LONG_ROWS
  );
}

function renderForeign() {
  foreignSection.innerHTML = '';
  foreignSection.appendChild(
    createSectionHeader(
      '外来音扩展',
      '包含现代日语借词中常见的扩展音节与小假名组合。'
    )
  );

  const top = document.createElement('div');
  top.className = 'table-wrap';

  const table = document.createElement('table');
  const thead = document.createElement('thead');
  const headRow = document.createElement('tr');

  const first = document.createElement('th');
  first.className = 'row-label';
  first.textContent = '组';
  headRow.appendChild(first);

  FIVE_VOWELS.forEach((vowel) => {
    const th = document.createElement('th');
    th.textContent = vowel;
    headRow.appendChild(th);
  });

  thead.appendChild(headRow);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  FOREIGN_VOWEL_ROWS.forEach((row) => {
    const tr = document.createElement('tr');

    const rowLabel = document.createElement('th');
    rowLabel.className = 'line-label';
    rowLabel.textContent = row.line;
    tr.appendChild(rowLabel);

    row.cells.forEach((item) => {
      appendSoundCell(tr, item);
    });

    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  top.appendChild(table);
  foreignSection.appendChild(top);

  const comboTitle = document.createElement('p');
  comboTitle.className = 'section-note';
  comboTitle.textContent = '常见外来音组合：';
  foreignSection.appendChild(comboTitle);

  const chips = document.createElement('div');
  chips.className = 'chips';
  FOREIGN_COMBOS.forEach((item) => {
    const chip = document.createElement('div');
    chip.className = 'chip';
    chip.appendChild(createSoundButton(item));
    chips.appendChild(chip);
  });
  foreignSection.appendChild(chips);
}

function renderSpecial() {
  specialSection.innerHTML = '';
  specialSection.appendChild(
    createSectionHeader(
      '特殊拍与发音规则',
      '下面给出常见规则与可点读示例。'
    )
  );

  const grid = document.createElement('div');
  grid.className = 'special-grid';

  SPECIAL_ITEMS.forEach((item) => {
    const card = document.createElement('article');
    card.className = 'special-card';

    const h3 = document.createElement('h3');
    h3.textContent = item.title;
    card.appendChild(h3);

    const p = document.createElement('p');
    p.textContent = item.desc;
    card.appendChild(p);

    const sampleList = document.createElement('div');
    sampleList.className = 'sample-list';
    item.samples.forEach((sample) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'sample-btn';
      btn.dataset.speak = sample.speak;
      btn.textContent = sample.label;
      sampleList.appendChild(btn);
    });

    card.appendChild(sampleList);
    grid.appendChild(card);
  });

  specialSection.appendChild(grid);
}

function scoreBrowserVoice(voice) {
  const name = (voice?.name || '').toLowerCase();
  const lang = (voice?.lang || '').toLowerCase();
  let score = 0;

  if (lang.startsWith('ja')) score += 50;
  if (/siri/.test(name)) score += 120;
  if (/natural/.test(name)) score += 90;
  if (/kyoko|nanami|otoya|ja-jp/.test(name)) score += 80;
  if (/enhanced|premium|high quality/.test(name)) score += 60;
  if (voice?.default) score += 15;

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

function setTtsStatus(text) {
  ttsStatus.textContent = text;
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
  return (payload.voices || [])
    .map((voice) => voice.name)
    .filter((name) => typeof name === 'string' && name.startsWith('ja-JP-'))
    .sort((a, b) => scoreCloudVoiceName(b) - scoreCloudVoiceName(a));
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

function setupClickSpeak() {
  document.addEventListener('click', (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const node = target.closest('[data-speak]');
    if (!(node instanceof HTMLElement)) return;

    const text = node.dataset.speak || '';
    if (!text) return;

    speak(text);
  });
}

function initTtsPanel() {
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
  setTtsStatus(CLOUD_TTS_FALLBACK_STATUS);

  renderGojuon();
  renderDakuon();
  renderYoon();
  renderYoonLong();
  renderForeign();
  renderSpecial();

  setupClickSpeak();
  initTtsPanel();
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

window.addEventListener('beforeunload', () => {
  for (const url of audioCache.values()) {
    URL.revokeObjectURL(url);
  }
});

init().catch((err) => {
  console.error(err);
  setTtsStatus(`初始化失败：${err.message}`);
});
