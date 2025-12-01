# Documentacion Tecnica - Sistema de Deteccion de Matriculas

## Indice

1. [Arquitectura del Sistema](#arquitectura-del-sistema)
2. [Especificaciones de la Base de Datos](#especificaciones-de-la-base-de-datos)
3. [Modelo de Vision Artificial](#modelo-de-vision-artificial)
4. [Sistema de Vinculacion](#sistema-de-vinculacion)
5. [Instalacion y Configuracion](#instalacion-y-configuracion)
6. [API y Funciones Principales](#api-y-funciones-principales)
7. [Estructura del Proyecto](#estructura-del-proyecto)

## Arquitectura del Sistema

El sistema de deteccion de matriculas esta compuesto por tres componentes principales:

### 1. Base de Datos (PostgreSQL)

La base de datos almacena toda la informacion relacionada con propietarios, vehiculos y detecciones. Utiliza PostgreSQL como sistema de gestion de bases de datos relacionales.

### 2. Modelo de Vision Artificial

El modelo utiliza EasyOCR, una biblioteca de reconocimiento optico de caracteres (OCR) que puede detectar y leer texto en imagenes. El modelo esta entrenado para reconocer caracteres alfanumericos en varios idiomas.

### 3. Sistema de Vinculacion

El sistema de vinculacion conecta las matriculas detectadas por el modelo de vision artificial con los propietarios registrados en la base de datos.

## Especificaciones de la Base de Datos

### Esquema de Base de Datos

#### Tabla: propietarios

Almacena la informacion personal de los propietarios de vehiculos.

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| id | SERIAL PRIMARY KEY | Identificador unico del propietario |
| nombre_completo | VARCHAR(255) | Nombre completo del propietario |
| documento_identidad | VARCHAR(50) UNIQUE | Numero de documento de identidad |
| telefono | VARCHAR(20) | Numero de telefono de contacto |
| email | VARCHAR(255) | Direccion de correo electronico |
| direccion | TEXT | Direccion de residencia |
| fecha_registro | TIMESTAMP | Fecha y hora de registro en el sistema |
| activo | BOOLEAN | Estado activo/inactivo del registro |

#### Tabla: vehiculos

Almacena la informacion de los vehiculos y su relacion con los propietarios.

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| id | SERIAL PRIMARY KEY | Identificador unico del vehiculo |
| numero_placa | VARCHAR(20) UNIQUE | Numero de placa del vehiculo |
| marca | VARCHAR(100) | Marca del vehiculo |
| modelo | VARCHAR(100) | Modelo del vehiculo |
| año | INTEGER | Año de fabricacion |
| color | VARCHAR(50) | Color del vehiculo |
| propietario_id | INTEGER | Referencia al propietario (FK) |
| fecha_registro | TIMESTAMP | Fecha y hora de registro |
| activo | BOOLEAN | Estado activo/inactivo |

**Relacion**: Un vehiculo pertenece a un propietario (relacion 1:N)

#### Tabla: detecciones

Registra todas las detecciones de matriculas realizadas por el sistema.

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| id | SERIAL PRIMARY KEY | Identificador unico de la deteccion |
| numero_placa_detectado | VARCHAR(20) | Numero de placa detectado |
| vehiculo_id | INTEGER | Referencia al vehiculo si se encontro (FK) |
| confianza | DECIMAL(5,2) | Nivel de confianza de la deteccion (0-100) |
| ruta_imagen | TEXT | Ruta de la imagen procesada |
| fecha_deteccion | TIMESTAMP | Fecha y hora de la deteccion |
| estado | VARCHAR(50) | Estado: pendiente, verificada, no_encontrada |

**Relacion**: Una deteccion puede estar asociada a un vehiculo (relacion N:1)

### Indices

Para optimizar las consultas, se han creado los siguientes indices:

- `idx_vehiculos_placa`: Sobre `vehiculos.numero_placa` para busquedas rapidas por placa
- `idx_vehiculos_propietario`: Sobre `vehiculos.propietario_id` para joins eficientes
- `idx_detecciones_placa`: Sobre `detecciones.numero_placa_detectado` para busquedas
- `idx_detecciones_fecha`: Sobre `detecciones.fecha_deteccion` para ordenamiento temporal

### Integridad Referencial

- La relacion entre `vehiculos` y `propietarios` utiliza `ON DELETE CASCADE`, lo que significa que si se elimina un propietario, se eliminan sus vehiculos asociados.
- La relacion entre `detecciones` y `vehiculos` utiliza `ON DELETE SET NULL`, preservando el historial de detecciones incluso si se elimina un vehiculo.

## Modelo de Vision Artificial

### Tecnologia Utilizada

El sistema utiliza **EasyOCR**, una biblioteca de OCR de codigo abierto que:

- Soporta mas de 80 idiomas
- No requiere entrenamiento previo
- Funciona con CPU (no requiere GPU)
- Proporciona niveles de confianza para cada deteccion

### Proceso de Deteccion

1. **Carga de Imagen**: La imagen se carga desde el sistema de archivos
2. **Preprocesamiento** (opcional):
   - Conversion a escala de grises
   - Filtrado bilateral para reducir ruido
   - Aplicacion de umbral adaptativo
3. **Reconocimiento OCR**: EasyOCR analiza la imagen y detecta texto
4. **Limpieza de Texto**: 
   - Conversion a mayusculas
   - Eliminacion de caracteres especiales
   - Normalizacion de caracteres confusos (O->0, I->1, S->5)
5. **Validacion**: Se verifica que el texto tenga al menos 4 caracteres alfanumericos
6. **Retorno**: Se retorna el texto limpio y el nivel de confianza

### Limitaciones

- La precision depende de la calidad de la imagen
- Requiere que la placa sea claramente visible
- Puede tener dificultades con angulos extremos o iluminacion deficiente
- El tiempo de procesamiento varia segun el tamano de la imagen

## Sistema de Vinculacion

### Flujo de Procesamiento

1. **Deteccion**: El sistema detecta el numero de placa en la imagen
2. **Busqueda en BD**: Se consulta la base de datos para encontrar el vehiculo con esa placa
3. **Vinculacion**: Si se encuentra, se obtiene la informacion del propietario
4. **Registro**: Se guarda la deteccion en la tabla `detecciones` con el estado correspondiente:
   - `verificada`: Si se encontro el vehiculo en la BD
   - `no_encontrada`: Si no se encontro el vehiculo

### Manejo de Errores

El sistema maneja graciosamente los siguientes casos:

- Imagen no encontrada
- No se detecta ninguna placa en la imagen
- Placa detectada pero no encontrada en la base de datos
- Errores de conexion a la base de datos
- Errores en el procesamiento de la imagen

Todos los errores se registran y se proporcionan mensajes informativos al usuario.

## Instalacion y Configuracion

### Requisitos del Sistema

- Python 3.8 o superior
- PostgreSQL 12 o superior
- 4GB de RAM minimo (recomendado 8GB)
- Espacio en disco: 2GB para dependencias

### Dependencias de Software

Las dependencias principales son:

- `opencv-python`: Procesamiento de imagenes
- `easyocr`: Reconocimiento optico de caracteres
- `psycopg2-binary`: Conexion a PostgreSQL
- `python-dotenv`: Gestion de variables de entorno
- `numpy`: Operaciones numericas
- `Pillow`: Manipulacion de imagenes
- `flask`: Servidor web (opcional, para futuras extensiones)

### Variables de Entorno

El sistema requiere las siguientes variables de entorno (configuradas en `.env`):

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=license_plate_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña
```

## API y Funciones Principales

### DatabaseManager

Clase para gestionar operaciones de base de datos.

#### Metodos Principales

- `buscar_propietario_por_placa(numero_placa)`: Busca propietario por numero de placa
- `registrar_deteccion(...)`: Registra una deteccion en la BD
- `agregar_propietario(...)`: Agrega un nuevo propietario
- `agregar_vehiculo(...)`: Agrega un nuevo vehiculo
- `obtener_historial_detecciones(limite)`: Obtiene historial de detecciones

### LicensePlateDetector

Clase para detectar matriculas en imagenes.

#### Metodos Principales

- `detectar_matricula(imagen, confianza_minima)`: Detecta placa en imagen
- `detectar_matricula_avanzado(...)`: Version con preprocesamiento avanzado
- `preprocesar_imagen(imagen)`: Preprocesa imagen para mejor deteccion
- `limpiar_texto_placa(texto)`: Limpia y normaliza texto detectado

### LinkingSystem

Sistema principal que integra deteccion y vinculacion.

#### Metodos Principales

- `procesar_imagen(ruta_imagen)`: Procesa imagen completa (deteccion + vinculacion)
- `buscar_propietario(numero_placa)`: Busca propietario directamente
- `obtener_historial(limite)`: Obtiene historial de detecciones

## Estructura del Proyecto

```
copia/
├── app.py                          # Aplicacion principal (CLI)
├── requirements.txt                # Dependencias de Python
├── config.env.example              # Ejemplo de variables de entorno
├── README.md                       # Documentacion principal
├── DOCUMENTACION_TECNICA.md        # Esta documentacion
├── MANUAL_INSTALACION.md           # Manual de instalacion
├── MANUAL_USUARIO.md               # Manual de usuario
├── database/
│   ├── schema.sql                  # Esquema de base de datos
│   ├── sample_data.sql             # Datos de ejemplo
│   ├── init_db.py                  # Script de inicializacion
│   └── db_manager.py               # Gestor de base de datos
├── models/
│   └── license_plate_detector.py   # Modelo de vision artificial
└── system/
    └── linking_system.py           # Sistema de vinculacion
```

## Consideraciones de Rendimiento

- El tiempo de deteccion promedio es de 2-5 segundos por imagen
- La base de datos puede manejar miles de registros eficientemente gracias a los indices
- Se recomienda procesar imagenes en lotes para mejor rendimiento
- El modelo OCR funciona mejor con imagenes de alta resolucion (minimo 640x480)

## Seguridad

- Las contraseñas de base de datos deben almacenarse en variables de entorno
- No se recomienda exponer la base de datos directamente a internet
- Las imagenes procesadas pueden contener informacion sensible; considerar encriptacion
- Implementar autenticacion para acceso a funciones administrativas

## Extensiones Futuras

Posibles mejoras al sistema:

- Interfaz web con Flask/FastAPI
- Procesamiento de video en tiempo real
- API REST para integracion con otros sistemas
- Dashboard de estadisticas y analiticas
- Sistema de alertas para placas no registradas
- Mejora del modelo con entrenamiento personalizado
- Soporte para multiples formatos de placa

