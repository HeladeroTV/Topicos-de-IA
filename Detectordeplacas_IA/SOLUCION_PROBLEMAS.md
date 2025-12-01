# Solucion de Problemas - Interfaz Web

## El servidor no inicia

### Error: "Address already in use" o "Puerto en uso"

**Solucion:**
1. Detener procesos anteriores:
   ```bash
   lsof -ti:8080 | xargs kill -9
   ```

2. O usar otro puerto:
   ```bash
   python3 app_web.py 5001
   ```

3. En macOS, desactivar AirPlay Receiver:
   - System Settings > General > AirDrop & Handoff
   - Desactivar "AirPlay Receiver"

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solucion:**
```bash
pip3 install flask flask-cors
```

## No puedo acceder desde el navegador

### La pagina no carga

1. **Verificar que el servidor este corriendo:**
   ```bash
   lsof -ti:8080
   ```
   Si no muestra nada, el servidor no esta corriendo.

2. **Verificar la URL correcta:**
   - Local: http://localhost:8080
   - Desde otra computadora: http://[IP]:8080

3. **Verificar firewall:**
   - macOS: System Settings > Network > Firewall
   - Asegurese de permitir conexiones entrantes

### Error 404 en archivos estaticos

**Verificar estructura de carpetas:**
```bash
ls -la static/css/
ls -la static/js/
ls -la templates/
```

Deben existir:
- `static/css/style.css`
- `static/js/app.js`
- `templates/index.html`

## No funciona la deteccion de matriculas

### Error al subir imagen

1. **Verificar permisos de carpeta uploads:**
   ```bash
   mkdir -p uploads
   chmod 755 uploads
   ```

2. **Verificar tamaño de imagen:**
   - Maximo: 16MB
   - Formatos: JPG, PNG, BMP, GIF

### Error: "No se pudo detectar ninguna matricula"

- La imagen debe tener buena calidad
- La placa debe ser claramente visible
- Intentar con otra imagen

### Error de conexion a base de datos

**Verificar:**
1. PostgreSQL esta corriendo:
   ```bash
   pg_isready
   ```

2. Archivo .env configurado correctamente:
   ```bash
   cat .env
   ```

3. Base de datos inicializada:
   ```bash
   python3 database/init_db.py
   ```

## Problemas en dispositivos moviles

### No puedo acceder desde mi telefono

1. **Verificar que esten en la misma red WiFi**

2. **Obtener la IP de su computadora:**
   ```bash
   # macOS/Linux
   ifconfig | grep "inet " | grep -v 127.0.0.1
   
   # Windows
   ipconfig
   ```

3. **Usar la IP correcta:**
   ```
   http://[SU_IP]:8080
   ```
   Ejemplo: `http://192.168.1.100:8080`

4. **Verificar firewall:**
   - Permitir conexiones en puerto 8080

### La interfaz no se ve bien en movil

- Limpiar cache del navegador
- Usar navegador actualizado (Chrome, Safari, Firefox)
- Verificar que el viewport este configurado (ya incluido en el HTML)

## Errores comunes

### "Internal Server Error"

1. Verificar logs del servidor en la terminal
2. Verificar que todas las dependencias esten instaladas
3. Verificar permisos de archivos

### "CORS Error"

Ya esta configurado CORS en la aplicacion. Si persiste:
- Verificar que flask-cors este instalado
- Limpiar cache del navegador

### JavaScript no funciona

1. Abrir consola del navegador (F12)
2. Verificar errores en la consola
3. Verificar que app.js se este cargando:
   - Network tab > buscar app.js
   - Debe tener status 200

## Comandos utiles

### Reiniciar servidor
```bash
# Detener
lsof -ti:8080 | xargs kill -9

# Iniciar
python3 app_web.py 8080
```

### Ver logs en tiempo real
El servidor muestra logs automaticamente en la terminal donde se ejecuta.

### Probar servidor
```bash
python3 test_web.py
```

## Obtener ayuda

Si el problema persiste:

1. Verificar logs del servidor
2. Verificar consola del navegador (F12)
3. Verificar que todas las dependencias esten instaladas
4. Verificar que PostgreSQL este configurado (si se necesita funcionalidad completa)

