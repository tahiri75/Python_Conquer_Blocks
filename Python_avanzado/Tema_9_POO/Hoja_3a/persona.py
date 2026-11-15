"""'CLASE PERSONA
Define una clase Persona con atributos como nombre, edad y profesión.
Luego, crea varios objetos de esta clase y muestra su información."""


# Definición de la clase
class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def show_information(self):
        print(
            f"La persona se llama {self.nombre}, su edad es {self.edad} y su profesion es {self.profesion}"
        )


continuar = True
while continuar:
    # Pedir los datos
    nombre = input("Teclee el nombre de la persona: ")
    edad = input("Teclee la edad: ")
    profesion = input("Teclee la profesion: ")

    # Crear el objeto
    objeto_persona = persona(nombre, edad, profesion)

    # Imprimir los datos
    objeto_persona.show_information()

    # preguntar si desea continuar
    continuar = input("Desea continuar con otra persona (s/n): ") == "s"
# fin del while para continuar con otra persona
