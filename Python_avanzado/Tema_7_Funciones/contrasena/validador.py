# Validar contraseña
def validar_contrasena(contrasena):
    # validar longitud
    if len(contrasena) < 8:
        print("Longitud inválida")
        return False
    # validar si contrasena contiene algún dígito del 0 al 9
    elif not any(caracter.isdigit() for caracter in contrasena):
        print("La contraseña debe contener dígitos")
        return False
    # validar si contiene minusculas
    elif not any(caracter.islower() for caracter in contrasena):
        print("La contraseña debe contener letras minúsculas")
        return False
    # validar si contiene mayusculas
    elif not any(caracter.isupper() for caracter in contrasena):
        print("La contraseña debe contener letras mayúsculas")
        return False
    # validar si contiene caracteres especiales
    elif not any(caracter in "!@#$%^&*()-+" for caracter in contrasena):
        print("La contraseña debe contener caracteres especiales")
        return False
    print("Contraseña válida")
    return True
