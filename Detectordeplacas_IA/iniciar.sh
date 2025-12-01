#!/bin/bash
# Script para iniciar el sistema de deteccion de matriculas

echo "============================================================"
echo "SISTEMA DE DETECCION DE MATRICULAS"
echo "============================================================"
echo ""

# Verificar si PostgreSQL esta corriendo
if ! pg_isready -h localhost -p 5432 > /dev/null 2>&1; then
    echo "ADVERTENCIA: PostgreSQL no esta corriendo"
    echo ""
    echo "Para iniciar PostgreSQL:"
    echo "  - macOS (Homebrew): brew services start postgresql"
    echo "  - Linux: sudo systemctl start postgresql"
    echo "  - Windows: Iniciar servicio desde Administrador de Servicios"
    echo ""
    read -p "¿Desea continuar de todos modos? (s/n): " continuar
    if [ "$continuar" != "s" ] && [ "$continuar" != "S" ]; then
        exit 1
    fi
    echo ""
fi

# Verificar archivo .env
if [ ! -f .env ]; then
    echo "Creando archivo .env desde config.env.example..."
    cp config.env.example .env
    echo "IMPORTANTE: Edite el archivo .env con sus credenciales de PostgreSQL"
    echo ""
fi

# Ejecutar la aplicacion
echo "Iniciando aplicacion..."
echo ""
python3 app.py

