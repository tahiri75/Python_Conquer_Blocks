"""'Imagina que estás trabajando en un sistema de gestión de costos de envío para
una empresa de logística. El sistema debe calcular el costo de envío para
diferentes destinos, distancias y pesos de paquetes. Implementa una función
llamada calcular_costo_envio que tome como entrada un destino, una distancia
en kilómetros y un peso en kilogramos, y devuelva el costo total del envío.
Requerimientos:
1. El costo base de envío es de $5.0.
2. El costo por kilómetro de distancia es de $0.1.
3. El costo por kilogramo de peso es de $0.2.
Implementa la función de manera eficiente utilizando memoización para evitar
recalcular el costo para los mismos destinos, distancias y pesos."""

import functools
import time


@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia, peso):
    costo_base = 5
    costo_kilometro = distancia * 0.1
    costo_peso = peso * 0.2
    return costo_base + costo_kilometro + costo_peso


destino_1 = "Ciudad A"
distancia_1 = 150
peso_1 = 2.5

inicio = time.time()
costo_1 = calcular_costo_envio(destino_1, distancia_1, peso_1)
final = time.time()

inicio_memo = time.time()
costo_1_con_memo = calcular_costo_envio(destino_1, distancia_1, peso_1)
final_memo = time.time()

print("Costo 1 sin memo: ", costo_1, " tiempo: ", final - inicio)
print("Costo 1 con memo: ", costo_1_con_memo, " tiempo: ", final_memo - inicio_memo)
