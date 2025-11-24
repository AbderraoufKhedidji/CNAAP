
from fastapi import APIRouter


users_router: APIRouter = APIRouter(prefix="/users", tags=["Users"])

