# 🚀 Codebase AI – AI-Powered Codebase Intelligence Platform

> An intelligent AI-powered developer assistant that understands unfamiliar Git repositories, answers natural-language questions about the codebase, and provides exact source-code references.

Codebase AI transforms a Git repository into an intelligent, searchable code knowledge base.

Instead of manually searching through hundreds or thousands of files, developers can simply ask questions such as:

- "Where is authentication handled?"
- "How does the login flow work?"
- "Where is the Session class implemented?"
- "Which function validates the password?"
- "What does this service do?"

The system retrieves the most relevant code, uses an LLM to explain it, and provides precise file, symbol, and line references that can be opened directly in the integrated code viewer.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [Key Features](#-key-features)
- [Why Codebase AI?](#-why-codebase-ai)
- [How It Works](#-how-it-works)
- [System Architecture](#-system-architecture)
- [Indexing Pipeline](#-indexing-pipeline)
- [RAG Query Pipeline](#-rag-query-pipeline)
- [Hybrid Retrieval](#-hybrid-retrieval)
- [AI Grounding](#-ai-grounding)
- [Source Citations](#-source-citations)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Request Flow](#-request-flow)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Running the Project](#-running-the-project)
- [Example Queries](#-example-queries)
- [Security](#-security)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

# 📖 Overview

Modern software repositories can contain thousands of files and millions of lines of code.

Understanding an unfamiliar codebase often requires developers to:

- Search through multiple files
- Identify important classes and functions
- Understand dependencies
- Trace execution flows
- Find authentication logic
- Locate database operations
- Understand API implementations
- Ask senior developers for guidance

Codebase AI solves this problem by allowing developers to **ask the codebase itself**.

The platform accepts a Git repository, analyzes its source code, creates searchable representations of meaningful code structures, and uses Retrieval-Augmented Generation (RAG) to answer developer questions.

### Core Promise

> **Give us an unfamiliar repository. Ask where something lives or how it works. Codebase AI finds the relevant code, explains it, and shows exactly where the answer came from.**

---

# ❗ Problem Statement

Developers working with unfamiliar repositories spend significant time understanding existing code.

Traditional approaches rely heavily on:

```text
Manual File Search
        ↓
Keyword Search
        ↓
Open Multiple Files
        ↓
Understand Functions
        ↓
Trace Dependencies
        ↓
Understand Architecture
