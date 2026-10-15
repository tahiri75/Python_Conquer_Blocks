"""'Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])"""

base_datos = [
    {"Producto": "Leche", "Precio": 9},
    {"Producto": "Pan", "Precio": 2},
    {"Producto": "Huevos", "Precio": 5},
]


def agregar_venta(producto, precio):
    base_datos.append({"Producto": producto, "Precio": precio})


def mostrar_ventas():
    for venta in base_datos:
        print(f"Producto: {venta['Producto']}, Precio: {venta['Precio']}")
        print("-----")


# Pedir al usuario que ingrese un producto y su precio
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))

# Agregar la venta a la base de datos
agregar_venta(producto, precio)

# Mostrar las ventas de productos con sus respectivos precios
mostrar_ventas()
