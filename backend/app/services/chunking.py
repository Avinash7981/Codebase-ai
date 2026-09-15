from typing import Dict, Any, List
import uuid

class ChunkingService:
    def __init__(self, max_chunk_size: int = 1500):
        self.max_chunk_size = max_chunk_size

    def chunk_symbols(self, symbols: List[Dict[str, Any]], repo_id: str) -> List[Dict[str, Any]]:
        """
        Takes extracted symbols and creates semantic chunks.
        For MVP, we treat each function/class as a chunk unless it's too large.
        """
        chunks = []
        for symbol in symbols:
            source = symbol["source_code"]
            
            if len(source) <= self.max_chunk_size:
                chunks.append(self._create_chunk_dict(symbol, repo_id, source))
            else:
                # Naive splitting for very large symbols
                # A more advanced version would split by AST nodes
                lines = source.split("\n")
                current_chunk_lines = []
                current_size = 0
                
                for line in lines:
                    if current_size + len(line) > self.max_chunk_size and current_chunk_lines:
                        chunk_text = "\n".join(current_chunk_lines)
                        chunks.append(self._create_chunk_dict(symbol, repo_id, chunk_text))
                        current_chunk_lines = []
                        current_size = 0
                        
                    current_chunk_lines.append(line)
                    current_size += len(line) + 1 # +1 for newline
                    
                if current_chunk_lines:
                    chunk_text = "\n".join(current_chunk_lines)
                    chunks.append(self._create_chunk_dict(symbol, repo_id, chunk_text))
                    
        return chunks
        
    def _create_chunk_dict(self, symbol: Dict[str, Any], repo_id: str, text: str) -> Dict[str, Any]:
        return {
            "chunk_id": str(uuid.uuid4()),
            "repository_id": repo_id,
            "file_path": symbol["file_path"],
            "symbol_name": symbol["symbol_name"],
            "symbol_type": symbol["symbol_type"],
            "parent_symbol": symbol["parent_symbol"],
            "start_line": symbol["start_line"],
            "end_line": symbol["end_line"],
            "language": symbol["language"],
            "source_code": text
        }
