# Dependencias y Tecnologias

## Backend Framework

- **FastAPI**: Framework web moderno, rápido y asincrónico para APIs en Python.

## ASGI Server

- **Uvicorn**: Servidor ASGI para correr FastAPI.

## Data Validation & Configuration

- **Pydantic**: Validación de datos y modelos.
- **Pydantic-settings**: Manejo de configuración tipo `.env`.
- **python-dotenv**: Leer archivos `.env`.

## Authentication & Security

- **python-jose**: JWT y firmas digitales.
- **passlib[bcrypt]**: Hashing seguro de contraseñas.

## Database / ORM

- **SQLModel**: ORM moderno basado en SQLAlchemy y Pydantic.
- **SQLAlchemy**: Motor de ORM clásico.
- **SQLite**: Base de datos ligera integrada (no requiere driver extra).

## Testing

- **pytest**: Framework de testing.
- **pytest-asyncio**: Soporte para tests asíncronos.
- **pytest-cov**: Reporte de cobertura de tests.
- **httpx**: Cliente HTTP async para testing de endpoints.

## Utilities

- **orjson**: JSON rápido.
- **email-validator**: Validación de emails.
- **starlette**: Middlewares y utilidades usadas internamente por FastAPI.
