"""'PALABRAS COMUNES
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count())."""

mi_texto = """PALABRAS COMUNES
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count())."""


# funcion para crear el fichero
def create_file(filename, texto):
    with open(filename, "w") as objFile:
        objFile.write(texto)


# funcion para leer el fichero
def read_file(filename):
    # capturar excetion si no existe el fichero
    try:
        with open(filename) as objFile:
            return objFile.read()
    except FileNotFoundError:
        print("No existe el fichero")
        return None


filename = "text_file.txt"

# crear fichero
create_file(filename, mi_texto)

# pedir palabra que desa buscar
palabra = input("Teclee la palabra que desea buscar en el fichero: ")

# leer fichero y devolver contenido
contenido = read_file(filename)

if contenido:
    print(
        f"La palabra {palabra} aparece {contenido.lower().count(palabra)} veces en el fichero"
    )
