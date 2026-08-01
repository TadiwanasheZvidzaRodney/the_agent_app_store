from prisma.models import Session
from db.client import db

async def switch_user_agent(user_id: str, new_agent_id: str) -> Session:
    await db.session.update_many(
        where={"user_id": user_id, "isActive": True},
        data={"isActive": False}
    )
    session = await db.session.create(
        data={
            "user_id": user_id,
            "agent_id": new_agent_id,
            "isActive": True
        }
    )
    return session
