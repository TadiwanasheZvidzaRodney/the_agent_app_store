from fastapi import APIRouter, HTTPException
import db.agents.crud as crud
from .schemas import AgentCreate, AgentUpdate, ChatRequest, ChatResponse

router = APIRouter()

@router.get("/", summary="List all agents", description="Returns a list of all agents currently available in the system, both active and inactive.")
async def get_all_agents():
    return await crud.get_all_agents()

@router.get("/active", summary="List active agents", description="Returns a list of all active agents available to handle requests in the App Store.")
async def get_active_agents():
    return await crud.get_active_agents()

@router.get("/{agent_id}", summary="Get agent details", description="Retrieves the full configuration and details of a specific agent by its ID.")
async def get_agent(agent_id: str):
    agent = await crud.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.post("/", summary="Create a new agent", description="Registers a new specialized AI agent with the system.")
async def create_agent(agent: AgentCreate):
    return await crud.create_agent(
        name=agent.name,
        system_prompt=agent.system_prompt,
        description=agent.description,
        voice_type=agent.voice_type,
        llm_model=agent.llm_model,
        isActive=agent.isActive
    )

@router.put("/{agent_id}", summary="Update an agent", description="Partially updates the configuration of an existing AI agent.")
async def update_agent(agent_id: str, agent: AgentUpdate):
    update_data = {k: v for k, v in agent.model_dump(exclude_unset=True).items()}
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
        
    try:
        updated = await crud.update_agent(agent_id, update_data)
        if not updated:
            raise HTTPException(status_code=404, detail="Agent not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{agent_id}", summary="Delete an agent", description="Permanently removes an agent from the system.")
async def delete_agent(agent_id: str):
    try:
        deleted = await crud.delete_agent(agent_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Agent not found")
        return {"status": "success", "message": "Agent deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{agent_id}/chat", response_model=ChatResponse, summary="Chat with an agent", description="Send a message to a specialized AI agent and get a textual response. The agent has the ability to delegate tasks to other agents.")
async def chat_with_agent(agent_id: str, req: ChatRequest):
    from db.crud import get_or_create_user, switch_user_agent
    from core.router import MessageRouter
    
    session_id = req.session_id
    if not session_id:
        db_user = await get_or_create_user(req.web_user_id, "Web User")
        session = await switch_user_agent(db_user.id, agent_id)
        session_id = session.id
        
    reply, new_session_id = await MessageRouter.process_web_message(session_id=session_id, text=req.text)
    return {"reply": reply, "session_id": new_session_id}
