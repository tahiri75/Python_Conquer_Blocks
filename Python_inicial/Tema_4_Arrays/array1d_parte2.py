import numpy as np

# --- 1. Crea un array con 15 números enteros aleatorios entre 1 y 100 ---
array1 = np.random.randint(1, 101, 15)
print(f"Array con 15 números enteros aleatorios entre 1 y 100: {array1}")
# --- 2. Multiplica todos los elementos del array usando un bucle y después usando un
# --- método de numpy. Compara los resultados ---
# --- problema de memoria porque el número se va de la memoria reservada ---
producto_bucle = 1
for elemento in array1:
    producto_bucle = producto_bucle * elemento
producto_numpy = np.prod(array1)
print(f"Producto con bucle: {producto_bucle}")
print(f"Producto con numpy: {producto_numpy}")
# --- 3. Crea otro array con 15 números decimales aleatorios entre 0 y 1 ---
array2 = np.random.random(15)  # no hace falta poner 0 y 1
print(f"Array con 15 números decimales aleatorios entre 0 y 1: {array2}")
# --- 4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
# --- operador y después con una función de numpy
# --- (Pista: busca en google que función de numpy hace esto)
array_suma_operador = array1 + array2
array_suma_numpy = np.add(array1, array2)
print(f"Suma con operador: {array_suma_operador}")
print(f"Suma con numpy: {array_suma_numpy}")
# --- 5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
# --- (Pista: busca en google que función de numpy hace esto)
array_resta_operador = array1 - array2
array_resta_numpy = np.subtract(array1, array2)
print(f"Resta con operador: {array_resta_operador}")
print(f"Resta con numpy: {array_resta_numpy}")
# --- 6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
# --- después con una función de numpy
# --- (Pista: busca en google que función de numpy hace esto)
array_multiplicacion_operador = array1 * array2
array_multiplicacion_numpy = np.multiply(array1, array2)
print(f"Multiplicación con operador: {array_multiplicacion_operador}")
print(f"Multiplicación con numpy: {array_multiplicacion_numpy}")
# --- 7. Encuentra el valor más alto del primer array que has creado ---
valor_maximo = np.max(array1)
print(f"Valor más alto del primer array: {valor_maximo}")
# --- 8. Calcula la media (mean), la mediana (median) y la desviación estándar (standard
# --- deviation) de los arrays (Nota: No nos importa el significado matemático de estos
# --- valores, lo importante es que encuentres que función de numpy necesitas. Puedes
# --- hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
# --- haber más resultados).
media_array1 = np.mean(array1)
mediana_array1 = np.median(array1)
desviacion_array1 = np.std(array1)
media_array2 = np.mean(array2)
mediana_array2 = np.median(array2)
desviacion_array2 = np.std(array2)
print(f"Media del primer array: {media_array1}")
print(f"Mediana del primer array: {mediana_array1}")
print(f"Desviación estándar del primer array: {desviacion_array1}")
print(f"Media del segundo array: {media_array2}")
print(f"Mediana del segundo array: {mediana_array2}")
print(f"Desviación estándar del segundo array: {desviacion_array2}")
