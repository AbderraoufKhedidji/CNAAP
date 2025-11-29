@echo off
echo ==========================================
echo  CNAA Project - Docker Startup
echo ==========================================

set RESET=%1

echo.

IF /I "%RESET%"=="-r" (
    echo Reset completo solicitado...
    echo Deteniendo contenedores existentes...
    docker-compose down --rmi all -v --remove-orphans
    echo Limpiando builds...
    docker-compose build --no-cache
) ELSE (
    echo Deteniendo contenedores existentes...
    docker-compose down
)

echo.
echo Buscando imágenes existentes del proyecto...
docker images | findstr /I "cnaap" > nul

IF %ERRORLEVEL%==0 (
    IF /I "%RESET%"=="-r" (
        echo Imágenes reconstruidas por reset.
    ) ELSE (
        echo Imagenes encontradas. Iniciando sin build...
        docker-compose up -d
    )
) ELSE (
    echo No existen imagenes. Construyendo proyecto...
    docker-compose up --build -d
)

echo.
echo Iniciando proyecto...
docker-compose ps
