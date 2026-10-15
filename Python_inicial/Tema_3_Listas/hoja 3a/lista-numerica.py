# lista_numero = [1,2,3,4,5,6,7,8,9,10]

lista_numero_for = []

lista_numero_par_inv = []

# --- lista de números del 1 al 10 con for ---
for i in range(1, 11):
    lista_numero_for.append(i)

# --- lista de números del 1 al 10 con range ---
lista_numero_range = list(range(1, 11))

# --- Imprimir listas
print("lista_numero_for: ", lista_numero_for)

print("lista_numero_range: ", lista_numero_range)

# --- lista de números del 1 al 10 en orden inverso ---
print(lista_numero_for[::-1])

# --- numeros pares en orden inverso ---
for i in range(9, -1, -1):
    if lista_numero_for[i] % 2 == 0:
        lista_numero_par_inv.append(lista_numero_for[i])
print("lista_numero_par_inv :", lista_numero_par_inv)

# --- cuadrado de cada numero ---
for i in range(0, 10):
    print(lista_numero_for[i] ** 2)

# --- comprimidos ---
print("pares comprimido")
print(list(range(10, 1, -2)))
numeros_pares_comp_inv = [numero for numero in lista_numero_for if numero % 2 == 0][
    ::-1
]
print("numeros_pares_comp-inv: ", numeros_pares_comp_inv)

print("cuadrados comprimido")
print([numero**2 for numero in range(1, len(lista_numero_for) + 1)])
print([numero**2 for numero in lista_numero_for])


# --- numero mayor y menor
print("numero mayor: ", max(lista_numero_for))
print("numero menor: ", min(lista_numero_for))

# --- suma con bucle ---
suma = 0
for num in lista_numero_for:
    suma += num
print("la suma con for de los numeros es: ", suma)

# --- suma sin bucle ---
suma_comp = sum(lista_numero_for)
print("la suma comprimida de los numeros es: ", suma_comp)

# --- encuentra el índice correspondiente al 8
indice_8_original = lista_numero_for.index(8)
print("el 8 en la lista original está en el index: ", indice_8_original)

indice_8_invertida = lista_numero_par_inv.index(8)
print("el 8 en la lista de pares invertida está en el index: ", indice_8_invertida)
