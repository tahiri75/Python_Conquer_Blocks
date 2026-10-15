"""'CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una
participación en clase. Quieres calcular la nota final de cada estudiante, donde los
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas,
donde n es el número de estudiantes. Cada columna representa una de las calificaciones
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola
columna."""

# Importar NumPy
import numpy as np

# Solicitar al usuario el número de estudiantes
num_estudiantes = int(input("Introduce el número de estudiantes: "))

# Crear un array para almacenar las calificaciones de los estudiantes
calificaciones = np.zeros((num_estudiantes, 4))

# Solicitar al usuario las calificaciones de cada estudiante
for i in range(num_estudiantes):
    print(f"Introduce las calificaciones del estudiante {i+1}:")
    for j in range(4):
        calificaciones[i, j] = float(input(f"Calificación {j+1}: "))

# Definir los pesos de cada tipo de calificación
pesos = np.array([0.3, 0.3, 0.3, 0.1])
print(f"Pesos de las calificaciones: {pesos}")

# Calcular la nota final de cada estudiante
notas_finales = np.dot(calificaciones, pesos)

# Mostrar las notas finales
print("Notas finales de los estudiantes:")
for i in range(num_estudiantes):
    print(f"Estudiante {i+1}: {notas_finales[i]:.2f}")

# Calcular las notas finales usando un bucle for
notas_finales_for = np.zeros(num_estudiantes)

for i in range(num_estudiantes):
    notas_finales_temp = np.multiply(calificaciones[i, :], pesos)
    print(f"Notas finales del estudiante {i+1} con pesos: {notas_finales_temp}")
    notas_finales_for[i] = np.sum(notas_finales_temp)
    # Mostrar la nota final del estudiante con 2 lugares decimales
    print(f"Nota final del estudiante {i+1}: {notas_finales_for[i]:.2f}")
