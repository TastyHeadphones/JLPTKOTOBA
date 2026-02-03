# JLPT Kotoba (日本語語彙)

A premium, modern web application for mastering JLPT (Japanese Language Proficiency Test) vocabulary, featuring native audio, furigana transparency, and example sentences.

## Features

- 🌸 **Premium UI**: Beautiful, clean interface designed with Japanese aesthetics.
- 🔊 **Text-to-Speech**: Native-sounding audio for every word and example sentence.
- 📖 **Furigana Support**: Clear reading aids above Kanji.
- 🏷️ **Level Filtering**: Easily filter vocabulary by JLPT levels (N5-N1).
- 🔍 **Search**: Instant search across words, readings, and meanings.
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices.

## Project Structure

```
JLPTKOTOBA/
├── jlpt-web/          # React + Vite Web Application
│   ├── src/
│   │   ├── data/      # JSON vocabulary data
│   │   └── components/# UI Components
│   └── ...
├── scripts/           # Data processing scripts
│   ├── parse_vocab.py # Converts markdown to JSON
│   └── enrich_vocab.py# Generates examples (LLM helper)
└── vocab_master.md    # Source of Truth Data
```

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python 3.x

### Installation

1.  **Clone the repository**
2.  **Install dependencies**:
    ```bash
    cd jlpt-web
    npm install
    ```

### Running Locally

```bash
cd jlpt-web
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) to view the app.

## Data Management

### Updating Vocabulary
The source of truth is `vocab_master.md`. If you edit this file, update the web app data by running:

```bash
# From project root
python3 scripts/parse_vocab.py
```

### Enriching Data (Example Sentences)
To generate example sentences using an LLM (Mock/Demo mode by default):

```bash
# From project root
python3 scripts/enrich_vocab.py
```
> **Note**: Edit `scripts/enrich_vocab.py` to connect to your OpenAI/Anthropic API key for real generated sentences.

## Deployment

This project includes a GitHub Actions workflow `.github/workflows/deploy.yml` that automatically builds and deploys the application to **GitHub Pages** when you push to the `main` branch.

**Important**: 
1. Go to your repository **Settings > Pages**.
2. Set "Source" to **GitHub Actions**.

## License

MIT
