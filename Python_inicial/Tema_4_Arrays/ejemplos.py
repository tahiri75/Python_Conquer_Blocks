import numpy as np

# --- mascaras booleanas ---
otro_array = np.arange(10)
print(otro_array)
print(otro_array > 5)
print(otro_array[otro_array > 5])
list = otro_array[0:2]
print(list)

inventario = np.array(["Lavadora", "Freidora", "Refrigerador"])
precio = np.array([200, 100, 800])
print(inventario[precio > 100])

# --- compresion de listas ---
# crear lista de numeros de 0 a 9
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)
numeros_mayor_5 = [numero for numero in numeros if numero > 5]
print(numeros_mayor_5)
