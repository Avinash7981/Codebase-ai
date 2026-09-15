from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Default to sqlite for hackathon-friendly local running if no postgres is available
    DATABASE_URL: str = "sqlite+aiosqlite:///./codebase.db"
    
    # Empty QDRANT_URL means use local file-based storage
    QDRANT_URL: str = ""
    QDRANT_PATH: str = "./qdrant_data"
    
    LLM_PROVIDER: str = "openai"
    LLM_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    LLM_MODEL: str = "gpt-4o-mini"
    LLM_API_BASE: Optional[str] = None
    
    class Config:
        env_file = "../.env"

settings = Settings()
