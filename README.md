# JLPTKOTOBA

从 `PDF` 目录内的词汇表 PDF 提取词条，生成一个可检索的静态网页，支持：
- 中文释义 + 英文释义
- 日文例句
- 汉字假名（Furigana）
- 点击词条/例句进行 TTS 朗读
- 独立 50 音发音页（含浊音、半浊音、拗音、拗音长音、外来音与特殊拍）
- 独立汉字总览页（汇总全部汉字，支持检索、筛选、点击放大）

## 目录结构
- `PDF/`：原始词汇表 PDF
- `scripts/build_site.py`：解析 PDF 并生成数据
- `public/`：静态站点（`index.html`、`styles.css`、`app.js`、`gojuon.html`、`gojuon.css`、`gojuon.js`、`kanji.html`、`kanji.css`、`kanji.js`）
- `public/data/`：按来源与分页切分后的词条数据
- `scripts/build_kanji_data.py`：从词条数据抽取全部汉字并生成分页数据

## 本地运行
```bash
cd /Users/young/Github/JLPTKOTOBA/public
python3 -m http.server 8000
```
然后访问：`http://localhost:8000`
50 音页：`http://localhost:8000/gojuon.html`
汉字页：`http://localhost:8000/kanji.html`

## 假名说明
假名在构建阶段由 `pykakasi` 预生成，页面直接渲染，不依赖在线词典。

## 重新生成数据
```bash
python3 -m pip install pykakasi
python3 /Users/young/Github/JLPTKOTOBA/scripts/build_site.py
python3 /Users/young/Github/JLPTKOTOBA/scripts/build_kanji_data.py
```

## GitHub Pages 部署
仓库内已提供 GitHub Actions 部署配置，推送到 `main` 分支后自动发布。

## 说明
- 英文释义优先来自 JMdict（由脚本下载并解析）。
- 未命中英文释义的词条会显示 `—`。
- 前端按来源文件与分页加载词条，避免一次性加载全部数据导致卡顿或崩溃。
- 页面滚动到底部会自动加载下一批词条（无“加载更多”按钮）。
- 汉字页支持三种排序：教材顺序（默认）、学年顺序、频次顺序。

## Cloud Text-to-Speech
- 页面使用 Google Cloud Text-to-Speech API（REST：`text:synthesize`）。
- 需要在页面的 `Cloud TTS Key` 输入框填入你自己的 API Key（会保存在浏览器 `localStorage`）。
- API Key 需启用 `Cloud Text-to-Speech API`，并建议做 HTTP Referrer 限制。
- 默认声音为 `ja-JP-Chirp3-HD-Iapetus`；可在页面切换其它日语 voice。
- 页面会尝试拉取你账号可用的 `ja-JP` voice 列表，并自动更新下拉框。
- 未填写 Key 或云端失败时会回退到浏览器内置 TTS。
