# Funcionalidad de Cámara - Sistema de Detección de Matrículas

## Descripción

El sistema ahora permite capturar imágenes directamente desde la cámara del dispositivo (webcam o cámara del móvil) y procesarlas de la misma forma que las imágenes subidas desde archivo.

## Características

### Compatibilidad
- **Desktop**: Usa la webcam del computador
- **Móviles**: Usa la cámara del dispositivo (preferiblemente cámara trasera)
- **Tablets**: Compatible con cámaras frontales y traseras

### Funcionalidades
1. **Acceso a cámara**: Solicita permiso para acceder a la cámara del dispositivo
2. **Vista previa en vivo**: Muestra el video de la cámara en tiempo real
3. **Captura de foto**: Permite capturar una foto del video en vivo
4. **Procesamiento**: Procesa la foto capturada con el mismo detector mejorado
5. **Alternancia**: Puede cambiar entre cámara y subida de archivo

## Cómo Usar

### Desde Desktop

1. Abra la aplicación en el navegador: http://localhost:8080
2. Vaya a la pestaña "Detectar Matrícula"
3. Haga clic en el botón "Usar Cámara"
4. Permita el acceso a la cámara cuando el navegador lo solicite
5. Apunte la cámara hacia la placa del vehículo
6. Haga clic en "Capturar Foto"
7. Revise la foto capturada
8. Haga clic en "Procesar Esta Foto"
9. El sistema procesará la imagen y mostrará los resultados

### Desde Dispositivo Móvil

1. Abra la aplicación en el navegador móvil: http://[IP]:8080
2. Vaya a la pestaña "Detectar Matrícula"
3. Toque el botón "Usar Cámara"
4. Permita el acceso a la cámara cuando el navegador lo solicite
5. Apunte la cámara hacia la placa del vehículo
6. Toque "Capturar Foto"
7. Revise la foto capturada
8. Toque "Procesar Esta Foto"
9. El sistema procesará la imagen y mostrará los resultados

## Controles Disponibles

### Botones de Modo
- **Usar Cámara**: Cambia al modo de captura desde cámara
- **Usar Archivo**: Vuelve al modo de subida de archivo

### Controles de Cámara
- **Capturar Foto**: Toma una foto del video en vivo
- **Detener Cámara**: Detiene el video y libera la cámara

### Controles de Foto Capturada
- **Procesar Esta Foto**: Envía la foto al servidor para procesamiento
- **Descartar**: Descarta la foto y permite capturar otra

## Requisitos

### Navegador
- Chrome 53+ (recomendado)
- Firefox 36+
- Safari 11+
- Edge 12+

### Permisos
- El navegador solicitará permiso para acceder a la cámara
- Debe permitir el acceso para que funcione
- En móviles, puede requerir HTTPS (en producción)

### Conexión
- HTTPS recomendado para dispositivos móviles (en producción)
- HTTP funciona en localhost y redes locales

## Características Técnicas

### Resolución de Video
- Resolución ideal: 1280x720
- Se adapta automáticamente a la capacidad del dispositivo
- Optimizado para rendimiento

### Calidad de Captura
- Formato: JPEG
- Calidad: 95%
- Procesamiento: Mismo detector mejorado que archivos

### Compatibilidad Móvil
- Prefiere cámara trasera en dispositivos móviles
- Soporta orientación vertical y horizontal
- Interfaz adaptativa para pantallas táctiles

## Solución de Problemas

### La cámara no inicia

**Problema**: El botón "Usar Cámara" no funciona

**Soluciones**:
1. Verificar que el navegador soporte `getUserMedia()`
2. Verificar permisos de cámara en configuración del navegador
3. Asegurarse de que no hay otra aplicación usando la cámara
4. Intentar en otro navegador

### No se puede acceder a la cámara en móvil

**Problema**: El navegador no solicita permiso o muestra error

**Soluciones**:
1. Usar HTTPS (en producción) o localhost (en desarrollo)
2. Verificar permisos de cámara en configuración del dispositivo
3. Intentar en otro navegador móvil
4. Verificar que la cámara no esté siendo usada por otra app

### La foto capturada está borrosa

**Problema**: La imagen no es clara

**Soluciones**:
1. Asegurarse de que hay buena iluminación
2. Mantener el dispositivo estable al capturar
3. Acercarse más a la placa
4. Limpiar el lente de la cámara

### El procesamiento falla

**Problema**: La foto se captura pero no se procesa

**Soluciones**:
1. Verificar conexión a internet/servidor
2. Intentar capturar otra foto
3. Verificar que la placa sea claramente visible
4. Revisar consola del navegador para errores

## Mejores Prácticas

### Para Mejor Detección

1. **Iluminación**: Asegurar buena iluminación sobre la placa
2. **Distancia**: Mantener distancia adecuada (no muy cerca, no muy lejos)
3. **Ángulo**: Capturar desde frente, evitando ángulos extremos
4. **Estabilidad**: Mantener el dispositivo estable al capturar
5. **Enfoque**: Asegurar que la placa esté enfocada

### Para Rendimiento

1. **Detener cámara**: Detener la cámara cuando no se use para ahorrar recursos
2. **Una foto a la vez**: Procesar una foto antes de capturar otra
3. **Conexión estable**: Usar WiFi cuando sea posible

## Seguridad y Privacidad

- Las imágenes capturadas se procesan en el servidor
- No se almacenan permanentemente (solo temporalmente para procesamiento)
- El acceso a la cámara requiere permiso explícito del usuario
- Las imágenes se eliminan después del procesamiento

## Limitaciones Actuales

- No hay procesamiento en tiempo real (solo captura y procesa)
- Requiere conexión al servidor para procesar
- La calidad depende de la cámara del dispositivo
- En algunos navegadores móviles requiere HTTPS

## Próximas Mejoras

Posibles mejoras futuras:
- Procesamiento en tiempo real con detección automática
- Indicador visual cuando se detecta una placa
- Modo de captura continua
- Mejora de calidad de imagen automática
- Soporte para múltiples cámaras

