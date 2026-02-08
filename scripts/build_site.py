import json
import os
import re
import gzip
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

import pdfplumber

ROOT = Path('/Users/young/Github/JLPTKOTOBA')
PDF_DIR = ROOT / 'PDF'
DATA_DIR = ROOT / 'data'
PUBLIC_DIR = ROOT / 'public'

JMDICT_GZ = DATA_DIR / 'JMdict_e.gz'
TANAKA_ZIP = DATA_DIR / 'jpn-eng.zip'

JMDICT_URL = 'https://www.edrdg.org/pub/Nihongo/JMdict_e.gz'
TANAKA_URL = 'https://www.manythings.org/anki/jpn-eng.zip'


def download_if_missing(url, path):
    if path.exists():
        return
    print(f'Downloading {url}...')
    rc = os.system(f"curl -L '{url}' -o '{path}'")
    if rc != 0 or not path.exists():
        raise RuntimeError(f'Failed to download {url}')


def group_lines(words, y_tol=2.0):
    # Group words into lines based on top coordinate
    lines = []
    for w in sorted(words, key=lambda x: (x['top'], x['x0'])):
        placed = False
        for line in lines:
            if abs(line['top'] - w['top']) <= y_tol:
                line['words'].append(w)
                placed = True
                break
        if not placed:
            lines.append({'top': w['top'], 'words': [w]})
    # Normalize line order and word order
    for line in lines:
        line['words'] = sorted(line['words'], key=lambda x: x['x0'])
    lines = sorted(lines, key=lambda x: x['top'])
    return lines


def is_header_line(text):
    if not text:
        return True
    header_markers = ['TRY', '日本語', '達陣', '單字表', '從日檢', '作者', '出版']
    if any(m in text for m in header_markers):
        return True
    if re.fullmatch(r'\d+', text):
        return True
    return False


def parse_pdfs():
    def is_hiragana_only(text):
        return bool(text) and re.fullmatch(r'[\u3040-\u309f]+', text) is not None

    entries = []
    for pdf_path in sorted(PDF_DIR.glob('*.pdf')):
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                words = page.extract_words(extra_attrs=['size'])
                lines = group_lines(words)
                current = None
                for line in lines:
                    left_words = [w for w in line['words'] if w['x0'] < 200]
                    right_words = [w for w in line['words'] if w['x0'] >= 200]
                    left_text = ''.join(w['text'] for w in left_words).strip()
                    right_text = ''.join(w['text'] for w in right_words).strip()

                    if is_header_line(left_text) and not right_text:
                        continue

                    if right_text:
                        # continuation lines for descriptions
                        if (not left_text) or ('。' in left_text and current is not None):
                            if current is not None:
                                current['zh'] = (current['zh'] + ' ' + right_text).strip()
                            continue

                        # New entry
                        term = left_text.replace(' ', '')
                        zh = right_text.replace(' ', '')

                        # Treat long hiragana lines as continuation (likely furigana for explanations)
                        if is_hiragana_only(term) and len(term) >= 8 and current is not None:
                            current['zh'] = (current['zh'] + ' ' + zh).strip()
                            continue

                        # Handle colon entries like "ねぶた祭り： 青森睡魔祭："
                        if '：' in term and '：' in zh:
                            term = term.split('：')[0]
                            zh = zh.split('：')[0]
                        elif '：' in term and not zh:
                            term = term.split('：')[0]

                        term = re.sub(r'\d+$', '', term).strip()
                        zh = re.sub(r'\s*\d+\s*$', '', zh).strip()

                        # Skip noisy lines
                        if not term or is_header_line(term):
                            continue

                        current = {'term': term, 'zh': zh, 'source': pdf_path.name}
                        entries.append(current)
                    else:
                        # likely a reading line; ignore
                        continue
    # Deduplicate by term+zh
    seen = set()
    deduped = []
    for e in entries:
        key = (e['term'], e['zh'])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(e)
    return deduped


def build_jmdict_maps():
    download_if_missing(JMDICT_URL, JMDICT_GZ)
    print('Parsing JMdict...')
    kanji_map = {}
    reading_map = {}
    with gzip.open(JMDICT_GZ, 'rb') as f:
        tree = ET.parse(f)
    root = tree.getroot()
    for entry in root.findall('entry'):
        kebs = [k.text for k in entry.findall('k_ele/keb') if k.text]
        rebs = [r.text for r in entry.findall('r_ele/reb') if r.text]
        glosses = []
        for sense in entry.findall('sense'):
            for gloss in sense.findall('gloss'):
                lang = gloss.attrib.get('{http://www.w3.org/XML/1998/namespace}lang', 'eng')
                if lang == 'eng' and gloss.text:
                    glosses.append(gloss.text)
        if not glosses:
            continue
        glosses = glosses[:5]
        for k in kebs:
            kanji_map.setdefault(k, glosses)
        for r in rebs:
            reading_map.setdefault(r, glosses)
    return kanji_map, reading_map


class AhoNode:
    __slots__ = ('next', 'fail', 'out')
    def __init__(self):
        self.next = {}
        self.fail = None
        self.out = []


def build_aho_automaton(patterns):
    root = AhoNode()
    for pat in patterns:
        node = root
        for ch in pat:
            node = node.next.setdefault(ch, AhoNode())
        node.out.append(pat)
    # build fail links
    queue = []
    for node in root.next.values():
        node.fail = root
        queue.append(node)
    while queue:
        r = queue.pop(0)
        for ch, u in r.next.items():
            queue.append(u)
            v = r.fail
            while v and ch not in v.next:
                v = v.fail
            u.fail = v.next[ch] if v and ch in v.next else root
            u.out += u.fail.out
    return root


def find_examples(terms):
    download_if_missing(TANAKA_URL, TANAKA_ZIP)
    print('Searching example sentences...')
    pending = set(terms)
    examples = {}
    root = build_aho_automaton(pending)

    def is_japanese_text(text):
        return bool(re.search(r'[\u3040-\u30ff\u4e00-\u9faf]', text))

    with zipfile.ZipFile(TANAKA_ZIP) as z:
        # find the Japanese/English text file
        name = None
        for n in z.namelist():
            if n.endswith('jpn.txt'):
                name = n
                break
        if name is None:
            return examples
        with z.open(name) as f:
            for raw in f:
                try:
                    line = raw.decode('utf-8').strip()
                except UnicodeDecodeError:
                    continue
                if not line:
                    continue
                parts = line.split('\t')
                jp = parts[0]
                if not is_japanese_text(jp):
                    continue
                # Aho-Corasick scan
                node = root
                for ch in jp:
                    while node and ch not in node.next:
                        node = node.fail
                    if not node:
                        node = root
                        continue
                    node = node.next[ch]
                    for pat in node.out:
                        if pat in pending:
                            examples[pat] = jp
                            pending.remove(pat)
                    if not pending:
                        return examples
    return examples


def normalize_term(term):
    t = term.replace('～', '').replace('・', '')
    t = re.sub(r'（.*?）', '', t)
    t = re.sub(r'\\(.*?\\)', '', t)
    t = t.replace('〜', '').strip()
    t = re.sub(r'する$', '', t)
    return t




SUFFIX_TRANSLATIONS = {
    '地方': 'region',
    '会社': 'company',
    '作品': 'work',
    '名前': 'name',
    '問題': 'problem',
    '祭り': 'festival',
    '賞': 'award',
    '機': 'machine',
    '性': 'nature',
    '感': 'feeling',
    '率': 'rate',
    '制': 'system',
    '化': 'ization',
    '力': 'power',
    '者': 'person',
    '度': 'degree',
    '界': 'world',
    '料': 'fee',
    '部': 'section',
    '体': 'body',
}


def lookup_gloss(term, kanji_map, reading_map):
    candidates = [term, normalize_term(term)]
    for c in candidates:
        if c in kanji_map:
            return kanji_map[c]
        if c in reading_map:
            return reading_map[c]

    # Split by separators
    for sep in ['・', '/', '／']:
        if sep in term:
            parts = [p for p in term.split(sep) if p]
            glosses = []
            for p in parts:
                g = kanji_map.get(p) or reading_map.get(p) or kanji_map.get(normalize_term(p))
                if not g:
                    glosses = []
                    break
                glosses.append(g[0])
            if glosses:
                return ['; '.join(glosses)]

    # Handle の constructions
    if 'の' in term:
        prefix, suffix = term.rsplit('の', 1)
        suffix_gloss = kanji_map.get(suffix) or reading_map.get(suffix) or kanji_map.get(normalize_term(suffix))
        if suffix_gloss:
            return [f"{suffix_gloss[0]} (related to {prefix})"]

    # Handle common suffixes
    for suffix, eng in SUFFIX_TRANSLATIONS.items():
        if term.endswith(suffix) and len(term) > len(suffix):
            base = term[:-len(suffix)]
            base_gloss = kanji_map.get(base) or reading_map.get(base) or kanji_map.get(normalize_term(base))
            if base_gloss:
                return [f"{base_gloss[0]} {eng}"]

    # Try longest substring match
    norm = normalize_term(term)
    best = None
    for i in range(len(norm)):
        for j in range(len(norm), i + 1, -1):
            sub = norm[i:j]
            if sub in kanji_map:
                best = kanji_map[sub]
                break
        if best:
            break
    return best


def main():
    entries = parse_pdfs()
    kanji_map, reading_map = build_jmdict_maps()

    terms = [e['term'] for e in entries]
    examples = find_examples(terms)

    out = []
    for i, e in enumerate(entries, 1):
        term = e['term']
        zh = e['zh']
        norm = normalize_term(term)

        gloss = lookup_gloss(term, kanji_map, reading_map)
        en = '; '.join(gloss) if gloss else ''

        example = examples.get(term) or examples.get(norm)
        if not example:
            example = f"この単語は「{term}」です。"

        out.append({
            'id': i,
            'term': term,
            'zh': zh,
            'en': en,
            'example': example,
            'source': e['source']
        })

    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    with open(PUBLIC_DIR / 'words.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Wrote {len(out)} entries to {PUBLIC_DIR / "words.json"}')

if __name__ == '__main__':
    main()
