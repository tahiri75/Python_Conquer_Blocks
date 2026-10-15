# --- pedir palabra ---
palabra = input("Ingrese una palabra: ")

# --- imprimir la palabra al reves ---
print("La palabra al revés es:", palabra[::-1])

# --- imprimir la palabra al revés mostrando las letras una a una ---
print("La palabra al revés es:")
for letra in palabra[::-1]:
    print(letra)

# --- otra forma de imprimir la palabra al revés mostrando las letras una a una ---
print("La palabra al revés es:")
for letra in range(len(palabra) - 1, -1, -1):
    print(palabra[letra])
