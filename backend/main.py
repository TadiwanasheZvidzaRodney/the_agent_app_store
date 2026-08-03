import asyncio
import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from db.client import db
from transports.telegram.transport import start_telegram_bot
from api.agents.router import router as agents_router
from api.users.router import router as users_router

# Load env
load_dotenv()

app = FastAPI(title="Agent App Store API")

# Add CORS middleware for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents_router, prefix="/api/agents", tags=["Agents"])
app.include_router(users_router, prefix="/api/users", tags=["Users"])

@app.on_event("startup")
async def startup_event():
    logger.info("Connecting to database...")
    try:
        await db.connect()
        logger.info("Connected to database.")
        
        import json
        import os
        from db.crud import sync_core_agents
        
        # Sync modular agents
        agents_dir = os.path.join(os.path.dirname(__file__), "agents")
        core_agents = []
        if os.path.exists(agents_dir):
            for category in os.listdir(agents_dir):
                category_path = os.path.join(agents_dir, category)
                if os.path.isdir(category_path):
                    for filename in os.listdir(category_path):
                        if filename.endswith(".json"):
                            with open(os.path.join(category_path, filename), "r") as f:
                                try:
                                    agent_data = json.load(f)
                                    agent_data["category"] = category
                                    core_agents.append(agent_data)
                                except json.JSONDecodeError as e:
                                    logger.error(f"Error parsing {filename}: {e}")
            
        if core_agents:
            await sync_core_agents(core_agents)
            logger.info(f"Synced {len(core_agents)} modular agents to DB.")
            
    except Exception as e:
        logger.error(f"Failed to connect or sync DB: {e}")
        
    asyncio.create_task(start_telegram_bot())

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Disconnecting from database...")
    await db.disconnect()

@app.get("/api/health")
async def api_health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
