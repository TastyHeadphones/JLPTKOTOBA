import gzip
import json
import os
import re
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

import pdfplumber
from pykakasi import kakasi

ROOT = Path('/Users/young/Github/JLPTKOTOBA')
PDF_DIR = ROOT / 'PDF'
DATA_DIR = ROOT / 'data'
PUBLIC_DIR = ROOT / 'public'

JMDICT_GZ = DATA_DIR / 'JMdict_e.gz'
JMDICT_URL = 'https://www.edrdg.org/pub/Nihongo/JMdict_e.gz'
KANJI_RE = re.compile(r'[\u4e00-\u9faf々〆ヵヶ]')
KKS = kakasi()
CHUNK_SIZE = 120


def download_if_missing(url, path):
    if path.exists():
        return
    print(f'Downloading {url}...')
    rc = os.system(f"curl -L '{url}' -o '{path}'")
    if rc != 0 or not path.exists():
        raise RuntimeError(f'Failed to download {url}')


def group_lines(words, y_tol=2.0):
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
                        if (not left_text) or ('。' in left_text and current is not None):
                            if current is not None:
                                current['zh'] = (current['zh'] + ' ' + right_text).strip()
                            continue

                        term = left_text.replace(' ', '')
                        zh = right_text.replace(' ', '')

                        if is_hiragana_only(term) and len(term) >= 8 and current is not None:
                            current['zh'] = (current['zh'] + ' ' + zh).strip()
                            continue

                        if '：' in term and '：' in zh:
                            term = term.split('：')[0]
                            zh = zh.split('：')[0]
                        elif '：' in term and not zh:
                            term = term.split('：')[0]

                        term = re.sub(r'\d+$', '', term).strip()
                        zh = re.sub(r'\s*\d+\s*$', '', zh).strip()

                        if not term or is_header_line(term):
                            continue

                        current = {'term': term, 'zh': zh, 'source': pdf_path.name}
                        entries.append(current)

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


def normalize_term(term):
    t = term.replace('～', '').replace('〜', '').replace('・', '')
    t = re.sub(r'（.*?）', '', t)
    t = re.sub(r'\(.*?\)', '', t)
    t = t.strip('：: ').strip()
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

    if 'の' in term:
        prefix, suffix = term.rsplit('の', 1)
        suffix_gloss = kanji_map.get(suffix) or reading_map.get(suffix) or kanji_map.get(normalize_term(suffix))
        if suffix_gloss:
            return [f"{suffix_gloss[0]} (related to {prefix})"]

    for suffix, eng in SUFFIX_TRANSLATIONS.items():
        if term.endswith(suffix) and len(term) > len(suffix):
            base = term[:-len(suffix)]
            base_gloss = kanji_map.get(base) or reading_map.get(base) or kanji_map.get(normalize_term(base))
            if base_gloss:
                return [f"{base_gloss[0]} {eng}"]

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


def _stable_index(term, count):
    return sum(ord(c) for c in term) % count


def _is_kana(text):
    return bool(text) and re.fullmatch(r'[\u3040-\u30ffー]+', text) is not None


def _pick(templates, term):
    return templates[_stable_index(term, len(templates))]


def generate_example(term):
    raw = term.strip()
    base = normalize_term(raw)
    display = base or raw
    filled = raw.replace('～', '十').replace('〜', '十')

    suru_templates = [
        '{w}件、最近は職場でも普通に使う場面が増えてきたよ。',
        '来月の企画は私が{w}ことになって、今準備で忙しい。',
        'この案件、先に{w}と後の流れがかなり楽になる。',
        '急ぎの連絡が来たから、まずは今日中に{w}つもりだよ。',
        'チームで相談して、明日の朝いちで{w}方針にした。',
    ]
    verb_templates = [
        '今日は予定を少し早めて、駅前で{w}ことにしたんだ。',
        '忙しい日でも、要点だけはちゃんと{w}ようにしている。',
        '急な話だったけど、落ち着いて{w}たらうまくいった。',
        'この場面では、周りを見ながら{w}のが大事だと思う。',
        '最近は無理をせず、自分のペースで{w}ようにしてる。',
    ]
    i_adj_templates = [
        'この店、思ったより{w}から、また来たいって思った。',
        '最初は不安だったけど、やってみたら意外と{w}ね。',
        '最近この方法が{w}って分かって、かなり助かってる。',
        'その説明、短いのにすごく{w}から頭に入りやすい。',
        '今日は風が{w}し、早めに帰った方がよさそうだね。',
    ]
    adverb_templates = [
        '朝の会議で部長が{w}説明してくれて、全員すぐ理解できた。',
        '彼は質問に{w}答えるから、話していて安心できる。',
        '今日は時間がないから、ポイントだけ{w}共有しておくね。',
        '現場では{w}動くのが大事で、焦るとかえってミスする。',
        '相手の反応を見ながら{w}進めたら、会話がすごくスムーズだった。',
    ]
    noun_templates = [
        '最近のニュースで{w}って言葉をよく聞くし、身近な話題になってる。',
        'この前の打ち合わせでも{w}が話題になって、みんなで意見を出した。',
        '最初は難しく感じたけど、{w}の意味が分かると面白くなるね。',
        '実際に使ってみると、{w}の大事さを改めて実感する。',
        '友達と話していても{w}の話が出ることが増えてきたよ。',
    ]
    name_templates = [
        '昨日、{w}の特集を見て、改めてすごい人だと思った。',
        '授業で{w}の話が出てきて、もっと調べたくなった。',
        '最近、{w}に関する動画を見ていてかなり興味が湧いた。',
        '本屋で{w}の関連本を見かけて、つい手に取ってしまった。',
        '友達が{w}に詳しくて、話を聞いているだけで面白かった。',
    ]

    if re.search(r'（.*?する.*?）', raw) or raw.endswith('する'):
        w = display + 'する' if not display.endswith('する') else display
        return _pick(suru_templates, raw).format(w=w)

    if '～' in raw or '〜' in raw:
        return _pick(noun_templates, raw).format(w=filled)

    if re.search(r'[0-9０-９]{4}', raw) or re.search(r'[・.]', raw):
        return _pick(name_templates, raw).format(w=display)

    if display.endswith(('に', 'と')) and _is_kana(display):
        return _pick(adverb_templates, raw).format(w=display)

    if display.endswith('い') and len(display) >= 2 and _is_kana(display[-2:]):
        return _pick(i_adj_templates, raw).format(w=display)

    if display.endswith(('う', 'く', 'ぐ', 'す', 'つ', 'ぬ', 'ぶ', 'む', 'る')) and _is_kana(display[-1]):
        return _pick(verb_templates, raw).format(w=display)

    return _pick(noun_templates, raw).format(w=display)


def make_ruby_html(text):
    parts = []
    for token in KKS.convert(text):
        orig = token.get('orig', '')
        hira = token.get('hira', '')
        if KANJI_RE.search(orig) and hira and hira != orig:
            parts.append(f'<ruby>{escape(orig)}<rt>{escape(hira)}</rt></ruby>')
        else:
            parts.append(escape(orig))
    return ''.join(parts)


def source_key(source_name):
    return source_name.replace('.pdf', '')


def main():
    entries = parse_pdfs()
    kanji_map, reading_map = build_jmdict_maps()

    out = []
    for i, e in enumerate(entries, 1):
        term = e['term']
        zh = e['zh']
        example = generate_example(term)

        gloss = lookup_gloss(term, kanji_map, reading_map)
        en = '; '.join(gloss) if gloss else ''

        out.append({
            'id': i,
            'term': term,
            'term_ruby': make_ruby_html(term),
            'zh': zh,
            'en': en,
            'example': example,
            'example_ruby': make_ruby_html(example),
            'source': e['source']
        })

    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    # Keep a full dump for offline inspection.
    with open(PUBLIC_DIR / 'words.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)

    data_dir = PUBLIC_DIR / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    by_source = {}
    for item in out:
        key = source_key(item['source'])
        by_source.setdefault(key, []).append(item)

    index = {'sources': []}
    for key in sorted(by_source.keys()):
        items = by_source[key]
        page_count = (len(items) + CHUNK_SIZE - 1) // CHUNK_SIZE

        for page in range(page_count):
            chunk = items[page * CHUNK_SIZE:(page + 1) * CHUNK_SIZE]
            chunk_path = data_dir / f'{key}_p{page + 1}.json'
            with open(chunk_path, 'w', encoding='utf-8') as f:
                json.dump(chunk, f, ensure_ascii=False)

        index['sources'].append({
            'id': key,
            'label': key,
            'count': len(items),
            'pages': page_count,
            'chunk_prefix': f'{key}_p'
        })

    with open(data_dir / 'index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False)

    print(f'Wrote {len(out)} entries into chunk files under {data_dir}')


if __name__ == '__main__':
    main()
