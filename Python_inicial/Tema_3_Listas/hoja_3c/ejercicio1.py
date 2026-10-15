"""
BASE DE DATOS DE UN COLEGIO:
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase.

"""

listaEstudiantes = ["Nathalie", "Daniel", "Andy", "mama", "papa"]
"""'
database = [
    ["Nathalie", [6.4, 7, 9.1], 0],
    ["Daniel", [6, 7, 9], 0],
    ["Andy", [9, 9, 8.6], 0],
    ["mama", [8, 9, 6.9], 0],
    ["papa", [9, 9, 8], 0],
]

print(database)
"""

# --- Pedir las notas de los estudiantes ---

database = []
for estudiante in listaEstudiantes:
    # pedir notas de cada estudiante
    notas = []
    print(f"Ingrese las notas de {estudiante}")
    deberes = float(input("Notas de deberes: "))
    notas.append(deberes)
    examenes = float(input("Notas de examenes: "))
    notas.append(examenes)
    proyectos = float(input("Notas de proyectos: "))
    notas.append(proyectos)
    # añadir estudiante y lista de notas
    database.append([estudiante, notas])

print(database)

# --- interrumpir ejecusión para probar
# quit()

# --- Total de notas medias para calcular media de la clase ---
totalClase = 0

# --- calcular nota media de cada estudiante ---
for data in database:
    nombre = data[0]
    notas = data[1]
    # print(nombre)
    # print(notas)

    # -- calcular promedio de cada estudiante
    """'
    suma_notas = 0
    for nota in notas:
        suma_notas += nota
    media = suma_notas / len(notas)
    """
    media = sum(notas) / len(notas)
    # --- guardar promedio redondear a 2 decimales
    # data[2] = round(media, 2)
    # --- sumar nota media a total de la clase
    totalClase += round(media, 2)

    # print(nombre, notas, round(media, 2))
    print(f"La media de {nombre} es {media:.2f}")

# --- calcular nota media de la clase ---
mediaClase = totalClase / len(database)

# print("Base de datos con notas medias de cada estudiante:")
# print(database)
print(f"Media de la clase: {round(mediaClase, 2)}")

print("Media de la clase: {:.2f}".format(mediaClase))
