from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from services.api.features.routers_service import RoutersService

app = FastAPI(title="Mi API con FastAPI")

# --------------------
# Configurar CORS
# --------------------
origins = [
    "http://localhost",
    "http://localhost:3000",  # Frontend React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Registrar routers en la app
# --------------------
app.include_router(RoutersService.UsersRouter)
app.include_router(RoutersService.ClientsRouter)

