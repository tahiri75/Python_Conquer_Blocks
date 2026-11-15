"""'COCHE
Crea una clase "Coche" con atributos como marca, modelo y año.
Implementa un método para encender el coche y otro para apagarlo (puedes
simular el encendido y apagado con una variable booleana)."""


# definición de la clase
class coche:
    def __init__(self, marca, modelo, anno):
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.encendido = False

    def encender(self):
        print("Encender...")
        self.encendido = True

    def apagar(self):
        print("Apagar...")
        self.encendido = False

    def show_information(self):
        if self.encendido == True:
            on = "encendido"
        else:
            on = "apagado"
        print(
            f"El coche es de la marca {self.marca}, modelo {self.modelo}, año {self.anno} y está {on}"
        )


# pedir datos del coche
print("Teclee los datos del coche: ")
marca = input("Marca: ")
modelo = input("Modelo: ")
anno = input("Año: ")

# crear objeto
objeto_coche = coche(marca, modelo, anno)

objeto_coche.encender()
objeto_coche.show_information()

objeto_coche.apagar()
objeto_coche.show_information()
