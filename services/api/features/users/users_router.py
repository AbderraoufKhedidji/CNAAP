
from fastapi import APIRouter


users_router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("")
async def get_clients():
    return "holaa desde user2s"