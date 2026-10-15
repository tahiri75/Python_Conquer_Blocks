contrasena_correcta = "tahiri"
contrasena = input("Teclee la contraseña: ")

if contrasena.lower() == contrasena_correcta.lower():
    print("Contraseña correcta")
else:
    print("contraseña incorrecta")
    contrasena = input("Teclee la contraseña nuevamente: ")
    if contrasena.lower() == contrasena_correcta.lower():
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")
