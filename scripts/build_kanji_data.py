import gzip
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

from pykakasi import kakasi

ROOT = Path('/Users/young/Github/JLPTKOTOBA')
PUBLIC_DIR = ROOT / 'public'
DATA_DIR = PUBLIC_DIR / 'data'
RAW_DATA_DIR = ROOT / 'data'
WORDS_JSON = PUBLIC_DIR / 'words.json'
KANJIDIC2_GZ = RAW_DATA_DIR / 'kanjidic2.xml.gz'
KANJIDIC2_URL = 'https://www.edrdg.org/pub/Nihongo/kanjidic2.xml.gz'

KANJI_RE = re.compile(r'[\u4e00-\u9faf々〆ヵヶ]')
PAGE_SIZE = 200
MAX_WORD_SAMPLES = 5
MAX_EXAMPLE_SAMPLES = 1
MAX_READING_SAMPLES = 10

KKS = kakasi()


def source_key(source_name):
    return (source_name or '').replace('.pdf', '')


def extract_kanji(text):
    return sorted(set(KANJI_RE.findall(text or '')))


def extract_term_readings(term):
    per_char = {}
    for token in KKS.convert(term or ''):
        orig = token.get('orig', '')
        hira = token.get('hira', '')
        if not orig or not hira:
            continue
        if not KANJI_RE.search(orig):
            continue
        for ch in set(orig):
            if not KANJI_RE.fullmatch(ch):
                continue
            per_char.setdefault(ch, set()).add(hira)
    return per_char


def download_if_missing(url, path):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    req = Request(url, headers={'User-Agent': 'JLPTKOTOBA/1.0'})
    with urlopen(req, timeout=120) as resp, open(path, 'wb') as f:
        while True:
            chunk = resp.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)


def _parse_int(text):
    if text is None:
        return None
    text = text.strip()
    if not text or not re.fullmatch(r'\d+', text):
        return None
    return int(text)


def load_kanjidic_meta():
    download_if_missing(KANJIDIC2_URL, KANJIDIC2_GZ)
    meta = {}
    with gzip.open(KANJIDIC2_GZ, 'rb') as f:
        tree = ET.parse(f)
    root = tree.getroot()

    for character in root.findall('character'):
        literal = (character.findtext('literal') or '').strip()
        if not literal:
            continue

        misc = character.find('misc')
        if misc is None:
            continue

        grade = _parse_int(misc.findtext('grade'))
        freq_rank = _parse_int(misc.findtext('freq'))
        stroke_count = None
        first_stroke = misc.findtext('stroke_count')
        if first_stroke is not None:
            stroke_count = _parse_int(first_stroke)

        meta[literal] = {
            'grade': grade,
            'freq_rank': freq_rank,
            'stroke_count': stroke_count,
        }

    return meta


def grade_bucket(grade):
    if grade in (1, 2, 3, 4, 5, 6, 8, 9, 10):
        return grade
    return 99


def build():
    if not WORDS_JSON.exists():
        raise RuntimeError(f'Missing input file: {WORDS_JSON}')

    words = json.loads(WORDS_JSON.read_text(encoding='utf-8'))
    kanjidic_meta = load_kanjidic_meta()

    source_order = {}
    for item in words:
        src = source_key(item.get('source', ''))
        if src and src not in source_order:
            source_order[src] = len(source_order) + 1

    by_kanji = {}
    source_kanji_counter = Counter()

    def ensure_entry(ch):
        if ch not in by_kanji:
            by_kanji[ch] = {
                'kanji': ch,
                'count_term': 0,
                'count_example': 0,
                'sources': set(),
                'readings': set(),
                'words': [],
                'examples': [],
                'first_seen_entry': 10**9,
                'first_seen_source_order': 10**9,
                '_seen_words': set(),
                '_seen_examples': set(),
            }
        return by_kanji[ch]

    for item in words:
        entry_id = int(item.get('id') or 0)
        term = item.get('term', '')
        example = item.get('example', '')
        zh = item.get('zh', '')
        en = item.get('en', '')
        src = source_key(item.get('source', ''))
        src_ord = source_order.get(src, 10**9)

        term_chars = extract_kanji(term)
        example_chars = extract_kanji(example)
        readings = extract_term_readings(term)

        for ch in term_chars:
            entry = ensure_entry(ch)
            entry['count_term'] += 1
            entry['sources'].add(src)
            entry['first_seen_entry'] = min(entry['first_seen_entry'], entry_id)
            entry['first_seen_source_order'] = min(entry['first_seen_source_order'], src_ord)
            if src:
                source_kanji_counter[(src, ch)] += 1

            for r in readings.get(ch, []):
                entry['readings'].add(r)

            if term and term not in entry['_seen_words'] and len(entry['words']) < MAX_WORD_SAMPLES:
                entry['words'].append({
                    'term': term,
                    'zh': zh,
                    'en': en,
                    'source': src,
                })
                entry['_seen_words'].add(term)

        for ch in example_chars:
            entry = ensure_entry(ch)
            entry['count_example'] += 1
            entry['sources'].add(src)
            entry['first_seen_entry'] = min(entry['first_seen_entry'], entry_id)
            entry['first_seen_source_order'] = min(entry['first_seen_source_order'], src_ord)
            if src:
                source_kanji_counter[(src, ch)] += 1

            if example and example not in entry['_seen_examples'] and len(entry['examples']) < MAX_EXAMPLE_SAMPLES:
                entry['examples'].append({
                    'example': example,
                    'source': src,
                })
                entry['_seen_examples'].add(example)

    out = []
    for entry in by_kanji.values():
        extra = kanjidic_meta.get(entry['kanji'], {})
        freq = entry['count_term'] + entry['count_example']
        out.append({
            'kanji': entry['kanji'],
            'frequency': freq,
            'count_term': entry['count_term'],
            'count_example': entry['count_example'],
            'grade': extra.get('grade'),
            'freq_rank': extra.get('freq_rank'),
            'stroke_count': extra.get('stroke_count'),
            'first_seen_entry': entry['first_seen_entry'],
            'first_seen_source_order': entry['first_seen_source_order'],
            'sources': sorted([s for s in entry['sources'] if s]),
            'readings': sorted(entry['readings'])[:MAX_READING_SAMPLES],
            'words': entry['words'],
            'examples': entry['examples'],
        })

    def textbook_key(item):
        return (
            item.get('first_seen_source_order', 10**9),
            item.get('first_seen_entry', 10**9),
            item['kanji'],
        )

    def school_key(item):
        grade = item.get('grade')
        return (
            grade_bucket(grade),
            grade if grade is not None else 99,
            item.get('freq_rank') if item.get('freq_rank') is not None else 99_999,
            item.get('stroke_count') if item.get('stroke_count') is not None else 99,
            item.get('first_seen_entry', 10**9),
            item['kanji'],
        )

    def frequency_key(item):
        return (
            -item['frequency'],
            -item['count_term'],
            item.get('first_seen_entry', 10**9),
            item['kanji'],
        )

    for i, item in enumerate(sorted(out, key=textbook_key), 1):
        item['rank_textbook'] = i
    for i, item in enumerate(sorted(out, key=school_key), 1):
        item['rank_school'] = i
    for i, item in enumerate(sorted(out, key=frequency_key), 1):
        item['rank_frequency'] = i

    out.sort(key=textbook_key)

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    page_count = (len(out) + PAGE_SIZE - 1) // PAGE_SIZE
    for page in range(page_count):
        chunk = out[page * PAGE_SIZE:(page + 1) * PAGE_SIZE]
        chunk_path = DATA_DIR / f'kanji_p{page + 1}.json'
        chunk_path.write_text(json.dumps(chunk, ensure_ascii=False), encoding='utf-8')

    source_ids = sorted({src for src, _ in source_kanji_counter.keys()})
    sources = []
    for src in source_ids:
        count = sum(1 for item in out if src in item['sources'])
        sources.append({
            'id': src,
            'label': src,
            'count': count,
        })

    index = {
        'dataset': 'project-wordlists',
        'title': '漢字一覧',
        'total': len(out),
        'page_size': PAGE_SIZE,
        'pages': page_count,
        'default_sort': 'textbook',
        'sort_modes': [
            {'id': 'textbook', 'label': '教材顺序'},
            {'id': 'school', 'label': '学年顺序'},
            {'id': 'frequency', 'label': '频次顺序'},
        ],
        'sources': sources,
        'generated_at': datetime.now(timezone.utc).isoformat(),
    }
    (DATA_DIR / 'kanji_index.json').write_text(json.dumps(index, ensure_ascii=False), encoding='utf-8')

    print(f'Built kanji data: {len(out)} kanji, {page_count} pages')


if __name__ == '__main__':
    build()
