import os
import shutil
import tempfile
from urllib.parse import urlparse
from git import Repo

class IngestionService:
    def __init__(self, workspace_dir: str = "/tmp/codebase_ai_workspace"):
        self.workspace_dir = workspace_dir
        os.makedirs(self.workspace_dir, exist_ok=True)

    def is_valid_github_url(self, url: str) -> bool:
        parsed = urlparse(url)
        if parsed.netloc not in ["github.com", "www.github.com"]:
            return False
        parts = parsed.path.strip("/").split("/")
        if len(parts) < 2:
            return False
        return True

    def clone_repository(self, url: str, repo_id: str) -> str:
        """Clones the repository and returns the path to the cloned directory."""
        if url.startswith("local://"):
            return url.replace("local://", "")
            
        if not self.is_valid_github_url(url):
            raise ValueError(f"Invalid GitHub URL: {url}")
        
        target_dir = os.path.join(self.workspace_dir, repo_id)
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        
        Repo.clone_from(url, target_dir, depth=1)
        return target_dir

    def filter_files(self, repo_path: str) -> list[str]:
        """Filters out non-essential files from the repository."""
        relevant_files = []
        ignore_dirs = {".git", "node_modules", "venv", "dist", "build", "coverage", "__pycache__"}
        valid_extensions = {
            ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".c", ".cpp", ".h", ".hpp", ".go",
            ".json", ".txt", ".toml", ".xml", ".mod", ".example"
        }
        valid_files = {
            "package.json", "requirements.txt", "pyproject.toml", "pom.xml", "go.mod", 
            "dockerfile", "docker-compose.yml", "tsconfig.json", ".env.example"
        }
        
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                is_valid_ext = ext in valid_extensions
                is_valid_file = file.lower() in valid_files
                if is_valid_ext or is_valid_file:
                    rel_path = os.path.relpath(os.path.join(root, file), repo_path)
                    relevant_files.append(rel_path)
                    
        return relevant_files
