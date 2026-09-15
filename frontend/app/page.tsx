"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [repoUrl, setRepoUrl] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  const handleAnalyze = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!repoUrl.includes("github.com") && !repoUrl.startsWith("local://")) {
      setError("Please enter a valid GitHub repository URL or local path.");
      return;
    }
    setError("");
    setIsLoading(true);

    const API_URL = process.env.NEXT_PUBLIC_API_URL || "";

    try {
      const res = await fetch(`${API_URL}/api/repositories`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ repository_url: repoUrl }),
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => null);
        throw new Error(errData?.detail || "Failed to start indexing");
      }

      const data = await res.json();
      router.push(`/dashboard?id=${data.repository_id}`);
    } catch (err: any) {
      if (err.message === "Failed to fetch" || err.message === "Load failed") {
        setError("Network error: Could not connect to the backend API.");
      } else {
        setError(`Repository analysis failed: ${err.message}`);
      }
      setIsLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-zinc-950 text-white">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <div className="text-center space-y-8">
          <h1 className="text-6xl font-bold tracking-tight bg-gradient-to-r from-blue-400 to-indigo-400 text-transparent bg-clip-text">
            Codebase AI
          </h1>
          <p className="text-xl text-zinc-400 max-w-2xl mx-auto">
            Ask questions about unfamiliar repositories and get grounded answers with the exact code behind them.
          </p>
          
          <form onSubmit={handleAnalyze} className="max-w-xl mx-auto flex flex-col gap-4 mt-12">
            <input
              type="text"
              placeholder="https://github.com/username/repository"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              className="w-full px-4 py-3 rounded-lg bg-zinc-900 border border-zinc-800 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              disabled={isLoading}
            />
            {error && <p className="text-red-400 text-sm text-left">{error}</p>}
            
            <button
              type="submit"
              disabled={isLoading || !repoUrl}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-4 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? "Analyzing..." : "Analyze Repository"}
            </button>
          </form>
        </div>
      </div>
    </main>
  );
}
