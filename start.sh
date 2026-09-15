#!/bin/bash
set -e

# Make sure we're in the backend directory for uvicorn
cd backend

# Use virtual environment if it exists (for local testing parity)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the FastAPI application binding to 0.0.0.0 and PORT
# Use fallback port 8000 if PORT is not set
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
