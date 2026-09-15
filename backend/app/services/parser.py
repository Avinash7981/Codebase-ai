try:
    from tree_sitter_languages import get_language, get_parser
    HAS_TREESITTER = True
except ImportError:
    HAS_TREESITTER = False

from typing import Dict, Any, List, Optional
import os
import re

class CodeParser:
    def __init__(self):
        self.is_fallback = not HAS_TREESITTER
        if not self.is_fallback:
            self.ext_to_lang = {
                ".py": "python",
                ".js": "javascript",
                ".jsx": "javascript",
                ".ts": "typescript",
                ".tsx": "tsx",
                ".java": "java",
                ".c": "c",
                ".cpp": "cpp",
                ".h": "cpp",
                ".hpp": "cpp",
                ".go": "go"
            }
            
            self.parsers = {}
            for lang_name in set(self.ext_to_lang.values()):
                try:
                    lang = get_language(lang_name)
                    parser = get_parser(lang_name)
                    self.parsers[lang_name] = parser
                except Exception as e:
                    print(f"Failed to load parser for {lang_name}: {e}")
        else:
            print("WARNING: Tree-sitter unavailable. Using regex-based fallback parser.")

    def parse_file(self, file_path: str, repo_path: str) -> List[Dict[str, Any]]:
        """Parses a file and extracts meaningful semantic units (functions, classes)."""
        full_path = os.path.join(repo_path, file_path)
        ext = os.path.splitext(file_path)[1].lower()
        
        with open(full_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
            
        if self.is_fallback:
            return self._regex_extract(source_code, file_path, ext)
            
        lang_name = self.ext_to_lang.get(ext)
        if not lang_name or lang_name not in self.parsers:
            return []
            
        parser = self.parsers[lang_name]
        tree = parser.parse(bytes(source_code, "utf8"))
        
        symbols = []
        self._extract_symbols(tree.root_node, source_code, file_path, lang_name, symbols)
        return symbols

    def _regex_extract(self, source_code: str, file_path: str, ext: str) -> List[Dict[str, Any]]:
        symbols = []
        lines = source_code.split('\n')
        # Naive fallback for python defs
        for i, line in enumerate(lines):
            match = re.match(r'^\s*(def|class)\s+([a-zA-Z0-9_]+)', line)
            if match:
                symbols.append({
                    "symbol_name": match.group(2),
                    "symbol_type": "function" if match.group(1) == "def" else "class",
                    "parent_symbol": None,
                    "start_line": i + 1,
                    "end_line": min(i + 15, len(lines)),
                    "source_code": "\n".join(lines[i:i+15]),
                    "file_path": file_path,
                    "language": ext[1:]
                })
        return symbols

    def _extract_symbols(self, node, source_code: str, file_path: str, lang_name: str, symbols: List[Dict[str, Any]], parent_symbol: Optional[str] = None):
        """Recursively traverse the AST to extract symbols."""
        # This is a simplified extraction logic. A robust implementation would use Tree-sitter queries.
        
        is_symbol = False
        symbol_name = None
        symbol_type = None
        
        # Very basic naive heuristic for detecting functions/classes based on node types
        node_type = node.type
        
        if node_type in ["function_definition", "method_definition", "arrow_function", "function_declaration", "method_declaration"]:
            symbol_type = "function"
            is_symbol = True
        elif node_type in ["class_definition", "class_declaration", "type_declaration"]:
            symbol_type = "class"
            is_symbol = True
            
        if is_symbol:
            # Try to find the name identifier
            # Typically it's a child node named 'identifier' or 'name'
            for child in node.children:
                if child.type in ["identifier", "name", "property_identifier", "type_identifier"]:
                    symbol_name = source_code[child.start_byte:child.end_byte]
                    break
            
            if symbol_name:
                start_line = node.start_point[0] + 1
                end_line = node.end_point[0] + 1
                symbol_code = source_code[node.start_byte:node.end_byte]
                
                symbols.append({
                    "symbol_name": symbol_name,
                    "symbol_type": symbol_type,
                    "parent_symbol": parent_symbol,
                    "start_line": start_line,
                    "end_line": end_line,
                    "source_code": symbol_code,
                    "file_path": file_path,
                    "language": lang_name
                })
                parent_symbol = symbol_name

        # Recurse into children
        for child in node.children:
            self._extract_symbols(child, source_code, file_path, lang_name, symbols, parent_symbol)
