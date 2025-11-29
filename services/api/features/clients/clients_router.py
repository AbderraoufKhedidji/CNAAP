from fastapi import APIRouter


clients_router = APIRouter(prefix="/clients", tags=["Clients"])

@clients_router.get("")
async def getClients():
    return "holaa desde clientes"