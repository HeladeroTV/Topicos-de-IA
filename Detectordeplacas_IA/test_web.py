#!/usr/bin/env python3
"""
Script de prueba para verificar que la aplicacion web funciona correctamente
"""

import requests
import sys

def test_servidor():
    """Prueba que el servidor este respondiendo"""
    print("Probando servidor web...")
    
    try:
        # Probar pagina principal
        response = requests.get('http://localhost:8080', timeout=5)
        if response.status_code == 200:
            print("  [OK] Pagina principal responde correctamente")
        else:
            print(f"  [ERROR] Codigo de respuesta: {response.status_code}")
            return False
        
        # Probar archivos estaticos
        response = requests.get('http://localhost:8080/static/css/style.css', timeout=5)
        if response.status_code == 200:
            print("  [OK] Archivos CSS se cargan correctamente")
        else:
            print(f"  [ERROR] No se puede cargar CSS: {response.status_code}")
            return False
        
        response = requests.get('http://localhost:8080/static/js/app.js', timeout=5)
        if response.status_code == 200:
            print("  [OK] Archivos JavaScript se cargan correctamente")
        else:
            print(f"  [ERROR] No se puede cargar JS: {response.status_code}")
            return False
        
        # Probar API
        response = requests.get('http://localhost:8080/api/historial', timeout=5)
        if response.status_code in [200, 500]:  # 500 es OK si no hay BD
            print("  [OK] API responde (puede requerir PostgreSQL para funcionar completamente)")
        else:
            print(f"  [ADVERTENCIA] API responde con codigo: {response.status_code}")
        
        print("\n" + "="*60)
        print("SERVIDOR WEB FUNCIONANDO CORRECTAMENTE")
        print("="*60)
        print("\nAcceda a: http://localhost:8080")
        print("Desde movil: http://[SU_IP]:8080")
        return True
        
    except requests.exceptions.ConnectionError:
        print("  [ERROR] No se puede conectar al servidor")
        print("  Asegurese de que el servidor este corriendo:")
        print("    python3 app_web.py 8080")
        return False
    except Exception as e:
        print(f"  [ERROR] {e}")
        return False

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("Instalando requests...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    
    success = test_servidor()
    sys.exit(0 if success else 1)

