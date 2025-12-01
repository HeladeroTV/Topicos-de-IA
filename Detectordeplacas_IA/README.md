# 🚗🔍 Sistema de Detección de Matrículas

Sistema integral de detección de matrículas capaz de identificar a los propietarios de vehículos mediante visión artificial y una base de datos PostgreSQL.

## 📋 Descripción General del Proyecto

Este proyecto implementa un sistema completo que combina tecnologías de visión artificial con gestión de bases de datos para detectar y reconocer números de matrícula de vehículos, vinculándolos automáticamente con la información de sus propietarios registrados en la base de datos.

## 🎯 Objetivo General

El objetivo principal de este proyecto es crear un sistema que detecte con precisión las matrículas de los vehículos y las asocie con sus respectivos propietarios, proporcionando una solución integral para la identificación de vehículos mediante reconocimiento óptico de caracteres (OCR) y gestión de información en bases de datos relacionales.

## 📜 Descripción del Problema

En diversos contextos como seguridad, gestión de estacionamientos, control de acceso vehicular y aplicación de la ley, existe la necesidad de identificar rápidamente a los propietarios de vehículos a partir de sus placas. El proceso manual de identificación presenta varios desafíos:

- **Lentitud**: El proceso manual requiere tiempo considerable para verificar cada vehículo
- **Errores Humanos**: La lectura manual de placas es propensa a errores de transcripción
- **No Escalable**: Difícil de implementar en entornos con alto volumen de vehículos
- **Falta de Trazabilidad**: No hay registro automático de las verificaciones realizadas

Este sistema automatiza este proceso mediante el uso de tecnologías de visión artificial y bases de datos relacionales, proporcionando una solución eficiente, precisa y escalable.

## 💡 Justificación

Este proyecto es importante porque:

- **⚡ Automatización**: Reduce significativamente el tiempo necesario para identificar propietarios de vehículos, pasando de minutos a segundos
- **🎯 Precisión**: Minimiza errores humanos en la lectura de placas mediante algoritmos de visión artificial
- **📈 Escalabilidad**: Puede procesar grandes volúmenes de imágenes de manera eficiente sin degradación del rendimiento
- **📊 Trazabilidad**: Mantiene un registro completo de todas las detecciones realizadas con fecha, hora y nivel de confianza
- **🔒 Seguridad**: Útil en control de acceso vehicular, seguridad perimetral y vigilancia
- **🚦 Aplicación de la Ley**: Facilita la identificación rápida de vehículos en investigaciones
- **🅿️ Gestión de Estacionamientos**: Automatiza el control de acceso y facturación
- **🚛 Gestión de Flotas**: Permite el seguimiento automático de vehículos empresariales
- **🌍 Impacto Social**: Contribuye a la seguridad ciudadana y eficiencia en la gestión vehicular

## ⭐ Características Principales

- ✅ Detección automática de matrículas en imágenes utilizando EasyOCR
- 🗄️ Base de datos PostgreSQL para almacenamiento robusto de información
- 🔗 Sistema de vinculación automática entre placas detectadas y propietarios
- 💻 Interfaz de línea de comandos (CLI) intuitiva y fácil de usar
- 🌐 Interfaz web moderna y responsive
- 📝 Registro completo de todas las detecciones realizadas con historial
- 🔍 Búsqueda rápida de propietarios por número de placa
- ➕ Gestión completa de propietarios y vehículos (CRUD)
- 📊 Niveles de confianza para cada detección
- 📸 Procesamiento de imágenes con múltiples formatos

## 🔧 Componentes Clave del Sistema

### 1. 🗄️ Base de Datos (PostgreSQL)

**Propósito**: La base de datos sirve como el núcleo del sistema, almacenando información vital sobre los propietarios de vehículos y sus vehículos.

**Sistema de Gestión**: PostgreSQL - Base de datos relacional robusta y escalable

**Estructura de la Base de Datos:**

La base de datos almacena:
- 👤 **Información de propietarios**: Datos personales, contacto y documentación
- 🚙 **Información de vehículos**: Placas, marca, modelo, año, color y relación con propietarios
- 📝 **Historial de detecciones**: Registro completo de todas las detecciones realizadas

**Tablas Principales:**
- `propietarios`: Datos personales completos (nombre, documento, teléfono, email, dirección)
- `vehiculos`: Información detallada de vehículos y relación con propietarios
- `detecciones`: Registro de detecciones con nivel de confianza y estado

**Características de Diseño:**
- 🔑 Claves primarias y foráneas para integridad referencial
- 📊 Índices optimizados para búsquedas rápidas
- 🔗 Relaciones establecidas entre tablas (1:N entre propietarios y vehículos)
- 🛡️ Eliminación en cascada para mantener consistencia de datos

### 2. 🧠 Modelo de Visión Artificial

**Propósito**: Este modelo detecta y reconoce los números de matrícula de imágenes utilizando tecnología OCR avanzada.

**Framework Utilizado**: EasyOCR - Biblioteca de reconocimiento óptico de caracteres

**Proceso de Detección:**

1. 📸 **Recopilación de Datos**: Procesamiento de imágenes con diversas matrículas
2. 🔄 **Preprocesamiento**: 
   - Normalización de imágenes
   - Conversión a escala de grises
   - Mejora de contraste y reducción de ruido
   - Aplicación de filtros para mejor legibilidad
3. 🏋️‍♂️ **Reconocimiento**: Detección y lectura de texto en placas
4. ✅ **Validación**: Limpieza y normalización del texto detectado
5. 📊 **Evaluación**: Nivel de confianza para cada detección (0-100%)

**Capacidades:**
- Detectar texto en imágenes con diferentes ángulos e iluminación
- Reconocer números de placa alfanuméricos
- Proporcionar niveles de confianza para cada detección
- Funcionar sin GPU (optimizado para CPU)
- Soporta múltiples formatos de imagen

### 3. 🔗 Sistema de Vinculación

**Propósito**: Este sistema conecta los números de matrícula detectados con el propietario del vehículo correspondiente en la base de datos.

**Lógica de Enlace:**

Conecta automáticamente:
- 🔍 Matrículas detectadas con vehículos registrados en la base de datos
- 👤 Vehículos con sus respectivos propietarios
- 📝 Registra el estado de cada detección (verificada/no encontrada)

**Funcionalidades:**
- Búsqueda eficiente en base de datos por número de placa
- Consulta de información completa del propietario
- Registro automático de cada detección
- Manejo de casos donde la placa no está registrada

**⚠️ Manejo de Errores:**
- Casos donde no se encuentra una matrícula en la base de datos
- Imágenes sin placas detectables
- Errores de conexión a la base de datos
- Mensajes informativos al usuario
- Registro de errores para análisis posterior

## 💻 Requisitos del Sistema

- 🐍 **Python 3.8 o superior**
- 🗄️ **PostgreSQL 12 o superior**
- 💾 **4GB de RAM mínimo** (8GB recomendado)
- 💿 **Espacio en disco**: 2GB para dependencias
- 🌐 **Conexión a Internet** (para instalación inicial)

## ⚙️ Instalación Rápida

### 1️⃣ **Clonar o descargar el proyecto**

```bash
git clone <url_del_repositorio>
cd copia
```

### 2️⃣ **Instalar dependencias de Python**

```bash
pip install -r requirements.txt
```

### 3️⃣ **Configurar PostgreSQL**

- Crear base de datos: `license_plate_db`
- Copiar `config.env.example` a `.env`
- Configurar credenciales en `.env`

### 4️⃣ **Inicializar base de datos**

```bash
python database/init_db.py
```

### 5️⃣ **Ejecutar la aplicación**

```bash
# Interfaz CLI
python app.py

# Interfaz Web
python app_web.py
```

📖 Para instrucciones detalladas, consulte el **[📘 Manual de Instalación](MANUAL_INSTALACION.md)**

## 🚀 Uso Básico

### 📸 Procesar una Imagen

```bash
python app.py --imagen /ruta/a/imagen.jpg
```

### 💻 Modo Interactivo (CLI)

```bash
python app.py
```

**Menú de opciones:**
1. 🔍 Detectar matrícula en imagen
2. 👤 Buscar propietario por número de placa
3. ➕ Agregar nuevo propietario
4. 🚗 Agregar nuevo vehículo
5. 📊 Ver historial de detecciones
6. 🚪 Salir

### 🌐 Interfaz Web

```bash
python app_web.py
```

Acceda a: `http://localhost:8080`

📖 Para instrucciones detalladas, consulte el **[📗 Manual de Usuario](MANUAL_USUARIO.md)**

## 📁 Estructura del Proyecto

```
copia/
├── 📄 app.py                          # Aplicación principal (CLI)
├── 🌐 app_web.py                      # Aplicación web (Flask)
├── 📋 requirements.txt                # Dependencias de Python
├── ⚙️ config.env.example              # Ejemplo de configuración
├── 📘 README.md                       # Este archivo
├── 📑 DOCUMENTACION_TECNICA.md        # Documentación técnica completa
├── 📗 MANUAL_INSTALACION.md           # Manual de instalación paso a paso
├── 📕 MANUAL_USUARIO.md               # Manual de usuario final
├── 🔧 SOLUCION_PROBLEMAS.md           # Guía de solución de problemas
├── 🚀 iniciar.sh                      # Script para iniciar CLI
├── 🌐 iniciar_web.sh                  # Script para iniciar servidor web
│
├── 🗄️ database/                       # Módulo de base de datos
│   ├── schema.sql                    # Esquema de base de datos
│   ├── sample_data.sql               # Datos de ejemplo
│   ├── init_db.py                    # Script de inicialización
│   ├── db_manager.py                 # Gestor de base de datos
│   └── FUNCIONAMIENTO_BD.md          # Documentación de BD
│
├── 🧠 models/                         # Módulo de visión artificial
│   └── license_plate_detector.py     # Detector de matrículas OCR
│
├── 🔗 system/                         # Módulo de sistema de vinculación
│   └── linking_system.py             # Sistema de vinculación
│
├── 🎨 static/                         # Recursos estáticos web
│   ├── css/
│   │   └── style.css                 # Estilos de la interfaz web
│   └── js/
│       └── app.js                    # JavaScript del cliente
│
├── 📄 templates/                      # Plantillas HTML
│   └── index.html                    # Página principal web
│
└── 📤 uploads/                        # Carpeta para imágenes procesadas
```

## 📚 Documentación Completa

El proyecto incluye documentación exhaustiva para usuarios finales y desarrolladores:

### 📄 Documentación para Usuarios Finales

- **[📗 Manual de Usuario](MANUAL_USUARIO.md)**: Guía completa sobre cómo operar el sistema
  - Instrucciones paso a paso para cada funcionalidad
  - Capturas de pantalla y ejemplos
  - Casos de uso comunes
  - Consejos y mejores prácticas

- **[🔧 Solución de Problemas](SOLUCION_PROBLEMAS.md)**: Guía de troubleshooting
  - Problemas comunes y sus soluciones
  - Errores típicos durante la operación
  - Cómo obtener ayuda

### 📑 Documentación Técnica y Manual de Instalación

- **[📘 Manual de Instalación](MANUAL_INSTALACION.md)**: Proceso completo de instalación
  - Requisitos previos del sistema
  - Instalación de dependencias
  - Configuración de PostgreSQL
  - Configuración de variables de entorno
  - Inicialización de la base de datos
  - Verificación de la instalación

- **[📑 Documentación Técnica](DOCUMENTACION_TECNICA.md)**: Detalles técnicos completos
  - Arquitectura del sistema
  - Especificaciones de la base de datos
  - API y funciones principales
  - Detalles del modelo de visión artificial
  - Sistema de vinculación
  - Consideraciones de rendimiento y seguridad

- **[🗄️ Funcionamiento de la Base de Datos](database/FUNCIONAMIENTO_BD.md)**: Documentación de BD
  - Esquema detallado de tablas
  - Relaciones y claves foráneas
  - Índices y optimizaciones
  - Consultas SQL importantes

## 🗄️ Resumen del Funcionamiento de la Base de Datos

### Esquema de Base de Datos

La base de datos utiliza **PostgreSQL** y consta de tres tablas principales:

1. **👤 propietarios**: 
   - Almacena información personal completa
   - Campos: nombre, documento, teléfono, email, dirección
   - Clave primaria: `id`

2. **🚗 vehiculos**: 
   - Almacena información de vehículos y su relación con propietarios
   - Campos: placa, marca, modelo, año, color, propietario_id
   - Clave primaria: `id`
   - Clave foránea: `propietario_id` → `propietarios(id)`

3. **📝 detecciones**: 
   - Registra todas las detecciones realizadas por el sistema
   - Campos: placa detectada, confianza, fecha, estado, vehículo_id
   - Clave primaria: `id`
   - Clave foránea: `vehiculo_id` → `vehiculos(id)`

### 🔗 Relaciones

- Un propietario puede tener múltiples vehículos (relación 1:N)
- Un vehículo pertenece a un solo propietario
- Una detección puede estar asociada a un vehículo (si se encuentra en la BD)

### 🛡️ Integridad Referencial

- Las claves foráneas garantizan la integridad de los datos
- `ON DELETE CASCADE`: Vehículos se eliminan cuando se elimina un propietario
- `ON DELETE SET NULL`: Detecciones se preservan aunque se elimine un vehículo
- Índices optimizados para búsquedas rápidas por placa

## 🛠️ Tecnologías Utilizadas

- **🐍 Python 3.8+**: Lenguaje de programación principal
- **🗄️ PostgreSQL**: Sistema de gestión de bases de datos relacional
- **🧠 EasyOCR**: Biblioteca de reconocimiento óptico de caracteres (OCR)
- **📸 OpenCV**: Procesamiento y manipulación de imágenes
- **🔌 psycopg2**: Adaptador de PostgreSQL para Python
- **🌐 Flask**: Framework web para interfaz HTTP
- **🎨 HTML/CSS/JavaScript**: Interfaz web responsive
- **📦 NumPy**: Operaciones numéricas y manejo de arrays
- **🖼️ Pillow**: Manipulación adicional de imágenes

## ⚠️ Limitaciones y Consideraciones

- 📷 La precisión de la detección depende de la calidad de la imagen
- 🔍 Requiere que la placa sea claramente visible en la imagen
- ⏱️ El tiempo de procesamiento es de 2-5 segundos por imagen
- 📐 Funciona mejor con imágenes de alta resolución (mínimo 640x480)
- 🌙 Puede tener dificultades con ángulos extremos o iluminación deficiente
- 💾 Requiere espacio suficiente para almacenar imágenes procesadas

## 🤝 Contribuciones

Este es un proyecto académico desarrollado con fines educativos. Para sugerencias o mejoras:

1. 🐛 Reporte bugs abriendo un issue
2. 💡 Proponga nuevas características
3. 🔧 Envíe pull requests con mejoras
4. 📖 Mejore la documentación

## 📜 Licencia

Este proyecto es de uso educativo y académico.

## 👨‍💻 Autor

Sistema desarrollado como proyecto académico de detección de matrículas.

**Desarrollado con:** 🐍 Python | 🗄️ PostgreSQL | 🧠 EasyOCR | 📸 OpenCV

## 📌 Versión

**Versión 1.0.0** - Sistema completamente funcional

## 📞 Contacto y Soporte

Para problemas técnicos o preguntas:

- 📖 Consulte la documentación incluida
- 🔧 Revise la [Guía de Solución de Problemas](SOLUCION_PROBLEMAS.md)
- 📝 Revise los logs de error del sistema
- 💬 Abra un issue en el repositorio

## 🎯 Estado del Proyecto

✅ **Proyecto Completo y Funcional**

- [x] Base de datos PostgreSQL implementada
- [x] Modelo de visión artificial funcionando
- [x] Sistema de vinculación operativo
- [x] Interfaz CLI completa
- [x] Interfaz Web implementada
- [x] Documentación exhaustiva
- [x] Scripts de instalación
- [x] Tests implementados

---

**🚗🔍 Sistema de Detección de Matrículas** - Identificación automática de propietarios de vehículos mediante visión artificial

