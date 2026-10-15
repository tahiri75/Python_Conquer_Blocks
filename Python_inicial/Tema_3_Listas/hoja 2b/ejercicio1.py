lista_numeros = []

# --- pedir al usuario que introduzca 5 números ---
for i in range(0, 4):
    numero = int(input("Teclee el número " + str(i + 1) + " : "))
    lista_numeros.append(numero)

print("Los números introducidos son:", lista_numeros)

# --- imprimir el mayor número de la lista ---

print("El mayor número de la lista es:", max(lista_numeros))

#  --- imprimir el mayor número de la lista sin usar max ---

mayor = lista_numeros[0]
for i in range(1, len(lista_numeros)):
    if lista_numeros[i] > mayor:
        mayor = lista_numeros[i]

print("El mayor número de la lista sin usar max es:", mayor)
