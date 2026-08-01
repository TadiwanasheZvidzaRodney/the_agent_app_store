from typing import List, Optional
from prisma.models import User
from db.client import db

async def get_or_create_user(telegram_id: str, username: str) -> User:
    user = await db.user.find_unique(where={"telegram_id": telegram_id})
    if not user:
        user = await db.user.create(data={"telegram_id": telegram_id, "username": username})
    return user

async def get_users() -> List[User]:
    return await db.user.find_many()

async def get_user(user_id: str) -> Optional[User]:
    return await db.user.find_unique(where={"id": user_id})

async def delete_user(user_id: str) -> Optional[User]:
    return await db.user.delete(where={"id": user_id})
