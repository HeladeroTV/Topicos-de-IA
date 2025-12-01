"""
Aplicacion Principal del Sistema de Deteccion de Matriculas
Interfaz de linea de comandos para interactuar con el sistema
"""

import os
import sys
from system.linking_system import LinkingSystem
from database.db_manager import DatabaseManager
import argparse

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "="*60)
    print("SISTEMA DE DETECCION DE MATRICULAS")
    print("="*60)
    print("1. Detectar matricula en imagen")
    print("2. Buscar propietario por numero de placa")
    print("3. Agregar nuevo propietario")
    print("4. Agregar nuevo vehiculo")
    print("5. Ver historial de detecciones")
    print("6. Salir")
    print("="*60)

def detectar_matricula(linker):
    """Funcion para detectar matricula en una imagen"""
    print("\n--- DETECCION DE MATRICULA ---")
    ruta_imagen = input("Ingrese la ruta de la imagen: ").strip()
    
    if not os.path.exists(ruta_imagen):
        print(f"Error: La imagen no existe en {ruta_imagen}")
        return
    
    print("\nProcesando imagen...")
    resultado = linker.procesar_imagen(ruta_imagen)
    
    print("\n" + "-"*60)
    print("RESULTADO DE LA DETECCION")
    print("-"*60)
    print(f"Numero de placa detectado: {resultado.get('numero_placa', 'N/A')}")
    print(f"Nivel de confianza: {resultado.get('confianza', 0):.2f}%")
    
    if resultado.get('propietario'):
        print("\n--- INFORMACION DEL PROPIETARIO ---")
        prop = resultado['propietario']
        print(f"Nombre: {prop['nombre_completo']}")
        print(f"Documento: {prop['documento_identidad']}")
        print(f"Telefono: {prop.get('telefono', 'N/A')}")
        print(f"Email: {prop.get('email', 'N/A')}")
        print(f"Direccion: {prop.get('direccion', 'N/A')}")
        
        if resultado.get('vehiculo'):
            print("\n--- INFORMACION DEL VEHICULO ---")
            veh = resultado['vehiculo']
            print(f"Marca: {veh['marca']}")
            print(f"Modelo: {veh['modelo']}")
            print(f"Año: {veh['año']}")
            print(f"Color: {veh.get('color', 'N/A')}")
    else:
        print("\nNo se encontro propietario registrado para esta placa")
    
    if resultado.get('error'):
        print(f"\nAdvertencia: {resultado['error']}")

def buscar_propietario(linker):
    """Funcion para buscar propietario por numero de placa"""
    print("\n--- BUSCAR PROPIETARIO ---")
    numero_placa = input("Ingrese el numero de placa: ").strip().upper()
    
    propietario = linker.buscar_propietario(numero_placa)
    
    if propietario:
        print("\n" + "-"*60)
        print("INFORMACION ENCONTRADA")
        print("-"*60)
        print(f"Numero de placa: {propietario['numero_placa']}")
        print(f"Marca: {propietario['marca']}")
        print(f"Modelo: {propietario['modelo']}")
        print(f"Año: {propietario['año']}")
        print(f"Color: {propietario.get('color', 'N/A')}")
        print(f"\nPropietario: {propietario['nombre_completo']}")
        print(f"Documento: {propietario['documento_identidad']}")
        print(f"Telefono: {propietario.get('telefono', 'N/A')}")
        print(f"Email: {propietario.get('email', 'N/A')}")
        print(f"Direccion: {propietario.get('direccion', 'N/A')}")
    else:
        print(f"\nNo se encontro informacion para la placa: {numero_placa}")

def agregar_propietario(db_manager):
    """Funcion para agregar un nuevo propietario"""
    print("\n--- AGREGAR NUEVO PROPIETARIO ---")
    nombre = input("Nombre completo: ").strip()
    documento = input("Documento de identidad: ").strip()
    telefono = input("Telefono (opcional): ").strip() or None
    email = input("Email (opcional): ").strip() or None
    direccion = input("Direccion (opcional): ").strip() or None
    
    if not nombre or not documento:
        print("Error: Nombre y documento son obligatorios")
        return
    
    propietario_id = db_manager.agregar_propietario(
        nombre, documento, telefono, email, direccion
    )
    
    if propietario_id:
        print(f"\nPropietario agregado exitosamente con ID: {propietario_id}")
    else:
        print("\nError al agregar el propietario. Verifique los datos.")

def agregar_vehiculo(db_manager):
    """Funcion para agregar un nuevo vehiculo"""
    print("\n--- AGREGAR NUEVO VEHICULO ---")
    numero_placa = input("Numero de placa: ").strip().upper()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    año = input("Año: ").strip()
    color = input("Color (opcional): ").strip() or None
    propietario_id = input("ID del propietario: ").strip()
    
    if not all([numero_placa, marca, modelo, año, propietario_id]):
        print("Error: Todos los campos son obligatorios excepto color")
        return
    
    try:
        año = int(año)
        propietario_id = int(propietario_id)
    except ValueError:
        print("Error: Año y ID de propietario deben ser numeros")
        return
    
    vehiculo_id = db_manager.agregar_vehiculo(
        numero_placa, marca, modelo, año, propietario_id, color
    )
    
    if vehiculo_id:
        print(f"\nVehiculo agregado exitosamente con ID: {vehiculo_id}")
    else:
        print("\nError al agregar el vehiculo. Verifique los datos.")

def ver_historial(linker):
    """Funcion para ver el historial de detecciones"""
    print("\n--- HISTORIAL DE DETECCIONES ---")
    limite = input("Numero de registros a mostrar (default 20): ").strip()
    limite = int(limite) if limite.isdigit() else 20
    
    historial = linker.obtener_historial(limite)
    
    if not historial:
        print("\nNo hay detecciones registradas")
        return
    
    print(f"\nMostrando {len(historial)} registros mas recientes:")
    print("-"*80)
    for det in historial:
        print(f"\nFecha: {det['fecha_deteccion']}")
        print(f"Placa detectada: {det['numero_placa_detectado']}")
        print(f"Confianza: {det['confianza']:.2f}%")
        print(f"Estado: {det['estado']}")
        if det.get('nombre_completo'):
            print(f"Propietario: {det['nombre_completo']}")
            print(f"Vehiculo: {det['marca']} {det['modelo']}")
        else:
            print("Propietario: No encontrado")
        print("-"*80)

def main():
    """Funcion principal"""
    parser = argparse.ArgumentParser(description='Sistema de Deteccion de Matriculas')
    parser.add_argument('--imagen', type=str, help='Ruta a imagen para procesar directamente')
    
    args = parser.parse_args()
    
    # Si se proporciona una imagen directamente, procesarla y salir
    if args.imagen:
        linker = LinkingSystem()
        resultado = linker.procesar_imagen(args.imagen)
        print(f"Placa detectada: {resultado.get('numero_placa', 'No detectada')}")
        if resultado.get('propietario'):
            print(f"Propietario: {resultado['propietario']['nombre_completo']}")
        linker.cerrar()
        return
    
    # Modo interactivo
    linker = LinkingSystem()
    db_manager = DatabaseManager()
    
    try:
        while True:
            mostrar_menu()
            opcion = input("\nSeleccione una opcion: ").strip()
            
            if opcion == '1':
                detectar_matricula(linker)
            elif opcion == '2':
                buscar_propietario(linker)
            elif opcion == '3':
                agregar_propietario(db_manager)
            elif opcion == '4':
                agregar_vehiculo(db_manager)
            elif opcion == '5':
                ver_historial(linker)
            elif opcion == '6':
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpcion no valida. Intente nuevamente.")
            
            input("\nPresione Enter para continuar...")
    
    except KeyboardInterrupt:
        print("\n\nSaliendo del sistema...")
    finally:
        linker.cerrar()
        db_manager.close()

if __name__ == "__main__":
    main()

