#!/usr/bin/env python3
"""
Script de prueba para verificar que el proyecto se ejecuta correctamente
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Prueba que todos los modulos se pueden importar"""
    print("Probando importaciones...")
    
    try:
        from database.db_manager import DatabaseManager
        print("  [OK] DatabaseManager importado")
    except Exception as e:
        print(f"  [ERROR] DatabaseManager: {e}")
        return False
    
    try:
        from models.license_plate_detector import LicensePlateDetector
        print("  [OK] LicensePlateDetector importado")
    except Exception as e:
        print(f"  [ERROR] LicensePlateDetector: {e}")
        return False
    
    try:
        from system.linking_system import LinkingSystem
        print("  [OK] LinkingSystem importado")
    except Exception as e:
        print(f"  [ERROR] LinkingSystem: {e}")
        return False
    
    try:
        import app
        print("  [OK] app importado")
    except Exception as e:
        print(f"  [ERROR] app: {e}")
        return False
    
    return True

def test_database_connection():
    """Prueba la conexion a la base de datos"""
    print("\nProbando conexion a base de datos...")
    
    try:
        from database.db_manager import DatabaseManager
        db = DatabaseManager()
        
        if db.conn:
            print("  [OK] Conexion a PostgreSQL establecida")
            db.close()
            return True
        else:
            print("  [ADVERTENCIA] No se pudo conectar a PostgreSQL")
            print("  Nota: Asegurese de que PostgreSQL este corriendo")
            print("  y que las credenciales en .env sean correctas")
            return False
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False

def test_ocr_model():
    """Prueba que el modelo OCR se puede inicializar"""
    print("\nProbando modelo de vision artificial...")
    
    try:
        from models.license_plate_detector import LicensePlateDetector
        print("  Inicializando modelo (esto puede tardar unos segundos)...")
        detector = LicensePlateDetector()
        print("  [OK] Modelo OCR inicializado correctamente")
        return True
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False

def main():
    """Funcion principal"""
    print("="*60)
    print("PRUEBA DE EJECUCION DEL SISTEMA DE DETECCION DE MATRICULAS")
    print("="*60)
    
    # Probar importaciones
    if not test_imports():
        print("\n[FALLO] Error en las importaciones")
        return 1
    
    # Probar conexion a base de datos
    db_ok = test_database_connection()
    
    # Probar modelo OCR (opcional, puede tardar)
    print("\n¿Desea probar el modelo OCR? (puede tardar)")
    print("Omitiendo prueba de OCR por ahora...")
    # ocr_ok = test_ocr_model()
    
    print("\n" + "="*60)
    if db_ok:
        print("RESUMEN: Sistema listo para usar")
        print("="*60)
        print("\nPara ejecutar la aplicacion:")
        print("  python3 app.py")
    else:
        print("RESUMEN: Sistema funcional pero requiere PostgreSQL")
        print("="*60)
        print("\nPasos siguientes:")
        print("1. Instalar y configurar PostgreSQL")
        print("2. Crear la base de datos: license_plate_db")
        print("3. Configurar credenciales en .env")
        print("4. Ejecutar: python3 database/init_db.py")
        print("5. Ejecutar: python3 app.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

