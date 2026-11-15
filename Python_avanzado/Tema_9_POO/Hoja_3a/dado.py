"""'DADO
Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras.
Implementa un método para lanzar el dado y mostrar el resultado (quizás te
convenga usar el modulo random)."""

# definición de la clase
import random


class dado:
    def __init__(self):
        self.caras = 6

    def lanzar_dado(self):
        print(random.randint(1, self.caras))


continuar = True
while continuar:
    objecto_dado = dado()
    objecto_dado.lanzar_dado()

    continuar = input("Desea lanzar otra vez (s/n): ") == "s"
