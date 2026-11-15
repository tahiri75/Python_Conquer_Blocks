"""'Ejercicio 5:
Problema de Análisis de Datos de Ventas:
Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el
monto de la venta y la ubicación del comprador. Realiza un análisis avanzado
de estas ventas.
Python avanzado - ejercicios 4
1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda."""

from collections import defaultdict
from datetime import datetime

ventas = [
    {
        "nombre": "producto1",
        "fecha_venta": "2026-10-26",
        "monto": "600",
        "ubicacion_comprador": "España",
    },
    {
        "nombre": "producto2",
        "fecha_venta": "2026-09-26",
        "monto": "900",
        "ubicacion_comprador": "Francia",
    },
    {
        "nombre": "producto3",
        "fecha_venta": "2026-08-26",
        "monto": "800",
        "ubicacion_comprador": "Cuba",
    },
    {
        "nombre": "producto4",
        "fecha_venta": "2022-10-26",
        "monto": "400",
        "ubicacion_comprador": "USA",
    },
    {
        "nombre": "producto5",
        "fecha_venta": "2026-07-26",
        "monto": "200",
        "ubicacion_comprador": "España",
    },
]


def ventas_ultimo_trimestre(ventas):
    return [
        venta
        for venta in ventas
        if datetime.strptime(venta["fecha_venta"], "%Y-%m-%d").month in {10, 11, 12}
    ]


def ventas_superiores_a(ventas, minimo):
    return [venta for venta in ventas if float(venta["monto"]) > minimo]


def promedios_por_ubicacion(ventas):
    ventas_por_ubicacion = defaultdict(list)

    for venta in ventas:
        ventas_por_ubicacion[venta["ubicacion_comprador"]].append(float(venta["monto"]))

    return {
        ubicacion: sum(montos) / len(montos)
        for ubicacion, montos in ventas_por_ubicacion.items()
    }


def ordenar_por_promedio_descendente(promedios):
    return dict(sorted(promedios.items(), key=lambda item: item[1], reverse=True))


ventas_q4 = ventas_ultimo_trimestre(ventas)
ventas_altas = ventas_superiores_a(ventas_q4, 500)
promedios = promedios_por_ubicacion(ventas_altas)
resultado = ordenar_por_promedio_descendente(promedios)

print("Ventas del último trimestre:", ventas_q4)
print("Ventas con monto superior a 500:", ventas_altas)
print("Promedio por ubicación:", promedios)
print("Ubicaciones ordenadas por promedio descendente:", resultado)
