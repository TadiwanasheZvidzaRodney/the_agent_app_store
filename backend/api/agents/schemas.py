from pydantic import BaseModel
from typing import Optional

class AgentCreate(BaseModel):
    name: str
    system_prompt: str
    description: Optional[str] = None
    voice_type: str = "default"
    llm_model: str = "llama3-8b-8192"
    isActive: bool = True

class AgentUpdate(BaseModel):
    name: Optional[str] = None
    system_prompt: Optional[str] = None
    description: Optional[str] = None
    voice_type: Optional[str] = None
    llm_model: Optional[str] = None
    isActive: Optional[bool] = None
