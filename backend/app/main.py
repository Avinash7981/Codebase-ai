from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import router
app = FastAPI(title="Codebase AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local emergency demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}

