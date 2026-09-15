from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Default to sqlite for hackathon-friendly local running if no postgres is available
    DATABASE_URL: str = "sqlite+aiosqlite:///./codebase.db"
    
    # Empty QDRANT_URL means use local file-based storage
    QDRANT_URL: str = ""
    QDRANT_PATH: str = "./qdrant_data"
    
    # Default to gemini — free tier, no OpenAI quota needed
    LLM_PROVIDER: str = "gemini"
    LLM_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    # gemini-2.0-flash is the stable free-tier model
    LLM_MODEL: str = "gemini-2.0-flash"
    LLM_API_BASE: Optional[str] = None
    
    class Config:
        # Support .env one level up (local dev) OR in backend dir (production)
        env_file = [".env", "../.env"]
        env_file_encoding = "utf-8"

settings = Settings()
