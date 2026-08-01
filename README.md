# The Agent App Store 🤖

A modular, highly scalable "App Store" for AI agents. This platform allows users to browse, switch between, and interact with various AI personas, primarily utilizing a Telegram interface and a high-performance web dashboard.

## 🏗 Architecture

This project strictly adheres to a **Domain-Driven Design (DDD)** and Separation of Concerns:
- **Backend**: FastAPI (Python), serving as the core orchestration and API layer.
- **Frontend**: React + Vite + Vanilla CSS, providing a premium, ultra-modern dashboard for agent management.
- **AI Pipeline**: Built on the [Pipecat](https://pipecat.ai) framework.
- **Database**: PostgreSQL (hosted on [Supabase](https://supabase.com)) accessed via `prisma-client-py` with asyncio support.
- **Transports**: Highly modular, currently supporting **Telegram** webhooks and API polling, with a unified `MessageRouter` designed to easily support WhatsApp and WebSockets in the future.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- Node.js 18+
- A [Supabase](https://supabase.com) account (for PostgreSQL)
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
 │   ├── /api               # REST API Routers & Schemas (Agents, Users)
 │   ├── /core              # Core AI Pipeline logic (Pipecat orchestration)
 │   ├── /db                # Prisma Client & CRUD logic separated by domain
 │   ├── /prisma            # Prisma schema definitions (Modularized)
 │   ├── /services          # External integrations (Groq, TTS)
 │   ├── /transports        # Protocol integrations
 │   │   └── /telegram      # Telegram bot webhooks and API polling
 │   ├── main.py            # Entry point for Uvicorn
 │   └── requirements.txt
 │
 ├── /frontend              # React + Vite application
 │   ├── /src
 │   │   ├── /assets
 │   │   ├── /components
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
