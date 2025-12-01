# Inicio de la Interfaz Web

## Ejecutar el Servidor Web

Para iniciar la interfaz web del sistema de deteccion de matriculas:

```bash
python3 app_web.py
```

El servidor se iniciara en: **http://localhost:5000**

## Acceso desde Navegador

1. Abra su navegador web
2. La interfaz se adaptara automaticamente a dispositivos moviles y tablets

## Acceso desde Dispositivos Moviles

Para acceder desde un dispositivo movil en la misma red:

1. Encuentre la IP de su computadora:
   - macOS/Linux: `ifconfig | grep "inet "`
   - Windows: `ipconfig`

2. En su dispositivo movil, abra el navegador y vaya a:
   ```
   http://[IP_DE_SU_COMPUTADORA]:5000
   ```
   Ejemplo: `http://192.168.1.100:5000`

## Caracteristicas de la Interfaz Web

### Responsive Design
- Adaptacion automatica a pantallas moviles, tablets y desktop
- Menu de pestañas optimizado para touch
- Formularios adaptativos
- Vista previa de imagenes

### Funcionalidades Disponibles

1. **Detectar Matricula**: Suba una imagen y el sistema detectara la placa automaticamente
2. **Buscar Propietario**: Busque por numero de placa
3. **Agregar Registro**: Agregue nuevos propietarios y vehiculos
4. **Historial**: Vea todas las detecciones realizadas

## Requisitos

- Python 3.8+
- Flask instalado (incluido en requirements.txt)
- PostgreSQL configurado (para funcionalidad completa)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

## Solucion de Problemas

### El servidor no inicia
- Verifique que el puerto 5000 no este en uso
- Asegurese de tener Flask instalado: `pip3 install flask flask-cors`

### No se puede acceder desde el movil
- Verifique que el firewall permita conexiones en el puerto 5000
- Asegurese de que el dispositivo movil este en la misma red
- Use la IP correcta de su computadora

### Error al procesar imagenes
- Verifique que la carpeta `uploads/` exista y tenga permisos de escritura
- Asegurese de que las imagenes no excedan 16MB

## Detener el Servidor

Presione `Ctrl+C` en la terminal donde esta corriendo el servidor.

