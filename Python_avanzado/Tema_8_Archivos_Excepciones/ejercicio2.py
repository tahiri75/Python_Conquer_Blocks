"""'MANIPULACION DE ARCHIVOS Y FILENOTFOUNDERROR
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de
gatos en el primer archivo y tres nombres de perros en el segundo archivo.
Escribe un programa que intente leer estos archivos e imprima el contenido
de cada archivo en la pantalla. Envuelve tu código en un bloque try-except
para capturar el error de FileNotFoundError, e imprime un mensaje amigable
si falta algún archivo. Mueve uno de los archivos a una ubicación diferente
en tu sistema y asegúrate de que el código en el bloque except se ejecute
correctamente. Modifica tu bloque except para que falle en silencio si falta
alguno de los archivos."""


# funcion para crear los ficheros
def create_file(filename, animal="perro"):
    with open(filename, "w") as objFile:
        for i in range(0, 3):
            name = input(f"Tecle el nombre del {animal} {i+1}: ")
            objFile.write(name + "\n")


# funcion para leer los ficheros
def read_file(filename, animal="perro"):
    # capturar excetion si no existe el fichero
    try:
        with open(filename) as objFile:
            print(f"Nombres de los {animal}s")
            print(objFile.read())
    except FileNotFoundError:
        # si no existe no hacer nada
        pass


# crear los ficheros
create_file("cats.txt", "gato")
# comentar creación del segundo fichero para provocar el error al leerlo
# create_file("dogs.txt")

# Leer e imprimir el contenido de los ficheros
read_file("cats.txt", "gato")
read_file("dogs.txt")
