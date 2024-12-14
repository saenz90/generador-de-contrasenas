# Generador de Contraseñas Seguras

Esta aplicación en Python genera contraseñas seguras basadas en las preferencias del usuario. Permite personalizar la contraseña en cuanto a longitud y tipo de caracteres (mayúsculas, minúsculas, números y símbolos especiales), asegurando así la creación de contraseñas robustas y difíciles de adivinar.

## Características

- **Personalización de contraseñas**: Puedes elegir si deseas incluir mayúsculas, minúsculas, números y símbolos especiales.
- **Longitud mínima de la contraseña**: La aplicación asegura que la longitud mínima de la contraseña sea de 8 caracteres.
- **Validación de entradas**: Se valida que el usuario ingrese respuestas correctas para las opciones de tipo de caracteres y la longitud de la contraseña. Si se introduce un valor no válido, el programa pide la entrada nuevamente.

## Requisitos

- Python 3.x o superior.
- No se requieren librerías externas, ya que la aplicación usa módulos estándar de Python como `random` y `string`.

## Instalación

### Pasos para descargar y ejecutar el código en tu máquina local:

1. **Clonar el repositorio**:
   Si tienes `git` instalado, abre tu terminal y clona este repositorio en tu máquina local utilizando el siguiente comando:
   ```bash
   git clone https://github.com/tu_usuario/generador-de-contraseñas-seguras.git
   ```
   Esto descargará una copia del repositorio en tu máquina.

   Si no tienes `git` instalado, puedes descargar el archivo ZIP del repositorio desde la página de GitHub y descomprimirlo en tu máquina.

2. **Acceder al directorio del proyecto**:
   Una vez descargado el repositorio, navega al directorio del proyecto con el siguiente comando:
   ```bash
   cd generador-de-contraseñas-seguras
   ```

3. **Verificar la instalación de Python**:
   Asegúrate de que tienes Python 3.x instalado. Puedes verificar la versión de Python con el siguiente comando:
   ```bash
   python --version
   ```
   Si tienes varias versiones de Python, puede ser necesario usar `python3` en lugar de `python`.

4. **Ejecutar el script**:
   Para ejecutar la aplicación, solo necesitas correr el archivo principal del proyecto. En la terminal, ejecuta el siguiente comando:
   ```bash
   python generador_de_contraseñas.py
   ```
   O si tu sistema utiliza `python3`, usa:
   ```bash
   python3 generador_de_contraseñas.py
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

