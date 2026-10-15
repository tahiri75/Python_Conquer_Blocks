"""'
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.
Supón ahora que tu input es un string como este:
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string.
"""

# --- separar cada estudiante por "\n" ---
cadena_completa = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\nMaria Garcia 12316487A 43527 2 7.1 8.6 5.4\nJuan Perez 647829236A 43527 2 8.1 8.5 8.4"
list_estudiantes = cadena_completa.split("\n")
print(list_estudiantes)

# --- separar datos de cada estudiante por " " ---
list_datos = []
for estudiante in list_estudiantes:
    list_datos.append(estudiante.split(" "))
print(list_datos)

# --- Imprimir DNI y nota media de cada estudiante ---
for estudiante in list_datos:
    print(
        f"DNI: {estudiante[2]}  nota media: {round((float(estudiante[5]) + float(estudiante[6]) + float(estudiante[7])) / 3, 2)}"
    )
