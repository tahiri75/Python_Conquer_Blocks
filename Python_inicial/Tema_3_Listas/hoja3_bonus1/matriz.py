"""'
Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo:
M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
numero de objetos)
"""

# --- crear listas de ejemplo ---
list_m1 = [[2, 5, 9], [6, 1, 8], [7, 5, 4]]
list_m2 = [[4, 2, 3], [4, 5], [6, 8, 2]]

fila_maximos = []
columna_maximos = []
suma_filas = []
suma_columnas = []

# --- comprobar si es matriz ---
matriz = list_m1  # list_m2
len_fila1 = len(matriz[0])
suma_filas.append(sum(matriz[0]))
for i in range(1, len(matriz)):
    suma_filas.append(sum(matriz[i]))
    if len_fila1 != len(matriz[i]):
        print("La lista no es una matriz")
        break
else:
    # --- es una matriz ------------
    # --- buscar fila de máximos ---
    index_max = suma_filas.index(max(suma_filas))
    fila_maximos = matriz[index_max]
    # --- buscar columna de máximos ---
    suma_columnas = []
    for j in range(0, len_fila1):  # como es matriz todas las filas miden lo mismo
        suma_columna = 0
        for k in range(0, len(matriz)):
            # print(matriz[k][j])
            suma_columna += matriz[k][j]
        # print(suma_columna)
        suma_columnas.append(suma_columna)
    # print(suma_columnas)
    index_max_col = suma_columnas.index(max(suma_columnas))
    # print(index_max_col)
    for fila in matriz:
        columna_maximos.append(fila[index_max_col])


print("Lista original: ", matriz)
print("Fila máximos: ", fila_maximos)
print("Columna máximos: ", columna_maximos)
