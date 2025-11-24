# BACKEND PYTHON WINDOWS

## Descargas PYTHON 3.14
    - python -> https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe (añadir al path)
    - setx /M PY_PYTHON "3.14" (powershell en modo administrador)
## Crear entorno virtual
    - En /services/api  ->  py -m venv .venv

## Ejecutar entorno virtual
    - .venv\Scripts\activate 

## Actualizar pip 
    - py -m pip install --upgrade pip
