from typing import List, Optional
from db.client import db
from prisma.models import User, Agent, Session, Message

async def get_or_create_user(telegram_id: str, username: str) -> User:
    user = await db.user.find_unique(where={"telegram_id": telegram_id})
    if not user:
        user = await db.user.create(data={"telegram_id": telegram_id, "username": username})
    return user

async def get_active_agents() -> List[Agent]:
    return await db.agent.find_many(where={"isActive": True})

async def get_agent_by_id(agent_id: str) -> Optional[Agent]:
    return await db.agent.find_unique(where={"id": agent_id})

async def switch_user_agent(user_id: str, new_agent_id: str) -> Session:
    # Deactivate any existing active session for this user
    await db.session.update_many(
        where={"user_id": user_id, "isActive": True},
        data={"isActive": False}
    )
    # Create and activate new session
    session = await db.session.create(
        data={
            "user_id": user_id,
            "agent_id": new_agent_id,
            "isActive": True
        }
    )
    return session

async def get_active_session(user_id: str) -> Optional[Session]:
    return await db.session.find_first(
        where={"user_id": user_id, "isActive": True},
        include={"agent": True} # include the agent to know system_prompt
    )

async def save_message(session_id: str, role: str, content: str) -> Message:
    return await db.message.create(
        data={
            "session_id": session_id,
            "role": role,
            "content": content
        }
    )

async def get_session_history(session_id: str, limit: int = 20) -> List[Message]:
    return await db.message.find_many(
        where={"session_id": session_id},
        order={"createdAt": "asc"},
        take=limit
    )

async def sync_core_agents(core_agents: List[dict]):
    """Called on startup to upsert core system agents into the DB."""
    for agent_data in core_agents:
        existing = await db.agent.find_unique(where={"id": agent_data["id"]})
        if existing:
            await db.agent.update(where={"id": agent_data["id"]}, data=agent_data)
        else:
            await db.agent.create(data=agent_data)
