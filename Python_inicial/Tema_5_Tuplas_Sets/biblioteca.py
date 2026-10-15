"""'LA BIBLIOTECA:
Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor."""

lista_libros = [
    ("El aleph", "Jorge Luis Borges"),
    ("Cien años de soledad", "Gabriel García Márquez"),
    ("La ciudad y los perros", "Mario Vargas Llosa"),
]

nueva_lista = [
    (titulo, autor.split()[-2] + " " + autor.split()[-1])
    for titulo, autor in lista_libros
]

print(nueva_lista)
