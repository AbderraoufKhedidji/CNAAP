
from fastapi import APIRouter
from features.users.users_router import users_router
from features.clients.clients_router import clients_router


class RoutersService:
    UsersRouter: APIRouter = users_router
    ClientsRouter: APIRouter = clients_router