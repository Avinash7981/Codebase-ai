from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
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

# Setup frontend static file serving
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "out")

if os.path.exists(frontend_dir):
    # Mount Next.js static assets
    app.mount("/_next", StaticFiles(directory=os.path.join(frontend_dir, "_next")), name="next_assets")
    
    # Catch-all route to serve the SPA
    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # Prevent path traversal
        if ".." in full_path:
            return FileResponse(os.path.join(frontend_dir, "index.html"))
            
        file_path = os.path.join(frontend_dir, full_path)
        
        # If specific file requested exists (like favicon.ico)
        if full_path and os.path.isfile(file_path):
            return FileResponse(file_path)
            
        # Next.js static export generates .html files for routes
        if full_path and os.path.isfile(file_path + ".html"):
            return FileResponse(file_path + ".html")
            
        # Fallback to SPA index
        if full_path == "dashboard":
            return FileResponse(os.path.join(frontend_dir, "dashboard.html"))
            
        return FileResponse(os.path.join(frontend_dir, "index.html"))

