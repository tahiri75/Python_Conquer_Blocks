"""'FACTORIAL
Implementa una función recursiva llamada factorial que calcule el factorial de
un número entero positivo. El factorial de un número n se define como el
producto de todos los números enteros positivos desde 1 hasta n.
(El factorial de 0 y de 1 es igual a 1)"""


def calcular_factorial(number):
    """'calcular factorial de number"""
    # INPUT:
    # - number: int
    # OUTPUT:
    # - result: int //factorial de number
    if number == 0 or number == 1:
        return 1
    else:
        return number * calcular_factorial(number - 1)


number = int(input("Teclee el número para calcular su factorial: "))
print("Factorial: ", calcular_factorial(number))
