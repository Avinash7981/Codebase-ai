# Codebase AI

Codebase AI is a powerful codebase intelligence platform that allows you to easily ingest a GitHub repository and ask questions about its code using semantic retrieval and AI models.

## Features

- **GitHub Repository Ingestion**: Clone and analyze public repositories.
- **Semantic Code Search**: Retrieve exact files, symbols, and code chunks.
- **Hybrid Retrieval System**: Combines semantic embeddings with lexical/keyword search for maximum accuracy.
- **Deterministic Local Fallback**: Continues to work reliably using standard Python libraries even when heavy dependencies (like BGE embeddings) fail to install.
- **Persistent Vector Store**: Uses an optimized SQLite backend to ensure data survives server restarts.
- **LLM Fallback Architecture**: Defaults to free-tier AI providers (Gemini) with automatic failover to fallback models (OpenAI) if unavailable.
- **Live Code Viewer**: Automatically jumps to the cited source code file and line number.

## Architecture

- **Backend**: FastAPI (Python)
- **Frontend**: Next.js & React (TypeScript)
- **Vector Database**: SQLite (using a lightweight localized chunk storage system)

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python (3.10+)
- `git` installed

### Environment Variables

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

Ensure you set:
- `GEMINI_API_KEY`: Your Google Gemini API key.
- `LLM_API_KEY`: Your OpenAI API key (for fallback).

### Running the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

### Usage

1. Open `http://localhost:3000` in your browser.
2. Enter a public GitHub repository URL (e.g., `https://github.com/psf/requests`).
3. Wait for the ingestion and indexing process to complete.
4. Ask a question about the codebase!

## License

MIT License
