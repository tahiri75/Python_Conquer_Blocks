"""'SUMA ELEMENTOS DE UNA LISTA
Crea una función recursiva llamada suma_lista que calcule la suma de todos
los elementos de una lista de enteros. Puedes asumir que la lista no está
vacía."""


def suma_lista(lista):
    """'suma elementos de la lista"""
    # INPUT:
    # - lista: list
    # OUTPUT:
    # - result: int //suma de los elementos de la lista
    if len(lista) == 0:
        return 0
    else:
        element = lista.pop(0)
        print(element)
        return element + suma_lista(lista)


element = "0"
lista = []
while element != "f":
    element = input("Teclee un número de la lista o f para terminar: ")
    if element.isnumeric():
        lista.append(int(element))
    else:
        element = "f"

# lista = [1, 7, 8, 5, 3, 10]

print(suma_lista(lista))
