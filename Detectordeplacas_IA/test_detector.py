#!/usr/bin/env python3
"""
Script de prueba para el detector mejorado de matriculas
"""

import sys
import os
from models.license_plate_detector import LicensePlateDetector

def test_detector(imagen_path):
    """Prueba el detector con una imagen"""
    if not os.path.exists(imagen_path):
        print(f"Error: La imagen no existe: {imagen_path}")
        return
    
    print("="*60)
    print("PRUEBA DEL DETECTOR MEJORADO DE MATRICULAS")
    print("="*60)
    print(f"\nImagen: {imagen_path}")
    print("\nInicializando detector...")
    
    detector = LicensePlateDetector()
    
    print("\nProcesando imagen...")
    print("(Esto puede tardar unos segundos)")
    
    placa, confianza = detector.detectar_matricula(imagen_path, confianza_minima=0.3)
    
    print("\n" + "="*60)
    print("RESULTADO")
    print("="*60)
    
    if placa:
        print(f"Placa detectada: {placa}")
        print(f"Confianza: {confianza:.2f}%")
        
        # Validar formato
        es_valido, score = detector.validar_formato_placa(placa)
        print(f"Formato valido: {es_valido}")
        print(f"Score de formato: {score:.2f}")
    else:
        print("No se detecto ninguna placa")
    
    print("="*60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 test_detector.py <ruta_a_imagen>")
        print("\nEjemplo:")
        print("  python3 test_detector.py uploads/imagen.jpg")
        sys.exit(1)
    
    imagen_path = sys.argv[1]
    test_detector(imagen_path)

