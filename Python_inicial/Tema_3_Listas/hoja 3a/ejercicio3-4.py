# --- pedir frase ---
frase = input("Ingrese una frase: ")

# --- pedir letra ---
letra = input("Ingrese una letra: ")

# --- contar cuantas veces aparece la letra en la frase ---
contador = 0
for i in frase:
    if i == letra:
        contador += 1

# --- imprimir el resultado ---
print(
    "La letra '"
    + letra
    + "' aparece "
    + str(contador)
    + " veces en la frase '"
    + frase
    + "'"
)
