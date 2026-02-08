# JLPTKOTOBA

从 `PDF` 目录内的词汇表 PDF 提取词条，生成一个可检索的静态网页，支持：
- 中文释义 + 英文释义
- 日文例句
- 汉字假名（Furigana）
- 点击词条/例句进行 TTS 朗读

## 目录结构
- `PDF/`：原始词汇表 PDF
- `scripts/build_site.py`：解析 PDF 并生成数据
- `public/`：静态站点（`index.html`、`styles.css`、`app.js`、`words.json`）

## 本地运行
```bash
cd /Users/young/Github/JLPTKOTOBA/public
python3 -m http.server 8000
```
然后访问：`http://localhost:8000`

## 假名说明
假名由 Kuromoji 库在线词典生成（CDN）。

## 重新生成数据
```bash
python3 /Users/young/Github/JLPTKOTOBA/scripts/build_site.py
```

## GitHub Pages 部署
仓库内已提供 GitHub Actions 部署配置，推送到 `main` 分支后自动发布。

## 说明
- 英文释义优先来自 JMdict（由脚本下载并解析）。
- 若未命中英文释义，网页端会用 MyMemory 翻译 API 生成并缓存（保存在浏览器 `localStorage`）。
