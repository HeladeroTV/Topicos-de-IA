# Manual de Usuario - Sistema de Deteccion de Matriculas

Este manual proporciona instrucciones detalladas sobre como usar el sistema de deteccion de matriculas.

## Inicio Rapido

Para iniciar el sistema, ejecute:

```bash
python app.py
```

Se mostrara un menu principal con las opciones disponibles.

## Menu Principal

El sistema presenta un menu con las siguientes opciones:

1. Detectar matricula en imagen
2. Buscar propietario por numero de placa
3. Agregar nuevo propietario
4. Agregar nuevo vehiculo
5. Ver historial de detecciones
6. Salir

## Funcionalidades Detalladas

### 1. Detectar Matricula en Imagen

Esta funcion permite procesar una imagen y detectar automaticamente el numero de placa, luego buscar el propietario en la base de datos.

**Pasos para usar:**

1. Seleccione la opcion 1 del menu principal
2. Ingrese la ruta completa a la imagen que desea procesar
   - Ejemplo: `/ruta/a/imagen.jpg` o `C:\ruta\a\imagen.jpg`
3. El sistema procesara la imagen (esto puede tardar unos segundos)
4. Se mostraran los resultados:
   - Numero de placa detectado
   - Nivel de confianza de la deteccion
   - Informacion del propietario (si se encuentra)
   - Informacion del vehiculo (si se encuentra)

**Formatos de imagen soportados:**
- JPG/JPEG
- PNG
- BMP
- TIFF

**Recomendaciones:**
- Use imagenes de buena calidad y resolucion
- Asegurese de que la placa sea claramente visible
- Evite angulos extremos o iluminacion deficiente
- El tiempo de procesamiento es de 2-5 segundos por imagen

**Ejemplo de uso desde linea de comandos:**

```bash
python app.py --imagen /ruta/a/placa.jpg
```

### 2. Buscar Propietario por Numero de Placa

Esta funcion permite buscar directamente un propietario en la base de datos usando el numero de placa.

**Pasos para usar:**

1. Seleccione la opcion 2 del menu principal
2. Ingrese el numero de placa a buscar
   - El sistema automaticamente convertira a mayusculas
   - No es necesario incluir espacios o guiones
3. Se mostrara la informacion encontrada:
   - Datos del vehiculo (marca, modelo, año, color)
   - Datos del propietario (nombre, documento, contacto)

**Nota:** Si la placa no esta registrada, se mostrara un mensaje indicando que no se encontro informacion.

### 3. Agregar Nuevo Propietario

Esta funcion permite registrar un nuevo propietario en el sistema.

**Pasos para usar:**

1. Seleccione la opcion 3 del menu principal
2. Complete el formulario con la informacion solicitada:
   - **Nombre completo**: Obligatorio
   - **Documento de identidad**: Obligatorio (debe ser unico)
   - **Telefono**: Opcional
   - **Email**: Opcional
   - **Direccion**: Opcional
3. El sistema validara los datos y creara el registro
4. Se mostrara el ID asignado al nuevo propietario

**Importante:** 
- El documento de identidad debe ser unico
- Necesitara el ID del propietario para agregar vehiculos

### 4. Agregar Nuevo Vehiculo

Esta funcion permite registrar un nuevo vehiculo y asociarlo a un propietario existente.

**Pasos para usar:**

1. Seleccione la opcion 4 del menu principal
2. Complete el formulario con la informacion solicitada:
   - **Numero de placa**: Obligatorio (debe ser unico)
   - **Marca**: Obligatorio (ej: Toyota, Honda, Ford)
   - **Modelo**: Obligatorio (ej: Corolla, Civic, Focus)
   - **Año**: Obligatorio (numero de 4 digitos)
   - **Color**: Opcional
   - **ID del propietario**: Obligatorio (debe existir en la base de datos)
3. El sistema validara los datos y creara el registro
4. Se mostrara el ID asignado al nuevo vehiculo

**Importante:**
- El numero de placa debe ser unico
- El propietario debe existir previamente en el sistema
- Puede encontrar el ID del propietario consultando la base de datos o usando la opcion 2

### 5. Ver Historial de Detecciones

Esta funcion muestra un registro de todas las detecciones realizadas por el sistema.

**Pasos para usar:**

1. Seleccione la opcion 5 del menu principal
2. Ingrese el numero de registros que desea ver (por defecto 20)
3. Se mostrara una lista de detecciones con:
   - Fecha y hora de la deteccion
   - Numero de placa detectado
   - Nivel de confianza
   - Estado (verificada/no_encontrada)
   - Informacion del propietario (si se encontro)

**Informacion mostrada:**
- Las detecciones se ordenan de mas reciente a mas antigua
- Se indica si la placa fue encontrada en la base de datos
- Se muestra el nivel de confianza de cada deteccion

## Flujo de Trabajo Recomendado

### Escenario 1: Procesar una Imagen Nueva

1. Tome o obtenga una imagen de un vehiculo con la placa visible
2. Use la opcion 1 para procesar la imagen
3. Revise los resultados:
   - Si se encontro el propietario, la informacion estara disponible
   - Si no se encontro, puede agregar el vehiculo usando las opciones 3 y 4

### Escenario 2: Registrar un Vehiculo Nuevo

1. Primero agregue el propietario (opcion 3)
2. Anote el ID del propietario que se le asigna
3. Agregue el vehiculo asociado (opcion 4)
4. Use el ID del propietario al agregar el vehiculo

### Escenario 3: Consultar Informacion de una Placa

1. Si conoce el numero de placa, use la opcion 2
2. Si solo tiene una imagen, use la opcion 1

## Interpretacion de Resultados

### Nivel de Confianza

El nivel de confianza indica que tan seguro esta el sistema de que la deteccion es correcta:

- **90-100%**: Muy alta confianza, deteccion muy probablemente correcta
- **70-89%**: Alta confianza, deteccion probablemente correcta
- **50-69%**: Confianza media, revisar manualmente
- **Menos de 50%**: Baja confianza, puede ser incorrecta

### Estados de Deteccion

- **Verificada**: La placa fue detectada y encontrada en la base de datos
- **No encontrada**: La placa fue detectada pero no existe en la base de datos
- **Pendiente**: La deteccion esta en proceso (raro)

## Consejos y Mejores Practicas

1. **Calidad de Imagenes:**
   - Use imagenes de al menos 640x480 pixeles
   - Asegurese de que la placa este enfocada
   - Evite reflejos o sombras sobre la placa

2. **Formato de Placas:**
   - El sistema funciona mejor con placas que tienen texto claro
   - Puede tener dificultades con placas muy sucias o danadas
   - Funciona con varios formatos de placa

3. **Mantenimiento de Datos:**
   - Mantenga la base de datos actualizada
   - Revise periodicamente el historial de detecciones
   - Agregue nuevos vehiculos cuando sea necesario

4. **Rendimiento:**
   - El procesamiento puede tardar 2-5 segundos por imagen
   - Para multiples imagenes, proceselas una por una
   - El sistema funciona mejor con imagenes individuales

## Solucion de Problemas Comunes

### Problema: "No se pudo detectar ninguna matricula"

**Soluciones:**
- Verifique que la imagen sea clara y la placa visible
- Intente con otra imagen del mismo vehiculo
- Asegurese de que el formato de imagen sea compatible
- Verifique que la ruta a la imagen sea correcta

### Problema: "No se encontro propietario para la placa"

**Soluciones:**
- Verifique que el numero de placa este correctamente registrado
- Agregue el vehiculo y propietario usando las opciones 3 y 4
- Revise que no haya errores de escritura en el numero de placa

### Problema: "Error al conectar con la base de datos"

**Soluciones:**
- Verifique que PostgreSQL este ejecutandose
- Revise las credenciales en el archivo `.env`
- Consulte el Manual de Instalacion para configuracion

### Problema: "El documento de identidad ya existe"

**Soluciones:**
- Cada propietario debe tener un documento unico
- Verifique que no este intentando duplicar un registro
- Use la opcion 2 para buscar propietarios existentes

## Preguntas Frecuentes

**P: ¿Puedo procesar multiples imagenes a la vez?**
R: Actualmente el sistema procesa una imagen a la vez. Puede ejecutar el comando multiples veces o usar scripts personalizados.

**P: ¿Que formatos de placa soporta el sistema?**
R: El sistema puede detectar cualquier placa con texto alfanumerico visible, independientemente del formato.

**P: ¿Se guardan las imagenes procesadas?**
R: Solo se guarda la ruta de la imagen en la base de datos, no la imagen en si. Las imagenes originales no se modifican.

**P: ¿Puedo eliminar registros?**
R: Los registros se pueden eliminar directamente desde PostgreSQL. El sistema actual no incluye interfaz para eliminacion.

**P: ¿El sistema funciona con video?**
R: Actualmente solo procesa imagenes estaticas. Para video, procese frames individuales.

## Siguiente Paso

Para detalles tecnicos sobre la arquitectura y configuracion avanzada, consulte la **Documentacion Tecnica**.

