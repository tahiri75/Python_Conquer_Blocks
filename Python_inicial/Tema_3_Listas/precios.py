# --- lista de precios ---
lista_precios = [
    ("leche", 15),
    ("pan", 12),
    ("queso", 30),
    ("huevos", 20),
    ("jamon", 50),
]

lista_precios.sort(key=lambda x: x[1])
print("Lista de precios ordenada por precio:", lista_precios)

# --- imprimir el precio más caro ---
print("El precio más caro es:", max(lista_precios, key=lambda x: x[1]))

print("El precio más caro sin usar máx: ", lista_precios[-1])

precioTotal = 0
promedio = 0

for producto, precio in lista_precios:
    precioTotal += precio

promedio = precioTotal / len(lista_precios)
print("El precio promedio es:", promedio)
