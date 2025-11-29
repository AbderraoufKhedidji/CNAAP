import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from features.routers_service import RoutersService
from _shared.domain.db.db import apiDbContext
from asyncpg import ConnectionDoesNotExistError, CannotConnectNowError

app = FastAPI(title="Mi API con FastAPI")

async def wait_for_db(retries: int = 10, delay: float = 2.0):
    """Intenta conectar a la base de datos hasta que esté lista."""
    for i in range(retries):
        try:
            await apiDbContext.create_tables()
            return
        except Exception as e:
            print(f"DB no lista, reintentando ({i+1}/{retries})... {e}")
            await asyncio.sleep(delay)
    raise RuntimeError("No se pudo conectar a la base de datos después de varios intentos.")

@app.on_event("startup")
async def startup_event():
    await wait_for_db()

# --------------------
# Configurar CORS
# --------------------
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Registrar routers
# --------------------
app.include_router(RoutersService.UsersRouter)
app.include_router(RoutersService.ClientsRouter)
