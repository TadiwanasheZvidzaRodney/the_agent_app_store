from fastapi import APIRouter, HTTPException
from typing import List
import db.users.crud as crud
from .schemas import UserCreate

router = APIRouter()

@router.get("/", summary="List all users", description="Returns a list of all registered users in the database.")
async def get_users():
    return await crud.get_users()

@router.get("/{user_id}", summary="Get user details", description="Retrieves the profile information of a specific user.")
async def get_user(user_id: str):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", summary="Delete a user", description="Permanently removes a user and their associated sessions from the system.")
async def delete_user(user_id: str):
    try:
        deleted = await crud.delete_user(user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        return {"status": "success", "message": "User deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
