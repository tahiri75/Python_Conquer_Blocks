lista_frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]

# --- imprimir la lista de frutas ---
print("La lista de frutas es:", lista_frutas)

# --- imprimir la longitud de la lista de frutas  ---
print("La longitud de la lista de frutas es:", len(lista_frutas))

# --- imprimir un elemento de la lista de frutas ---
print("El tercer elemento de la lista de frutas es:", lista_frutas[2])

# --- cambiar un elemento de la lista de frutas ---
lista_frutas[1] = "mora"
print("La lista de frutas después de cambiar el segundo elemento es:", lista_frutas)

# --- añadir un elemento a la lista de frutas ---
lista_frutas.append("mango")
print("La lista de frutas después de añadir un elemento es:", lista_frutas)

lista_frutas.insert(0, "uva")
print("La lista de frutas después de añadir un elemento al principio es:", lista_frutas)

# --- imprimir la longitud de la lista de frutas  ---
print("La longitud de la lista de frutas ahora es:", len(lista_frutas))

# --- imprimir la lista de frutas ---
for i in range(len(lista_frutas)):
    print("Fruta " + str(i + 1) + ":", lista_frutas[i])

# --- eliminar el último elemento de la lista de frutas ---
ultima_fruta = lista_frutas.pop()
print("La última fruta de la lista es:", ultima_fruta)
print("La lista de frutas después de eliminar la última es:", lista_frutas)

# --- imprimir la lista de frutas ---
for i in range(len(lista_frutas)):
    if len(lista_frutas[i]) > 5:
        print(
            "Fruta " + str(i + 1) + ":",
            lista_frutas[i],
            ", Longitud: ",
            len(lista_frutas[i]),
        )

lista_frutas.remove("cereza")
print("La lista de frutas después de eliminar la cereza es:", lista_frutas)

lista_frutas.sort()
print("La lista de frutas ordenada es:", lista_frutas)

lista_frutas.reverse()
print("La lista de frutas al revés es:", lista_frutas)

lista_frutas.clear()
print("La lista de frutas después de vaciarla es:", lista_frutas)
