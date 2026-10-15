# generar contraseña
def generar_contrasena(
    longitud=12,
    incluir_mayusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_especiales=True,
):
    import random
    import string

    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += "!@#$%^&*()-+"  # string.punctuation

    if not caracteres:
        raise ValueError(
            "Debe seleccionar al menos un tipo de carácter para generar la contraseña."
        )

    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    return contrasena
