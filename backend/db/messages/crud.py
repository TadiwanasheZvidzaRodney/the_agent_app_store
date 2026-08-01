from typing import List
from prisma.models import Message
from db.client import db

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
