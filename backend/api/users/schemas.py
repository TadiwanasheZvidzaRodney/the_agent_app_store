from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    telegram_id: str
    username: Optional[str] = None
