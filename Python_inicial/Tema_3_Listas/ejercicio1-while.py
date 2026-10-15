lista_numeros = []
# --- con while ---
while len(lista_numeros) < 4:
    numero = input("Teclee el número " + str(len(lista_numeros) + 1) + " : ")
    if numero.isnumeric() == False:
        print("No ha introducido un número válido, por favor vuelva a intentarlo.")
        continue
    numero = int(numero)
    lista_numeros.append(numero)

# --- imprimir el mayor número de la lista ---
print("El mayor número de la lista es:", max(lista_numeros))

# --- imprimir el menor número de la lista ---
print("El menor número de la lista es:", min(lista_numeros))

# --- imprimir la lista ordenada ---
lista_numeros.sort()
print("La lista ordenada es:", lista_numeros)

# --- imprimir la lista al revés ---
lista_numeros.reverse()
print("La lista al revés es:", lista_numeros)
