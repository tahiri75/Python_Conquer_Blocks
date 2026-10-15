"""'Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”"""


def validar_formulario(name, email, phone):
    # verificar nombre
    if len(name) < 3:
        print("Nombre inválido")
        return False
    # verificar teléfono solo dígitos y longitud = 9
    elif not phone.isdigit() or len(phone) != 9:
        print("Teléfono inválido")
        return False
    # verificar email
    elif ("@" not in email) or ("." not in email):
        print("Email inválido")
        return False

    return True


nombre = input("Introduce tu nombre: ")
email = input("Introduce tu correo electrónico: ")
telefono = input("Introduce tu número de teléfono: ")
valido = validar_formulario(nombre, email, telefono)
# valido = validar_formulario("Pedro", "pedro@gmail.com", "1000456789")
if valido:
    print("Formulario válido")
else:
    print("Formulario inválido")
