lista_numeros = []

# --- pedir al usuario que introduzca 5 números ---
for i in range(0, 4):
    numero = int(input("Teclee el número " + str(i + 1) + " : "))
    lista_numeros.append(numero)

print("Los números introducidos son:", lista_numeros)

# --- imprimir el mayor número de la lista ---

print("El mayor número de la lista es:", max(lista_numeros))

# --- imprimir la lista ordenada ---

lista_numeros.sort()
print("La lista ordenada es:", lista_numeros)
