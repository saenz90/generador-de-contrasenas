import random
import string

def generar_contraseña():
    # Definir los caracteres que se pueden utilizar en la contraseña y almacenarlos en vectores
    mayusculas = list(string.ascii_uppercase)  # A-Z
    minusculas = list(string.ascii_lowercase)  # a-z
    numeros = list(string.digits)  # 0-9
    simbolos = list('~¡@#$%^*()_-+={}[]|:;\",.¿')  # símbolos especiales

    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 8 caracteres): "))
            if longitud < 8:
                print("La longitud mínima es de 8 caracteres. Intenta de nuevo.")
            else:
                break  # Si la longitud es válida, salir del bucle
        except ValueError:
            print("Por favor, ingresa un número válido para la longitud.")

    while True:
        incluir_mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower()
        if incluir_mayusculas not in ['si', 'no', 's', 'n']:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
        else:
            incluir_mayusculas = incluir_mayusculas in ['si', 's']
            break
    
    while True:
        incluir_minusculas = input("¿Incluir minúsculas? (si/no): ").lower()
        if incluir_minusculas not in ['si', 'no', 's', 'n']:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
        else:
            incluir_minusculas = incluir_minusculas in ['si', 's']
            break

    while True:
        incluir_numeros = input("¿Incluir números? (si/no): ").lower()
        if incluir_numeros not in ['si', 'no', 's', 'n']:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
        else:
            incluir_numeros = incluir_numeros in ['si', 's']
            break

    while True:
        incluir_simbolos = input("¿Incluir símbolos especiales? (si/no): ").lower()
        if incluir_simbolos not in ['si', 'no', 's', 'n']:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
        else:
            incluir_simbolos = incluir_simbolos in ['si', 's']
            break

    # Crear un conjunto de caracteres disponibles basados en las preferencias
    caracteres_disponibles = []

    if incluir_mayusculas:
        caracteres_disponibles.extend(mayusculas)
    if incluir_minusculas:
        caracteres_disponibles.extend(minusculas)
    if incluir_numeros:
        caracteres_disponibles.extend(numeros)
    if incluir_simbolos:
        caracteres_disponibles.extend(simbolos)

    # Si no se selecciona ningún tipo de carácter, mostrar un mensaje de error
    if not caracteres_disponibles:
        print("Debe seleccionar al menos una categoría (mayúsculas, minúsculas, números o símbolos).")
        return None

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    
    return contraseña

def main():
    print("Generador de Contraseñas Seguras")
    contraseña = generar_contraseña()
    
    if contraseña:
        print(f"\nContraseña generada: {contraseña}")

if __name__ == "__main__":
    main()
