import gzip
import json
import os
import urllib.request
from pathlib import Path

ROOT = Path('/Users/young/Github/JLPTKOTOBA')
DEST = ROOT / 'public' / 'kuromoji-dict'
META_URL = 'https://unpkg.com/kuromoji@0.1.2/dict/?meta'
BASE_URL = 'https://unpkg.com/kuromoji@0.1.2'

DEST.mkdir(parents=True, exist_ok=True)

meta = json.loads(urllib.request.urlopen(META_URL).read().decode('utf-8'))
files = [f['path'] for f in meta.get('files', []) if f['path'].endswith('.dat.gz')]

for path in files:
    url = BASE_URL + path
    name = Path(path).name
    out_gz = DEST / name
    out_dat = DEST / name[:-3]

    if out_dat.exists():
        continue

    print('Downloading', url)
    data = urllib.request.urlopen(url).read()
    out_gz.write_bytes(data)

    print('Decompressing', out_gz.name)
    with gzip.open(out_gz, 'rb') as f_in:
        out_dat.write_bytes(f_in.read())

    out_gz.unlink(missing_ok=True)

print('Done:', DEST)
