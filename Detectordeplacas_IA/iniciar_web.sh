#!/bin/bash
# Script para iniciar el servidor web

echo "============================================================"
echo "INICIANDO SERVIDOR WEB - SISTEMA DE DETECCION DE MATRICULAS"
echo "============================================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 no esta instalado"
    exit 1
fi

# Verificar dependencias
echo "Verificando dependencias..."
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Instalando dependencias..."
    pip3 install flask flask-cors
fi

# Verificar archivos necesarios
if [ ! -f "app_web.py" ]; then
    echo "Error: app_web.py no encontrado"
    exit 1
fi

# Crear carpetas necesarias
mkdir -p uploads templates static/css static/js

# Detener procesos anteriores en puerto 8080
echo "Verificando puerto 8080..."
lsof -ti:8080 | xargs kill -9 2>/dev/null
sleep 1

# Iniciar servidor
echo ""
echo "Iniciando servidor en puerto 8080..."
echo "Acceda a: http://localhost:8080"
echo "Para dispositivos moviles: http://[SU_IP]:8080"
echo ""
echo "Presione Ctrl+C para detener el servidor"
echo "============================================================"
echo ""

python3 app_web.py 8080

