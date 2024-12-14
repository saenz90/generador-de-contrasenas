# Generador de Contraseñas Seguras

Esta aplicación en Python genera contraseñas seguras basadas en las preferencias del usuario. Permite personalizar la contraseña en cuanto a longitud y tipo de caracteres (mayúsculas, minúsculas, números y símbolos especiales), asegurando así la creación de contraseñas robustas y difíciles de adivinar.

## Características

- **Personalización de contraseñas**: Puedes elegir si deseas incluir mayúsculas, minúsculas, números y símbolos especiales.
- **Longitud mínima de la contraseña**: La aplicación asegura que la longitud mínima de la contraseña sea de 8 caracteres.
- **Validación de entradas**: Se valida que el usuario ingrese respuestas correctas para las opciones de tipo de caracteres y la longitud de la contraseña. Si se introduce un valor no válido, el programa pide la entrada nuevamente.

## Requisitos

- Python 3.11 o superior.

## Instalación

### Pasos para descargar y ejecutar el código en tu máquina local:

1. **Descargar repositorio o archivo.py**:
   Puedes descargar el archivo ZIP del repositorio con el boton verde que dice `<> code` -> `Download ZIP` y descomprimirlo en tu máquina o descargar el archivo "generador.py" manualmente.

2. **Acceder al directorio y abrir la linea de comandos (cmd)**:
   Una vez descargado el repositorio, navega a la carpeta que tengas el proyecto con tu explorador de archivos, presiona `Ctrl` + `L`, escribe cmd.exe y presiona enter o ejecuta cmd y navega hasta la carpeta del proyecto.

3. **Verificar la instalación de Python**:
   Asegúrate de que tienes Python 3.11 o superior instalado. Puedes verificar la versión de Python con el siguiente comando:
   ```bash
   python --version
   ```
   Si tienes varias versiones de Python, puede ser necesario usar `python3` en lugar de `python`.

4. **Ejecutar el script**:
   Para ejecutar la aplicación, solo necesitas correr el archivo principal del proyecto. En la terminal, ejecuta el siguiente comando:
   ```bash
   python generador.py
   ```
   O si tu sistema utiliza `python3`, usa:
   ```bash
   python3 generador.py
   ```

## Uso

1. Al ejecutar el programa, se te pedirá que ingreses la longitud deseada para la contraseña (debe ser al menos 8 caracteres).
2. Luego, el programa te preguntará si deseas incluir mayúsculas, minúsculas, números y símbolos especiales. Puedes responder con `si` o `s` para sí o `no` o `n` para no.
3. Si todas las entradas son válidas, el programa generará una contraseña aleatoria y segura según tus preferencias.

### Ejemplo de ejecución

```bash
Generador de Contraseñas Seguras
Introduce la longitud de la contraseña (mínimo 8 caracteres): 12
¿Incluir mayúsculas? (si/no): si
¿Incluir minúsculas? (si/no): si
¿Incluir números? (si/no): si
¿Incluir símbolos especiales? (si/no): si

Contraseña generada: A1b@C3dE4fG!
```

