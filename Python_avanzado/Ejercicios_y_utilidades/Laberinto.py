"""'Problema de Resolución de Laberinto:
Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). Tu tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:
0 : Camino permitido.
1 : Pared, no se puede atravesar.
9 : Salida del laberinto.
2. Debes implementar la función resolver_laberinto que utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.
4. Puedes usar una lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0, -1) ), derecha ( (0, 1) )."""


def resolver_laberinto(
    laberinto, fila, columna, total_filas, total_columnas, camino=None
):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if camino is None:
        camino = []

    print(f"fila: {fila}")
    print(f"columna: {columna}")
    if fila >= total_filas or fila < 0 or columna >= total_columnas or columna < 0:
        print("return por fuera de laberinto")
        return None
    if (fila, columna) in camino:
        print("return porque ya pasé")
        return None
    if laberinto[fila][columna] == 1:
        print("return por pared")
        return None
    if laberinto[fila][columna] == 9:
        camino.append((fila, columna))
        print("return por fin")
        return camino
    if laberinto[fila][columna] == 0:
        camino.append((fila, columna))
        for mov in movimientos:
            result = resolver_laberinto(
                laberinto,
                fila + mov[0],
                columna + mov[1],
                total_filas,
                total_columnas,
                camino.copy(),
            )
            if result:
                return result
        return None


def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(fila)


def imprimir_solucion(laberinto, camino):
    for i in range(0, len(laberinto)):
        for j in range(0, len(laberinto[i])):
            if (i, j) in camino:
                print("*", end=" ")
            else:
                print(laberinto[i][j], end=" ")
        print()


laberinto = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 9],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
]

total_filas = len(laberinto)
total_columnas = len(laberinto[0])

print(f"total filas: {total_filas}")
print(f"total columnas: {total_columnas}")

imprimir_laberinto(laberinto)

camino = resolver_laberinto(laberinto, 0, 0, total_filas, total_columnas)

imprimir_laberinto(laberinto)
print(camino)
imprimir_solucion(laberinto, camino)
