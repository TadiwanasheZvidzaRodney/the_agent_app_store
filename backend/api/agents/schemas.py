from pydantic import BaseModel, Field
from typing import Optional

class AgentCreate(BaseModel):
    name: str = Field(..., description="The display name of the agent.", example="Fitness Coach")
    system_prompt: str = Field(..., description="The system prompt defining the agent's persona, knowledge, and behaviors.", example="You are a strict but encouraging fitness coach.")
    description: Optional[str] = Field(None, description="A brief description of what the agent does, displayed in the App Store UI.", example="Helps you achieve your fitness goals.")
    voice_type: str = Field("default", description="The voice style/ID used by Edge TTS for audio generation.", example="en-US-JennyNeural")
    llm_model: str = Field("llama-3.1-8b-instant", description="The underlying LLM model string used by Groq.", example="llama-3.1-8b-instant")
    isActive: bool = Field(True, description="Whether the agent is currently available in the App Store.")

class AgentUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The display name of the agent.")
    system_prompt: Optional[str] = Field(None, description="The system prompt defining the agent's persona.")
    description: Optional[str] = Field(None, description="A brief description of what the agent does.")
    voice_type: Optional[str] = Field(None, description="The voice style/ID used by Edge TTS.")
    llm_model: Optional[str] = Field(None, description="The underlying LLM model string used by Groq.")
    isActive: Optional[bool] = Field(None, description="Whether the agent is currently available.")

class ChatRequest(BaseModel):
    session_id: Optional[str] = Field(None, description="The existing conversation session ID. If not provided, a new session is created.", example="cm23xxyz...")
    text: str = Field(..., description="The user's message to the agent.", example="I want to build muscle.")
    web_user_id: str = Field("web-user-1", description="The identifier for the web user. Used to associate sessions when session_id is omitted.")

class ChatResponse(BaseModel):
    reply: str = Field(..., description="The agent's text response.", example="Great! Let's start by looking at your current diet.")
    session_id: str = Field(..., description="The session ID associated with this conversation.", example="cm23xxyz...")
