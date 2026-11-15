"""'RECTÁNGULO
Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa
un método para calcular el área y el perímetro del rectángulo."""


# Definición de la clase
class rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    # Métodos de la clase
    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)


continuar = True
while continuar:
    # Pedir los datos
    try:
        longitud = float(input("Teclee la longitud del rectángulo: "))
        ancho = float(input("Teclee el ancho del rectángulo: "))

        # Crear el objeto
        objeto_rectangulo = rectangulo(longitud, ancho)

        # Imprimir los datos
        print(f"El área del rectángulo es: {objeto_rectangulo.calcular_area()}")
        print(
            f"El perímetro del rectángulo es: {objeto_rectangulo.calcular_perimetro()}"
        )

    # capturar errores de tipo de dato
    except ValueError:
        print(
            "Por favor, ingrese valores numéricos válidos para la longitud y el ancho del rectángulo."
        )

    continuar = input("Desea continuar con otros valores (s/n): ") == "s"
