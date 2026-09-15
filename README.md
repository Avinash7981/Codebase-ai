AHAHA reyy 😭 now I understood exactly what you want. You don’t want just the beginning. You want a complete A–Z README that a judge can open and understand the entire project:

PS → Problem → Proposed Solution → Features → Workflow → Flowcharts → Architecture → RAG → Retrieval → Embeddings → Database → LLM → Citations → Tech Stack → Folder Structure → Installation → Environment → Run → Demo → Security → Limitations → Future Scope → Author.

Below is the full README.md you can directly replace your current README with.

⸻

🚀 Codebase AI – AI-Powered Codebase Intelligence Platform

Understand any unfamiliar Git repository using natural language. Find the right code, understand how it works, and jump directly to the exact source behind the answer.

Codebase AI is an AI-powered developer assistant that transforms an unfamiliar Git repository into an intelligent, searchable code knowledge base.

Instead of manually searching through hundreds or thousands of files, developers can ask questions such as:

* “Where is authentication handled?”
* “How does the login flow work?”
* “Where is the Session class implemented?”
* “Which function validates the password?”
* “How are HTTP requests handled?”
* “What does this service do?”

Codebase AI analyzes the repository, extracts meaningful code structures, creates searchable representations, retrieves the most relevant code, and uses an LLM to generate a grounded explanation.

Every answer is connected to exact source files, symbols, and line ranges, which can be opened directly inside the integrated CodeViewer.

⸻

📑 Table of Contents

* Overview⁠￼
* Problem Statement⁠￼
* Proposed Solution⁠￼
* Core Idea⁠￼
* Key Features⁠￼
* Why Codebase AI⁠￼
* How It Works⁠￼
* System Architecture⁠￼
* Complete System Flow⁠￼
* Repository Ingestion Pipeline⁠￼
* Code Parsing⁠￼
* Semantic Chunking⁠￼
* Embedding Generation⁠￼
* Vector Storage⁠￼
* RAG Query Pipeline⁠￼
* Hybrid Retrieval⁠￼
* Context Construction⁠￼
* AI Grounding⁠￼
* Source Citations⁠￼
* CodeViewer⁠￼
* Technology Stack⁠￼
* Project Structure⁠￼
* Data Model⁠￼
* API Flow⁠￼
* Installation⁠￼
* Environment Variables⁠￼
* Running the Application⁠￼
* Using Codebase AI⁠￼
* Example Queries⁠￼
* Demo Workflow⁠￼
* Security⁠￼
* Error Handling⁠￼
* Performance⁠￼
* Current Limitations⁠￼
* Future Improvements⁠￼
* Hackathon Impact⁠￼
* Contributing⁠￼
* License⁠￼
* Author⁠￼

⸻

📖 Overview

Modern software repositories can contain:

* Thousands of files
* Millions of lines of code
* Multiple programming languages
* Complex dependencies
* Deeply nested services
* Authentication systems
* Database layers
* API controllers
* Configuration files
* Utility modules

Understanding such a repository manually can take hours or even days.

A developer usually has to:

Find files
    ↓
Search keywords
    ↓
Open multiple files
    ↓
Identify classes/functions
    ↓
Trace dependencies
    ↓
Understand execution flow
    ↓
Build mental model

Codebase AI changes this workflow.

Ask a question
      ↓
AI searches the repository
      ↓
Relevant code is retrieved
      ↓
LLM explains the code
      ↓
Exact sources are shown
      ↓
Developer opens the referenced code

Core Promise

Give us an unfamiliar repository. Ask where something lives or how it works. Codebase AI finds the relevant code, explains it, and shows exactly where the answer came from.

⸻

❗ Problem Statement

The Problem

Developers frequently work with codebases they did not create.

Examples include:

* Joining an existing company project
* Contributing to an open-source repository
* Maintaining legacy systems
* Debugging unfamiliar services
* Onboarding new developers
* Understanding third-party libraries
* Working with large microservice architectures

The traditional approach is slow and fragmented.

Existing Workflow

Developer
    ↓
Search Repository
    ↓
Read Files
    ↓
Find Functions
    ↓
Trace Imports
    ↓
Understand Logic
    ↓
Search Again
    ↓
Ask Senior Developer

This creates several problems:

1. Slow onboarding

New developers can spend hours understanding where functionality lives.

2. Difficult code navigation

Finding the correct implementation is difficult in large repositories.

3. Context switching

Developers continuously switch between files and tools.

4. Weak keyword search

A keyword may appear in dozens of irrelevant files.

5. Lack of architectural understanding

Finding a function is not enough. Developers need to understand how components interact.

6. AI hallucination risk

Generic AI assistants may generate explanations without actually examining the repository.

⸻

💡 Proposed Solution

Codebase AI provides a repository-aware AI assistant.

The system converts a Git repository into a searchable knowledge base.

Git Repository
      ↓
File Filtering
      ↓
Code Parsing
      ↓
Symbol Extraction
      ↓
Semantic Chunking
      ↓
Embeddings
      ↓
Persistent Vector Store
      ↓
Hybrid Retrieval
      ↓
Relevant Code Context
      ↓
LLM
      ↓
Grounded Answer
      ↓
Exact Source Citations
      ↓
CodeViewer

Instead of asking a generic AI:

“How does authentication work?”

the developer asks Codebase AI:

“How does authentication work in this repository?”

The system searches the actual repository and generates an answer using retrieved source code.

⸻

🧠 Core Idea

Codebase AI follows three core principles:

🔎 Find

Locate the most relevant files, functions, classes, and code sections.

🧠 Understand

Use retrieved repository context to explain how the code works.

📍 Prove

Show the exact source code responsible for the answer.

              CODEBASE AI
                   │
          ┌────────┴────────┐
          ↓                 ↓
        FIND             UNDERSTAND
          │                 │
          └────────┬────────┘
                   ↓
                 PROVE
                   │
                   ↓
          Exact Source Code

⸻

✨ Key Features

1. 🔗 Git Repository Ingestion

Users provide a GitHub repository URL.

Codebase AI:

* Validates the repository
* Clones it
* Filters unnecessary files
* Reads supported source code
* Builds an internal code index

⸻

2. 🧹 Intelligent File Filtering

The system ignores unnecessary content such as:

.git/
node_modules/
venv/
dist/
build/
__pycache__/
binary files
generated files
large irrelevant assets

Important configuration files are preserved:

package.json
requirements.txt
pyproject.toml
pom.xml
go.mod
Dockerfile
docker-compose.yml
tsconfig.json
.env.example

⸻

3. 🌳 Code Parsing

The system analyzes source code and extracts meaningful structures.

Examples:

Classes
Functions
Methods
Modules
Imports
Configuration sections

Supported/target languages include:

Python
JavaScript
TypeScript
Java
C
C++
Go

⸻

4. 🧩 Semantic Code Chunking

Instead of splitting code randomly by character count, Codebase AI creates meaningful chunks around code structures.

Example:

Class
 ├── Constructor
 ├── Method A
 ├── Method B
 └── Method C

Each chunk maintains metadata such as:

repository_id
file_path
language
symbol_name
symbol_type
parent_symbol
start_line
end_line
source_code
signature
chunk_id

This makes retrieval more precise.

⸻

5. 🧠 Local Embeddings

Code chunks are converted into numerical representations.

The intended embedding model is:

BAAI/bge-small-en-v1.5

This enables semantic similarity between:

User Question
       ↓
Embedding
       ↓
Compare against code embeddings
       ↓
Relevant chunks

The current hackathon environment also contains a deterministic local fallback so the demo remains functional when heavyweight ML dependencies cannot be downloaded.

⸻

6. 🔍 Hybrid Retrieval

Codebase AI doesn’t depend on one search strategy.

It combines:

Semantic similarity

Finds conceptually related code.

Keyword search

Finds exact terms.

Symbol search

Finds classes/functions/methods.

Structural information

Uses relationships between code components when available.

Conceptually:

                User Query
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
      Semantic   Keyword   Symbol
       Search     Search    Search
          │         │         │
          └─────────┼─────────┘
                    ↓
             Hybrid Ranking
                    ↓
             Relevant Chunks

This is especially useful for code because developers often use exact symbols such as:

Session
authenticate()
validate_password()
PaymentService
create_token()

⸻

7. 💬 RAG-Based Answers

Codebase AI uses Retrieval-Augmented Generation.

The LLM does not simply answer from general knowledge.

Instead:

Question
   ↓
Retrieve Repository Code
   ↓
Build Context
   ↓
Send Context to LLM
   ↓
Generate Answer

This reduces hallucination and keeps answers tied to the actual repository.

⸻

8. 📍 Exact Source Citations

Every answer can contain source references such as:

src/requests/sessions.py
Session
Lines 7–21

The citation metadata contains:

File path
Symbol
Symbol type
Start line
End line
Chunk ID
Source code

⸻

9. 🖥️ Integrated CodeViewer

Clicking a source citation opens the referenced code.

The CodeViewer:

* Opens the correct file
* Displays source code
* Jumps to the referenced lines
* Highlights the relevant range

This creates a direct connection:

AI Explanation
      ↓
Citation
      ↓
Exact Source

⸻

10. 🔄 Persistent Index

The indexed repository is stored locally.

This means the system can preserve:

Repository
Files
Chunks
Embeddings
Metadata

and retrieve them after a backend restart without necessarily re-ingesting the repository.

⸻

🎯 Why Codebase AI?

Traditional code search answers:

“Where does this word appear?”

Codebase AI answers:

“Where is this functionality implemented, how does it work, and what exact code proves it?”

Traditional Search

Search "authentication"
        ↓
100 results
        ↓
Developer manually investigates

Codebase AI

"Where is authentication handled?"
        ↓
Relevant code retrieved
        ↓
AI explanation
        ↓
Exact source citation
        ↓
Open code

⸻

⚙️ How It Works

The platform has two major pipelines:

┌───────────────────────────────┐
│       INDEXING PIPELINE       │
│                               │
│ GitHub → Parse → Chunk →      │
│ Embed → Store                 │
└───────────────┬───────────────┘
                │
                ↓
        Code Knowledge Base
                │
                ↓
┌───────────────────────────────┐
│         QUERY PIPELINE        │
│                               │
│ Question → Retrieve → Context │
│ → LLM → Answer → Citation     │
└───────────────────────────────┘

⸻

🏗️ System Architecture

flowchart TB
    USER[👤 Developer]
    FRONTEND[🖥️ Next.js Frontend]
    API[⚡ FastAPI Backend]
    INGEST[📥 Repository Ingestion]
    FILTER[🧹 File Filtering]
    PARSER[🌳 Code Parser]
    CHUNK[🧩 Semantic Chunking]
    EMBED[🧠 Embedding Service]
    STORE[(🗄️ Persistent Local Vector Store)]
    RETRIEVE[🔍 Hybrid Retrieval]
    CONTEXT[📦 Context Builder]
    LLM[🤖 Gemini / OpenAI LLM]
    CITE[📍 Citation Generator]
    VIEWER[🖥️ Monaco CodeViewer]
    USER --> FRONTEND
    FRONTEND --> API
    API --> INGEST
    INGEST --> FILTER
    FILTER --> PARSER
    PARSER --> CHUNK
    CHUNK --> EMBED
    EMBED --> STORE
    API --> RETRIEVE
    RETRIEVE --> STORE
    RETRIEVE --> CONTEXT
    CONTEXT --> LLM
    LLM --> CITE
    CITE --> FRONTEND
    FRONTEND --> VIEWER

⸻

🔄 Complete System Flow

flowchart LR
A[GitHub URL]
--> B[Validate Repository]
B --> C[Clone Repository]
C --> D[Filter Files]
D --> E[Parse Source Code]
E --> F[Extract Symbols]
F --> G[Create Semantic Chunks]
G --> H[Generate Embeddings]
H --> I[(Persistent Vector Store)]
J[User Question]
--> K[Query Processing]
K --> L[Semantic Search]
K --> M[Keyword Search]
K --> N[Symbol Search]
L --> O[Hybrid Ranking]
M --> O
N --> O
O --> P[Context Builder]
P --> Q[LLM]
Q --> R[Grounded Answer]
R --> S[Source Citations]
S --> T[CodeViewer]

⸻

📥 Repository Ingestion Pipeline

When a repository is submitted:

Step 1 — URL validation

The backend verifies that the repository exists.

Step 2 — Clone

The repository is cloned into a temporary working directory.

Step 3 — File filtering

Unnecessary files and directories are removed from processing.

Step 4 — Parsing

Source files are analyzed.

Step 5 — Symbol extraction

The system identifies:

Classes
Functions
Methods
Imports
Modules

Step 6 — Chunking

Meaningful code units are converted into searchable chunks.

Step 7 — Embeddings

Each chunk receives a vector representation.

Step 8 — Storage

Chunks, metadata, and vectors are persisted.

Step 9 — Ready

The repository becomes searchable.

⸻

🌳 Code Parsing

The intended parser architecture is AST-aware.

Conceptually:

Source File
    ↓
Parser
    ↓
Abstract Syntax Tree
    ↓
Symbols
    ├── Classes
    ├── Functions
    ├── Methods
    ├── Imports
    └── Modules

For example:

class Session:
    def __init__(self):
        self.headers = {}
        self.cookies = {}
    def request(self, method, url):
        ...

can become:

Chunk 1
Session.__init__
Chunk 2
Session.request

This is much more useful than blindly splitting the file every N characters.

⸻

🧩 Semantic Chunking

A chunk contains both code and metadata.

Example:

{
  "chunk_id": "chunk_123",
  "repository_id": "repo_001",
  "file_path": "src/requests/sessions.py",
  "language": "python",
  "symbol_name": "Session",
  "symbol_type": "class",
  "start_line": 7,
  "end_line": 21
}

This metadata later becomes the source citation.

⸻

🧠 Embedding Generation

Embeddings transform code into numerical vectors.

Code Chunk
    ↓
Embedding Model
    ↓
[0.12, -0.04, 0.73, ...]

The user’s question is also transformed:

"Where is HTTP session management?"
            ↓
       Query Vector
            ↓
     Similarity Search
            ↓
Relevant Code Chunks

Primary embedding model

BAAI/bge-small-en-v1.5

Demo fallback

Because heavyweight ML dependencies can be difficult to install in restricted environments, the current implementation supports a deterministic local fallback.

This keeps the architecture operational without falsely requiring a network download during the demo.

⸻

🗄️ Vector Storage

The application uses a persistent local vector-search implementation for the current hackathon environment.

It stores:

Repository metadata
File metadata
Code chunks
Embeddings
Symbol information
Source locations

The storage layer is intentionally isolated behind a service interface so that a production deployment can replace the local implementation with a dedicated vector database such as Qdrant.

⸻

🔍 RAG Query Pipeline

When a developer asks:

“Where is the Session class implemented?”

the system performs:

Question
   ↓
Normalize Query
   ↓
Generate Query Representation
   ↓
Semantic Search
   ↓
Keyword Search
   ↓
Symbol Search
   ↓
Hybrid Ranking
   ↓
Top Relevant Chunks
   ↓
Context Builder
   ↓
LLM
   ↓
Grounded Answer

⸻

🔀 Hybrid Retrieval

Code retrieval combines multiple signals.

Semantic Score

Measures conceptual similarity.

Keyword Score

Measures exact term matches.

Symbol Score

Prioritizes matching classes/functions.

Structural Score

Can prioritize related code structures.

Conceptual ranking:

Final Score =
    Semantic Score
    +
    Keyword Score
    +
    Symbol Score
    +
    Structural Score

This allows queries such as:

"Session"
"authentication"
"password validation"
"HTTP request flow"
"database connection"

to retrieve useful source code even when the exact wording differs.

⸻

📦 Context Construction

Retrieved chunks are not blindly passed to the LLM.

The context builder:

* Removes duplicates
* Groups related chunks
* Preserves file paths
* Preserves symbols
* Preserves line ranges
* Includes useful relationships
* Controls context size

Example:

Context
1. src/requests/sessions.py
   Session.__init__
   Lines 7–21
2. src/requests/api.py
   request()
   Lines 45–72
3. src/requests/models.py
   Request
   Lines 10–30

⸻

🤖 AI Grounding

The LLM is instructed to answer using repository context.

Important grounding rules:

Use provided repository context.
Do not invent files.
Do not invent functions.
Do not invent classes.
Do not invent relationships.
Do not claim code exists without evidence.
If evidence is insufficient:
say that there is insufficient evidence.

This makes the assistant more trustworthy for software engineering tasks.

⸻

📍 Source Citations

Each answer can be connected to a source.

Example:

The Session class is implemented in:
src/requests/sessions.py
The class initializes session state including headers,
cookies, and configuration.

Citation:

Session
src/requests/sessions.py
Lines 7–21

Clicking it opens the corresponding code.

⸻

🖥️ CodeViewer

The CodeViewer is built around the Monaco editor.

Citation clicked
      ↓
File path resolved
      ↓
Source code loaded
      ↓
Line range located
      ↓
Relevant lines highlighted

This allows the developer to immediately verify the AI’s answer.

⸻

🛠️ Technology Stack

Frontend

Technology	Purpose
Next.js	Web application
TypeScript	Type-safe frontend
Tailwind CSS	Styling
shadcn/ui	UI components
Lucide	Icons
Monaco Editor	CodeViewer

⸻

Backend

Technology	Purpose
Python	Backend language
FastAPI	REST API
Uvicorn	Application server
SQLite	Persistent local storage
Git	Repository ingestion

⸻

AI / RAG

Technology	Purpose
Gemini API	LLM generation
OpenAI-compatible API	Alternative LLM provider
BGE-small	Embeddings
Hybrid retrieval	Code search
AST/regex parser	Code understanding

⸻

📂 Project Structure

codebase-ai/
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   └── endpoints.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   │   └── repository.py
│   │   │
│   │   └── services/
│   │       ├── ingestion.py
│   │       ├── parser.py
│   │       ├── chunking.py
│   │       ├── embeddings.py
│   │       ├── retrieval.py
│   │       ├── local_vector_store.py
│   │       └── llm.py
│   │
│   ├── data/
│   │
│   ├── tests/
│   │
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   │
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   ├── globals.css
│   │   │
│   │   └── dashboard/
│   │       └── [id]/
│   │           └── page.tsx
│   │
│   ├── components/
│   │   ├── CodeViewer.tsx
│   │   └── ui/
│   │
│   ├── package.json
│   └── tsconfig.json
│
├── demo_repo/
│
├── .env
├── .env.example
├── docker-compose.yml
└── README.md

⸻

🗃️ Data Model

The system maintains information about repositories, files and chunks.

Repository

repository_id
name
url
status
files_count
chunks_count
created_at
updated_at

File

file_id
repository_id
path
language
size

Code Chunk

chunk_id
repository_id
file_id
file_path
language
symbol_name
symbol_type
parent_symbol
start_line
end_line
source_code
embedding

Relationships

Potential relationships include:

imports
calls
extends
implements
references
contains

⸻

🔄 Request Flow

sequenceDiagram
participant U as Developer
participant F as Frontend
participant B as FastAPI
participant R as Retrieval
participant S as Storage
participant L as LLM
participant C as CodeViewer
U->>F: Ask question
F->>B: POST /query
B->>R: Search repository
R->>S: Retrieve relevant chunks
S-->>R: Matching code
R-->>B: Ranked context
B->>L: Grounded prompt
L-->>B: Answer
B-->>F: Answer + citations
F-->>U: Display response
U->>C: Click citation
C-->>U: Open exact source lines

⸻

🔌 API Flow

The backend exposes endpoints for:

Repository ingestion

POST /api/repositories

Input:

{
  "url": "https://github.com/psf/requests"
}

⸻

Repository status

GET /api/repositories/{repository_id}/status

Returns information such as:

{
  "status": "indexed",
  "files": 40,
  "chunks": 807
}

⸻

Ask question

POST /api/repositories/{repository_id}/query

Example:

{
  "question": "Where is the Session class implemented?"
}

Response conceptually:

{
  "answer": "...",
  "citations": [
    {
      "file_path": "src/requests/sessions.py",
      "symbol_name": "Session",
      "start_line": 7,
      "end_line": 21
    }
  ]
}

⸻

🚀 Installation

Prerequisites

Install:

* Git
* Python 3.10+
* Node.js 18+
* npm

Optional:

* Docker

⸻

1️⃣ Clone Repository

git clone https://github.com/Avinash7981/Codebase-ai.git

Then:

cd Codebase-ai

⸻

2️⃣ Backend Setup

Go to backend:

cd backend

Create virtual environment:

python3 -m venv venv

Activate it.

macOS / Linux

source venv/bin/activate

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

⸻

3️⃣ Frontend Setup

Open another terminal:

cd frontend

Install dependencies:

npm install

⸻

🔑 Environment Variables

Create:

.env

in the project root/backend configuration location used by your application.

Example:

LLM_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
LLM_MODEL=gemini-3.6-flash
LLM_API_KEY=YOUR_OPENAI_API_KEY
LLM_API_BASE=

Important

Never commit real API keys to GitHub.

Use:

.env

and keep it inside .gitignore.

Provide:

.env.example

with placeholders instead.

⸻

▶️ Running the Project

Start Backend

From the backend directory:

uvicorn app.main:app --reload --port 8000

Backend:

http://localhost:8000

⸻

Start Frontend

From the frontend directory:

npm run dev

Frontend normally runs at:

http://localhost:3000

⸻

🌐 Using Codebase AI

Step 1

Open the frontend.

http://localhost:3000

⸻

Step 2

Paste a GitHub repository URL.

Example:

https://github.com/psf/requests

⸻

Step 3

Click:

Analyze Repository

⸻

Step 4

Wait for:

Repository connected ✓
Files discovered ✓
Parsing code ✓
Generating embeddings ✓
AI knowledge ready ✓

⸻

Step 5

Ask a question.

Example:

Where is the Session class implemented?

⸻

Step 6

Codebase AI retrieves relevant code.

⸻

Step 7

The LLM generates a grounded explanation.

⸻

Step 8

Click the citation.

The exact source code opens inside CodeViewer.

⸻

💬 Example Queries

Repository Navigation

Where is the Session class implemented?
Where is authentication handled?
Where are database connections created?

⸻

Code Understanding

What does the Session class do?
What does the __init__ method initialize?
How does this service work?

⸻

Flow Analysis

How does an HTTP request flow through the code?
How does the login process work?
How is a request authenticated?

⸻

Developer Onboarding

What are the main components of this repository?
Which files should I understand first?
Where is the main entry point?

⸻

🎬 Recommended Hackathon Demo

Use a repository with enough real code to demonstrate retrieval.

For example:

https://github.com/psf/requests

Demo Question 1

Ask:

Where is the Session class implemented?

Expected:

src/requests/sessions.py

Then click the citation.

🔥 This demonstrates:

Question
 ↓
Retrieval
 ↓
Source
 ↓
CodeViewer

⸻

Demo Question 2

Ask:

What does the Session init method initialize?

The system should explain the initialization logic and cite the relevant lines.

⸻

Demo Question 3

Ask:

How does the requests library send HTTP requests?

This demonstrates a more conceptual question requiring multiple relevant code chunks.

⸻

🛡️ Security

Codebase AI treats repository content as untrusted data.

Important principles include:

Never execute repository code

The system analyzes source code but should not execute arbitrary cloned repository programs.

Repository isolation

Each chunk is associated with:

repository_id

Retrieval should only return chunks belonging to the requested repository.

API key protection

LLM keys remain on the backend.

They are never exposed to the frontend.

Environment variables

Secrets should be stored in:

.env

and never committed.

Prompt injection resistance

Repository files are treated as data, not instructions to the AI system.

⸻

⚡ Performance

Codebase AI is designed to process repositories in stages.

Clone
 ↓
Filter
 ↓
Parse
 ↓
Chunk
 ↓
Batch Store

For large repositories, chunks are inserted in batches rather than issuing thousands of individual database transactions.

This reduces ingestion overhead and prevents the application from freezing while writing large indexes.

⸻

🔄 Persistent Storage

A key design requirement is that indexed information survives backend restarts.

Repository
     ↓
Index
     ↓
Persistent Storage
     ↓
Backend Restart
     ↓
Load Existing Index
     ↓
Continue Querying

Therefore the developer does not necessarily need to re-ingest the same repository every time the backend restarts.

⸻

🚨 Error Handling

Codebase AI handles several failure scenarios.

Invalid repository

Repository analysis failed:
Repository not found

Network failure

The user receives a clear ingestion error instead of an indefinite loading state.

LLM failure

The system supports provider fallback when configured.

Gemini
  ↓ failure
Retry
  ↓ failure
OpenAI fallback

Insufficient evidence

Instead of hallucinating:

I couldn't find enough evidence in the indexed
repository to answer this confidently.

⸻

🔁 Resilient LLM Architecture

The LLM layer is provider-independent.

                LLM Service
                    │
            ┌───────┴────────┐
            ↓                ↓
         Gemini           OpenAI
            │                │
            └───────┬────────┘
                    ↓
                 Answer

The architecture allows the provider to be changed through configuration without rewriting the entire application.

⸻

📊 Example End-to-End Result

Question:

Where is the Session class implemented?

Retrieval:

src/requests/sessions.py
Session
Lines 7–21

AI:

The Session class is implemented in
src/requests/sessions.py.
It manages persistent HTTP session state and
initializes configuration such as headers and
session-level settings.

Citation:

Session
src/requests/sessions.py : 7–21

Click:

→ CodeViewer
→ sessions.py
→ exact lines highlighted

⸻

🧪 Acceptance Test

A successful deployment should pass:

✓ Frontend starts
✓ Backend starts
✓ Repository URL accepted
✓ Git clone succeeds
✓ Files filtered
✓ Source code parsed
✓ Chunks generated
✓ Embeddings generated/fallback generated
✓ Chunks persisted
✓ Retrieval returns relevant sources
✓ LLM generates grounded answer
✓ Citations returned
✓ CodeViewer opens cited source
✓ Backend restart does not destroy index

⸻

📈 Current Demo Metrics

The system has been tested against the psf/requests repository.

Example indexing result:

Repository: psf/requests
Files processed: 40
Chunks generated: 807

Example successful retrieval:

Question:
Where are HTTP sessions handled?
Relevant source:
src/requests/sessions.py

⸻

⚠️ Current Limitations

The current hackathon implementation prioritizes a reliable local demonstration.

Embedding fallback

The environment may use deterministic local embeddings when the BGE/PyTorch stack cannot be installed due to dependency/network restrictions.

Parser fallback

A lightweight parsing fallback is available when Tree-sitter grammars cannot be installed.

Local vector storage

The current demo uses persistent local storage rather than requiring a separately deployed vector database.

These choices keep the application:

* Fast to start
* Local
* Network-resilient
* Easy to demonstrate

The architecture can later be upgraded to production-grade infrastructure.

⸻

🚀 Future Improvements

1. Advanced Code Graph

Build a complete dependency graph:

Function
 ↓
Calls
 ↓
Function
 ↓
Database

⸻

2. Impact Analysis

Allow questions such as:

“If I change PaymentService, what could break?”

Output:

PaymentService
      ↓
OrderService
      ↓
CheckoutController
      ↓
API /checkout

⸻

3. Architecture Explorer

Automatically generate:

Frontend
   ↓
API
   ↓
Services
   ↓
Database

⸻

4. Code Flow Visualization

Show:

POST /login
     ↓
Controller
     ↓
Auth Service
     ↓
Password Validation
     ↓
JWT Generation
     ↓
Response

⸻

5. Developer Onboarding Mode

Generate:

Repository Overview
       ↓
Important Files
       ↓
Main Components
       ↓
Entry Points
       ↓
Request Flows

⸻

6. Multi-Language Expansion

Extend parsing and retrieval support for:

Rust
Kotlin
C#
PHP
Ruby
Swift
Dart

⸻

7. Pull Request Intelligence

Analyze a PR and answer:

What changed?
What components are affected?
What tests should be updated?
What could break?

⸻

8. IDE Integration

Future versions could integrate directly with:

VS Code
JetBrains IDEs
Cursor
GitHub

⸻

🌍 Real-World Applications

Codebase AI can help with:

👨‍💻 Developer Onboarding

Understand an unfamiliar project quickly.

🏢 Enterprise Codebases

Navigate large internal repositories.

🔧 Legacy Systems

Understand old and undocumented code.

🌐 Open Source

Help contributors understand projects before submitting changes.

🐛 Debugging

Locate relevant code paths.

📚 Software Education

Help students understand real-world repositories.

⸻

🏆 Hackathon Value Proposition

Codebase AI addresses a real developer productivity problem.

Before

Unfamiliar Repository
        ↓
Hours of Searching
        ↓
Manual Investigation
        ↓
Multiple Files
        ↓
Confusion

After

Unfamiliar Repository
        ↓
Ask Codebase AI
        ↓
Relevant Code
        ↓
AI Explanation
        ↓
Exact Citation
        ↓
Immediate Understanding

The key differentiator

The AI doesn’t just tell you the answer. It shows you exactly where the answer lives in the codebase.

⸻

🔮 Product Vision

Codebase AI can evolve from a code Q&A tool into a complete:

AI Codebase Intelligence Platform

Future capabilities:

                 CODEBASE AI
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
   Code Search    Code Explain   Architecture
       │              │              │
       └──────────────┼──────────────┘
                      ↓
               Code Intelligence
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
      Debugging   Impact       Onboarding
                  Analysis

⸻

🤝 Contributing

Contributions are welcome.

1. Fork the repository

git fork

2. Create a branch

git checkout -b feature/new-feature

3. Make changes

4. Commit

git commit -m "Add new feature"

5. Push

git push origin feature/new-feature

6. Open a Pull Request

⸻

🔐 Environment Safety

Never commit:

.env
API keys
database passwords
private credentials
service account keys

Use:

.env.example

for sharing configuration structure.

⸻

📄 License

This project is licensed under the MIT License.

⸻

👨‍💻 Author

Avinash Goud

B.Tech CSE Student | AI Builder | Full Stack Developer

GitHub:

https://github.com/Avinash7981

⸻

⭐ Final Note

Codebase AI is built around one simple idea:

Don’t make developers read the entire codebase. Let them ask the codebase.

From repository ingestion to intelligent retrieval, grounded AI answers, exact citations, and interactive source navigation, Codebase AI turns an unfamiliar repository into an interactive source of knowledge.

⸻

🚀 Codebase AI

GIVE IT A REPOSITORY
        ↓
ASK A QUESTION
        ↓
FIND THE CODE
        ↓
UNDERSTAND THE CODE
        ↓
VERIFY THE SOURCE

Find. Understand. Prove. 🔥
