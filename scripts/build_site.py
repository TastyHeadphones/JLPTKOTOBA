import gzip
import json
import os
import re
import time
import bz2
import xml.etree.ElementTree as ET
from collections import deque
from html import escape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pdfplumber
from pykakasi import kakasi

ROOT = Path('/Users/young/Github/JLPTKOTOBA')
PDF_DIR = ROOT / 'PDF'
DATA_DIR = ROOT / 'data'
PUBLIC_DIR = ROOT / 'public'

JMDICT_GZ = DATA_DIR / 'JMdict_e.gz'
JMDICT_URL = 'https://www.edrdg.org/pub/Nihongo/JMdict_e.gz'
TATOEBA_JPN_SENTENCES = DATA_DIR / 'jpn_sentences.tsv.bz2'
TATOEBA_JPN_ENG_LINKS = DATA_DIR / 'jpn-eng_links.tsv.bz2'
TATOEBA_ENG_SENTENCES = DATA_DIR / 'eng_sentences.tsv.bz2'
TATOEBA_JPN_SENTENCES_URL = 'https://downloads.tatoeba.org/exports/per_language/jpn/jpn_sentences.tsv.bz2'
TATOEBA_JPN_ENG_LINKS_URL = 'https://downloads.tatoeba.org/exports/per_language/jpn/jpn-eng_links.tsv.bz2'
TATOEBA_ENG_SENTENCES_URL = 'https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences.tsv.bz2'
KANJI_RE = re.compile(r'[\u4e00-\u9faf々〆ヵヶ]')
JP_CHAR_RE = re.compile(r'[\u3040-\u30ff\u4e00-\u9faf]')
KKS = kakasi()
CHUNK_SIZE = 120
GEMINI_TEXT_MODEL = os.getenv('GEMINI_TEXT_MODEL', 'gemma-3-4b-it')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_BATCH_SIZE = int(os.getenv('GEMINI_BATCH_SIZE', '8'))
GEMINI_MAX_RETRIES = int(os.getenv('GEMINI_MAX_RETRIES', '4'))
GEMINI_TIMEOUT_SECS = int(os.getenv('GEMINI_TIMEOUT_SECS', '90'))
GEMINI_BATCH_PAUSE = float(os.getenv('GEMINI_BATCH_PAUSE', '1.0'))
AI_EXAMPLE_CACHE = DATA_DIR / 'ai_examples_cache.json'
AI_EXAMPLE_CACHE_VERSION = 'v2'

# A tiny set of OCR-damaged headwords that cannot be used verbatim as natural terms.
MANUAL_EXAMPLE_OVERRIDES = {
    'ある組織を構成する人、ある仕事': '彼は新しいプロジェクトのメンバーとして、資料作成を担当している。',
    'はらが立つ': '店員の失礼な態度に、私は本当に腹が立った。',
    'この、私たちのという意味': 'このノートは私たちのなので、勝手に持っていかないでください。',
    '手をつなぐ': '道を渡るとき、子どもと手をつないで歩いた。',
    'ひとははおや': '友だちのお母さんは、とても明るくて親切な人です。',
    '新せいひん': 'この新製品は、使いやすさと軽さが大きな特長です。',
}


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


def canonical_term_for_example(term):
    t = (term or '').strip()
    if not t:
        return ''
    # Prefer quoted headwords in glossary-style notes such as "「少し」のていねいな言".
    quoted = re.search(r'「([^」]+)」', t)
    if quoted:
        t = quoted.group(1)
    t = t.replace('～', '').replace('〜', '')
    t = re.sub(r'[①-⑳]\s*$', '', t)
    t = t.strip('「」"\'')
    t = re.sub(r'（[^）]*）', '', t)
    t = re.sub(r'\([^)]*\)', '', t)
    # Handle malformed notes like "入管（＝入国管理局" without closing bracket.
    t = re.split(r'[（(]', t)[0]
    t = re.split(r'[：:，,；;＝=]', t)[0]
    t = t.replace('の略', '')
    t = re.sub(r'の(?:ていねい|丁寧|カジュアル|かたい)な?言.*$', '', t)
    t = re.sub(r'を丁寧に呼.*$', '', t)
    t = re.sub(r'を基準とした金額のこと.*$', '', t)
    t = re.sub(r'という意味.*$', '', t)
    t = re.sub(r'の気持ち・思い.*$', '', t)
    if '、' in t and len(t) >= 8:
        t = t.split('、', 1)[0]
    if 'を' in t and len(t) >= 8:
        t = t.split('を', 1)[0]
    t = t.replace('　', '').replace(' ', '')
    if re.match(r'^[ぁ-ゖァ-ヺ][一-龯].+', t):
        t = t[1:]
    t = t.strip()
    if not t:
        t = normalize_term(term).strip()
    return t or (term or '').strip()


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

    queue = deque()
    for node in root.next.values():
        node.fail = root
        queue.append(node)

    while queue:
        current = queue.popleft()
        for ch, nxt in current.next.items():
            queue.append(nxt)
            fail = current.fail
            while fail and ch not in fail.next:
                fail = fail.fail
            nxt.fail = fail.next[ch] if fail and ch in fail.next else root
            nxt.out.extend(nxt.fail.out)

    return root


def aho_find_patterns(root, text):
    node = root
    matched = set()
    for ch in text:
        while node and ch not in node.next:
            node = node.fail
        if not node:
            node = root
            continue
        node = node.next[ch]
        if node.out:
            matched.update(node.out)
    return matched


def _is_valid_jp_sentence(text):
    if not text or not JP_CHAR_RE.search(text):
        return False
    length = len(text)
    if length < 10 or length > 56:
        return False
    if re.search(r'https?://|www\\.', text):
        return False
    if re.search(r'[A-Za-z]{4,}', text):
        return False
    if text.count('「') != text.count('」'):
        return False
    return True


EN_STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'in',
    'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'with',
    'someone', 'something', 'one', 'ones', 'person', 'people', 'make',
    'made', 'do', 'does', 'did', 'have', 'has', 'had',
}


def _extract_en_keywords(text):
    words = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", (text or '').lower())
    return {w for w in words if w not in EN_STOPWORDS}


def _term_variants(term):
    raw = (term or '').strip()
    canon = canonical_term_for_example(raw)
    variants = {
        raw,
        canon,
        normalize_term(raw),
        normalize_term(canon),
        re.sub(r'（.*?）', '', raw).strip(),
        re.sub(r'\\(.*?\\)', '', raw).strip(),
    }
    cleaned = set()
    for v in variants:
        v = v.replace(' ', '').strip()
        if len(v) >= 2 and JP_CHAR_RE.search(v):
            cleaned.add(v)
    return cleaned


def _score_example(sentence, en_line, entry):
    term = entry['term']
    norm = normalize_term(term)
    en_gloss = entry.get('en', '')

    if not _is_valid_jp_sentence(sentence):
        return -10_000

    if term not in sentence and (not norm or norm not in sentence):
        return -10_000

    score = 0
    length = len(sentence)
    score += 130 - abs(length - 24) * 2

    if sentence.endswith('。'):
        score += 12
    if re.search(r'[!?！？]', sentence):
        score -= 6
    if re.search(r'[0-9０-９]{3,}', sentence):
        score -= 6

    if term in sentence:
        score += 85
    elif norm and norm in sentence:
        score += 45

    # Prefer examples whose English translation aligns with dictionary gloss.
    gloss_words = _extract_en_keywords(en_gloss)
    if gloss_words:
        line_words = _extract_en_keywords(en_line)
        overlap = len(gloss_words & line_words)
        score += overlap * 24
        if overlap == 0:
            score -= 12

    return score


def build_corpus_examples(entries):
    download_if_missing(TATOEBA_JPN_SENTENCES_URL, TATOEBA_JPN_SENTENCES)
    download_if_missing(TATOEBA_JPN_ENG_LINKS_URL, TATOEBA_JPN_ENG_LINKS)
    download_if_missing(TATOEBA_ENG_SENTENCES_URL, TATOEBA_ENG_SENTENCES)
    print('Collecting corpus examples...')

    pattern_to_ids = {}
    for idx, entry in enumerate(entries):
        for pattern in _term_variants(entry['term']):
            pattern_to_ids.setdefault(pattern, set()).add(idx)

    root = build_aho_automaton(pattern_to_ids.keys())
    best = {}

    jpn_to_eng = {}
    needed_eng_ids = set()
    with bz2.open(TATOEBA_JPN_ENG_LINKS, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 2:
                continue
            jpn_id, eng_id = parts[0], parts[1]
            # Keep the first linked English sentence only.
            if jpn_id in jpn_to_eng:
                continue
            jpn_to_eng[jpn_id] = eng_id
            needed_eng_ids.add(eng_id)

    eng_map = {}
    with bz2.open(TATOEBA_ENG_SENTENCES, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t', 2)
            if len(parts) < 3:
                continue
            sid, lang, text = parts
            if lang != 'eng' or sid not in needed_eng_ids:
                continue
            eng_map[sid] = text

    with bz2.open(TATOEBA_JPN_SENTENCES, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t', 2)
            if len(parts) < 3:
                continue
            sid, lang, jp = parts
            if lang != 'jpn':
                continue
            if not _is_valid_jp_sentence(jp):
                continue

            matched_patterns = aho_find_patterns(root, jp)
            if not matched_patterns:
                continue

            candidate_ids = set()
            for pat in matched_patterns:
                candidate_ids.update(pattern_to_ids.get(pat, ()))

            en_line = eng_map.get(jpn_to_eng.get(sid, ''), '')
            for idx in candidate_ids:
                entry = entries[idx]
                score = _score_example(jp, en_line, entry)
                if score < 75:
                    continue
                prev = best.get(idx)
                if prev is None or score > prev[0]:
                    best[idx] = (score, jp)

    matched = {idx: pair[1] for idx, pair in best.items()}
    print(f'Corpus examples matched: {len(matched)}/{len(entries)}')
    return matched


def _clean_model_json(text):
    if not text:
        return ''
    content = text.strip()
    if content.startswith('```'):
        content = re.sub(r'^```[a-zA-Z]*\n?', '', content)
        content = re.sub(r'\n?```$', '', content)
    return content.strip()


def _normalize_ai_sentence(text):
    if not text:
        return ''
    sent = text.strip()
    sent = sent.replace('**', '').replace('`', '')
    sent = sent.replace('<br>', ' ').replace('<br/>', ' ')
    sent = re.sub(r'^\s*\d+\s*[.)、]\s*', '', sent)
    sent = sent.strip(' "\'')
    sent = sent.strip('「」')
    sent = sent.replace('\n', ' ').strip()
    sent = re.sub(r'\s+', ' ', sent)
    # Remove trailing romanization/transliteration hints.
    sent = re.sub(r'\s*\([^)]*[A-Za-z][^)]*\)\s*$', '', sent).strip()
    sent = sent.strip('「」')
    return sent


def _sanitize_example_sentence(text):
    sent = _normalize_ai_sentence(text)
    if not sent:
        return ''
    # Drop inline romanization blocks like "(Kono ...)".
    sent = re.sub(r'\([^)]*[A-Za-z][^)]*\)', '', sent)
    sent = sent.replace('*', '')
    sent = re.sub(r'\s+', ' ', sent).strip()
    # Keep only the first full Japanese sentence when trailing notes/translations exist.
    m = re.search(r'[。！？]', sent)
    if m:
        sent = sent[:m.end()].strip()
    return sent


def _extract_gemini_text(payload):
    parts = []
    for cand in payload.get('candidates', []):
        for part in cand.get('content', {}).get('parts', []):
            if 'text' in part and part['text']:
                parts.append(part['text'])
    return '\n'.join(parts).strip()


def _validation_variants(term):
    out = set()
    raw = (term or '').strip()
    if not raw:
        return out
    canon = canonical_term_for_example(raw)
    candidates = {
        raw,
        canon,
        normalize_term(raw),
        normalize_term(canon),
    }
    for c in candidates:
        v = (c or '').replace(' ', '').replace('　', '').strip()
        if v:
            out.add(v)
    return out


def _to_hira(text):
    parts = []
    for token in KKS.convert(text or ''):
        hira = token.get('hira') or token.get('orig') or ''
        parts.append(hira)
    return ''.join(parts)


def _validate_ai_example(example, term, raw_term=''):
    if not example:
        return False
    sent = example.strip()
    if not JP_CHAR_RE.search(sent):
        return False
    if len(sent) < 6 or len(sent) > 120:
        return False
    variants = set()
    variants.update(_term_variants(term))
    variants.update(_validation_variants(term))
    if raw_term:
        variants.update(_term_variants(raw_term))
        variants.update(_validation_variants(raw_term))
    if any(v in sent for v in variants):
        return True

    # Accept kana/kanji orthographic variants with the same reading.
    hira_sent = _to_hira(sent)
    for v in variants:
        if len(v) < 2:
            continue
        hira_v = _to_hira(v)
        if hira_v and hira_v in hira_sent:
            return True
    return False


def _example_cache_key(entry):
    return '\t'.join([
        AI_EXAMPLE_CACHE_VERSION,
        GEMINI_TEXT_MODEL,
        (entry.get('example_term') or '').strip(),
        (entry.get('term') or '').strip(),
        (entry.get('zh') or '').strip(),
        (entry.get('en') or '').strip(),
    ])


def _load_ai_example_cache():
    if not AI_EXAMPLE_CACHE.exists():
        return {}
    try:
        with open(AI_EXAMPLE_CACHE, 'r', encoding='utf-8') as f:
            raw = json.load(f)
        if not isinstance(raw, dict):
            return {}
        out = {}
        for k, v in raw.items():
            if isinstance(k, str) and isinstance(v, str):
                out[k] = v
        return out
    except (OSError, json.JSONDecodeError):
        return {}


def _save_ai_example_cache(cache):
    AI_EXAMPLE_CACHE.parent.mkdir(parents=True, exist_ok=True)
    with open(AI_EXAMPLE_CACHE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False)


def _gemini_request(prompt, api_key):
    url = (
        f'https://generativelanguage.googleapis.com/v1beta/models/'
        f'{GEMINI_TEXT_MODEL}:generateContent?key={api_key}'
    )
    body = {
        'contents': [
            {
                'parts': [{'text': prompt}],
            }
        ],
        'generationConfig': {
            'temperature': 0.3,
            'topP': 0.9,
            'maxOutputTokens': 2048,
        },
    }
    req = Request(
        url,
        data=json.dumps(body, ensure_ascii=False).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    with urlopen(req, timeout=GEMINI_TIMEOUT_SECS) as resp:
        payload = json.loads(resp.read().decode('utf-8'))
    text = _extract_gemini_text(payload)
    if not text:
        raise RuntimeError('Gemini returned empty text response')
    return text


def _build_batch_prompt(batch):
    lines = []
    for item in batch:
        lines.append(
            json.dumps(
                {
                    'id': item['id'],
                    'term': item.get('example_term') or item['term'],
                    'raw_term': item['term'],
                    'zh': item['zh'],
                    'en': item['en'],
                },
                ensure_ascii=False,
            )
        )

    instruction = (
        '你是日语教材编写者。请为每个词条写1句教科书级日语例句。\\n'
        '要求：\\n'
        '1) 必须结合词义（zh/en），语义准确。\\n'
        '2) 难度中等，口语自然，像日语教材中的标准例句。\\n'
        '3) 句子自然、完整、适中长度（15-45字为主）。\\n'
        '4) 请优先使用常用汉字书写（日语自然写法）。\\n'
        '5) 例句必须包含 term 本身（原样）。\\n'
        '6) 严禁输出解释、注释、编号、markdown。\\n'
        '7) 只输出 JSON 数组。\\n'
        '输出格式：[{\"id\":1,\"example\":\"...。\"}]\\n'
        '待处理词条：\\n'
        + '\\n'.join(lines)
    )
    return instruction


def _request_ai_examples_batch(batch, api_key):
    prompt = _build_batch_prompt(batch)
    text = _gemini_request(prompt, api_key)
    cleaned = _clean_model_json(text)
    try:
        arr = json.loads(cleaned)
    except json.JSONDecodeError:
        # Try to recover from extra text around JSON.
        l = cleaned.find('[')
        r = cleaned.rfind(']')
        if l == -1 or r == -1 or r <= l:
            raise
        arr = json.loads(cleaned[l:r + 1])

    out = {}
    for obj in arr if isinstance(arr, list) else []:
        if not isinstance(obj, dict):
            continue
        idx = obj.get('id')
        if isinstance(idx, str) and idx.isdigit():
            idx = int(idx)
        example = _sanitize_example_sentence((obj.get('example') or '').strip())
        if isinstance(idx, int):
            out[idx] = example
    return out


def _request_ai_single_sentence(entry, api_key):
    target = (entry.get('example_term') or entry.get('term') or '').strip()
    prompt = (
        '你是日语教材编写者。请写1句自然、口语、教材级日语例句。\\n'
        f'term: {target}\\n'
        f'zh: {entry.get("zh", "")}\\n'
        f'en: {entry.get("en", "")}\\n'
        '要求：必须原样包含 term；长度 8-45 字；只输出句子本身，不要解释，不要 JSON。'
    )
    text = _gemini_request(prompt, api_key)
    cleaned = _clean_model_json(text)
    if not cleaned:
        return ''

    if cleaned.startswith('{') or cleaned.startswith('['):
        try:
            payload = json.loads(cleaned)
            if isinstance(payload, dict):
                ex = payload.get('example', '')
                return _sanitize_example_sentence(ex)
            if isinstance(payload, list) and payload:
                head = payload[0]
                if isinstance(head, dict):
                    return _sanitize_example_sentence(head.get('example', ''))
                if isinstance(head, str):
                    return _sanitize_example_sentence(head)
        except json.JSONDecodeError:
            pass

    lines = [ln.strip() for ln in cleaned.splitlines() if ln.strip()]
    return _sanitize_example_sentence(lines[0] if lines else cleaned)


def _retry_delay_seconds(attempt, err):
    # Respect API rate limits aggressively to avoid mass failures.
    if isinstance(err, HTTPError) and getattr(err, 'code', None) == 429:
        retry_after = 0
        try:
            if err.headers:
                value = err.headers.get('Retry-After')
                if value and value.isdigit():
                    retry_after = int(value)
        except Exception:
            retry_after = 0
        return float(retry_after) if retry_after > 0 else float(min(90, 10 * (attempt + 1)))

    if isinstance(err, (URLError, TimeoutError)):
        return float(min(30, 3 * (attempt + 1)))

    return float(min(20, 1.5 * (attempt + 1)))


def build_ai_examples(entries, missing_ids):
    if not missing_ids:
        return {}
    if not GEMINI_API_KEY:
        raise RuntimeError('GEMINI_API_KEY is required to generate missing examples')

    print(f'Generating AI examples for {len(missing_ids)} entries (model={GEMINI_TEXT_MODEL})...')
    result = {}
    id_to_entry = {entry['id']: entry for entry in entries}
    cache = _load_ai_example_cache()

    for idx in missing_ids:
        entry = id_to_entry[idx]
        target_term = entry.get('example_term') or entry['term']
        cached = _sanitize_example_sentence(cache.get(_example_cache_key(entry), ''))
        if _validate_ai_example(cached, target_term, raw_term=entry['term']):
            result[idx] = cached if cached.endswith('。') else cached + '。'

    pending = [idx for idx in missing_ids if idx not in result]
    if result:
        print(f'AI cache hit: {len(result)}/{len(missing_ids)}')

    effective_batch_size = GEMINI_BATCH_SIZE
    if GEMINI_TEXT_MODEL.startswith('gemma-'):
        # Gemma follows single-item prompts much more reliably than batched JSON arrays.
        effective_batch_size = 1
    batch_pause = GEMINI_BATCH_PAUSE if effective_batch_size > 1 else max(GEMINI_BATCH_PAUSE, 0.8)

    # Batch generation pass
    total_batches = (len(pending) + effective_batch_size - 1) // effective_batch_size if pending else 0
    batch_counter = 0
    for start in range(0, len(pending), effective_batch_size):
        batch_ids = pending[start:start + effective_batch_size]
        batch = [id_to_entry[i] for i in batch_ids]
        batch_counter += 1
        print(f'AI batch {batch_counter}/{total_batches}: {len(batch_ids)} entries')

        batch_examples = {}
        for attempt in range(GEMINI_MAX_RETRIES):
            try:
                batch_examples = _request_ai_examples_batch(batch, GEMINI_API_KEY)
                break
            except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as err:
                if attempt == GEMINI_MAX_RETRIES - 1:
                    print(f'Batch failed after retries: ids {batch_ids[0]}..{batch_ids[-1]} ({err})')
                    batch_examples = {}
                    break
                delay = _retry_delay_seconds(attempt, err)
                if isinstance(err, HTTPError) and getattr(err, 'code', None) == 429:
                    print(f'Rate limited on batch {batch_counter}, sleeping {delay:.1f}s')
                time.sleep(delay)

        for idx in batch_ids:
            cand = _sanitize_example_sentence(batch_examples.get(idx, ''))
            entry = id_to_entry[idx]
            target_term = entry.get('example_term') or entry['term']
            if _validate_ai_example(cand, target_term, raw_term=entry['term']):
                sent = cand if cand.endswith('。') else cand + '。'
                result[idx] = sent
                cache[_example_cache_key(entry)] = sent

        if batch_counter % 5 == 0:
            _save_ai_example_cache(cache)
        time.sleep(batch_pause)

    # Single item recovery pass for unresolved ids.
    unresolved = [idx for idx in missing_ids if idx not in result]
    if unresolved:
        print(f'Retrying unresolved examples one-by-one: {len(unresolved)}')

    for idx in unresolved:
        entry = id_to_entry[idx]
        single = [{
            'id': entry['id'],
            'term': entry['term'],
            'example_term': entry.get('example_term') or entry['term'],
            'zh': entry['zh'],
            'en': entry['en'],
        }]
        success = False
        for attempt in range(GEMINI_MAX_RETRIES):
            try:
                cand = _request_ai_single_sentence(single[0], GEMINI_API_KEY)
                target_term = entry.get('example_term') or entry['term']
                if _validate_ai_example(cand, target_term, raw_term=entry['term']):
                    sent = cand if cand.endswith('。') else cand + '。'
                    result[idx] = sent
                    cache[_example_cache_key(entry)] = sent
                    success = True
                    break
            except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as err:
                delay = _retry_delay_seconds(attempt, err)
                if isinstance(err, HTTPError) and getattr(err, 'code', None) == 429:
                    print(f'Rate limited on single id={idx}, sleeping {delay:.1f}s')
                time.sleep(delay)
                continue
            time.sleep(0.2)
        if not success:
            print(f'AI single retry failed: id={idx}, term={entry["term"]}')
        elif idx % 20 == 0:
            _save_ai_example_cache(cache)

    unresolved = [idx for idx in missing_ids if idx not in result]
    if unresolved:
        for idx in list(unresolved):
            entry = id_to_entry[idx]
            manual = MANUAL_EXAMPLE_OVERRIDES.get(entry['term'])
            if not manual:
                continue
            sent = _sanitize_example_sentence(manual)
            if not sent.endswith('。'):
                sent += '。'
            result[idx] = sent
            cache[_example_cache_key(entry)] = sent

    unresolved = [idx for idx in missing_ids if idx not in result]
    if unresolved:
        sample = ','.join(str(i) for i in unresolved[:10])
        raise RuntimeError(
            f'Failed to generate AI examples for {len(unresolved)} entries. '
            f'First unresolved ids: {sample}'
        )

    _save_ai_example_cache(cache)
    print(f'AI generated examples: {len(result)}/{len(missing_ids)}')
    return result


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
    for i, entry in enumerate(entries, 1):
        entry['id'] = i
        entry['example_term'] = canonical_term_for_example(entry['term'])
        gloss = lookup_gloss(entry['term'], kanji_map, reading_map)
        entry['en'] = '; '.join(gloss) if gloss else ''

    corpus_examples = build_corpus_examples(entries)
    missing_ids = [e['id'] for e in entries if (e['id'] - 1) not in corpus_examples]
    ai_examples = build_ai_examples(entries, missing_ids) if missing_ids else {}
    print(f'Final example coverage: {len(corpus_examples) + len(ai_examples)}/{len(entries)}')

    out = []
    for e in entries:
        i = e['id']
        term = e['term']
        zh = e['zh']
        en = e.get('en', '')
        example = corpus_examples.get(i - 1) or ai_examples.get(i, '')
        example = _sanitize_example_sentence(example)
        if example and not re.search(r'[。！？]$', example):
            example += '。'
        if not example:
            raise RuntimeError(f'Missing example for entry id={i}, term={term}')

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
