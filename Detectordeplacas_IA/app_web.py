"""
Aplicacion Web del Sistema de Deteccion de Matriculas
Interfaz web responsive para acceso desde navegador y dispositivos moviles
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
from system.linking_system import LinkingSystem
from database.db_manager import DatabaseManager

app = Flask(__name__)
CORS(app)

# Configuracion
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Crear carpeta de uploads si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Verifica si el archivo tiene una extension permitida"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Pagina principal"""
    return render_template('index.html')

@app.route('/api/detectar', methods=['POST'])
def detectar_matricula():
    """API para detectar matricula en una imagen"""
    try:
        if 'imagen' not in request.files:
            return jsonify({'error': 'No se proporciono ninguna imagen'}), 400
        
        file = request.files['imagen']
        if file.filename == '':
            return jsonify({'error': 'No se selecciono ningun archivo'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Tipo de archivo no permitido'}), 400
        
        # Guardar archivo
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Procesar imagen
        linker = LinkingSystem()
        resultado = linker.procesar_imagen(filepath, guardar_imagen=True)
        linker.cerrar()
        
        # Preparar respuesta
        respuesta = {
            'exito': resultado.get('exito', False),
            'numero_placa': resultado.get('numero_placa'),
            'confianza': resultado.get('confianza', 0),
            'propietario': resultado.get('propietario'),
            'vehiculo': resultado.get('vehiculo'),
            'imagen_url': f'/uploads/{unique_filename}'
        }
        
        if not resultado.get('exito'):
            respuesta['error'] = resultado.get('error', 'Error desconocido')
        
        return jsonify(respuesta)
        
    except Exception as e:
        return jsonify({'error': f'Error al procesar imagen: {str(e)}'}), 500

@app.route('/api/buscar', methods=['POST'])
def buscar_propietario():
    """API para buscar propietario por numero de placa"""
    try:
        data = request.get_json()
        numero_placa = data.get('numero_placa', '').strip().upper()
        
        if not numero_placa:
            return jsonify({'error': 'Numero de placa requerido'}), 400
        
        linker = LinkingSystem()
        propietario = linker.buscar_propietario(numero_placa)
        linker.cerrar()
        
        if propietario:
            return jsonify({
                'exito': True,
                'propietario': {
                    'id': propietario['propietario_id'],
                    'nombre_completo': propietario['nombre_completo'],
                    'documento_identidad': propietario['documento_identidad'],
                    'telefono': propietario.get('telefono'),
                    'email': propietario.get('email'),
                    'direccion': propietario.get('direccion')
                },
                'vehiculo': {
                    'id': propietario['vehiculo_id'],
                    'numero_placa': propietario['numero_placa'],
                    'marca': propietario['marca'],
                    'modelo': propietario['modelo'],
                    'año': propietario['año'],
                    'color': propietario.get('color')
                }
            })
        else:
            return jsonify({
                'exito': False,
                'error': f'No se encontro informacion para la placa: {numero_placa}'
            })
            
    except Exception as e:
        return jsonify({'error': f'Error al buscar propietario: {str(e)}'}), 500

@app.route('/api/propietario', methods=['POST'])
def agregar_propietario():
    """API para agregar un nuevo propietario"""
    try:
        data = request.get_json()
        
        nombre = data.get('nombre_completo', '').strip()
        documento = data.get('documento_identidad', '').strip()
        telefono = data.get('telefono', '').strip() or None
        email = data.get('email', '').strip() or None
        direccion = data.get('direccion', '').strip() or None
        
        if not nombre or not documento:
            return jsonify({'error': 'Nombre y documento son obligatorios'}), 400
        
        db_manager = DatabaseManager()
        propietario_id = db_manager.agregar_propietario(
            nombre, documento, telefono, email, direccion
        )
        db_manager.close()
        
        if propietario_id:
            return jsonify({
                'exito': True,
                'propietario_id': propietario_id,
                'mensaje': 'Propietario agregado exitosamente'
            })
        else:
            return jsonify({'error': 'Error al agregar el propietario'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Error al agregar propietario: {str(e)}'}), 500

@app.route('/api/vehiculo', methods=['POST'])
def agregar_vehiculo():
    """API para agregar un nuevo vehiculo"""
    try:
        data = request.get_json()
        
        numero_placa = data.get('numero_placa', '').strip().upper()
        marca = data.get('marca', '').strip()
        modelo = data.get('modelo', '').strip()
        año = data.get('año', '')
        color = data.get('color', '').strip() or None
        propietario_id = data.get('propietario_id')
        
        if not all([numero_placa, marca, modelo, año, propietario_id]):
            return jsonify({'error': 'Todos los campos son obligatorios excepto color'}), 400
        
        try:
            año = int(año)
            propietario_id = int(propietario_id)
        except ValueError:
            return jsonify({'error': 'Año y ID de propietario deben ser numeros'}), 400
        
        db_manager = DatabaseManager()
        vehiculo_id = db_manager.agregar_vehiculo(
            numero_placa, marca, modelo, año, propietario_id, color
        )
        db_manager.close()
        
        if vehiculo_id:
            return jsonify({
                'exito': True,
                'vehiculo_id': vehiculo_id,
                'mensaje': 'Vehiculo agregado exitosamente'
            })
        else:
            return jsonify({'error': 'Error al agregar el vehiculo'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Error al agregar vehiculo: {str(e)}'}), 500

@app.route('/api/historial', methods=['GET'])
def obtener_historial():
    """API para obtener el historial de detecciones"""
    try:
        limite = request.args.get('limite', 50, type=int)
        
        linker = LinkingSystem()
        historial = linker.obtener_historial(limite)
        linker.cerrar()
        
        return jsonify({
            'exito': True,
            'historial': historial,
            'total': len(historial)
        })
        
    except Exception as e:
        return jsonify({'error': f'Error al obtener historial: {str(e)}'}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Servir archivos subidos"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    import sys
    
    # Intentar usar puerto 8080, si no esta disponible usar 5001
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    
    print("="*60)
    print("SISTEMA DE DETECCION DE MATRICULAS - INTERFAZ WEB")
    print("="*60)
    print(f"Servidor iniciado en: http://localhost:{port}")
    print("Presione Ctrl+C para detener el servidor")
    print("="*60)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=port)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\nError: El puerto {port} esta en uso.")
            print("Intente con otro puerto: python3 app_web.py 5001")
            sys.exit(1)
        else:
            raise

