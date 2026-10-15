import numpy as np

# --- 9. Crea un arrays lleno de 1s con una longitud dada por el usuario ---
longitud = int(input("Introduce la longitud del array: "))
array1 = np.ones(longitud)
print(f"Array lleno de 1s con longitud {longitud}: {array1}")
# --- 10. Cambia la forma del array para que tenga una estructura de tipo (filas, columnas) ---
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))
if filas * columnas == longitud:
    nuevo_array = np.reshape(array1, (filas, columnas))
    print(f"Array con forma ({filas}, {columnas}): {nuevo_array}")
else:
    print(
        "Error: La longitud del array no coincide con el producto de filas y columnas."
    )
# --- 11. Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas) ---
if filas * columnas == longitud:
    nuevo_array = np.reshape(array1, (filas, columnas))
    if filas != columnas:
        print(
            "Error: No se puede crear una matriz identidad con forma no cuadrada. Se creará una matriz identidad cuadrada con tamaño igual al número de filas."
        )
    matriz_identidad = np.eye(filas)
    print(f"Matriz identidad con forma ({filas}, {filas}): {matriz_identidad}")
    # --- 12. Concatena ambas estructuras horizontalmente y verticalmente ---
    # Horizontalmente
    concatenado_horizontal = np.concatenate((nuevo_array, matriz_identidad), axis=1)
    print(f"Concatenado horizontalmente: {concatenado_horizontal}")
    # Verticalmente
    if filas != columnas:
        print(
            "Error: No se puede concatenar verticalmente un array no cuadrado con una matriz identidad cuadrada. Se realizará la concatenación vertical solo si el número de filas es igual al número de columnas."
        )
    else:
        concatenado_vertical = np.concatenate((nuevo_array, matriz_identidad), axis=0)
        print(f"Concatenado verticalmente: {concatenado_vertical}")
