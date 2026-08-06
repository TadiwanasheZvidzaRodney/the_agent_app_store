from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    telegram_id: str = Field(..., description="The unique identifier from Telegram or a custom web user ID.", example="123456789")
    username: Optional[str] = Field(None, description="The user's display name or username.", example="johndoe")
