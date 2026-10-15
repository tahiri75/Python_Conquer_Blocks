"""'NUMERO FAVORITO
Escribe un programa que solicite al usuario su número favorito. Utiliza
json.dump() para almacenar este número en un archivo. Escribe un
programa separado que lea este valor e imprima el mensaje: "Sé cuál es tu
número favorito… Es ____.” Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites). Si el número ya está
almacenado, muestra el número favorito al usuario. Si no lo está, solicita al
usuario su número favorito y guárdalo en un archivo. Ejecuta el programa al
menos dos veces para asegurarte de que funciona correctamente."""

import json


# funcion para crear el fichero
def create_json_file(filename, numero):
    with open(filename, "w") as objFile:
        json.dump(numero, objFile)


# funcion para leer el fichero
def read_json_file(filename):
    # capturar excetion si no existe el fichero
    try:
        with open(filename) as objFile:
            return json.load(objFile)
    except FileNotFoundError:
        # si no existe devolver None
        return None


filename = "numerofavorito.json"

# leer el número
numero_guardado = read_json_file(filename)
if numero_guardado == None:
    # pedir el número
    numero_favorito = input("Teclea tu número favorito: ")
    # guardar el número
    create_json_file(filename, numero_favorito)
    # leer el número guardado
    numero_guardado = read_json_file(filename)
    # imprimir el número
    print(f"Sé cual es tu número favorito, es: {numero_guardado}")
else:
    # imprimir el número
    print(f"Sé cual es tu número favorito, es: {numero_guardado}")
