"""'EMPRESA DE ELECTRONICA
Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente."""

import numpy as np

# Crear un array con los datos
datos = np.array(
    [
        ["2022-01-01", "Componente 1", "Lote A", 80],
        ["2022-01-15", "Componente 1", "Lote B", 90],
        ["2022-02-01", "Componente 2", "Lote C", 85],
        ["2022-02-15", "Componente 2", "Lote D", 95],
        ["2022-03-01", "Componente 1", "Lote E", 75],
        ["2022-03-15", "Componente 2", "Lote F", 90],
    ]
)

tipos_componentes = np.unique(datos[:, 1])
cant_tipos = np.count_nonzero(tipos_componentes)
calidad_componentes = np.zeros(cant_tipos)

for i in range(0, cant_tipos):
    calidad_componentes[i] = np.mean(
        datos[datos[:, 1] == tipos_componentes[i], 3].astype(float)
    )

print("---Calidad promedio por tipo de componente---")
for i in range(0, cant_tipos):
    print(
        f"Tipo de componente: {tipos_componentes[i]} --- Calidad promedio: {calidad_componentes[i]:.2f}"
    )

index_sort = np.argsort(calidad_componentes, descending=True)
index_max = np.argmax(calidad_componentes)
print(index_sort)
print("El componente de mayor calidad es ", tipos_componentes[index_sort[0]])
print(index_max)
print("El componente de mayor calidad es ", tipos_componentes[index_max])

fechas = datos[:, 0]
print(fechas)

# --- extraer el mes ---
meses, counts = np.unique([int(fecha[5:7]) for fecha in fechas], return_counts=True)
print(meses)
cant_meses = np.count_nonzero(meses)
componentes_x_mes = np.zeros(cant_meses)

for i in range(0, cant_meses):
    for dato in datos:
        if int(dato[0][5:7]) == meses[i]:
            componentes_x_mes[i] += 1

print("---Componentes por mes---")
for i in range(0, cant_meses):
    print(f"Mes: {meses[i]} --- Cantidad de componentes: {int(componentes_x_mes[i])}")

print("---Componentes por mes sin for--")
for i in range(len(meses)):
    print(f"Mes: {meses[i]} --- Cantidad de componentes: {counts[i]}")
