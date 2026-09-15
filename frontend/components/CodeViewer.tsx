"use client";

import Editor from "@monaco-editor/react";

interface CodeViewerProps {
  code: string;
  language: string;
  highlightLines?: [number, number]; // [start, end]
  filePath?: string;
}

export default function CodeViewer({ code, language, highlightLines, filePath }: CodeViewerProps) {
  // Map common languages to monaco equivalents
  const langMap: Record<string, string> = {
    ts: "typescript",
    tsx: "typescript",
    js: "javascript",
    jsx: "javascript",
    py: "python",
    go: "go",
    java: "java",
    c: "c",
    cpp: "cpp",
  };

  const getLang = (lang: string) => langMap[lang] || lang;

  return (
    <div className="flex flex-col h-full w-full rounded-md overflow-hidden border border-zinc-800 bg-zinc-950">
      {filePath && (
        <div className="flex items-center justify-between px-4 py-2 bg-zinc-900 border-b border-zinc-800 text-xs text-zinc-400 font-mono">
          <span>{filePath}</span>
          <span>{getLang(language)}</span>
        </div>
      )}
      <div className="flex-1 relative">
        <Editor
          height="100%"
          language={getLang(language)}
          theme="vs-dark"
          value={code}
          options={{
            readOnly: true,
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            fontSize: 13,
            padding: { top: 16, bottom: 16 },
            lineNumbers: "on",
            renderLineHighlight: "all",
          }}
          onMount={(editor, monaco) => {
            if (highlightLines) {
              const [start, end] = highlightLines;
              editor.revealLineInCenter(start);
              
              // We could use decorations to highlight the specific line range
              editor.createDecorationsCollection([
                {
                  range: new monaco.Range(start, 1, end, 1),
                  options: {
                    isWholeLine: true,
                    className: "bg-blue-500/20",
                    marginClassName: "bg-blue-500/50",
                  }
                }
              ]);
            }
          }}
        />
      </div>
    </div>
  );
}
