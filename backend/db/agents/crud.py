from typing import List, Optional, Dict, Any
from prisma.models import Agent
from db.client import db

async def create_agent(name: str, system_prompt: str, description: Optional[str] = None, 
                       voice_type: str = "default", llm_model: str = "llama-3.1-8b-instant", 
                       isActive: bool = True) -> Agent:
    return await db.agent.create(
        data={
            "name": name,
            "system_prompt": system_prompt,
            "description": description,
            "voice_type": voice_type,
            "llm_model": llm_model,
            "isActive": isActive
        }
    )

async def get_active_agents() -> List[Agent]:
    return await db.agent.find_many(where={"isActive": True})

async def get_all_agents() -> List[Agent]:
    return await db.agent.find_many()

async def get_agent(agent_id: str) -> Optional[Agent]:
    return await db.agent.find_unique(where={"id": agent_id})

async def update_agent(agent_id: str, data: Dict[str, Any]) -> Optional[Agent]:
    return await db.agent.update(where={"id": agent_id}, data=data)

async def delete_agent(agent_id: str) -> Optional[Agent]:
    return await db.agent.delete(where={"id": agent_id})
