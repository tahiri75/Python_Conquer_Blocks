"""'ANALISIS DE DATOS CLIMÁTICOS
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes."""

import numpy as np

# Datos de clima
clima = np.array(
    [
        [20, 70, 1009, 1],
        [21, 60, 1011, 1],
        [22, 40, 1010, 1],
        [18, 75, 1012, 2],
        [21, 60, 1008, 3],
        [22, 65, 1008, 3],
        [25, 60, 1010, 4],
        [27, 49, 1007, 5],
        [29, 50, 1007, 5],
        [28, 51, 1007, 5],
        [30, 45, 1005, 6],
        [10, 30, 1005, 6],
        [32, 40, 1002, 7],
        [33, 35, 1001, 8],
        [31, 45, 1003, 9],
        [30, 42, 1001, 9],
        [29, 42, 1002, 9],
        [35, 43, 1001, 9],
        [28, 50, 1006, 10],
        [25, 60, 1010, 11],
        [27, 59, 1012, 11],
        [24, 58, 1011, 11],
        [22, 70, 1011, 12],
    ]
)

clima_x_mes = np.zeros((12, 3))

for element in clima:
    mes = int(element[3]) - 1  # Restamos 1 para que enero sea el índice 0
    clima_x_mes[mes] += element[:3]

print("Suma de temperatura, humedad y presión atmosférica por mes:")
for i in range(12):
    print(
        f"Mes {i+1}: Temperatura: {clima_x_mes[i][0]}, Humedad: {clima_x_mes[i][1]}, Presión atmosférica: {clima_x_mes[i][2]}"
    )

for i in range(12):
    clima_x_mes[i] = clima_x_mes[i] / np.count_nonzero(clima[:, 3] == i + 1)

print("Promedio de temperatura, humedad y presión atmosférica por mes:")
for i in range(12):
    print(
        f"Mes {i+1}: Temperatura: {clima_x_mes[i][0]:.2f}, Humedad: {clima_x_mes[i][1]:.2f}, Presión atmosférica: {clima_x_mes[i][2]:.2f}"
    )

print("Promedio de temperatura, humedad y presión atmosférica otra solución:")
# otra solucion
meses = clima[:, 3].astype(int)
temperaturas = clima[:, 0]
temp_mes = np.zeros(12)

humedad = clima[:, 1]
hum_mes = np.zeros(12)

presion = clima[:, 2]
pres_mes = np.zeros(12)

for mes in range(12):
    temp_mes[mes] = np.mean(temperaturas[meses == mes + 1])
    hum_mes[mes] = np.mean(humedad[meses == mes + 1])
    pres_mes[mes] = np.mean(presion[meses == mes + 1])
    print(
        f"Mes {mes + 1}: Temperatura promedio: {temp_mes[mes]:.2f}, Humedad promedio: {hum_mes[mes]:.2f}, Presión atmosférica promedio: {pres_mes[mes]:.2f}"
    )
