"""'POTENCIA
Implementa una función recursiva llamada potencia que calcule el resultado
de elevar un número a una potencia dada. Puedes asumir que tanto el
número como la potencia son enteros no negativos."""


def calcular_potencia(numero, potencia):
    """'calcular potencia de numero"""
    # INPUT:
    # - numero: int
    # - potencia: int
    # OUTPUT:
    # - result: int //potencia de numero
    if numero == 0:
        return 0
    elif potencia == 0:
        return 1
    else:
        return numero * calcular_potencia(numero, potencia - 1)


numero = int(input("Teclee el número para calcular su potencia: "))
potencia = int(input("Teclee la potencia: "))
print("Número ^ potencia: ", calcular_potencia(numero, potencia))
