"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import CodeViewer from "@/components/CodeViewer";
import { Send, Terminal, Database, ArrowRight, Activity, Code, FileText, Layers } from "lucide-react";

export default function Dashboard() {
  const params = useParams();
  const repoId = params.id as string;
  
  const [status, setStatus] = useState<any>(null);
  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState<{role: string, content: string, sources?: any[]}[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [selectedSource, setSelectedSource] = useState<any>(null);
  
  useEffect(() => {
    // Poll for status
    const interval = setInterval(async () => {
      try {
        const res = await fetch(`http://localhost:8000/api/repositories/${repoId}/status`, {
          cache: "no-store",
          headers: {
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
          }
        });
        if (res.ok) {
          const data = await res.json();
          setStatus(data);
          if (data.status === "completed" || data.status === "failed") {
            clearInterval(interval);
          }
        }
      } catch (e) {
        console.error(e);
      }
    }, 2000);
    
    return () => clearInterval(interval);
  }, [repoId]);

  const [showRetry, setShowRetry] = useState(false);
  
  const askQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;
    
    const userQ = question;
    setQuestion("");
    setChat(prev => [...prev, { role: "user", content: userQ }]);
    setIsLoading(true);
    setShowRetry(false);
    
    const retryTimer = setTimeout(() => {
      setShowRetry(true);
    }, 2500);
    
    try {
      const res = await fetch(`http://localhost:8000/api/repositories/${repoId}/query`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userQ }),
      });
      
      const data = await res.json();
      clearTimeout(retryTimer);
      
      setChat(prev => [...prev, { 
        role: "assistant", 
        content: data.answer || "No answer returned.",
        sources: data.sources 
      }]);
    } catch (e: any) {
      clearTimeout(retryTimer);
      setChat(prev => [...prev, { role: "assistant", content: "Error: " + e.message }]);
    } finally {
      setIsLoading(false);
      setShowRetry(false);
    }
  };

  if (!status) {
    return <div className="flex h-screen items-center justify-center bg-zinc-950 text-white">Loading dashboard...</div>;
  }

  if (status.status !== "completed") {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center p-24 bg-zinc-950 text-white font-mono">
        <div className="max-w-xl w-full border border-zinc-800 rounded-xl p-8 bg-zinc-900/50 shadow-2xl">
          <h2 className="text-xl font-bold mb-6 flex items-center gap-3">
            <Activity className="w-5 h-5 text-blue-400 animate-pulse" />
            Understanding your repo
          </h2>
          
          <div className="space-y-4 text-sm text-zinc-300">
            <div className="flex items-center gap-3">
              <span className={status.progress >= 10 ? "text-green-400" : "text-zinc-600"}>✓</span> 
              Repository connected
            </div>
            <div className="flex items-center gap-3">
              <span className={status.progress >= 30 ? "text-green-400" : "text-zinc-600"}>✓</span> 
              Files discovered and filtered
            </div>
            <div className="flex items-center gap-3">
              <span className={status.progress >= 40 ? "text-blue-400" : "text-zinc-600"}>●</span> 
              Parsing code and extracting symbols
            </div>
            <div className="flex items-center gap-3">
              <span className={status.progress >= 70 ? "text-blue-400" : "text-zinc-600"}>○</span> 
              Generating embeddings
            </div>
            <div className="flex items-center gap-3">
              <span className={status.progress >= 100 ? "text-green-400" : "text-zinc-600"}>○</span> 
              AI knowledge ready
            </div>
          </div>
          
          <div className="mt-8">
            <div className="w-full bg-zinc-800 rounded-full h-2 mb-2 overflow-hidden">
              <div className="bg-blue-500 h-2 rounded-full transition-all duration-500 ease-out" style={{ width: `${status.progress}%` }}></div>
            </div>
            <div className="flex justify-between text-xs text-zinc-500 font-mono">
              <span>{status.progress}%</span>
              <span>{status.files_processed} / {status.total_files} files • {status.chunks_created} chunks</span>
            </div>
          </div>
          
          {status.status === "failed" && (
            <div className="mt-6 p-4 bg-red-500/10 border border-red-500/20 rounded-lg text-red-400 text-sm">
              Error: {status.message}
            </div>
          )}
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen bg-zinc-950 text-zinc-200 overflow-hidden font-sans">
      {/* Left Sidebar - Chat */}
      <div className="w-1/3 flex flex-col border-r border-zinc-800 bg-zinc-950">
        <div className="p-4 border-b border-zinc-800 flex items-center justify-between">
          <h1 className="font-semibold text-lg bg-gradient-to-r from-blue-400 to-indigo-400 text-transparent bg-clip-text">Codebase AI</h1>
          <div className="text-xs text-zinc-500 font-mono flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-green-500 inline-block"></span>
            Indexed
          </div>
        </div>
        
        <div className="flex-1 overflow-y-auto p-4 space-y-6 scrollbar-thin scrollbar-thumb-zinc-800">
          {chat.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center space-y-4 opacity-50">
              <Terminal className="w-12 h-12 text-zinc-600" />
              <p className="text-sm">Ask anything about this repository...</p>
              <div className="flex flex-col gap-2 mt-4 text-xs">
                <button onClick={() => setQuestion("Where is authentication handled?")} className="px-3 py-2 bg-zinc-900 rounded border border-zinc-800 hover:bg-zinc-800 text-left">"Where is authentication handled?"</button>
                <button onClick={() => setQuestion("How does login work?")} className="px-3 py-2 bg-zinc-900 rounded border border-zinc-800 hover:bg-zinc-800 text-left">"How does login work?"</button>
              </div>
            </div>
          ) : (
            chat.map((msg, i) => (
              <div key={i} className={`flex flex-col ${msg.role === "user" ? "items-end" : "items-start"}`}>
                <div className={`max-w-[85%] rounded-2xl px-4 py-3 ${
                  msg.role === "user" 
                    ? "bg-blue-600 text-white" 
                    : "bg-zinc-900 border border-zinc-800 text-zinc-300 leading-relaxed"
                }`}>
                  <p className="whitespace-pre-wrap text-sm">{msg.content}</p>
                </div>
                
                {msg.sources && msg.sources.length > 0 && (
                  <div className="mt-3 w-full bg-zinc-900/50 border border-zinc-800 rounded-xl p-3">
                    <h4 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-2 flex items-center gap-2">
                      <FileText className="w-3 h-3" /> Sources
                    </h4>
                    <div className="space-y-2">
                      {msg.sources.map((src, idx) => (
                        <button 
                          key={idx}
                          onClick={() => setSelectedSource(src)}
                          className="w-full text-left p-2 rounded hover:bg-zinc-800 border border-transparent hover:border-zinc-700 transition-colors flex items-start gap-3 group"
                        >
                          <Code className="w-4 h-4 text-zinc-500 mt-0.5 group-hover:text-blue-400" />
                          <div className="overflow-hidden">
                            <div className="text-sm font-medium text-zinc-300 truncate">{src.symbol_name}</div>
                            <div className="text-xs text-zinc-500 font-mono truncate">{src.file_path} : {src.start_line}-{src.end_line}</div>
                          </div>
                        </button>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))
          )}
          {isLoading && (
            <div className="flex flex-col items-start space-y-2">
              <div className="bg-zinc-900 border border-zinc-800 rounded-2xl px-4 py-3 text-zinc-400 text-sm flex items-center gap-2">
                <div className="w-1.5 h-1.5 rounded-full bg-zinc-500 animate-bounce"></div>
                <div className="w-1.5 h-1.5 rounded-full bg-zinc-500 animate-bounce" style={{ animationDelay: "0.15s" }}></div>
                <div className="w-1.5 h-1.5 rounded-full bg-zinc-500 animate-bounce" style={{ animationDelay: "0.3s" }}></div>
              </div>
              {showRetry && (
                <div className="text-xs text-yellow-500/80 animate-pulse px-2">
                  AI provider temporarily unavailable. Retrying...
                </div>
              )}
            </div>
          )}
        </div>
        
        <div className="p-4 border-t border-zinc-800 bg-zinc-950">
          <form onSubmit={askQuestion} className="relative">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask a question..."
              className="w-full bg-zinc-900 border border-zinc-800 rounded-xl py-3 pl-4 pr-12 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 text-white"
              disabled={isLoading}
            />
            <button 
              type="submit" 
              disabled={isLoading || !question.trim()}
              className="absolute right-2 top-2 p-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg disabled:opacity-50 transition-colors"
            >
              <Send className="w-4 h-4" />
            </button>
          </form>
        </div>
      </div>
      
      {/* Right Sidebar - Code / Explorer */}
      <div className="flex-1 bg-zinc-950 flex flex-col p-4 pl-0">
        <div className="flex-1 rounded-xl overflow-hidden border border-zinc-800 shadow-2xl bg-zinc-900 flex flex-col">
          {selectedSource ? (
            <CodeViewer 
              code={selectedSource.source_code || "// Source code not loaded in preview mode yet"} 
              language={selectedSource.file_path.split('.').pop() || "ts"}
              highlightLines={[selectedSource.start_line, selectedSource.end_line]}
              filePath={selectedSource.file_path}
            />
          ) : (
            <div className="h-full flex flex-col items-center justify-center text-zinc-500 p-8 text-center space-y-6">
              <div className="w-24 h-24 rounded-2xl bg-zinc-800/50 flex items-center justify-center mb-4 border border-zinc-800 shadow-inner">
                <Layers className="w-10 h-10 text-zinc-600" />
              </div>
              <h3 className="text-xl font-medium text-zinc-300">Repository Explorer</h3>
              <p className="max-w-md text-sm leading-relaxed">
                Ask a question about the repository in the chat panel. 
                Click on any of the source citations in the AI's response to open the exact code here.
              </p>
              
              <div className="grid grid-cols-2 gap-4 mt-8 w-full max-w-lg text-left">
                <div className="bg-zinc-950/50 p-4 rounded-xl border border-zinc-800">
                  <Database className="w-5 h-5 text-indigo-400 mb-2" />
                  <div className="text-sm font-medium text-zinc-300">Semantic Search</div>
                  <div className="text-xs text-zinc-500 mt-1">Powered by local BGE embeddings</div>
                </div>
                <div className="bg-zinc-950/50 p-4 rounded-xl border border-zinc-800">
                  <Code className="w-5 h-5 text-emerald-400 mb-2" />
                  <div className="text-sm font-medium text-zinc-300">Tree-sitter</div>
                  <div className="text-xs text-zinc-500 mt-1">AST-based chunking & parsing</div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
