# Manual de Instalacion - Sistema de Deteccion de Matriculas

Este manual proporciona instrucciones detalladas para instalar y configurar el sistema de deteccion de matriculas en su entorno.

## Requisitos Previos

Antes de comenzar la instalacion, asegurese de tener instalado:

1. **Python 3.8 o superior**
   - Verificar version: `python3 --version`
   - Descargar desde: https://www.python.org/downloads/

2. **PostgreSQL 12 o superior**
   - Verificar version: `psql --version`
   - Descargar desde: https://www.postgresql.org/download/

3. **pip** (gestor de paquetes de Python)
   - Generalmente viene con Python
   - Verificar: `pip3 --version`

4. **Git** (opcional, para clonar el repositorio)
   - Verificar: `git --version`

## Paso 1: Instalacion de PostgreSQL

### En Windows

1. Descargue el instalador desde el sitio oficial de PostgreSQL
2. Ejecute el instalador y siga las instrucciones
3. Durante la instalacion, configure una contraseña para el usuario `postgres`
4. Asegurese de que el servicio de PostgreSQL este ejecutandose

### En Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### En macOS

```bash
brew install postgresql
brew services start postgresql
```

## Paso 2: Configuracion de PostgreSQL

1. Acceda a PostgreSQL como superusuario:

```bash
sudo -u postgres psql
```

O en Windows, use pgAdmin o la linea de comandos.

2. Cree la base de datos:

```sql
CREATE DATABASE license_plate_db;
```

3. Cree un usuario (opcional, puede usar el usuario postgres):

```sql
CREATE USER tu_usuario WITH PASSWORD 'tu_contraseña';
GRANT ALL PRIVILEGES ON DATABASE license_plate_db TO tu_usuario;
```

4. Salga de psql:

```sql
\q
```

## Paso 3: Clonar o Descargar el Proyecto

Si tiene acceso al repositorio Git:

```bash
git clone <url_del_repositorio>
cd copia
```

O descargue y extraiga el archivo ZIP del proyecto.

## Paso 4: Crear Entorno Virtual (Recomendado)

Es recomendable usar un entorno virtual para aislar las dependencias:

```bash
python3 -m venv venv
```

Activar el entorno virtual:

- En Linux/macOS:
```bash
source venv/bin/activate
```

- En Windows:
```bash
venv\Scripts\activate
```

## Paso 5: Instalar Dependencias

1. Navegue al directorio del proyecto:

```bash
cd copia
```

2. Instale las dependencias:

```bash
pip install -r requirements.txt
```

**Nota**: La instalacion de EasyOCR puede tardar varios minutos ya que descarga modelos de lenguaje. Sea paciente.

## Paso 6: Configurar Variables de Entorno

1. Copie el archivo de ejemplo:

```bash
cp config.env.example .env
```

2. Edite el archivo `.env` con sus credenciales de PostgreSQL:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=license_plate_db
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aqui
```

Reemplace `tu_contraseña_aqui` con la contraseña que configuro para PostgreSQL.

## Paso 7: Inicializar la Base de Datos

Ejecute el script de inicializacion:

```bash
python database/init_db.py
```

Este script creara todas las tablas necesarias en la base de datos.

Si ve el mensaje "Base de datos inicializada correctamente", la instalacion fue exitosa.

## Paso 8: (Opcional) Cargar Datos de Ejemplo

Para probar el sistema con datos de ejemplo:

```bash
psql -U postgres -d license_plate_db -f database/sample_data.sql
```

O desde psql:

```bash
psql -U postgres -d license_plate_db
\i database/sample_data.sql
```

## Paso 9: Verificar la Instalacion

Ejecute la aplicacion principal:

```bash
python app.py
```

Si aparece el menu principal, la instalacion fue exitosa.

## Solucion de Problemas

### Error: "No se pudo conectar con la base de datos"

- Verifique que PostgreSQL este ejecutandose:
  - Linux: `sudo systemctl status postgresql`
  - Windows: Verifique en Servicios
  - macOS: `brew services list`

- Verifique las credenciales en el archivo `.env`

- Verifique que la base de datos exista:
```bash
psql -U postgres -l
```

### Error: "ModuleNotFoundError: No module named 'easyocr'"

- Asegurese de que el entorno virtual este activado
- Reinstale las dependencias: `pip install -r requirements.txt`

### Error: "Permission denied" al acceder a PostgreSQL

- Verifique que el usuario tenga permisos sobre la base de datos
- En Linux, puede necesitar cambiar la configuracion de autenticacion en `pg_hba.conf`

### Error al instalar EasyOCR

EasyOCR requiere espacio en disco y tiempo para descargar modelos. Asegurese de tener:
- Al menos 2GB de espacio libre
- Conexion a internet estable
- Paciencia (puede tardar 5-10 minutos)

### Problemas con OpenCV

Si tiene problemas con OpenCV:

```bash
pip uninstall opencv-python
pip install opencv-python-headless
```

## Verificacion de Componentes

Para verificar que todo esta instalado correctamente:

1. **Python y dependencias**:
```bash
python -c "import cv2, easyocr, psycopg2; print('OK')"
```

2. **PostgreSQL**:
```bash
psql -U postgres -d license_plate_db -c "SELECT version();"
```

3. **Conexion desde Python**:
```bash
python -c "from database.db_manager import DatabaseManager; db = DatabaseManager(); print('Conexion OK' if db.conn else 'Error')"
```

## Siguiente Paso

Una vez completada la instalacion, consulte el **Manual de Usuario** para aprender a usar el sistema.

## Soporte

Si encuentra problemas durante la instalacion:

1. Revise los logs de error
2. Verifique que todos los requisitos previos esten instalados
3. Consulte la seccion de Solucion de Problemas
4. Revise la documentacion tecnica para detalles adicionales

