contrasena = input("Teclee la contraseña: ")

if (
    ("*" in contrasena)
    and ("#" in contrasena)
    and (
        "a" in contrasena
        or "e" in contrasena
        or "i" in contrasena
        or "u" in contrasena
        or "o" in contrasena
    )
):
    print("Contraseña segura")
else:
    print("contraseña no segura")
