import sqlite3
import os
import uuid
import datetime

os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data"), exist_ok=True)
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "codebase_ai.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS repositories (
            id TEXT PRIMARY KEY,
            url TEXT,
            status TEXT,
            progress INTEGER,
            files_processed INTEGER,
            total_files INTEGER,
            chunks_created INTEGER,
            message TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

class RepoRecord:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            UPDATE repositories SET 
            status=?, progress=?, files_processed=?, total_files=?, chunks_created=?, message=?
            WHERE id=?
        """, (self.status, self.progress, self.files_processed, self.total_files, self.chunks_created, self.message, self.id))
        conn.commit()
        conn.close()

def create_repo(url: str) -> RepoRecord:
    repo_id = str(uuid.uuid4())
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO repositories (id, url, status, progress, files_processed, total_files, chunks_created, message, created_at)
        VALUES (?, ?, 'pending', 0, 0, 0, 0, '', ?)
    """, (repo_id, url, datetime.datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return get_repo(repo_id)

def get_repo(repo_id: str) -> RepoRecord:
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM repositories WHERE id=?", (repo_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return None
    return RepoRecord(**dict(row))

# Fake dependency to replace get_db
async def get_db():
    return None
