"""'
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
venta.
"""

# --- Lista con las ventas del mes ---

ventas = [
    120,
    80,
    140,
    200,
    75,
    100,
    180,
    220,
    160,
    110,
    90,
    120,
    170,
    190,
    250,
    300,
    95,
    110,
    140,
    180,
    200,
    160,
    120,
    80,
    170,
    150,
    210,
    190,
    230,
    250,
]

# --- Lista días de la semana

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

ventas_X_dia_semana = [0, 0, 0, 0, 0, 0, 0]

# --- sumar dias semana ---
dia_venta = 0

for i in range(0, len(ventas)):
    ventas_X_dia_semana[dia_venta] = ventas_X_dia_semana[dia_venta] + ventas[i]
    dia_venta += 1
    if dia_venta == 7:
        dia_venta = 0

# --- imprimir días de la semana ---
i = 0
for dia in dias_semana:
    print(f"{dia}: {ventas_X_dia_semana[i]} ventas")
    i += 1
