import uuid
from sqlalchemy import Column, String, DateTime, Integer, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class Repository(Base):
    __tablename__ = "repositories"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url = Column(String, nullable=False)
    status = Column(String, default="pending")
    progress = Column(Integer, default=0)
    files_processed = Column(Integer, default=0)
    total_files = Column(Integer, default=0)
    chunks_created = Column(Integer, default=0)
    message = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
