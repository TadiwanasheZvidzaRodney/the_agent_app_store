# The Hub: AI Agent Swarm Ecosystem 🤖

A modular, highly scalable "App Store" for AI agents. This platform allows users to browse, switch between, and interact with various AI personas. It has evolved from a simple Telegram bot into a **Massive Multi-Agent Swarm Ecosystem** where agents can dynamically discover and collaborate with each other.

## 🧠 Core Features

- **Hierarchical Swarm Architecture**: Top-level "Supervisor" agents (like the Master Orchestrator) can break down complex user requests and delegate sub-tasks to specialist agents in the background, synthesizing their responses for the user.
- **Semantic Agent Discovery**: Utilizing Supabase `pgvector`, agents are embedded into a vector space based on their capabilities. Supervisors dynamically search the vector database to discover and recruit the exact experts they need on the fly.
- **Multi-Transport Interfaces**: 
  - **Web Dashboard & Chat**: A premium React dashboard to create agents and a dedicated web-chat UI to interact with them directly in the browser.
  - **Telegram Bot**: Native integration via webhooks/polling, maintaining conversation memory across transports.
- **Modular Domains**: Agents are structured logically by domain (`business`, `personal`, `system`), making it trivial to scale the ecosystem.

## 🏗 Architecture

This project strictly adheres to a **Domain-Driven Design (DDD)** and Separation of Concerns:
- **Backend**: FastAPI (Python), serving as the core orchestration and API layer.
- **Frontend**: React + Vite + Vanilla CSS, providing a premium, ultra-modern dashboard for agent management.
- **Database**: PostgreSQL with `pgvector` (hosted on Supabase) accessed via `prisma-client-py` with asyncio support.
- **Routing**: A unified `MessageRouter` that handles cross-agent tool calling, memory management, and dynamic LLM (Groq) generation.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- Node.js 18+
- A [Supabase](https://supabase.com) account (for PostgreSQL, **must support pgvector**)
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- A [Groq API Key](https://console.groq.com/) for LLM inference

### 2. Environment Setup

Navigate to the `backend/` directory and create a `.env` file:
```env
# Supabase PostgreSQL connection strings
DATABASE_URL="postgresql://postgres.[YOUR-PROJECT-REF]:[YOUR-PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:6543/postgres?pgbouncer=true"
DIRECT_URL="postgresql://postgres.[YOUR-PROJECT-REF]:[YOUR-PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:5432/postgres"

# API Keys
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
GROQ_API_KEY="your_groq_api_key"
```

### 3. Backend Installation

We use a Python Virtual Environment to keep dependencies clean.

```bash
cd backend/
# Create and activate virtual environment (Windows/MINGW64)
python -m venv venv
source venv/Scripts/activate

# Install requirements
pip install -r requirements.txt

# Generate the Prisma Client and push the schema to Supabase
prisma generate
prisma db push
```

### 4. Frontend Installation

```bash
cd frontend/
npm install
```

---

## 💻 Running Locally

You will need two terminals running simultaneously.

### Start the Backend (Terminal 1)
```bash
cd backend/
source venv/Scripts/activate
uvicorn main:app --reload
```
*The backend runs on `http://localhost:8000`. This will simultaneously start the FastAPI server and the Telegram bot polling.*

### Start the Frontend (Terminal 2)
```bash
cd frontend/
npm run dev
```
*The frontend runs on `http://localhost:5173`.*

---

## 📁 Project Structure

```text
/agents_store
 ├── /backend               # Python FastAPI application
 │   ├── /agents            # Modular JSON agent definitions
 │   │   ├── /business      # Business specialists (e.g. Sales, Tech Support)
 │   │   ├── /personal      # Personal specialists (e.g. Fitness, Therapy)
 │   │   └── /system        # Supervisor agents (e.g. Master Orchestrator)
 │   ├── /api               # REST API Routers & Schemas (Agents, Users)
 │   ├── /core              # Unified MessageRouter & Swarm Delegation
 │   ├── /db                # Prisma Client & Vector Search logic
 │   ├── /prisma            # Prisma schema definitions (Modularized)
 │   ├── /services          # External integrations (Groq, TTS, Embeddings)
 │   ├── /transports        # Protocol integrations (Telegram)
 │   └── main.py            # Entry point for Uvicorn
 │
 ├── /frontend              # React + Vite application
 │   ├── /src
 │   │   ├── /assets
 │   │   ├── /components
 │   │   ├── /pages         # Dashboard, Landing Page, and Web Chat UI
 │   │   ├── App.jsx
 │   │   └── index.css      # Premium Design System tokens
 │   ├── index.html
 │   └── package.json
 │
 ├── AGENTS.md              # System Architecture Rules & Guidelines
 └── .gitignore             # Global git ignores
```

## 📜 Contributing
Please refer to `AGENTS.md` for strict guidelines regarding anti-spaghetti code and maintaining absolute separation of concerns.
