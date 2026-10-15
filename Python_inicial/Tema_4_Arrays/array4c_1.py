"""'DATOS CINEMATOGRÁFICOS
Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película."""

import numpy as np

peliculas = np.array(
    [
        ["peli 1", "comedia", 120, 1990, 8.5],
        ["peli 2", "accion", 110, 2005, 7.8],
        ["peli 3", "drama", 95, 2010, 6.9],
        ["peli 4", "comedia", 100, 1985, 7.5],
        ["peli 5", "accion", 130, 2015, 8.1],
        ["peli 6", "drama", 115, 2000, 6.7],
        ["peli 7", "comedia", 90, 1995, 8.2],
        ["peli 8", "accion", 105, 2010, 7.4],
        ["peli 9", "drama", 125, 1980, 6.8],
        ["peli 10", "comedia", 95, 2000, 8.0],
    ]
)

# --- obtener los géneros únicos y su cantidad de apariciones ---
generos, conteo_generos = np.unique(peliculas[:, 1], return_counts=True)
print(generos)
print(conteo_generos)

# --- ordenar los géneros por popularidad ---
index_sort = np.argsort(conteo_generos)[::-1]
print(index_sort)
print("El género más popular es ", generos[index_sort[0]])

# --- obtener las décadas y la cantidad de películas por década ---
decadas = np.unique(peliculas[:, 3].astype(int) // 10 * 10)
cant_decadas = len(decadas)

peliculas_X_decadas = np.zeros(cant_decadas)

print(decadas)

for i in range(0, cant_decadas):
    # cant_peli = 0
    # for pelicula in peliculas:
    #     if (
    #         pelicula[3].astype(int) >= decadas[i]
    #         and pelicula[3].astype(int) < decadas[i] + 10
    #     ):
    #         cant_peli += 1
    cant_peli = np.count_nonzero(
        (peliculas[:, 3].astype(int) >= decadas[i])
        & (peliculas[:, 3].astype(int) < decadas[i] + 10)
    )
    peliculas_X_decadas[i] = cant_peli

print("---Cantidad de películas x décadas---")
for i in range(0, cant_decadas):
    print(
        f"Década: {decadas[i]} --- cantidad de peliculas: {peliculas_X_decadas[i].astype(int)}"
    )

# --- Duración promedio por género ---
cant_generos = len(generos)
duracion_genero = np.zeros(cant_generos)
duracion_genero_mean = np.zeros(cant_generos)
duraciones = peliculas[:, 2]
todos_generos = peliculas[:, 1]

for i in range(0, cant_generos):
    # --- con for ---
    genero_count = 0
    duracion_total = 0
    for pelicula in peliculas:
        if pelicula[1] == generos[i]:
            genero_count += 1
            duracion_total += int(pelicula[2])
    duracion_genero[i] = duracion_total / genero_count

    # --- con np.mean ---
    duracion_genero_mean[i] = np.mean(
        duraciones[todos_generos == generos[i]].astype(float)
    )

print("---Duración promedio por género---")
for i, genero in enumerate(generos):
    print(
        f"Género: {genero} --- Duración promedio: {duracion_genero[i]:.2f} --- con mean: {duracion_genero_mean[i]:.2f}"
    )
