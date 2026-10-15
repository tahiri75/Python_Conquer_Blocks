"""'DATOS CLIENTES:
Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
segunda base de datos contiene el nombre del cliente, la dirección y el historial de
pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre."""

base_datos1 = [
    ("Juan", "juan@example.com", "555-1234"),
    ("Maria", "maria@example.com", "555-5678"),
    ("Pedro", "pedro@example.com", "555-9012"),
]
base_datos2 = [
    ("Juan", "Calle 123", ["Libro1", "Libro2"]),
    ("Maria", "Calle 456", ["Libro3"]),
    ("Luis", "Calle 789", ["Libro4"]),
]

set1 = set(data[0] for data in base_datos1)
print(set1)

set2 = set(data[0] for data in base_datos2)
print(set2)

list_result = list(set1.intersection(set2))
print(list_result)

base_datos_result = []

for name in list_result:
    for data in base_datos1:
        if data[0] == name:
            add1 = data[1:]

    for data2 in base_datos2:
        if data2[0] == name:
            add2 = data2[1:]

    base_datos_result.append(tuple([name, add1 + add2]))

print(base_datos_result)

for result in base_datos_result:
    print(result)
