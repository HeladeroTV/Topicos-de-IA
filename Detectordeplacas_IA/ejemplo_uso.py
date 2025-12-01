"""
Ejemplo de uso del Sistema de Deteccion de Matriculas
Este script demuestra como usar las diferentes funcionalidades del sistema
"""

from system.linking_system import LinkingSystem
from database.db_manager import DatabaseManager

def ejemplo_completo():
    """Ejemplo completo de uso del sistema"""
    
    print("="*60)
    print("EJEMPLO DE USO DEL SISTEMA DE DETECCION DE MATRICULAS")
    print("="*60)
    
    # Inicializar el sistema
    linker = LinkingSystem()
    db_manager = DatabaseManager()
    
    try:
        # Ejemplo 1: Agregar un propietario
        print("\n1. Agregando un nuevo propietario...")
        propietario_id = db_manager.agregar_propietario(
            nombre_completo="Pedro Martinez",
            documento_identidad="99887766F",
            telefono="555-9999",
            email="pedro.martinez@email.com",
            direccion="Avenida Ejemplo 789"
        )
        
        if propietario_id:
            print(f"   Propietario agregado con ID: {propietario_id}")
            
            # Ejemplo 2: Agregar un vehiculo para ese propietario
            print("\n2. Agregando un vehiculo para el propietario...")
            vehiculo_id = db_manager.agregar_vehiculo(
                numero_placa="TEST1234",
                marca="Toyota",
                modelo="Camry",
                año=2021,
                propietario_id=propietario_id,
                color="Blanco"
            )
            
            if vehiculo_id:
                print(f"   Vehiculo agregado con ID: {vehiculo_id}")
        
        # Ejemplo 3: Buscar propietario por placa
        print("\n3. Buscando propietario por numero de placa...")
        propietario = linker.buscar_propietario("TEST1234")
        
        if propietario:
            print(f"   Propietario encontrado: {propietario['nombre_completo']}")
            print(f"   Vehiculo: {propietario['marca']} {propietario['modelo']} {propietario['año']}")
        else:
            print("   No se encontro propietario para esa placa")
        
        # Ejemplo 4: Procesar una imagen (requiere que exista una imagen)
        print("\n4. Ejemplo de procesamiento de imagen...")
        print("   Nota: Para procesar una imagen real, use:")
        print("   resultado = linker.procesar_imagen('/ruta/a/imagen.jpg')")
        
        # Ejemplo 5: Obtener historial
        print("\n5. Obteniendo historial de detecciones...")
        historial = linker.obtener_historial(limite=5)
        print(f"   Se encontraron {len(historial)} detecciones recientes")
        
        for det in historial[:3]:  # Mostrar solo las primeras 3
            print(f"   - {det['fecha_deteccion']}: {det['numero_placa_detectado']} "
                  f"(Confianza: {det['confianza']:.2f}%)")
        
        print("\n" + "="*60)
        print("Ejemplo completado exitosamente")
        print("="*60)
        
    except Exception as e:
        print(f"\nError durante el ejemplo: {e}")
    
    finally:
        # Cerrar conexiones
        linker.cerrar()
        db_manager.close()

def ejemplo_busqueda():
    """Ejemplo de busqueda de propietario"""
    print("\n--- EJEMPLO DE BUSQUEDA ---")
    
    linker = LinkingSystem()
    
    try:
        # Buscar por placa
        placa = "ABC1234"  # Cambiar por una placa existente
        resultado = linker.buscar_propietario(placa)
        
        if resultado:
            print(f"\nInformacion encontrada para placa {placa}:")
            print(f"Propietario: {resultado['nombre_completo']}")
            print(f"Documento: {resultado['documento_identidad']}")
            print(f"Vehiculo: {resultado['marca']} {resultado['modelo']}")
        else:
            print(f"\nNo se encontro informacion para la placa: {placa}")
    
    finally:
        linker.cerrar()

if __name__ == "__main__":
    # Ejecutar ejemplo completo
    ejemplo_completo()
    
    # Ejecutar ejemplo de busqueda
    # ejemplo_busqueda()

