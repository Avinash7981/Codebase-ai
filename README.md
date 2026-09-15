UPDATE README.md — FINAL HACKATHON VERSION

Replace the current README.md with a polished, professional, complete README for Codebase AI.

IMPORTANT:
- Do not change application code.
- Do not change functionality.
- Only update README.md.
- Include the live demo link prominently.
- Make the README suitable for hackathon judges.
- Clearly explain the problem, solution, architecture, workflow, tech stack, setup, API flow, features, security, limitations, and future scope.
- Do not claim features that are not implemented.
- Current deployed demo uses Gemini for LLM generation.
- Keep the documentation technically accurate.

LIVE DEMO:
https://codebase-ai-1.onrender.com

GITHUB:
https://github.com/Avinash7981/Codebase-ai

Use the following README content:

# 🚀 Codebase AI

> **Understand any unfamiliar codebase using AI — with answers grounded in the actual source code.**

[🚀 Live Demo](https://codebase-ai-1.onrender.com) • [💻 GitHub](https://github.com/Avinash7981/Codebase-ai)

---

## 📌 Problem Statement

Understanding an unfamiliar codebase is one of the biggest challenges for developers.

When joining an existing project, developers often spend hours:

- Searching through hundreds of files
- Finding where a feature is implemented
- Understanding relationships between classes and functions
- Tracing how requests flow through the application
- Understanding unfamiliar modules
- Identifying the exact code responsible for a behavior

Traditional keyword search is not enough because developers ask questions in natural language such as:

> "Where is authentication handled?"

> "How does login work?"

> "Where is this API request processed?"

> "What happens when a new session is created?"

The challenge is not simply finding text.

The challenge is **understanding the codebase.**

---

# 💡 Proposed Solution

## Codebase AI

Codebase AI is an AI-powered codebase intelligence platform that allows developers to connect a GitHub repository and ask natural-language questions about its implementation.

Instead of generating generic answers, Codebase AI retrieves relevant source code from the repository and uses that context to generate grounded answers.

Every answer can be connected back to:

- File
- Symbol
- Function/Class
- Line range
- Actual source code

### Core Principle

> **Find → Understand → Prove**

Codebase AI doesn't just tell developers what the code does.

It shows them **where the answer came from.**

---

# 🎯 Key Features

### 🔗 GitHub Repository Ingestion

Connect a GitHub repository and automatically analyze its source code.

The system:

1. Clones the repository
2. Filters irrelevant files
3. Parses source code
4. Extracts meaningful symbols
5. Creates semantic chunks
6. Generates embeddings
7. Stores searchable representations

---

### 🧠 Semantic Code Search

Developers can ask questions using natural language.

Example:

```text
Where is authentication handled?
