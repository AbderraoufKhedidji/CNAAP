
from fastapi import APIRouter
from services.api.features.users.users_router import users_router
from services.api.features.clients.clients_router import clients_router


class RoutersService:
    UsersRouter: APIRouter = users_router
    ClientsRouter: APIRouter = clients_router