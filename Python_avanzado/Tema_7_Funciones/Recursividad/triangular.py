"""'NUMERO TRIANGULAR
Crea una función recursiva llamada numero_triangular que calcule el n-ésimo
número triangular. Un número triangular se obtiene al sumar todos los
números naturales desde 1 hasta n."""


def calcular_triangular(number):
    """'calcular triangular de number"""
    # INPUT:
    # - number: int
    # OUTPUT:
    # - result: int //triangular de number
    if number == 1:
        return 1
    else:
        return number + calcular_triangular(number - 1)


number = int(input("Teclee el número para calcular su número triangular: "))
print("Tirangular: ", calcular_triangular(number))
