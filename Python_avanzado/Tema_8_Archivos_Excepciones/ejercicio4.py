"""'BUSCANDO EN PI
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt"""


# funcion para leer el fichero
def read_file(filename):
    # capturar excetion si no existe el fichero
    try:
        with open(filename) as objFile:
            return objFile.read()
    except FileNotFoundError:
        print("No existe el fichero")
        return None


# Leer fichero y devolver contenido
contenido = read_file("pi_10000.txt")

fecha = input("Tecle su fecha de nacimiento: ")

posicion = contenido.find(fecha)

if posicion == -1:
    print("Su fecha de nacimiento no aparece en los 1000 primeros dígitos de PI")
else:
    print(
        f"Su fecha de nacimiento aparece en los 1000 primeros dígitos de PI en la posición {posicion}"
    )
