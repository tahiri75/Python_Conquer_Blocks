# --- Pedir datos del estudiante ---
nombre = str(input("Teclee el nombre del estudiante: "))
edad = int(input("Teclee la edad: "))
nota = float(input("Teclee la nota media "))

# --- comprobar si cumple las condiciones
if edad >= 17 and edad <= 21 and nota > 8:
    print("El estudiante ", nombre, " puede optar por la beca")
elif edad < 17 or edad > 21:
    print(
        "El estudiante ",
        nombre,
        " puede no optar por la beca porque no cumple con la edad",
    )
elif nota < 8:
    print(
        "El estudiante ",
        nombre,
        " puede no optar por la beca porque no cumple con la nota mínima",
    )
