from fastapi import APIRouter, HTTPException
import db.agents.crud as crud
from .schemas import AgentCreate, AgentUpdate

router = APIRouter()

@router.get("/")
async def get_all_agents():
    return await crud.get_all_agents()

@router.get("/active")
async def get_active_agents():
    return await crud.get_active_agents()

@router.get("/{agent_id}")
async def get_agent(agent_id: str):
    agent = await crud.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.post("/")
async def create_agent(agent: AgentCreate):
    return await crud.create_agent(
        name=agent.name,
        system_prompt=agent.system_prompt,
        description=agent.description,
        voice_type=agent.voice_type,
        llm_model=agent.llm_model,
        isActive=agent.isActive
    )

@router.put("/{agent_id}")
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

@router.delete("/{agent_id}")
async def delete_agent(agent_id: str):
    try:
        deleted = await crud.delete_agent(agent_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Agent not found")
        return {"status": "success", "message": "Agent deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
