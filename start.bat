@echo off
echo ==========================================
echo  CNAA Project - Docker Startup
echo ==========================================

echo.
echo Deteniendo contenedores existentes...
docker-compose down

echo.
echo Buscando imágenes existentes del proyecto...
docker images | findstr /I "cnaap" > nul

IF %ERRORLEVEL%==0 (
    echo Imagenes encontradas. Iniciando sin build...
    docker-compose up -d
) ELSE (
    echo No existen imagenes. Construyendo proyecto...
    docker-compose up --build -d
)

echo.
echo Iniciando proyecto...
docker-compose ps

echo.
echo ==========================================
echo  Iniciando desarrollo en backend y frontend
echo ==========================================

:: Abrir consola para backend
start "" cmd /k "cd /d %~dp0services\api && .venv\Scripts\activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"

:: Abrir consola para frontend
start "" cmd /k "cd /d %~dp0clients\mainFront && npx astro dev"

