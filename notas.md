# BACKEND PYTHON WINDOWS

## Descargas PYTHON 3.14

    - descargar python -> https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe (añadir al path)
    - setx /M PY_PYTHON "3.14" (powershell en modo administrador)

## Arrancar aplicacion

    - start.bat

## Comandos para hacer una migracio

Generar migracion:
    - alembic revision --autogenerate -m "Descripción del cambio"
Aplicar migracion a la base de datos:
    - alembic upgrade head