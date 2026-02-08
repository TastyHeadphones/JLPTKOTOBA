# JLPTKOTOBA

从 `PDF` 目录内的词汇表 PDF 提取词条，生成一个可检索的静态网页，支持：
- 中文释义 + 英文释义
- 日文例句
- 汉字假名（Furigana）
- 点击词条/例句进行 TTS 朗读

## 目录结构
- `PDF/`：原始词汇表 PDF
- `scripts/build_site.py`：解析 PDF 并生成数据
- `public/`：静态站点（`index.html`、`styles.css`、`app.js`）
- `public/data/`：按来源与分页切分后的词条数据

## 本地运行
```bash
cd /Users/young/Github/JLPTKOTOBA/public
python3 -m http.server 8000
```
然后访问：`http://localhost:8000`

## 假名说明
假名在构建阶段由 `pykakasi` 预生成，页面直接渲染，不依赖在线词典。

## 重新生成数据
```bash
python3 -m pip install pykakasi
python3 /Users/young/Github/JLPTKOTOBA/scripts/build_site.py
```

## GitHub Pages 部署
仓库内已提供 GitHub Actions 部署配置，推送到 `main` 分支后自动发布。

## 说明
- 英文释义优先来自 JMdict（由脚本下载并解析）。
- 未命中英文释义的词条会显示 `—`。
- 前端按来源文件与分页加载词条，避免一次性加载全部数据导致卡顿或崩溃。
- 页面滚动到底部会自动加载下一批词条（无“加载更多”按钮）。

## OpenAI TTS
- 页面支持 OpenAI 自然语音（模型：`gpt-4o-mini-tts`）。
- 需要在页面的 `OpenAI Key` 输入框填入你自己的 API Key（仅保存在当前浏览器会话）。
- 未填写 Key 时会自动回退到浏览器内置 TTS。
- 语音为 AI 生成音频。
