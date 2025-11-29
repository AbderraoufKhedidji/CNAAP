import asyncio
from _shared.domain.db.api_db_context import ApiDbContext

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@postgres:5432/cnaap_db"

apiDbContext = ApiDbContext(DATABASE_URL)

async def main():
    # Crear todas las tablas definidas en Base.metadata
    await apiDbContext.create_tables()
    print("Tablas creadas correctamente")

if __name__ == "__main__":
    asyncio.run(main())
