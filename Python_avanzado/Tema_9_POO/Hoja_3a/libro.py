"""'LIBRO
Crea una clase "Libro" con atributos como título, autor y año de publicación.
Luego, crea varios objetos Libro y muestra su información."""


# Definición de la clase
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    # Métodos de la clase
    def show_information(self):
        print(
            f"El libro se llama {self.titulo}, su autor es {self.autor} y fue publicado en {self.año_publicacion}"
        )

    def show_short_information(self):
        print(
            f"Título: {self.titulo}, autor: {self.autor}, año de publicación: {self.año_publicacion}"
        )


lista_libros = []

continuar = True
while continuar:
    # Pedir los datos
    titulo = input("Teclee el título del libro: ")
    autor = input("Teclee el autor del libro: ")
    año_publicacion = input("Teclee el año de publicación: ")

    # Crear el objeto
    objeto_libro = Libro(titulo, autor, año_publicacion)

    # Imprimir los datos
    objeto_libro.show_information()

    # Guardar el objeto en la lista
    lista_libros.append(objeto_libro)

    # Preguntar si desea continuar
    respuesta = input("¿Desea ingresar otro libro? (s/n): ")
    if respuesta.lower() != "s":
        continuar = False

# imprimir la lista de libros ingresados
print("\nLista de libros ingresados:")
for libro in lista_libros:
    libro.show_short_information()
