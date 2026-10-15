"""'Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos."""

red_social = [
    ("Juan", ["Maria", "Pedro", "Luis"]),
    ("Maria", ["Juan", "Pedro", "Juan"]),
    ("Pedro", ["Juan", "Maria"]),
    ("Luis", ["Juan"]),
]

tupla_amigos = tuple()

for i in range(0, len(red_social)):
    usuario, amigos = red_social[i]
    # print(f"Usuario: {usuario}, Amigos: {amigos}")
    amigos_unicos = list(set(amigos))  # Eliminar duplicados usando un conjunto (set)
    # print(amigos_unicos)
    red_social[i] = (
        usuario,
        amigos_unicos,
    )  # Crear una nueva tupla con el usuario y sus amigos únicos
    num_amigos = len(amigos_unicos)  # Contar el número de amigos únicos
    # print(f"{usuario} tiene {num_amigos} amigos únicos: {amigos_unicos}")
    tupla_amigos += (
        (usuario, amigos_unicos, num_amigos),
    )  # Agregar la tupla (usuario, num_amigos) a la tupla de amigos

# print(red_social)
print(tupla_amigos)
tupla_amigos_ordenada = sorted(tupla_amigos, key=lambda x: x[2], reverse=True)
print(tupla_amigos_ordenada)
usuario_mas_amigos = tupla_amigos_ordenada[0][0]
print(
    f"El usuario con más amigos es: {usuario_mas_amigos} con {tupla_amigos_ordenada[0][2]} amigos."
)
